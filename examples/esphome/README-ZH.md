# reTerminal Sticky ESPHome 配置模板

[English](README.md) | [示例总览](../README-ZH.md) | [仓库首页](../../README-ZH.md)

> **当前状态：** 规划中。当前可立即编译运行的原生固件示例请参阅 [`examples/esp-idf/`](../esp-idf/README-ZH.md)。

本目录用于存放面向 Seeed Studio reTerminal Sticky 的 **ESPHome** YAML 配置模板、自定义组件引用及 Home Assistant 接入示例。

## 规划目录结构

```text
examples/esphome/
├── common/              # 可复用的板级公共配置（引脚、I2C/SPI 总线、按键）
├── dashboard/           # 开箱即用的 Home Assistant 电子纸看板 YAML
└── secrets.yaml.example # 脱敏的 Wi-Fi 与 API 凭据配置模板
```

## 配置约定

- 无线网络密码、API 密钥与 OTA 凭据统一提供脱敏模板 `secrets.yaml.example`，真实凭据保存在本地未追踪文件中。
- 每套配置在对应 `README.md` 中注明已验证的 ESPHome 版本、底层框架类型及支持的电子纸控制器型号（SSD1677 / SSD2677）。
- 引脚与总线定义参考 [`examples/esp-idf/peripherals/main/pin_config.h`](../esp-idf/peripherals/main/pin_config.h)。
