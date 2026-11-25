# reTerminal Sticky ESP-IDF Examples

[简体中文](README-ZH.md) | [Examples Overview](../README.md) | [Repository Home](../../README.md)

Official **ESP-IDF v5.4** examples and shared driver components for Seeed Studio reTerminal Sticky (`ESP32-S3`, 32 MB Flash, 8 MB Octal PSRAM). Every example automatically detects **SSD1677** or **SSD2677** e-paper panels with a single firmware build.

## Examples

Recommended learning order:

| Example | Path | Recommended For | Highlights |
| --- | --- | --- | --- |
| **Peripheral Examples** | [`peripherals/`](peripherals/) | Bringing up individual hardware peripherals, reading minimal `demo_xxx.cpp/.h` snippets, hardware diagnostics | Sequential self-test of all onboard peripherals (SHT40, e-paper, buzzer, charger, RTC, BQ27220, IMU, PDM mic, MicroSD, GT911 touch, buttons), plus deep sleep & board power-off tests |
| **Dashboard Demo** | [`dashboard/`](dashboard/) | Building a complete multi-page e-paper application with clean layered architecture | 6-page app (`board` / `devices` / `app` / `pages` / `ui`), `Canvas` drawing, swipe & button navigation, minute partial refresh, and deep-sleep page-state restoration |

## Shared Components

All ESP-IDF examples in this directory share a single [`components/`](components/) pool via `EXTRA_COMPONENT_DIRS` in each example's `CMakeLists.txt`:

```text
examples/esp-idf/
├── components/                # Shared Sticky driver components
│   ├── seeed_epaper/          # SSD1677 / SSD2677 / UC8179 e-paper driver
│   ├── gt911/                 # GT911 capacitive touch controller driver
│   ├── bq27220/               # BQ27220 battery fuel gauge driver
│   ├── pcf8563/               # PCF8563 RTC helpers and calendar validation
│   ├── button/                # ESP IoT Button (Apache-2.0, includes local ISR patch)
│   └── debug_logging/         # Optional menuconfig driver diagnostics
├── peripherals/               # Minimal onboard peripheral examples
└── dashboard/                 # Six-page dashboard application demo
```

| Component | Purpose | Notes |
| --- | --- | --- |
| [`seeed_epaper`](components/seeed_epaper/README.md) | E-paper panel abstraction & controller backends | Supports mono full, mono partial, and 4-level grayscale refresh |
| [`gt911`](components/gt911/) | Capacitive touch controller driver | Dedicated I2C0 touch interface |
| [`bq27220`](components/bq27220/) | Battery fuel gauge driver | Voltage, current, SOC, SOH, capacity, temperature, cycles |
| [`pcf8563`](components/pcf8563/) | External RTC helper library | Register access, BCD & calendar validation |
| [`button`](components/button/README.md) | Physical button driver (`espressif/button` 4.1.6) | Retains [Apache-2.0](components/button/license.txt) and [local cache-safe ISR patch](components/button/LOCAL_PATCHES.md) |
| [`debug_logging`](components/debug_logging/) | Optional driver diagnostic logging | Controlled via `idf.py menuconfig` |

## Prerequisites & Build

- **ESP-IDF v5.4** ([Get Started Guide](https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32s3/get-started/))
- reTerminal Sticky (SSD1677 or SSD2677) and USB-C data cable

Open an ESP-IDF v5.4 terminal inside either example directory and build normally:

```bash
cd examples/esp-idf/peripherals   # or: cd examples/esp-idf/dashboard
idf.py set-target esp32s3
idf.py build
idf.py -p PORT flash monitor
```

Replace `PORT` with your serial device (for example `/dev/cu.usbmodem*` on macOS, `/dev/ttyACM0` on Linux, or `COM5` on Windows). Exit the serial monitor with `Ctrl+]`.

> **Note:** Keep `dependencies.lock` intact; the first configure step may require internet access so the ESP Component Manager can fetch `espressif/cmake_utilities`.

## Creating a Standalone Project

If you want to copy one of the examples outside `OSHW-reTerminal-Sticky` as the starting point for your own repository:

1. Copy the example folder (e.g., `examples/esp-idf/dashboard`) to your target workspace.
2. Copy `examples/esp-idf/components` into the copied project folder so `components/` sits directly beside `main/`.
3. Open the copied `CMakeLists.txt` and remove the line:

```cmake
list(APPEND EXTRA_COMPONENT_DIRS "../components")
```

4. Build as a standard self-contained ESP-IDF project:

```bash
idf.py set-target esp32s3
idf.py build
```

You may remove any unused components (for example, `pcf8563` if your project does not list it in `main/CMakeLists.txt`).

## Tutorials & License

- Tutorials: [Basics](https://www.seeedstudio.com/sticky/docs/en/device-guide/esp-basics/) | [Pages and peripherals](https://www.seeedstudio.com/sticky/docs/en/device-guide/esp-pages/) | [Refresh and sleep](https://www.seeedstudio.com/sticky/docs/en/device-guide/esp-refresh/)
- License: [MIT License](../../LICENSE) for original Seeed Studio code; [Apache-2.0](components/button/license.txt) for the bundled Espressif `button` component.
