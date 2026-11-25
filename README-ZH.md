# OSHW-reTerminal-Sticky

[English](README.md)

**Seeed Studio reTerminal Sticky** 开源硬件与软件资源总仓库。reTerminal Sticky 是基于 ESP32-S3 的电子纸终端，配备 800 × 480 电子纸屏幕（固件自动识别 SSD1677 / SSD2677）、电容触摸、温湿度与六轴传感器、RTC、电量计、MicroSD 卡槽、PDM 麦克风、蜂鸣器及板级电源管理。

## 仓库目录结构

本仓库统一承载 reTerminal Sticky 的软件示例、预编译固件与开源硬件资料，各目录已按模块划分并随资料就绪逐步填充：

| 路径 | 状态 | 说明 |
| --- | --- | --- |
| [`examples/esp-idf/`](examples/esp-idf/README-ZH.md) | 已开放 | ESP-IDF v5.4 共享驱动组件及官方示例（`peripherals`、`dashboard`） |
| [`examples/arduino/`](examples/arduino/README-ZH.md) | 规划中 | Arduino / PlatformIO 驱动库与示例 |
| [`examples/esphome/`](examples/esphome/README-ZH.md) | 规划中 | ESPHome YAML 配置模板 |
| [`examples/community/`](examples/community/README-ZH.md) | 规划中 | 社区开发者贡献的应用与示例 |
| [`firmware/`](firmware/README-ZH.md) | 已开放 | 官方出厂固件版本总表、SHA-256 校验值、烧录指南及 GitHub Releases 自动同步 |
| [`hardware/`](hardware/README-ZH.md) | 已开放 | 官方原理图 PDF、3D 模型（`.stp`）与 3D 打印资源入口（PCB / BOM 与器件手册持续补充） |
| [`docs/`](docs/README-ZH.md) | 规划中 | 仓库补充技术文档与硬件版本记录 |

## 板载硬件概览

| 子系统 | 硬件与规格 |
| --- | --- |
| 主控与存储 | ESP32-S3，32 MB Flash，8 MB 八线 PSRAM（80 MHz） |
| 电子纸屏幕 | 800 × 480（SSD1677 或 SSD2677，固件自动识别；支持黑白全刷/局刷及四阶灰度） |
| 触摸屏 | GT911 电容触摸控制器（独立 I2C0） |
| 环境传感器 | SHT40 温湿度传感器（`0x44`，I2C1） |
| 六轴 IMU | LSM6DS3TR-C 加速度计与陀螺仪（`0x6A`，I2C1） |
| 实时时钟 | PCF8563 RTC（`0x51`，I2C1） |
| 电池与电源 | BQ27220 电量计（`0x55`，I2C1）、BQ25616 充电控制与状态检测、硬件电源锁存 |
| 音频 | PDM 麦克风、LEDC PWM 蜂鸣器 |
| 扩展存储 | MicroSD 卡槽（与电子纸共享 SPI2 总线） |
| 实体按键 | 3 个物理按键：`POWER / OK / AI`（GPIO4）、`UP`（GPIO5）、`DOWN`（GPIO6） |

经过验证的完整引脚分配与总线说明请参考 [`examples/esp-idf/peripherals/main/pin_config.h`](examples/esp-idf/peripherals/main/pin_config.h) 或 [`examples/esp-idf/dashboard/main/pin_config.h`](examples/esp-idf/dashboard/main/pin_config.h)；官方电路原理图与 3D 模型见 [`hardware/`](hardware/README-ZH.md)。

## 快速开始（ESP-IDF）

1. 按 [ESP-IDF v5.4 入门指南](https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4/esp32s3/get-started/) 安装开发环境。
2. 克隆本仓库：

```bash
git clone https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky.git
cd OSHW-reTerminal-Sticky
```

3. 在 [`examples/esp-idf/`](examples/esp-idf/README-ZH.md) 中选择示例工程：
   - **板载硬件验证 / 单外设最小参考例程**：[`examples/esp-idf/peripherals`](examples/esp-idf/peripherals/README-ZH.md)
   - **六页综合应用仪表盘 Demo**：[`examples/esp-idf/dashboard`](examples/esp-idf/dashboard/README-ZH.md)
4. 进入对应示例目录编译并烧录：

```bash
cd examples/esp-idf/peripherals   # 或：cd examples/esp-idf/dashboard
idf.py set-target esp32s3
idf.py build
idf.py -p PORT flash monitor
```

关于共享驱动组件架构以及如何将单个示例拆出为独立工程，请参阅 [ESP-IDF 示例总览](examples/esp-idf/README-ZH.md)。

## 官方文档

Seeed Studio reTerminal Sticky ESP-IDF 系列教程：

- [ESP-IDF 开发基础](https://www.seeedstudio.com/sticky/docs/zh/device-guide/esp-basics/)
- [页面与外设开发](https://www.seeedstudio.com/sticky/docs/zh/device-guide/esp-pages/)
- [屏幕刷新与低功耗](https://www.seeedstudio.com/sticky/docs/zh/device-guide/esp-refresh/)

## 许可证

- 本仓库自有软件源码采用 [MIT 许可证](LICENSE)，版权归属 2026 Seeed Studio。
- 随附的 Espressif 按键组件保留其 [Apache-2.0 许可证](examples/esp-idf/components/button/license.txt)、源码版权声明及[本地补丁记录](examples/esp-idf/components/button/LOCAL_PATCHES.md)。
- ESP-IDF 与 Component Manager 依赖遵循各自原有许可证。
- [`hardware/schematics/`](hardware/schematics/reTerminal_Sticky_Schematic_diagram_260609.pdf) 中的官方电路原理图采用 **CC BY-SA 4.0** 许可证（以原理图图框标注为准）；后续补充的其他硬件设计文件遵循 [`hardware/`](hardware/README-ZH.md) 目录下的对应许可声明。
