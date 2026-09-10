---
layout: default
title: Ethosuximide
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 1
---

# Ethosuximide
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

# Ethosuximide: From Absence Seizures to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ethosuximide is an anticonvulsant established for the treatment of absence seizures in epilepsy, acting via inhibition of thalamic T-type (Ca_v3) calcium channels.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
but this prediction is currently supported by **no clinical trials** and **no published literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence seizures (epilepsy) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ethosuximide's established mechanism of action is inhibition of T-type (Ca_v3) calcium channels in thalamic neurons, which reduces the abnormal neuronal firing underlying absence seizures. This is a well-characterised, neurone-specific electrophysiological effect.

NSIAD, in contrast, is caused by a gain-of-function mutation in the AVPR2 (vasopressin V2) receptor, which drives ADH-independent, constitutive activation of cAMP signalling and excessive water reabsorption in the renal collecting duct. This is a G-protein-coupled receptor/second-messenger pathway entirely distinct from voltage-gated neuronal calcium channels.

No known or indirect mechanistic link connects these two pathways, and no biological rationale currently supports repurposing ethosuximide for NSIAD. The high TxGNN score (99.91%) should therefore be interpreted as a knowledge-graph association rather than a pharmacologically validated hypothesis — it is not corroborated by any trial or literature evidence at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Ethosuximide currently holds no marketing authorisation on record and has a "not marketed" status; no UK product entries are available for this candidate indication.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for this indication, and no established mechanistic link between ethosuximide's known pharmacology and NSIAD pathophysiology. The evidence level (L5) reflects a model prediction only.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for ethosuximide (currently a data gap)
- UK/MHRA product labelling, warnings and contraindications (currently a data gap)
- Preclinical or mechanistic studies exploring any plausible link between T-type calcium channel modulation and AVPR2/cAMP signalling
- At minimum, case reports or observational data before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

