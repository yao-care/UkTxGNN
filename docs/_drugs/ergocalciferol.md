---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ergocalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Ergocalciferol (vitamin D2) is conventionally used to prevent and treat vitamin D deficiency and related bone disorders. The TxGNN model's top-ranked prediction for this drug is **familial isolated hypoparathyroidism due to impaired PTH secretion**, with a very high similarity score, but currently **no clinical trials and no published literature** support this specific pairing — it is a computational association only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin D deficiency (general pharmacological use; no UK marketing authorisation is currently on file for this product) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack. Based on known pharmacology, ergocalciferol is a vitamin D2 compound requiring hepatic and renal hydroxylation to become biologically active; it is established for treating vitamin D deficiency and deficiency-related bone disease. Vitamin D and parathyroid hormone (PTH) both sit on the same calcium–phosphate homeostatic axis, which is the shared biological signal the TxGNN knowledge graph has picked up on.

However, the model's rationale for this specific candidate is weak: familial isolated hypoparathyroidism is conventionally managed with active vitamin D analogues (e.g. calcitriol), not with ergocalciferol, because the condition can involve impaired renal activation of vitamin D precursors. The high TxGNN score most likely reflects strong statistical co-occurrence between "vitamin D" and "PTH–calcium metabolism" concepts in the knowledge graph, rather than a clinically validated mechanistic hypothesis specific to ergocalciferol.

No clinical trials or literature record any direct investigation of ergocalciferol in this indication, which is consistent with this being a knowledge-graph-driven association rather than a research-supported hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

No UK marketing authorisation is currently on file for ergocalciferol in this dataset (market status: Not marketed; 0 licences recorded). As a result, no approved SmPC indication text is available to compare against the predicted new indication.

## Safety Considerations

Key warnings, contraindications and drug interaction data are not currently available for this product. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 (model-prediction-only) candidate with no supporting clinical trials or literature, and the proposed mechanism runs against standard clinical practice, which favours active vitamin D analogues over ergocalciferol for this condition. A Blocking data gap on SmPC warnings/contraindications also prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- SmPC warnings, contraindications and drug interaction data (currently a Blocking gap)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- At minimum, preclinical or mechanistic literature directly linking ergocalciferol to PTH-secretion disorders before this candidate can move beyond S0
- Consider prioritising other candidates from the same TxGNN run with stronger evidence bases instead — notably hypophosphatemia and hypophosphatemic rickets (both Evidence Level L3, "Proceed with Guardrails"), which have supporting clinical trials and/or literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

