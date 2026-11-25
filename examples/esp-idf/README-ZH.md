# reTerminal Sticky ESP-IDF 示例总览

[English](README.md) | [示例总览](../README-ZH.md) | [仓库首页](../../README-ZH.md)

面向 Seeed Studio reTerminal Sticky（`ESP32-S3`、32 MB Flash、8 MB 八线 PSRAM）的官方 **ESP-IDF v5.4** 示例工程与共享驱动组件。所有示例均通过同一份固件自动识别 **SSD1677** 与 **SSD2677** 电子纸控制器，无需手动切换驱动。

## 示例清单

推荐按以下顺序阅读与上手：

| 示例 | 目录 | 适用场景 | 核心内容 |
| --- | --- | --- | --- |
| **板载外设最小例程** | [`peripherals/`](peripherals/README-ZH.md) | 硬件自检、单独查阅某个外设的最小 `demo_xxx.cpp/.h` 驱动写法、快速复制复用 | 上电顺序演示全部板载外设（SHT40、电子纸、蜂鸣器、充电控制、RTC、BQ27220、IMU、PDM 麦克风、MicroSD、GT911 触摸、按键），并包含深睡与板级关机测试 |
| **应用仪表盘 Demo** | [`dashboard/`](dashboard/README-ZH.md) | 学习完整电子纸应用分层架构、直接体验综合交互 | 六页完整应用（`board` / `devices` / `app` / `pages` / `ui` 分层）、`Canvas` 绘图、按键与滑动翻页、分钟局刷与深睡页面状态恢复 |

## 共享驱动组件

本目录下所有 ESP-IDF 示例通过各自 `CMakeLists.txt` 中的 `EXTRA_COMPONENT_DIRS` 统一引用同一份 [`components/`](components/) 组件池，集中维护双屏驱动与补丁：

```text
examples/esp-idf/
├── components/                # Sticky 共享驱动组件池
│   ├── seeed_epaper/          # SSD1677 / SSD2677 / UC8179 电子纸驱动
│   ├── gt911/                 # GT911 电容触摸控制器驱动
│   ├── bq27220/               # BQ27220 电池电量计驱动
│   ├── pcf8563/               # PCF8563 外部 RTC 驱动与日期校验
│   ├── button/                # ESP IoT Button（Apache-2.0，含本地 ISR 补丁）
│   └── debug_logging/         # 可选驱动诊断日志开关
├── peripherals/               # 板载外设最小参考例程
└── dashboard/                 # 六页综合应用仪表盘 Demo
```

| 组件 | 用途 | 说明 |
| --- | --- | --- |
| [`seeed_epaper`](components/seeed_epaper/README.md) | 电子纸面板抽象层与控制器后端 | 支持黑白全刷、黑白局刷、四阶灰度全刷 |
| [`gt911`](components/gt911/) | 电容触摸控制器驱动 | 使用独立 I2C0 触摸总线 |
| [`bq27220`](components/bq27220/) | 电池电量计驱动 | 读取电压、电流、SOC、SOH、容量、温度及循环次数 |
| [`pcf8563`](components/pcf8563/) | 外部 RTC 辅助组件 | 寄存器读写、VL 标志、BCD 与日历合法性校验 |
| [`button`](components/button/README.md) | 按键驱动组件（基于 `espressif/button` 4.1.6） | 保留 [Apache-2.0](components/button/license.txt) 协议及[本地 Cache 安全 ISR 补丁](components/button/LOCAL_PATCHES.md) |
| [`debug_logging`](components/debug_logging/) | 可选驱动调试日志 | 通过 `idf.py menuconfig` 控制开关 |

## 环境与编译

- **ESP-IDF v5.4**（[ESP-IDF 入门指南](https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4/esp32s3/get-started/)）
- reTerminal Sticky（SSD1677 或 SSD2677）及 USB-C 数据线

在 ESP-IDF v5.4 终端中进入任一示例目录，按常规流程构建烧录即可：

```bash
cd examples/esp-idf/peripherals   # 或：cd examples/esp-idf/dashboard
idf.py set-target esp32s3
idf.py build
idf.py -p PORT flash monitor
```

将 `PORT` 替换为实际串口（例如 macOS 的 `/dev/cu.usbmodem*`、Linux 的 `/dev/ttyACM0` 或 Windows 的 `COM5`）；按 `Ctrl+]` 退出监视器。

> **提示：** 请保留各示例目录中的 `dependencies.lock`；首次配置可能需要联网由 ESP Component Manager 下载 `espressif/cmake_utilities`。

## 独立拆出工程进行二次开发

如果你想以某个示例为起点，单独复制到本仓库之外新建自己的项目：

1. 将所需示例目录（例如 `examples/esp-idf/dashboard`）复制到目标路径。
2. 将同级的 `examples/esp-idf/components` 完整复制到该工程目录下，使其与 `main/` 并列成为 `components/`。
3. 打开工程根目录的 `CMakeLists.txt`，删除下面这一行：

```cmake
list(APPEND EXTRA_COMPONENT_DIRS "../components")
```

4. 随后即可作为完全独立的 ESP-IDF 工程正常编译：

```bash
idf.py set-target esp32s3
idf.py build
```

如果新工程不需要某些组件（例如未在 `main/CMakeLists.txt` 中引用的 `pcf8563`），可按需从本地 `components/` 中移除。

## 教程与许可证

- 官方教程：[开发基础](https://www.seeedstudio.com/sticky/docs/zh/device-guide/esp-basics/) | [页面与外设](https://www.seeedstudio.com/sticky/docs/zh/device-guide/esp-pages/) | [刷新与低功耗](https://www.seeedstudio.com/sticky/docs/zh/device-guide/esp-refresh/)
- 许可证：自有源码采用 [MIT 许可证](../../LICENSE)；随附 Espressif `button` 组件保留 [Apache-2.0 许可证](components/button/license.txt)。
