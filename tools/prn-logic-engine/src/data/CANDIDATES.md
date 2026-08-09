# PRN Johor 2026 — Candidate Intelligence Registry

**Classification:** TLP:AMBER — Operational Use Only  
**Last Updated:** 2026-06-28  
**Status:** Pre-nomination (intelligence gathering phase)

---

## 📋 Status Legend

- ✅ **Confirmed** — Officially nominated or publicly announced
- ⚠️ **Likely** — Strong intelligence, high probability
- 🔍 **Monitoring** — Names circulating, unconfirmed
- ❓ **TBD** — No intelligence yet

---

## 🏛️ Confirmed Candidates (Post-Nomination)

*This section will be populated after nomination day (June 27, 2026)*

---

## 🎯 Known Candidates (Pre-Nomination Intelligence)

### N17 Semerah (Batu Pahat) — ✅ Ground Truth Validated

| Coalition | Candidate | Party | Status | Profile |
|-----------|-----------|-------|--------|---------|
| **BN** | Mohd Fared Mohd Khalid | UMNO | ✅ Confirmed | Incumbent ADUN, Johor EXCO for Islamic Religious Affairs. Lawyer. Campaign: "Maju Johor" stability + EXCO service delivery. |
| **PH** | Mohd Khuzzan Abu Bakar | PKR | ✅ Confirmed | Former Semerah ADUN (2018-2022), former Johor EXCO. Deputy Chairman TalentCorp. Won this seat in 2018. |
| **PN** | Halim@Othman Kepol (Abang Halim) | PAS | ✅ Confirmed | PAS representative, deeply tied to PAS Parit Sulong regional framework. Community fixture via PASTI networks. |

---

### N24 Senggarang (Batu Pahat)

| Coalition | Candidate | Party | Status | Profile |
|-----------|-----------|-------|--------|---------|
| **BN** | Mohd Fared Mohd Khalid | UMNO | ⚠️ Likely | Incumbent ADUN. Strong rural Malay base. |
| **PH** | [Name TBD] | PKR | 🔍 Monitoring | Need local PKR chief intelligence. |
| **PN** | Rashid | [Party TBD] | 🔍 Monitoring | Former Batu Pahat MP, known local figure. Vulnerability: defector narrative. |

---

### N27 Layang-Layang (Kluang) — ✅ Ground Truth Validated

| Coalition | Candidate | Party | Status | Profile |
|-----------|-----------|-------|--------|---------|
| **BN** | Chua Jian Boon | MCA | ✅ Confirmed | Chinese candidate in 56.6% Malay seat. Collapses BN ceiling to 15-25%. |
| **PH** | Guna Balakrishnan | PKR | ⚠️ Likely | Indian candidate. Needs 75%+ Indian consolidation to win. Profile requires verification (NOT "PKR Tebrau deputy chief" — that's Arthur Chiong). |
| **PN** | Abd Mutalip Abd Rahim | Bersatu | ✅ Confirmed | Incumbent, ex-BN→Bersatu defector. Long-time local name. |

---

### N33 Tenggaroh (Mersing) — ⭐ FELDA Battleground

| Coalition | Candidate | Party | Status | Profile |
|-----------|-----------|-------|--------|---------|
| **BN** | [Name TBD] | UMNO | ⚠️ Likely | UMNO candidate (switched from MIC in 2022). Corrective move for 82.7% Malay majority. |
| **PH** | [Name TBD] | PKR | ❓ TBD | Need intelligence. 2022 base only 7.13%. |
| **PN** | [Name TBD] | PAS | ⚠️ Likely | Primary challenger. 2022: 42.78% vote share. |

---

### N41 Puteri Wangsa (Tebrau) — ⭐ Tier-1 Battleground

| Coalition | Candidate | Party | Status | Profile |
|-----------|-----------|-------|--------|---------|
| **BN** | Teow Chia Ling | MCA | ⚠️ Likely | Focusing on local-service credibility (congestion, public facilities). |
| **PH** | Dr Maszlee Malik | PKR | ✅ Confirmed | Former Education Minister. PH deploying heavyweight to reclaim seat. |
| **MUDA** | Rashifa Aljunied | MUDA | ✅ Confirmed | 26 years old, Chief of Staff to MUDA President. Youth appeal play. Incumbent Amira Aisya NOT defending. |
| **Bersama** | Nicholas Paul Vincent | Bersama | ⚠️ Likely | Entering progressive southern Johor seat. |
| **Independent** | [Name TBD] | — | ❓ TBD | Five-cornered fight expected. |

---

## 📊 Seats Requiring Candidate Intelligence

### Priority 1 (Tier-1 Battlegrounds)
- [ ] **N12 Kempas** (JB) — Need BN/PH/PN candidates
- [ ] **N13 Bukit Batu** (Kulai) — Need BN/PH/PN candidates
- [ ] **N41 Puteri Wangsa** (Tebrau) — Partial (Maszlee confirmed)

### Priority 2 (Upside Seats)
- [ ] **N16 Sungai Balang** (Muar) — Need BN/PH/PN candidates
- [ ] **N17 Semerah** (Batu Pahat) — ✅ COMPLETE
- [ ] **N27 Layang-Layang** (Kluang) — ✅ COMPLETE

### Priority 3 (BN-Leaning / Monitoring)
- [ ] **N01 Buloh Kasap** (Segamat)
- [ ] **N02 Pemanis** (Segamat)
- [ ] **N04 Bukit Naning** (Muar)
- [ ] **N14 Pulai Sebatang** (Pontian)
- [ ] **N15 Kukup** (Pontian)
- [ ] **N18 Bukit Kepong** (Muar)
- [ ] **N19 Sri Medan** (Batu Pahat)
- [ ] **N24 Senggarang** (Batu Pahat) — Partial
- [ ] **N25 Johor Lama** (Mersing)
- [ ] **N26 Tanjung Surat** (Mersing)
- [ ] **N32 Endau** (Mersing)
- [ ] **N33 Tenggaroh** (Mersing) — Partial
- [ ] **N35 Pasir Raja** (Kota Tinggi)

---

## 🔧 Update Instructions

When candidate intelligence is confirmed:

1. Update this file with candidate details
2. Update corresponding `src/data/nXX-seat-name.ts` file:
   ```typescript
   candidates: {
     bn: {
       name: 'Full Name',
       coalition: 'BN',
       party: 'UMNO',
       incumbent: true/false,
       profile: 'Brief profile with strengths/vulnerabilities'
     },
     ph: { ... },
     pn: { ... }
   }
   ```
3. Commit to GitHub with message: "Update [Seat] candidates — [Candidate Name] confirmed"
4. Tag war room team for validation

---

## 📝 Candidate Profile Template

```markdown
### NXX Seat Name (Parliament)

| Coalition | Candidate | Party | Status | Profile |
|-----------|-----------|-------|--------|---------|
| **BN** | [Name] | [Party] | [Status] | [Profile with strengths, vulnerabilities, network] |
| **PH** | [Name] | [Party] | [Status] | [Profile] |
| **PN** | [Name] | [Party] | [Status] | [Profile] |

**Key Dynamics:**
- [Malay vote split potential]
- [Incumbency advantage/disadvantage]
- [Personal vote vs party vote]
- [Defector narrative if applicable]
- [Community network strength]
```

---

**Intelligence Sources:**
- Excel DUN files (19 June 2026)
- Ground truth validation repos
- Public announcements
- War room intelligence network

**Contact:** Loop Engineering Political Monitoring Unit
