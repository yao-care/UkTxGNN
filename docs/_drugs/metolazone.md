---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 5
---

# Metolazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metolazone: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic pharmacologically used to manage hypertension and oedema by inhibiting the Na-Cl symporter in the distal convoluted tubule. The TxGNN model predicts a possible role in **Malignant Renovascular Hypertension**, but this prediction is currently supported by **no clinical trials** and **no published literature**, resting entirely on knowledge-graph inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset — no formal approved-indication text is available (no UK marketing authorisation on record) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Metolazone is not available in this evidence pack (flagged as a High-severity data gap). However, the pack's own rationale text confirms Metolazone is a **thiazide-like diuretic** that inhibits the Na-Cl cotransporter in the distal convoluted tubule, producing a well-established antihypertensive and diuretic effect — this is consistent with its general pharmacological class.

Malignant renovascular hypertension is a specific pathological subtype driven by renal artery stenosis and a high-renin state. In this condition, the core mechanistic treatments are ACE inhibitors/ARBs or renal revascularisation, not diuretics in isolation. While Metolazone's antihypertensive action provides a superficial rationale for symptomatic blood pressure lowering, it does not address the primary renin-angiotensin-driven pathophysiology, and the evidence pack explicitly notes there is no direct supporting evidence for this specific indication.

Two related predictions in this dataset — malignant hypertensive renal disease (rank 2, L4) — are somewhat more plausible, since Metolazone has a recognised clinical property of maintaining diuretic/antihypertensive activity even at low GFR, and is commonly co-administered with loop diuretics to manage diuretic resistance and volume overload in renal impairment. This is background pharmacological knowledge rather than evidence specific to this dataset, and it too lacks indication-specific trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: A separate lower-ranked prediction (pulmonary hypertension due to lung disease/hypoxia, rank 4) returned 20 PubMed hits, but all are generic "hypoxia" biology/oncology papers with no connection to Metolazone or the disease indication — these appear to be keyword-matching artefacts rather than genuine supporting evidence, and are not included here.*

---

## UK Market Information

Metolazone does not currently hold a marketing authorisation in the United Kingdom according to this dataset (0 licences on record). No product name, dosage form, or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** TFDA/UK product-label warnings and contraindications are recorded as a **Blocking** data gap in this evidence pack — this must be resolved before any safety evaluation (Stage S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN knowledge-graph inference (Evidence Level L5) with no supporting clinical trials or literature, and the disease-specific pathophysiology (renal-artery-stenosis-driven, high-renin hypertension) is not well matched to a diuretic's core mechanism. Combined with the absence of UK marketing authorisation and a Blocking-severity safety data gap, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Structured mechanism-of-action data from DrugBank (High-severity gap, DG002)
- UK SmPC/BNF warnings and contraindications (Blocking gap, DG001) — required before any S1 safety screening
- Targeted literature/trial search specific to renovascular or renal hypertensive disease (current PubMed results are non-specific and not usable as evidence)
- Consideration of the related rank-2 candidate (malignant hypertensive renal disease, L4), which has a stronger pharmacological rationale via Metolazone's known efficacy in renal impairment, as a more promising research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

