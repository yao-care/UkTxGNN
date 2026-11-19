---
layout: default
title: Hydroquinone
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
description: "Hydroquinone: predicted new indication Seborrheic keratosis (evidence level L5). Approved use: Not available in the data compiled for this report"
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
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (11 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for hydroquinone: "Topical application of hydroquinone produces a reversible depigmentation of the skin by inhibition of the enzymatic oxidation of tyrosine to 3,4-dihydroxyphenylalanine (dopa) (Denton, C. et al., 1952)1 and suppression of other melanocyte metabolic processes (Jimbow, K. et al., 1974)2. Exposure to sunlight or ultraviolet light will cause repigmentation of bleached areas (Parrish, L.A. et al., 1978)3." ([DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b), label version 2026-07-10; accessed 2026-11-19.) From general pharmacology, hydroquinone inhibits tyrosinase and reduces melanin synthesis. This could plausibly lighten the pigmentation of seborrheic keratosis lesions.

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

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1315000G0AAAWAW | Hydroquinone 2% cream | Depigmenting agents |
| 1315000G0AABEBE | Hydroquinone 2% in Aqueous cream | Depigmenting agents |
| 1315000G0AABKBK | Hydroquinone 20% cream | Depigmenting agents |
| 1315000G0AAAQAQ | Hydroquinone 3% cream | Depigmenting agents |
| 1315000G0AAALAL | Hydroquinone 4% cream | Depigmenting agents |
| 1315000G0AAABAB | Hydroquinone 5% cream | Depigmenting agents |
| 1315000G0BEABAW | Eldoquin 2% cream | Depigmenting agents |
| 1315000G0BEAAAL | Eldoquin 4% cream | Depigmenting agents |
| 1315000G0AABHBH | Hydrocort 1% / Tretinoin 0.025% / Hydroquinone 4% in Aq crm | Depigmenting agents |
| 1315000G0AABJBJ | Hydrocort 1%/Tret 0.025%/Hydroquinone 4% in Gen Unguen M crm | Depigmenting agents |
| 1315000G0AABIBI | Hydrocortisone 1% / Tretinoin 0.1% / Hydroquinone 5% cream | Depigmenting agents |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

