---
layout: default
title: Inositol Nicotinate
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Inositol Nicotinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Inositol Nicotinate: From No Recorded Indication to Vitamin Deficiency Disorder

## One-Sentence Summary

> Inositol nicotinate is a niacin (vitamin B3) ester with no recorded original indication or UK marketing authorisation in this evidence pack.
> The TxGNN model predicts a possible link to **Vitamin Deficiency Disorder**,
> but this is currently supported by **0 clinical trials** and **0 publications** — a prediction based on knowledge-graph inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation or indication history on record |
| Predicted New Indication | Vitamin deficiency disorder |
| TxGNN Prediction Score | 99.96% (rank 824) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for inositol nicotinate. Based on known chemistry, it is an ester of nicotinic acid (niacin, vitamin B3) and inositol, which hydrolyses to release both compounds. This structural composition provides a molecular-level rationale for a link to vitamin deficiency disorders — but this is a **compositional relationship, not validated pharmacological evidence**.

No original indication is recorded in this evidence pack, and the TxGNN score for "vitamin deficiency disorder" (and closely related "biotin metabolic disease") most likely reflects proximity of vitamin/metabolite nodes in the knowledge graph rather than a demonstrated therapeutic effect. Several other top-ranked predictions for this drug (e.g. non-syndromic esophageal malformation, several unrelated hepatic-vascular conditions sharing an identical score of 0.9962) show no plausible biological mechanism and are likely artefacts of node clustering in the graph — this pattern further underscores that the model output alone cannot be treated as clinical evidence for any of the ranked indications, including the top one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Inositol nicotinate is **not marketed** in the United Kingdom, and no marketing authorisations are on record. No product name, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: warnings, contraindications and drug interaction data are currently unrecorded (flagged as a **blocking** data gap — DG001), meaning no formal safety review has been possible for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a TxGNN model score with no supporting clinical trials or literature (L5), and two data gaps — one blocking (missing safety/contraindication data, DG001) and one high-severity (missing mechanism of action, DG002) — prevent any meaningful safety or mechanistic assessment. The drug also has no UK marketing authorisation, and several co-ranked predictions for this candidate show implausible mechanisms, suggesting the underlying knowledge-graph signal may be noisy rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- SmPC-equivalent warnings and contraindications (DG001, blocking) — required before any S1 safety evaluation
- Confirmed mechanism of action data from DrugBank or equivalent source (DG002)
- Original indication and regulatory history, to establish similarity/rationale for the predicted new use
- At least preclinical or observational evidence for the vitamin deficiency disorder link, to move beyond L5
- Clarification of UK availability/import status given zero current marketing authorisations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

