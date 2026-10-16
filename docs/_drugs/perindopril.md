---
layout: default
title: Perindopril
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Perindopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
---

# Perindopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Perindopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Perindopril is an angiotensin-converting enzyme (ACE) inhibitor, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but the data compiled for this report contain **no clinical trials** and **no directly relevant publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 (preclinical or mechanistic evidence only; see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 4 |
| Recommended Decision | Hold |

*Note: The only publication linked to this indication is an observational study on renal cancer, which is not relevant to perindopril. Strictly, the evidence for this prediction is closer to L5 (model prediction only).*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, perindopril is an ACE inhibitor. It blocks the renin-angiotensin-aldosterone system (RAAS), which lowers blood pressure and reduces pressure within the kidney's filtering units (glomerular hypertension).

Malignant hypertensive renal disease is kidney damage caused by severely raised blood pressure. It is closely related to the approved hypertension indication, and RAAS activation is a known driver of the condition. Mechanistically, RAAS blockade is therefore plausible.

However, the very high TxGNN score (99.77%) most likely reflects how close this disease sits to hypertension in the knowledge graph, rather than independent evidence of benefit. Malignant hypertension is also an acute, high-risk setting in which ACE inhibitors may cause a sharp fall in blood pressure or kidney injury, so plausibility alone is not enough.

Other predictions generated for this drug (for context only): malignant renovascular hypertension (99.77%, L5), pulmonary hypertension due to lung disease or hypoxia (99.75%, L4, animal data only), pulmonary hypertension of unclear multifactorial mechanism (99.75%, L5), and Braddock syndrome (99.66%, L5, no rationale evident). All are currently on Hold.

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

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051Y0BBABAB | Coversyl Arginine Tab 5mg | Not stated | Not stated |
| 0205051Y0AAAAAA | Perindopril Arginine Tab 2.5mg | Not stated | Not stated |
| 0205051M0BBABAB | Coversyl Tab 4mg | Not stated | Not stated |
| 0205051M0AAAAAA | Perindopril Erbumine Tab 2mg | Not stated | Not stated |

All four authorisations are single-ingredient products and currently valid. Please refer to the BNF (cardiovascular system, ACE inhibitors) and the SmPC for approved indications and dosing.

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
- Approved indication text for the four UK authorisations, to confirm the baseline licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

