---
layout: default
title: Bezafibrate
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 0
---

# Bezafibrate
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

# Bezafibrate: Drug Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Bezafibrate is a pan-PPAR agonist fibrate, clinically established for the management of hyperlipidaemia and mixed dyslipidaemia.
No TxGNN repurposing predictions were generated in the current Evidence Pack, preventing a full indication evaluation.
This report documents the data gaps and outlines the remediation steps required before a substantive repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperlipidaemia / mixed dyslipidaemia (known from pharmacological literature; not recorded in Evidence Pack) |
| Predicted New Indication | Not available — no TxGNN predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| UK Market Status | Not marketed (per Evidence Pack; data completeness unverified — see below) |
| Number of Marketing Authorisations | 0 (per Evidence Pack) |
| Recommended Decision | Hold |

---

## Why No Prediction is Available

The Evidence Pack for Bezafibrate (DrugBank: DB01393) contains an empty `predicted_indications` field. This is an atypical output that most likely reflects upstream data pipeline failures rather than a genuine absence of repurposing signals. Three probable causes are identified:

**1. Missing original indication data.** The `original_indications` field in the Evidence Pack is empty. TxGNN requires a seed indication context to anchor its graph traversal; without this, no disease repurposing candidates can be ranked or returned. Bezafibrate is well established in clinical use as a lipid-regulating agent, and this field should be populated before the pipeline is re-run.

**2. Unresolved data gaps at pack generation.** Two data gaps were flagged at the time this Evidence Pack was produced — both of meaningful severity:

| Gap ID | Item Missing | Severity | Impact |
|--------|-------------|----------|--------|
| DG001 | Safety warnings / contraindications (SmPC) | Blocking | Prevents safety pre-screening |
| DG002 | Mechanism of action (MOA) | High | Prevents mechanistic plausibility analysis |

Until DG001 is resolved, the candidate cannot pass the minimum safety threshold required to advance.

**3. Potential UK regulatory data retrieval failure.** The Evidence Pack records zero MHRA marketing authorisations and a market status of "not marketed." Independent pharmacopoeia records indicate that Bezafibrate is currently authorised and available in the UK (e.g., Bezalip 200 mg tablets, Bezalip Mono 400 mg modified-release tablets). This discrepancy strongly suggests a data retrieval issue in the regulatory ingestion step rather than a true absence of UK authorisations.

---

## Safety Considerations

All safety data fields in the current Evidence Pack are unavailable.

> Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated, and all three critical data domains — original indication, mechanism of action, and UK regulatory authorisation — are absent or incomplete. A repurposing evaluation cannot be meaningfully conducted without these foundations.

**To proceed, the following is needed:**

- **Re-populate original indications**: Add Bezafibrate's established indication (hyperlipidaemia / mixed dyslipidaemia) to the Evidence Pack input and re-run the TxGNN prediction pipeline.
- **Resolve DG001 — SmPC retrieval**: Obtain the current UK SmPC from the MHRA product licence database; parse safety warnings, contraindications, and special precautions sections.
- **Resolve DG002 — MOA data**: Query the DrugBank API (DB01393) to retrieve the mechanism of action (pan-PPAR agonism: PPARα/γ/δ) and populate the `original_moa` field.
- **Correct UK regulatory data**: Re-run the MHRA licence ingestion step to retrieve active product licences for Bezafibrate; verify against the MHRA public register and BNF entry.
- **Re-generate Evidence Pack**: Once all inputs are corrected, regenerate the full Evidence Pack (v5+) including clinical trial and literature evidence, then commission a new evaluation report.

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application. Suspected adverse reactions should be reported via the Yellow Card Scheme.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

