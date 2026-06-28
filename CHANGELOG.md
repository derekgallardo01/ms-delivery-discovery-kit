# Changelog

Notable changes to the Microsoft delivery discovery & scoping kit. Dates are
when the change landed on `main`.

## 2026-06-27 — Second worked engagement (Whitford Legal)
- `examples/discovery-whitford-legal.md` — completed discovery for a
  fictional mid-sized law firm deploying a Copilot Studio agent over their
  internal knowledge base
- `examples/sow-whitford-legal.md` — matching SOW with milestones, eval-set
  ownership transfer, sensitive-topic escalation, USD pricing
- `tests/test_validate.py` extended to cover the new examples

## 2026-06-27 — GitHub Actions CI
- `.github/workflows/ci.yml` running pytest + validate on Python 3.11
- CI status badge added to README

## 2026-06-27 — Build-out: worked example + linter + tests + usage doc
- `examples/discovery-greenfield-logistics.md` + `examples/sow-greenfield-logistics.md`
  — fully completed discovery + SOW for a fictional logistics SMB
- `validate.py` placeholder linter; checks `examples/` by default, takes a
  file path for ad-hoc draft checks
- 2 tests asserting examples validate clean and bare templates still look
  like templates
- `docs/usage.md` — step-by-step usage + per-engagement customization
- README expanded with usage steps, file index, link to docs/usage.md

## 2026-06-27 — Initial public release
- `discovery-questionnaire.md` — structured questions covering goals,
  current state, data/systems, users, security/compliance, success criteria
- `sow-template.md` — statement-of-work template (scope, deliverables,
  assumptions, out-of-scope, timeline, acceptance, commercials)
