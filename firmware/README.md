# reTerminal Sticky Prebuilt Firmware

[简体中文](README-ZH.md) | [Repository Home](../README.md)

Official prebuilt factory firmware packages for **Seeed Studio reTerminal Sticky** (`ESP32-S3`, 32 MB Flash). Every official release is verified by SHA-256 checksum and published to this repository's [GitHub Releases](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases).

- **One-Click Browser Flasher (Recommended):** Flash any official release directly over USB in desktop Chrome or Edge via the [Official Firmware Web Flasher](https://www.seeedstudio.com/sticky/playground/official-firmware/).
- **Build from Source:** See [`examples/esp-idf/`](../examples/esp-idf/) for ESP-IDF v5.4 driver components and reference firmware.

<!-- BEGIN OFFICIAL_FIRMWARE_CATALOG -->

## Official Factory Firmware Releases

| Version | Channel | Layout | Size | SHA-256 | Download |
| --- | --- | --- | --- | --- | --- |
| **v1.2.0** (Latest) | `stable` | Merged (`0x0`) | 31.75 MiB | `5cd55031ddee26cf32ed9e01dd89ed8d820bdbfe752d0140b136177fab26a2a2` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.2.0/reterminal_sticky_1_2_0.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.2.0/SHA256SUMS.txt) · [Release](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v1.2.0) |
| `v1.1.0` | `stable` | Merged (`0x0`) | 31.75 MiB | `8b149c809b7c07c680a59ab5621d7bd29ca85a8c1c9e9060b0040b387b4517e4` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.1.0/reterminal_sticky_1_1_0.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.1.0/SHA256SUMS.txt) · [Release](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v1.1.0) |
| `v1.0.1` | `stable` | Merged (`0x0`) | 31.75 MiB | `36f74e22c5f366af82d31eab224c10a380bf7cb6081e8d52b6c290d7b54b577c` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.0.1/reterminal_sticky_1_0_1.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.0.1/SHA256SUMS.txt) · [Release](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v1.0.1) |
| `v0.5.1` | `stable` | Merged (`0x0`) | 31.75 MiB | `ec4a0c578d9cdac6944e7ea60336b4e4ee31a15a71f6ef6d56ac9bbf7b1bbcd5` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.5.1/merged-flash_v051_prod.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.5.1/SHA256SUMS.txt) · [Release](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.5.1) |
| `v0.4.1` | `stable` | Merged (`0x0`) | 31.75 MiB | `aba151075f359440e1ae399468af370024648b5c69d59ddf37336ea00edcf87d` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.4.1/merged-flash_v041_prod.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.4.1/SHA256SUMS.txt) · [Release](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.4.1) |
| `v0.3.3` | `stable` | Merged (`0x0`) | 31.75 MiB | `57b72cc53c7d61d16b84694735cbe766d425c1add2f230edac16eb5ad10a2f6a` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.3.3/sticky_0.3.3.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.3.3/SHA256SUMS.txt) · [Release](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.3.3) |
| `v0.2.1` | `stable` | Partitioned (6 files) | 22.02 MiB | See partition table below ([`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/SHA256SUMS.txt)) | [Release Assets](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.2.1) |

<details>
<summary><strong>Partition layout & SHA-256 checksums for v0.2.1</strong></summary>

| File | Offset | Size | SHA-256 | Download |
| --- | --- | --- | --- | --- |
| `bootloader.bin` | `0x0` | 21.05 KiB | `7076cf06ec5a947cd15d8aea3a46144f6296780fd33a47601361f66e44195ac5` | [Download](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/bootloader.bin) |
| `partition-table.bin` | `0x8000` | 3.00 KiB | `8370e5f553721492ae6605c8a71aa642a2b5bc064c6b8885ac096bfc31a11f1f` | [Download](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/partition-table.bin) |
| `ota_data_initial.bin` | `0x86000` | 8.00 KiB | `7d2c7ac4888bfd75cd5f56e8d61f69595121183afc81556c876732fd3782c62f` | [Download](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/ota_data_initial.bin) |
| `reterminal_template.bin` | `0x90000` | 2.80 MiB | `12b868fc231228271bbf3f008c671cd030063992808c423b61bc8ca60161d732` | [Download](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/reterminal_template.bin) |
| `sys_storage.bin` | `0xC90000` | 9.19 MiB | `85c642467579081944e26579aed1ff96c70e79f3d1d868374c502b41896e0191` | [Download](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/sys_storage.bin) |
| `usr_storage.bin` | `0x15C0000` | 10.00 MiB | `ea729c22a9796bec404bf06d7ef063f74ca15fd854d13a1d8512f5d92b7dad28` | [Download](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/usr_storage.bin) |

```bash
esptool.py --chip esp32s3 -p PORT -b 921600 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m \
  0x0 bootloader.bin \
  0x8000 partition-table.bin \
  0x86000 ota_data_initial.bin \
  0x90000 reterminal_template.bin \
  0xC90000 sys_storage.bin \
  0x15C0000 usr_storage.bin
```

</details>

## Flashing Reference (`esptool.py`)

### Merged Single-File Releases (`v1.2.0` and `v0.3.3+`)

Merged releases write the complete image starting at `0x0`. When restoring a device from third-party or community firmware, run `erase_flash` first so stale NVS or partition state is cleared:

```bash
# Optional: full erase when recovering from custom firmware
esptool.py --chip esp32s3 -p PORT erase_flash

# Flash official merged binary (example: v1.2.0)
esptool.py --chip esp32s3 -p PORT -b 460800 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m \
  0x0 reterminal_sticky_1_2_0.bin
```

Verify downloaded files locally before flashing:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

<!-- END OFFICIAL_FIRMWARE_CATALOG -->

## Directory Layout & Synchronization

```text
firmware/
├── factory/
│   └── versions.json    # Machine-readable catalog, offsets, and SHA-256 index
├── README.md
└── README-ZH.md
```

Official firmware packages are automatically mirrored from [`Seeed-Projects/reterminal-sticky-playground-registry`](https://github.com/Seeed-Projects/reterminal-sticky-playground-registry/tree/main/firmwares/sticky-factory) via [`.github/workflows/sync-official-firmware.yml`](../.github/workflows/sync-official-firmware.yml) whenever a new official factory build is published.
