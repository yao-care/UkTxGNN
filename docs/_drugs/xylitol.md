---
layout: default
title: Xylitol
parent: Model Prediction Only (L5)
nav_order: 656
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Xylitol: predicted new indication Meningococcal infection (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "xylitol"
predicted_indications: ["meningococcal infection"]
---

# Xylitol
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

## Xylitol: From an Unspecified Original Indication to Meningococcal Infection
{: .text-alpha }

## One-Sentence Summary

Xylitol is a sugar alcohol sold in the UK as part of a mucin/xylitol/sorbitol lozenge, but no approved indication is recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **meningococcal infection**,
but there are currently **no clinical trials** and **no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded. Based on the information compiled, no direct mechanistic link between xylitol and meningococcal infection has been established. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

One speculative, unverified rationale is that xylitol has been reported to reduce the adherence of some respiratory bacteria (for example *Streptococcus pneumoniae* and *Haemophilus influenzae*) to nasopharyngeal epithelium and to reduce biofilm formation. Whether this extends to *Neisseria meningitidis* colonisation is not supported by the data compiled for this report.

Invasive meningococcal disease is life-threatening. Xylitol would not be expected to replace antibiotic treatment or vaccination.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1203050A0AAAKAK | Mucin/Xylitol/Sorbitol Lozenge 65/59/55.5 mg | Not stated | Not stated |

This is a single-ingredient authorisation record that is currently valid. The identifier shown is as supplied in the compiled data and is not in the standard MHRA "PL" format, so it should be verified against the MHRA register.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (PrimeKG) links xylitol to a contraindication edge for **dental fluorosis**. This comes from the knowledge graph and not from product label text, so it should be interpreted cautiously.

No drug interaction records were found in the data compiled for this report.

Please refer to the SmPC and BNF for full warnings, contraindications and interaction information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational model. There are no registered trials or publications, no mechanism of action data, no recorded original indication, and no label-based safety data. Meningococcal infection is a serious condition where unproven treatments carry significant risk.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- The approved indication, dosage form and SmPC for the authorised lozenge product
- Label-based warnings and contraindications from the SmPC and BNF
- Preclinical or observational evidence on xylitol and *Neisseria meningitidis* adherence or nasopharyngeal carriage
- Review of the dental fluorosis contraindication signal
- Clarification of the intended route and formulation, as route compatibility has not been assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

