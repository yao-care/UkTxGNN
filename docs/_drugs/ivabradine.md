---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ivabradine: From an Unspecified Original Indication to Hypertrichosis

## One-Sentence Summary

> The original indication and mechanism of action for Ivabradine are not documented in the current evidence pack, and the drug holds no UK marketing authorisation.
> The TxGNN model predicts a possible link to **Hypertrichosis**, but this prediction is supported by **no clinical trials** and **no literature**,
> and the model's own rationale flags it as a likely **statistical artefact** rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (data gap) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ivabradine in this evidence pack, and no original indication has been recorded, so a direct pharmacological comparison between the original and predicted indications cannot be made from the supplied data.

Based on general pharmacology, Ivabradine is understood as a selective HCN4/If channel inhibitor acting on the sinoatrial node to lower heart rate. The evidence pack's own repurposing rationale explicitly states that this mechanism has **no known overlap** with hair follicle growth regulation, and further notes that hypertrichosis is a rare-disease ontology node with low connectivity in the knowledge graph — a known source of spurious high-confidence scores ("model artefact") in TxGNN. The same caveat applies to the other five ranked predictions in this pack (Ambras-type hypertrichosis, a periodontal malformation syndrome, Dandy-Walker malformation syndrome, an isolated hair-shaft disorder, and nephrogenic syndrome of inappropriate antidiuresis): all score above 99% yet none have any mechanistic, clinical, or literature support, and all carry a Hold recommendation.

In short, the high TxGNN score alone is **not** sufficient grounds to consider this prediction pharmacologically plausible without independent corroborating evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: 20 PubMed records were retrieved for a lower-ranked candidate, "malformation syndrome with odontal/periodontal component" — but on review, all are general periodontal pathophysiology/treatment-guideline papers with no mention of Ivabradine or If-channel biology. This reflects background literature attached via a broad disease-ontology match rather than drug-specific evidence, and does not support that repurposing hypothesis either.)*

---

## UK Market Information

Ivabradine currently holds no UK marketing authorisation and is not marketed in the UK according to this evidence pack (0 licences on record). No product, dosage form, or approved-indication data is therefore available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications, and drug interaction data were not available in this evidence pack.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on an L5 TxGNN score with no supporting clinical trials, no literature, no confirmed mechanism of action, and no original indication on record. The evidence pack's own analysis identifies the prediction as a probable model artefact arising from a low-connectivity rare-disease node, not a credible biological hypothesis.

**To proceed, the following is needed:**
- Original indication and mechanism of action for Ivabradine (e.g. via DrugBank/SmPC lookup)
- SmPC-derived warnings, contraindications, and drug interaction data (currently a blocking data gap for safety screening)
- Independent mechanistic rationale linking If-channel inhibition to hair follicle biology, if one exists
- Any real-world, case-report, or preclinical evidence specific to Ivabradine and hypertrichosis before this candidate is reconsidered for advancement beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

