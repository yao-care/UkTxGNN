---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 1
---

# Carbocisteine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Carbocisteine: From Respiratory Mucolysis to Gout

## One-Sentence Summary

Carbocisteine is a mucolytic agent used to reduce sputum viscosity and aid mucus clearance in respiratory conditions such as chronic bronchitis and COPD. The TxGNN model predicts it may have potential utility in **Gout**, achieving a high prediction score of **99.67%**. However, this prediction is currently supported by **no clinical trials** and **no published literature**, placing it at model-only evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucolytic agent for respiratory conditions (no MHRA licence on record) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Carbocisteine is a mucolytic (sulphydryl-containing) agent whose primary mechanism involves modification of disulphide bonds in mucin glycoproteins, thereby reducing sputum viscosity and improving mucus clearance in the airways. It also possesses antioxidant properties and mild anti-inflammatory activity through inhibition of the NF-κB signalling pathway.

The proposed mechanistic link to gout is indirect and largely theoretical. Gout is driven by monosodium urate crystal deposition, which triggers acute inflammation via activation of the NLRP3 inflammasome. Carbocisteine's thiol (–SH) group could theoretically interfere with NLRP3 inflammasome activation — a central pathway in acute gouty inflammation — however, no direct experimental evidence currently supports this hypothesis. Its antioxidant properties might also indirectly reduce oxidative-stress-mediated uric acid production through indirect modulation of xanthine oxidase activity, but again without direct mechanistic data.

The high TxGNN knowledge graph score (0.9967) is most likely driven by shared network topology features — such as common nodes related to chronic inflammation and metabolic dysregulation — rather than direct mechanistic similarity between carbocisteine's mucolytic action and gout pathophysiology. The overall mechanistic rationale remains weak, and clinical validation is entirely absent at this stage.

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
Although the TxGNN model assigns Carbocisteine a high prediction score for gout (99.67%), this is unsupported by any clinical trials, published literature, or established mechanistic evidence; the predicted link remains speculative and entirely unvalidated.

**To proceed, the following is needed:**

- Preclinical studies examining the effect of carbocisteine (or analogous thiol compounds) on NLRP3 inflammasome activity in urate crystal-induced inflammation models
- Full mechanism of action data from DrugBank to confirm antioxidant and anti-inflammatory molecular targets
- A structured literature review to identify any *in vitro* or animal studies linking carbocisteine to uric acid metabolism or gout-related pathways
- Clarification of UK regulatory status via MHRA and the BNF — carbocisteine may be available in the UK under a product not captured in the current dataset
- SmPC-level safety and contraindication data before any clinical evaluation or prescribing consideration can proceed
- Upgrading from L5 to at least L4 (preclinical evidence) before this candidate can be considered for further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

