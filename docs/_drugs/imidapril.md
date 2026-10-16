---
layout: default
title: Imidapril
parent: Model Prediction Only (L5)
nav_order: 333
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Imidapril: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
---

# Imidapril
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

# Imidapril: From Hypertension to Pulmonary Hypertension

## One-Sentence Summary

Imidapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but **no clinical trials or publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); no approved indication text is available in the UK authorisation data |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, imidapril is an ACE inhibitor prodrug, converted to its active form imidaprilat. It reduces angiotensin II formation and lowers vascular resistance. Its efficacy in systemic hypertension is established.

The renin-angiotensin system also influences pulmonary vascular tone and remodelling, which gives a plausible but unproven link to pulmonary hypertension. However, ACE inhibitors have not shown reliable benefit in pulmonary arterial hypertension, and systemic hypotension is a risk. The TxGNN score is a computational prediction only.

**Other predicted indications (all L5, all Hold, no trials or literature):**

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.78% | Theoretical attenuation of hypoxia-driven vascular remodelling; ACE inhibition may impair hypoxic pulmonary vasoconstriction and ventilation-perfusion matching |
| Malignant hypertensive renal disease | 99.76% | Close to the original indication, so more an extension than true repurposing; ACE inhibitors can worsen renal function in acute settings (e.g. renal artery stenosis, volume depletion) |
| Malignant renovascular hypertension | 99.76% | Strongly renin-angiotensin dependent, but ACE inhibitors can precipitate acute kidney injury in bilateral renal artery stenosis or a solitary kidney |
| Braddock syndrome | 99.70% | No clear mechanistic link; the score likely reflects network proximity to hypertension-related nodes |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051W0AAAAAA | Imidapril HCl Tab 10 mg | Tablet (as indicated by product name) | Not stated in the data compiled |

The listed authorisation number is not in the standard UK PL format, so it should be verified against the MHRA register. Current MHRA and NICE status for imidapril should also be confirmed.

## Safety Considerations

- **Drug Interactions**: The only interaction record is pharmacological. Imidapril acts on its target, angiotensin-converting enzyme (ACE), and no interacting drugs with severity levels were identified.
- **Mechanism-based cautions** (from the repurposing assessment, not label text): ACE inhibitors can worsen renal function in renal artery stenosis (especially bilateral or in a solitary kidney) and volume depletion, and can cause systemic hypotension.

Warnings and contraindications from the product label were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no clinical trials or publications. ACE inhibitors have not shown reliable benefit in pulmonary arterial hypertension, and there are renal and haemodynamic safety concerns. The two renal and renovascular hypertension predictions are close to the existing indication and would need careful safety review.

**To proceed, the following is needed:**
- Product label safety data (warnings and contraindications) from the SmPC and BNF
- Mechanism of action data (e.g. from DrugBank)
- A systematic literature search on ACE inhibitors in pulmonary hypertension
- Verification of the UK marketing authorisation details (dosage form, approved indication, MHRA register entry)
- A clear hypothesis for the target pulmonary hypertension subgroup, and a safety plan for renal function and blood pressure, before any trial is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

