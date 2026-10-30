---
layout: default
title: Febuxostat
parent: Model Prediction Only (L5)
nav_order: 276
evidence_level: L5
indication_count: 3
monitor_inn: "Febuxostat"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
last_modified_at: 2026-10-30
description: "Febuxostat: predicted new indication Renal hypouricemia (hypouricemia, renal) (evidence level L5). Approved use: Not recorded in the local data"
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Febuxostat: xanthine oxidase inhibitor → Renal hypouricemia (hypouricemia, renal)
{: .text-alpha }

## One-Sentence Summary

Febuxostat is a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid.
The TxGNN model predicts it for **renal hypouricemia**, but the mechanism points the wrong way for this condition, and the evidence is thin: **1 clinical trial** of uncertain relevance and **2 publications**, none showing therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Febuxostat is known to be a non-purine selective xanthine oxidase inhibitor, so it reduces the formation of uric acid.

Renal hypouricemia is a condition in which serum urate is already low (below 2 mg/dL, or 119 μmol/L). It is typically caused by loss-of-function variants in urate transporters such as URAT1 or GLUT9. Lowering urate further is mechanistically counterintuitive. It could, in principle, raise the risk of exercise-induced acute kidney injury or xanthinuria-like effects.

The high TxGNN score probably reflects network proximity to urate metabolism rather than a true therapeutic rationale. A 2023 case report describes a young footballer with familial renal hypouricemia and recurrent exercise-induced acute kidney injury, and discusses non-purine selective xanthine oxidoreductase inhibitors as a possible preventive option. This is hypothesis-level and does not demonstrate benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | A prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with hyperuricaemia and calculi. Its link to renal hypouricemia is unverified. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate below 2 mg/dL), its causes and its relevance to rheumatologists. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (indexed as review) | Internal Medicine | A 16-year-old footballer with familial renal hypouricemia (URAT1 variants) and recurrent exercise-induced acute kidney injury. Hydration alone did not prevent episodes, and a xanthine oxidoreductase inhibitor is discussed as possible prophylaxis. |

## UK Market Information

Febuxostat is marketed in the UK, and the local data show one valid single-ingredient licence record (product record: Febuxostat tablet 80 mg). No dosage form or indication text is recorded for it in the local data.

## Safety Considerations

- **Drug Interactions**: 22 interactions are recorded, 20 of them listed in detail. The major-level interactions are:
  - Mercaptopurine
  - Azathioprine
  - Leflunomide
  - Teriflunomide

  Moderate-level interactions include:
  - Theophylline, aminophylline, dyphylline and oxtriphylline
  - Methotrexate
  - Tioguanine
  - Naltrexone
  - Asparaginase and pegaspargase
  - Brentuximab vedotin
  - Clofarabine
  - Epirubicin
  - Trabectedin
  - Interferon beta-1a, interferon beta-1b and peginterferon beta-1a
- **Other considerations**: Further urate lowering in a patient with already low urate may carry a risk of exercise-induced acute kidney injury or xanthinuria-like effects.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism runs counter to the condition: febuxostat lowers urate, and urate is already low in renal hypouricemia. No study shows therapeutic benefit, and the single registered trial concerns hyperuricaemia with calculi, not this disease. The high score is not backed by clinical evidence.

**To proceed, the following is needed:**
- A clear mechanistic case for benefit rather than harm in patients with low baseline urate
- Studies that directly examine renal hypouricemia, such as controlled or well-documented case series on exercise-induced acute kidney injury
- A safety assessment covering xanthine accumulation and kidney risk
- Full UK safety information from the SmPC and BNF, plus the mechanism of action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

