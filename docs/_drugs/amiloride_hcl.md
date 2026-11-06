---
noindex: true
sitemap: false
layout: default
title: Amiloride Hcl
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-06
predicted_indications: []
---

# Amiloride Hcl
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

## Amiloride HCL: Repurposing Evaluation — Evidence Pack Incomplete, No Prediction Generated
{: .text-alpha }

---

## One-Sentence Summary

Amiloride HCL is a well-established potassium-sparing diuretic with a long clinical history, typically used in the management of oedema and hypertension. However, this evidence pack contains **no TxGNN-generated repurposing predictions**, and multiple critical data fields — including mechanism of action, and safety data — are either absent or flagged as gaps. A substantive repurposing recommendation **cannot be made** on the basis of this evidence pack alone; remediation of data gaps is required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in evidence pack |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable — no predicted indication available |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (48 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 48 |
| Recommended Decision | **Hold** |

> ⚠️ **Data Quality Note:** Amiloride is a long-established compound. This must be investigated before any regulatory conclusions are drawn.

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction has been generated for Amiloride HCL in this evidence pack. Therefore, a formal mechanistic rationale for a new indication cannot be presented at this time.

Currently, detailed mechanism of action data is not available within the evidence pack. Based on known pharmacological information, Amiloride HCL is a potassium-sparing diuretic that acts by blocking epithelial sodium channels (ENaC) in the distal nephron, reducing sodium reabsorption whilst preserving potassium. Its established use in oedema management associated with heart failure and hypertension has been well documented since its introduction in the 1960s.

Mechanistically, ENaC blockade has attracted research interest in conditions beyond the kidney — most notably in cystic fibrosis (where airway ENaC overactivity contributes to mucociliary dysfunction) and in certain oncological contexts. However, without a formal TxGNN prediction or curated evidence, these observations remain speculative for the purposes of this report and should not be used to guide clinical decision-making.

---

## Clinical Trial Evidence

No predicted indication is available in this evidence pack. Clinical trial evidence cannot be retrieved or presented without a defined target indication.

Currently no related clinical trials are linked to a repurposing indication for this drug in the evidence pack.

---

## Literature Evidence

No predicted indication is available in this evidence pack. Literature evidence cannot be retrieved or presented without a defined target indication.

Currently no related literature is available within this evidence pack.

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0202030C0AAA8A8 | Amiloride 1.5mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AABBBB | Amiloride 1.7mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAAZAZ | Amiloride 10mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AABABA | Amiloride 12.5mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAA1A1 | Amiloride 1mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AABEBE | Amiloride 2.3mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAA4A4 | Amiloride 2.5mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAA6A6 | Amiloride 2mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAA5A5 | Amiloride 300micrograms/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAA2A2 | Amiloride 3mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAAYAY | Amiloride 400micrograms/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAA3A3 | Amiloride 4mg/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AABDBD | Amiloride 500micrograms/5ml oral liquid | Amiloride hydrochloride |
| 0202030C0AAACAC | Amiloride 5mg tablets | Amiloride hydrochloride |
| 0202030C0AAASAS | Amiloride 5mg/5ml oral solution sugar free | Amiloride hydrochloride |
| 0202030C0AAAXAX | Amiloride 5mg/5ml oral suspension | Amiloride hydrochloride |
| 0202030C0AABCBC | Amiloride 800micrograms/5ml oral liquid | Amiloride hydrochloride |
| 0202040C0BBAAAA | Amil-Co 5mg/50mg tablets | Co-amilozide (Amiloride hydrochloride/hydrochlorothiazide) |
| 0202030C0BFAAAS | Amilamont 5mg/5ml oral solution sugar free | Amiloride hydrochloride |
| 0202040C0BGAAAA | Amilmaxco 5mg/50mg tablets | Co-amilozide (Amiloride hydrochloride/hydrochlorothiazide) |

Showing 20 of 48 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

---

## Safety Considerations

All safety fields in this evidence pack are flagged as data gaps. No warnings, contraindications, or drug interaction data are available from this source.

Please refer to the SmPC and BNF (Section 2.2.3) for full safety information on Amiloride HCL. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is critically incomplete: no TxGNN repurposing prediction has been generated, and all safety fields are absent. Proceeding with any repurposing evaluation in the current state would be premature and potentially misleading.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping** — `drugbank_id` is null; this is likely the root cause of missing MOA, safety, and regulatory data. Query DrugBank using the INN "amiloride" to retrieve the correct identifier (expected: DB00594).
- **Retrieve mechanism of action (MOA)** — Query DrugBank API for Amiloride HCL's pharmacology record (ENaC blocker / potassium-sparing diuretic) to enable mechanistic plausibility analysis.
- **Retrieve SmPC safety data** — Download and parse the current MHRA SmPC to populate key warnings, contraindications, and drug interactions.
- **Re-run TxGNN prediction pipeline** — Once the DrugBank ID and regulatory data are resolved, re-run the TxGNN model to generate repurposing candidates with confidence scores.
- **Re-submit evidence pack** — Once all blocking data gaps (DG001, DG002) are remediated, resubmit for a full evaluation report.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation prior to any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

