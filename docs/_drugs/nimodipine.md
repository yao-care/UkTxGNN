---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 2
---

# Nimodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nimodipine: From Subarachnoid Haemorrhage-Associated Cerebral Vasospasm to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Nimodipine is a dihydropyridine calcium channel blocker originally used to prevent cerebral vasospasm following aneurysmal subarachnoid haemorrhage. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolaemia**, but currently **no clinical trials** and **no published literature** support this direction, and the underlying mechanistic rationale is assessed as weak even within the evidence pack itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of cerebral vasospasm following aneurysmal subarachnoid haemorrhage (drawn from the evidence pack's mechanistic notes; no UK licence data is available to confirm this) |
| Predicted New Indication | Homozygous Familial Hypercholesterolaemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nimodipine is not available (flagged as a data gap at source). Based on known clinical use, nimodipine is a dihydropyridine-class calcium channel blocker that acts on L-type calcium channels in vascular smooth muscle, with established efficacy in preventing cerebral vasospasm after subarachnoid haemorrhage.

Homozygous familial hypercholesterolaemia (HoFH) is caused by loss-of-function mutations in the LDL receptor (LDLR), leading to impaired clearance of LDL cholesterol. This pathway has no established direct or indirect connection to calcium channel signalling. The evidence pack's own mechanistic assessment explicitly concludes that biological plausibility for this link is weak — the prediction appears to derive solely from similarity in the TxGNN knowledge-graph embedding space, rather than from any validated pharmacological relationship.

Given the absence of original MOA data, the lack of any supporting trials or literature, and the model's own acknowledgement of poor mechanistic grounding, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Nimodipine currently holds no marketing authorisation in the United Kingdom for the products captured in this evidence pack (0 licences registered). No MHRA licence data or approved indication text is available to reference at this time.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications, and drug interaction data for this candidate are currently unavailable — this is flagged as a Blocking data gap and must be resolved before any safety evaluation can proceed.)*

---

## Additional Predicted Indication (Lower Confidence)

A second, lower-ranked prediction was also generated: **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)** (TxGNN score 99.05%, rank 7812, Evidence Level L5, no supporting trials or literature). NSIAD results from gain-of-function mutations in the V2 vasopressin receptor (AVPR2), acting via the Gs–cAMP–PKA pathway. While theoretical crosstalk between calcium signalling and cAMP pathways exists, no preclinical or clinical evidence supports nimodipine's efficacy here either. This candidate carries the same "Hold" recommendation for the same reasons as the primary prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions are model-derived only (L5), with no clinical trials, no published literature, and an explicitly weak mechanistic rationale. Nimodipine is also not currently marketed in the UK, and critical safety data (SmPC warnings, contraindications, DDIs) are missing — a Blocking gap that alone prevents progression to safety evaluation.

**To proceed, the following is needed:**
- Confirmed original mechanism of action (MOA) data for nimodipine
- SmPC-derived warnings, contraindications, and drug interaction data (currently a Blocking data gap)
- Any preclinical or in vitro evidence specifically linking calcium channel blockade to LDLR function (HoFH) or AVPR2 signalling (NSIAD)
- Reassessment once independent trial or literature evidence emerges for either indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

