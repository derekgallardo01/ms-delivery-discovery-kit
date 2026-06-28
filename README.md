# Microsoft delivery — discovery & scoping kit

[![CI](https://github.com/derekgallardo01/ms-delivery-discovery-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/derekgallardo01/ms-delivery-discovery-kit/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#)

**Docs:** [Getting started](docs/getting-started.md) · [Usage](docs/usage.md) · [Diagrams](docs/diagrams.md) · [FAQ](docs/faq.md)

A reusable kit for the first phase of any Microsoft / Power Platform
engagement: a structured **discovery questionnaire** that surfaces
requirements, constraints, and risks up front, and a **statement-of-work
template** that turns the answers into a clear, agreed scope. Ships with a
fully worked example and a placeholder linter so half-finished SOWs don't
reach a client.

```bash
python validate.py                                     # check examples/ are fully filled in
python validate.py sow-greenfield-logistics.md         # check your draft before sending
python -m pytest -q                                    # 2 tests gating the kit
```

## Why it exists

Most Microsoft projects that go sideways do so because scope was never
pinned down — data sources, permissions, success criteria, and who-does-what
were assumed rather than agreed. Running a real discovery before quoting
prevents that, and it signals to a client that you work like a consultant,
not an order-taker.

## What's inside

| File | Purpose |
|------|---------|
| [discovery-questionnaire.md](discovery-questionnaire.md) | Structured questions covering goals, current state, data/systems, users, security/compliance, and success criteria. |
| [sow-template.md](sow-template.md) | A statement-of-work template: scope, deliverables, assumptions, out-of-scope, timeline, and acceptance. |
| [examples/discovery-greenfield-logistics.md](examples/discovery-greenfield-logistics.md) | A completed discovery for a fictional logistics SMB (Asana → SharePoint sync). |
| [examples/sow-greenfield-logistics.md](examples/sow-greenfield-logistics.md) | The corresponding SOW derived from those answers. |
| [validate.py](validate.py) | Placeholder linter — checks for unfilled `<…>` markers. Run it on your draft before sending. |
| [tests/](tests/) | Self-tests: examples must validate clean; bare templates must still look like templates. |
| [docs/usage.md](docs/usage.md) | Step-by-step usage + how to customize the kit. |

## How to use it

1. Send (or walk through) [discovery-questionnaire.md](discovery-questionnaire.md)
   at kickoff. Save the answers as `discovery-<client>.md`.
2. Fill [sow-template.md](sow-template.md) from the answers — including an
   explicit out-of-scope list and observable acceptance criteria. Save as
   `sow-<client>.md`.
3. Run `python validate.py sow-<client>.md` before sending to catch unfilled
   placeholders.
4. Get sign-off before building. The out-of-scope and acceptance sections are
   what protect both sides later.

[docs/usage.md](docs/usage.md) walks the process end-to-end with the worked
example, and covers how to extend the questionnaire / SOW per industry.
