---
layout: default
title: Alfentanil
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 1
---

# Alfentanil
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

# Alfentanil: From Opioid Anaesthesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Alfentanil is a potent, short-acting μ-opioid receptor agonist widely used as an intraoperative analgesic and anaesthetic adjunct. The TxGNN model assigns it a high prediction score (99.51%) for potential use in **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, yet detailed mechanistic analysis reveals a critical logical gap in the proposed pathway. There are **no supporting clinical trials** and **no supporting publications** for this indication, placing this candidate at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No authorisation data available in current dataset |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, alfentanil is a potent μ-opioid receptor (OPRM1) agonist with rapid onset and short duration of action, used clinically for intraoperative analgesia, conscious sedation, and as an anaesthetic supplement. Its well-characterised central nervous system activity forms the starting point for the proposed mechanistic chain.

The TxGNN model's reasoning appears to follow a four-step pathway: alfentanil's μ-opioid agonism → modulation of hypothalamic arginine vasopressin (AVP/ADH) release (supported by animal studies and limited observational human data, whereby opioids may suppress AVP secretion) → the known pathophysiology of NSIAD, caused by gain-of-function mutations in the AVPR2 (V2 vasopressin receptor) gene, leading to constitutive receptor activation, elevated cAMP, AQP2 membrane insertion, inappropriate water retention, and hyponatraemia.

However, there is a **critical mechanistic gap**: NSIAD is fundamentally caused by constitutive activation of the AVPR2 receptor, which is entirely independent of circulating AVP concentrations. Because the mutant receptor is "always on" regardless of ligand, any suppression of AVP secretion by alfentanil would be therapeutically irrelevant — it would be akin to turning off a tap that is no longer connected to the pipe. The high TxGNN score (0.9951) most likely reflects topological proximity in the knowledge graph between the opioid signalling axis, ADH pathways, and renal water metabolism nodes, rather than a genuine pharmacological relationship. This is a classic example of a **high-score, low-plausibility** outcome in graph-based prediction algorithms.

**Mechanistic plausibility: 1 out of 5 — extremely low**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No MHRA marketing authorisations for alfentanil are recorded in the current dataset. Clinicians should independently verify the current licensing status via the MHRA Product Licence Register and the BNF, as alfentanil preparations (e.g., Rapifen®, Janssen) may hold authorisations not captured in this evidence pack version.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The core pathological mechanism of NSIAD — constitutive AVPR2 receptor activation independent of AVP levels — renders opioid-mediated suppression of AVP secretion mechanistically irrelevant. With no supporting clinical trials, no published literature, and a mechanistic plausibility score of 1/5, there is currently no evidence base to justify further development of this candidate.

**To proceed, the following would be needed:**

- Formal MOA documentation from DrugBank or primary literature to confirm or refute any direct effect of alfentanil (or its metabolites) on AVPR2 or downstream cAMP/AQP2 signalling
- A revised mechanistic hypothesis that directly addresses constitutive AVPR2 activation — for example, evidence of alfentanil acting as a partial inverse agonist at AVPR2 or modulating downstream second-messenger pathways independently of AVP binding
- Preclinical data (in vitro cell models expressing gain-of-function AVPR2 mutations, or appropriate animal models) directly testing alfentanil in NSIAD-relevant systems
- MHRA SmPC review and a structured safety assessment before any exploratory study is considered
- Independent expert review by a clinical pharmacologist with expertise in renal water and sodium disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

