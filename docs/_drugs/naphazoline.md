---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Naphazoline: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Temporary relief of eye redness"
monitor_inn: "naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
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

## Naphazoline: From Ocular Redness (Decongestant Eye Drops) to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Naphazoline is an alpha-adrenergic vasoconstrictor used in eye drops to reduce redness by narrowing swollen blood vessels in the eye.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but there are **no clinical trials and no publications** supporting this prediction. It is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Temporary relief of eye redness (vasoconstrictor eye drops; the authorisation record contains no indication text) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, naphazoline is a topical alpha-adrenergic agonist. It acts on alpha-1A, alpha-2A and alpha-2C adrenoceptors and narrows blood vessels, which is why it is used in decongestant eye drops.

On review, **the prediction is not biologically plausible**. Local vasoconstriction is not a recognised way to promote hair growth, and it could in theory reduce blood flow to hair follicles. Established hair-loss treatments act through different pathways: minoxidil (a vasodilator and potassium channel opener), finasteride, and JAK inhibitors.

The same pattern appears across the other top predictions: alopecia, alopecia areata, hypertrichosis (excess hair growth, the opposite direction) and several rare congenital syndromes. This suggests the high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a true pharmacological effect. The score should be treated as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the predicted indication.

For context, the only publication retrieved for any of the top ten predictions relates to open-angle glaucoma (rank 8): [PMID 1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/) (1992, Aust N Z J Ophthalmol). It examined topical corticosteroids after argon laser trabeculoplasty, not naphazoline, so it provides no support for naphazoline use.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1104020ABAAAAAA (BNF code) | Hamamelis/Naphazoline Eye Drops 12.5/0.01% | Eye drops | Not stated in the data compiled |

This is a single-ingredient authorisation record for a witch hazel (hamamelis) and naphazoline eye drop product. Dosage form and indication text were not recorded in the data compiled for this report. Please check the current SmPC and BNF entry.

---

## Safety Considerations

- **Contraindications and cautions (knowledge-graph-derived, not label text):** The TxGNN knowledge graph links naphazoline with caution in the following conditions: hypertension, cardiovascular and heart disease, hyperglycaemia, diabetes mellitus and diabetic ketoacidosis, angle-closure (closed-angle) glaucoma, hyperthyroidism (Graves' disease, thyrotoxicosis), and eye infections including conjunctivitis. These should be verified against the SmPC.
- **Receptor interactions:** Pharmacology data show activity at alpha-1A, alpha-2A and alpha-2C adrenoceptors in humans. No drug-drug interactions with a graded severity level were identified.
- **Relevance to predicted uses:** Sympathomimetic mydriasis may risk angle closure in susceptible eyes, so use in glaucoma is a concern rather than a benefit.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or relevant publications, and the mechanism (local vasoconstriction) does not plausibly support hair growth and may be counterproductive.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking alpha-adrenergic agonism to follicle biology, supported by preclinical data
- Mechanism of action data and the product's SmPC (indication, dosage form, warnings and contraindications), which are missing from the data compiled
- Confirmation of route compatibility, since the licensed product is an ophthalmic preparation and the predicted use would be on the scalp
- Any clinical or observational evidence in hair disorders before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

