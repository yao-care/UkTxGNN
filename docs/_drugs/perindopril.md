---
layout: default
title: Perindopril
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
monitor_inn: "perindopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Perindopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Perindopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Perindopril: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Perindopril is an angiotensin-converting enzyme (ACE) inhibitor, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but the data compiled for this report contain **no clinical trials** and **no directly relevant publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 (preclinical or mechanistic evidence only; see note below) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (23 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 23 |
| Recommended Decision | Hold |

*Note: The only publication linked to this indication is an observational study on renal cancer, which is not relevant to perindopril. Strictly, the evidence for this prediction is closer to L5 (model prediction only).*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, perindopril is an ACE inhibitor. It blocks the renin-angiotensin-aldosterone system (RAAS), which lowers blood pressure and reduces pressure within the kidney's filtering units (glomerular hypertension).

Malignant hypertensive renal disease is kidney damage caused by severely raised blood pressure. It is closely related to the approved hypertension indication, and RAAS activation is a known driver of the condition. Mechanistically, RAAS blockade is therefore plausible.

However, the very high TxGNN score (0.9977) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of benefit. Malignant hypertension is also an acute, high-risk setting in which ACE inhibitors may cause a sharp fall in blood pressure or kidney injury, so plausibility alone is not enough.

Other predictions generated for this drug (for context only): malignant renovascular hypertension (0.9977, L5), pulmonary hypertension due to lung disease or hypoxia (0.9975, L4, animal data only), pulmonary hypertension of unclear multifactorial mechanism (0.9975, L5), and Braddock syndrome (0.9966, L5, no rationale evident). All are currently on Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Observational (cohort) | Urologiia | Functional state of a solitary kidney after nephrectomy for renal cancer. Does not address malignant hypertensive nephropathy or perindopril, so it provides no support for this prediction. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0205051M0AAACAC | Perindopril erbumine 1mg/5ml oral liquid | Perindopril erbumine |
| 0205051M0AAAJAJ | Perindopril erbumine 2mg oral powder sachets | Perindopril erbumine |
| 0205051M0AAAAAA | Perindopril erbumine 2mg tablets | Perindopril erbumine |
| 0205051M0AAADAD | Perindopril erbumine 2mg/5ml oral suspension | Perindopril erbumine |
| 0205051M0AAAMAM | Perindopril erbumine 3mg/5ml oral solution | Perindopril erbumine |
| 0205051M0AAABAB | Perindopril erbumine 4mg tablets | Perindopril erbumine |
| 0205051M0AAAKAK | Perindopril erbumine 4mg/5ml oral solution | Perindopril erbumine |
| 0205051M0AAALAL | Perindopril erbumine 4mg/5ml oral suspension | Perindopril erbumine |
| 0205051M0AAAFAF | Perindopril erbumine 8mg tablets | Perindopril erbumine |
| 0205051M0AAAHAH | Perindopril erbumine 8mg/5ml oral liquid | Perindopril erbumine |
| 0205051AAAAACAC | Perindopril tosilate 10mg tablets | Perindopril tosilate |
| 0205051AAAAAAAA | Perindopril tosilate 2.5mg tablets | Perindopril tosilate |
| 0205051AAAAABAB | Perindopril tosilate 5mg tablets | Perindopril tosilate |
| 0205051M0BBAAAA | Coversyl 2mg tablets | Perindopril erbumine |
| 0205051M0BBABAB | Coversyl 4mg tablets | Perindopril erbumine |
| 0205051M0BBACAF | Coversyl 8mg tablets | Perindopril erbumine |
| 0205051N0BBAAAA | Coversyl Plus tablets | Perindopril erbumine with diuretic |
| 0205051ACAAABAB | Perindopril erbumine 4mg / Amlodipine 10mg tablets | Perindopril with calcium channel blocker |
| 0205051ACAAAAAA | Perindopril erbumine 4mg / Amlodipine 5mg tablets | Perindopril with calcium channel blocker |
| 0205051N0AAAAAA | Perindopril erbumine 4mg / Indapamide 1.25mg tablets | Perindopril erbumine with diuretic |

Showing 20 of 23 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Please refer to the BNF (cardiovascular system, ACE inhibitors) and the SmPC for approved indications and dosing.

<!-- review:begin uk-lic-20261106-perindopril-1 -->

> **Review correction (2026-11-06)**: Originally stated: "All four authorisations are single-ingredient products and currently valid. Please refer to the BNF (cardiovascular system, ACE inhibitors) and the SmPC for approved indications and dosing." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 23 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-perindopril-1 -->

---

## Safety Considerations

**Contraindications / conditions flagged in the knowledge graph** (derived from drug-disease links, not label text):
- Kidney disease, renal artery obstruction
- Liver disease, gallbladder disease
- Angioedema (including ACE-inhibitor-induced, acquired and hereditary forms)
- Neutropenia, agranulocytosis
- Hypotensive disorder
- Connective tissue, bone and cartilage disease
- Pyoureter

Relevance to this prediction: kidney disease and renal artery obstruction are directly pertinent to a renal indication and call for caution. Case reports in the compiled literature also describe life-threatening angioedema with ACE inhibitors.

**Drug Interactions:** 213 potential interactions were identified. Examples include:
- **Major:** potassium citrate, potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** metformin and other antidiabetic agents (alogliptin, canagliflozin, dapagliflozin, empagliflozin, saxagliptin, chlorpropamide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, morphine, bupropion, dronabinol, picosulfuric acid, polyethylene glycol with electrolytes

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link is plausible, but there are no clinical trials and no relevant publications. The high TxGNN score appears to reflect proximity to the existing hypertension indication. The renal safety signals for ACE inhibitors add further reason for caution.

**To proceed, the following is needed:**
- Clinical or observational evidence of perindopril (or ACE inhibitors) in malignant hypertensive nephropathy
- Mechanism of action data from DrugBank
- SmPC and BNF warnings and contraindications, which are needed before any safety screening
- A renal safety plan (renal function and potassium monitoring, caution in renal artery stenosis)
- Approved indication text, to confirm the baseline licence

<!-- review:begin uk-lic-20261106-perindopril-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Approved indication text for the four UK authorisations, to confirm the baseline licence" Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 23 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-perindopril-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "All four authorisations are single-ingredient products and currently valid" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "for the four UK authorisations" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

