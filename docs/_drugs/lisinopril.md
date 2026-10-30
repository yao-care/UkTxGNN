---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 376
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Lisinopril"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
description: "Lisinopril: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Not recorded in the local data"
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Lisinopril: Pulmonary hypertension with unclear multifactorial mechanism
{: .text-alpha }

## One-Sentence Summary

Lisinopril is an ACE inhibitor, originally used to treat hypertension and myocardial infarction.
but **no clinical trials** and **no publications** specific to this subtype were found. This is an anatomical subtype of an already-established indication rather than a true repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lisinopril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension and myocardial infarction is established, and its effects on remodelling and afterload are the accepted rationale for use after MI.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already an approved indication. The high TxGNN score most likely reflects the ontology relationship with the parent MI term rather than a new therapeutic signal. The same mechanism would apply, but no subtype-specific evidence was provided.

**Other predictions in the list (for context):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Pulmonary hypertension (unclear multifactorial mechanism) | 0.9989 | L5 | Model prediction only; ACE inhibitors are not established therapy |
| Pulmonary hypertension owing to lung disease/hypoxia | 0.9989 | L5 | Literature is mostly off-target (muscle, retina, pancreas, fish); no lisinopril clinical evidence |
| Malignant hypertensive renal disease | 0.9989 | L5 | Extension of hypertension indication; needs renal function and potassium monitoring |
| Braddock syndrome | 0.9986 | L5 | No mechanistic rationale evident |
| Chronic pulmonary heart disease | 0.9968 | L3 | Two small Russian-language clinical studies of lisinopril; the most interesting research question |
| Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 0.9933 | L5 | COL4A1-related; no mechanistic link evident |

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

For the lower-ranked prediction **chronic pulmonary heart disease**, the following clinical publications were retrieved (design and sample size could not be verified):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (likely non-randomised) | Kardiologiia | Lisinopril 10 mg/day was associated with attenuated pulmonary hypertension, improved right ventricular systolic function and better diastolic filling in patients with heart failure, ischaemic heart disease and COPD |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (likely non-randomised) | Problemy tuberkuleza i boleznei legkikh | Lisinopril in chronic cor pulmonale; no abstract available |
| [26895877](https://pubmed.ncbi.nlm.nih.gov/26895877/) | 2016 | Review | Eur J Pediatr | Discusses ACE inhibitor use in paediatric chronic heart failure; indirect relevance only |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051L0AAAAAA | Lisinopril Tablets 2.5 mg | Tablet | Not stated in the data compiled for this report |

The identifier above appears to be a BNF-style product code rather than an MHRA PL number, and the record contains no indication or manufacturer text. Please verify against the MHRA product database and the BNF.

## Safety Considerations

- **Contraindications and disease associations flagged in the knowledge graph** (not label text, so they should be confirmed against the SmPC): angioedema (including hereditary, acquired and ACE-inhibitor-induced), kidney disease, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, aortic stenosis and aortic valve disease, hypotension, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, hyperparathyroidism, neutropenia and agranulocytosis, systemic lupus erythematosus and connective tissue disease, and bone disease.
- **Drug Interactions** (100 interactions recorded; main ones shown):
  - **Major:** potassium citrate, potassium bicarbonate (risk of hyperkalaemia)
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), aspirin, morphine, bupropion, dronabinol, and bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes)
- **Literature safety signals:** a case report of severe bradycardia and hypotension with concomitant tizanidine and lisinopril (PMID 20852161), and a case report of lisinopril-induced small bowel angioedema (PMID 42226836).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posterolateral myocardial infarction is a subtype of an indication for which lisinopril is already established, so this is not a genuine repurposing opportunity. The prediction has no subtype-specific trials or literature (L4). Of the other predictions, chronic pulmonary heart disease is the only one with direct lisinopril clinical data (L3), but these are small, likely non-randomised studies.

**To proceed, the following is needed:**
- Confirmation of the UK authorisation details (MHRA PL number, dosage forms, approved indications) from the MHRA database and SmPC
- Label-based warnings and contraindications from the SmPC and BNF to replace the knowledge-graph-derived list
- Mechanism of action data (currently unavailable)
- For chronic pulmonary heart disease: retrieval of full texts to verify design and sample size, followed by a controlled trial if the signal holds
- Review of whether MI subtype terms should be excluded from the repurposing pipeline as ontology duplicates of an approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

