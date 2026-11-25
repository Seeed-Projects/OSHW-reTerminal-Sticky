#!/usr/bin/env python3
"""Synchronize official reTerminal Sticky firmware releases and catalog docs.

Reads `firmwares/sticky-factory/firmware.json` from the upstream Playground
Registry repository, verifies manifest and binary SHA-256 checksums, optionally
publishes missing GitHub Releases in the target repository, and updates:
  - `firmware/factory/versions.json`
  - `firmware/README.md` (between catalog markers)
  - `firmware/README-ZH.md` (between catalog markers)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_SOURCE_REPO = "Seeed-Projects/reterminal-sticky-playground-registry"
DEFAULT_SOURCE_REF = "main"
DEFAULT_TARGET_REPO = "Seeed-Projects/OSHW-reTerminal-Sticky"
FIRMWARE_ENTRY_PATH = "firmwares/sticky-factory"
RELEASE_TAG_PREFIX = "firmware-official-v"
WEB_FLASHER_URL = "https://www.seeedstudio.com/sticky/playground/official-firmware/"
USER_AGENT = "seeed-oshw-firmware-sync/1.0"
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
HTTP_RETRIES = 3

CATALOG_BEGIN_MARKER = "<!-- BEGIN OFFICIAL_FIRMWARE_CATALOG -->"
CATALOG_END_MARKER = "<!-- END OFFICIAL_FIRMWARE_CATALOG -->"


@dataclass(frozen=True)
class FirmwarePart:
    file_name: str
    offset: int
    size: int
    sha256: str
    download_url: str

    @property
    def offset_hex(self) -> str:
        return "0x0" if self.offset == 0 else f"0x{self.offset:X}"


@dataclass(frozen=True)
class FirmwareReleaseSpec:
    version: str
    channel: str
    name: str
    chip_family: str
    flash_size: str
    flash_mode: str
    flash_freq: str
    baud_rate: int
    prompt_erase: bool
    manifest_url: str
    upstream_release_url: str | None
    parts: tuple[FirmwarePart, ...]

    @property
    def release_tag(self) -> str:
        return f"{RELEASE_TAG_PREFIX}{self.version}"

    @property
    def release_title(self) -> str:
        return f"reTerminal Sticky Official Firmware v{self.version}"

    @property
    def total_size(self) -> int:
        return sum(part.size for part in self.parts)

    @property
    def is_merged_single_binary(self) -> bool:
        return len(self.parts) == 1 and self.parts[0].offset == 0

    def target_release_url(self, target_repo: str) -> str:
        return f"https://github.com/{target_repo}/releases/tag/{self.release_tag}"

    def target_asset_url(self, target_repo: str, asset_name: str) -> str:
        quoted = urllib.parse.quote(asset_name)
        return (
            f"https://github.com/{target_repo}/releases/download/"
            f"{self.release_tag}/{quoted}"
        )


def http_get_bytes(url: str, timeout: int = 60) -> bytes:
    last_err: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_err = exc
            if attempt < HTTP_RETRIES:
                time.sleep(2**attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_err}") from last_err


def download_and_verify_part(part: FirmwarePart, dest_path: Path) -> None:
    last_err: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = urllib.request.Request(
            part.download_url, headers={"User-Agent": USER_AGENT}
        )
        digest = hashlib.sha256()
        total = 0
        try:
            with urllib.request.urlopen(req, timeout=300) as resp, dest_path.open(
                "wb"
            ) as out:
                while True:
                    chunk = resp.read(DOWNLOAD_CHUNK_SIZE)
                    if not chunk:
                        break
                    out.write(chunk)
                    digest.update(chunk)
                    total += len(chunk)
            break
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_err = exc
            dest_path.unlink(missing_ok=True)
            if attempt < HTTP_RETRIES:
                time.sleep(2**attempt)
    else:
        raise RuntimeError(
            f"Failed to download {part.download_url}: {last_err}"
        ) from last_err

    if total != part.size:
        dest_path.unlink(missing_ok=True)
        raise RuntimeError(
            f"Size mismatch for {part.file_name}: expected {part.size}, got {total}"
        )

    actual_sha256 = digest.hexdigest().lower()
    if actual_sha256 != part.sha256.lower():
        dest_path.unlink(missing_ok=True)
        raise RuntimeError(
            f"SHA-256 mismatch for {part.file_name}: "
            f"expected {part.sha256}, got {actual_sha256}"
        )


def raw_repo_url(repo: str, ref: str, rel_path: str) -> str:
    clean_path = rel_path.lstrip("/")
    return f"https://raw.githubusercontent.com/{repo}/{ref}/{clean_path}"


def slugify_version(value: str) -> str:
    # Matches `slugifyVersion` in reterminal-sticky-playground-registry/scripts/list-build-targets.mjs
    slug = re.sub(r"[^a-z0-9.]+", "-", value.strip().lower()).strip("-")
    if not slug or not re.match(r"^[a-z0-9][a-z0-9.-]*$", slug):
        raise RuntimeError(f"Invalid version slug derived from {value!r}")
    return slug


def clean_part_filename(raw_path: str, prefix: str = "") -> tuple[str, str]:
    split = urllib.parse.urlsplit(raw_path)
    rel_clean_path = split.path.lstrip("/")
    base_name = posixpath.basename(rel_clean_path)
    if not base_name:
        raise RuntimeError(f"Invalid firmware part path: {raw_path!r}")
    final_name = f"{prefix}{base_name}" if prefix else base_name
    return rel_clean_path, final_name


def parse_manifest_parts(
    manifest: dict[str, Any],
    manifest_url: str,
    filename_prefix: str = "",
) -> tuple[str, list[FirmwarePart]]:
    builds = manifest.get("builds") or []
    if not builds:
        raise RuntimeError(f"Manifest {manifest_url} contains no builds")
    build = builds[0]
    chip_family = str(build.get("chipFamily", "ESP32-S3"))
    raw_parts = build.get("parts") or []
    if not raw_parts:
        raise RuntimeError(f"Manifest {manifest_url} contains no flash parts")

    parts: list[FirmwarePart] = []
    for raw_part in raw_parts:
        rel_clean_path, file_name = clean_part_filename(
            str(raw_part["path"]), prefix=filename_prefix
        )
        part_url = urllib.parse.urljoin(manifest_url, rel_clean_path)
        parts.append(
            FirmwarePart(
                file_name=file_name,
                offset=int(raw_part["offset"]),
                size=int(raw_part["size"]),
                sha256=str(raw_part["sha256"]).lower(),
                download_url=part_url,
            )
        )
    return chip_family, parts


def fetch_upstream_specs(source_repo: str, source_ref: str) -> list[FirmwareReleaseSpec]:
    firmware_json_url = raw_repo_url(
        source_repo, source_ref, f"{FIRMWARE_ENTRY_PATH}/firmware.json"
    )
    metadata = json.loads(http_get_bytes(firmware_json_url).decode("utf-8"))
    entry_id = str(metadata.get("id", "sticky-factory"))
    flash_cfg = metadata.get("flash") or {}
    raw_versions = flash_cfg.get("versions") or []
    if not raw_versions:
        raise RuntimeError(f"No flash.versions found in {firmware_json_url}")

    specs: list[FirmwareReleaseSpec] = []
    for entry in raw_versions:
        version = str(entry["version"])
        channel = str(entry.get("channel", "stable"))
        upstream_release_url = entry.get("releaseUrl")

        if "manifestPath" in entry:
            rel_manifest = posixpath.normpath(
                f"{FIRMWARE_ENTRY_PATH}/{entry['manifestPath']}"
            )
            manifest_url = raw_repo_url(source_repo, source_ref, rel_manifest)
            manifest = json.loads(http_get_bytes(manifest_url).decode("utf-8"))
            chip_family, parts = parse_manifest_parts(manifest, manifest_url)
        elif "manifestUrl" in entry:
            manifest_url = str(entry["manifestUrl"])
            manifest_bytes = http_get_bytes(manifest_url)
            expected_manifest_sha = str(entry.get("manifestSha256", "")).lower()
            if expected_manifest_sha:
                actual_manifest_sha = (
                    hashlib.sha256(manifest_bytes).hexdigest().lower()
                )
                if actual_manifest_sha != expected_manifest_sha:
                    raise RuntimeError(
                        f"Manifest SHA-256 mismatch for v{version}: "
                        f"expected {expected_manifest_sha}, got {actual_manifest_sha}"
                    )
            manifest = json.loads(manifest_bytes.decode("utf-8"))
            chip_family, parts = parse_manifest_parts(manifest, manifest_url)
        elif entry.get("sourceBuild") is True:
            tag = f"registry-{entry_id}-{slugify_version(version)}"
            upstream_release_url = f"https://github.com/{source_repo}/releases/tag/{tag}"
            manifest_url = (
                f"https://github.com/{source_repo}/releases/download/"
                f"{tag}/manifest.json"
            )
            manifest = json.loads(http_get_bytes(manifest_url).decode("utf-8"))
            chip_family, parts = parse_manifest_parts(manifest, manifest_url)
        elif "variants" in entry:
            variants = entry["variants"]
            parts = []
            manifest = {}
            chip_family = "ESP32-S3"
            manifest_url = firmware_json_url
            for idx, variant in enumerate(variants):
                variant_id = str(variant["id"])
                rel_manifest = posixpath.normpath(
                    f"{FIRMWARE_ENTRY_PATH}/{variant['manifestPath']}"
                )
                v_manifest_url = raw_repo_url(source_repo, source_ref, rel_manifest)
                v_manifest = json.loads(http_get_bytes(v_manifest_url).decode("utf-8"))
                if idx == 0:
                    manifest = v_manifest
                    manifest_url = v_manifest_url
                prefix = f"{variant_id}-" if len(variants) > 1 else ""
                chip_family, v_parts = parse_manifest_parts(
                    v_manifest, v_manifest_url, filename_prefix=prefix
                )
                parts.extend(v_parts)
        else:
            raise RuntimeError(
                f"Unsupported delivery format in firmware.json for version {version}"
            )

        specs.append(
            FirmwareReleaseSpec(
                version=version,
                channel=channel,
                name=str(
                    manifest.get("name", metadata.get("name", "Official Firmware"))
                ),
                chip_family=chip_family,
                flash_size=str(manifest.get("flashSize", "32MB")),
                flash_mode=str(manifest.get("flashMode", "dio")),
                flash_freq=str(manifest.get("flashFreq", "80m")),
                baud_rate=int(manifest.get("baudRate", 460800)),
                prompt_erase=bool(manifest.get("new_install_prompt_erase", True)),
                manifest_url=manifest_url,
                upstream_release_url=upstream_release_url,
                parts=tuple(parts),
            )
        )

    return specs


def format_size(num_bytes: int) -> str:
    if num_bytes >= 1024 * 1024:
        return f"{num_bytes / (1024 * 1024):.2f} MiB"
    if num_bytes >= 1024:
        return f"{num_bytes / 1024:.2f} KiB"
    return f"{num_bytes} B"


def build_normalized_manifest(spec: FirmwareReleaseSpec) -> dict[str, Any]:
    return {
        "name": "reTerminal Sticky Official Firmware",
        "version": spec.version,
        "flashSize": spec.flash_size,
        "flashMode": spec.flash_mode,
        "flashFreq": spec.flash_freq,
        "baudRate": spec.baud_rate,
        "new_install_prompt_erase": spec.prompt_erase,
        "builds": [
            {
                "chipFamily": spec.chip_family,
                "parts": [
                    {
                        "path": part.file_name,
                        "offset": part.offset,
                        "size": part.size,
                        "sha256": part.sha256,
                    }
                    for part in spec.parts
                ],
            }
        ],
    }


def build_sha256sums_text(spec: FirmwareReleaseSpec) -> str:
    return "".join(f"{part.sha256}  {part.file_name}\n" for part in spec.parts)


def build_esptool_command(spec: FirmwareReleaseSpec) -> str:
    chip_arg = spec.chip_family.lower().replace("-", "")
    lines = [
        f"esptool.py --chip {chip_arg} -p PORT -b {spec.baud_rate} \\",
        "  --before default_reset --after hard_reset \\",
        (
            f"  write_flash --flash_mode {spec.flash_mode} "
            f"--flash_size {spec.flash_size} --flash_freq {spec.flash_freq} \\"
        ),
    ]
    for idx, part in enumerate(spec.parts):
        suffix = " \\" if idx < len(spec.parts) - 1 else ""
        lines.append(f"  {part.offset_hex} {part.file_name}{suffix}")
    return "\n".join(lines)


def build_release_notes(spec: FirmwareReleaseSpec, source_repo: str) -> str:
    lines = [
        f"Official factory firmware **v{spec.version}** (`{spec.channel}`) for **Seeed Studio reTerminal Sticky** (`{spec.chip_family}`).",
        "",
        "### Flash Parameters",
        "",
        f"- **Chip:** `{spec.chip_family}`",
        f"- **Flash Configuration:** `{spec.flash_size}`, `{spec.flash_mode.upper()}`, `{spec.flash_freq}`",
        f"- **Recommended Baud Rate:** `{spec.baud_rate}`",
        f"- **Web Flasher:** [reTerminal Sticky Official Firmware Playground]({WEB_FLASHER_URL})",
        "",
        "### Package Checksums (SHA-256)",
        "",
        "| File | Flash Offset | Size | SHA-256 |",
        "| --- | --- | --- | --- |",
    ]
    for part in spec.parts:
        lines.append(
            f"| `{part.file_name}` | `{part.offset_hex}` | "
            f"{part.size:,} B ({format_size(part.size)}) | `{part.sha256}` |"
        )
    lines.extend(
        [
            "",
            "### Command-Line Flashing (`esptool.py`)",
            "",
            "```bash",
            build_esptool_command(spec),
            "```",
            "",
            f"Mirrored from [`{source_repo}`](https://github.com/{source_repo}/tree/main/{FIRMWARE_ENTRY_PATH}).",
            "",
        ]
    )
    return "\n".join(lines)


def run_gh(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        ["gh", *args],
        check=False,
        text=True,
        capture_output=True,
    )
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).strip()
        raise RuntimeError(f"gh {' '.join(args)} failed ({proc.returncode}): {detail}")
    return proc


def get_existing_release_assets(target_repo: str, tag: str) -> dict[str, int] | None:
    proc = run_gh(
        ["release", "view", tag, "--repo", target_repo, "--json", "assets,isDraft"],
        check=False,
    )
    if proc.returncode != 0:
        return None
    payload = json.loads(proc.stdout)
    if payload.get("isDraft"):
        return {}
    return {
        str(asset["name"]): int(asset["size"])
        for asset in (payload.get("assets") or [])
    }


def publish_github_releases(
    specs: list[FirmwareReleaseSpec],
    target_repo: str,
    source_repo: str,
) -> None:
    if not shutil.which("gh"):
        raise RuntimeError("GitHub CLI ('gh') is required for --publish-releases")

    latest_version = specs[0].version

    # Backfill oldest-to-newest so historical releases appear in chronological order.
    for spec in reversed(specs):
        is_latest = spec.version == latest_version
        existing_assets = get_existing_release_assets(target_repo, spec.release_tag)

        manifest_bytes = (
            json.dumps(build_normalized_manifest(spec), indent=2) + "\n"
        ).encode("utf-8")
        sha256sums_bytes = build_sha256sums_text(spec).encode("utf-8")

        expected_sizes = {part.file_name: part.size for part in spec.parts}
        expected_sizes["manifest.json"] = len(manifest_bytes)
        expected_sizes["SHA256SUMS.txt"] = len(sha256sums_bytes)

        if existing_assets is not None and all(
            existing_assets.get(name) == size for name, size in expected_sizes.items()
        ):
            print(f"[skip] Release {spec.release_tag} already complete.")
            if is_latest:
                run_gh(
                    [
                        "release",
                        "edit",
                        spec.release_tag,
                        "--repo",
                        target_repo,
                        "--latest",
                    ],
                    check=False,
                )
            continue

        print(
            f"[sync] Preparing release {spec.release_tag} ({len(spec.parts)} part(s))..."
        )
        with tempfile.TemporaryDirectory(prefix=f"sticky-fw-{spec.version}-") as tmp:
            tmp_dir = Path(tmp)
            upload_paths: list[Path] = []

            for part in spec.parts:
                part_path = tmp_dir / part.file_name
                print(
                    f"  -> Downloading {part.file_name} ({format_size(part.size)})..."
                )
                download_and_verify_part(part, part_path)
                upload_paths.append(part_path)

            manifest_path = tmp_dir / "manifest.json"
            manifest_path.write_bytes(manifest_bytes)
            upload_paths.append(manifest_path)

            sums_path = tmp_dir / "SHA256SUMS.txt"
            sums_path.write_bytes(sha256sums_bytes)
            upload_paths.append(sums_path)

            notes_path = tmp_dir / "RELEASE_NOTES.md"
            notes_path.write_text(
                build_release_notes(spec, source_repo), encoding="utf-8"
            )

            latest_flag = "--latest" if is_latest else "--latest=false"
            if existing_assets is None:
                run_gh(
                    [
                        "release",
                        "create",
                        spec.release_tag,
                        *[str(p) for p in upload_paths],
                        "--repo",
                        target_repo,
                        "--title",
                        spec.release_title,
                        "--notes-file",
                        str(notes_path),
                        latest_flag,
                    ]
                )
                print(f"[done] Created release {spec.release_tag}.")
            else:
                run_gh(
                    [
                        "release",
                        "upload",
                        spec.release_tag,
                        *[str(p) for p in upload_paths],
                        "--clobber",
                        "--repo",
                        target_repo,
                    ]
                )
                run_gh(
                    [
                        "release",
                        "edit",
                        spec.release_tag,
                        "--repo",
                        target_repo,
                        "--title",
                        spec.release_title,
                        "--notes-file",
                        str(notes_path),
                        latest_flag,
                    ]
                )
                print(f"[done] Updated release {spec.release_tag}.")


def build_versions_index(
    specs: list[FirmwareReleaseSpec],
    source_repo: str,
    target_repo: str,
) -> dict[str, Any]:
    return {
        "schemaVersion": 1,
        "id": "sticky-factory",
        "name": "reTerminal Sticky Official Firmware",
        "sourceRepository": f"https://github.com/{source_repo}/tree/main/{FIRMWARE_ENTRY_PATH}",
        "webFlasherUrl": WEB_FLASHER_URL,
        "latestVersion": specs[0].version,
        "versions": [
            {
                "version": spec.version,
                "channel": spec.channel,
                "chipFamily": spec.chip_family,
                "flashSize": spec.flash_size,
                "flashMode": spec.flash_mode,
                "flashFreq": spec.flash_freq,
                "baudRate": spec.baud_rate,
                "layout": "merged" if spec.is_merged_single_binary else "partitioned",
                "totalSize": spec.total_size,
                "releaseTag": spec.release_tag,
                "releaseUrl": spec.target_release_url(target_repo),
                "manifestUrl": spec.target_asset_url(target_repo, "manifest.json"),
                "checksumsUrl": spec.target_asset_url(target_repo, "SHA256SUMS.txt"),
                "parts": [
                    {
                        "fileName": part.file_name,
                        "offset": part.offset,
                        "offsetHex": part.offset_hex,
                        "size": part.size,
                        "sha256": part.sha256,
                        "downloadUrl": spec.target_asset_url(
                            target_repo, part.file_name
                        ),
                        "upstreamDownloadUrl": part.download_url,
                    }
                    for part in spec.parts
                ],
            }
            for spec in specs
        ],
    }


def render_catalog_en(specs: list[FirmwareReleaseSpec], target_repo: str) -> str:
    latest = specs[0]
    partitioned_specs = [s for s in specs if not s.is_merged_single_binary]

    lines = [
        "## Official Factory Firmware Releases",
        "",
        "| Version | Channel | Layout | Size | SHA-256 | Download |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for idx, spec in enumerate(specs):
        ver_label = f"**v{spec.version}** (Latest)" if idx == 0 else f"`v{spec.version}`"
        release_url = spec.target_release_url(target_repo)
        sums_url = spec.target_asset_url(target_repo, "SHA256SUMS.txt")
        if spec.is_merged_single_binary:
            part = spec.parts[0]
            bin_url = spec.target_asset_url(target_repo, part.file_name)
            layout = f"Merged (`{part.offset_hex}`)"
            sha_col = f"`{part.sha256}`"
            dl_col = (
                f"[`.bin`]({bin_url}) · "
                f"[`SHA256SUMS`]({sums_url}) · "
                f"[Release]({release_url})"
            )
        else:
            layout = f"Partitioned ({len(spec.parts)} files)"
            sha_col = f"See partition table below ([`SHA256SUMS`]({sums_url}))"
            dl_col = f"[Release Assets]({release_url})"

        lines.append(
            f"| {ver_label} | `{spec.channel}` | {layout} | "
            f"{format_size(spec.total_size)} | {sha_col} | {dl_col} |"
        )

    for spec in partitioned_specs:
        lines.extend(
            [
                "",
                "<details>",
                f"<summary><strong>Partition layout & SHA-256 checksums for v{spec.version}</strong></summary>",
                "",
                "| File | Offset | Size | SHA-256 | Download |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for part in spec.parts:
            part_url = spec.target_asset_url(target_repo, part.file_name)
            lines.append(
                f"| `{part.file_name}` | `{part.offset_hex}` | "
                f"{format_size(part.size)} | `{part.sha256}` | "
                f"[Download]({part_url}) |"
            )
        lines.extend(
            [
                "",
                "```bash",
                build_esptool_command(spec),
                "```",
                "",
                "</details>",
            ]
        )

    latest_merged = next((s for s in specs if s.is_merged_single_binary), latest)
    lines.extend(
        [
            "",
            "## Flashing Reference (`esptool.py`)",
            "",
            f"### Merged Single-File Releases (`v{latest_merged.version}` and `v0.3.3+`)",
            "",
            "Merged releases write the complete image starting at `0x0`. When restoring a device from third-party or community firmware, run `erase_flash` first so stale NVS or partition state is cleared:",
            "",
            "```bash",
            "# Optional: full erase when recovering from custom firmware",
            "esptool.py --chip esp32s3 -p PORT erase_flash",
            "",
            f"# Flash official merged binary (example: v{latest_merged.version})",
            build_esptool_command(latest_merged),
            "```",
            "",
            "Verify downloaded files locally before flashing:",
            "",
            "```bash",
            "shasum -a 256 -c SHA256SUMS.txt",
            "```",
        ]
    )
    return "\n".join(lines)


def render_catalog_zh(specs: list[FirmwareReleaseSpec], target_repo: str) -> str:
    latest = specs[0]
    partitioned_specs = [s for s in specs if not s.is_merged_single_binary]

    lines = [
        "## 官方出厂固件版本清单",
        "",
        "| 版本 | 通道 | 镜像格式 | 体积 | SHA-256 校验值 | 下载入口 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for idx, spec in enumerate(specs):
        ver_label = (
            f"**v{spec.version}**（最新）"
            if idx == 0
            else f"`v{spec.version}`"
        )
        release_url = spec.target_release_url(target_repo)
        sums_url = spec.target_asset_url(target_repo, "SHA256SUMS.txt")
        if spec.is_merged_single_binary:
            part = spec.parts[0]
            bin_url = spec.target_asset_url(target_repo, part.file_name)
            layout = f"单文件整包（`{part.offset_hex}`）"
            sha_col = f"`{part.sha256}`"
            dl_col = (
                f"[`.bin`]({bin_url}) · "
                f"[`SHA256SUMS`]({sums_url}) · "
                f"[发布页]({release_url})"
            )
        else:
            layout = f"多分区拆包（{len(spec.parts)} 个文件）"
            sha_col = f"见下方分区明细（[`SHA256SUMS`]({sums_url})）"
            dl_col = f"[发布页附件]({release_url})"

        lines.append(
            f"| {ver_label} | `{spec.channel}` | {layout} | "
            f"{format_size(spec.total_size)} | {sha_col} | {dl_col} |"
        )

    for spec in partitioned_specs:
        lines.extend(
            [
                "",
                "<details>",
                (
                    f"<summary><strong>展开查看 v{spec.version} "
                    "分区烧录地址与 SHA-256 明细</strong></summary>"
                ),
                "",
                "| 文件名 | 起始地址 | 体积 | SHA-256 | 下载 |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for part in spec.parts:
            part_url = spec.target_asset_url(target_repo, part.file_name)
            lines.append(
                f"| `{part.file_name}` | `{part.offset_hex}` | "
                f"{format_size(part.size)} | `{part.sha256}` | "
                f"[下载]({part_url}) |"
            )
        lines.extend(
            [
                "",
                "```bash",
                build_esptool_command(spec),
                "```",
                "",
                "</details>",
            ]
        )

    latest_merged = next((s for s in specs if s.is_merged_single_binary), latest)
    lines.extend(
        [
            "",
            "## 命令行烧录参考（`esptool.py`）",
            "",
            f"### 单文件整包烧录（`v{latest_merged.version}` 及 `v0.3.3+`）",
            "",
            "单文件合并镜像从 `0x0` 地址起始写入。若设备此前刷入过社区固件或第三方固件，恢复官方出厂固件前可先执行整片擦除以清理旧分区数据：",
            "",
            "```bash",
            "# Optional: full erase before restoring factory firmware",
            "esptool.py --chip esp32s3 -p PORT erase_flash",
            "",
            f"# Flash official merged firmware (v{latest_merged.version})",
            build_esptool_command(latest_merged),
            "```",
            "",
            "烧录前可在本地核对文件完整性：",
            "",
            "```bash",
            "shasum -a 256 -c SHA256SUMS.txt",
            "```",
        ]
    )
    return "\n".join(lines)


def update_marked_section(path: Path, block_body: str) -> bool:
    original = path.read_text(encoding="utf-8")
    begin_idx = original.find(CATALOG_BEGIN_MARKER)
    end_idx = original.find(CATALOG_END_MARKER)
    if begin_idx == -1 or end_idx == -1 or end_idx < begin_idx:
        raise RuntimeError(
            f"Missing {CATALOG_BEGIN_MARKER} / {CATALOG_END_MARKER} markers in {path}"
        )
    replacement = f"{CATALOG_BEGIN_MARKER}\n\n{block_body}\n\n{CATALOG_END_MARKER}"
    updated = (
        original[:begin_idx]
        + replacement
        + original[end_idx + len(CATALOG_END_MARKER) :]
    )
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize official reTerminal Sticky firmware releases and docs."
    )
    parser.add_argument(
        "--source-repo",
        default=os.environ.get("SOURCE_REPO", DEFAULT_SOURCE_REPO),
        help="Upstream registry GitHub owner/repo.",
    )
    parser.add_argument(
        "--source-ref",
        default=os.environ.get("SOURCE_REF", DEFAULT_SOURCE_REF),
        help="Branch, tag, or commit in the upstream registry repo.",
    )
    parser.add_argument(
        "--target-repo",
        default=os.environ.get("TARGET_REPO", DEFAULT_TARGET_REPO),
        help="Target GitHub owner/repo hosting mirrored releases.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Local root path of OSHW-reTerminal-Sticky.",
    )
    parser.add_argument(
        "--publish-releases",
        action="store_true",
        help="Download missing official firmware binaries, verify SHA-256, and publish GitHub Releases.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root: Path = args.repo_root.resolve()

    print(
        f"Fetching official firmware metadata from {args.source_repo}@{args.source_ref}..."
    )
    specs = fetch_upstream_specs(args.source_repo, args.source_ref)
    print(
        f"Discovered {len(specs)} official version(s): "
        + ", ".join(s.version for s in specs)
    )

    if args.publish_releases:
        publish_github_releases(specs, args.target_repo, args.source_repo)

    versions_json = (
        json.dumps(
            build_versions_index(specs, args.source_repo, args.target_repo),
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )

    changed_files: list[str] = []
    if write_if_changed(repo_root / "firmware/factory/versions.json", versions_json):
        changed_files.append("firmware/factory/versions.json")
    if update_marked_section(
        repo_root / "firmware/README.md", render_catalog_en(specs, args.target_repo)
    ):
        changed_files.append("firmware/README.md")
    if update_marked_section(
        repo_root / "firmware/README-ZH.md", render_catalog_zh(specs, args.target_repo)
    ):
        changed_files.append("firmware/README-ZH.md")

    if changed_files:
        print("Updated files: " + ", ".join(changed_files))
    else:
        print("Catalog files already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
