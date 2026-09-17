---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 271
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Finasteride: From Androgen-Dependent Conditions to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5α-reductase inhibitor generally used for androgen-dependent conditions such as benign prostatic hyperplasia and androgenetic alopecia (the evidence pack itself does not record a specific original indication or MOA). The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as lacking a plausible mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack (`original_indications` empty; commonly known indications include BPH and androgenetic alopecia) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, finasteride inhibits 5α-reductase, reducing conversion of testosterone to dihydrotestosterone (DHT), and is used clinically where androgen-dependent tissue growth is the target (e.g. prostate enlargement, male pattern hair loss).

Ambras type hypertrichosis universalis congenita, however, is a congenital condition linked to chromosomal rearrangement near 8q22, causing diffuse lanugo-type hair overgrowth that is **not androgen-dependent**. The evidence pack's own rationale states there is "no reasonable connection" between this disease mechanism and finasteride's DHT-suppression pathway, with zero supporting trials or literature. This prediction should be treated as a likely knowledge-graph embedding artefact rather than a biologically grounded hypothesis.

For context, the model's next-ranked candidate, "hypertrichosis (disease)" (rank 2, L4), has some supporting literature, but the mechanistic direction is actually opposite to finasteride's known clinical effect (finasteride reduces androgen-dependent hair growth rather than promoting generalised hypertrichosis). Lower-ranked candidates (Dandy-Walker-associated syndrome, isolated hair shaft abnormality, familial trichomegaly, and a periodontal malformation syndrome) are similarly unsupported by trial or literature evidence and were assessed by the pipeline as likely noise. None of the six predicted indications in this pack currently reach a level of evidence suitable to progress beyond hypothesis-generation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Finasteride currently has no recorded UK marketing authorisations in this evidence pack (market status: Not Marketed; 0 licences on file). No product-level authorisation data is available to tabulate.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis universalis congenita) has zero clinical trials, zero literature, and no plausible mechanistic link to finasteride's known pharmacology — this is an L5, model-only signal. None of the other five predicted indications in this pack reach a stronger evidence tier either.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for finasteride (currently a data gap)
- MHRA/SmPC warnings and contraindications data to support an initial safety screen (currently blocking, per data gap DG001)
- A biologically plausible mechanistic hypothesis linking finasteride to any of the predicted indications before further investment in evidence collection
- If pursuing the hypertrichosis-adjacent signal (rank 2) instead, targeted trial/literature search specifically evaluating finasteride's effect on non-androgen-dependent hair growth
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

