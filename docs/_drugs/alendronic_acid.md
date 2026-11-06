---
noindex: true
sitemap: false
layout: default
title: Alendronic Acid
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-06
predicted_indications: []
---

# Alendronic Acid
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

## Alendronic Acid: Drug Repurposing Evaluation — No Candidate Indications Identified
{: .text-alpha }

## One-Sentence Summary

Alendronic acid is a nitrogen-containing bisphosphonate widely used clinically for the treatment and prevention of osteoporosis and Paget's disease of bone. The current Evidence Pack (version v4, data cutoff 2026-04-04) contains **no TxGNN-predicted repurposing candidates**, making a standard repurposing evaluation impossible at this stage. Two blocking data gaps — UK regulatory labelling and mechanism of action data — must be resolved before this assessment can progress.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | None identified |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No predictions generated |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (16 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 16 |
| Recommended Decision | Hold |

> ⚠️ **Data Quality Notice**: This Evidence Pack is materially incomplete. Alendronic acid (DrugBank DB00630) is a well-established bisphosphonate with multiple MHRA-authorised products in the UK (e.g., Fosamax, and numerous generics). This must be investigated and corrected before any repurposing analysis is meaningful.

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0606020A0AAAAAA | Alendronic acid 10mg tablets | Alendronic acid |
| 0606020A0AAADAD | Alendronic acid 35mg/5ml oral solution | Alendronic acid |
| 0606020A0AAABAB | Alendronic acid 5mg tablets | Alendronic acid |
| 0606020A0AAAHAH | Alendronic acid 70mg effervescent tablets sugar free | Alendronic acid |
| 0606020A0AAACAC | Alendronic acid 70mg tablets | Alendronic acid |
| 0606020A0AAAFAF | Alendronic acid 70mg/100ml soln unit dose sugar free | Alendronic acid |
| 0606020A0AAAEAE | Alendronic acid 70mg/5ml oral solution | Alendronic acid |
| 0606020A0AAAGAG | Alendronic acid 70mg/75ml oral solution unit dose | Alendronic acid |
| 0606020Y0AAABAB | Alendronic acid 70mg / Colecalciferol 140microgram tablets | Alendronic acid/colecalciferol |
| 0606020Y0AAAAAA | Alendronic acid 70mg / Colecalciferol 70microgram tablets | Alendronic acid/colecalciferol |
| 0606020Y0BCAAAB | Bentexo 70mg/5,600unit tablets | Alendronic acid/colecalciferol |
| 0606020A0BCAAAH | Binosto 70mg effervescent tablets | Alendronic acid |
| 0606020A0BBAAAA | Fosamax 10mg tablets | Alendronic acid |
| 0606020A0BBABAB | Fosamax 5mg tablets | Alendronic acid |
| 0606020A0BBADAC | Fosamax Once Weekly 70mg tablets | Alendronic acid |
| 0606020Y0BBAAAA | Fosavance tablets | Alendronic acid/colecalciferol |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) was returned in this Evidence Pack.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is too incomplete to support any repurposing evaluation — there are no predicted indications, no original indication records, no UK regulatory data, and no safety information.

**To proceed, the following is needed:**

- **[Critical — DG001]** Retrieve and parse the UK SmPC (MHRA-approved labelling) for Alendronic acid to populate approved indications, warnings, and contraindications
- **[Critical — DG002]** Query DrugBank API (DB00630) to retrieve mechanism of action, pharmacodynamics, and drug interaction data
- **[Critical]** Re-run the TxGNN prediction pipeline; confirm that `predicted_indications` is populated with at least one candidate before generating a repurposing report
- **[Recommended]** Once predictions are available, cross-reference with NICE technology appraisals and BNF bone metabolism drug category (BNF Chapter 6.6) for contextual relevance

---

*This report is generated for research purposes only and does not constitute medical advice. Any drug repurposing candidate identified by TxGNN requires clinical validation before application. All findings should be interpreted in the context of current clinical guidelines and regulatory requirements.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

