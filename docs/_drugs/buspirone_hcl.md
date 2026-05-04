---
layout: default
title: Buspirone Hcl
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 0
---

# Buspirone Hcl
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

# Buspirone HCl: Generalised Anxiety Disorder — Repurposing Evaluation Incomplete

## One-Sentence Summary

Buspirone HCl is a non-benzodiazepine anxiolytic used in the management of generalised anxiety disorder (GAD), acting as a partial agonist at serotonin 5-HT1A receptors and, to a lesser extent, dopamine D2 receptors. The current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, as critical upstream data — including the DrugBank identifier, original indications, and MHRA authorisation records — were not successfully retrieved by the data pipeline. A formal repurposing evaluation cannot be completed until these gaps are resolved; this report serves as a preliminary holding summary only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Generalised Anxiety Disorder (background knowledge — not confirmed in Evidence Pack) |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction not generated; no supporting studies identified |
| UK Market Status | Not marketed (data retrieval failure — manual verification required) |
| Number of Marketing Authorisations | 0 (likely a pipeline data gap; generic buspirone tablets are understood to be available in the UK) |
| Recommended Decision | **Hold** |

> **Important note on UK market status:** The Evidence Pack records zero MHRA marketing authorisations for Buspirone HCl. This is almost certainly a data collection failure rather than a true market absence — generic buspirone hydrochloride tablets (e.g., 5 mg and 10 mg) are listed in the British National Formulary (BNF) and have been available in the UK. Manual verification against the [MHRA Product Licence Register](https://products.mhra.gov.uk/) is required before any regulatory conclusions are drawn.

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information for buspirone hydrochloride. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Buspirone HCl is critically incomplete: no TxGNN repurposing predictions were generated, no DrugBank identifier was resolved, MHRA authorisation records could not be retrieved, and mechanism of action and safety data are absent. It is not possible to produce a responsible repurposing evaluation without these foundational data elements.

**To proceed, the following is needed:**

- **Confirm DrugBank identifier**: Buspirone HCl is expected to map to DrugBank entry **DB00490**. Confirm this via the DrugBank API and relink the Evidence Pack accordingly.
- **Re-run TxGNN predictions**: Once the DrugBank ID is confirmed, re-run the prediction pipeline to generate repurposing candidate indications with associated TxGNN scores.
- **Retrieve MOA and pharmacology data**: Query the DrugBank API for mechanism of action, pharmacodynamics, and toxicity data for DB00490.
- **Verify MHRA authorisations**: Manually search the [MHRA Product Licence Register](https://products.mhra.gov.uk/) for all current UK marketing authorisations for buspirone hydrochloride and update `taiwan_regulatory.licenses` accordingly.
- **Obtain SmPC**: Download the current Summary of Product Characteristics (SmPC) from the MHRA to extract approved indications, contraindications, warnings, and monitoring requirements.
- **Retrieve drug–drug interaction data**: Query DrugBank or the MHRA Yellow Card database for known interactions, particularly with MAOIs, CYP3A4 inhibitors/inducers, and CNS-active agents, which are known concerns for this drug class.
- **Confirm original indication**: Formally populate `drug.original_indications` from the SmPC to enable mechanism-to-indication alignment analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

