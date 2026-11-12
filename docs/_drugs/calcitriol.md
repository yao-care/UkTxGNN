---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 5
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-11-12
description: "Calcitriol: predicted new indication obsolete vitamin D deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Calcitriol: Active vitamin D hormone → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active hormonal form of vitamin D. The TxGNN model predicts it may be relevant to **obsolete vitamin D deficiency**, but the data compiled for this report contain **no clinical trials** and **no publications** directly supporting this prediction. The prediction therefore rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (13 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not currently available. Calcitriol is the active form of vitamin D, so a mechanistic link to vitamin D deficiency is biologically plausible.

The disease term is flagged as obsolete in the disease ontology, so the prediction may reflect a legacy label rather than a distinct new disease. The very high score (0.9996) is a model output only. No trials or literature were found to test it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0906040C0AAAEAE | Calcitriol 1micrograms/1ml solution for injection ampoules | Calcitriol |
| 0906040C0AAAAAA | Calcitriol 250nanogram capsules | Calcitriol |
| 0906040C0AAADAD | Calcitriol 2micrograms/1ml solution for injection ampoules | Calcitriol |
| 1305020W0AAAAAA | Calcitriol 3micrograms/g ointment | Calcitriol |
| 0906040C0AAABAB | Calcitriol 500nanogram capsules | Calcitriol |
| 0906040C0AAAGAG | Calcitriol 500nanograms/5ml oral liquid | Calcitriol |
| 0906040C0AAAIAI | Calcitriol 5micrograms/5ml oral liquid | Calcitriol |
| 0906040C0BCABAE | Calcijex 1micrograms/1ml solution for injection ampoules | Calcitriol |
| 0906040C0BCAAAD | Calcijex 2micrograms/1ml solution for injection ampoules | Calcitriol |
| 0906040C0BBACAI | Rocaltrol 1micrograms/ml oral solution | Calcitriol |
| 0906040C0BBAAAA | Rocaltrol 250nanogram capsules | Calcitriol |
| 0906040C0BBABAB | Rocaltrol 500nanogram capsules | Calcitriol |
| 1305020W0BBAAAA | Silkis ointment | Calcitriol |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

No indication text or dosage-form details were recorded in the local licence data. Prescribers should check the current SmPC and the BNF entry for authorised uses and formulations.

<!-- review:begin uk-lic-20261106-calcitriol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data compiled for this report show that calcitriol is currently marketed in the UK, with a valid single-ingredient authorisation. No indication text or dosage-form details were recorded in the local licence data." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 13 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-calcitriol-1 -->

## Safety Considerations

- **Drug Interactions** (100 interactions recorded; selected examples):
  - **Major**: cholecalciferol, calcifediol (additive vitamin D effects), and burosumab.
  - **Moderate**:
    - Thiazide and thiazide-like diuretics (hydrochlorothiazide, bendroflumethiazide, chlorothiazide, chlorthalidone, benzthiazide).
    - Enzyme-inducing anticonvulsants and barbiturates (fosphenytoin, carbamazepine, amobarbital, butabarbital, butalbital).
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol).
    - Digoxin and digitoxin.
    - Aluminium hydroxide.
    - Topical calcipotriol.

No key warnings or contraindication text were available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials or publications directly studying this condition. The disease term is also flagged as obsolete in the ontology, so the evidence level is L5.

**To proceed, the following is needed:**
- Clarification of which current, non-obsolete clinical diagnosis the predicted term maps to
- Published clinical evidence in that condition
- Mechanism of action data
- Label-based warnings and contraindications from the SmPC and BNF

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data compiled for this report show that calcitriol is currently marketed in the UK, with a valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

