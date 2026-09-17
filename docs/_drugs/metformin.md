---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 368
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metformin: From Undocumented Indication to Classic Stiff Person Syndrome

## One-Sentence Summary

This evidence pack does not include documented original indications or mechanism of action data for Metformin, and the drug is currently **not marketed in the UK** according to this dataset. The TxGNN model's top prediction is **Classic Stiff Person Syndrome**, but this signal is supported by **0 clinical trials** and **0 publications** — it is a purely computational (knowledge-graph) association with no corroborating clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Metformin in this evidence pack, so a full pharmacological rationale cannot be constructed here.

Based on the model's own rationale, the association is weak: Classic Stiff Person Syndrome is an autoimmune neurological condition mediated by anti-GAD65 antibodies causing GABAergic transmission dysfunction. This has no established biological connection to Metformin's commonly cited mechanisms (AMPK activation, mitochondrial complex I inhibition). The high TxGNN score (99.45%) reflects graph co-occurrence patterns within the knowledge graph rather than a validated pharmacological pathway, and the model's rank (5,380th overall) also indicates this is a low-confidence tail prediction rather than a strong signal.

It is also worth noting that the other four candidates in this evidence pack show similarly weak or even concerning patterns — one candidate (thiamine-responsive dysfunction syndrome) is a mitochondrial/metabolic disorder where Metformin's complex I inhibition could theoretically worsen lactic acidosis risk, suggesting a potential contraindication direction rather than therapeutic benefit. None of the five predictions has any supporting clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations are recorded for Metformin in this dataset (market status: **not marketed**, 0 licenses on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Note:** This evidence pack flags a **blocking data gap** (DG001) — MHRA/manufacturer label warnings and contraindications are not yet available for this candidate, which prevents a full S1 safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is evidence level L5 (model prediction only) with no clinical trials or literature support, and the proposed mechanistic link is not biologically well-founded. A blocking data gap (missing regulatory safety label data) also prevents progression to a formal safety assessment at this stage.

**To proceed, the following is needed:**
- MHRA-equivalent SmPC/label data — warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action data (DrugBank query, DG002)
- Documented original indication(s) and current global regulatory status for Metformin
- Preclinical or case-level evidence establishing a plausible biological link to stiff person syndrome spectrum disorders before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

