---
layout: default
title: Ammonia
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ammonia: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Psoriasis, parapsoriasis, acne, seborrhoeic dermatitis…"
monitor_inn: "Ammonia"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial"]
---

# Ammonia
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ammonia: From Dermatological Conditions (Psoriasis, Acne, Seborrhoeic Dermatitis) to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Ammonia is listed in the knowledge graph for several skin conditions, including psoriasis, acne and seborrhoeic dermatitis.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**,
but there are **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, acne, seborrhoeic dermatitis, pityriasis simplex, seborrhoeic keratosis, keratinisation disorders (knowledge graph annotations; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ammonia, so the high score cannot be traced to a biological rationale.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of *Borrelia* infection (Lyme disease) and is treated with antibiotics. There is no known role for ammonia in this condition. The prediction most likely reflects network proximity to the original dermatological indications in the knowledge graph rather than a true pharmacological effect.

Other top-ranked predictions show the same pattern, with scores between 99.56% and 99.64% and no supporting studies:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Neonatal dermatomyositis | 99.64% | L5 | No mechanistic link; use in neonates would raise serious safety concerns |
| 3 | Acne keloid | 99.63% | L5 | Only an indirect link through the acne annotation, with no defined mechanism |
| 4 | Secondary interstitial lung disease of childhood associated with a connective tissue disease | 99.61% | L5 | Ammonia is a respiratory irritant, so pulmonary exposure is more likely harmful than therapeutic |
| 5 | Amyopathic dermatomyositis | 99.60% | L5 | Likely driven by shared dermatological neighbours in the graph |
| 6 | Hydroa vacciniforme, familial | 99.56% | L5 | No known pathway to the disease |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190400000AAUIUI | Ammonia Soln Strong 3.5% | Not stated | Not stated |

This single authorisation is a valid single-ingredient product. Dosage form and approved indication details are not available in the data compiled for this report, so please check the MHRA records, the SmPC and the BNF.

## Safety Considerations

**Knowledge graph contraindication associations** (taken from graph relationships, not from product label text):
- Anogenital human papillomavirus infection
- Common wart
- Diabetes mellitus
- Diabetic ketoacidosis
- Dermatitis
- Peripheral vascular disease, including intermittent claudication and peripheral arterial disease

**Additional considerations from the evaluation:**
- Ammonia is a known respiratory irritant and toxicant. Inhalation or pulmonary exposure is a particular concern.
- Use in neonates and children would need careful safety review.

No drug interaction data were found. For the full safety profile, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (99.70%), with no clinical trials, no publications and no plausible mechanism. Acrodermatitis chronica atrophicans has an established antibiotic treatment, and ammonia has known toxicity concerns.

**To proceed, the following is needed:**
- Mechanism of action data for ammonia (for example from DrugBank)
- Label warnings and contraindications from the SmPC and BNF
- Dosage form and approved indication details for the UK-authorised product
- Preclinical or mechanistic evidence linking ammonia to the predicted condition
- A safety assessment covering systemic and respiratory toxicity, and use in children and neonates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

