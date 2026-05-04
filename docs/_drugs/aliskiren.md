---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Aliskiren: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Aliskiren is the world's first orally active direct renin inhibitor, originally developed and approved for the treatment of essential hypertension. The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5)**, with **no registered clinical trials** and **no publications** currently identified for this specific indication. This is a model-only prediction with no supporting clinical evidence, and a Hold decision is recommended at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (essential) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not currently authorised in the United Kingdom |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published information referenced within the evidence itself, Aliskiren is the world's first orally active direct renin inhibitor — it blocks the renin-angiotensin-aldosterone system (RAAS) at its most upstream rate-limiting step, namely the cleavage of angiotensinogen to angiotensin I by renin. Its blood pressure-lowering efficacy in essential hypertension has been demonstrated across multiple clinical trials involving more than 5,000 patients, with antihypertensive potency broadly comparable to ACE inhibitors, angiotensin receptor blockers (ARBs), and thiazide diuretics at standard doses.

WHO Group 5 pulmonary hypertension (PH) represents a heterogeneous category of conditions driven by unclear or multifactorial mechanisms, encompassing haematological disorders (e.g. haemolytic anaemias), systemic and metabolic conditions, and complex congenital diseases. RAAS activation is thought to contribute to pulmonary vascular constriction and structural remodelling through angiotensin II-mediated pathways — providing, in principle, a theoretical basis for upstream renin inhibition. However, this mechanistic link is exceptionally tenuous for Group 5 PH specifically, where the dominant drivers are disease-specific rather than vasomotor.

Crucially, no preclinical or clinical studies have been identified that test Aliskiren — or any direct renin inhibitor — specifically in WHO Group 5 PH. The high TxGNN prediction score (99.98%) most likely reflects the structural proximity of the "hypertension" node to the pulmonary hypertension cluster within the knowledge graph, rather than any indication-specific biological signal. This prediction does not, at this stage, meet the threshold for active investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Important context for research planning:** The ALTITUDE trial (a large randomised controlled trial of Aliskiren in patients with type 2 diabetes at high cardiovascular and renal risk) identified a significant safety signal: Aliskiren combined with an ACE inhibitor or ARB was associated with increased rates of ischaemic stroke, hypotension, hyperkalaemia, and renal impairment. This led to an FDA and EMA/MHRA contraindication for dual RAAS blockade in diabetic patients in 2012. Any future research programme involving Aliskiren must account for this safety profile from the outset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no relevant published literature supporting the use of Aliskiren in pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5). The high TxGNN score is almost certainly driven by graph proximity to the hypertension node rather than a biologically specific signal, and no plausible mechanistic link for Group 5 PH has been established.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) obtained from DrugBank API or primary pharmacological literature
- MHRA Summary of Product Characteristics (SmPC) to clarify approved indications, contraindications, and key warnings, including the ALTITUDE-derived dual RAAS blockade restriction
- Targeted literature search for Aliskiren or renin inhibition specifically in pulmonary vascular biology (in vitro or in vivo models)
- Biological plausibility review by a pulmonary hypertension specialist to determine whether Group 5 PH is a scientifically justifiable focus
- Regulatory status clarification: Aliskiren (Rasilez®) held a European Marketing Authorisation but was voluntarily withdrawn from several markets following the ALTITUDE safety signal — MHRA product status should be verified before any UK-based study is designed

---

> **Note on other predicted indications in this Evidence Pack:**
> Six additional TxGNN predictions were evaluated. The most evidenced is **cerebrovascular disorder** (rank 7, score 99.19%, Evidence Level L3): this includes a terminated Phase 2/3 MRI trial (ALPINE; [NCT01417104](https://clinicaltrials.gov/study/NCT01417104)) and 13 publications, including animal studies demonstrating neuroprotection with renin inhibition and critical ALTITUDE safety analyses highlighting increased ischaemic stroke risk with combined RAAS blockade. **Malignant renovascular hypertension** (rank 4, L4) and **chronic pulmonary heart disease** (rank 6, L4) also carry some mechanistic plausibility with limited pharmacological literature. All currently carry a Research Question designation pending further evidence generation, and all require resolution of the ALTITUDE safety signal before clinical translation.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

