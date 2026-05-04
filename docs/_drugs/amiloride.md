---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 6
---

# Amiloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Amiloride: From Hypertension and Oedema to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron, used clinically to manage hypertension and oedema — most commonly in combination with loop or thiazide diuretics.
The TxGNN model predicts it may have therapeutic activity in **Malignant Hypertensive Renal Disease**, with a prediction score of **99.82%**.
However, there are currently **no registered clinical trials** and **no relevant publications** directly supporting this specific indication, placing the evidence at **Level L5** — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and oedema (potassium-sparing diuretic; not currently licensed as a standalone product in the UK) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 — model prediction only; no clinical studies identified |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, amiloride is a pyrazine-derived potassium-sparing diuretic that selectively blocks ENaC in the collecting duct of the distal nephron. This reduces tubular sodium reabsorption and, consequently, circulating blood volume — producing antihypertensive and natriuretic effects whilst preserving serum potassium. In clinical practice, amiloride is most often used in combination with furosemide or hydrochlorothiazide to mitigate hypokalaemia in patients managed for hypertension, chronic oedema, and heart failure.

Malignant hypertensive renal disease is a hypertensive emergency defined by severe, rapidly escalating blood pressure causing acute renal injury, frequently accompanied by hypertensive retinopathy, microangiopathic haemolytic anaemia, and encephalopathy. The TxGNN model likely generates a high prediction score by drawing on the network proximity between amiloride's ENaC-blocking properties and hypertension-related renal pathology nodes within the knowledge graph. Whilst there is a broad biological link — ENaC inhibition does reduce blood pressure and decrease renal tubular sodium load — this mechanistic pathway is generic rather than specific to malignant hypertensive nephropathy.

Critically, the clinical plausibility for amiloride as primary therapy in this emergency setting is weak. Malignant hypertension requires rapid, controlled blood pressure reduction using intravenous agents such as labetalol, hydralazine, or sodium nitroprusside. An oral potassium-sparing diuretic acting over hours is poorly positioned for this acute context. The high TxGNN score is likely a function of broad ENaC–hypertension network association rather than a targeted mechanistic prediction, and must be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.82%), there is no clinical trial or published literature evidence for amiloride in malignant hypertensive renal disease (Level L5), and the mechanistic rationale does not support its use in this acute hypertensive emergency — a context requiring intravenous antihypertensive therapy rather than an oral potassium-sparing diuretic.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) data from DrugBank or current SmPC, confirming ENaC-specific pharmacodynamic profile
- UK safety data from MHRA (key warnings and contraindications), particularly regarding hyperkalaemia risk and renal impairment thresholds
- Preclinical evidence specifically linking ENaC inhibition to pathophysiological mechanisms in malignant hypertensive nephropathy (e.g., tubular injury models, Na⁺ overload in endothelial damage)
- Pharmacokinetic data confirming adequate bioavailability and dose–response in the context of acute renal injury, where oral absorption may be unreliable
- Expert nephrology opinion on whether adjunctive potassium-sparing diuresis could have a defined supportive role within a broader intravenous treatment protocol

---

> **Note on alternative predictions in this Evidence Pack:** Of the six TxGNN predictions evaluated, **chronic pulmonary heart disease (cor pulmonale)** (Rank 6; Evidence Level L3; Recommendation: Research Question) presents the most clinically coherent case for further investigation. Two controlled studies — a pilot crossover RCT (PMID [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/), 1991) demonstrating haemodynamic improvement with amiloride in chronic congestive heart failure on digoxin, and a double-blind randomised crossover trial (PMID [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/), 1987) comparing frusemide–amiloride combination against captopril in mild heart failure — provide direct pharmacological support. The use of amiloride as a potassium-sparing diuretic in managing fluid overload and right heart strain in cor pulmonale aligns directly with its established clinical role, and this indication merits a dedicated, more detailed evaluation report.

---

*This report is for research and informational purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Suspected adverse reactions should be reported via the MHRA Yellow Card Scheme at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

