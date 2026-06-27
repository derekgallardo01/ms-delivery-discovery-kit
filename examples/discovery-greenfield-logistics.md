# Discovery questionnaire — Greenfield Logistics

*Worked example. A fictional 20-person logistics SMB whose dispatch lives in
Asana and whose ops team works from SharePoint. The brief is a daily sync of
approved jobs from Asana into a SharePoint list.*

## 1. Outcome
- **In one sentence:** every morning at 6:00 AM AEST, every job approved in the
  Asana "Dispatch" board the previous day is visible as a row in the SharePoint
  "Deliveries" list, with no duplicates and no manual copying.
- **Success in numbers:** saves the ops coordinator ~30 minutes per day
  (130 hours/year); zero missed jobs in spot-check audits over the first month.
- **End user:** Cara Naidoo (ops coordinator). Comfortable with SharePoint
  list filtering. Not a developer.

## 2. Current state
- **Today:** Cara opens Asana each morning, filters the Dispatch board to "approved
  yesterday", copies columns (Job ID, Customer, Pickup, Drop, Driver, Window)
  into the SharePoint list one row at a time.
- **Trigger:** manual; happens whenever she logs in.
- **Data flow:** Asana Dispatch project → manual paste → SharePoint Deliveries
  list (site: `/sites/ops`, list ID known).
- **Tried before:** an intern wrote an Excel macro that pulled the Asana CSV
  export; it broke when Asana added a column and nobody noticed for three days.

## 3. Systems & data
- **Platforms:** Asana (business plan, API access available), Microsoft 365 E3
  (SharePoint Online, Power Automate per-user plan for Cara), no Azure subscription.
- **Volume:** ~25–60 jobs/day; roughly 1,500/month.
- **Sensitive data:** customer names + addresses (PII). No financial or health
  data. Subject to Australian Privacy Principles (APPs).
- **Sample:** Cara has shared a 7-day Asana export (CSV) and a screenshot of the
  current SharePoint list with 5 sample rows.

## 4. Access & constraints
- **Sandbox:** yes — separate `/sites/ops-sandbox` site already provisioned;
  Cara is site owner.
- **Connectors:** Asana premium connector is licensed under Cara's Power
  Automate plan. SharePoint connector built-in.
- **Must-use:** Power Automate (already paid for; they don't want a third-party
  iPaaS).
- **Must-not-use:** anything that exports PII to a non-Microsoft / non-Asana
  service.
- **Deadline:** working in sandbox by 2026-07-22; production by 2026-08-05
  (before Cara's annual leave).
- **Budget ceiling:** AUD 6,000 (incl. GST) for the build.

## 5. Scope & handover
- **One-time or ongoing:** one-time build. No monthly retainer for now.
- **Maintainer:** Cara (with my help in the 14-day post-handover support window).
- **Documentation:** non-developer-readable handover guide + a 3–5 min walkthrough
  video. Cara needs to be able to change the schedule and add/remove notification
  recipients herself.
- **Explicitly out of scope:** any change to the Asana board structure, custom
  SharePoint columns beyond the existing six, two-way sync (writes only go
  Asana → SharePoint, never the reverse), reporting / Power BI dashboard on top
  of the data.
