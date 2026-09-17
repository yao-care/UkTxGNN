---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From ACE Inhibitor Therapy to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Ramipril belongs to the ACE inhibitor (ACEI) class, typically used for hypertension and related cardiovascular/renal conditions (the specific licensed original indication is not recorded in this evidence pack). The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, but this prediction is currently supported by **no clinical trials** and **no published literature** — it rests on the knowledge-graph association alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap — see DG001/DG002); drug class is ACE inhibitor |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ramipril is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale attached to this prediction, ramipril is understood to act as an ACE inhibitor, and the theoretical link proposed is that RAAS (renin-angiotensin-aldosterone system) inhibition could influence pulmonary vascular tone.

However, this mechanistic link is explicitly flagged as weak in the pack's own rationale: there is no clinical or preclinical evidence supporting ACEI use in this specific condition, and the target disease itself is defined by an "unclear multifactorial mechanism" — meaning the underlying pathophysiology is not established. This makes it difficult to construct a credible causal pathway between the drug's known pharmacology and the proposed indication.

In short, this is a graph-derived association (TxGNN rank 1153 of its predictions for this drug) without corroborating clinical, trial, or literature evidence, and should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations were identified for ramipril in this evidence pack (market status: **Not Marketed**, 0 licences on record). This may reflect a data gap rather than confirmed absence from the UK market — verification against the current MHRA product register and BNF listing is recommended before any decision is finalised.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note on class-level safety signal:** While reviewing other TxGNN-predicted indications for this drug within the same evidence pack, one entry (malignant renovascular hypertension, rank 4) flags that bilateral renal artery stenosis / renovascular hypertension is a well-recognised contraindication or high-risk scenario for ACE inhibitors (risk of precipitating acute renal failure). This is not itself part of the predicted indication under review, but it is a relevant class-level caution worth carrying into any safety assessment of ramipril.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN knowledge-graph score (L5 evidence) with zero clinical trials and zero literature citations. The disease's own "unclear multifactorial mechanism" designation further weakens the plausibility of a specific causal link to ACEI pharmacology. Combined with a blocking data gap on TFDA/MHRA-equivalent warnings and contraindications (DG001) and an unconfirmed UK market status, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- SmPC/product warnings and contraindications data (currently blocking safety assessment — DG001)
- Confirmed mechanism of action documentation (DG002)
- Verification of current UK marketing authorisation status via MHRA register
- Any preclinical or mechanistic studies specifically linking ACE inhibition to this pulmonary hypertension subtype, should they emerge

**Additional note:** Within this same evidence pack, two other predicted indications for ramipril currently carry stronger evidence than this top-ranked one — intracerebral haemorrhage (rank 8, L4, animal-model evidence) and cerebral artery occlusion (rank 10, L3, one Phase 2 trial plus multiple mechanistic/animal studies, though with a noted negative finding for ramipril specifically versus candesartan). These may warrant evaluation ahead of the current top-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

