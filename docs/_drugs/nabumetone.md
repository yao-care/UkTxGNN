---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: From NSAID Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone is a non-steroidal anti-inflammatory drug (NSAID), with its class-level use in osteoarthritis (OA) and rheumatoid arthritis (RA) pain and inflammation management referenced within the evidence pack's own rationale texts (no formal original indication record was available in this dataset). The TxGNN model's top prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic assessment concludes there is no plausible pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded; NSAID class use in OA/RA pain and inflammation referenced in rationale evidence only |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% (rank 277 of all candidates) |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (original_moa: Data Gap). Based on known information, Nabumetone belongs to the NSAID class, with COX inhibition as its presumed pharmacological mechanism, referenced through its rationale linkage to OA/RA pain management in lower-ranked candidates within this evidence pack.

For the top-ranked candidate, however, the evidence pack's own mechanistic assessment explicitly states there is **no reasonable biological link**: Acromesomelic Dysplasia, Hunter-Thompson Type is caused by *NPR2* gene mutations, resulting in a growth-plate cartilage regulatory disorder. This is a non-inflammatory, structural skeletal dysplasia — it has no established relationship to the anti-inflammatory/analgesic mechanism of NSAIDs such as nabumetone.

This is a clear example of the TxGNN model producing a statistically high similarity score without corresponding biological plausibility, a known limitation of pure network-embedding-based repurposing scores when disconnected from mechanistic or clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Nabumetone is currently **not marketed** in the UK according to the source dataset, with no marketing authorisations recorded (total_licenses: 0). No product-level information is available for this candidate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acromesomelic Dysplasia, Hunter-Thompson Type) has no supporting clinical trials or literature (L5, Decision Stage S0), and the evidence pack's own mechanistic rationale explicitly rejects a plausible pharmacological connection between NSAID activity and this non-inflammatory genetic skeletal disorder.

**To proceed, the following is needed:**
- TFDA/MHRA product labelling — warnings, contraindications (currently Blocking data gap, DG001)
- Confirmed mechanism of action (MOA) data from DrugBank or SmPC (High priority data gap, DG002)
- If repurposing is still of interest for this drug, consider redirecting evaluation toward the **more mechanistically plausible lower-ranked candidates** in this evidence pack, which reached S1/Research Question status rather than Hold:
  - **Pseudoachondroplasia** (rank 7, L4) — NSAID commonly used for symptomatic joint pain in this population
  - **Spondyloarthropathy, susceptibility to** (rank 8, L4) — NSAIDs are a first-line class treatment for spondyloarthropathies
  - **Rheumatoid Nodulosis** (rank 10, L4) — an RA-spectrum condition where NSAID use is already established for the broader disease category
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

