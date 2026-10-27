---
layout: default
title: Fluticasone
parent: Model Prediction Only (L5)
nav_order: 302
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Fluticasone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the data compiled for this report (the products are inh…"
monitor_inn: "fluticasone"
predicted_indications: ["migraine disorder", "Prinzmetal angina", "migraine with brainstem aura"]
---

# Fluticasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Fluticasone: From Respiratory Disease (Inhaled Combination Products) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Fluticasone is an inhaled glucocorticoid, available in the UK within combination inhalers with salmeterol or formoterol.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no clinical trials** and only **1 publication** (a pharmacovigilance review of adverse events, not efficacy) in the data compiled for this report.
This prediction rests on model output alone and is not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the products are inhaled fluticasone combination inhalers) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluticasone is a glucocorticoid used in combination with long-acting beta-2 agonists (salmeterol, formoterol) in inhaled products. Its anti-inflammatory activity is established in airway disease, but this has not been shown to carry over to migraine.

Neuroinflammation has been proposed as a contributor to migraine, which is the only plausible conceptual link. However, inhaled fluticasone acts mainly locally and has low systemic bioavailability, so there is no established route by which it would reach a central neurological target. The very high TxGNN score (0.992) appears to be a graph-propagation signal and not a mechanistically grounded finding.

The same applies to the other two predictions in the data: **Prinzmetal angina** (score 99.19%) and **migraine with brainstem aura** (score 99.09%). Both are L5 with no trials or publications. Prinzmetal angina is driven by coronary vasospasm, for which calcium channel blockers and nitrates are standard, and there is no recognised pathway for fluticasone. Migraine with brainstem aura is a rare subtype, and its prediction likely reflects the same signal as migraine generally.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Review | Annals of Allergy, Asthma & Immunology | WHO pharmacovigilance review of neuropsychiatric disturbances reported with intranasal corticosteroids. It addresses adverse events, not efficacy, and if anything raises a safety signal rather than supporting therapeutic use. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0302000N0AAAXAX | Fluticasone/Salmeterol inhaler 100/50 mcg, 60 doses | Inhaler | Not available |
| 0302000N0AABLBL | Fluticasone/Formoterol inhaler 50/5 mcg, 120 doses | Inhaler | Not available |

Both products are listed as valid single-entry records. The identifiers shown are those in the compiled data and are not in the standard PL number format. Approved indication text and manufacturer details were not available.

---

## Safety Considerations

- **Drug Interactions**: 474 potential interactions were identified in the interaction database. Those with a defined severity include:
  - **Major**: clarithromycin (a strong CYP3A4 inhibitor, which can raise systemic corticosteroid exposure)
  - **Moderate**: aprepitant, inhaled rapid-acting human insulin
  - Many other entries (for example prednisone, triamcinolone, simvastatin, omeprazole, morphine) have no severity grading recorded.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score. There are no trials, and the single publication concerns adverse neuropsychiatric events, not benefit. There is no plausible mechanism by which a locally acting inhaled corticosteroid would treat migraine, Prinzmetal angina or migraine with brainstem aura.

**To proceed, the following is needed:**
- Mechanism of action data and a credible pathway linking fluticasone to migraine pathophysiology
- Preclinical or clinical evidence of efficacy in migraine
- Warnings and contraindications from the SmPC and BNF, plus approved indication text for the UK products
- Assessment of route and systemic exposure, given that the available products are inhaled and migraine is a central condition
- Review of the neuropsychiatric safety signal reported with corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

