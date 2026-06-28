# Getting started

The kit's whole job is to make the first phase of a Microsoft / Power
Platform engagement repeatable. Here's how a typical engagement uses it.

## 1. Send (or run) the discovery questionnaire at kickoff

Either email [`discovery-questionnaire.md`](../discovery-questionnaire.md)
ahead of the kickoff call, or walk through it live and capture the
answers inline. Save the answers as `discovery-<client>.md`.

**Don't skip §4 (Access & constraints).** That section is where the
hidden blockers live — sandbox availability, connector licensing,
must-not-use tools, hard deadlines. A SOW written without those answers
is a SOW you'll have to amend later.

## 2. Turn the answers into a SOW

Copy [`sow-template.md`](../sow-template.md) to `sow-<client>.md`. Fill
it from the discovery answers, keeping each section tight. The worked
examples
([Greenfield Logistics](../examples/sow-greenfield-logistics.md) /
[Whitford Legal](../examples/sow-whitford-legal.md)) show the level of
specificity that protects both sides:

- **Out of scope** lists *concrete* things, not "anything not in §2".
- **Acceptance criteria** are observable — "3 consecutive days passing",
  not "works correctly".
- **Milestones** have dates and outputs, not just labels.
- **Assumptions** name the access the client owes you and by when.

## 3. Validate before sending

```bash
python validate.py sow-<client>.md
```

The linter catches unfilled `<…>` placeholders. Run it on every SOW
before sending — leftover template markers are the single most
preventable bad first impression.

## 4. Get sign-off, then build

The out-of-scope and acceptance sections are what protect both sides
later. Don't start building without sign-off — even a one-line email
"agreed, proceed" against the named SOW version.

## See it end-to-end on a worked example

[`examples/discovery-greenfield-logistics.md`](../examples/discovery-greenfield-logistics.md)
→ [`examples/sow-greenfield-logistics.md`](../examples/sow-greenfield-logistics.md)
shows the full chain: a fictional logistics SMB asks for an Asana →
SharePoint sync, the answers become a fixed-price SOW with explicit
out-of-scope and acceptance criteria.

For a different engagement shape (Copilot Studio rollout),
[`examples/discovery-whitford-legal.md`](../examples/discovery-whitford-legal.md)
→ [`examples/sow-whitford-legal.md`](../examples/sow-whitford-legal.md).

## What to read next

- [Usage](usage.md) · [Diagrams](diagrams.md) · [FAQ](faq.md)
