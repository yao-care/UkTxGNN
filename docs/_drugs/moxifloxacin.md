---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Moxifloxacin is a fourth-generation fluoroquinolone antibiotic; specific original licensed indications and mechanism of action data are not available in this evidence pack. The TxGNN model predicts a possible link to **Hyperamylasemia**, but this prediction is currently supported by **no clinical trials and no published literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset — known generically as a fluoroquinolone antibiotic |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per available data) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, moxifloxacin is a fourth-generation fluoroquinolone antibiotic that acts by inhibiting bacterial DNA gyrase and topoisomerase IV; its established role is in treating bacterial infections, not metabolic or pancreatic enzyme disorders.

For hyperamylasemia specifically, no mechanistic pathway connects an antibacterial agent to pancreatic exocrine function or amylase metabolism. The evidence pack confirms this: the prediction is derived purely from the TxGNN knowledge graph score, with no supporting clinical trials or literature identified. This should be treated as a low-confidence, exploratory signal rather than a pharmacologically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Two critical data gaps affect this evaluation and should be resolved before further review:
- **Blocking**: SmPC-level warnings and contraindications are not yet available, which prevents a proper S1 safety assessment.
- **High**: Mechanism of action data has not yet been retrieved, limiting assessment of mechanistic plausibility.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (hyperamylasemia) is supported only by a raw TxGNN score, with no mechanistic rationale, clinical trials, or literature evidence (Evidence Level L5). Combined with missing safety data (warnings/contraindications) and missing MOA data, there is currently no basis to progress this candidate.

**To proceed, the following is needed:**
- Resolve DG001: obtain SmPC warnings/contraindications from the relevant regulatory source
- Resolve DG002: obtain confirmed mechanism of action data from DrugBank
- Identify any mechanistic or preclinical rationale specific to hyperamylasemia, or deprioritise this candidate in favour of stronger signals

**Note on alternative candidates:** Among the ten TxGNN-predicted indications reviewed for moxifloxacin, **bubonic plague** (rank 10, score 99.41%, Evidence Level L3) shows substantially stronger and more plausible support — moxifloxacin's known DNA gyrase/topoisomerase IV inhibition gives it direct bactericidal activity against *Yersinia pestis*, and multiple animal-model and in vitro PK/PD studies corroborate this. If a repurposing direction for moxifloxacin is to be pursued, this candidate warrants evaluation ahead of hyperamylasemia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

