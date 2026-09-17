---
layout: default
title: Idebenone
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Idebenone
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

# Idebenone: From No UK-Licensed Indication to Hepatic Porphyria

## One-Sentence Summary

> No original indication or UK marketing authorisation is on record for Idebenone in this evidence pack; the drug is currently **not marketed** in the UK.
> The TxGNN model's top prediction is **Hepatic Porphyria** (score 99.92%),
> but this is a **model-only signal with zero supporting clinical trials or literature**, and the evidence pack itself flags the mechanistic link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available – no UK marketing authorisation or indication data on record |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is not populated for Idebenone in this evidence pack. However, the model's own mechanistic rationale notes that Idebenone is a synthetic analogue of coenzyme Q10 (CoQ10), acting on the mitochondrial electron transport chain and exhibiting antioxidant properties.

No original indication data is available, so a direct comparison between Idebenone's established use and hepatic porphyria cannot be made. Importantly, the evidence pack's own assessment of this prediction is explicitly cautious: hepatic porphyria's pathology centres on a deficiency in haem synthesis enzymes leading to accumulation of porphyrin precursors, a pathway with no established direct link to mitochondrial oxidative phosphorylation or antioxidant mechanisms. The mechanistic connection is therefore described as weak, and this prediction is presented as arising purely from TxGNN's topological (network-similarity) reasoning rather than from any known biological pathway overlap.

Nine further candidate indications are listed in the underlying dataset (e.g. idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, immune-mediated necrotizing myopathy), all scored at similarly high TxGNN confidence but all rated L5/Hold with no supporting trials or literature. Several of these (e.g. necrotizing myopathy, antisynthetase syndrome) have a somewhat more plausible mitochondrial/oxidative-stress rationale than the top-ranked hepatic porphyria prediction, but none currently have any empirical evidence base.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations are on record for Idebenone as of the data cutoff (2026-09-03). The drug's market status is recorded as **not marketed** in the UK, with zero licences held.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this evidence pack has a Blocking data gap on prescribing warnings/contraindications, meaning no formal safety pre-screening (S1) has been completed for Idebenone.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN topological score but is supported by zero clinical trials, zero literature, and no UK marketing history. The evidence pack itself rates the mechanistic plausibility for hepatic porphyria as weak, and a Blocking data gap on safety labelling (warnings/contraindications) means the candidate cannot yet enter formal safety pre-screening.

**To proceed, the following is needed:**
- MHRA/SmPC-sourced warnings and contraindications for Idebenone (resolves Blocking gap DG001)
- Confirmed mechanism of action data from DrugBank or equivalent source (resolves DG002)
- Preclinical or observational evidence linking Idebenone to haem/porphyrin metabolism specifically
- Reassessment of route of administration and dosing feasibility, since no UK licensed formulation currently exists
- Consideration of whether other candidates in this batch (e.g. immune-mediated necrotizing myopathy, antisynthetase syndrome) merit prioritisation given their comparatively stronger mitochondrial rationale, pending the same evidence-generation steps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

