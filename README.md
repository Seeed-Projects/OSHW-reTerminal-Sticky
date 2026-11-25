# OSHW-reTerminal-Sticky

[简体中文](README-ZH.md)

Open-source hardware and software resource repository for **Seeed Studio reTerminal Sticky** — an ESP32-S3 based e-paper terminal featuring an 800 × 480 display (automatic SSD1677 / SSD2677 detection in firmware), capacitive touch, environmental & motion sensors, RTC, fuel gauge, MicroSD, PDM microphone, buzzer, and hardware power management.

## Repository Structure

This repository is organized as a unified hub for reTerminal Sticky examples, prebuilt firmware, and open-source hardware files. Each directory holds a dedicated category of resources and is populated as releases become available:

| Path | Status | Description |
| --- | --- | --- |
| [`examples/esp-idf/`](examples/esp-idf/) | Available | ESP-IDF v5.4 shared driver components and official examples (`peripherals`, `dashboard`) |
| [`examples/arduino/`](examples/arduino/) | Planned | Arduino / PlatformIO libraries and examples |
| [`examples/esphome/`](examples/esphome/) | Planned | ESPHome YAML configurations |
| [`examples/community/`](examples/community/) | Planned | Community-contributed projects and applications |
| [`firmware/`](firmware/) | Available | Official factory firmware catalog, SHA-256 checksums, flashing guide, and automated GitHub Releases sync |
| [`hardware/`](hardware/) | Available | Official schematic PDF, 3D model (`.stp`), and 3D-printable playground link (PCB/BOM & datasheets planned) |
| [`docs/`](docs/) | Planned | Repository-specific technical notes and hardware revision logs |

## Onboard Hardware Overview

| Subsystem | Hardware / Specification |
| --- | --- |
| MCU & Memory | ESP32-S3, 32 MB Flash, 8 MB Octal PSRAM (80 MHz) |
| Display | 800 × 480 e-paper panel (SSD1677 or SSD2677, auto-detected by firmware; mono full/partial & 4-level grayscale) |
| Touch | GT911 capacitive touch controller (dedicated I2C0) |
| Environment Sensor | SHT40 temperature & humidity (`0x44`, I2C1) |
| 6-Axis IMU | LSM6DS3TR-C accelerometer & gyroscope (`0x6A`, I2C1) |
| RTC | PCF8563 real-time clock (`0x51`, I2C1) |
| Battery & Power | BQ27220 fuel gauge (`0x55`, I2C1), BQ25616 charger enable/status, hardware power hold/lock |
| Audio | PDM microphone and LEDC PWM buzzer |
| Storage | MicroSD card slot (shares SPI2 bus with the e-paper display) |
| Buttons | 3 physical buttons: `POWER / OK / AI` (GPIO4), `UP` (GPIO5), `DOWN` (GPIO6) |

For verified pin assignments and bus sharing notes, see [`examples/esp-idf/peripherals/main/pin_config.h`](examples/esp-idf/peripherals/main/pin_config.h) or [`examples/esp-idf/dashboard/main/pin_config.h`](examples/esp-idf/dashboard/main/pin_config.h). Official schematics and 3D CAD models are available under [`hardware/`](hardware/).

## Quick Start (ESP-IDF)

1. Install **ESP-IDF v5.4** following the [ESP-IDF Get Started Guide](https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32s3/get-started/).
2. Clone this repository:

```bash
git clone https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky.git
cd OSHW-reTerminal-Sticky
```

3. Choose an example under [`examples/esp-idf/`](examples/esp-idf/):
   - **Start with hardware verification / minimal driver reference:** [`examples/esp-idf/peripherals`](examples/esp-idf/peripherals/)
   - **Explore a complete six-page interactive application:** [`examples/esp-idf/dashboard`](examples/esp-idf/dashboard/)
4. Build and flash from the example directory:

```bash
cd examples/esp-idf/peripherals   # or: cd examples/esp-idf/dashboard
idf.py set-target esp32s3
idf.py build
idf.py -p PORT flash monitor
```

See the [ESP-IDF Examples Guide](examples/esp-idf/README.md) for shared component details and instructions on extracting a standalone project.

## Documentation

Official Seeed Studio ESP-IDF tutorials for reTerminal Sticky:

- [ESP-IDF Basics](https://www.seeedstudio.com/sticky/docs/en/device-guide/esp-basics/)
- [Pages and Peripherals](https://www.seeedstudio.com/sticky/docs/en/device-guide/esp-pages/)
- [Refresh and Deep Sleep](https://www.seeedstudio.com/sticky/docs/en/device-guide/esp-refresh/)

## License

- Original software in this repository is licensed under the [MIT License](LICENSE), Copyright (c) 2026 Seeed Studio.
- The bundled Espressif button component retains its [Apache-2.0 license](examples/esp-idf/components/button/license.txt), copyright notices, and [local patch record](examples/esp-idf/components/button/LOCAL_PATCHES.md).
- ESP-IDF and ESP Component Manager dependencies retain their respective licenses.
- Hardware schematics under [`hardware/schematics/`](hardware/schematics/reTerminal_Sticky_Schematic_diagram_260609.pdf) are licensed under **CC BY-SA 4.0** (as marked on the schematic title block); additional hardware design files carry their respective license notices under [`hardware/`](hardware/).
