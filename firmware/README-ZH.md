# reTerminal Sticky 预编译固件

[English](README.md) | [仓库首页](../README-ZH.md)

**Seeed Studio reTerminal Sticky**（`ESP32-S3`，32 MB Flash）官方出厂与恢复固件汇总。所有版本均经 SHA-256 完整性校验，并归档在本仓库的 [GitHub Releases](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases) 中。

- **网页一键刷机（推荐）：** 使用桌面端 Chrome 或 Edge 浏览器连接 USB 数据线，通过 [官方在线刷机工具](https://www.seeedstudio.com/sticky/playground/official-firmware/) 直接选择版本烧录。
- **从源码编译：** 如需自行开发或编译固件，请参阅 [`examples/esp-idf/`](../examples/esp-idf/README-ZH.md)。

<!-- BEGIN OFFICIAL_FIRMWARE_CATALOG -->

## 官方出厂固件版本清单

| 版本 | 通道 | 镜像格式 | 体积 | SHA-256 校验值 | 下载入口 |
| --- | --- | --- | --- | --- | --- |
| **v1.2.0**（最新） | `stable` | 单文件整包（`0x0`） | 31.75 MiB | `5cd55031ddee26cf32ed9e01dd89ed8d820bdbfe752d0140b136177fab26a2a2` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.2.0/reterminal_sticky_1_2_0.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.2.0/SHA256SUMS.txt) · [发布页](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v1.2.0) |
| `v1.1.0` | `stable` | 单文件整包（`0x0`） | 31.75 MiB | `8b149c809b7c07c680a59ab5621d7bd29ca85a8c1c9e9060b0040b387b4517e4` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.1.0/reterminal_sticky_1_1_0.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.1.0/SHA256SUMS.txt) · [发布页](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v1.1.0) |
| `v1.0.1` | `stable` | 单文件整包（`0x0`） | 31.75 MiB | `36f74e22c5f366af82d31eab224c10a380bf7cb6081e8d52b6c290d7b54b577c` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.0.1/reterminal_sticky_1_0_1.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v1.0.1/SHA256SUMS.txt) · [发布页](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v1.0.1) |
| `v0.5.1` | `stable` | 单文件整包（`0x0`） | 31.75 MiB | `ec4a0c578d9cdac6944e7ea60336b4e4ee31a15a71f6ef6d56ac9bbf7b1bbcd5` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.5.1/merged-flash_v051_prod.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.5.1/SHA256SUMS.txt) · [发布页](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.5.1) |
| `v0.4.1` | `stable` | 单文件整包（`0x0`） | 31.75 MiB | `aba151075f359440e1ae399468af370024648b5c69d59ddf37336ea00edcf87d` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.4.1/merged-flash_v041_prod.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.4.1/SHA256SUMS.txt) · [发布页](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.4.1) |
| `v0.3.3` | `stable` | 单文件整包（`0x0`） | 31.75 MiB | `57b72cc53c7d61d16b84694735cbe766d425c1add2f230edac16eb5ad10a2f6a` | [`.bin`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.3.3/sticky_0.3.3.bin) · [`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.3.3/SHA256SUMS.txt) · [发布页](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.3.3) |
| `v0.2.1` | `stable` | 多分区拆包（6 个文件） | 22.02 MiB | 见下方分区明细（[`SHA256SUMS`](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/SHA256SUMS.txt)） | [发布页附件](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/tag/firmware-official-v0.2.1) |

<details>
<summary><strong>展开查看 v0.2.1 分区烧录地址与 SHA-256 明细</strong></summary>

| 文件名 | 起始地址 | 体积 | SHA-256 | 下载 |
| --- | --- | --- | --- | --- |
| `bootloader.bin` | `0x0` | 21.05 KiB | `7076cf06ec5a947cd15d8aea3a46144f6296780fd33a47601361f66e44195ac5` | [下载](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/bootloader.bin) |
| `partition-table.bin` | `0x8000` | 3.00 KiB | `8370e5f553721492ae6605c8a71aa642a2b5bc064c6b8885ac096bfc31a11f1f` | [下载](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/partition-table.bin) |
| `ota_data_initial.bin` | `0x86000` | 8.00 KiB | `7d2c7ac4888bfd75cd5f56e8d61f69595121183afc81556c876732fd3782c62f` | [下载](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/ota_data_initial.bin) |
| `reterminal_template.bin` | `0x90000` | 2.80 MiB | `12b868fc231228271bbf3f008c671cd030063992808c423b61bc8ca60161d732` | [下载](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/reterminal_template.bin) |
| `sys_storage.bin` | `0xC90000` | 9.19 MiB | `85c642467579081944e26579aed1ff96c70e79f3d1d868374c502b41896e0191` | [下载](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/sys_storage.bin) |
| `usr_storage.bin` | `0x15C0000` | 10.00 MiB | `ea729c22a9796bec404bf06d7ef063f74ca15fd854d13a1d8512f5d92b7dad28` | [下载](https://github.com/Seeed-Projects/OSHW-reTerminal-Sticky/releases/download/firmware-official-v0.2.1/usr_storage.bin) |

```bash
esptool.py --chip esp32s3 -p PORT -b 921600 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m \
  0x0 bootloader.bin \
  0x8000 partition-table.bin \
  0x86000 ota_data_initial.bin \
  0x90000 reterminal_template.bin \
  0xC90000 sys_storage.bin \
  0x15C0000 usr_storage.bin
```

</details>

## 命令行烧录参考（`esptool.py`）

### 单文件整包烧录（`v1.2.0` 及 `v0.3.3+`）

单文件合并镜像从 `0x0` 地址起始写入。若设备此前刷入过社区固件或第三方固件，恢复官方出厂固件前可先执行整片擦除以清理旧分区数据：

```bash
# Optional: full erase before restoring factory firmware
esptool.py --chip esp32s3 -p PORT erase_flash

# Flash official merged firmware (v1.2.0)
esptool.py --chip esp32s3 -p PORT -b 460800 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 32MB --flash_freq 80m \
  0x0 reterminal_sticky_1_2_0.bin
```

烧录前可在本地核对文件完整性：

```bash
shasum -a 256 -c SHA256SUMS.txt
```

<!-- END OFFICIAL_FIRMWARE_CATALOG -->

## 目录结构与自动同步说明

```text
firmware/
├── factory/
│   └── versions.json    # 机器可读的版本元数据、烧录偏移与 SHA-256 索引
├── README.md
└── README-ZH.md
```

本目录及本仓库 Releases 中的官方固件由 [`.github/workflows/sync-official-firmware.yml`](../.github/workflows/sync-official-firmware.yml) 自动从 [`Seeed-Projects/reterminal-sticky-playground-registry`](https://github.com/Seeed-Projects/reterminal-sticky-playground-registry/tree/main/firmwares/sticky-factory) 实时同步更新。
