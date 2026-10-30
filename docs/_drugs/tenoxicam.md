---
layout: default
title: Tenoxicam
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 8
monitor_inn: "Tenoxicam"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "trigeminal autonomic cephalalgia", "alopecia"]
last_modified_at: 2026-10-30
description: "Tenoxicam: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Arthritic joint disease and arthropathy"
---

# Tenoxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Tenoxicam: From Arthritic Joint Disease to Brachydactyly-Syndactyly Syndrome
{: .text-alpha }

## One-Sentence Summary

Tenoxicam is a non-steroidal anti-inflammatory drug (NSAID).
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
There are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arthritic joint disease and arthropathy (relations recorded in the knowledge graph; no approved indication text is available in the licence record) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

On the data available, it is not clearly reasonable. Detailed mechanism of action data for tenoxicam is not available in the data compiled for this report. Tenoxicam belongs to the NSAID class, which acts by inhibiting cyclooxygenase (COX) and reducing prostaglandin synthesis. This explains its use in painful, inflammatory joint conditions.

Brachydactyly-syndactyly syndrome is a congenital developmental disorder in which the digits are malformed. The cause is genetic and structural, not inflammatory. COX inhibition has no plausible role in correcting a developmental defect of this kind. No mechanistic link between the original indication and this condition has been identified.

The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not supported by any trial, publication or biological rationale, and it should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Status |
|---------|------|------|
| 100101040AAAAAA | Tenoxicam Tab 20 mg | Valid, single-ingredient product |

The licence record contains no approved indication text, dosage form or manufacturer, so the authorised indications cannot be confirmed from the data compiled for this report. Please check the current SmPC and the BNF.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications, so the evidence level is L5. It also has no plausible mechanistic basis: an anti-inflammatory COX inhibitor would not be expected to alter a congenital limb malformation.

**To proceed, the following is needed:**
- A plausible biological rationale linking the drug's mechanism to the condition, along with confirmed mechanism of action data
- Any preclinical or clinical study that directly addresses this disease
- Confirmed approved indications, dosage form and safety information from the SmPC and BNF

**Note on other predictions for this drug:** Among the other TxGNN predictions, **headache disorder** (score 0.9968) has the most support. It has one Phase 4 trial comparing intravenous tenoxicam with intravenous ibuprofen in acute migraine ([NCT06786650](https://clinicaltrials.gov/study/NCT06786650); 100 participants, active but not recruiting, no results yet). If the team wants to pursue a repurposing question for tenoxicam, that is the more promising direction. The alopecia-related predictions should not be pursued, because the only related publication reports alopecia as a possible adverse effect of tenoxicam ([PMID 9303679](https://pubmed.ncbi.nlm.nih.gov/9303679/)).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

