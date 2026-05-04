---
layout: default
title: Roflumilast
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 0
---

# Roflumilast
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

# Roflumilast: Repurposing Potential Under Review — TxGNN Predictions Pending

---

## One-Sentence Summary

Roflumilast (DrugBank: DB01656) is a selective phosphodiesterase-4 (PDE4) inhibitor approved for the management of severe chronic obstructive pulmonary disease (COPD) associated with chronic bronchitis, and is marketed in the United Kingdom as Daxas.
This Evidence Pack is **critically incomplete**: no TxGNN repurposing predictions have been generated, UK regulatory data was not captured in the structured fields, and key safety information is absent.
A full repurposing evaluation cannot be issued at this stage; the recommended decision is **Hold** pending resolution of the two identified data gaps (DG001, DG002).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe COPD associated with chronic bronchitis *(known from external sources; not captured in current Evidence Pack structured fields)* |
| Predicted New Indication | Pending — TxGNN prediction pipeline has not been executed for this drug |
| TxGNN Prediction Score | Pending |
| Evidence Level | Cannot be determined |
| UK Market Status | Data collection incomplete — Evidence Pack records 0 licences; however, Roflumilast is known to hold MHRA marketing authorisation (Daxas) |
| Number of Marketing Authorisations | 0 recorded in current data *(likely a data collection error — see above)* |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Roflumilast (DB01656) contains two identified data gaps — one classified as **Blocking** (DG001: MHRA SmPC warnings and contraindications) and one as **High** (DG002: mechanism of action) — and, critically, the TxGNN prediction pipeline has not been run for this drug, meaning there are no repurposing candidates to evaluate.

**To proceed, the following is needed:**

- **Run the TxGNN prediction pipeline**: Execute both the knowledge graph (KG) and deep learning (DL) prediction methods for Roflumilast (DB01656) against the current disease vocabulary to generate ranked repurposing candidates with confidence scores.
- **Collect UK regulatory data**: Retrieve MHRA marketing authorisation records for Daxas (roflumilast) to confirm licence numbers (PL), approved indications, dosage forms, and current market status — the zero-licence figure in the current Evidence Pack appears to reflect a data collection failure rather than actual market absence.
- **Populate mechanism of action (DG002)**: Query the DrugBank API for DB01656 to document the selective PDE4 inhibitor MOA, including subtype selectivity (PDE4B preference), downstream cAMP pathway effects, and known anti-inflammatory targets relevant to repurposing analysis.
- **Obtain safety data (DG001)**: Download and parse the current UK SmPC for Daxas from the MHRA product information portal to populate warnings (including psychiatric events, weight loss), contraindications, and drug interaction data.
- **Regenerate the Evidence Pack**: Once all gaps above are resolved, regenerate a complete Evidence Pack (v5+) and resubmit for a full repurposing evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

