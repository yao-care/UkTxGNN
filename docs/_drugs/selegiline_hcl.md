---
layout: default
title: Selegiline Hcl
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 0
---

# Selegiline Hcl
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

# Selegiline HCl: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

---

## One-Sentence Summary

Selegiline HCl is a selective monoamine oxidase B (MAO-B) inhibitor, widely recognised in clinical practice for the management of Parkinson's disease. However, this Evidence Pack contains **no TxGNN-predicted new indications**, **no UK marketing authorisation records**, and **no usable safety data**, meaning a substantive repurposing evaluation cannot be completed at this stage. Immediate data remediation is required before any recommendation can be made.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in this Evidence Pack |
| Predicted New Indication | None — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (model prediction only — not yet generated) |
| UK Market Status | Not marketed (per data; see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **⚠ Data Integrity Note:** Selegiline hydrochloride (e.g., Eldepryl®) has historically been available in UK clinical practice as an adjunct treatment for Parkinson's disease. The zero-licence result likely reflects a mapping failure against the MHRA authorisations database rather than genuine absence from the UK market. This must be verified before the report is finalised.

---

## Why is This Prediction Reasonable?

No TxGNN prediction has been generated for this drug in the current Evidence Pack, so a mechanistic justification for a specific new indication cannot be provided at this time.

From publicly available information, selegiline HCl irreversibly inhibits MAO-B, thereby reducing the breakdown of dopamine in the striatum. At higher doses it also inhibits MAO-A, which broadens its pharmacological activity to include serotonergic and noradrenergic pathways — the basis for its transdermal formulation (Emsam®, approved in the US) being investigated as an antidepressant. These mechanistic properties make selegiline a plausible repurposing candidate across neuropsychiatric indications, but **no prediction score or supporting evidence has been provided in this Evidence Pack** to support or quantify that claim.

Once the TxGNN pipeline is re-run with a confirmed DrugBank ID and the MHRA licence data is correctly ingested, a full mechanistic rationale section will be possible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## UK Market Information

No MHRA marketing authorisation records were returned for this drug. As noted above, this is likely a data pipeline issue. The following remediation step is recommended:

- Manually search the [MHRA Product Licence Register](https://products.mhra.gov.uk/) for "selegiline" and "Eldepryl" to retrieve current PL numbers, dosage forms, and approved indications.
- Cross-reference with the [BNF section 4.9.1 (Dopaminergic drugs used in Parkinson's disease)](https://bnf.nice.org.uk/drugs/selegiline-hydrochloride/) for current clinical status.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Note for prescribers:** Selegiline belongs to the MAO inhibitor class. Even in its MAO-B selective form, clinically significant food and drug interactions (e.g., with tyramine-containing foods at higher doses, serotonergic agents, and sympathomimetics) are well documented. A full DDI and contraindication review must be completed before any repurposing evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack does not contain the minimum data required for a drug repurposing evaluation — specifically, TxGNN predictions are absent, MHRA licence records were not retrieved, and all safety fields are unpopulated. No clinical recommendation can be made on the basis of this pack alone.

**To proceed, the following is needed:**

- [ ] **Confirm DrugBank ID** for selegiline HCl (the `query_log` records a successful DrugBank lookup but `drugbank_id` remains null — the mapping result should be reviewed and the correct ID populated)
- [ ] **Re-run TxGNN prediction pipeline** with the confirmed DrugBank ID to generate `predicted_indications`
- [ ] **Retrieve MHRA marketing authorisation data** — search MHRA Product Licence Register for "selegiline" and populate `licenses` array with PL numbers, product names, dosage forms, and approved indications
- [ ] **Populate MOA field** — query DrugBank API for mechanism of action and pharmacology summary (Data Gap DG002, severity: High)
- [ ] **Retrieve SmPC safety data** — download and parse the relevant MHRA-approved SmPC PDF to populate `key_warnings`, `contraindications`, and DDI fields (Data Gap DG001, severity: Blocking)
- [ ] **Re-submit Evidence Pack** once the above gaps are resolved; a full L1–L4 evaluation report can then be generated

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application in patient care. Suspected adverse reactions should be reported via the [MHRA Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

