---
layout: default
title: Candesartan Cilexetil
parent: Model Prediction Only (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Candesartan Cilexetil: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Candesartan cilexetil"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Candesartan Cilexetil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Candesartan Cilexetil: From Hypertension to Malignant Renovascular Hypertension
{: .text-alpha }

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but currently there are **no clinical trials** and **no directly relevant publications** supporting this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the approved indication text is not available in the data compiled for this report |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, candesartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is well established.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, so blocking the AT1 receptor is mechanistically plausible. The high TxGNN score probably reflects the close similarity of this condition to the approved hypertension indication in the knowledge graph, rather than independent evidence.

There is an important safety caveat. Drugs that block the renin-angiotensin system can precipitate acute renal failure in patients with bilateral renal artery stenosis, or stenosis affecting a solitary kidney. This is exactly the population in which renovascular hypertension occurs, so the benefit-risk balance needs careful evaluation before any further development.

**Other predictions in the data (all L5, all Hold):**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 99.68% | Renoprotective role of ARBs in other kidney diseases is an inference only; no direct evidence |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.67% | Heterogeneous category; systemic hypotension is a concern |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.67% | Plausible but unproven link; the two retrieved papers do not directly support it |
| 5 | Braddock syndrome | 99.56% | No mechanistic link identified; likely a knowledge-graph artefact |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the lead prediction (malignant renovascular hypertension). The only publications retrieved relate to the rank 4 prediction, and both are tangential:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31396238](https://pubmed.ncbi.nlm.nih.gov/31396238/) | 2019 | Preclinical (mouse) | Frontiers in Immunology | Candesartan cilexetil improved neurological outcomes in a mouse model of neonatal hypoxia-induced seizures through anti-inflammatory effects; not a pulmonary hypertension study |
| [21423692](https://pubmed.ncbi.nlm.nih.gov/21423692/) | 2011 | Preclinical (rat) | Evid Based Complement Alternat Med | Hachimijiogan (a herbal formulation, not candesartan) was compared with an angiotensin II receptor blocker in a remnant kidney model; not relevant to pulmonary hypertension |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205052C0AAABAB | Candesartan Cilexetil Tab 4mg | Tablet (not specified in the data) | Not available in the data compiled for this report |

The authorisation identifier shown is as recorded in the data and is not in the standard MHRA "PL" format. It should be verified against the MHRA register. Candesartan sits within the BNF cardiovascular chapter (angiotensin-II receptor antagonists); NICE-appraised indications should be checked directly.

## Safety Considerations

**Contraindications and conditions of concern (from the TxGNN knowledge graph, not from product label text):**

The knowledge graph links candesartan to the following conditions as contraindications or cautions. These should be confirmed against the SmPC:

- **Renal and vascular:** anuria, impaired renal function, renal artery obstruction, hypotensive disorder
- **Metabolic and electrolyte:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, phosphorus metabolism disease, hyperparathyroidism, osteitis fibrosa, nephrocalcinosis, hyperuricaemia, gout
- **Hepatic and biliary:** liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis, neonatal jaundice
- **Autoimmune:** systemic lupus erythematosus (including paediatric)

Some of these entries appear to reflect warnings for combination products (for example, those containing a thiazide diuretic) rather than candesartan alone, so they should be interpreted with caution.

Please refer to the SmPC and BNF for authoritative warnings and drug interaction information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials and no directly relevant literature. The target population, renovascular disease, carries a recognised risk of acute renal failure with renin-angiotensin system blockade.

**To proceed, the following is needed:**
- Product label data (indication, warnings and contraindications) for the UK authorisation, including a verified MHRA licence number and dosage form
- Mechanism of action data confirmed from a source such as DrugBank
- A systematic literature review on ARBs in renovascular hypertension and malignant hypertension, including renal safety in renal artery stenosis
- A safety plan covering renal function and potassium monitoring, and exclusion of bilateral renal artery stenosis
- Review of whether the remaining predictions (pulmonary hypertension, Braddock syndrome) merit any further work, given the lack of mechanistic support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

