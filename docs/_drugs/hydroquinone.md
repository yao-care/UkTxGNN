---
layout: default
title: Hydroquinone
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Hydroquinone: predicted new indication Seborrheic keratosis (evidence level L4). Approved use: Not available in the data compiled for this report"
monitor_inn: "Hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Hydroquinone: From Pigmentary Disorders to Seborrheic Keratosis
{: .text-alpha }

## One-Sentence Summary

Hydroquinone is a topical depigmenting agent that inhibits tyrosinase, and a 4% cream is marketed in the UK for skin lightening.
The TxGNN model predicts it may be effective for **seborrheic keratosis**, but this is based on **no clinical trials** and **1 observational publication** that supports the idea only indirectly.
This is a model-driven hypothesis with weak supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From general pharmacology, hydroquinone inhibits tyrosinase and reduces melanin synthesis. This could plausibly lighten the pigmentation of seborrheic keratosis lesions.

Any benefit would be cosmetic only. Hydroquinone would not treat the underlying epidermal proliferation. The only supporting publication is a prospective observational study of combination treatment for facial pigmentary disorders in Asian patients, which is indirect evidence.


---

## Clinical Trial Evidence

Currently no related clinical trials registered for seborrheic keratosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Cohort (prospective observational) | Journal of Plastic, Reconstructive & Aesthetic Surgery | Combination treatment algorithm for facial pigmentary disorders in Asian patients. Most patients had multiple disorders. Indirect evidence for seborrheic keratosis. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1315000G0AAAIAI | Hydroquinone Cream 4% | Cream (per product name) | Not available |

---

## Cytotoxicity

This section does not apply: hydroquinone is not classified as an antineoplastic drug.

---

## Safety Considerations

- **Potential contraindications from the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text): sunburn, adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary haemorrhagic telangiectasia, peripheral vascular disease, intermittent claudication, peripheral arterial disease, atopic eczema and dermatitis.
- **Other safety considerations from the supporting literature:** exogenous ochronosis is a recognised adverse effect of hydroquinone-containing skin-lightening creams, and it can confound the diagnosis of pigmentary disorders.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a single indirect observational study, with no trials. Any benefit would be cosmetic rather than disease-modifying.

**To proceed, the following is needed:**
- Mechanism of action data
- Product label information (approved indication, warnings and contraindications) for the UK-marketed product
- Controlled studies of hydroquinone in seborrheic keratosis
- A review of the knowledge-graph contraindication signals against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

