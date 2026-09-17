---
layout: default
title: L-Glutamine
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# L-Glutamine
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

Using the `Skill` tool wasn't needed here — this is a direct drug-repurposing report generation task matching the user's explicit formatting instructions, so I'll follow those directly.

# L-Glutamine: From Nutritional Supplementation to Drug-Induced Osteoporosis

## One-Sentence Summary

L-Glutamine is a non-essential amino acid conventionally used as a nutritional and immune-supportive agent; a specific original approved indication is not documented in this evidence pack. The TxGNN model predicts potential effectiveness for **Drug-Induced Osteoporosis** with a score of **99.98%**, but this is currently supported by **zero clinical trials and zero publications** — the pipeline's own mechanistic review flags this as a probable false positive rather than a genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` and `original_moa` are both unavailable) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for L-Glutamine in this evidence pack. Based on general pharmacological knowledge, L-glutamine's known actions relate to intestinal mucosal repair, immune modulation, and serving as a precursor for glutathione synthesis — none of which have an established link to osteoclast activity or bone remodelling pathways.

The evidence pack's own repurposing rationale is explicit on this point: *"No known mechanism: L-Glutamine acts mainly on mucosal repair, immune modulation and glutathione precursor synthesis, with no known connection to bone metabolism or osteoclast regulation pathways. The high TxGNN score may reflect knowledge-graph embedding similarity rather than a genuine biological mechanism."*

This is an important caveat: a high prediction score alone (99.98%) does not indicate biological plausibility. It most likely reflects structural similarity within the knowledge graph embedding space rather than a testable pharmacological hypothesis, and should not be treated as supportive evidence on its own.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No UK marketing authorisations are recorded for L-Glutamine in this evidence pack (`total_licenses = 0`). Market status is recorded as **Not marketed**. No product-level data (formulation, licence numbers, approved indication text) is currently available for review.

## Safety Considerations

No safety data (key warnings, contraindications, drug interactions) is currently available for L-Glutamine in this evidence pack. Notably, this is flagged in the underlying data as a **Blocking** gap (DG001 — MHRA/SmPC-equivalent warnings and contraindications), meaning even a preliminary safety screen (S1) cannot be completed until this is resolved.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (drug-induced osteoporosis) has no supporting clinical trials or literature (L5) and the pipeline's own mechanistic analysis identifies it as a likely embedding-similarity artefact rather than a biologically grounded hypothesis. Combined with a blocking gap in safety data, there is currently no basis to progress this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain MHRA/SmPC-equivalent warnings and contraindications for L-Glutamine
- Resolve DG002: obtain a confirmed mechanism of action (e.g. via DrugBank API)
- Obtain baseline data on L-Glutamine's original/current approved indication(s), which is currently missing entirely from this evidence pack

**Separate note for consideration:** among the ten candidates in this evidence pack, rank 3 (**dermatitis**) has a materially stronger evidence base than the top-ranked candidate — three RCTs (PMID 30753262, 28588793, 30587616) and a Phase NA completed trial (NCT03015077, n=59), reaching evidence level L2 with a "Research Question" recommendation. However, the evidence there is concentrated specifically in radiotherapy/chemotherapy-induced oral mucositis and dermatitis, not dermatitis broadly, and would need to be evaluated as its own narrower candidate rather than under the general "dermatitis" label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

