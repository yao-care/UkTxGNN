---
layout: default
title: Dornase Alfa
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
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

# Dornase alfa: From Cystic Fibrosis to Fryns Smeets Thiry Syndrome

## One-Sentence Summary

Dornase alfa is a recombinant human DNase I originally used to reduce mucus viscosity in cystic fibrosis. The TxGNN model's top-ranked candidate for this drug is **Fryns Smeets Thiry syndrome**, but the prediction score is only **50%** (effectively a coin-flip, indistinguishable from noise), and there are **no clinical trials and no literature** supporting this or any of the other nine candidates generated for this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (per mechanistic notes in this evidence pack; no formal UK licence record was supplied) |
| Predicted New Indication | Fryns Smeets Thiry syndrome |
| TxGNN Prediction Score | 50.0% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dornase alfa is a recombinant human DNase I enzyme. Its established mechanism is enzymatic cleavage of extracellular DNA in respiratory mucus/sputum, which reduces sputum viscosity and improves airway clearance — this is why it is used in cystic fibrosis.

For this candidate, the mechanistic case does **not** hold up. Fryns Smeets Thiry syndrome is a rare multi-system congenital malformation syndrome with no known relationship to extracellular DNA burden or mucus viscosity. The evidence pack's own rationale for this pairing explicitly flags the TxGNN score of 0.5 as "near-zero discriminative power" and attributes the association to knowledge-graph embedding noise rather than a genuine biological signal.

This pattern is not limited to the top candidate: all ten predicted indications returned for dornase alfa carry an identical score of 0.5 and sit at very low rank (~998,000+ out of the full candidate list), spanning entirely unrelated categories — rare congenital syndromes, a rickettsial infection, central and peripheral neurological conditions, and an endocrine disorder. None share a plausible mechanistic link to DNase I activity. This is consistent with the model producing no usable signal for this drug rather than identifying a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No marketing authorisation records were supplied for this evidence pack (market status: not marketed; total licences: 0). No MHRA marketing authorisation or NICE appraisal data is available to reference at this time.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score (50%) sits at the model's noise floor, and all ten candidate indications for this drug show the same negligible score with no supporting clinical trials or literature — this points to an absence of real signal rather than an under-evidenced but plausible lead. Combined with the absence of any UK marketing authorisation, this candidate does not warrant further evaluation as currently framed.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data via the DrugBank API (currently a **High**-severity gap, DG002)
- TFDA/MHRA SmPC warnings, contraindications and DDI data (currently a **Blocking**-severity gap, DG001) before any safety pre-screen (S1) can begin
- If dornase alfa is to be re-evaluated, re-run the TxGNN prediction with a higher score threshold, since the current top-10 list for this drug does not contain a mechanistically credible candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

