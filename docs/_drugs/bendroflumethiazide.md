---
layout: default
title: Bendroflumethiazide
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 5
---

# Bendroflumethiazide
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

# Bendroflumethiazide: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bendroflumethiazide is a thiazide diuretic of the benzothiadiazine class, established in clinical practice for the management of hypertension and oedema. The TxGNN model predicts it may have relevance to **Malignant Hypertensive Renal Disease**, with a prediction confidence score of **99.88%**. However, there are currently **no registered clinical trials** and **no directly relevant published literature** supporting this repurposing direction — evidence rests solely on class-level mechanistic inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in current dataset (thiazide diuretic; clinically used for hypertension and oedema) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per current dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Bendroflumethiazide is a thiazide (benzothiadiazine) diuretic that acts by inhibiting the sodium–chloride co-transporter (SLC12A3) in the distal convoluted tubule of the kidney. This reduces tubular reabsorption of sodium and water, lowering circulating blood volume and producing a sustained antihypertensive effect. This mechanism of action provides a class-level, indirect pharmacological rationale for the TxGNN prediction — the knowledge graph associates thiazide diuretics with hypertensive disease nodes, which in turn connect to hypertensive renal complications.

Malignant hypertensive renal disease is a severe, potentially life-threatening condition characterised by rapidly accelerating blood pressure causing acute renal injury, with pathological features including fibrinoid necrosis and thrombotic microangiopathy. It represents a hypertensive emergency. In this acute setting, current clinical guidelines recommend intravenous agents such as labetalol or sodium nitroprusside, rather than oral thiazide diuretics, for prompt blood pressure control.

There are two particularly important limitations to the biological plausibility of this prediction. First, thiazide diuretics exhibit substantially reduced antihypertensive efficacy when the glomerular filtration rate (GFR) falls below approximately 30 mL/min — a threshold commonly breached in malignant hypertensive renal disease. Second, the volume depletion associated with thiazide use may compromise renal perfusion in an already compromised kidney, raising safety concerns in this specific patient population. The high TxGNN score most likely reflects topological generalisation within the knowledge graph (thiazide → systemic hypertension → hypertensive renal disease), rather than a direct or targeted mechanistic link to this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No marketing authorisations for Bendroflumethiazide were identified in the current dataset. This may reflect a data collection limitation rather than the drug's true regulatory status; clinicians should verify current licensing information via the MHRA product licence register and the British National Formulary (BNF). Note that Bendroflumethiazide-containing combination products (e.g., co-tenidone) may carry separate authorisations not captured here.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is based solely on knowledge graph topology and pharmacological class-level inference; there are no clinical trials, no targeted literature, and no direct mechanistic evidence supporting bendroflumethiazide for malignant hypertensive renal disease. Critically, the clinical characteristics of this indication — a hypertensive emergency with acute kidney injury and severely reduced GFR — are precisely the conditions under which thiazide diuretics are least likely to be effective or clinically safe.

**To proceed, the following is needed:**

- Verification of MHRA marketing authorisation status via the MHRA database and BNF, including any combination products
- Detailed mechanism of action data from DrugBank (currently a data gap)
- Full SmPC / MHRA product information to complete contraindication and warning assessment
- Pharmacokinetic and pharmacodynamic data on bendroflumethiazide efficacy and safety at low GFR (< 30 mL/min)
- Targeted literature search specifically investigating thiazide diuretics in the context of malignant hypertensive nephropathy
- Expert nephrology and clinical pharmacology consultation before any further development steps are considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

