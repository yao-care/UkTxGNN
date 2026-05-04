---
layout: default
title: Celiprolol Hcl
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 0
---

# Celiprolol Hcl
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

# Celiprolol HCL: Repurposing Evaluation — No Prediction Data Available

## One-Sentence Summary

Celiprolol HCL is a beta-adrenoceptor blocking agent not currently authorised for marketing in the United Kingdom.
The TxGNN model returned **no predicted indications** for this candidate, and the underlying Evidence Pack contains critical data gaps in original indication, mechanism of action, and safety profile.
As a result, **no evidence-based repurposing recommendation** can be made at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No TxGNN prediction available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction only (no predictions returned) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## UK Market Information

Celiprolol HCL currently holds **no MHRA marketing authorisation** in the United Kingdom. There are no registered products, dosage forms, or approved indications on record in this Evidence Pack.

> **Note for clinicians:** Celiprolol is available in certain other European markets (e.g., France, Germany) for cardiovascular indications. However, in the absence of a UK marketing authorisation, any clinical use would require a Specials licence or named-patient basis application via the MHRA, and standard BNF/NICE guidance does not apply.

---

## Safety Considerations

No safety data is available in this Evidence Pack. Please refer to the current SmPC (if sourced from another jurisdiction), the BNF, and relevant MHRA guidance before considering any clinical use.

Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Celiprolol HCL is incomplete across all critical domains — TxGNN returned no predicted indications, the mechanism of action is unrecorded, the drug has no UK marketing authorisation, and no safety profile has been retrieved. There is currently no basis on which to evaluate or recommend a repurposing pathway.

**To proceed, the following is needed:**

- **TxGNN prediction run**: Re-run the TxGNN pipeline with a confirmed DrugBank ID for Celiprolol (DrugBank DB01353) to generate ranked disease predictions.
- **Mechanism of action**: Retrieve MOA data from DrugBank or literature (celiprolol is understood to be a cardioselective β₁-blocker with partial β₂-agonist activity, but this must be confirmed from source data).
- **Original indication confirmation**: Populate `original_indications` from MHRA Specials records, EMA authorisations, or published pharmacopoeial data.
- **Safety data retrieval**: Download and parse the relevant SmPC (e.g., from the French or German medicines agency) to populate key warnings, contraindications, and drug interaction profile.
- **DrugBank ID linkage**: Confirm and record the DrugBank ID so that DDI queries, category classification, and MOA extraction can proceed correctly.
- **UK pathway assessment**: If a TxGNN prediction is subsequently generated, assess whether a Specials licence or a full MHRA application would be the appropriate UK regulatory route.

---

*This report was generated on 2026-04-05. All findings are based solely on the data provided in Evidence Pack version v4 (candidate ID: TW-UNKNOWN-multi). This report is intended for research purposes only and does not constitute medical advice or a clinical recommendation. Any repurposing candidate requires prospective clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

