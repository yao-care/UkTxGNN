---
noindex: true
sitemap: false
layout: default
title: Azelastine
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Azelastine
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

## Azelastine: Evaluation Pending — No Repurposing Prediction Available
{: .text-alpha }

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
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (13 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 13 |
| Recommended Decision | Hold |

---

## Why Evaluation Cannot Proceed

The evidence pack for Azelastine (DB00972) contains two critical gaps that prevent the TxGNN pipeline from generating a repurposing hypothesis, and prevent the evaluation team from conducting any mechanistic or safety analysis.

No mechanism of action (MOA) data is recorded in this evidence pack. MOA information is fundamental to repurposing analysis — without it, there is no pharmacological basis on which to assess whether the drug's biological targets are relevant to any candidate disease. The evidence pack metadata classifies this as a **High-severity** gap (DG002), requiring resolution via the DrugBank API.

The TxGNN model returned no predicted indications for this compound. Based on how the pipeline operates, this is most likely a consequence of incomplete or unresolved DrugBank input data rather than a genuine absence of repurposing potential. Azelastine is an established antihistamine in widespread international clinical use, and repurposing signal is plausible once the pipeline inputs are corrected.

Clinicians should note that Azelastine has been in clinical use internationally (as a nasal spray and eye drops for allergic conditions), and the MHRA Product Licence register should be consulted directly to verify current UK authorisation status before drawing conclusions from this figure.

<!-- review:begin uk-lic-20261106-azelastine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The UK marketing authorisation data also appears incomplete: zero MHRA licences are recorded. Clinicians should note that Azelastine has been in clinical use internationally (as a nasal spray and eye drops for allergic conditions), and the MHRA Product Licence register should be consulted directly to verify current UK authorisation status before drawing conclusions from this figure." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 13 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-azelastine-1 -->

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
- **Re-run TxGNN pipeline:** Once DrugBank data is complete, re-run the prediction pipeline and confirm whether a valid repurposing candidate is generated
- **Proceed to full evaluation:** If a prediction is returned, initiate evidence collection (ClinicalTrials.gov, PubMed, ICTRP) for the predicted indication and re-issue this report using the standard format

<!-- review:begin uk-lic-20261106-azelastine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "**Verify UK market status:** Cross-check against the MHRA Product Licence register to confirm whether existing authorisations were missed in the current data pull / **Re-run TxGNN pipeline:** Once DrugBank data is complete, re-run the prediction pipeline and confirm whether a valid repurposing candidate is generated" Removed: it said licence data still had to be fetched from the MHRA or that licence records were incomplete; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which does not contain MHRA licences. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-azelastine-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The UK marketing authorisation data also appears incomplete: zero MHRA licences are recorded" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "**Verify UK market status:** Cross-check against the MHRA Product Licence register to confirm whether existing authorisations were missed in" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

