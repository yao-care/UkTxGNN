---
layout: default
title: Amitriptyline Hcl
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 0
---

# Amitriptyline Hcl
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

# Amitriptyline Hydrochloride: Repurposing Evaluation Pending — Critical Data Gaps Identified

---

## One-Sentence Summary

Amitriptyline hydrochloride is a long-established tricyclic antidepressant with well-documented clinical applications in the UK, including neuropathic pain, depression, and migraine prophylaxis.
However, this Evidence Pack contains **no TxGNN predicted indications** and is missing key regulatory, mechanism-of-action, and safety data, making a formal repurposing evaluation impossible at this stage.
**A Hold decision is recommended** until the data gaps identified below are resolved and the prediction pipeline is re-run successfully.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No predictions returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — prediction pipeline incomplete; no supporting studies assessable |
| UK Market Status | Unconfirmed (data reports unlicensed — see data quality note) |
| Number of Marketing Authorisations | 0 recorded (likely a data extraction failure — see below) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Quality Note:** Amitriptyline hydrochloride is a long-established medicine with a well-known presence in the UK. The reported market status of "not marketed" with zero MHRA authorisations is almost certainly a data extraction failure rather than an accurate regulatory picture. The MHRA Products database should be queried directly before this Evidence Pack is used for any downstream decision-making.

---

## Why is This Prediction Reasonable?

No TxGNN predicted indications were returned in this Evidence Pack, so no mechanistic rationale for a specific new indication can be constructed at this stage.

Mechanism of action data was not supplied. Based on established pharmacological literature, amitriptyline is a tricyclic antidepressant (TCA) that primarily inhibits the presynaptic reuptake of norepinephrine and serotonin. It also exhibits significant antihistaminergic, anticholinergic, and sodium channel-blocking activity. These secondary properties are thought to underpin its widely used off-label applications in neuropathic pain, functional gastrointestinal disorders, and migraine prophylaxis in UK clinical practice.

Once the TxGNN pipeline has been re-run successfully and predicted indications are available, the mechanistic plausibility of each prediction should be evaluated against these known pharmacological properties.

---

## Clinical Trial Evidence

No predicted indication is present in this Evidence Pack. Disease-specific clinical trial evidence cannot be presented until a target indication is identified from TxGNN output.

---

## Literature Evidence

No predicted indication is present in this Evidence Pack. Disease-specific literature evidence cannot be presented until a target indication is identified from TxGNN output.

---

## UK Market Information

No MHRA marketing authorisation records are present in this Evidence Pack. This is inconsistent with the known regulatory status of amitriptyline in the UK, and should be treated as a data extraction failure rather than a genuine absence of licences. Please query the following sources directly:

| Resource | URL |
|----------|-----|
| MHRA Products Database | https://products.mhra.gov.uk/ |
| BNF — Amitriptyline | https://bnf.nice.org.uk/drugs/amitriptyline-hydrochloride/ |
| NICE Evidence | https://www.nice.org.uk/ |

---

## Safety Considerations

No safety data was supplied in this Evidence Pack. Please refer to the current SmPC and the BNF entry for amitriptyline hydrochloride for warnings, contraindications, and drug interactions. Report suspected adverse reactions via the **Yellow Card Scheme** at https://yellowcard.mhra.gov.uk/.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for amitriptyline hydrochloride is incomplete in every critical dimension — there are no TxGNN predictions, no regulatory records, no mechanism-of-action data, and no safety data. A repurposing evaluation cannot be conducted on this basis.

**To proceed, the following is needed:**

1. **Re-run the TxGNN prediction pipeline** — the `predicted_indications` array is empty. Confirm whether amitriptyline was successfully mapped to a DrugBank node and whether the KG/DL prediction step completed without error. The expected DrugBank identifier is **DB00321**; note that `drugbank_id` is currently null, which is the likely root cause of the failed prediction.

2. **Confirm the DrugBank ID** — populate `drugbank_id` with **DB00321** (amitriptyline) and re-run the full pipeline from the drug-mapping stage onward.

3. **Retrieve MHRA marketing authorisation data** — query the MHRA Products database for all current and historic authorisations for amitriptyline hydrochloride. The current data showing zero licences is almost certainly a pipeline error.

4. **Obtain mechanism-of-action data** — retrieve the MOA from the DrugBank API once the DrugBank ID is confirmed.

5. **Extract safety data** — download the current SmPC from the MHRA website and parse key warnings, contraindications, and clinically significant drug interactions (note: TCAs carry well-known interactions with MAOIs, SSRIs, and QT-prolonging agents).

6. **Re-submit the completed Evidence Pack** — once items 1–5 are resolved, regenerate the Evidence Pack and submit for a full evaluation report.

---

*This report is generated for research purposes only and does not constitute clinical or regulatory advice. All repurposing candidates require prospective clinical validation before any change to prescribing practice. Adverse reactions should be reported via the MHRA Yellow Card Scheme.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

