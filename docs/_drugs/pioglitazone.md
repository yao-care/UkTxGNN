---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-06
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Pioglitazone"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Pioglitazone is an insulin-sensitising agent (a PPAR-gamma agonist) originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but there are currently **no clinical trials** and **no publications** supporting this prediction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (23 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 23 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pioglitazone is a thiazolidinedione (PPAR-gamma agonist) whose efficacy in type 2 diabetes is well established. It improves insulin sensitivity and may support beta-cell function.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations. INPPL1 encodes SHIP2, a negative regulator of PI3K/insulin signalling. The only conceivable link is a shared insulin-signalling pathway. No direct connection between PPAR-gamma agonism and the disease mechanism has been established, so the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

For context, other top-ranked predictions are also unsupported by trial or literature data:

- **Stiff person syndrome (classic and focal variants):** a speculative immunomodulatory link via PPAR-gamma.
- **Thiamine-responsive dysfunction syndrome:** likely driven by the shared diabetes phenotype.
- **Localised lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic):** theoretical plausibility through adipocyte differentiation, but the conditions are localised.
- **Pancreatic agenesis:** pioglitazone needs functioning beta-cells and endogenous insulin, so it would not address the underlying deficit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0601023B0AAAAAA | Pioglitazone 15mg tablets | Pioglitazone hydrochloride |
| 0601023B0AAAEAE | Pioglitazone 15mg/5ml oral suspension | Pioglitazone hydrochloride |
| 0601023B0AAABAB | Pioglitazone 30mg tablets | Pioglitazone hydrochloride |
| 0601023B0AAADAD | Pioglitazone 30mg/5ml oral suspension | Pioglitazone hydrochloride |
| 0601023B0AAACAC | Pioglitazone 45mg tablets | Pioglitazone hydrochloride |
| 0601023B0AAAFAF | Pioglitazone 45mg/5ml oral suspension | Pioglitazone hydrochloride |
| 0601023B0BBAAAA | Actos 15mg tablets | Pioglitazone hydrochloride |
| 0601023B0BBABAB | Actos 30mg tablets | Pioglitazone hydrochloride |
| 0601023B0BBACAC | Actos 45mg tablets | Pioglitazone hydrochloride |
| 0601023W0BBAAAA | Competact 15mg/850mg tablets | Metformin hydrochloride/pioglitazone |
| 0601023B0BEAAAA | Diabiom 15mg tablets | Pioglitazone hydrochloride |
| 0601023B0BEABAB | Diabiom 30mg tablets | Pioglitazone hydrochloride |
| 0601023B0BEACAC | Diabiom 45mg tablets | Pioglitazone hydrochloride |
| 0601023B0BDACAA | Glidipion 15mg tablets | Pioglitazone hydrochloride |
| 0601023B0BDAAAB | Glidipion 30mg tablets | Pioglitazone hydrochloride |
| 0601023B0BDABAC | Glidipion 45mg tablets | Pioglitazone hydrochloride |
| 0601023B0BCADAA | Glizofar 15mg tablets (Arrow) | Pioglitazone hydrochloride |
| 0601023B0BCAAAA | Glizofar 15mg tablets (Teva) | Pioglitazone hydrochloride |
| 0601023B0BCAEAB | Glizofar 30mg tablets (Arrow) | Pioglitazone hydrochloride |
| 0601023B0BCABAB | Glizofar 30mg tablets (Teva) | Pioglitazone hydrochloride |

Showing 20 of 23 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

The identifier is not in standard MHRA "PL" format, and the approved indication text is not available. Please verify against the MHRA register and the BNF (Section 6.1.2, thiazolidinediones).

## Safety Considerations

- **Contraindications (associations from the TxGNN model (deep learning), not label text; they may reflect similarities the model learned between related diseases, not biological evidence):** kidney disease, liver disease, gallbladder disease, congestive heart failure, adrenocortical insufficiency/Addison disease, infectious disease, thymus gland disease, and several pituitary and growth hormone deficiency or hypogonadotropic hypogonadism conditions (including hypopituitarism, Sheehan syndrome and Kallmann syndrome). Congestive heart failure is the most clinically familiar of these for pioglitazone. These associations should be confirmed against the SmPC.
- **Drug Interactions:** 100 interactions were recorded. Most examples shown are Moderate, for example:
  - Hydrochlorothiazide
  - Hydrocortisone
  - Salbutamol
  - Formoterol
  - Epinephrine
  - Pseudoephedrine
  - Phenylephrine
  - Acetazolamide
  - Abiraterone
  - Alpelisib
  - Ethanol

  Minor examples include nifedipine, ethinylestradiol and topical corticosteroids.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5), with no trials or publications for opsismodysplasia and no established mechanistic link to the underlying INPPL1/SHIP2 defect. Across the other top-ranked predictions, none has supporting clinical evidence.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a plausible mechanistic rationale linking PPAR-gamma agonism to SHIP2/INPPL1 biology
- Preclinical evidence (for example, disease models or patient-derived cells)
- Verified MHRA marketing authorisation details, including the approved indication, and SmPC warnings and contraindications
- A safety assessment for a rare, likely paediatric population, given the heart failure, fracture and fluid retention concerns that apply to this drug class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

