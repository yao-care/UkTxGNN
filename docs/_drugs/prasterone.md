---
layout: default
title: Prasterone
parent: Model Prediction Only (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prasterone: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Systemic lupus erythematosus"
---

# Prasterone
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

# Prasterone: From Systemic Lupus Erythematosus to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Prasterone (dehydroepiandrosterone, DHEA) was originally associated with systemic lupus erythematosus and psychologic dyspareunia.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on a graph-based model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus; paediatric systemic lupus erythematosus; psychologic dyspareunia (knowledge graph indications; no approved indication text is available for the UK product) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, prasterone is a sex-steroid precursor (DHEA), with immunomodulatory activity that is relevant to its link with lupus. Pharmacology data compiled for this report also show an interaction with glycine receptors.

Heparin cofactor 2 deficiency is a heritable defect in a serpin (SERPIND1) that regulates coagulation. Prasterone has no established mechanism for correcting such a deficiency. The high score appears to reflect network proximity in the knowledge graph rather than a biological rationale. Any link, for example indirect effects on coagulation through sex-steroid metabolism, is speculative.

The same pattern applies to the other top-ranked predictions, which are mostly coagulation and platelet disorders (factor V excess, antithrombin type 2 deficiency, thrombophilia, protein S deficiency, pseudo-von Willebrand disease, primary platelet release disorder). Of the ten predictions, **scleroderma** is the most mechanistically coherent, as it is an autoimmune connective tissue disease related to lupus. It is flagged as a research question and would need a dedicated literature and trial search.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0604030Q0AAAIAI | Prasterone Tab 25mg | Not specified | Not specified |

The identifier above resembles a BNF-style product code (BNF section 6.4.3 relates to sex hormones) rather than a standard PL number, and it should be verified against the MHRA register. The compiled data show one valid single-ingredient authorisation. No NICE-appraised indication was identified in the data.

## Safety Considerations

- **Drug Interactions / Pharmacology**: One pharmacological interaction was recorded, with the glycine receptor (all subtypes), where dehydroepiandrosterone is listed as a metabolite ligand. No clinically graded drug-drug interactions were identified.
- **Coagulation concern**: Oral androgens and oestrogens can influence haemostatic factors. For the thrombophilia-type predictions, this raises a possible thrombotic safety concern rather than a therapeutic rationale, and a safety review would be needed before any efficacy question.

Please refer to the SmPC and BNF for full safety information, including warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest solely on model scores, with no trials or publications and no plausible mechanism for heparin cofactor 2 deficiency. Safety data (warnings and contraindications) are also missing, so the evidence level remains L5.

**To proceed, the following is needed:**
- Mechanism of action data for prasterone
- Product label information (warnings, contraindications, approved indication, dosage form) for the UK authorisation
- A dedicated literature and trial search, with scleroderma prioritised as the most coherent candidate
- A safety review of haemostatic effects before any thrombophilia-related indication is considered
- Assessment of route and formulation compatibility with the predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

