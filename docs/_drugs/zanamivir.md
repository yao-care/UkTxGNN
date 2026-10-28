---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Zanamivir: predicted new indication Pyelonephritis (evidence level L5). Approved use: Influenza"
monitor_inn: "Zanamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Zanamivir: From Influenza to Pyelonephritis
{: .text-alpha }

## One-Sentence Summary

Zanamivir is a neuraminidase inhibitor, originally used to treat influenza.
The TxGNN model predicts it may be effective for **pyelonephritis**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (approved indication text is not available in the UK licence record) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Zanamivir is known to be a viral neuraminidase inhibitor, and its efficacy in influenza is established.

Pyelonephritis is typically a bacterial infection of the kidney. No plausible mechanistic link to viral neuraminidase inhibition has been identified, and the high score comes from the TxGNN model (deep learning). It may reflect similarities the model learned between related diseases, not biological evidence, and there is no supporting clinical or literature evidence. On current information, the prediction is not mechanistically credible.

Other top-ranked predictions (for example disorders of tyrosine and phenylalanine metabolism, dengue susceptibility, aspergillosis susceptibility, Legionnaires' disease susceptibility, HIV susceptibility and schistosomiasis susceptibility) show the same pattern. None has a supporting clinical trial, and the few publications retrieved concern influenza antiviral resistance and are unrelated to those conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pyelonephritis.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BNF code 0503040A0AAAAAA | Zanamivir powder for inhalation 5 mg disk with device | Inhalation powder | Not available in the compiled data |

The BNF classification for this product is within the antiviral chapter (influenza, section 5.3.4).

## Safety Considerations

- **Contraindication-related disease associations (knowledge graph, not label text):** epilepsy, chronic obstructive pulmonary disease, severe early-onset COPD, bronchial disease and delirium. These come from graph associations and should be verified against the SmPC. Inhaled zanamivir carries a recognised risk of bronchospasm in people with airways disease.
- **Drug Interactions (8 recorded):**
  - Insulin human (inhalation, rapid acting): Moderate
  - Clarithromycin, loratadine, montelukast, ketotifen, fexofenadine, ibuprofen and diclofenac: severity level not classified

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no registered trials or relevant publications. Pyelonephritis is a bacterial infection, and there is no plausible mechanistic link to a viral neuraminidase inhibitor.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic rationale for the new indication
- Preclinical or clinical evidence for activity in the predicted condition
- Approved indication text and dosage form details from the UK licence record
- SmPC warnings and contraindications for a formal safety review
- Assessment of route compatibility (inhaled powder versus the route likely needed for a kidney infection)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

