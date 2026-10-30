---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 531
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Quinapril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Quinapril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Quinapril
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

## Quinapril: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Quinapril is an angiotensin-converting enzyme (ACE) inhibitor originally used to treat hypertension.
but there are currently **no clinical trials** and **no publications** directly supporting this prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, quinapril is an ACE inhibitor. It lowers angiotensin II and therefore blood pressure. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension.

Renovascular hypertension is strongly driven by the renin-angiotensin-aldosterone system (RAAS), so blocking this pathway is plausible. However, the high TxGNN score probably reflects similarity to the approved hypertension indication rather than new evidence.

There is also a notable safety concern. ACE inhibitors carry a known risk of acute renal function decline in bilateral renal artery stenosis or in a solitary kidney, which is exactly the population in which renovascular hypertension occurs.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 0.9986 | L5 | Hold |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9985 | L5 | Research Question |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 0.9985 | L5 | Hold |
| 5 | Braddock syndrome | 0.9979 | L5 | Hold |

- **Malignant hypertensive renal disease:** RAAS blockade is mechanistically relevant, because reduced intraglomerular pressure and antiproteinuric effects are known class benefits. No quinapril-specific evidence was available, and renal safety (hyperkalaemia, creatinine rise) would need assessment.
- **Pulmonary hypertension due to lung disease/hypoxia:** Animal studies suggest quinapril reduces hypoxic pulmonary hypertension and vascular remodelling (see Literature Evidence). There is no human evidence, and systemic vasodilation could worsen ventilation-perfusion matching.
- **Pulmonary hypertension, unclear multifactorial mechanism:** Any rationale is extrapolated from RAAS involvement in pulmonary vascular remodelling. The group is heterogeneous and no direct evidence is available.
- **Braddock syndrome:** No clear mechanistic link could be established. The high score is likely a TxGNN model (deep learning) artefact.

## Clinical Trial Evidence


## Literature Evidence

No literature is available for the top-ranked prediction. The only publications identified relate to the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), and both are preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Preclinical (animal study) | Circulation | Inhibiting tissue ACE with quinapril reduced hypoxic pulmonary hypertension and pulmonary vascular remodelling |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Preclinical (animal study) | J Cardiovasc Pharmacol | In rats after myocardial infarction, quinapril preserved left ventricular function and energy metabolism (indirect relevance) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051Q0AAACAC | Quinapril HCl Tablets 20 mg | Tablet | Not stated in the data compiled for this report |

Note: this identifier is formatted like a BNF code rather than an MHRA PL number, so the MHRA licence details should be verified.

## Safety Considerations

- **Contraindications and conditions of concern (from the knowledge graph, not label text):** kidney disease, anuria, angioedema (including hereditary, acquired and RAAS-blocker-induced forms), pancreatitis, liver disease, hepatic encephalopathy/coma, gallbladder disease, systemic lupus erythematosus and connective tissue disease, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, hyperuricaemia and gout, neutropenia and agranulocytosis, hypotension, hyperparathyroidism and bone disease, and neonatal jaundice.
- **Drug Interactions:** 100 interactions were identified. The one rated Major is **potassium citrate** (risk of hyperkalaemia). Moderate interactions include metformin, aspirin, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin), tetracyclines (doxycycline, tetracycline), morphine, bupropion, atropine, chlorpropamide, and several bowel preparations and laxatives.
- **Renal safety:** ACE inhibitors may cause acute renal function decline in bilateral renal artery stenosis or a solitary kidney. This is directly relevant to the top two predicted indications.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no clinical trials or literature. The high score likely reflects similarity to the existing hypertension indication. The renal safety risk of ACE inhibitors in renovascular disease adds further caution.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- SmPC and BNF warnings and contraindications, which are currently missing and block safety screening
- Verification of the UK licence details (MHRA PL number, dosage form, approved indication)
- Clinical evidence for quinapril, or the ACE inhibitor class, in renovascular hypertension, including renal safety data in bilateral renal artery stenosis
- For pulmonary hypertension, human studies beyond the preclinical findings, which would need to be assessed as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

