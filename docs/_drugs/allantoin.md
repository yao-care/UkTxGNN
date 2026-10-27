---
layout: default
title: Allantoin
parent: Model Prediction Only (L5)
nav_order: 38
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Allantoin: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Psoriasis, parapsoriasis, seborrhoeic dermatitis, pityriasis simplex…"
monitor_inn: "allantoin"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial", "exanthem (disease)"]
---

# Allantoin
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

## Allantoin: From Psoriasis and Dermatitis to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Allantoin is a topical skin agent, supplied here in a coal tar extract/allantoin cream (5%/2%), originally used for psoriasis, seborrhoeic dermatitis and related skin conditions.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but there are **no clinical trials and no publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, seborrhoeic dermatitis, pityriasis simplex, dermatitis, seborrhoeic keratosis (from the TxGNN knowledge graph; no licensed indication text is available) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, allantoin is a topical keratolytic and wound-healing agent, and it is used here in a combination with coal tar extract for inflammatory and scaling skin conditions. Its epithelial and anti-irritant actions have no established connection to retinal microvascular pathology.

The high TxGNN score is a computational prediction only. On the data compiled for this report, there is no supported mechanistic link between allantoin and diabetic retinopathy, and no similarity analysis to the original indications has been completed. Route compatibility is also unassessed: allantoin is a topical product, while retinal disease would normally require ocular or systemic delivery.

Other predictions in the list are more biologically plausible from a dermatological standpoint but are equally unsupported by clinical data. The most plausible is **acne keloid** (rank 4, score 99.48%), where allantoin's proposed effects on extracellular matrix, fibroblast proliferation and wound healing give a reasonable, though unproven, rationale. This one is flagged as a research question rather than a hold. The remaining predictions (acrodermatitis chronica atrophicans, neonatal dermatomyositis, childhood connective-tissue-disease-associated interstitial lung disease, amyopathic dermatomyositis, familial hydroa vacciniforme and exanthem) have weak or no mechanistic support, at best offering minor symptomatic skin soothing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1305020C0AABABA | Coal Tar Ext/Allantoin Cream 5%/2% | Not specified | Not specified |

The licence is recorded as a valid single-ingredient authorisation. The identifier is not in the standard MHRA PL format, and the dosage form, manufacturer and approved indication text were not available in the data compiled for this report. Please verify the product details against the MHRA register and the BNF.

## Safety Considerations

- **Knowledge-graph contraindication signals (not label text):** The TxGNN knowledge graph links allantoin to the following conditions via contraindication edges: inherited porphyria, porphyrin metabolism disease, porphyria, kidney disease, pyoureter, haematologic disease, liver disease, gallbladder disease, G6PD deficiency, glycogen storage disease, cystinuria, galactosaemia, folliculitis, seborrhoeic dermatitis and dermatitis. These are model-derived associations and should not be read as licensed contraindications. Some, such as seborrhoeic dermatitis and dermatitis, overlap with the original indications, so they should be interpreted with caution and checked against the product SmPC.
- **Drug interactions:** No interactions were found in the queried database.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for severe nonproliferative diabetic retinopathy has a high model score but no trials, no literature and no credible mechanistic link, and allantoin is a topical skin agent. Evidence is at L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for allantoin
- Preclinical or mechanistic evidence linking allantoin to retinal microvascular disease
- Assessment of route compatibility (topical product versus ocular or systemic delivery)
- Label-based warnings and contraindications from the SmPC and BNF
- Licensed indication, dosage form and manufacturer details for the UK authorisation
- Consideration of acne keloid as a better-supported research question, with preclinical or pilot clinical validation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

