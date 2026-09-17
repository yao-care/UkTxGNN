---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Teriparatide (recombinant human parathyroid hormone 1-34) is an osteoanabolic agent used to treat osteoporosis by stimulating osteoblast activity.
The TxGNN model predicts it may be effective for **Duodenal Ulcer**, but this candidate currently has **no supporting clinical trials and no supporting literature**, and the accompanying mechanistic rationale in this evidence pack explicitly flags it as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (pharmacological indication referenced throughout this evidence pack; no formal UK regulatory record is on file) |
| Predicted New Indication | Duodenal Ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this candidate (data gap). Based on the information available, teriparatide is a recombinant PTH(1-34) analogue that acts as an osteoanabolic agent by activating the PTH1 receptor on osteoblasts, promoting bone formation. It is established for use in osteoporosis and related bone-fragility conditions.

There is no known mechanistic link between PTH1R-mediated osteoanabolic signalling and the mucosal protection or acid-related pathology underlying duodenal ulcer disease. The evidence pack's own rationale for this candidate states directly that no biological plausibility has been identified, and this is corroborated by the complete absence of clinical trials or published literature for this drug-disease pairing. This combination of a high statistical TxGNN score with zero corroborating evidence and no mechanistic basis is a recognised pattern in embedding-based repurposing models — a high score alone does not indicate a genuine therapeutic signal.

It is worth noting that this evidence pack also contains a considerably stronger candidate further down the ranked list: **pregnancy and lactation-associated osteoporosis (rank 8)**, which shares teriparatide's core mechanism (correcting insufficient osteoblast activity) and is supported by cohort studies, case series and documented off-label clinical use. Reviewers may wish to prioritise that candidate over the top-ranked but mechanistically unsupported duodenal ulcer prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

No UK marketing authorisation is currently on file for teriparatide in the regulatory dataset used for this evidence pack (market status: Not marketed; total licences: 0). Prescribers and reviewers should verify current UK availability directly against the MHRA products database and the BNF, as this evidence pack's regulatory data may not reflect real-time licensing status.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenal ulcer prediction has a high TxGNN score but is supported by no clinical trials, no published literature, and no plausible mechanistic link — the evidence pack's own analysis identifies it as a statistically high-confidence but biologically implausible prediction. This does not meet the threshold to advance beyond an initial screening stage.

**To proceed, the following is needed:**
- MHRA-approved SmPC warnings, precautions and contraindications for teriparatide, currently missing from this evidence pack (Blocking data gap)
- Confirmed mechanism of action data from DrugBank, currently missing (High-severity data gap)
- Any preclinical or mechanistic hypothesis specifically linking PTH signalling to gastroduodenal mucosal pathology, should this candidate be pursued further
- Consideration of re-scoping this repurposing evaluation toward **pregnancy and lactation-associated osteoporosis**, which shows substantially stronger evidence (Evidence Level L3, multiple cohort studies and reviews, and documented off-label clinical precedent) within the same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

