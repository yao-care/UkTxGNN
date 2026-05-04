---
layout: default
title: Amorolfine Hcl
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 0
---

# Amorolfine Hcl
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

# Amorolfine HCL: No TxGNN Repurposing Predictions Returned

## One-Sentence Summary

Amorolfine HCL is a morpholine-class antifungal agent indicated for the topical treatment of onychomycosis (fungal nail infections).
The TxGNN pipeline returned **no predicted repurposing indications** for this compound in the current run, and critical data items — including DrugBank ID, mechanism of action, and UK marketing authorisation records — are absent from this Evidence Pack.
A complete repurposing evaluation **cannot be performed** until these gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infections — based on pharmacological class; not confirmed in Evidence Pack) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model returned no predictions |
| UK Market Status | Recorded as "not marketed" in this Evidence Pack *(see data note below)* |
| Number of Marketing Authorisations | 0 per Evidence Pack *(verification against MHRA register strongly recommended)* |
| Recommended Decision | **Hold** |

> **⚠️ Data Integrity Note:** Amorolfine 5% nail lacquer (brand name **Loceryl**, Galderma) holds an established MHRA marketing authorisation in the United Kingdom for the treatment of mild-to-moderate onychomycosis. The Evidence Pack's record of zero UK licences appears to reflect a data pipeline error — likely a query against the Taiwan TFDA register rather than the MHRA register — rather than the true UK regulatory position. This must be corrected before any formal evaluation proceeds. Please verify at [MHRA Product Licence Register](https://products.mhra.gov.uk/).

---

## Why No Prediction Is Available

No TxGNN repurposing prediction has been returned for amorolfine HCL, and therefore a mechanistic justification for a new indication cannot be presented at this stage.

For background context, amorolfine is a morpholine antifungal whose mechanism centres on the disruption of fungal ergosterol biosynthesis: it inhibits two key enzymes in the pathway — **Δ¹⁴ reductase** and **Δ⁸→Δ⁷ isomerase** — leading to depletion of ergosterol and accumulation of toxic sterol intermediates (ignosterol, obtusifolione) in the fungal cell membrane. This mechanism is highly selective for fungi and has no established relevance to human disease pathways, which may partially explain the absence of repurposing signal.

The most likely technical cause of the missing prediction is the **absence of a DrugBank ID** in the Evidence Pack. The TxGNN graph traversal requires a valid DrugBank node to anchor the drug in the knowledge graph. Querying under the salt name "AMOROLFINE HCL" rather than the INN "amorolfine" (free base) may have caused the DrugBank lookup to fail. The correct DrugBank identifier should be retrieved and the prediction re-run before concluding that no repurposing opportunity exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any repurposing indication, as no TxGNN predictions were returned.

---

## Literature Evidence

Currently no related literature available for any repurposing indication, as no TxGNN predictions were returned.

---

## UK Market Information

The Evidence Pack records zero active UK marketing authorisations. This is inconsistent with known MHRA regulatory history and should be treated as a data error pending verification.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| Not available in this Evidence Pack | — | — | — |

**Recommended action:** Cross-check against the [MHRA Public Assessment Reports](https://www.gov.uk/government/collections/public-assessment-reports) and the **BNF Section 13.10.2** (Antifungal preparations for skin) to confirm current licence status, approved indications, and whether any licences have lapsed or been voluntarily surrendered.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) is available within this Evidence Pack. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** ([yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk)).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is insufficient to support a drug repurposing evaluation for amorolfine HCL. No TxGNN predictions have been generated, and the absence of a DrugBank ID, mechanism of action data, and valid UK regulatory records means none of the core evaluation criteria can be assessed at this time.

**To proceed, the following is needed:**

- **Correct the DrugBank query**: Re-query using the INN "amorolfine" (free base, not the HCl salt name); the expected DrugBank ID is DB04816 — confirm and populate `drugbank_id` in the Evidence Pack
- **Re-run TxGNN prediction pipeline** with a verified DrugBank node ID to generate candidate indications
- **Rectify UK regulatory data**: Query the MHRA register directly (not the Taiwan TFDA) and populate `taiwan_regulatory.licenses` with accurate MHRA marketing authorisation records, including the Loceryl PL number and approved indication text
- **Retrieve MOA data**: Pull full mechanism of action, pharmacodynamics, and toxicity data from DrugBank API once the correct ID is confirmed
- **Retrieve UK SmPC safety data**: Download and parse the current MHRA-approved SmPC for Loceryl to populate warnings, contraindications, and drug interaction fields
- **Review INN normalisation logic**: Investigate why the pipeline fails to resolve "AMOROLFINE HCL" to its base INN — this is likely a systemic issue that may affect other salt-form entries in the dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

