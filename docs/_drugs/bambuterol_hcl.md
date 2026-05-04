---
layout: default
title: Bambuterol Hcl
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Bambuterol Hcl
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

# Bambuterol HCL: Drug Repurposing Evaluation — No Active Prediction Available

## One-Sentence Summary

Bambuterol HCL is a long-acting beta-2 adrenoceptor agonist prodrug (of terbutaline), historically used in the management of bronchial asthma and chronic obstructive pulmonary disease (COPD).
The TxGNN model was unable to generate a repurposing prediction for this drug at this time — the `predicted_indications` array in the current evidence pack is empty.
No clinical trial, literature, or mechanistic evidence can therefore be evaluated for a new indication at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / COPD (historical use; no active UK marketing authorisation on record) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Model prediction pipeline incomplete; no candidate generated |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is a Prediction Not Yet Available?

The evidence pack was returned with an empty `predicted_indications` array, meaning the TxGNN knowledge graph and deep learning pipeline did not produce a scored repurposing candidate for Bambuterol HCL. This is most likely because a DrugBank ID (`drugbank_id: null`) could not be resolved for this drug entry, which is a prerequisite for mapping the compound into the TxGNN knowledge graph. Without a valid node in the graph, neither knowledge graph traversal nor the deep learning model can generate a prediction.

Detailed mechanism of action data is also absent from the evidence pack. Based on published pharmacology, bambuterol HCL is a carbamate prodrug that undergoes plasma and tissue hydrolysis to release terbutaline, a selective β₂-adrenoceptor agonist. Its bronchodilatory effects are mediated through cyclic AMP-dependent smooth muscle relaxation in the airways. Whether this mechanism might support repurposing into adjacent disease areas (e.g., premature labour, hyperkalaemia, or inflammatory airway conditions) cannot be formally assessed without a model-generated candidate and supporting evidence data.

Resolving the DrugBank identifier and re-running the prediction pipeline is therefore the critical first step before any repurposing evaluation can proceed.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack contains no TxGNN-predicted indications, no UK marketing authorisations, no DrugBank identifier, and no mechanism of action data — the minimum inputs required for a meaningful drug repurposing evaluation are not yet in place.

**To proceed, the following is needed:**

- **Resolve DrugBank ID**: Match "BAMBUTEROL HCL" to its canonical DrugBank entry (likely DB01223 via its active metabolite terbutaline; verify the prodrug entry directly) to enable knowledge graph node mapping
- **Re-run TxGNN pipeline**: Once the DrugBank ID is confirmed, execute `scripts/run_kg_prediction.py` and the deep learning model to generate scored repurposing candidates
- **Retrieve MOA data**: Query the DrugBank API for pharmacodynamics, mechanism, and drug class categorisation
- **Obtain MHRA safety data**: Download the SmPC to populate key warnings, contraindications, and drug interaction profiles
- **Confirm UK regulatory history**: Check the MHRA Public Assessment Report (PAR) register for any historic or revoked product licences (Bambec was previously marketed in the UK as a once-daily tablet and may have a revoked PL on record)
- **Re-submit Evidence Pack**: Once the above data gaps (DG001, DG002) are remediated, resubmit for a full evaluation report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

