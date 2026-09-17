---
layout: default
title: Sulindac
parent: Model Prediction Only (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac: From NSAID Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Sulindac is a non-steroidal anti-inflammatory drug (NSAID); however, detailed original indication and mechanism-of-action data were not available in this Evidence Pack. The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal dysplasia, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale text flags the mechanistic link as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Sulindac is not currently marketed in the UK and no approved indication text was provided in the source data |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for Sulindac in this pack. Based on known pharmacology, Sulindac is a cyclooxygenase (COX)-inhibiting NSAID, traditionally used for pain and inflammation associated with musculoskeletal conditions such as osteoarthritis and rheumatoid arthritis.

The top-ranked predicted indication, Acromesomelic Dysplasia (Hunter-Thompson type), is a rare skeletal dysplasia caused by mutations in the *GDF5*/*CDMP1* gene affecting the bone morphogenetic protein (BMP) pathway. There is no known interaction between COX inhibition and BMP signalling, and the pack's own mechanistic-link narrative explicitly states this association is likely a statistical co-occurrence artefact of the knowledge-graph embedding, rather than a biologically grounded hypothesis. The same caveat applies to predictions ranked 2–8 (brachyolmia-related syndromes, myosclerosis, pseudoachondroplasia, brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, WHIM syndrome) — all are rare developmental or genetic disorders with no plausible link to NSAID pharmacology.

Two lower-ranked candidates merit note for context, though they were not the top-ranked prediction and are therefore not the primary focus of this report: **rheumatoid vasculitis** (rank 9, L4) has a plausible but weak indirect link via Sulindac's anti-inflammatory use in rheumatoid arthritis, and **hypermobility of coccyx** (rank 10, L4, decision stage S1, "Research Question") has the most coherent mechanistic rationale — NSAID-mediated prostaglandin suppression is a recognised approach to coccydynia pain management — though it still lacks any direct clinical or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Sulindac currently holds no marketing authorisation in the United Kingdom. The Evidence Pack records a UK market status of "not marketed" with zero total licences on file as of the data cutoff (17 September 2026).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** UK-specific product warnings and contraindications for Sulindac could not be retrieved for this Evidence Pack and are flagged as a **Blocking** data gap (DG001), which prevents this candidate from progressing to an initial safety assessment (Stage S1) regardless of the strength of the efficacy prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Acromesomelic Dysplasia, Hunter-Thompson Type) has no supporting clinical trials or literature, and the mechanistic rationale itself acknowledges a lack of biological plausibility. Combined with a blocking data gap on UK product safety information, this candidate cannot proceed past the earliest screening stage.

**To proceed, the following is needed:**
- MHRA/SmPC-sourced warnings, contraindications, and drug interaction data for Sulindac (currently blocking)
- Confirmed mechanism-of-action documentation from DrugBank or an equivalent source
- If pursued further, re-evaluation should prioritise the lower-ranked but mechanistically more coherent candidates — hypermobility of coccyx (coccydynia) and rheumatoid vasculitis — over the top-ranked rare skeletal dysplasia prediction
- Should any candidate advance, dedicated searches for relevant clinical trials and literature, as none are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

