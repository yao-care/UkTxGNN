---
layout: default
title: Saxagliptin
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 0
---

# Saxagliptin
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

# Saxagliptin (DB06335): Type 2 Diabetes Mellitus — No Repurposing Prediction Available

---

## One-Sentence Summary

Saxagliptin is a selective dipeptidyl peptidase-4 (DPP-4) inhibitor used in the management of type 2 diabetes mellitus. This evidence pack contains **no TxGNN repurposing predictions** for this drug, and two critical data fields — mechanism of action and UK regulatory safety information — are missing. A full repurposing evaluation cannot be completed until these gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (DPP-4 inhibitor class — clinical knowledge; not captured in evidence pack) |
| Predicted New Indication | Not available — no TxGNN prediction generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (no studies retrieved; model prediction not generated) |
| UK Market Status | Not recorded in evidence pack (0 authorisations returned) |
| Number of Marketing Authorisations | 0 (as per evidence pack — see note below) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction is present in this evidence pack, so a mechanism-based cross-indication rationale cannot be constructed at this stage.

From established clinical pharmacology, Saxagliptin reversibly and selectively inhibits DPP-4, the enzyme that rapidly inactivates the incretin hormones GLP-1 (glucagon-like peptide-1) and GIP (glucose-dependent insulinotropic polypeptide). By extending the half-life of these hormones, Saxagliptin potentiates glucose-dependent insulin secretion from pancreatic beta cells and suppresses inappropriate glucagon release, resulting in improved glycaemic control in type 2 diabetes mellitus.

Detailed mechanism of action data was not captured in this evidence pack (data gap DG002). Until this is resolved, any mechanistic reasoning about candidate new indications — for example, cardio-metabolic, renal, or inflammatory conditions where DPP-4 biology has been explored in the literature — would rest on inference rather than verified data. Remediation via the DrugBank API (DB06335) is required before proceeding.

---

## Clinical Trial Evidence

Currently no related clinical trials retrieved in this evidence pack.

---

## Literature Evidence

Currently no related literature available in this evidence pack.

---

## UK Market Information

No marketing authorisation records were returned in this evidence pack (0 licences, status: not marketed).

> **Important caveat:** This is likely a data collection gap rather than an accurate reflection of the UK regulatory position. Saxagliptin is authorised by the MHRA and is available in the UK as **Onglyza®** (saxagliptin 2.5 mg and 5 mg film-coated tablets, AstraZeneca AB) for the treatment of type 2 diabetes mellitus in adults. It is also available as a fixed-dose combination with dapagliflozin (Qtern®). MHRA licence data must be retrieved and populated in the evidence pack before evaluation proceeds.

---

## Safety Considerations

No safety data was returned in this evidence pack. Please refer to the current Saxagliptin SmPC and the BNF (section 6.1.2 — Antidiabetic drugs) for full safety information. Of note, the SAVOR-TIMI 53 cardiovascular outcomes trial identified an increased risk of hospitalisation for heart failure with saxagliptin, which is reflected in a black-box–equivalent warning in the approved prescribing information.

Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is critically incomplete — no TxGNN repurposing predictions have been generated, both the MHRA safety profile and the mechanism of action are absent, and the UK regulatory licence data has not been collected. A meaningful repurposing evaluation cannot be produced from the current data.

**To proceed, the following is needed:**

1. **Resolve DG001 (Blocking):** Retrieve and parse the current MHRA SmPC for Saxagliptin (Onglyza®) to extract warnings, contraindications, special precautions, and drug interactions. This is a prerequisite for safety-stage screening.
2. **Resolve DG002 (High):** Query the DrugBank API for DB06335 to populate the mechanism of action, pharmacodynamics, and target data. This is required for mechanistic plausibility analysis.
3. **Populate UK licence data:** Retrieve MHRA marketing authorisation records (PL numbers, approved indications, dosage forms, current market status) to complete the regulatory section.
4. **Re-run TxGNN prediction pipeline:** Once drug data are populated, re-run the knowledge graph and deep learning prediction steps to generate repurposing candidates for Saxagliptin.
5. **Re-generate this report:** Issue a new evidence pack (v5+) incorporating the above data, then produce a full repurposing evaluation report with candidate indication, evidence tables, and safety review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

