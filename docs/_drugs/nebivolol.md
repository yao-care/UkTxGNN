---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 5
---

# Nebivolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nebivolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Nebivolol is a highly selective β1-blocker with additional nitric oxide (NO)-mediated vasodilatory properties, originally used to treat hypertension.
> The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
> but this direction is currently supported by **no registered clinical trials** and **no published literature** — the prediction rests on mechanistic extrapolation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from repurposing rationale; no formal indication text available) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 (mechanism/preclinical reasoning only; no clinical or trial evidence) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for nebivolol is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale supplied alongside the prediction, nebivolol is described as a highly selective β1-adrenergic receptor antagonist that additionally promotes vasodilation via endothelial nitric oxide release — distinguishing it pharmacologically from older, non-selective beta-blockers.

The predicted indication, malignant hypertensive renal disease, is mechanistically continuous with nebivolol's established use in hypertension: both involve blood pressure control as the central therapeutic goal, and the disease represents a severe renal manifestation of poorly controlled hypertension rather than a distinct pathological target. However, malignant hypertension is a hypertensive emergency typically managed acutely with intravenous agents (e.g. labetalol, nicardipine); oral agents such as nebivolol would, at most, play a role in subsequent maintenance therapy rather than acute management. This means the prediction reflects a disease-subtype extension within the same pharmacological pathway, rather than a genuinely novel mechanism of action being repurposed.

No clinical trials or published literature currently support this specific application, and the evidence pack does not provide comparator data (e.g. against ACE inhibitors, which have stronger evidence in hypertensive renal disease). The prediction should therefore be regarded as a research hypothesis requiring dedicated investigation rather than an actionable clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Nebivolol currently holds no marketing authorisation captured in this evidence pack, and market status is recorded as **not marketed**. No product licences, dosage forms, or approved indication text are available for review.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications, and drug–drug interaction data for nebivolol were not available in this evidence pack (flagged as a Blocking-severity data gap, DG001). This gap must be resolved before any safety-related decision can be made.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by mechanistic reasoning (L4, S1 "Research Question" stage) with no clinical trials or literature specific to nebivolol in this indication, and a Blocking-severity safety data gap (missing warnings/contraindications) currently prevents even an initial safety screen. The drug is also not marketed in the UK, so there is no existing regulatory foothold to build on.

**To proceed, the following is needed:**
- TFDA/MHRA SmPC warnings and contraindications to unblock safety screening (DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Dedicated literature/trial search specific to nebivolol in malignant hypertensive renal disease (current PubMed results for a related candidate were dominated by generic "hypoxia biology" papers unrelated to this drug, and should not be treated as supporting evidence)
- Comparative evidence against standard-of-care agents (e.g. ACE inhibitors, IV antihypertensives) for this specific renal indication

*Other candidates in this evidence pack (malignant renovascular hypertension, PH due to lung disease/hypoxia, PH with unclear mechanism, Braddock syndrome) were reviewed and are assessed as weaker or non-credible signals — largely mechanism-only extrapolations or likely knowledge-graph noise — and are not recommended for further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

