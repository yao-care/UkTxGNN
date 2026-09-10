---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 5
---

# Metoclopramide
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

# Metoclopramide: From Nausea/Vomiting and GI Motility Disorders to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a dopamine D2‑receptor antagonist and prokinetic agent used internationally for nausea, vomiting and gastrointestinal motility disorders (no UK licence record is present in this evidence pack). The TxGNN model's top-ranked prediction suggests possible efficacy for **Gastric Ulcer**, but this specific candidate is currently supported by **no clinical trials and no literature**, so the finding is model-driven only and requires further scrutiny before any development action.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nausea, vomiting and gastrointestinal motility disorders (general pharmacological knowledge — no UK marketing authorisation data available in this evidence pack) |
| Predicted New Indication | Gastric Ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this product record is not available in the evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, metoclopramide is a dopamine D2‑receptor antagonist and gastroprokinetic agent: it accelerates gastric emptying and increases lower oesophageal sphincter tone. In theory this could reduce mucosal irritation from bile reflux or delayed gastric emptying, which provides a plausible — but indirect — mechanistic link to gastric ulcer.

However, gastric ulcer pathophysiology is predominantly driven by acid hypersecretion and *Helicobacter pylori* infection, and standard treatment relies on acid suppression (PPI/H2RA) and eradication therapy rather than motility modulation. The high TxGNN score most likely reflects proximity within the knowledge graph (e.g. shared "gastrointestinal tract" nodes) rather than a genuine, evidence-backed pharmacological effect. No clinical trial or published study in this evidence pack directly examines metoclopramide for gastric ulcer treatment or prevention.

It is worth noting that a lower-ranked prediction in the same evidence pack — **gastroduodenitis** (rank 2, score 99.90%) — is supported by 20 literature items describing metoclopramide's effects on antroduodenal motor coordination, reaching evidence level L4. This may represent a more mechanistically coherent research question than the top-ranked gastric ulcer prediction, though it too lacks controlled clinical trial data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No marketing authorisations are recorded for Metoclopramide in this evidence pack. Market status is listed as "Not marketed," with 0 total licences on file. UK-specific licence, product name, dosage form and approved indication text could not be extracted (TFDA/MHRA label data was flagged as a Blocking-severity data gap in the source evidence pack).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gastric Ulcer) has no supporting clinical trials or literature and evidence level L5 — this is a pure knowledge-graph association rather than a substantiated repurposing signal, and mechanistically it sits at odds with standard acid-suppression-based ulcer therapy.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or SmPC (currently a data gap)
- UK/TFDA label warnings, contraindications and product licence information (currently a Blocking data gap preventing safety pre-screening)
- Direct clinical or preclinical evidence testing metoclopramide specifically in gastric ulcer, rather than general GI motility studies
- Consider reprioritising evaluation toward **gastroduodenitis** (rank 2), which has a stronger literature base (20 publications, L4) around metoclopramide's effect on antroduodenal motor coordination, as a more promising research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

