---
layout: default
title: Nicardipine
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 5
---

# Nicardipine
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

# Nicardipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

> Nicardipine is a dihydropyridine calcium channel blocker; no formal original-indication or mechanism-of-action data is recorded in this evidence pack, though it is widely known for use in hypertensive emergencies.
> The TxGNN model's top-ranked prediction is **Pulmonary Hypertension with Unclear Multifactorial Mechanism**,
> but this is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags safety concerns rather than therapeutic support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (drug class: dihydropyridine calcium channel blocker) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Nicardipine in this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic notes accompanying the predictions, Nicardipine is understood to be a dihydropyridine calcium channel blocker whose core pharmacology is systemic vasodilation and blood pressure reduction; the intravenous formulation is widely used in clinical practice for hypertensive emergencies.

For the top-ranked prediction — pulmonary hypertension with unclear multifactorial mechanism — the model's own rationale is **not supportive**: calcium channel blockers are only effective in a small, vasoreactivity-positive subset of Group 1 idiopathic pulmonary arterial hypertension, identified only after formal acute vasodilator testing, and this indication label is too ambiguous to confirm that subgroup. The rank 2 candidate (pulmonary hypertension due to lung disease/hypoxia, WHO Group 3) is explicitly flagged in the evidence as **potentially harmful** — non-selective vasodilators can blunt hypoxic pulmonary vasoconstriction, worsening V/Q mismatch and hypoxaemia — and the rationale recommends this association be excluded rather than pursued.

The more mechanistically coherent candidates in this dataset are ranked 3 and 4 (malignant renovascular hypertension; malignant hypertensive renal disease), where Nicardipine's established IV use in hypertensive emergency provides a plausible pharmacological link. However, these remain at evidence level L4 with zero supporting trials or literature in this pack, and rank 5 (Braddock syndrome) is most likely knowledge-graph noise with no known pathophysiological connection to calcium channel blockade.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(This applies to all five predicted indications in this evidence pack, including malignant renovascular hypertension and malignant hypertensive renal disease.)*

---

## Literature Evidence

Currently no related literature available.

*(No publications are recorded for any of the five predicted indications.)*

---

## UK Market Information

Nicardipine is **not marketed** in the UK per this evidence pack, and no marketing authorisations are currently on file (0 licenses recorded). No dosage form or approved-indication data is available for reference.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** MHRA-equivalent labelled warnings and contraindications for Nicardipine are recorded as a **Blocking** data gap (DG001) in this evidence pack — this means an initial safety screen (S1) cannot currently be completed, and no safety table can be populated from source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications rest on TxGNN model scores alone, with zero supporting clinical trials or literature (evidence level L4–L5). The two highest-scoring predictions are mechanistically weak or actively flagged as potentially harmful rather than therapeutic. The drug also has no current UK marketing authorisation, and a Blocking-severity gap in labelled safety data (warnings/contraindications) prevents any meaningful safety evaluation at this stage.

**To proceed, the following is needed:**
- MHRA/SmPC-equivalent warnings and contraindications (resolve DG001, Blocking)
- Confirmed mechanism of action from DrugBank or equivalent source (resolve DG002)
- Independent literature/trial search specifically for malignant renovascular hypertension and malignant hypertensive renal disease (the more mechanistically plausible candidates), since none are currently captured in this pack
- Re-evaluation of the pulmonary hypertension candidates against current WHO Group 1/Group 3 clinical guidance before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

