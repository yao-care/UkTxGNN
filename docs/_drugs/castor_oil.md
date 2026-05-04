---
layout: default
title: Castor Oil
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 0
---

# Castor Oil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Castor Oil: Drug Repurposing Evaluation — No Predictions Available

## One-Sentence Summary

Castor oil (DrugBank: DB11113) is a plant-derived substance with historically established uses as a stimulant laxative and topical emollient, and is not currently authorised in the UK under an MHRA marketing authorisation.
The current TxGNN model run has **not generated any predicted new indications** for this compound, and critical data gaps in mechanism of action and regulatory information mean that a full repurposing evaluation cannot be completed at this stage.
No evidence level can be assigned until predictions and supporting data are available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No recorded indications in current dataset |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction is Available

The TxGNN knowledge graph and deep learning pipeline did not return any repurposing candidates for castor oil in the current run. This is likely due to one or more of the following factors:

1. **Complex mixture, not a single molecular entity**: Castor oil is a plant-derived triglyceride mixture obtained from *Ricinus communis*, composed primarily of ricinoleic acid (~90%) alongside other fatty acids. Knowledge graph models such as TxGNN are optimised for single chemical entities; complex natural product mixtures may be poorly represented in the underlying graph topology, reducing the model's ability to traverse meaningful disease-drug edges.

2. **Missing mechanism of action (MOA) data**: Without a formally defined molecular target or pathway in the DrugBank record, the graph traversal algorithm has insufficient anchor points from which to infer related therapeutic indications.

3. **No approved indication anchor**: The absence of any recorded approved indication in the dataset removes a key signal that TxGNN uses to identify biologically adjacent disease nodes.

Currently, detailed mechanism of action data is not available for castor oil in this Evidence Pack. Based on established pharmacological knowledge, castor oil is hydrolysed in the small intestine to release ricinoleic acid, which stimulates intestinal peristalsis via activation of EP3 prostanoid receptors on intestinal smooth muscle — a mechanism distinct from most repurposable small molecules. Any assessment of its applicability to other conditions would require a full MOA review sourced directly from the DrugBank API (DB11113) and primary literature.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted indications and has blocking-severity data gaps in both safety and mechanism of action data; proceeding with any repurposing evaluation or clinical feasibility assessment would be premature and potentially unsafe.

**To proceed, the following is needed:**

- **Re-run TxGNN pipeline** after confirming that DB11113 (castor oil) is correctly represented as a mappable entity in the knowledge graph; consider whether ricinoleic acid (the primary active component) should be submitted as the query molecule instead
- **Retrieve MOA data** from the DrugBank API for DB11113, including molecular targets, pathways, and pharmacodynamic properties
- **Obtain UK MHRA regulatory data**: confirm whether any castor oil-containing products hold a current Marketing Authorisation in the UK (including unlicensed specials or borderline products), retrieve the relevant SmPC, and record approved indication text
- **Complete safety assessment**: extract key warnings, contraindications, and drug–drug interaction data from the SmPC and DrugBank
- **Clarify the drug entity**: determine whether TxGNN evaluation should proceed for castor oil as a whole, or for its principal active constituent ricinoleic acid (DrugBank DB03364), which may yield more meaningful graph-based predictions

> ⚠️ **Research use only.** This evaluation is intended for research reference purposes only and does not constitute medical advice. Any repurposing candidates identified must undergo appropriate clinical validation before application. All content should be reviewed alongside current MHRA guidance and the BNF.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

