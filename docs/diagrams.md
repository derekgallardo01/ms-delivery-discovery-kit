# Diagrams

This is a templates kit, not a runnable system — the diagrams here are
about how the templates fit into an engagement, not about code paths.

## 1. The engagement flow this kit covers (and what comes after)

```mermaid
flowchart LR
    L["Inbound lead<br/>(Upwork message,<br/>referral, intro)"] --> SC["1-hr paid scoping call"]
    SC --> DQ["Discovery questionnaire<br/>(this kit)"]
    DQ --> SOW["Statement of work<br/>(this kit)"]
    SOW --> SIGN{"Signed?"}
    SIGN -- "no" --> RENEG["Renegotiate or walk"]
    SIGN -- "yes" --> HLD["HLD<br/>(solution-architecture-hld kit)"]
    HLD --> BUILD["Build<br/>(against agreed acceptance criteria)"]
    BUILD --> ACC["Acceptance<br/>(eval set + UAT)"]
    ACC --> HO["Handover<br/>(project-handover-pack kit)"]
    HO --> SUP["Post-go-live support window<br/>(per SOW §8)"]
    SUP --> DONE["Engagement closed"]
```

The discovery + SOW kit covers the first two steps after the scoping
call. The other kits cover later phases — the cross-links keep the
narrative continuous.

## 2. Sections of the questionnaire → sections of the SOW

```mermaid
flowchart LR
    subgraph DQ["Discovery questionnaire"]
      Q1["§1 Outcome"]
      Q2["§2 Current state"]
      Q3["§3 Systems & data"]
      Q4["§4 Access & constraints"]
      Q5["§5 Scope & handover"]
    end

    subgraph SOW["Statement of work"]
      S1["§1 Objective"]
      S2["§2 In scope"]
      S3["§3 Out of scope"]
      S4["§4 Deliverables & acceptance"]
      S5["§5 Milestones"]
      S6["§6 Assumptions"]
    end

    Q1 --> S1
    Q1 --> S4
    Q2 --> S2
    Q3 --> S2
    Q3 --> S6
    Q4 --> S5
    Q4 --> S6
    Q5 --> S2
    Q5 --> S3
```

## 3. SOW lifecycle — version control

```mermaid
stateDiagram-v2
    [*] --> Draft: copy sow-template.md
    Draft --> Linting: python validate.py sow-X.md
    Linting --> Draft: placeholders found, fix
    Linting --> Ready: validator passes (exit 0)
    Ready --> ClientReview: shared with client
    ClientReview --> Draft: changes requested
    ClientReview --> Signed: agreed
    Signed --> InFlight: build starts
    InFlight --> Amended: change request triggers §7
    Amended --> Signed: amendment signed
    InFlight --> Accepted: milestone criteria met
    Accepted --> [*]
```

The validator gate exists for one reason: leftover `<placeholder>`
markers from the template are the #1 unforced error when sending SOWs
under time pressure. The validator catches them automatically.

## 4. Two worked engagements at a glance

```mermaid
flowchart LR
    subgraph GL["Greenfield Logistics"]
      G1["20-person SMB"]
      G2["Asana → SharePoint sync"]
      G3["Fixed price AUD 4,800"]
      G4["3 milestones, 4 weeks"]
    end
    subgraph WL["Whitford Legal"]
      W1["60-lawyer firm"]
      W2["Copilot Studio agent over knowledge base"]
      W3["Fixed price USD 36,000"]
      W4["4 milestones, 12 weeks"]
    end
    GL --> SOW1["sow-greenfield-logistics.md"]
    WL --> SOW2["sow-whitford-legal.md"]
```

The two worked examples in [`examples/`](../examples/) bracket the
typical SMB / mid-market range. Your engagement will fit somewhere on
that spectrum.
