---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: From Hypertension and Heart Failure to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a non-selective beta- and alpha-1 adrenergic receptor antagonist, established in the management of hypertension, chronic heart failure, and angina pectoris.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (TxGNN score: 99.55%).
However, **no dedicated clinical trials or direct literature** currently support this specific repurposing direction, placing the prediction at an early mechanistic hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; chronic heart failure; angina pectoris |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| UK Market Status | No authorisation records in current dataset (verify via MHRA) |
| Number of Marketing Authorisations | 0 (in current dataset) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacological knowledge, Carvedilol is a combined non-selective beta-adrenergic (β1 and β2) and alpha-1 adrenergic receptor antagonist, with additional antioxidant properties (reactive oxygen species scavenging). This dual receptor blockade distinguishes it from conventional beta-blockers and provides the mechanistic basis for the TxGNN prediction.

In malignant renovascular hypertension, stenosis of a renal artery activates the juxtaglomerular apparatus and drives marked renin hypersecretion, resulting in an overactivated renin-angiotensin-aldosterone system (RAAS) and a severe, rapidly progressive hypertensive crisis with target organ damage. Carvedilol's alpha-1 blockade theoretically reduces renal afferent arteriolar resistance and systemic vascular resistance, whilst its beta-1 blockade suppresses juxtaglomerular renin release, thereby attenuating the underlying RAAS overactivation. Additionally, its antioxidant properties may reduce hypertension-induced renal oxidative stress injury. Notably, the second-ranked prediction — malignant hypertensive renal disease — carries an identical TxGNN score (99.55%), suggesting the model treats these two closely related conditions as overlapping nodes within the knowledge graph; both share the same mechanistic rationale.

It is important to note that malignant renovascular hypertension is a medical emergency, and current standard of care relies on intravenous antihypertensive agents (e.g., sodium nitroprusside, labetalol, nicardipine). No dedicated studies have examined the role of oral alpha/beta-blockers such as Carvedilol in this acute context. The TxGNN prediction therefore reflects mechanistic plausibility rather than demonstrated clinical benefit, and represents a hypothesis requiring dedicated investigation before any clinical translation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> A search of ClinicalTrials.gov and the ICTRP for Carvedilol in malignant renovascular hypertension returned zero results (query date: 26 March 2026).

---

## Literature Evidence

Currently no related literature available.

> A PubMed search combining Carvedilol with malignant renovascular hypertension returned zero results (query date: 26 March 2026). Twenty publications were retrieved for the related query "Carvedilol + pulmonary hypertension owing to lung disease/hypoxia" (the fourth-ranked predicted indication), but these addressed general hypoxia biology and were not directly relevant to the top predicted indication. No publications with confirmed relevance to the Carvedilol–malignant renovascular hypertension pair were identified.

---

## UK Market Information

No MHRA marketing authorisation records for Carvedilol are present in the current Evidence Pack dataset (total licences recorded: 0).

> **Important:** Carvedilol is a well-established cardiovascular medicine in UK clinical practice (e.g., Eucardic®; multiple generic formulations hold MHRA authorisation). The absence of records in this dataset is likely a data collection gap rather than a true reflection of market status. Clinicians should verify authorised indications, the current SmPC, and prescribing information via the [MHRA product information portal](https://products.mhra.gov.uk/) and the BNF before any clinical use.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct clinical trial or literature evidence supporting Carvedilol specifically for malignant renovascular hypertension; the TxGNN prediction (99.55%) is driven by mechanistic plausibility via dual alpha-1/beta adrenergic blockade and RAAS suppression, but the acute, life-threatening nature of this condition — combined with the established intravenous standard of care — means an oral repurposing strategy cannot be advanced without dedicated prospective evidence.

**To proceed, the following is needed:**
- Formal MOA documentation retrieved from DrugBank or primary pharmacological literature to support the mechanistic rationale
- Preclinical or translational studies examining Carvedilol in renovascular hypertension models (e.g., two-kidney, one-clip rat model)
- Exploration of a potential chronic maintenance or secondary-prevention role (post-acute stabilisation phase), where oral agents may be more clinically feasible than in the acute emergency setting
- Full safety assessment via the current MHRA SmPC: contraindications, key warnings, and drug–drug interactions
- Confirmation of UK marketing authorisation status and currently approved indications via the MHRA portal to resolve the dataset gap
- Evidence Pack refresh to populate MHRA licence records and SmPC-derived safety data before progression to formal repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

