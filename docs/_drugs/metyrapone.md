---
layout: default
title: Metyrapone
parent: Model Prediction Only (L5)
nav_order: 410
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Metyrapone: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Not recorded in the UK licence data compiled for this report (pharmac…"
monitor_inn: "Metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
---

# Metyrapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Metyrapone: From Cortisol Synthesis Inhibition to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Metyrapone is an inhibitor of adrenal steroid synthesis, used as a diagnostic tool for hypothalamic-pituitary function and occasionally in the treatment of Cushing's syndrome.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are **no clinical trials and no publications** supporting this prediction, so it rests on a computational signal alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the UK licence data compiled for this report (pharmacology sources describe use in diagnostic testing of hypothalamic-pituitary function and in Cushing's syndrome) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From pharmacology sources, metyrapone inhibits 11-beta-hydroxylase (CYP11B1) and, to a lesser extent, CYP11B2, which blocks the final step of cortisol synthesis in the adrenal gland.

Malignant hyperthermia is a different kind of disorder. It is driven by dysregulated calcium release through the skeletal muscle ryanodine receptor (RYR1). Cortisol synthesis inhibition does not address this pathway, and no mechanistic link has been established. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the myopathies and malignant hyperthermia, not biological evidence or a pharmacological rationale.

The other top-ranked predictions are also muscle or electrolyte disorders (for example malignant hyperthermia susceptibility, King-Denborough syndrome, central core myopathy, centronuclear myopathy and familial periodic paralysis). They share the same weakness: there is no plausible mechanistic connection to steroidogenesis inhibition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications were found for the lead prediction (exercise-induced malignant hyperthermia). For a lower-ranked prediction, familial periodic paralysis, one historical paper was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Other (historical physiological study) | The Journal of Clinical Investigation | In one patient with hyperkalaemic periodic paralysis, attacks were induced by potassium chloride, corticotropin-gel and several glucocorticoids, but not by mineralocorticoids or by ACTH-gel plus metyrapone. This is a tangential physiological observation, not evidence of therapeutic benefit. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0607030M0AAAAAA (BNF-style code; PL number not available) | Metyrapone capsules 250 mg | Capsule | Not stated in the compiled data |

One valid single-ingredient authorisation is recorded. The BNF classification code suggests placement in the endocrine chapter, but the approved indication text was not available.

---

## Cytotoxicity

Not applicable. Metyrapone is an endocrine agent and not an antineoplastic drug, so this section is omitted.

---

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease contraindication edges, not label text):** Addison disease, chronic primary adrenal insufficiency, adrenal insufficiency, adrenocortical insufficiency, congenital adrenal hyperplasia, familial glucocorticoid deficiency, X-linked adrenal hypoplasia congenita, familial adrenal hypoplasia with absent pituitary luteinising hormone, and inherited isolated adrenal insufficiency due to partial CYP11A1 deficiency. This is consistent with the drug's cortisol-lowering action.
- **Drug Interactions:** 12 interaction records were found. Ten are of Moderate severity and involve oestrogen-containing products (ethinylestradiol, estradiol, conjugated oestrogens, mestranol, esterified oestrogens, estrone sulfate, and topical forms) and cyproheptadine. The remaining two are pharmacological target records (CYP11B1 and CYP11B2) rather than drug-drug interactions.

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5), and there is no plausible mechanistic link between inhibition of cortisol synthesis and RYR1-driven malignant hyperthermia. Standard management relies on dantrolene, which acts on RYR1. The drug would also be risky in patients with adrenal insufficiency.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting CYP11B1 inhibition to the pathophysiology of malignant hyperthermia, supported by preclinical data
- Mechanism of action data and the approved indication text from the SmPC and BNF
- Complete label warnings and contraindications for a safety screen
- Any preclinical or clinical evidence before reconsideration, since none exists at present
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

