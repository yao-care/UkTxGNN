---
layout: default
title: Sulfinpyrazone
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Sulfinpyrazone
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

# Sulfinpyrazone: From Gout to Renal Hypouricemia

## One-Sentence Summary

> Sulfinpyrazone is a uricosuric agent historically used in the management of gout and hyperuricemia, though no formal original-indication or UK licensing data is recorded in this evidence pack.
> The TxGNN model's top-ranked prediction is **Renal Hypouricemia**, but the evidence pack's own mechanistic rationale flags this as a likely opposite-direction, low-plausibility signal.
> No clinical trials or literature currently support this specific prediction, and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no licences on file). Based on internal rationale notes, Sulfinpyrazone is historically a uricosuric agent used in gout treatment |
| Predicted New Indication | Renal Hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for Sulfinpyrazone in this evidence pack. However, the pack's own rationale notes describe Sulfinpyrazone as a uricosuric agent that inhibits renal tubular reabsorption of uric acid — a mechanism that **promotes** uric acid excretion and lowers serum urate.

The top-ranked predicted indication, Renal Hypouricemia, is a condition of pathologically *low* urate caused by *excessive* renal urate excretion. This is pharmacologically the opposite direction to Sulfinpyrazone's known uricosuric effect: giving a drug that further promotes urate excretion to a patient who already excretes too much urate has no plausible therapeutic rationale. The evidence pack's own annotation for this prediction explicitly flags it as a likely artefact of TxGNN's disease-embedding similarity rather than a genuine mechanistic signal, and no clinical trials or literature exist to support it.

By contrast, other candidates further down the ranked list in this pack show more plausible mechanistic direction — notably rank 3, Lesch-Nyhan syndrome (complete HGPRT deficiency causing severe hyperuricemia and gouty arthritis/nephropathy), where a uricosuric mechanism is directionally consistent with disease pathophysiology and is supported by a single review-level PubMed citation (evidence level L4). This candidate is not the subject of the current report title but is noted here for transparency, as it appears to be mechanistically better supported within the same evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No MHRA marketing authorisations are recorded for Sulfinpyrazone in this evidence pack (total licences: 0; market status: Not marketed).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Renal Hypouricemia) is directionally inconsistent with Sulfinpyrazone's known uricosuric mechanism, is unsupported by any clinical trial or literature evidence (Evidence Level L5, decision stage S0), and the evidence pack itself flags it as a probable false-positive prediction rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Product label warnings and contraindications from the relevant regulatory source (flagged as a **Blocking** data gap — required before any safety pre-assessment can proceed)
- Confirmed mechanism of action (MOA) data (flagged as a **High**-severity data gap)
- UK marketing authorisation and licensing status verification
- If pursuing repurposing further, re-evaluation should focus on the mechanistically consistent candidate identified within this pack (Lesch-Nyhan syndrome, rank 3, L4), including a targeted literature search rather than the current top-ranked, mechanistically inconsistent prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

