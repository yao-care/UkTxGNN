---
layout: default
title: Tolvaptan
parent: High Evidence (L1-L2)
nav_order: 586
evidence_level: L1
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tolvaptan: From Hyponatraemia Management to Polycystic Kidney Disease (ADPKD)

## One-Sentence Summary

Tolvaptan is a vasopressin V2-receptor antagonist whose original approved use — referenced within this evidence pack's clinical rationale — is management of hyponatraemia associated with heart failure/fluid overload. The TxGNN model predicts strong potential for **polycystic kidney disease 3, with or without polycystic liver disease** (i.e. the ADPKD/PLD spectrum), and this direction is already substantiated by **20 publications**, including two pivotal completed Phase 3 RCTs, even though no clinical trials are separately registered within this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally specified in the Evidence Pack (data gap); referenced context suggests hyponatraemia associated with heart failure/fluid overload |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The Evidence Pack's formal `original_moa` field is marked as a data gap, so no structured mechanism-of-action summary is available for tolvaptan as a standalone entry. However, the repurposing rationale attached to the top-ranked prediction describes tolvaptan as a **selective vasopressin V2-receptor antagonist** that inhibits cAMP signalling in the renal collecting duct — a pathway that is also the central driver of cyst formation and growth in autosomal dominant polycystic kidney disease (ADPKD).

This creates a direct mechanistic bridge between tolvaptan's known renal V2-receptor activity (used in the context of fluid/sodium management) and the predicted new indication: both rely on modulating vasopressin-driven signalling in the collecting duct epithelium, just applied to a different downstream pathology (fluid balance vs. cystogenesis).

Unlike many TxGNN predictions that rely purely on embedding similarity, this candidate is unusual in that it is **already backed by two completed, published Phase 3 RCTs** (TEMPO 3:4 and REPRISE, both in *NEJM*), which directly tested tolvaptan in ADPKD populations and demonstrated slowed decline in kidney function and reduced total kidney volume growth. This substantially strengthens the mechanistic plausibility beyond typical model-only predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials are separately registered within this evidence pack's `clinical_trials` field. The two pivotal Phase 3 RCTs supporting this indication (commonly known as TEMPO 3:4 and REPRISE) are captured as published trial-outcome literature below rather than as registry entries.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | New England Journal of Medicine | Pivotal trial (TEMPO 3:4) showing tolvaptan slows total kidney volume growth and eGFR decline in early ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | New England Journal of Medicine | REPRISE trial confirming efficacy and renal-function benefit of tolvaptan in later-stage ADPKD |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT | Pediatric Nephrology | Randomised trial (NCT02964273) assessing tolvaptan safety/pharmacodynamics and progression risk in paediatric ADPKD (ages 5–17) |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review & Meta-analysis | Nefrología | Pooled analysis confirming efficacy and safety profile of tolvaptan across ADPKD trials |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Evaluates disease-modifying agents, including tolvaptan, for slowing ADPKD progression |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive ADPKD review covering epidemiology, genetics, and tolvaptan's role in disease-modifying therapy |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrology Dialysis Transplantation | ERA Working Group/PKD International consensus on evidence-based initiation and monitoring of tolvaptan therapy |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | Journal of Hepatology | EASL Clinical Practice Guidelines covering management of polycystic liver disease, including ADPKD-associated PLD |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Reviews ADPKD/PLD overlap and notes tolvaptan's role in slowing renal deterioration and cyst growth |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Notes tolvaptan remains the only approved disease-modifying ADPKD therapy while reviewing emerging alternatives |

---

## UK Market Information

No UK marketing authorisation is currently recorded for tolvaptan in this Evidence Pack (`total_licenses = 0`, market status: **Not Marketed**). No product name, dosage form, or approved indication text is available to populate a licence table.

---

## Safety Considerations

The formal safety fields in this Evidence Pack (key warnings, contraindications, drug–drug interactions) are marked as data gaps and could not be populated.

However, the repurposing rationale for this prediction notes that tolvaptan carries a **known hepatotoxicity black-box warning** and a risk of **hypernatraemia/dysnatraemia**, and flags that regular liver function monitoring would be a required guardrail if the ADPKD indication were pursued.

Beyond this, please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence Level L1 is met — two completed Phase 3 RCTs (TEMPO 3:4 and REPRISE) directly validate tolvaptan's efficacy in ADPKD, going well beyond typical model-only predictions.
- The proposed mechanism (V2-receptor antagonism blocking cAMP-driven cystogenesis) is well established and coherent with tolvaptan's known pharmacology.
- A recognised hepatotoxicity guardrail (black-box warning, requiring liver function monitoring) must be factored into any development pathway.
- Lower-ranked candidate indications (ranks 2–10, e.g. renal-hepatic-pancreatic dysplasia, karyomegalic interstitial nephritis, hypertrichosis, Dandy-Walker-associated syndrome) show evidence level L4–L5 with little or no supporting literature and are appropriately held (**Hold**), not pursued further.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain formal MHRA/SmPC warnings and contraindications data before any S1 safety pre-assessment can proceed.
- Resolve **DG002 (High)**: obtain a structured mechanism-of-action summary from DrugBank to support formal mechanistic-link analysis.
- Clarify current UK marketing authorisation status for tolvaptan, given the "Not Marketed" flag in this pack.
- Complete route-compatibility assessment (currently marked "pending" in the Evidence Pack).
- Confirm drug–drug interaction data, particularly for CYP3A4 substrates/inhibitors relevant to long-term ADPKD dosing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

