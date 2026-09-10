---
layout: default
title: Imidapril
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 5
---

# Imidapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imidapril: From an Undocumented Original Indication to Pulmonary Hypertension (Unclear Multifactorial Mechanism)

## One-Sentence Summary

Imidapril's original indication and mechanism of action are not documented in the current evidence pack (flagged as data gaps). The TxGNN model predicts potential efficacy for **Pulmonary Hypertension with Unclear Multifactorial Mechanism**, but this prediction is currently supported by **no registered clinical trials** and **no published literature specific to this indication** — the only evidence is a computational model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (data gap — no licences or indication text available) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Imidapril in this evidence pack, and no original indication has been documented in the sources reviewed. Without a confirmed MOA or documented original indication, the mechanistic link between Imidapril and pulmonary hypertension cannot be independently verified from the data provided.

The evidence pack does flag this gap explicitly (DG002, High severity, DrugBank MOA query outstanding), which directly limits our ability to assess whether a plausible pharmacological rationale exists for this repurposing candidate. Until MOA data is retrieved, this prediction should be treated as a computational signal only, not a mechanistically substantiated hypothesis.

It is also worth noting that a lower-ranked candidate for this drug (Braddock syndrome, rank 5) was independently assessed within the evidence pack and flagged as a likely false-positive knowledge-graph association with no plausible mechanistic link — a useful reminder that TxGNN score alone, without corroborating mechanistic or clinical evidence, is not sufficient grounds for prioritisation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Imidapril is currently **not marketed** in the United Kingdom, and no marketing authorisations are recorded in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: A Blocking-severity data gap (DG001) has been identified — regulatory label warnings and contraindications have not yet been retrieved and reviewed. This must be resolved before any safety assessment (S1 stage) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pulmonary hypertension with unclear multifactorial mechanism) has no supporting clinical trials or literature, and the drug's mechanism of action and original indication are both unconfirmed data gaps. Combined with a Blocking-severity gap in regulatory safety data, there is currently insufficient evidence to move this candidate beyond initial screening.

**To proceed, the following is needed:**
- MOA confirmation via DrugBank API (DG002)
- Regulatory label warnings/contraindications retrieval from source agency (DG001, Blocking — required before any safety evaluation)
- Original indication and licensing history documentation
- Preclinical or clinical literature specific to pulmonary hypertension to substantiate the TxGNN signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

