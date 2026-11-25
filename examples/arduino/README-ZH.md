# reTerminal Sticky Arduino 与 PlatformIO 示例

[English](README.md) | [示例总览](../README-ZH.md) | [仓库首页](../../README-ZH.md)

> **当前状态：** 规划中。当前可立即编译体验的官方外设驱动与综合示例请参阅 [`examples/esp-idf/`](../esp-idf/README-ZH.md)。

本目录用于存放面向 Seeed Studio reTerminal Sticky 的 **Arduino** 与 **PlatformIO** 驱动库、板级配置及示例工程。

## 规划目录结构

```text
examples/arduino/
├── libraries/           # 随仓附带的 Arduino 驱动库（按需）
├── basic_peripherals/   # 屏幕、触摸、传感器与按键基础示例
└── platformio_demo/     # 包含 platformio.ini 的完整 PlatformIO 工程
```

## 目录与命名约定

- 每个示例使用全小写字母加下划线或短横线命名独立子目录（如 `basic_peripherals/`）。
- 每个示例目录内提供独立 `README.md`，写明所需的 Arduino ESP32 Core 版本、第三方库版本、开发板参数（Flash 容量、PSRAM 模式）以及屏幕兼容性（SSD1677 / SSD2677）。
- 引脚配置以 [`examples/esp-idf/peripherals/main/pin_config.h`](../esp-idf/peripherals/main/pin_config.h) 中经过验证的硬件定义为准。
