---
layout: default
title: Azelastine
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 0
---

# Azelastine
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

# Azelastine: Evaluation Pending — No Repurposing Prediction Available

## One-Sentence Summary

Azelastine (DB00972) is a pharmaceutical compound submitted for drug repurposing evaluation; however, this evidence pack currently lacks the data required to generate or assess a candidate new indication. The TxGNN prediction pipeline returned no candidate indications for this compound, and critical mechanistic and regulatory data remain outstanding. A **Hold** decision is recommended until the evidence pack is completed and the prediction pipeline can be re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this evidence pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Below L5 — no prediction generated |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Evaluation Cannot Proceed

The evidence pack for Azelastine (DB00972) contains two critical gaps that prevent the TxGNN pipeline from generating a repurposing hypothesis, and prevent the evaluation team from conducting any mechanistic or safety analysis.

No mechanism of action (MOA) data is recorded in this evidence pack. MOA information is fundamental to repurposing analysis — without it, there is no pharmacological basis on which to assess whether the drug's biological targets are relevant to any candidate disease. The evidence pack metadata classifies this as a **High-severity** gap (DG002), requiring resolution via the DrugBank API.

The TxGNN model returned no predicted indications for this compound. Based on how the pipeline operates, this is most likely a consequence of incomplete or unresolved DrugBank input data rather than a genuine absence of repurposing potential. Azelastine is an established antihistamine in widespread international clinical use, and repurposing signal is plausible once the pipeline inputs are corrected.

The UK marketing authorisation data also appears incomplete: zero MHRA licences are recorded. Clinicians should note that Azelastine has been in clinical use internationally (as a nasal spray and eye drops for allergic conditions), and the MHRA Product Licence register should be consulted directly to verify current UK authorisation status before drawing conclusions from this figure.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack contains no TxGNN-predicted indication and is missing critical drug-level data (MOA and regulatory label), making a meaningful repurposing evaluation impossible at this stage. No progression is possible until these gaps are resolved.

**To proceed, the following is needed:**

- **Resolve Blocking gap (DG001):** Obtain the full MHRA SmPC for Azelastine, including approved indications, warnings, and contraindications — download the SmPC PDF from the MHRA website and parse the relevant sections
- **Resolve High gap (DG002):** Retrieve MOA data for Azelastine (DB00972) via the DrugBank API to enable mechanistic rationale assessment
- **Verify UK market status:** Cross-check against the MHRA Product Licence register to confirm whether existing authorisations were missed in the current data pull
- **Re-run TxGNN pipeline:** Once DrugBank data is complete, re-run the prediction pipeline and confirm whether a valid repurposing candidate is generated
- **Proceed to full evaluation:** If a prediction is returned, initiate evidence collection (ClinicalTrials.gov, PubMed, ICTRP) for the predicted indication and re-issue this report using the standard format
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

