# Statement of Work — Whitford Legal: Copilot Studio knowledge agent

**Client:** Whitford Legal LLP · **Prepared by:** Derek G. · **Date:** 2026-08-01 · **Version:** 1.0

## 1. Objective
Deploy a Copilot Studio agent in Microsoft Teams that lets partners and
associates ask plain-English questions of the firm's internal knowledge base
(Policies, Precedents, Billing Procedures), with every answer carrying a
citation to the source document and active-client questions routed to an
assigned senior associate rather than answered.

## 2. In scope
- One Copilot Studio agent connected to the three SharePoint knowledge sites
  (`/sites/policies`, `/sites/precedents`, `/sites/billing-procedures`).
- Multi-turn conversation with conversation context window of three turns.
- Source-cited answers (document title + section link in the chat reply).
- Sensitive-topic escalation: any question mentioning an active client name,
  matter number, or the configured sensitive-topic list routes to an
  on-call senior associate via Teams DM instead of being answered.
- An 80-case golden eval set co-authored with the KM partner, with the
  associated CI gate so post-handover changes don't regress.
- Microsoft Teams as the delivery surface (web + desktop + mobile).
- Production cutover on 2026-09-30 plus 30 days of post-go-live support.

## 3. Out of scope
*(Anything not listed in §2. Naming these explicitly prevents scope creep.)*
- Expansion of the agent to any SharePoint site outside the three named in §2.
- Matter-specific knowledge ingestion (matter files stay outside the agent).
- Integration with the billing system, time-recording, or any case-management
  software.
- Fine-tuning a foundation model on firm content (only retrieval grounding).
- Multi-language; English-only at launch.
- Licensing or procurement of Copilot Studio / Azure OpenAI seats.

## 4. Deliverables & acceptance
| Deliverable | Acceptance criteria (how we agree it's "done") |
|-------------|------------------------------------------------|
| Copilot Studio agent (sandbox) | Answers all 80 eval-set questions with the expected source document; sensitive-topic and active-client cases escalate, never answer. |
| Copilot Studio agent (production) | Same eval set passes 100% in production; analytics shows ≥5 named users running ≥10 queries each in the first week. |
| Eval-set documentation | KM partner can add a new case and run the eval against the production agent without my involvement. |
| Handover pack | Handover guide, runbook, 3–5 min Loom walkthrough recorded by me with the KM partner watching. |

## 5. Milestones
| # | Milestone | Output | Target |
|---|-----------|--------|--------|
| 1 | Sandbox build + 30-case eval green | working agent in `whitford-pilot.onmicrosoft.com` | 2026-08-15 |
| 2 | Full 80-case eval green; sensitive-topic policy signed off by KM partner | green CI badge + signed memo | 2026-09-08 |
| 3 | Production cutover; first 50 users onboarded | live in `whitfordlegal.onmicrosoft.com`; analytics enabled | 2026-09-30 |
| 4 | Handover + 30-day support window closes | handover pack delivered; final review | 2026-10-30 |

## 6. Assumptions
- Whitford Legal provides me a guest account with site-owner on the three
  sandbox sites and read access to the production equivalents by **2026-08-04**.
- The Azure OpenAI subscription (`wlf-aoai-pilot`) is provisioned and approved
  for "no content filtering modifications" / no-retention option by Microsoft
  by **2026-08-08**.
- Privacy and data-handling configuration (separate `m365-privacy-config`
  engagement) is completed and signed off before production cutover.
- One round of revisions per milestone is included; further changes follow §7.

## 7. Change process
Any work outside §2 is quoted separately and added by written agreement before
work proceeds. Indicative hourly rate for change requests: USD 220/hr.

## 8. Commercials
- **Type:** fixed-price · **Amount:** USD 36,000 + applicable tax
- **Payment:** 25% on signature; 35% at Milestone 2; 40% at Milestone 3.
- **Support window:** 30 calendar days from production cutover, covering
  defect fixes and questions on documented use of the solution.

_Signed:_ Client ___________  Date _______  ·  Freelancer ___________  Date _______
