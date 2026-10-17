---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Calcitriol: predicted new indication Vitamin D deficiency (obsolete ontology term) (evidence level L5). Approved use: Hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders…"
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Calcitriol: From Mineral Metabolism Disorders to Vitamin D Deficiency

## One-Sentence Summary

Calcitriol is the active form of vitamin D. It was originally used for disorders of calcium and phosphate handling, such as hypoparathyroidism and renal osteodystrophy.
The TxGNN model predicts it may be effective for **vitamin D deficiency** (an ontology term now flagged as obsolete), but **no clinical trials and no publications** were found for this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, hypophosphataemia, hypoparathyroidism, renal osteodystrophy (from the knowledge graph; no approved indication text was available in the UK licence record) |
| Predicted New Indication | Vitamin D deficiency (obsolete ontology term) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Calcitriol is the hormonally active form of vitamin D. Its established uses are in conditions where the body cannot make enough active vitamin D or cannot regulate calcium and phosphate properly. This makes a link to vitamin D deficiency biologically plausible.

However, this is close to an on-label or near-label use rather than true repurposing. The predicted disease term is also marked as obsolete in the underlying ontology, so the very high score may partly reflect overlap with existing indications. In clinical practice, nutritional vitamin D deficiency is usually managed with cholecalciferol or ergocalciferol rather than the active metabolite. This is a point to verify against current guidance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1305020W0AAAAAA | Calcitriol ointment 0.0003% | Ointment (from product name) | Not stated in the record |

The only licence in the compiled data has an identifier that does not follow the usual MHRA "PL xxxxx/xxxx" format, and it has no indication text. It describes a topical ointment, which is not the route normally used for treating vitamin D deficiency. Please verify this record against the MHRA register, the BNF and the relevant SmPC before relying on it.

---

## Safety Considerations

- **Conditions linked to contraindication in the knowledge graph** (derived from network relationships, not from label text): kidney disease, pyoureter, sarcoidosis, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, hyperphosphataemia, hypervitaminosis and arteriosclerosis obliterans. Some of these overlap with conditions calcitriol is used to treat, so they should be read as signals to check rather than definitive contraindications.
- **Drug Interactions** (100 recorded; the main ones are shown):
  - **Major:** cholecalciferol, calcifediol and burosumab
  - **Moderate:**
    - Thiazide and thiazide-like diuretics (hydrochlorothiazide, bendroflumethiazide, chlorothiazide, chlorthalidone, benzthiazide)
    - Enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital)
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
    - Cardiac glycosides (digoxin, digitoxin)
    - Aluminium hydroxide
    - Topical calcipotriol

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but it has no supporting trials or publications. The target term is obsolete, and the use largely overlaps with existing practice, so there is nothing to act on yet.

Among the other predictions in the compiled data, **hereditary hypophosphataemic rickets** has the strongest support (two registered trials, Evidence Level L2, and guideline-type reviews). It would be a better candidate for further evaluation, with monitoring for hypercalciuria, nephrocalcinosis and hyperparathyroidism.

**To proceed, the following is needed:**
- Clarify which current disease term replaces "obsolete vitamin D deficiency" and whether this indication is already covered by existing guidance
- Mechanism of action data
- Verification of the UK licence record (identifier, formulation and approved indications) against the MHRA register and the SmPC
- Safety warnings and contraindications from the SmPC and BNF
- Any clinical or observational evidence specific to the final indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

