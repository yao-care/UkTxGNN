---
layout: default
title: Lisinopril
parent: Moderate Evidence (L3-L4)
nav_order: 376
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Lisinopril: predicted new indication Posterolateral myocardial infarction (evidence level L4). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Lisinopril"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Lisinopril: From Hypertension to Posterolateral Myocardial Infarction
{: .text-alpha }

## One-Sentence Summary

Lisinopril is an ACE inhibitor, originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**,
but **no clinical trials** and **no publications** specific to this subtype were found. This is an anatomical subtype of an already-established indication rather than a true repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge graph; the UK authorisation record contains no indication text) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lisinopril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension and myocardial infarction is established, and its effects on remodelling and afterload are the accepted rationale for use after MI.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already an approved indication. The high TxGNN score most likely reflects the ontology relationship with the parent MI term rather than a new therapeutic signal. The same mechanism would apply, but no subtype-specific evidence was provided.

**Other predictions in the list (for context):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Posteroinferior myocardial infarction | 99.90% | L4 | Subtype of approved MI indication; only indirect class-level evidence |
| Pulmonary hypertension (unclear multifactorial mechanism) | 99.89% | L5 | Model prediction only; ACE inhibitors are not established therapy |
| Pulmonary hypertension owing to lung disease/hypoxia | 99.89% | L4 | Literature is mostly off-target (muscle, retina, pancreas, fish); no lisinopril clinical evidence |
| Malignant renovascular hypertension | 99.89% | L4 | Falls under approved hypertension indication; risk in bilateral renal artery stenosis |
| Malignant hypertensive renal disease | 99.89% | L4 | Extension of hypertension indication; needs renal function and potassium monitoring |
| Septal myocardial infarction | 99.88% | L4 | Subtype of approved MI indication; one case report of uncertain relevance |
| Braddock syndrome | 99.86% | L5 | No mechanistic rationale evident |
| Chronic pulmonary heart disease | 99.68% | L3 | Two small Russian-language clinical studies of lisinopril; the most interesting research question |
| Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 99.33% | L5 | COL4A1-related; no mechanistic link evident |

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

