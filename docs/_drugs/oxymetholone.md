---
layout: default
title: Oxymetholone
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 1
---

# Oxymetholone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Oxymetholone: From Unspecified Original Indication to Seborrhoeic Dermatitis

## One-Sentence Summary

> Oxymetholone is an anabolic-androgenic steroid; no original indication data is currently on record for this evidence pack.
> The TxGNN model predicts a possible association with **Seborrhoeic Dermatitis** (score 99.05%),
> but this is supported by **no clinical trials** and **no published literature**, and the underlying pharmacology points in the opposite direction to a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current data (no `original_indications` on file) |
| Predicted New Indication | Seborrhoeic Dermatitis |
| TxGNN Prediction Score | 99.05% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable? (Caution Advised)

Detailed mechanism of action data is not currently available in this evidence pack. Based on known pharmacological class information, Oxymetholone is an **anabolic-androgenic steroid (AAS)**.

Androgens are well established to stimulate sebaceous gland proliferation and increase sebum production — this is precisely the mechanism believed to *drive* seborrhoeic dermatitis and acne, not treat it. Clinically, acne and increased sebum production are recognised adverse effects of androgen therapy. This places the predicted indication in **direct mechanistic opposition** to a plausible therapeutic effect.

The high TxGNN score (99.05%) most likely reflects strong graph connectivity between "androgen" and "sebaceous gland/skin" nodes in the knowledge graph — a reflection of a well-documented *adverse* pharmacological relationship rather than a *therapeutic* one. This prediction should be treated as a **candidate false positive** pending mechanistic review, and is not, on current evidence, a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Oxymetholone does not currently hold a marketing authorisation and has a UK market status of **Not marketed**. No licence records are available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications and drug interaction data for Oxymetholone are not currently available in this evidence pack (flagged as a blocking data gap — see Conclusion).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) — no clinical trials or literature support this indication.
- The proposed mechanism runs **counter** to the biological direction expected for treating seborrhoeic dermatitis, raising strong suspicion of a false positive driven by knowledge-graph node connectivity rather than genuine therapeutic signal.
- A **blocking** data gap exists on TFDA/SmPC-equivalent warnings and contraindications, meaning this candidate cannot yet enter a formal safety pre-assessment (S1).

**To proceed, the following is needed:**
- Full prescribing information (warnings, contraindications) to close the blocking data gap before any safety pre-assessment can begin.
- Confirmed mechanism of action data from DrugBank or equivalent source.
- An independent mechanistic review to assess whether the TxGNN score reflects a genuine therapeutic hypothesis or a graph-connectivity artefact, before any further evidence collection is commissioned for this indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

