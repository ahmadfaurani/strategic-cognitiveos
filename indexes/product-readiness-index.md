# Product Readiness Index

All products and their current readiness levels.

| Product | Initiative ID | Current Readiness | Target Readiness | Owner | Gaps | External Commitments | Overcommitment Risk |
|---------|-------------|-------------------|-----------------|-------|------|---------------------|---------------------|
| GovSec TIP | INIT-20260810-003 | Prototype (v3.0) | Demo-ready | faurani-jaafar | Stabilisation, hardening, E2E validation, Hadri handover | CyberDSA Oct 2026 joint launch with CSM | Medium — freeze may be breached if critical demo features missing |
| VoronCitadel | INIT-20260811-001 | Commercial-ready (assessed) | Commercial-ready | faurani-jaafar | Validate "Ready" assessment; compile formal documentation | CSM GTM activation (INIT-20260804-001) | Low — assessed as Ready, but assessment needs validation |
| ChainSentry | INIT-20260811-001 | Prototype (v3.0, verified 11 Aug 2026) | Commercial-ready | faurani-jaafar | 6 Critical gaps (deployment parity, external access, credential rotation, live-vs-demo boundary), 3 Must gaps (API/docs parity, integration health, quality gates), 4 Should gaps (schema migration, tenant isolation, outputs, alerting) | None identified | Medium — 6 Critical gaps must close before pilot |
| VoronDRQ | INIT-20260804-001 | Pilot | Commercial-ready | faurani-jaafar | GTM team mobilisation, COO approval | CSM joint GTM | Medium |
| VoronScout | — | *Pending* | — | — | — | — | — |
| LE-UIP | — | *Pending* | — | — | — | — | — |
| SEC-AF | — | *Pending* | — | — | — | — | — |

## Readiness Level Reference

| Level | External Commitment Allowed |
|-------|---------------------------|
| concept | No |
| framed | No |
| prototype | No |
| demo-ready | Demonstration only |
| pilot-ready | Pilot scope only |
| delivery-ready | Yes |
| commercial-ready | Yes |
| scale-ready | Yes |

## ChainSentry Detailed Readiness (MVP Spec v3.0, 14 Aug 2026)

### Verified Baseline (11 Aug 2026)
- Investigative surfaces: 26 page routes
- API route handlers: 44 (32/32 GET paths returned HTTP 200)
- Attribution corpus: 583,574 tags / 524,656 addresses / 78 chains
- Sanctions registry: 4,633 addresses
- Verified entity directory: 57 addresses
- Source health: 12 of 18 roles operational
- Automated jobs: 3 (daily sanctions, weekly attribution, 15-min alerts)
- Stability: No errors in 2,000-log-line window

### Critical Gaps (Must close before pilot)
1. Deployment parity — 22-commit/32-day gap between dev and deployed
2. External access & named identity — TLS termination, pilot accounts, session URL
3. Credential closure & secret governance — 4 exposed keys need rotation
4. Live-vs-demo boundary — 31-tool registry still fixture-backed

### Must-Have Gaps
1. API & documentation parity — in-product docs show illustrative routes, not implemented contract
2. Integration & anonymised-network health — 6 degraded source roles, Tor transport unreachable
3. Automated quality gates — tests don't run in CI, lint non-blocking, no risk-engine regression

### Should-Have Gaps
1. Schema migration & recovery — manual migrations, backup/restore not tested
2. Tenant isolation & quota control — only 1 tenant verified
3. Investigator outputs — no batch screening, PDF export, or audit-log UI
4. Alerting & observability — webhook-only delivery, no email, no structured logging

### Future Capabilities (Post-Pilot)
- Cryptographic dossier signing
- Bitcoin/non-EVM tracing
- Cross-chain bridge following
- Real-time streaming ingestion
- Messaging-channel alerts
- Case collaboration & assignment
- Saved searches & watchlists
- Self-service org onboarding
