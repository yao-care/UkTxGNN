---
layout: default
title: Chlorpromazine Hcl
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 0
---

# Chlorpromazine Hcl
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

# Chlorpromazine HCl: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

---

## One-Sentence Summary

Chlorpromazine hydrochloride is a first-generation (typical) antipsychotic of the phenothiazine class, historically used for schizophrenia, acute psychosis, and nausea management. This Evidence Pack, however, contains **no TxGNN-predicted new indications**, which prevents a standard repurposing analysis from being completed. The report below captures all available data and sets out precisely what is required before a full evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in Evidence Pack (historical use: schizophrenia / acute psychosis) |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no predictions or supporting studies present in pack |
| UK Market Status | Not marketed (per Evidence Pack — see data quality note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **⚠️ Data Quality Note:** The Evidence Pack records UK market status as "Not marketed" with zero licences. This is likely a data extraction error. Chlorpromazine (marketed as **Largactil®** by Sanofi) holds a current MHRA marketing authorisation in the United Kingdom for schizophrenia and related psychoses, and is listed in the BNF (Section 4.2.1). This discrepancy must be investigated and resolved before relying on the Evidence Pack for any regulatory decision.

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indication is present in this Evidence Pack, so a standard mechanistic rationale cannot be constructed.

For background context: Chlorpromazine is a dopamine D2 receptor antagonist with additional activity across histamine H1, muscarinic M1, and α-adrenergic receptors. This unusually broad receptor profile underpins both its antipsychotic efficacy and several off-label applications (antiemesis, intractable hiccups, acute mania). The breadth of its pharmacological footprint is precisely the type of profile that drug repurposing models such as TxGNN tend to find productive — making the absence of predictions unexpected, and suggesting a likely upstream data or mapping failure rather than a genuine null result.

Detailed mechanism of action data is currently absent from the Evidence Pack. Once the DrugBank ID is confirmed and the TxGNN pipeline is re-run, MOA data should be retrieved from DrugBank to support mechanistic justification for any predicted indication.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

---

## UK Market Information

No marketing authorisations are recorded in this Evidence Pack. As noted in the data quality warning above, this almost certainly reflects a mapping or extraction failure. The table below would normally be populated from MHRA licence data; it cannot be completed until the regulatory data discrepancy is resolved.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| — | — | — | Data not available in this Evidence Pack |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is too incomplete to support a drug repurposing evaluation. The TxGNN model has generated no predicted new indications for Chlorpromazine HCl, and all drug-level safety data — including warnings, contraindications, and drug interactions — are absent. The UK regulatory data appear incorrect, which further undermines confidence in the pack's integrity.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping:** Chlorpromazine's expected DrugBank ID is DB00477 — confirm and populate `drugbank_id` in the Evidence Pack, then re-run the TxGNN prediction pipeline.
- **Re-run TxGNN predictions:** Once the DrugBank ID is confirmed, execute the KG and DL prediction steps to generate `predicted_indications`.
- **Fix UK regulatory data:** Cross-check MHRA licence records for Chlorpromazine / Largactil® and correct the `market_status` and `licenses` fields.
- **Retrieve MOA from DrugBank:** Query the DrugBank API for DB00477 to populate mechanism of action data.
- **Retrieve safety data from MHRA SmPC:** Download and parse the Largactil SmPC to populate warnings, contraindications, and key drug interactions.
- **Re-issue Evidence Pack:** Once the above gaps are remediated, re-generate the Evidence Pack (target version ≥ v5) and re-submit for evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

