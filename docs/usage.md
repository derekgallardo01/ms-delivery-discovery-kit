# Usage

How to actually use this kit on a live engagement.

## Step 1 — Run the discovery questionnaire

Either send `discovery-questionnaire.md` to the prospect before the kickoff
call, or walk through it live and take notes inline. Either way the file
that comes back is the answers; commit it (or save it locally) as
`discovery-<client>.md`. See [examples/discovery-greenfield-logistics.md](../examples/discovery-greenfield-logistics.md)
for what a completed one looks like.

**Why answer every question in §4 (Access & constraints) before quoting:**
that section is where the hidden blockers live — sandbox availability,
connector licensing, must-not-use tools, hard deadlines. A SOW written
without those answers is a SOW you'll have to amend.

## Step 2 — Turn the answers into a SOW

Copy `sow-template.md` to `sow-<client>.md`. Fill it in from the discovery
answers, keeping each section tight. The worked example
[examples/sow-greenfield-logistics.md](../examples/sow-greenfield-logistics.md)
shows the level of specificity that actually protects both sides:

- **Out of scope** lists concrete things, not "anything not in section 2".
- **Acceptance criteria** are observable — "3 consecutive days passing", not
  "works correctly".
- **Milestones** have dates and outputs, not just labels.
- **Assumptions** name the access the client owes you and by when.

## Step 3 — Validate before sending

```bash
python validate.py path/to/sow-greenfield-logistics.md
```

The linter flags angle-bracket placeholders like `<client>` or `<date>` that
slipped through. Run it on every SOW before sending — half-finished
templates leaking to a client is the most preventable bad first impression.

`python validate.py` with no arguments checks every file under `examples/`
— that's the self-test that keeps the worked examples honest as the
templates evolve.

## Customizing the kit

### Adding a new question to the questionnaire

Edit `discovery-questionnaire.md`. The section structure (Outcome → Current
state → Systems & data → Access & constraints → Scope & handover) was chosen
because it maps 1:1 to the SOW sections; if you reorder the questionnaire,
reorder the SOW headings too so the flow from answers → SOW stays trivial.

### Adding a SOW section

Edit `sow-template.md`. Useful additions per industry:
- **Data-processing addendum** for clients with GDPR / APP obligations.
- **IP / source-code ownership** when the client wants their build under
  source control they own.
- **SLA** for ongoing-support engagements (not one-time builds).

After adding, run validate on the bare template — it should still emit
placeholders for any field you expect the user to fill (otherwise the new
section is silently optional).

### Adding a new worked example

Copy your engagement's SOW + discovery into `examples/` under a non-real
client name. Run validate — it should pass clean. Add a couple of lines to
`tests/test_validate.py` so the new example is regression-tested.

## What this kit is not

- **Not a contract.** Pair the SOW with your master services agreement
  (jurisdiction, indemnities, liability cap, IP, termination).
- **Not a project plan.** The milestones are commercial; a project plan
  lives in a separate doc with actual tasks/days.
- **Not industry-specific.** The questionnaire is intentionally generic. Add
  industry-specific sections (e.g. "data subject rights" for healthcare)
  per engagement.
