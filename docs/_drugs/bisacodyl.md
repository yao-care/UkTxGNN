---
layout: default
title: Bisacodyl
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 0
---

# Bisacodyl
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

# Bisacodyl: Evaluation on Hold — No Repurposing Predictions Available

## One-Sentence Summary

Bisacodyl is a stimulant laxative indicated for constipation and bowel preparation prior to medical procedures. The TxGNN model has not generated any repurposing predictions for this drug in the current run, and multiple critical data gaps prevent a meaningful evaluation at this stage. This report documents the current data status and outlines the steps required before a repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Constipation; bowel preparation (based on established pharmacological knowledge; no formal licence text retrieved) |
| Predicted New Indication | None available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no model predictions generated |
| UK Market Status | No authorisation data retrieved |
| Number of Marketing Authorisations | 0 (data retrieval incomplete) |
| Recommended Decision | Hold |

---

## Why No Prediction is Available

The TxGNN prediction pipeline did not return any repurposing candidates for Bisacodyl (DrugBank ID: DB09020) in this run. This is most likely due to missing upstream data rather than a genuine absence of signal, specifically:

- **Mechanism of action (MOA) data** was not retrieved. Without MOA data, the model's graph-based reasoning cannot fully characterise the drug node in the knowledge graph, which may suppress candidate generation.
- **Regulatory licence data** was not retrieved for the UK market (MHRA). The evidence pack records zero marketing authorisations. Bisacodyl is a well-established over-the-counter stimulant laxative marketed in the UK (e.g., Dulcolax), so this almost certainly reflects a retrieval gap rather than the true market status.

Once these data gaps are resolved and the pipeline is re-run, repurposing predictions are expected to be generated. Any subsequent report will include a full mechanistic rationale and evidence review.

---

## Safety Considerations

No safety data was retrieved in this evidence pack. Please refer to the current **Summary of Product Characteristics (SmPC)** and the **British National Formulary (BNF)** for full prescribing information, warnings, and contraindications. Suspected adverse reactions should be reported via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline has not generated any repurposing predictions for Bisacodyl, and two critical data gaps — missing MOA and missing UK regulatory data — must be resolved before a valid evaluation can be conducted.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve MHRA SmPC warnings and contraindications for Bisacodyl-containing products — download SmPC PDFs from the [MHRA Product Licence Register](https://www.gov.uk/check-if-a-medicine-is-licensed) or the [electronic Medicines Compendium (eMC)](https://www.medicines.org.uk/emc)
- **[High Priority]** Retrieve mechanism of action data from DrugBank API for DB09020
- Re-run the TxGNN prediction pipeline once the above data are available
- Manually verify UK market status: Bisacodyl is expected to hold multiple OTC MHRA licences (PL numbers); cross-check against the eMC or BNF Section 1.6 (Laxatives)
- Retrieve drug interaction data from an appropriate source (e.g., BNF Appendix 1, Stockley's Drug Interactions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

