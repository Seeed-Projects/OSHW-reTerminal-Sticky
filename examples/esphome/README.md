# reTerminal Sticky ESPHome Configurations

[简体中文](README-ZH.md) | [Examples Overview](../README.md) | [Repository Home](../../README.md)

> **Status:** Planned. For current native firmware examples, see [`examples/esp-idf/`](../esp-idf/).

This directory is reserved for **ESPHome** YAML configuration templates, external component references, and Home Assistant integration guides for Seeed Studio reTerminal Sticky.

## Planned Layout

```text
examples/esphome/
├── common/              # Reusable board packages (board pins, I2C/SPI buses, buttons)
├── dashboard/           # Ready-to-use Home Assistant e-paper dashboard YAML
└── secrets.yaml.example # Sanitized template for Wi-Fi and API credentials
```

## Configuration Conventions

- Provide a sanitized `secrets.yaml.example` template for Wi-Fi, API keys, and OTA passwords, keeping actual credentials in local untracked files.
- Document the tested ESPHome version, ESP-IDF/Arduino framework choice, and supported e-paper controller (SSD1677 / SSD2677) in each configuration's `README.md`.
- Refer to [`examples/esp-idf/peripherals/main/pin_config.h`](../esp-idf/peripherals/main/pin_config.h) for onboard GPIO and I2C/SPI bus assignments.
