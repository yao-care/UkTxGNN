---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the licence data compiled for this report (aprepitant i…"
monitor_inn: "Aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Aprepitant: From Chemotherapy-Related Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Aprepitant is a substance P/NK1 receptor antagonist. The data compiled for this report do not list an approved indication for the UK licence, so the original use is inferred from the drug class (antiemetic).
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and **0 relevant publications** supporting this prediction, so it rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (aprepitant is an NK1 antagonist antiemetic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Aprepitant is known as a substance P/NK1 receptor antagonist. NK1 signalling has been loosely linked to vasopressin regulation and renal water handling, which is the only basis for the prediction.

Nephrogenic SIAD, however, is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2). These act downstream of vasopressin release, so blocking NK1 is not expected to correct the primary defect. The very high TxGNN score is a computational output, not evidence of efficacy. The prediction should be regarded as weak biologically.

Other top-ranked predictions (for example hypertrichosis, pulmonary hypertension, leprosy and subarachnoid haemorrhage) are likewise unsupported by trial or literature data. Only subarachnoid haemorrhage and pulmonary hypertension have a plausible, preclinical-level hypothesis (NK1 signalling in blood-brain barrier disruption and pulmonary vascular tone, respectively).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000ADAAABAB (BNF code; not a PL number) | Aprepitant capsules 125 mg | Capsule | Not stated in the data compiled |

The BNF chemical code above is the only identifier available. Dosage form detail, manufacturer and approved indication text are not recorded.

## Safety Considerations

- **Knowledge-graph contraindication signal**: liver failure (from drug-disease contraindication edges in the TxGNN knowledge graph, not from label text; check against the SmPC).
- **Drug Interactions**: 100 interactions were identified. Examples from the interactions reviewed:
  - **Major**: fentanyl, alfentanil, acalabrutinib
  - **Moderate**: paclitaxel, abemaciclib, nifedipine, ibuprofen, lidocaine, dihydrocodeine, rabeprazole, levonorgestrel, hydrocortisone, albendazole, fluvoxamine, fosamprenavir, fosphenytoin, fostamatinib, gefitinib, abametapir (topical)
  - **Minor**: dolutegravir

Label warnings and contraindications were not available. Please refer to the SmPC and BNF, and report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score only. There are no trials or relevant publications, and the known biology of nephrogenic SIAD (a downstream V2 receptor defect) argues against NK1 antagonism being effective.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic case that addresses the AVPR2 gain-of-function defect
- Preclinical or case-level evidence of aprepitant effect on urine concentration or water handling
- Label warnings and contraindications from the SmPC and BNF, plus confirmation of the licensed indication
- If any alternative prediction is pursued, subarachnoid haemorrhage and pulmonary hypertension have the more plausible preclinical rationale, though neither has supporting clinical evidence yet
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

