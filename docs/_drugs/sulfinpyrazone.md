---
layout: default
title: Sulfinpyrazone
parent: Model Prediction Only (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Sulfinpyrazone"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome", "neonatal epileptic encephalopathy due to glutaminase deficiency", "genetic otorhinolaryngological malformation", "disorder of phenylalanine metabolism", "semicircular canal dehiscence syndrome", "idiopathic bilateral vestibulopathy", "familial nasal acilia", "juvenile nasopharyngeal angiofibroma (disease)"]
description: "Sulfinpyrazone: predicted new indication Hypouricemia, renal (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulfinpyrazone
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

## Sulfinpyrazone: Hypouricemia, renal
{: .text-alpha }

## One-Sentence Summary

Sulfinpyrazone is a uricosuric agent, originally used to treat hyperuricaemia.
The TxGNN model predicts it may be effective for **renal hypouricaemia**, but **no clinical trials and no publications** support this prediction, and the mechanistic direction appears to be contraindicated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sulfinpyrazone is a uricosuric agent that inhibits URAT1-mediated renal urate reabsorption and lowers serum urate. It also has a weak antiplatelet effect.

On closer inspection, the prediction is **not mechanistically reasonable**. Renal hypouricaemia is caused by loss-of-function of URAT1 (SLC22A12) or GLUT9, which already produces excessive urate excretion and low serum urate. A uricosuric drug would be expected to **worsen** this phenotype rather than treat it.

The other highly ranked predictions show the same pattern:
- **HPRT partial deficiency and Lesch-Nyhan syndrome:** the link is only symptomatic (lowering urate). Increased renal urate load raises the risk of urate nephropathy and stones, and xanthine oxidase inhibitors such as allopurinol are standard of care. Sulfinpyrazone would not address the neurological features of Lesch-Nyhan syndrome.
- **Glutaminase deficiency encephalopathy, ENT malformation, phenylalanine metabolism disorders, vestibular conditions, nasal acilia and juvenile nasopharyngeal angiofibroma:** no plausible mechanism was identified, and these predictions appear to reflect network proximity only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001040P0AAAAAA | Sulfinpyrazone Tablets 100 mg | Tablet (form not specified in the data) | Not specified in the data compiled |

One single-ingredient authorisation is recorded as valid. The identifier shown is not in standard MHRA PL format, so the number and indication should be verified against the MHRA register and the BNF.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text; to be confirmed against the SmPC): kidney disease, pyoureter, haematological disease, inflammatory bowel disease and urolithiasis.
- **Drug Interactions:** 100 interactions were identified. Examples include:
  - **Major:** deferasirox.
  - **Moderate:** aspirin (acetylsalicylic acid); sulfonylureas and related antidiabetic agents (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide, repaglinide); saxagliptin and linagliptin; aprepitant and rolapitant; cobicistat; eliglustat; naloxegol; nitisinone; fenfluramine; sibutramine.
  - **Minor:** nateglinide.
- The urolithiasis and kidney disease signals are particularly relevant, because increased urinary urate excretion is the expected effect of the drug.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or publications. None of the other top-ranked predictions has a plausible mechanism or supporting evidence.

**To proceed, the following is needed:**
- A mechanistic rationale showing a plausible benefit rather than harm. Without one, this indication should not be pursued.
- Mechanism of action data and label-based warnings and contraindications from the SmPC and BNF.
- Verification of the UK licence details (authorisation number, dosage form and approved indication).
- A review of lower-ranked predictions, or of other candidate drugs, for indications with a credible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

