---
layout: default
title: Treosulfan
parent: Model Prediction Only (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Treosulfan: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not stated in the UK licence data compiled for this report (the drug…"
---

# Treosulfan
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

# Treosulfan: From Haematopoietic Stem Cell Transplant Conditioning to Diabetic Cataract

## One-Sentence Summary

Treosulfan is an alkylating cytotoxic agent, used in conditioning treatment before haematopoietic stem cell transplantation. The TxGNN model predicts it may be effective for **diabetic cataract**, but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK licence data compiled for this report (the drug is known as an alkylating agent used in transplant conditioning) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

Other top-ranked predictions are all eye conditions with similar scores (98.9% to 99.0%): nuclear senile cataract, cortical cataract, tetanic cataract, craniostenosis cataract, immature cataract, mature cataract, type 2 diabetes-associated cataract, diabetic retinopathy and senile cataract. None has any trial or literature support.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, treosulfan is a prodrug that converts to epoxide intermediates, which alkylate DNA. It is used for conditioning before haematopoietic stem cell transplantation, where its cytotoxic and myelosuppressive effects are the intended action.

**The prediction is not supported by a plausible mechanism.** Diabetic cataract is driven by hyperglycaemia-related lens damage (polyol pathway, oxidative stress), which is unrelated to DNA alkylation. The same applies to the other predicted conditions:

- Age-related (nuclear, cortical, senile) cataract arises from oxidative damage and protein aggregation.
- Mature cataract is managed surgically.
- Tetanic cataract is treated by correcting the underlying calcium disorder.
- Diabetic retinopathy involves microvascular dysfunction and VEGF signalling, with established treatments (anti-VEGF, laser, corticosteroids).

The high TxGNN score most likely reflects the shared cataract-related neighbourhood in the knowledge graph rather than a pharmacological rationale. A systemic cytotoxic, myelosuppressive drug would carry substantial toxicity for a non-life-threatening eye condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BNF code 0801010Z0AAACAC | Treosulfan capsules 250 mg | Capsule | Not stated in the data compiled |

The record corresponds to a BNF classification code (chapter 8.1.1, alkylating drugs) rather than a standard PL number. Dosage form, manufacturer and indication text are missing from the data compiled for this report. Please check the current MHRA and BNF entries before relying on this information.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (profound myelosuppression is an expected effect at conditioning doses) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Full blood count with differential, liver and renal function; please refer to the SmPC for full details |
| Handling Protection | Must follow local cytotoxic drug handling procedures |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug-disease contraindication edges or drug interaction records were identified in the data compiled for this report. This should not be read as evidence of safety.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a graph-based score (Evidence Level L5), with no trials, no publications and no plausible mechanistic link. The risk-benefit balance of a systemic alkylating agent for cataract or diabetic retinopathy is unfavourable, given that effective surgical and medical options already exist.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a documented biological rationale linking treosulfan to lens or retinal pathology
- Preclinical evidence (L4) supporting any ocular effect
- Complete UK licence details (dosage form, manufacturer, approved indications) and the full SmPC warnings and contraindications
- Route and formulation feasibility assessment, since no ocular-suitable route has been identified
- A benefit-risk analysis against current standard care (cataract surgery, anti-VEGF, laser, corticosteroids)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

