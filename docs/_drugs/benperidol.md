---
layout: default
title: Benperidol
parent: Model Prediction Only (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Benperidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Benperidol: From Antisocial Personality Disorder to Insomnia

## One-Sentence Summary

Benperidol is a butyrophenone antipsychotic, listed in the data compiled for this report with an original indication of antisocial personality disorder.
The TxGNN model predicts it may be effective for **insomnia**, but there are **no clinical trials** and **no publications** supporting this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antisocial personality disorder (from the TxGNN knowledge graph; no approved indication text is available in the UK authorisation data) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 98.95% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology data show that benperidol binds the dopamine D2 and D4 receptors. It is a potent D2 antagonist of the butyrophenone class, used to manage antisocial hypersexual behaviour caused by mental illness.

The suggested link to insomnia is speculative. Sedation is a plausible secondary effect, possibly through histamine H1 or alpha-1 adrenergic blockade, but this has not been confirmed for benperidol. In antipsychotics, sedation is generally regarded as an adverse effect, not a therapeutic goal.

The extrapyramidal and QT-prolongation risks of a high-potency D2 antagonist argue against use for insomnia. The high TxGNN score is a computational output and is not evidence of clinical benefit.

Another predicted indication, "sleep disorder, initiating and maintaining sleep", is essentially the same clinical concept as insomnia. It should not be treated as independent corroboration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010B0AAAAAA | Benperidol Tab 250mcg | Tablet (as indicated by product name) | Not stated in the available data |

The identifier above is a BNF-style classification code (BNF section 4.2.1, antipsychotic drugs) and not a standard MHRA product licence number (PL). The licence details should be checked against MHRA records.

## Safety Considerations

- **Drug Interactions / Pharmacological Targets**: The interaction query returned no drug-drug interactions. The two entries are pharmacological targets: the dopamine D2 receptor (DRD2) and the D4 receptor (DRD4).
- **Class-related concerns** (from the mechanistic assessment, not label data):
  - Extrapyramidal effects and QT prolongation are risks of a high-potency D2 antagonist.
  - Antipsychotics can lower the seizure threshold.
  - D2 blockade is expected to worsen parkinsonism.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by a model score, with no trials or publications. The known pharmacology, and in particular the extrapyramidal and QT risks of a potent D2 antagonist, argues against a favourable benefit-risk balance for insomnia.

**To proceed, the following is needed:**
- Mechanism of action data, including receptor binding at H1 and alpha-1 adrenergic sites
- Label warnings and contraindications from the SmPC and BNF
- Confirmation of MHRA licence details, including the approved indication and dosage form
- Any preclinical or clinical evidence of hypnotic efficacy, with comparison against established insomnia treatments
- A safety assessment covering extrapyramidal symptoms, QT prolongation and seizure threshold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

