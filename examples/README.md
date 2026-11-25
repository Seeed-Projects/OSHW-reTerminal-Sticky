# reTerminal Sticky Software Examples

[简体中文](README-ZH.md) | [Repository Home](../README.md)

This directory organizes all reTerminal Sticky software examples by development framework.

## Framework Directory

| Path | Status | Description |
| --- | --- | --- |
| [`esp-idf/`](esp-idf/) | Available | Official ESP-IDF v5.4 examples (`peripherals`, `dashboard`) and shared driver components |
| [`arduino/`](arduino/) | Planned | Arduino / PlatformIO libraries and sketches |
| [`esphome/`](esphome/) | Planned | ESPHome YAML configuration templates |
| [`community/`](community/) | Planned | Community-contributed projects and applications |

## Shared Hardware Reference

All examples target the same onboard pinout (`ESP32-S3`, 32 MB Flash, 8 MB Octal PSRAM, SSD1677 / SSD2677 e-paper). For verified GPIO and bus assignments, see [`esp-idf/peripherals/main/pin_config.h`](esp-idf/peripherals/main/pin_config.h).
