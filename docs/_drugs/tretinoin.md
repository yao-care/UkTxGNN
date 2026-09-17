---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Acne / Acute Promyelocytic Leukaemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (DrugBank ID DB00755) is internationally known and used for acne vulgaris (topical) and acute promyelocytic leukaemia (oral, as all-*trans* retinoic acid), although no UK marketing authorisation is recorded in this evidence pack. The TxGNN model predicts a possible link to **Rheumatoid Nodulosis**, with a graph-association score of **99.84%**, but currently **no clinical trials** and **no published literature** support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no UK licence on file); internationally, tretinoin is indicated for acne vulgaris and acute promyelocytic leukaemia |
| Predicted New Indication | Rheumatoid Nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the repurposing rationale note accompanying this prediction, tretinoin is understood to act as a **retinoic acid receptor (RAR/RXR) agonist**, the same receptor family responsible for its known effects on cell differentiation in dermatology and haemato-oncology.

Rheumatoid nodulosis is a rare nodular variant within the rheumatoid disease spectrum, mechanistically distant from tretinoin's established uses in keratinocyte differentiation (acne) and promyelocyte maturation (APL). No overlapping pathway, shared target, or comorbidity rationale is documented in the evidence pack linking retinoid signalling to this condition.

The evidence pack's own assessment is explicit on this point: the high TxGNN score reflects a graph-embedding association only, with no literature or trial data available to corroborate a plausible mechanistic connection. As such, the biological rationale for this specific prediction cannot currently be evaluated and should be treated as speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No UK marketing authorisations are currently on record for Tretinoin in this evidence pack (market status: Not marketed; total licences: 0).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Detailed MHRA warnings, contraindications, and drug interaction data for Tretinoin were not available at the time of this evaluation (data cutoff 2026-09-17) and are flagged as a blocking data gap requiring resolution before any safety-related decision-making.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN graph-embedding score (L5, no clinical or literature evidence), and the underlying mechanistic plausibility between retinoid signalling and rheumatoid nodulosis cannot currently be assessed. Combined with the absence of confirmed UK safety data (warnings, contraindications, DDI), this candidate does not meet the threshold for further evaluation at this time.

**To proceed, the following is needed:**
- Resolution of the blocking safety data gap (MHRA/SmPC warnings and contraindications for Tretinoin)
- Confirmation of the drug's mechanism of action from a primary source (e.g., DrugBank API)
- At least preclinical or case-level evidence establishing a mechanistic link between retinoid signalling and rheumatoid nodulosis before advancing beyond S0
- Consideration of re-ranking against other candidates in this evidence pack with stronger evidence bases (e.g., osteoarthritis, rank 7, 20 literature citations, though with conflicting directionality; folliculitis decalvans, rank 10, flagged as "Research Question") — these may warrant separate, dedicated evaluation ahead of rheumatoid nodulosis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

