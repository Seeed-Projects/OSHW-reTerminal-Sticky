# reTerminal Sticky 开源硬件资料

[English](README.md) | [仓库首页](../README-ZH.md)

本目录存放 Seeed Studio reTerminal Sticky 的开源硬件原理图、结构 3D 模型及相关硬件参考资料。

## 已收录资源

| 资源 | 路径 / 链接 | 说明 |
| --- | --- | --- |
| **原理图（PDF）** | [`schematics/reTerminal_Sticky_Schematic_diagram_260609.pdf`](schematics/reTerminal_Sticky_Schematic_diagram_260609.pdf) | 官方电路原理图，版本 `V01`（`2026-06-05`，共 10 页，`CC BY-SA 4.0`） |
| **官方 3D 模型（STEP）** | [`mechanical/reTerminal_Sticky_3D.stp`](mechanical/reTerminal_Sticky_3D.stp) | 官方整机结构 CAD 模型（`ISO-10303-21` STEP 格式，`2026-10-26`） |
| **3D 打印外壳与支架** | [Seeed Studio Sticky Playground](https://www.seeedstudio.com/sticky/playground/3d-printables/) | 官方与社区 3D 打印外壳、挂架及桌面支架合集页面 |

固件实测引脚与总线定义请参阅 [`examples/esp-idf/peripherals/main/pin_config.h`](../examples/esp-idf/peripherals/main/pin_config.h)。

## 目录结构

```text
hardware/
├── schematics/                                         # 原理图 PDF 与 EDA 设计源文件
│   └── reTerminal_Sticky_Schematic_diagram_260609.pdf  # 官方 V01 原理图（10 页）
├── mechanical/                                         # 3D 外壳与配件结构文件（.stp / .3mf / .stl）
│   └── reTerminal_Sticky_3D.stp                        # 官方整机 3D 模型
├── pcb/                                                # 规划中：PCB 版图参考、丝印位号图与 BOM 清单
└── datasheets/                                         # 规划中：关键芯片与屏幕模组数据手册
```

## 组织与命名约定

- 硬件资料按硬件版本号或官方发布日期标识归档命名（例如 `v1.0/` 或与官方发布包一致的日期后缀）。
- 后续硬件版本更新附带纯文本变更记录，说明电气或结构调整点。
- 本目录下的开源硬件资料遵循各自声明的硬件开源许可证（官方原理图图框标明采用 **CC BY-SA 4.0** 协议）。
