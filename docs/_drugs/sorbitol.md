---
layout: default
title: Sorbitol
parent: Model Prediction Only (L5)
nav_order: 574
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Sorbitol: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "sorbitol"
predicted_indications: ["exercise-induced malignant hyperthermia"]
---

# Sorbitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Sorbitol: From an Unspecified Original Indication to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Sorbitol is a sugar alcohol used as an osmotic agent, laxative and excipient. No original indication is recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are **no clinical trials** and **no publications** supporting this direction. The prediction rests on a computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 0.9940 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sorbitol is generally known as an osmotic agent, laxative and pharmaceutical excipient. No efficacy in a defined original indication could be confirmed from the data compiled.

Malignant hyperthermia is a disorder of skeletal muscle calcium regulation, typically linked to RYR1 variants and triggered by volatile anaesthetics or succinylcholine. No plausible direct link between sorbitol and ryanodine receptor function or calcium handling is evident. The high score (0.9940) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a true therapeutic effect. The prediction needs mechanistic validation before it can be taken forward.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1203050A0AAAKAK | Mucin/Xylitol/Sorbitol Lozenge 65/59/55.5 mg | Not specified | Not specified |

The single authorisation is a combination lozenge product (mucin, xylitol and sorbitol). The listed number does not follow the usual MHRA PL format and should be verified against the MHRA register.

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (not label text) links sorbitol to a contraindication in **active peptic ulcer disease**.
- **Drug Interactions** (2 found):
  - **Tolevamer**: Major
  - **Lamivudine**: Moderate

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanistic link to the muscle calcium dysregulation underlying malignant hyperthermia. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a documented mechanistic rationale linking sorbitol to ryanodine receptor or calcium handling
- Confirmation of the original indication, dosage form and approved indication for the UK authorisation
- Label-based warnings and contraindications from the SmPC and BNF
- Preclinical or mechanistic studies to support any plausible biological link
- Review of the Major interaction with tolevamer and the knowledge-graph peptic ulcer contraindication signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

