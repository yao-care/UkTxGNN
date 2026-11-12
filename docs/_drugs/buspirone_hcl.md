---
noindex: true
sitemap: false
layout: default
title: Buspirone Hcl
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Buspirone Hcl
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

## Buspirone HCl: Generalised Anxiety Disorder — Repurposing Evaluation Incomplete
{: .text-alpha }

## One-Sentence Summary

Buspirone HCl is a non-benzodiazepine anxiolytic used in the management of generalised anxiety disorder (GAD), acting as a partial agonist at serotonin 5-HT1A receptors and, to a lesser extent, dopamine D2 receptors. The current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, as critical upstream data — including the DrugBank identifier, original indications — were not successfully retrieved by the data pipeline. A formal repurposing evaluation cannot be completed until these gaps are resolved; this report serves as a preliminary holding summary only.

<!-- review:begin uk-lic-20261106-buspirone_hcl-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, as critical upstream data — including the DrugBank identifier, original indications, and MHRA authorisation records — were not successfully retrieved by the data pipeline." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 9 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-buspirone_hcl-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Generalised Anxiety Disorder (background knowledge — not confirmed in Evidence Pack) |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction not generated; no supporting studies identified |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (9 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 9 |
| Recommended Decision | **Hold** |

> Manual verification against the [MHRA Product Licence Register](https://products.mhra.gov.uk/) is required before any regulatory conclusions are drawn.

<!-- review:begin uk-lic-20261106-buspirone_hcl-2 -->

> **Review correction (2026-11-06)**: Originally stated: "> **Important note on UK market status:** The Evidence Pack records zero MHRA marketing authorisations for Buspirone HCl. This is almost certainly a data collection failure rather than a true market absence — generic buspirone hydrochloride tablets (e.g., 5 mg and 10 mg) are listed in the British National Formulary (BNF) and have been available in the UK. Manual verification against the [MHRA Product Licence Register](https://products.mhra.gov.uk/) is required before any regulatory conclusions are drawn." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 9 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-buspirone_hcl-2 -->

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information for buspirone hydrochloride. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Buspirone HCl is critically incomplete: no TxGNN repurposing predictions were generated, no DrugBank identifier was resolved, and mechanism of action and safety data are absent. It is not possible to produce a responsible repurposing evaluation without these foundational data elements.

<!-- review:begin uk-lic-20261106-buspirone_hcl-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The Evidence Pack for Buspirone HCl is critically incomplete: no TxGNN repurposing predictions were generated, no DrugBank identifier was resolved, MHRA authorisation records could not be retrieved, and mechanism of action and safety data are absent." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 9 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-buspirone_hcl-3 -->

**To proceed, the following is needed:**

- **Confirm DrugBank identifier**: Buspirone HCl is expected to map to DrugBank entry **DB00490**. Confirm this via the DrugBank API and relink the Evidence Pack accordingly.
- **Re-run TxGNN predictions**: Once the DrugBank ID is confirmed, re-run the prediction pipeline to generate repurposing candidate indications with associated TxGNN scores.
- **Retrieve MOA and pharmacology data**: Query the DrugBank API for mechanism of action, pharmacodynamics, and toxicity data for DB00490.
- **Obtain SmPC**: Download the current Summary of Product Characteristics (SmPC) from the MHRA to extract approved indications, contraindications, warnings, and monitoring requirements.
- **Retrieve drug–drug interaction data**: Query DrugBank or the MHRA Yellow Card database for known interactions, particularly with MAOIs, CYP3A4 inhibitors/inducers, and CNS-active agents, which are known concerns for this drug class.
- **Confirm original indication**: Formally populate `drug.original_indications` from the SmPC to enable mechanism-to-indication alignment analysis.

<!-- review:begin uk-lic-20261106-buspirone_hcl-4 -->

> **Review correction (2026-11-06)**: Originally stated: "**Verify MHRA authorisations**: Manually search the [MHRA Product Licence Register](https://products.mhra.gov.uk/) for all current UK marketing authorisations for buspirone hydrochloride and update `taiwan_regulatory.licenses` accordingly. / **Obtain SmPC**: Download the current Summary of Product Characteristics (SmPC) from the MHRA to extract approved indications, contraindications, warnings, and monitoring requirements." Removed: leftover template text about Taiwan's TFDA, which does not apply to this UK page. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-buspirone_hcl-4 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and MHRA authorisation records" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "**Important note on UK market status:** The Evidence Pack records zero MHRA marketing authorisations for Buspirone HCl. This is almost certa" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "MHRA authorisation records could not be retrieved" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "**Verify MHRA authorisations**: Manually search the [MHRA Product Licence Register](https://products.mhra.gov.uk/) for all current UK market" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

