---
layout: default
title: Mazindol
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 7
---

# Mazindol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mazindol: Original Indication Not Recorded — Predicted New Indication of Hypervitaminosis (Low Confidence)

## One-Sentence Summary

> The available evidence pack does not record Mazindol's original licensed indication or mechanism of action.
> The TxGNN model's top-ranked prediction is **Hypervitaminosis**, but this candidate has **0 clinical trials** and **0 publications** supporting it,
> and the model's own mechanistic rationale explicitly flags the association as likely **knowledge graph noise** rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Mazindol is not currently available in this evidence pack (flagged as a blocking data gap), which prevents a full assessment of pharmacological plausibility.

More importantly, the model-generated rationale for this specific prediction states there is **no identifiable pharmacological link** between Mazindol's sympathomimetic/appetite-suppressant activity and the metabolic mechanisms underlying hypervitaminosis. The rationale concludes this is most likely a **spurious association arising from node-embedding similarity** in the knowledge graph, rather than a genuine repurposing hypothesis.

The same pattern holds across nearly all of the top-ranked predictions in this pack: proximal 16p11.2 microdeletion syndrome, obsolete hypertelorism, frontorhiny, pentosuria, and lethal polymalformative syndrome (Boissel type) are all structural, congenital, or benign conditions with no plausible pharmacological mechanism connecting them to Mazindol, and each is explicitly annotated by the model as likely graph noise. One candidate — postural orthostatic tachycardia syndrome (rank 5) — has not yet completed rationale review and remains pending; it may warrant separate evaluation once assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Mazindol currently holds no marketing authorisations and is not marketed. No licence records are available for review.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Mechanism of action and MHRA-equivalent warning/contraindication data are recorded as a blocking data gap (DG001, DG002) and could not be assessed for this report.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction is unsupported by any clinical trial or literature evidence, sits at evidence level L5, and is explicitly flagged by the model's own mechanistic rationale as a likely knowledge-graph artefact rather than a genuine repurposing signal. A blocking data gap in safety/labelling information also prevents any S1 safety screening.

**To proceed, the following is needed:**
- Mechanism of action data for Mazindol (DrugBank query, per DG002)
- SmPC-equivalent warnings, contraindications and DDI data (per DG001, blocking)
- Independent literature/mechanistic review of the pending candidate (postural orthostatic tachycardia syndrome, rank 5) before any further action
- Re-evaluation of the knowledge graph edges driving ranks 1–4, 6–7, given the consistent "likely noise" annotation across candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

