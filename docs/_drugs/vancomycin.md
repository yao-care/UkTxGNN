---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 610
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic long established for treating Gram-positive bacterial infections, including MRSA. The TxGNN model's top-ranked prediction for this drug is **Diffuse Scleroderma**, but this candidate has **no supporting clinical trials** and only **one loosely related case report**, and the evidence pack's own mechanistic review flags it as likely knowledge-graph noise rather than a genuine therapeutic signal.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in the UK regulatory dataset; per the evidence pack's mechanistic notes, Vancomycin is an established treatment for Gram-positive bacterial infections (e.g., MRSA) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured record (original MOA field is a data gap). However, the evidence pack's own mechanistic commentary consistently describes Vancomycin as a glycopeptide antibiotic that inhibits cell wall synthesis in Gram-positive bacteria — a well-characterised, purely antibacterial mode of action.

Diffuse scleroderma is an autoimmune fibrotic connective tissue disorder with no established relationship to bacterial cell wall biology. The repurposing rationale attached to this prediction explicitly states that there is no known mechanistic link between Vancomycin's antibacterial activity and scleroderma's autoimmune-fibrotic pathology, and that the single supporting literature reference is a case report of drug-induced erythroderma/sepsis with eosinophilia — a report about an adverse cutaneous reaction, not a treatment study for scleroderma.

Taken together, this candidate does not have a plausible pharmacological basis. It is assessed as a likely artefact of knowledge-graph co-occurrence rather than a genuine repurposing signal, consistent with its L5 evidence level (model prediction only) and "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Describes a case of diffuse exfoliative erythroderma with sepsis and eosinophilia in a patient previously treated with antibiotics (including agents in the same broad drug-rash context). Does not evaluate Vancomycin's efficacy in scleroderma and provides no supporting evidence for this indication. |

## UK Market Information

No UK marketing authorisation records are available in this Evidence Pack. Vancomycin is currently recorded as **not marketed** in the UK dataset used for this analysis (0 licenses on file).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction (Diffuse Scleroderma) has no clinical trial evidence and only one tangentially related case report describing an adverse skin reaction, not therapeutic benefit.
- The evidence pack's own mechanistic analysis concludes there is no plausible biological rationale linking Vancomycin's cell-wall-synthesis-inhibiting mechanism to scleroderma's autoimmune fibrotic pathology, and classifies this as likely a false-positive graph co-occurrence.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for Vancomycin (currently a High-severity data gap, DG002)
- TFDA/MHRA-equivalent label warnings and contraindications (currently a Blocking data gap, DG001) before any safety pre-screening (S1) can begin
- At minimum, preclinical or mechanistic studies specifically linking glycopeptide antibiotics to antifibrotic or immunomodulatory activity, plus a controlled trial or credible case series directly evaluating Vancomycin in scleroderma, before this candidate can advance beyond Hold
- **Note:** Among the 10 TxGNN-predicted indications reviewed for this drug, only *streptococcal pneumonia* (rank 9) reached L2 evidence with a "Proceed with Guardrails" recommendation, reflecting Vancomycin's established role against penicillin-resistant/MRSA-associated pneumonia. This represents a substantially more actionable signal than the top-ranked diffuse scleroderma prediction and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

