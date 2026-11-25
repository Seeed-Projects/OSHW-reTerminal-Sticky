# reTerminal Sticky Prebuilt Firmware

[简体中文](README-ZH.md) | [Repository Home](../README.md)

> **Status:** Planned. To build firmware from source today, see [`examples/esp-idf/`](../examples/esp-idf/).

This directory stores prebuilt factory and demo firmware images for Seeed Studio reTerminal Sticky, along with flashing commands and release notes.

## Planned Layout

```text
firmware/
├── factory/             # Official factory firmware releases and manifests
└── demos/               # Prebuilt showcase binaries (merged single-file images)
```

## Naming & Release Conventions

- Name merged flashable binaries with firmware name, target chip, and version (for example, `reterminal-sticky-factory-esp32s3-v1.0.0-merged.bin`).
- Include a short release note or manifest per release specifying the exact flash offset (`0x0` for merged binaries), SHA-256 checksum, and supported hardware revisions.
- Large historical binary archives are published via GitHub Releases and linked here.

## Flashing Reference (`esptool`)

For a merged single-file binary flashed at `0x0` on `ESP32-S3` (32 MB Flash, DIO, 80 MHz):

```bash
esptool.py --chip esp32s3 -p PORT -b 460800 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m \
  0x0 <firmware-merged.bin>
```
