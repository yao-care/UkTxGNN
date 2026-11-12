---
noindex: true
sitemap: false
layout: default
title: Amorolfine Hcl
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amorolfine Hcl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Amorolfine HCL: No TxGNN Repurposing Predictions Returned
{: .text-alpha }

## One-Sentence Summary

Amorolfine HCL is a morpholine-class antifungal agent indicated for the topical treatment of onychomycosis (fungal nail infections).
The TxGNN pipeline returned **no predicted repurposing indications** for this compound in the current run, and critical data items — including DrugBank ID, mechanism of action.
A complete repurposing evaluation **cannot be performed** until these gaps are remediated.

<!-- review:begin uk-lic-20261106-amorolfine_hcl-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The TxGNN pipeline returned **no predicted repurposing indications** for this compound in the current run, and critical data items — including DrugBank ID, mechanism of action, and UK marketing authorisation records — are absent from this Evidence Pack." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 8 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-amorolfine_hcl-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infections — based on pharmacological class; not confirmed in Evidence Pack) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model returned no predictions |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (8 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 8 |
| Recommended Decision | **Hold** |

> This must be corrected before any formal evaluation proceeds. Please verify at [MHRA Product Licence Register](https://products.mhra.gov.uk/).

<!-- review:begin uk-lic-20261106-amorolfine_hcl-2 -->

> **Review correction (2026-11-06)**: Originally stated: "> **⚠️ Data Integrity Note:** Amorolfine 5% nail lacquer (brand name **Loceryl**, Galderma) holds an established MHRA marketing authorisation in the United Kingdom for the treatment of mild-to-moderate onychomycosis. The Evidence Pack's record of zero UK licences appears to reflect a data pipeline error — likely a query against the Taiwan TFDA register rather than the MHRA register — rather than the true UK regulatory position. This must be corrected before any formal evaluation proceeds." Removed: leftover template text about Taiwan's TFDA, which does not apply to this UK page. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-amorolfine_hcl-2 -->

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

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1310020A0AAABAB | Amorolfine 0.25% cream | Amorolfine hydrochloride |
| 1310020A0AAAAAA | Amorolfine 5% medicated nail lacquer | Amorolfine hydrochloride |
| 1310020A0BEAAAA | Boots Fungal Nail Treatment 5% medicated nail lacquer | Amorolfine hydrochloride |
| 1310020A0BCAAAA | Curanail 5% medicated nail lacquer | Amorolfine hydrochloride |
| 1310020A0BBABAB | Loceryl 0.25% cream | Amorolfine hydrochloride |
| 1310020A0BBAAAA | Loceryl 5% medicated nail lacquer | Amorolfine hydrochloride |
| 1310020A0BDAAAA | Omicur 5% medicated nail lacquer | Amorolfine hydrochloride |
| 1310020A0BFAAAA | Schollmed Fungal Nail Treatment 5% medicated nail lacquer | Amorolfine hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

**Recommended action:** Cross-check against the [MHRA Public Assessment Reports](https://www.gov.uk/government/collections/public-assessment-reports) and the **BNF Section 13.10.2** (Antifungal preparations for skin) to confirm current licence status, approved indications, and whether any licences have lapsed or been voluntarily surrendered.

<!-- review:begin uk-lic-20261106-amorolfine_hcl-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The Evidence Pack records zero active UK marketing authorisations. This is inconsistent with known MHRA regulatory history and should be treated as a data error pending verification." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 8 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-amorolfine_hcl-3 -->

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
- **Retrieve MOA data**: Pull full mechanism of action, pharmacodynamics, and toxicity data from DrugBank API once the correct ID is confirmed
- **Retrieve UK SmPC safety data**: Download and parse the current MHRA-approved SmPC for Loceryl to populate warnings, contraindications, and drug interaction fields
- **Review INN normalisation logic**: Investigate why the pipeline fails to resolve "AMOROLFINE HCL" to its base INN — this is likely a systemic issue that may affect other salt-form entries in the dataset

<!-- review:begin uk-lic-20261106-amorolfine_hcl-4 -->

> **Review correction (2026-11-06)**: Originally stated: "**Rectify UK regulatory data**: Query the MHRA register directly (not the Taiwan TFDA) and populate `taiwan_regulatory.licenses` with accurate MHRA marketing authorisation records, including the Loceryl PL number and approved indication text / **Retrieve MOA data**: Pull full mechanism of action, pharmacodynamics, and toxicity data from DrugBank API once the correct ID is confirmed" Removed: leftover template text about Taiwan's TFDA, which does not apply to this UK page. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-amorolfine_hcl-4 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and UK marketing authorisation records — are absent from this Evidence Pack" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "**⚠️ Data Integrity Note:** Amorolfine 5% nail lacquer (brand name **Loceryl**, Galderma) holds an established MHRA marketing authorisation " | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "The Evidence Pack records zero active UK marketing authorisations. This is inconsistent with known MHRA regulatory history and should be tre" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "**Rectify UK regulatory data**: Query the MHRA register directly (not the Taiwan TFDA) and populate `taiwan_regulatory.licenses` with accura" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

