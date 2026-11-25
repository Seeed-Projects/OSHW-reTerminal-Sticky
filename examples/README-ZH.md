# reTerminal Sticky 软件示例总览

[English](README.md) | [仓库首页](../README-ZH.md)

本目录按开发框架分类存放 reTerminal Sticky 的软件示例工程。

## 框架目录

| 目录 | 状态 | 说明 |
| --- | --- | --- |
| [`esp-idf/`](esp-idf/README-ZH.md) | 已开放 | 官方 ESP-IDF v5.4 示例（`peripherals`、`dashboard`）与共享驱动组件 |
| [`arduino/`](arduino/README-ZH.md) | 规划中 | Arduino / PlatformIO 驱动库与示例程序 |
| [`esphome/`](esphome/README-ZH.md) | 规划中 | ESPHome YAML 配置模板 |
| [`community/`](community/README-ZH.md) | 规划中 | 社区开发者贡献的应用与示例 |

## 硬件引脚参考

所有示例均面向同一套硬件平台（`ESP32-S3`、32 MB Flash、8 MB 八线 PSRAM、SSD1677 / SSD2677 电子纸）。经过验证的引脚与总线分配详见 [`esp-idf/peripherals/main/pin_config.h`](esp-idf/peripherals/main/pin_config.h)。
