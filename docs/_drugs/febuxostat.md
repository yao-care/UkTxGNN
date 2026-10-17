---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 276
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Febuxostat: predicted new indication Renal hypouricaemia (evidence level L4). Approved use: Hyperuricaemia"
monitor_inn: "Febuxostat"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Febuxostat: From Hyperuricaemia to Renal Hypouricaemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor, originally used to treat hyperuricaemia.
The TxGNN model predicts it may be effective for **renal hypouricaemia**, but the supporting evidence is weak: **1 clinical trial** with unverified relevance and **2 publications** (reviews/case-level reports) currently exist, and none demonstrates therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricaemia (from the knowledge-graph indication data; no approved indication text is available for the UK licence) |
| Predicted New Indication | Renal hypouricaemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, febuxostat is a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid, and its efficacy in hyperuricaemia is established.

Mechanistically, however, the prediction is counterintuitive. Renal hypouricaemia is characterised by already low serum urate, typically caused by loss-of-function variants in urate transporters such as URAT1 or GLUT9. Lowering urate further could, in theory, raise the risk of exercise-induced acute kidney injury or xanthinuria-like effects. The high TxGNN score most likely reflects network proximity to urate metabolism rather than a genuine therapeutic rationale.

The one relevant literature item is a case report of a young footballer with familial renal hypouricaemia and recurrent exercise-induced acute kidney injury, in whom a non-purine xanthine oxidoreductase inhibitor (febuxostat) was considered as prophylaxis. This is indirect, hypothesis-level evidence and does not show therapeutic benefit.

Two other predictions were also generated for this drug, and they are mechanistically more coherent but still weakly evidenced:
- **HPRT partial deficiency** (rank 2, score 99.98%): urate overproduction could be controlled by xanthine oxidase inhibition, with evidence limited to case reports.
- **Lesch-Nyhan syndrome** (rank 3, score 99.68%): febuxostat could control hyperuricaemia and stones, but not the neurobehavioural features, which are the main unmet need. Evidence is limited to small case series.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of the effect of uric acid control on stone recurrence and renal function in patients with calculi and hyperuricaemia. Relevance to renal hypouricaemia is unverified. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative update on hypouricaemia (serum urate < 2 mg/dL), covering its causes and what rheumatologists should know. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (indexed as review) | Internal Medicine (Tokyo) | A 16-year-old footballer with familial renal hypouricaemia (URAT1 variants) and recurrent exercise-induced acute kidney injury; febuxostat was considered as prophylaxis when hydration failed. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001040V0AAAAAA | Febuxostat Tab 80mg | Not specified | Not specified in the data compiled for this report |

Only one valid single-ingredient authorisation is recorded. The identifier shown does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register before use.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text): stroke disorder, cerebrovascular disorder, cerebral infarction, myocardial infarction, coronary thrombosis, and haemoglobinopathy. These should be confirmed against the SmPC.
- **Drug Interactions** (22 recorded; main ones listed):
  - **Major:** mercaptopurine, azathioprine, leflunomide, teriflunomide.
  - **Moderate:** methotrexate, tioguanine, theophylline, aminophylline, dyphylline, oxtriphylline, naltrexone, asparaginase, pegaspargase, brentuximab vedotin, clofarabine, trabectedin, epirubicin, and interferon beta products.
- **Theoretical concerns for the predicted indications:** further urate lowering in renal hypouricaemia, and hypoxanthine/xanthine accumulation (with a risk of xanthine nephropathy or stones) in HPRT deficiency states.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on network proximity rather than a credible therapeutic rationale. Lowering urate further in renal hypouricaemia is mechanistically counterintuitive, and the only supporting evidence is an indirect case-level report and an unrelated Phase 4 trial.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Label warnings and contraindications from the SmPC/BNF, as safety screening cannot proceed without them
- Verification of the UK authorisation record, including approved indication, dosage form and licence number
- Evidence that urate lowering benefits patients with renal hypouricaemia (for example, prospective data in exercise-induced acute kidney injury)
- If the research focus shifts, a targeted review of HPRT deficiency and Lesch-Nyhan syndrome, where the mechanistic rationale is stronger
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

