---
layout: default
title: Hypromellose
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hypromellose: predicted new indication Hepatic veno-occlusive disease-immunodeficiency syndrome (evidence level L5). Approved use: Not stated in the licence data (ocular lubrication is the product's …"
monitor_inn: "Hypromellose"
predicted_indications: ["hepatic veno-occlusive disease-immunodeficiency syndrome", "pancytopenia due to IKZF1 mutations", "hepatic veno-occlusive disease", "combined immunodeficiency due to CRAC channel dysfunction", "absent thumb-short stature-immunodeficiency syndrome", "facial dysmorphism-immunodeficiency-livedo-short stature syndrome", "immuno-osseous dysplasia", "psoriasis", "autoinflammatory syndrome with pyogenic bacterial infection and amylopectinosis", "human herpesvirus 8-related tumor"]
---

# Hypromellose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Hypromellose: From Ocular Lubrication to Hepatic Veno-Occlusive Disease-Immunodeficiency Syndrome

## One-Sentence Summary

Hypromellose is a cellulose-derived polymer used as an ocular lubricant, viscosity enhancer and film former, and it is currently marketed in the UK as 0.3% eye drops.
The TxGNN model predicts it may be effective for **hepatic veno-occlusive disease-immunodeficiency syndrome**, but there are **no clinical trials** and **no publications** supporting this prediction.
The result is a graph-based signal only, with no biological rationale behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (ocular lubrication is the product's known use as an eye drop) |
| Predicted New Indication | Hepatic veno-occlusive disease-immunodeficiency syndrome |
| TxGNN Prediction Score | 98.30% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hypromellose is an inert, cellulose-derived excipient with negligible systemic absorption. Its role in eye drops is to lubricate the ocular surface and increase the viscosity of the formulation.

No mechanistic link has been identified between hypromellose and this disease. The predicted condition is an autosomal recessive immunodeficiency caused by SP110 mutation. It is a genetic disorder, and a non-absorbed polymer has no known way of influencing it. The high score of 0.983 most likely reflects patterns in the knowledge graph rather than real biology.

The other nine top-ranked predictions show the same pattern. They include pancytopenia due to IKZF1 mutations, hepatic veno-occlusive disease, CRAC channel dysfunction, several rare immunodeficiency syndromes, a HOIL-1 deficiency disorder and HHV-8-related tumours. None has a plausible mechanism, trial or publication. Psoriasis (rank 8) is the most biologically conceivable, since cellulose-ether polymers are used as vehicles in topical products and may have a mild emollient or barrier effect. However, this is not a disease-modifying mechanism, and no data support it.

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
| 1108010F0AAAAAA | Hypromellose Eye Drops 0.3% | Eye drops | Not stated in the licence data |

This is a single-ingredient product with a valid status. The data compiled for this report do not include NICE appraisals or a BNF classification for it.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone (Evidence Level L5), with no trials, no literature and no plausible mechanism. Hypromellose is a pharmacologically inert, non-absorbed excipient, so the high score is most likely a network artefact.

**To proceed, the following is needed:**
- Mechanism of action data for hypromellose
- Any preclinical or clinical evidence linking it to the predicted condition (none currently exists)
- Safety information from the SmPC and BNF, which was not available in the compiled data
- Route and formulation compatibility assessment, since the only UK product is an ophthalmic preparation and the predicted conditions are systemic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

