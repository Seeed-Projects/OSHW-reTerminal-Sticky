# reTerminal Sticky 社区项目

[English](README.md) | [示例总览](../README-ZH.md) | [仓库首页](../../README-ZH.md)

> **当前状态：** 欢迎社区开发者提交作品。

本目录用于收录社区开发者基于 Seeed Studio reTerminal Sticky 制作的开源应用、小组件与创意项目。

## 规划目录结构

```text
examples/community/
└── <project-name>/
    ├── README.md        # 功能简介、效果图、编译与烧录步骤
    ├── LICENSE          # 项目许可证（或沿用仓库根 MIT 许可证）
    └── ...              # 项目源码与资源文件
```

## 投稿约定

每个社区项目以全小写短横线命名独立目录（`examples/community/<project-name>/`），包含以下内容：

1. 一份 `README.md`，说明项目功能、所需开发框架及版本、构建烧录步骤与硬件版本要求。
2. 清晰的作者署名、开源协议说明及第三方字体或素材版权声明。
3. 引脚定义与 [`examples/esp-idf/peripherals/main/pin_config.h`](../esp-idf/peripherals/main/pin_config.h) 保持一致。
