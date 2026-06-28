# Discovery questionnaire — Whitford Legal

*Worked example. A fictional mid-sized corporate law firm (60 lawyers + 40
support) deploying a Copilot Studio agent over their firm's internal
knowledge base (policies, precedent library, billing procedures) for partner
and associate use via Microsoft Teams.*

## 1. Outcome
- **In one sentence:** partners and associates can ask plain-English questions
  in Teams ("What's our standard NDA carve-out for IP?", "What's the markup
  on disbursements?") and get a cited answer from the firm's internal
  knowledge base in seconds, with sensitive matters (active client questions)
  routed to a senior associate.
- **Success in numbers:** reduce repeat-question load on senior associates by
  60% over 90 days (measured by a sampled survey + Copilot Studio's analytics);
  zero answers cited from outside the approved knowledge sites in the eval set.
- **End user:** lawyers across two offices (San Francisco + London). Mixed
  technical comfort; the agent must work without training a typical lawyer.

## 2. Current state
- **Today:** the firm's internal SharePoint has 500+ policy and precedent
  documents. Search is "OK but not great" — keyword-only, no semantic
  ranking, no citation surface. Juniors DM seniors with the same
  questions repeatedly, especially on billing procedures and NDA standards.
- **Trigger:** lawyer types a question in Teams or a SharePoint search box.
- **Data flow today:** SharePoint search → result list → user opens doc → ctrl-F.
- **Tried before:** a junior associate spent a week building a custom search
  page with Power Apps. It indexed only one library and was abandoned.

## 3. Systems & data
- **Platforms:** Microsoft 365 E5 (firm-wide), Copilot Studio licenses for 100
  named users, SharePoint Online (three target sites: `/policies`,
  `/precedents`, `/billing-procedures`). Teams as the surface. No Azure
  OpenAI subscription yet; willing to add one for the pilot.
- **Volume:** ~500 documents at pilot start, growing ~30/month.
- **Sensitive data:** documents reference real clients and matter numbers
  (privileged information). The agent must never quote outside the approved
  sites. Active-client questions need to escalate, never be answered.
- **Sample:** firm has shared a 25-question test set drafted by the
  knowledge-management partner.

## 4. Access & constraints
- **Sandbox:** yes — `whitford-pilot.onmicrosoft.com` tenant provisioned,
  pre-seeded with 30 sample docs.
- **Connectors:** Copilot Studio + SharePoint connectors licensed. Azure
  OpenAI will be enabled in a new resource group `wlf-aoai-pilot`.
- **Must-use:** Microsoft 365 + Azure (no third-party LLMs).
- **Must-not-use:** no public-model training of any kind; no document
  egress outside the tenant; no exposure of client/matter names in logs.
- **Deadline:** sandbox demo to partners by **2026-08-15**; production go-live
  by **2026-09-30** (firm-wide associate refresh starts October).
- **Budget ceiling:** USD 40,000 (incl. eval-set build and 30 days of
  post-go-live support).

## 5. Scope & handover
- **One-time or ongoing:** initial pilot is one-time. If adoption hits >70%
  of associates monthly active, the firm will re-engage for site expansion
  in Q1.
- **Maintainer:** the KM partner + IT lead (with my support for the first
  30 days post-go-live).
- **Documentation:** non-developer-readable handover for the IT lead; the
  KM partner gets a 5-min walkthrough video. The eval-set must transfer
  ownership too — the KM partner will own the golden set after handover.
- **Explicitly out of scope:** expansion beyond the three named sites,
  matter-specific knowledge ingestion, billing-system integration,
  fine-tuning on firm content, multi-language (English only for now).
