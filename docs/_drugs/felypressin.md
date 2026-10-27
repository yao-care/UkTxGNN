---
layout: default
title: Felypressin
parent: Model Prediction Only (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Felypressin: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not stated in the data compiled for this report (marketed as a priloc…"
monitor_inn: "felypressin"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "esotropia", "diabetic retinopathy", "bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "chondroid hamartoma", "non-seminomatous lesion", "tumor of testis and paratestis", "pre-malignant neoplasm"]
---

# Felypressin
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

## Felypressin: From Local Anaesthetic Adjunct to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Felypressin is a vasopressin analogue (a V1 receptor agonist) used as a vasoconstrictor alongside local anaesthetics, and in the UK it is marketed in combination with prilocaine.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are **no clinical trials** and **no publications** supporting this prediction.
It is a model prediction only, and no mechanistic rationale has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (marketed as a prilocaine/felypressin local anaesthetic injection) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, felypressin is a vasopressin analogue acting mainly as a V1 receptor agonist. Its vasoconstrictor effect is used to prolong local anaesthesia when combined with prilocaine.

No established mechanistic link has been identified between this action and drug-induced osteoporosis. The high TxGNN score reflects a model prediction only, with no supporting trial or literature evidence. At present the prediction cannot be considered mechanistically plausible.

The other top-ranked predictions are similarly unsupported:

- **Severe non-proliferative diabetic retinopathy and diabetic retinopathy:** only a speculative vasopressin–microvascular link exists. V1-mediated vasoconstriction could plausibly worsen retinal ischaemia rather than help it.
- **Esotropia:** no plausible rationale; likely a graph-embedding artefact.
- **Bronchial adenomas/carcinoids (childhood), ductal or ductular proliferation, chondroid hamartoma, non-seminomatous lesion, tumour of testis and paratestis, and pre-malignant neoplasm:** no mechanism or supporting data. Several share an identical score, suggesting non-specific predictions.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1502010S0AAAIAI (BNF-style product code; not a PL number) | Prilocaine HCl/Felypressin injection, 2 ml | Injection | Not stated in the data compiled |

The product is a single-ingredient-type listing for the prilocaine/felypressin combination, classified under the BNF local anaesthetics section (15.2).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

One point from the mechanism of action is worth noting: as a vasoconstrictor, felypressin may be undesirable where tissue perfusion is already compromised (for example, retinal ischaemia in diabetic retinopathy). No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications rest on model scores alone (L5), with no clinical trials, no literature and no identified mechanistic link. For the diabetic retinopathy predictions, the drug's vasoconstrictor action raises a potential safety concern.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) and a plausible biological link to bone metabolism
- Preclinical or observational evidence for drug-induced osteoporosis
- SmPC warnings, contraindications and interaction data for the UK product
- Confirmation of the approved indication text and licence details (PL number, dosage form, manufacturer)
- Assessment of route compatibility, as the current product is a local anaesthetic injection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

