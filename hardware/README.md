# reTerminal Sticky Open-Source Hardware Files

[简体中文](README-ZH.md) | [Repository Home](../README.md)

This directory contains Seeed Studio reTerminal Sticky open-source hardware design files, mechanical CAD models, and related hardware references.

## Available Resources

| Resource | Path / Link | Details |
| --- | --- | --- |
| **Schematic (PDF)** | [`schematics/reTerminal_Sticky_Schematic_diagram_260609.pdf`](schematics/reTerminal_Sticky_Schematic_diagram_260609.pdf) | Official circuit schematic, Rev `V01` (`2026-06-05`, 10 pages, `CC BY-SA 4.0`) |
| **Official 3D Model (STEP)** | [`mechanical/reTerminal_Sticky_3D.stp`](mechanical/reTerminal_Sticky_3D.stp) | Official enclosure & assembly CAD model (`ISO-10303-21` STEP, `2026-10-26`) |
| **3D-Printable Cases & Stands** | [Seeed Studio Sticky Playground](https://www.seeedstudio.com/sticky/playground/3d-printables/) | Online gallery of 3D-printable enclosures, mounts, and desk stands |

For verified GPIO and bus assignments used in firmware, see [`examples/esp-idf/peripherals/main/pin_config.h`](../examples/esp-idf/peripherals/main/pin_config.h).

## Directory Layout

```text
hardware/
├── schematics/                                         # Schematic PDFs and EDA source files
│   └── reTerminal_Sticky_Schematic_diagram_260609.pdf  # Official Rev V01 schematic (10 pages)
├── mechanical/                                         # 3D enclosure & accessory files (.stp, .3mf, .stl)
│   └── reTerminal_Sticky_3D.stp                        # Official 3D assembly model
├── pcb/                                                # Planned: PCB layout references, silkscreen maps, BOM
└── datasheets/                                         # Planned: Key IC and panel datasheets
```

## Organization Conventions

- Version hardware packages explicitly by PCB or mechanical revision (for example, `v1.0/` or date-stamped filenames matching official releases).
- Pair updated binary design outputs (`.stp`, `.pdf`) with concise plain-text revision notes summarizing electrical or mechanical changes.
- Open-source hardware files follow their declared hardware licenses (the official schematic PDF is licensed under **CC BY-SA 4.0**, as noted in its title block).
