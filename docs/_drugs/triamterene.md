---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 6
---

# Triamterene
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

# Triamterene: From Potassium-Sparing Diuretic Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic that works by blocking the epithelial sodium channel (ENaC) to reduce sodium reabsorption; it currently holds no UK marketing authorisation. The TxGNN model's top-ranked prediction links it to **Malignant Renovascular Hypertension**, but this is a **model-only prediction (L5)** with no supporting clinical trials or literature, and the underlying mechanistic rationale itself flags a significant safety concern — potassium-sparing diuretics may be relatively contraindicated in this condition due to hyperkalaemia risk in the presence of renal impairment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified — no UK marketing authorisation on record; pharmacologically, Triamterene is a potassium-sparing diuretic used for oedema/hypertension management |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the formal drug record (flagged as a High-severity data gap). However, the evidence pack's mechanistic rationale describes Triamterene as a **potassium-sparing diuretic** that blocks ENaC in the distal nephron, reducing sodium reabsorption and producing a mild antihypertensive effect. On this basis, there is a theoretical, class-level link to hypertensive conditions generally.

However, the specific pathophysiology of malignant renovascular hypertension is driven by renal artery stenosis and marked activation of the renin-angiotensin-aldosterone system (RAAS), typically accompanied by declining renal function. In this setting, a potassium-sparing diuretic carries an elevated risk of hyperkalaemia and may be **relatively contraindicated** rather than beneficial. The evidence pack itself explicitly characterises this mechanistic link as "weak, with the direction of effect in question." This should be read as a caution rather than a supportive rationale.

No clinical trials, literature, or real-world evidence for this specific drug-indication pairing were found, so the prediction currently rests entirely on the TxGNN knowledge-graph score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Triamterene has no UK marketing authorisation on record in this evidence pack (market status: **Not Marketed**; total licences: **0**). No product-level dosage form or approved indication text is currently available to summarise here.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Note:** The evidence pack flags TFDA/MHRA-equivalent labelling warnings and contraindications as a **Blocking** data gap (DG001), meaning formal safety screening (S1 stage) cannot proceed until this is resolved. In addition, the mechanistic rationale for the top prediction raises a specific concern about hyperkalaemia risk when potassium-sparing diuretics are used in patients with renovascular disease and reduced renal function — this should be treated as a safety signal requiring clinical review, not merely a data gap.

---

## Other Predicted Indications from This Evidence Pack

This evidence pack scored six candidate indications for Triamterene. For completeness, the other five are summarised below; none currently reach a level of evidence sufficient to support progression beyond a research question.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 2 | Malignant hypertensive renal disease | 99.89% | L5 | Hold | Same hyperkalaemia concern as rank 1; no supporting evidence |
| 3 | Pulmonary hypertension (unclear multifactorial mechanism, WHO Group 5) | 99.88% | L5 | Hold | No mechanistic or evidentiary support |
| 4 | Pulmonary hypertension due to lung disease and/or hypoxia (WHO Group 3) | 99.88% | L4 | Research Question | Literature is largely hypoxia/oncology basic-science, not diuretic- or Triamterene-specific; diuretics are a guideline-supported class-effect adjunct for right heart volume overload |
| 5 | Braddock (CHOPS) syndrome | 99.84% | L5 | Hold | No known pathophysiological link; assessed as likely knowledge-graph noise |
| 6 | Chronic pulmonary heart disease (cor pulmonale) | 99.75% | L4 | Research Question | Literature supports diuretics generally (including triamterene-containing combinations) for volume management in chronic heart failure; not indication-specific trial evidence |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (malignant renovascular hypertension) has no supporting clinical trials or literature (L5, model-score only), and its own mechanistic rationale raises a plausible safety contraindication (hyperkalaemia risk) rather than supporting evidence. Combined with a Blocking data gap on formal drug warnings/contraindications, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent product labelling (warnings, contraindications) to resolve the Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank or equivalent primary source (DG002)
- Original licensed indication and regulatory history for Triamterene, to properly frame the "original vs new indication" comparison
- Clinical or pharmacological assessment of hyperkalaemia risk specifically in renovascular/renal-impaired hypertensive populations before any further consideration of ranks 1–2
- If pursuing the more plausible volume-management candidates (ranks 4 and 6), Triamterene-specific (rather than class-level) clinical evidence in pulmonary hypertension/cor pulmonale populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

