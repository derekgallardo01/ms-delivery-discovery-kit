# Statement of Work — Greenfield Logistics: Asana → SharePoint daily sync

**Client:** Greenfield Logistics Pty Ltd · **Prepared by:** Derek G. · **Date:** 2026-07-08 · **Version:** 1.0

## 1. Objective
Replace the daily manual copy of approved dispatch jobs from Asana into the
SharePoint "Deliveries" list with a scheduled Power Automate flow, eliminating
~30 minutes of ops-coordinator time per day and the risk of missed/duplicated
jobs.

## 2. In scope
- One Power Automate flow (scheduled daily at 06:00 AEST) reading the Asana
  "Dispatch" project via the Asana premium connector.
- Field mapping (six columns: Job ID, Customer, Pickup, Drop, Driver, Window)
  with idempotent upsert into the SharePoint "Deliveries" list, deduped on Job ID.
- Run log (in-flow + a SharePoint "Sync Log" list) with email notification on
  failure to a configurable distribution list.
- One round of testing in the `/sites/ops-sandbox` site, then promotion to the
  production `/sites/ops` site.
- Handover pack: handover guide, runbook, 3–5 min Loom walkthrough.

## 3. Out of scope
*(Anything not listed in section 2. Naming these explicitly prevents scope creep.)*
- Any change to the Asana Dispatch board structure (columns, custom fields,
  workflows).
- Custom SharePoint columns beyond the existing six on the "Deliveries" list.
- Two-way sync — writes go Asana → SharePoint only, never the reverse.
- Reporting / Power BI dashboards on top of the data.
- Asana or Microsoft 365 license procurement.
- Ongoing maintenance after the 14-day post-handover support window.

## 4. Deliverables & acceptance
| Deliverable | Acceptance criteria (how we agree it's "done") |
|-------------|------------------------------------------------|
| Power Automate flow (sandbox) | Runs on schedule against the sandbox site; correctly maps all six columns; zero duplicates on 3 consecutive daily runs with overlapping inputs; failure email lands when the source is unavailable. |
| Power Automate flow (production) | As above, but pointing at `/sites/ops` Deliveries list; passes the same acceptance criteria for 5 consecutive business days. |
| Handover guide | Written so a non-developer can answer: where the flow lives, how to check it ran, how to add a recipient, how to pause it, who to contact. |
| Loom walkthrough | 3–5 min, recorded with Cara's actual SharePoint view; uploaded; link in the handover guide. |

## 5. Milestones
| # | Milestone | Output | Target |
|---|-----------|--------|--------|
| 1 | Build on sample data in sandbox | flow runs end-to-end against the supplied 7-day Asana export | 2026-07-15 |
| 2 | Validate with real data + sign-off in sandbox | 5 consecutive sandbox days passing acceptance | 2026-07-22 |
| 3 | Promote to production + handover | flow live in `/sites/ops`; docs + walkthrough delivered | 2026-08-05 |

## 6. Assumptions
- Client provides Cara's Power Automate (per-user) account with Asana
  connector authorized, and grants me a guest account with site-owner access
  to `/sites/ops-sandbox` by **2026-07-10**.
- The Asana "Dispatch" project structure and column names will not change
  during the engagement; if they do, see §7.
- One round of revisions per milestone is included; further changes follow §7.

## 7. Change process
Any work outside §2 is quoted separately and added by written agreement before
work proceeds. Indicative hourly rate for change requests: AUD 180/hr.

## 8. Commercials
- **Type:** fixed-price · **Amount:** AUD 4,800 + GST (10%)
- **Payment:** 50% on signature (AUD 2,640 incl. GST); 50% on production
  acceptance at Milestone 3 (AUD 2,640 incl. GST).
- **Support window:** 14 calendar days from production acceptance, covering
  defect fixes and questions on documented use of the solution.

_Signed:_ Client ___________  Date _______  ·  Freelancer ___________  Date _______
