---
layout: default
title: Atovaquone
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 0
---

# Atovaquone
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

# Atovaquone (DB01117): Drug Repurposing Evaluation — Critical Data Gaps Identified

## One-Sentence Summary

Atovaquone (DrugBank ID: DB01117) has been submitted for drug repurposing evaluation via the TxGNN prediction pipeline.
Unfortunately, this Evidence Pack contains **critical data gaps** — including absent predicted indications, missing mechanism of action data, and no UK regulatory licensing records — that prevent a substantive repurposing assessment at this stage.
No evidence level can be assigned until the pipeline is re-run with complete input data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data available |
| Predicted New Indication | No TxGNN predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| UK Market Status | Not marketed (per current data) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

No safety data was returned for this candidate. Please refer to the current SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Atovaquone is incomplete in several blocking respects: the TxGNN model returned no predicted repurposing indications, and drug-level inputs (approved indications, mechanism of action, MHRA licensing) are all absent. No repurposing evaluation can be conducted without these foundational inputs.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** — confirm that Atovaquone's DrugBank ID (DB01117) is correctly mapped and that the knowledge graph contains sufficient edges for prediction; an empty `predicted_indications` array suggests a mapping or pipeline failure rather than a genuine null result
- **Retrieve MOA from DrugBank API** — query `https://go.drugbank.com/drugs/DB01117` to obtain mechanism of action, drug categories, and pharmacodynamics; this is required for mechanistic plausibility analysis
- **Verify MHRA marketing authorisation status** — Atovaquone-containing products (e.g. suspension formulations and combination products) may be authorised in Great Britain; cross-check against the MHRA product licence register and the Electronic Medicines Compendium (EMC) before confirming "not marketed" status
- **Obtain SmPC safety data** — download and parse the relevant SmPC(s) for approved warnings, contraindications, and drug interaction information to populate the safety section
- **Confirm drug classification** — determine whether Atovaquone meets criteria for the Cytotoxicity section (antiparasitic/antiprotozoal agents are typically excluded, but confirmation of DrugBank categories is needed)

---

> **Note:** This report reflects only the data provided in the submitted Evidence Pack (version v4, data cutoff 2026-04-04). The two blocking data gaps logged in the Evidence Pack meta — `DG001` (MHRA SmPC warnings/contraindications) and `DG002` (mechanism of action) — must be resolved before this candidate can be re-evaluated. Please resubmit with a complete Evidence Pack once the remediation steps above have been completed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

