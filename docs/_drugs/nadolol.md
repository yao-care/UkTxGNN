---
layout: default
title: Nadolol
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 5
---

# Nadolol
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

# Nadolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nadolol is a non-selective β-adrenoceptor antagonist whose established clinical use is in essential hypertension (confirmed regulatory indication text is not available in this evidence pack). The TxGNN model predicts a possible role in **Malignant Hypertensive Renal Disease**, but this prediction is currently supported by **no clinical trials** and **no published literature**, and by only a general mechanistic argument.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in regulatory data (no licences on file); rationale text indicates historical use in essential hypertension |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no clinical/literature evidence) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on the repurposing rationale supplied, Nadolol is a **non-selective β-adrenoceptor antagonist**; its blood-pressure-lowering effect (reduced cardiac output, suppression of renin release) is well established in essential hypertension.

Malignant hypertensive renal disease is a severe hypertensive emergency with renal involvement. The mechanistic argument for extending Nadolol to this indication is that a drug which lowers blood pressure and suppresses renin release could, in principle, contribute to blood pressure control in this setting. However, this is a **general mechanism-of-action extrapolation by TxGNN**, not evidence specific to this disease subtype. Malignant hypertension is typically managed with rapid-acting intravenous antihypertensives, and non-selective β-blockade is not a first-line approach.

It is also important to note that several other diseases predicted for this drug (ranked #3 and #4 in this evidence pack — pulmonary hypertension phenotypes) carry a **theoretical safety concern rather than an evidence gap**: non-selective β-blockade can reduce cardiac output and block β2 receptors, which may worsen right heart function or bronchoconstriction in patients with pulmonary hypertension or hypoxic lung disease. This suggests the underlying TxGNN signal may reflect proximity within cardiovascular-regulation network nodes rather than genuine therapeutic suitability, reinforcing the need for caution before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Nadolol currently holds **no UK marketing authorisations** in this dataset (total licences: 0; market status: Not marketed). No product-specific licence or approved indication text is available for review.

---

## Other Predicted Indications (Lower Priority, Same Evidence Pack)

| Rank | Disease | TxGNN Score | Evidence | Key Concern |
|------|---------|-------------|----------|--------------|
| 2 | Malignant renovascular hypertension | 99.59% | None | Standard treatment is revascularisation or ACEI/ARB; non-selective β-blockade is not a standard pathway |
| 3 | Pulmonary hypertension (unclear/multifactorial) | 99.53% | None | Possible **safety signal**: risk of worsening right heart function |
| 4 | Pulmonary hypertension due to lung disease/hypoxia | 99.53% | None | Possible **safety signal**: β2 blockade may worsen bronchoconstriction/hypoxic response |
| 5 | Braddock (CHOPS) syndrome | 99.43% | None | No known mechanistic link; likely a TxGNN false positive |

---

## Safety Considerations

- **Key mechanistic safety signal**: For the pulmonary hypertension–related predictions (ranks 3–4), non-selective β-blockade carries a theoretical risk of worsening right heart function and bronchoconstriction; these should be treated as potential contraindications rather than repurposing opportunities pending further review.
- No TFDA/SmPC-sourced warnings, contraindications, or drug interaction data are currently available for Nadolol in this evidence pack (flagged as a **Blocking** data gap — DG001).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (malignant hypertensive renal disease) has no supporting clinical trials or literature (Evidence Level L5), and a Blocking-severity safety data gap (missing TFDA warnings/contraindications) prevents even an initial safety assessment. Several lower-ranked predictions for this drug carry plausible mechanistic safety concerns rather than mere evidence gaps.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/SmPC warnings and contraindications for Nadolol
- Resolve DG002: confirm mechanism of action via DrugBank API
- Identify at least preclinical or observational evidence specific to malignant hypertensive renal disease before advancing beyond S0
- Explicit safety review of β-blockade risk in any pulmonary hypertension–related candidate before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

