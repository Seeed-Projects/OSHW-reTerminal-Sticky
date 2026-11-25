# reTerminal Sticky Community Projects

[简体中文](README-ZH.md) | [Examples Overview](../README.md) | [Repository Home](../../README.md)

> **Status:** Open for community submissions.

This directory collects community-contributed applications, widgets, and hardware hacks built for Seeed Studio reTerminal Sticky.

## Planned Layout

```text
examples/community/
└── <project-name>/
    ├── README.md        # Overview, screenshots/photos, build & flash steps
    ├── LICENSE          # Project license (or reference to repository MIT license)
    └── ...              # Project source files
```

## Submission Checklist

Each community project lives in its own kebab-case subdirectory (`examples/community/<project-name>/`) and includes:

1. A `README.md` covering functionality, required SDK/framework version, build and flash commands, and known hardware requirements.
2. Clear attribution and license information (including third-party assets or fonts).
3. Hardware pin usage aligned with [`examples/esp-idf/peripherals/main/pin_config.h`](../esp-idf/peripherals/main/pin_config.h).
