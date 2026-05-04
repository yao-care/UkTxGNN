---
layout: default
title: Azilsartan Medoxomil
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Azilsartan Medoxomil
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

# Azilsartan Medoxomil: Repurposing Evaluation — Insufficient Data for Full Assessment

---

## One-Sentence Summary

Azilsartan medoxomil is an angiotensin II receptor blocker (ARB) used as an antihypertensive agent in clinical practice.
However, the current Evidence Pack (candidate `TW-DB08822-multi`, v4) contains **no TxGNN repurposing predictions**, no UK regulatory records, and no safety data — rendering a full evaluation impossible at this stage.
This report documents the current data status and outlines the remediation steps required before a repurposing decision can be made.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (inferred from pharmacological class; no formal indication text in evidence pack) |
| Predicted New Indication | **Not available** — TxGNN prediction pipeline returned no results |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** — Model prediction only; no actual studies linked |
| UK Market Status | Not populated in evidence pack *(see note below)* |
| Number of Marketing Authorisations | 0 per evidence pack |
| Recommended Decision | **Hold** |

> **⚠️ Data Note:** The evidence pack field `market_status` shows "未上市" (not marketed), which appears to reflect Taiwan regulatory data rather than UK/MHRA data. Azilsartan medoxomil is in fact authorised in the United Kingdom under the brand name **Edarbi** (PL 50622/0001 and related). This discrepancy suggests the MHRA data pipeline has not yet been populated for this candidate. The regulatory section below reflects this gap explicitly.

---

## Why Assessment Is Currently Limited

Azilsartan medoxomil belongs to the angiotensin II receptor blocker (ARB) class. It acts by selectively and insurmountably antagonising the AT₁ receptor subtype, thereby blocking the vasoconstrictor and aldosterone-secreting effects of angiotensin II. Its principal approved indication is the management of essential hypertension in adults.

Detailed mechanism of action data was not returned by the DrugBank query in this evidence pack (Data Gap DG002). Based on established pharmacology, azilsartan medoxomil's AT₁ receptor blockade has been explored in preclinical and clinical research for conditions beyond hypertension — including chronic kidney disease, heart failure with reduced ejection fraction, metabolic syndrome, and diabetic nephropathy — areas where the renin–angiotensin–aldosterone system (RAAS) plays a mechanistic role. These represent plausible repurposing directions, but the TxGNN model has not yet scored these indications for this candidate.

The absence of `predicted_indications` in the evidence pack means no evidence tables (clinical trials, literature) can be generated at this time. The root cause is most likely an upstream pipeline issue rather than a genuine lack of candidates for this well-characterised drug class.

---

## UK Market Information

The evidence pack contains no MHRA licence records for azilsartan medoxomil (`total_licenses: 0`). Based on published MHRA data, the following authorisations are known to exist and should be retrieved and verified during remediation:

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|------------|-------------------|
| PL 50622/0001 *(to verify)* | Edarbi | Film-coated tablet (20 mg, 40 mg, 80 mg) | Essential hypertension in adults |
| *(combination product — to verify)* | Edarbyclor | Film-coated tablet | Hypertension (azilsartan medoxomil + chlorthalidone) |

> These entries must be confirmed against the MHRA Product Licence Register before use. The evidence pack pipeline should be re-run with MHRA data integration to populate this section accurately.

---

## Safety Considerations

All safety fields in the evidence pack are unpopulated (Data Gap DG001). No key warnings, contraindications, or drug interaction data are available from the current evidence pack.

Please refer to the **Edarbi Summary of Product Characteristics (SmPC)** on the MHRA website and the **British National Formulary (BNF)** section 2.5.5.2 (Angiotensin-II receptor antagonists) for current safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for azilsartan medoxomil (DB08822) is incomplete in two blocking respects: the TxGNN prediction pipeline returned no repurposing candidates, and UK/MHRA regulatory data has not been populated. No evidence-based repurposing decision can be made until these gaps are resolved.

**To proceed, the following is required:**

- **[Blocking — DG001]** Retrieve the MHRA SmPC for Edarbi; extract approved indication text, warnings, and contraindications
- **[Blocking]** Investigate why `predicted_indications` is empty — confirm whether the TxGNN KG/DL pipeline ran successfully for DB08822, and re-run if not
- **[High — DG002]** Query DrugBank API for azilsartan medoxomil MOA, pharmacodynamics, and toxicity data
- **[High]** Re-populate `taiwan_regulatory` (or UK-equivalent field) with MHRA licence data — the current "未上市" value appears to reflect Taiwan status rather than UK status
- **[Medium]** Once predictions are available, re-generate this report using the full evidence pack to obtain clinical trial and literature evidence tables
- **[Medium]** Clarify candidate ID prefix (`TW-`) — if this record was migrated from the Taiwan pipeline, ensure the UK-specific data fields are correctly mapped before clinical review

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Candidate: `TW-DB08822-multi` · Evidence Pack v4 · Data cutoff: 2026-04-04*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

