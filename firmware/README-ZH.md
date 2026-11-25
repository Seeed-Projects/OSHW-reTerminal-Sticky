# reTerminal Sticky 预编译固件

[English](README.md) | [仓库首页](../README-ZH.md)

> **当前状态：** 规划中。如需从源码自行编译固件，请参阅 [`examples/esp-idf/`](../examples/esp-idf/README-ZH.md)。

本目录用于存放 Seeed Studio reTerminal Sticky 的免编译出厂固件、演示固件以及对应的烧录说明与版本清单。

## 规划目录结构

```text
firmware/
├── factory/             # 官方出厂固件发布包与版本清单
└── demos/               # 预构建演示固件（单文件合并镜像）
```

## 命名与发布约定

- 合并后的单文件固件按「产品-固件用途-芯片-版本号」命名（例如 `reterminal-sticky-factory-esp32s3-v1.0.0-merged.bin`）。
- 每次发布附带简要说明或清单文件，写明烧录起始地址（合并镜像为 `0x0`）、SHA-256 校验值与适用的硬件版本。
- 体积较大的历史归档固件通过 GitHub Releases 分发，并在此处汇总下载链接。

## 烧录命令参考（`esptool`）

针对 `ESP32-S3`（32 MB Flash、DIO、80 MHz）的单文件合并固件，从 `0x0` 起始烧录：

```bash
esptool.py --chip esp32s3 -p PORT -b 460800 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m \
  0x0 <firmware-merged.bin>
```
