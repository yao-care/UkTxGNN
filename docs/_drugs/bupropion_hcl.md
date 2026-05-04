---
layout: default
title: Bupropion Hcl
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Bupropion Hcl
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

# Bupropion HCl: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Bupropion HCl is a well-recognised antidepressant and smoking cessation agent belonging to the aminoketone class; however, this Evidence Pack contains **no TxGNN-predicted new indications**, **no confirmed UK marketing authorisation records**, and **no retrievable safety data**, making a complete repurposing evaluation impossible at this stage. Two blocking data gaps (MHRA SmPC warnings and mechanism of action) must be resolved before any meaningful clinical assessment can proceed. A **Hold** decision is recommended pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data retrieved in this Evidence Pack |
| Predicted New Indication | No TxGNN prediction available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Model prediction only (no predictions generated) |
| UK Market Status | Not Marketed (per Evidence Pack; **verification recommended** — see note below) |
| Number of Marketing Authorisations | 0 (per Evidence Pack) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Integrity Note**: The Evidence Pack records UK market status as "Not Marketed" with zero licences. This warrants independent verification against the MHRA Product Licence register, as bupropion-containing products have a known international regulatory footprint (e.g., Zyban for smoking cessation). It is possible that the data retrieval step failed or the query was submitted under a non-matching name variant ("BUPROPION HCL" vs "bupropion hydrochloride").

---

## Why is This Prediction Reasonable?

No TxGNN-predicted indication is present in this Evidence Pack; therefore, a mechanism-based rationale for repurposing cannot be constructed from the available data.

Currently, detailed mechanism of action data is not available in the Evidence Pack (Data Gap DG002, rated **High** severity). Based on published pharmacology, bupropion HCl is understood to act as a norepinephrine–dopamine reuptake inhibitor (NDRI), with additional nicotinic acetylcholine receptor antagonism that underlies its use in smoking cessation. However, citing external knowledge to justify a repurposing claim would go beyond the scope of this Evidence Pack and is therefore deferred until:

1. The DrugBank API query for MOA is completed (remediation pathway: DG002).
2. A TxGNN prediction run is successfully completed and returns at least one candidate indication.

Until these prerequisites are met, no mechanistic bridge between an established and a new indication can be responsibly drawn.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any predicted indication, as no TxGNN prediction has been generated for this drug in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available for any predicted indication, as no TxGNN prediction has been generated for this drug in this Evidence Pack.

---

## UK Market Information

No marketing authorisation records were retrieved for Bupropion HCl in this Evidence Pack. The following verification steps are recommended before concluding the drug is unlicensed in the United Kingdom:

1. Search the [MHRA Products database](https://products.mhra.gov.uk/) using both "bupropion" and "bupropion hydrochloride".
2. Cross-reference with the [BNF (British National Formulary)](https://bnf.nice.org.uk/) under CNS chapter (antidepressants / smoking cessation).
3. Check NICE technology appraisals for bupropion-based formulations.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** ([yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/)).

> The Evidence Pack carries two unresolved data gaps that directly affect safety assessment:
> - **DG001 (Blocking)**: MHRA SmPC warnings and contraindications not retrieved. Without this information, a Stage 1 safety screen cannot be completed.
> - **DG002 (High)**: Mechanism of action not available. This limits the ability to assess pharmacodynamic drug–drug interactions and on-target adverse effect risks.

No drug–drug interaction data was returned (query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is structurally incomplete — it contains no TxGNN predictions, no UK licence data, and no safety information — making it impossible to conduct a meaningful drug repurposing evaluation or safety assessment for Bupropion HCl at this time.

**To proceed, the following is needed:**

- [ ] **Resolve DG001 (Blocking)**: Retrieve MHRA SmPC for Bupropion HCl. Download and parse the SmPC PDF from the MHRA website to extract key warnings, contraindications, and special population restrictions.
- [ ] **Resolve DG002 (High)**: Query DrugBank API using the INN "bupropion" (not salt form "bupropion HCl") to retrieve mechanism of action, pharmacodynamic targets, and toxicity data.
- [ ] **Re-run TxGNN prediction**: Confirm whether the prediction pipeline was executed for this drug. If no prediction score was generated, investigate whether the DrugBank ID lookup failed (DrugBank ID is currently null) and re-attempt mapping using the normalised INN.
- [ ] **Verify UK market status**: Cross-check the MHRA Product Licence register for any current or historic authorisations. The "Not Marketed" status is inconsistent with Bupropion's known international regulatory history and may reflect a data retrieval error rather than true UK regulatory absence.
- [ ] **Re-run Evidence Pack generation**: Once DG001 and DG002 are resolved and a TxGNN prediction is available, regenerate the full Evidence Pack (v5+) and resubmit for evaluation.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Any drug repurposing candidate identified requires clinical validation before application. All content should be read in conjunction with current MHRA guidance, the BNF, and relevant NICE appraisals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

