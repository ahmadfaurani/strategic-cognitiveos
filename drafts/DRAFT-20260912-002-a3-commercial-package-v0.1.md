# DRAFT-20260912-002 — A3 Commercial Package v0.1 (VoronCitadel)

**Status:** DRAFT v0.1 — for DAF markup (pricing authority) + Fuad technical-scope confirmation
**Gate:** A3 Commercial Packaging (`governance/AIP-PRODUCTIZATION-OPERATIONALIZATION.md`) — deadline was Sep 5, day 7+ overdue
**Exit criterion:** pricing sheet + POC template + SLA terms documented; ready for CSM to quote
**Sources:** DOC-20260908-004 (chain:SENTRY Cost Centre Plan v1.0 — verified cost baseline), DOC-20260825-001 (VoronCitadel Delivery Readiness Framework), GTM pricing envelope (MEMORY.md §4)
**Feeds:** CSM funnel v3; Sep 15 GTM lock-in; CyberDSA quoting window

---

## Part 1 — Pricing Sheet (v0.1)

### 1.1 PoC — 90-day engagement

| Component | Cost floor (DOC-20260908-004, vendor-verified 6 Sep) | Quote band |
|---|---|---|
| Non-people run rate | USD 331–1,277/month → USD 993–3,831 over 90 days | TBD (DAF margin call) |
| Pentest (optional line) | USD 3,500–15,000 | TBD — inside base price or option? |
| **PoC envelope (all-in)** | **USD 993–18,881** (approval rec. USD 19,000; USD ~4,000 if pentest deferred in writing) | TBD |
| People component | MYR 100k–150k/month (7-FTE envelope ≈ USD 24.7k–37.1k) — allocate per-engagement, not per-client | TBD allocation rule |

### 1.2 Beta — monthly recurring (non-people)

| Item | Cost floor | Quote band |
|---|---|---|
| Beta run rate | USD 1,263–5,816/month | TBD — recorded cap USD 15k–25k is oversized 6–33×; reset required |

Cost-side notes carried from DOC-20260908-004: retire/renew 3 expired supplier trials (Bitquery, Covalent, Arkham) before client onboarding; ransomware.live subscription now free (USD 99/mo saving); OpenSanctions/Shodan InternetDB licence classes need resolution before paying-client use.

### Decision flags (DAF — pricing authority)

- **DF-1:** Adopt the DOC-20260908-004 envelope as the official cost basis for CSM quoting? (envelope currently awaits your approval)
- **DF-2:** Pentest inside base PoC price, or priced as a client option? (written deferral drops the floor ~USD 4k)
- **DF-3:** Quote currency for CSM channel — USD or MYR?
- **DF-4:** Margin policy — cost-floor-plus-% or value-based bands per tier?

---

## Part 2 — POC Scope Menu + Template (v0.1 skeleton)

**Doctrine constraint:** Bursa is NOT the default POC template (DOC-20260825-001 §6). Track A = Standard VoronCitadel POC; Track B = Bursa Sector-Leader extension, quoted separately.

Template sections (Fuad to complete technical specifics):

1. Objective & success criteria (measurable, agreed pre-start)
2. Scope boundaries — data, integrations, user counts, environments
3. Duration & phase gates (90-day envelope default; checkpoint at day 30/60/90)
4. Environment & access model (incl. sovereign-hosting positioning)
5. Exit review & acceptance evidence (feeds substantiation-pack doctrine)
6. Exclusions — all future-state capabilities per DEC-20260822-001 scope governance

---

## Part 3 — SLA Terms (v0.1 skeleton)

Sections requiring content (Fuad technical / DAF commercial):

- Support tiers + response times (POC vs Beta differentiated)
- Availability commitments (realistic vs marketing claim — evidence doctrine)
- Escalation path & incident comms
- Liability cap + indemnity alignment (CSM added indemnity to the NDA framework — keep the two consistent)
- Data residency / sovereign hosting commitments

---

## Open Items

1. DF-1…DF-4 rulings (DAF)
2. Technical scope + SLA parameter input (Fuad)
3. Version bump v0.1 → v1.0 on ruling; then CSM-ready
