---
layout: default
title: Dorzolamide
parent: Model Prediction Only (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dorzolamide: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Dorzolamide"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "congestive heart failure", "acute pulmonary heart disease", "respiratory failure"]
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be useful in **primary hereditary glaucoma**, but **no clinical trials and no publications** specific to this condition were found in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension (from the knowledge graph, as the authorisation record gives no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dorzolamide inhibits carbonic anhydrase (mainly isoform II) in the ciliary body. This reduces aqueous humour secretion and lowers intraocular pressure (IOP). Detailed mechanism-of-action data were not available in the compiled data. The pharmacology records do list carbonic anhydrase isoforms 1, 7, 12 and 14 as human targets.

Primary hereditary glaucoma, such as congenital or juvenile forms, also involves raised IOP. A drug that reduces aqueous production therefore has a plausible mechanistic basis. The high score most likely reflects the model's similarity to the approved open-angle glaucoma indication, not independent evidence in hereditary disease.

One adjacent finding is a completed Phase 2 study (NCT01527682, n=37) of latanoprost and dorzolamide in paediatric glaucoma refractory to surgery. It is not specific to primary hereditary glaucoma, and the data compiled for this report do not include its results.

Several other predictions in the same output have higher evidence levels (for example "glaucoma 1, open angle" and "open angle glaucoma", both L1). These are confirmations of the existing licensed use, not repurposing findings. They are not tabulated here.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000P0AAAAAA | Dorzolamide Eye Drops 2% | Eye drops (from product name) | Not stated in the record |

The authorisation number does not follow the usual MHRA "PL" format. Please verify it against the MHRA register. Only one authorisation was identified, and it is a single-ingredient product.

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** The knowledge graph links dorzolamide to the following conditions as possible contraindications. This most likely reflects class effects, including those of the beta-blocker timolol in fixed-dose combination products. It should be checked against the SmPC.
  - Diabetes mellitus, diabetic ketoacidosis and hypoglycaemia
  - Myasthenia gravis and neuromuscular junction disease
  - Hyperthyroidism, Graves' disease and thyrotoxicosis
  - Atrioventricular block
  - Pulmonary emphysema and bronchial disease
  - Anaphylaxis
- **Drug Interactions:** The interaction query completed, but it returned only pharmacological target records (carbonic anhydrase 1, 7, 12 and 14), not interacting drugs. No clinical interaction data are available from this source.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a plausible mechanism but no supporting trials or publications specific to primary hereditary glaucoma. It is a computational result at evidence level L5.

**To proceed, the following is needed:**
- A targeted search for studies of carbonic anhydrase inhibitors in congenital and juvenile glaucoma, including the results of NCT01527682
- Paediatric safety and dosing data, as the licensed use is in adults with open-angle glaucoma and ocular hypertension
- SmPC warnings and contraindications, which were not available for this report
- Verification of the UK authorisation record, including dosage form and approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

