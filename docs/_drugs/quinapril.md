---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 5
---

# Quinapril
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

Using the report structure specified in the prompt to produce the following evaluation.

---

# Quinapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Quinapril is an ACE inhibitor conventionally associated with hypertension management, although this Evidence Pack contains no confirmed record of its original licensed indication. The TxGNN model predicts a possible link to **Malignant Renovascular Hypertension**, but this pairing is supported by **no clinical trials** and **no published literature**, and the model's own mechanistic rationale flags a plausible safety concern rather than a genuine therapeutic signal.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in source data; Quinapril is pharmacologically known as an ACE inhibitor, a class typically indicated for hypertension |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| UK Market Status | Not marketed in the UK |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Quinapril in this Evidence Pack. Based on known drug-class information (as noted within the model's own rationale), Quinapril is an ACE inhibitor, working by suppressing the renin-angiotensin-aldosterone system (RAAS) to lower blood pressure. This class-level mechanism is the sole basis for the predicted association with renovascular hypertension.

However, the relationship between the original use (presumed hypertension) and the predicted indication is mechanistically double-edged. Malignant renovascular hypertension frequently occurs in the context of bilateral renal artery stenosis, a setting in which ACE inhibitors are well recognised to carry a **relative contraindication** rather than a therapeutic benefit, due to the risk of precipitating acute renal failure when RAAS-dependent glomerular perfusion is withdrawn. The Evidence Pack's own repurposing rationale makes this point explicitly.

In short, this prediction appears to be a TxGNN score-driven pairing based on pharmacological class similarity, rather than a validated repurposing opportunity. The same caveat applies across the other candidate indications in this pack (malignant hypertensive renal disease, two subtypes of pulmonary hypertension, and Braddock syndrome) — all are scored L5 with no supporting trials, and the literature identified for the pulmonary hypertension candidates relates to general hypoxia biology rather than to Quinapril or pulmonary vascular disease specifically. All five candidates carry a model-generated "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Quinapril currently holds no marketing authorisations in the UK — the market status on record is "Not marketed" with 0 licences. No product name, dosage form, or approved indication text is available to summarise.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (and all four other TxGNN-ranked candidates) is supported by no clinical trials and no relevant literature, placing all at Evidence Level L5 (model prediction only). Compounding this, the mechanistic rationale itself suggests renovascular hypertension with bilateral renal artery stenosis is more plausibly a **safety risk setting** for ACE inhibitors than a genuine new indication, and Quinapril has no current UK marketing authorisation to build on.

**To proceed, the following is needed:**
- Confirmed mechanism of action and original licensed indication(s) for Quinapril from an authoritative source (e.g. DrugBank, SmPC)
- UK/MHRA licensing status confirmation, including whether any historical authorisation existed
- SmPC-derived warnings and contraindications, particularly regarding renal artery stenosis and renal function monitoring
- Disease-specific preclinical or clinical evidence directly addressing Quinapril's use in renovascular hypertension before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

