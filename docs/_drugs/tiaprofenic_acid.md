---
layout: default
title: Tiaprofenic Acid
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Tiaprofenic Acid
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

# Tiaprofenic Acid: From NSAID Therapy to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Tiaprofenic acid is a propionic acid-class NSAID (COX-1/2 inhibitor); its detailed original indication and mechanism-of-action data are not available in this Evidence Pack. The TxGNN model's top-ranked prediction is **Brachydactyly-Syndactyly Syndrome**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale explicitly states there is no known mechanistic link between NSAID/COX inhibition and this congenital skeletal disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap); drug is classified as a propionic acid-class NSAID (COX-1/2 inhibitor) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.99% (rank 289 among all candidates) |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tiaprofenic acid is not currently available in this Evidence Pack (flagged as a High-severity data gap). Based on the information that is present, tiaprofenic acid belongs to the propionic acid class of NSAIDs, working through COX-1/COX-2 inhibition to reduce prostaglandin synthesis — a mechanism typically applied to pain and inflammatory musculoskeletal conditions.

Brachydactyly-syndactyly syndrome, however, is a congenital limb-development disorder driven by genetic developmental defects, not by inflammatory or prostaglandin-mediated pathology. The Evidence Pack's own repurposing rationale is explicit on this point: it states there is **no known association** between COX inhibition/prostaglandin pathways and this syndrome's underlying biology, and attributes the high TxGNN score to an embedding-level similarity signal rather than a genuine mechanistic connection. On this basis, the top-ranked prediction should be treated as a model artefact rather than a credible repurposing hypothesis.

Of the ten candidates in this Evidence Pack, the most mechanistically defensible is ranked 6th — **spondyloarthropathy, susceptibility to** (evidence level L4, decision stage S1, recommendation "Research Question"). NSAIDs, including propionic acid derivatives, are an established first-line symptomatic class-effect treatment for spondyloarthropathies such as ankylosing spondylitis. However, this candidate is flagged as "susceptibility to" the disease rather than the disease itself, and no tiaprofenic acid-specific trial or literature evidence exists — the support is class-level inference only, not drug-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Tiaprofenic acid currently holds **no UK marketing authorisations** (0 licenses recorded) and is classified as **not marketed** in this dataset. No product, dosage form, or approved indication information is available.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this Evidence Pack marks TFDA/MHRA-equivalent label warnings and contraindications as a **Blocking** data gap, meaning a preliminary safety assessment (S1) cannot currently be completed for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (brachydactyly-syndactyly syndrome) is supported only by an L5 model score with no clinical trials, no literature, and an explicit statement in the model's own rationale that no plausible mechanistic link exists.
- Core safety data (label warnings, contraindications) are marked as a Blocking gap, and mechanism-of-action data is a High-severity gap — together these prevent even an initial (S1) safety review.
- The drug is not currently marketed in the UK (0 marketing authorisations), removing any regulatory or real-world usage signal that could support repurposing.

**To proceed, the following is needed:**
- Original indication and mechanism-of-action data for tiaprofenic acid (from DrugBank/SmPC)
- MHRA/SmPC label warnings and contraindications (currently a blocking gap)
- If pursuing a repurposing hypothesis at all, prioritise the mechanistically plausible spondyloarthropathy-susceptibility candidate (rank 6) over the top-ranked but mechanistically unsupported prediction, and seek drug-specific (not class-level) clinical or literature evidence before advancing past S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

