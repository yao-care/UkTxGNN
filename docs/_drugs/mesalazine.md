---
layout: default
title: Mesalazine
parent: Moderate Evidence (L3-L4)
nav_order: 367
evidence_level: L3
indication_count: 7
---

# Mesalazine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

Mesalazine (5-ASA) is an anti-inflammatory agent whose established use, referenced throughout this evidence pack, is inflammatory bowel disease (ulcerative colitis). TxGNN's highest-scoring predictions (e.g. congenital hypotrichosis, seborrheic keratosis) have no supporting evidence and are flagged **Hold**; among predictions with actual evidence, **rheumatoid arthritis** currently has the most developed evidence base — **6 clinical trials** (mostly on the parent compound sulfasalazine, several terminated or off-target) — while **osteoarthritis** is supported only by preclinical/mechanistic literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not separately listed in the regulatory dataset; mesalazine's established use (referenced repeatedly in this pack) is ulcerative colitis / inflammatory bowel disease |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L3 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mesalazine is not available (data gap DG002). Based on what is known, mesalazine is the active metabolite of sulfasalazine, an anti-inflammatory agent used in inflammatory bowel disease. Sulfasalazine itself is an established conventional DMARD for rheumatoid arthritis, acting through inhibition of NF-κB signalling and suppression of prostaglandin and leukotriene synthesis — the same pathways implicated in mesalazine's gut-directed anti-inflammatory action. This shared pharmacology is the biological basis for TxGNN linking mesalazine to RA.

However, an important caveat runs through the evidence: most of the RA-related trials in this pack actually studied **sulfasalazine (the parent drug)**, not mesalazine (the active metabolite) itself, and several are mislabelled or off-target (e.g. ulcerative colitis or AML studies incorrectly mapped to RA). Only one trial (NCT02930343) directly compares sulfasalazine-based combination DMARD therapy in RA, and it was terminated. This means the RA signal should be read as "class-level plausibility via the parent drug," not as direct mesalazine efficacy evidence.

A related, independently-scored prediction — osteoarthritis (not the primary focus of this report, evidence level L4) — offers additional mechanistic support: a 2024 *Nature Communications* study reports that 5-ASA suppresses osteoarthritis via the OSCAR–PPARγ axis, reinforcing the general idea that 5-ASA's anti-inflammatory activity may extend beyond the gut to joint disease. This strengthens the plausibility of the broader "5-ASA in joint inflammation" hypothesis, even though it does not directly evidence RA.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | Sulfasalazine vs leflunomide-based combination DMARD therapy in RA patients failing methotrexate monotherapy — most directly relevant trial, but terminated before completion |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Pharmacokinetics of sulfasalazine delayed-release tablets in children with juvenile idiopathic arthritis (PK only, not an efficacy trial; terminated with only 2 subjects) |
| [NCT05580861](https://clinicaltrials.gov/study/NCT05580861) | Phase 1/2 | Recruiting | 64 | Sulfasalazine combined with standard induction therapy in acute myeloid leukaemia (xCT-inhibition mechanism; unrelated to RA indication) |
| [NCT03591770](https://clinicaltrials.gov/study/NCT03591770) | Phase 4 | Terminated | 15 | Shingrix vaccine immunogenicity in ulcerative colitis patients on tofacitinib — mislabelled match, not RA-relevant |
| [NCT00514982](https://clinicaltrials.gov/study/NCT00514982) | Phase 2 | Withdrawn | 0 | Observational study of IBD-type therapy in Hermansky-Pudlak syndrome-associated colitis — withdrawn, not RA-relevant |
| [NCT06201793](https://clinicaltrials.gov/study/NCT06201793) | Phase 2 | Completed | 46 | Minocycline efficacy/safety in ulcerative colitis patients treated with mesalamine — a UC study, not RA-relevant |

**Note:** Only NCT02930343 is a genuine RA efficacy trial, and it was terminated. The remaining trials are either off-target (UC, AML) or non-efficacy (PK) studies that appear to have been matched on drug name rather than indication.

---

## Literature Evidence

Currently no related literature specifically evaluating mesalazine (or sulfasalazine) in rheumatoid arthritis was identified in this evidence pack.

*(For context: a separate TxGNN prediction for osteoarthritis is supported by 3 mechanistic/preclinical publications, including a 2024 Nature Communications paper on the OSCAR–PPARγ axis — see "Why is This Prediction Reasonable" above.)*

---

## UK Market Information

No marketing authorisations are recorded in this evidence pack (0 licences); market status is listed as **Not marketed**.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications and drug-drug interaction data are recorded as a blocking data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap exists (missing product label warnings/contraindications), which prevents any initial safety assessment (S1) regardless of indication.
- Even the best-evidenced candidate, rheumatoid arthritis (L3, decision stage S2, "Research Question"), rests mainly on trials of the parent compound sulfasalazine rather than mesalazine itself, and the single directly relevant Phase 3 trial was terminated. The other four top-ranked TxGNN predictions (congenital hypotrichosis, seborrheic keratosis, OA susceptibility, vulvar inverted follicular keratosis, pseudoachondroplasia) have no supporting evidence and no plausible mechanistic link.

**To proceed, the following is needed:**
- Product label / SmPC data (warnings, contraindications, DDI) to clear the blocking safety data gap
- Mechanism of action data for mesalazine specifically (distinct from sulfasalazine)
- Direct mesalazine (not sulfasalazine) clinical trial data in rheumatoid arthritis or osteoarthritis
- Clarification of whether the high-scoring but evidence-free predictions (hypotrichosis, keratosis conditions, pseudoachondroplasia) reflect genuine embedding signal or model artefact, before further resource is committed to this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

