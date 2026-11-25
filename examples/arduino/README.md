# reTerminal Sticky Arduino & PlatformIO Examples

[简体中文](README-ZH.md) | [Examples Overview](../README.md) | [Repository Home](../../README.md)

> **Status:** Planned. For production-ready driver references and interactive demos today, see [`examples/esp-idf/`](../esp-idf/).

This directory is reserved for **Arduino** and **PlatformIO** support packages, board profiles, and example sketches for Seeed Studio reTerminal Sticky.

## Planned Layout

```text
examples/arduino/
├── libraries/           # Reusable Arduino driver libraries (when bundled locally)
├── basic_peripherals/   # Minimal sketches for display, touch, sensors, and buttons
└── platformio_demo/     # Complete PlatformIO project with platformio.ini
```

## Contribution & Organization Conventions

- Use lowercase snake_case or kebab-case folder names matching each sketch or PlatformIO project.
- Include a `README.md` inside each example specifying the target Arduino ESP32 core version, required library versions, board configuration (Flash size, PSRAM mode), and panel compatibility (SSD1677 / SSD2677).
- Pin definitions follow the verified hardware mapping in [`examples/esp-idf/peripherals/main/pin_config.h`](../esp-idf/peripherals/main/pin_config.h).
