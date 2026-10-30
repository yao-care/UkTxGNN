---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Ethosuximide: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Absence epilepsy"
monitor_inn: "Ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
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

## Ethosuximide: From Absence Epilepsy to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ethosuximide is an anti-epileptic medicine originally used to treat absence epilepsy.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but currently there are **no clinical trials** and **no publications** supporting this direction; the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ethosuximide is generally understood to block T-type calcium channels in thalamic neurons, which underlies its efficacy in absence epilepsy. This is background knowledge and not drawn from the compiled data.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*) or, in some cases, *GNAS*. These produce constitutive receptor activity and water retention despite low vasopressin levels. A link between T-type calcium channel blockade and this process has not been established. Any connection, for example through renal calcium signalling or aquaporin-2 regulation, is speculative.

The very high TxGNN score (0.9991, model rank 1420) is a model-based prediction only. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be treated as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010I0AAABAB (BNF-style product code; PL number not available) | Ethosuximide oral solution 250mg/5ml | Oral solution | Not stated in the compiled data |

The BNF classification code (0408010) corresponds to the anti-epileptic drug section (BNF chapter 4.8.1).

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindication-related** (derived from drug-disease graph edges, not from product label text; these should be checked against the SmPC): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, haematological disease, liver disease, gallbladder disease, systemic lupus erythematosus (including paediatric), neutropenia, agranulocytosis, acute intermittent porphyria.
- **Drug Interactions**: 92 interactions were recorded. All 20 listed in the data are of moderate severity, including:
  - Central nervous system depressants and opioids: morphine (including liposomal), opium, ethanol, promethazine, chlorpheniramine
  - Cannabinoids: dronabinol, nabilone
  - Antiemetics: aprepitant, metoclopramide
  - Antimalarials: chloroquine, mefloquine, hydroxychloroquine
  - Folate-related agents: folic acid, leucovorin, levoleucovorin
  - Others: sibutramine, cobicistat, deferasirox, fostamatinib

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanism linking ethosuximide to NSIAD has been established. The drug's knowledge-graph contraindications (kidney disease, blood disorders) also warrant caution in a renal-related condition.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a testable hypothesis linking T-type calcium channel blockade to V2 receptor or aquaporin-2 signalling
- Preclinical studies (for example, cell models carrying *AVPR2* gain-of-function variants)
- Warnings and contraindications from the SmPC and BNF, to complete safety screening
- Approved indication text and PL number for the UK authorisation
- Assessment of route and formulation compatibility for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

