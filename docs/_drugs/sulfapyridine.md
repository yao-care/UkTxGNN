---
layout: default
title: Sulfapyridine
parent: Model Prediction Only (L5)
nav_order: 543
evidence_level: L5
indication_count: 10
---

# Sulfapyridine
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

# Sulfapyridine: From No Recorded Original Indication to Heparin-Induced Thrombocytopenia

## One-Sentence Summary

No approved original indication is recorded for Sulfapyridine in this Evidence Pack; it is a sulfonamide-class antibacterial historically associated with dermatological and rheumatological use, but no UK marketing authorisation or licensed indication text is available. The TxGNN model's top prediction is **Heparin-Induced Thrombocytopenia**, but the accompanying mechanistic review indicates this high score more plausibly reflects a known drug-induced adverse-reaction pathway than a genuine therapeutic signal. There are currently **0 clinical trials** and **0 publications** supporting this direction, and the evidence level is the lowest tier (**L5, model prediction only**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licensed indication is recorded for Sulfapyridine |
| Predicted New Indication | Heparin-Induced Thrombocytopenia (disease) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Sulfapyridine is not available in this Evidence Pack (data gap DG002), and no original indication is on record, so the usual comparison between original and predicted indication cannot be made here.

More importantly, the mechanistic review included in the Evidence Pack raises a direct concern rather than support for this prediction: Sulfapyridine is a sulfonamide antibacterial, and sulfonamide drugs as a class are well documented in the safety literature as a cause of drug-induced immune thrombocytopenia. This means the TxGNN model's high score for Heparin-Induced Thrombocytopenia is more likely to be capturing a "drug → adverse reaction" edge embedded in the knowledge graph rather than a "drug → treatment" relationship. In other words, the model may be flagging a **risk signal**, not a **treatment opportunity**.

This pattern is not isolated to the top-ranked prediction. Reviewing the remaining top-10 candidates in this Evidence Pack shows the same issue repeatedly: acquired aplastic anaemia, autoimmune haemolytic anaemia and haemoglobinuria are all conditions that sulfonamide drugs — including Sulfapyridine — are known to be able to *cause*, particularly in patients with G6PD deficiency, rather than conditions Sulfapyridine would be expected to treat. The hereditary angioedema / C1-inhibitor deficiency and GPI-anchor-related predictions, by contrast, show no identifiable mechanistic link in either direction. Taken together, none of the top 10 predictions in this batch presents a mechanistically coherent repurposing hypothesis worth advancing at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Sulfapyridine is **not currently marketed** in the UK, and no marketing authorisations are recorded in this Evidence Pack (0 licences on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: This Evidence Pack flags a Blocking data gap (DG001) — TFDA/manufacturer label warnings and contraindications for Sulfapyridine are not yet available, which prevents a formal safety pre-assessment (S1 stage) at this time.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten top-ranked TxGNN predictions for Sulfapyridine are supported only by model output (L5), with zero clinical trials or publications. Mechanistic review further indicates that several of the highest-scoring predictions (heparin-induced thrombocytopenia, acquired aplastic anaemia, autoimmune haemolytic anaemia, haemoglobinuria) align with known sulfonamide-induced adverse reactions rather than plausible therapeutic mechanisms, suggesting these scores may reflect adverse-reaction edges in the knowledge graph rather than genuine repurposing opportunities. Combined with a Blocking gap in label/warning data, this candidate does not currently support progression.

**To proceed, the following is needed:**
- TFDA/manufacturer label warnings and contraindications (resolves Blocking gap DG001, required before any safety pre-assessment)
- Confirmed mechanism of action data (DG002)
- Confirmation of Sulfapyridine's original/historical approved indication(s), currently absent from this Evidence Pack
- A review of the TxGNN prediction pipeline for this candidate to distinguish genuine treatment edges from drug-induced adverse-reaction edges in the underlying knowledge graph before any of the top-10 predictions are considered further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

