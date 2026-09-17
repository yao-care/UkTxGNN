---
layout: default
title: Raloxifene
parent: Model Prediction Only (L5)
nav_order: 494
evidence_level: L5
indication_count: 4
---

# Raloxifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Raloxifene: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM) best known for the treatment and prevention of postmenopausal osteoporosis. The TxGNN model predicts a possible new use in **Duodenal Ulcer**, but this signal is currently supported by **no clinical trials** and **no published literature** — it rests entirely on knowledge-graph inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (postmenopausal) — based on established pharmacology; not captured as structured data in this evidence pack |
| Predicted New Indication | Duodenal Ulcer |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, raloxifene is a SERM that acts primarily on oestrogen receptors in bone and breast tissue, and its efficacy in postmenopausal osteoporosis is well established.

The link between SERM activity and duodenal ulcer is weak. Some animal-model literature suggests oestrogen may have a mucosa-protective effect in the stomach and duodenum, but there is no direct mechanistic or clinical evidence connecting raloxifene specifically to ulcer healing or prevention. This prediction should be treated as a knowledge-graph association rather than a pharmacologically grounded hypothesis.

Of the four candidates in this evidence pack, the **hypoalphalipoproteinemia** signal (rank 2) has somewhat stronger mechanistic plausibility — raloxifene has been observed to lower LDL cholesterol as a secondary effect in osteoporosis trials (e.g. the MORE trial) — though this too lacks any direct supporting trial or literature evidence here.

### Other TxGNN-Predicted Candidates (Same Evidence Pack)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|----------------------|-------------|-----------------|------|
| 2 | Hypoalphalipoproteinemia | 99.65% | L5 | Plausible via known lipid-lowering side effect, but unproven |
| 3 | Duodenal Obstruction | 99.64% | L5 | Structural/mechanical condition; no biological rationale for SERM involvement — likely spurious association |
| 4 | Duodenogastric Reflux | 99.59% | L5 | Weak theoretical link via GI motility; no supporting evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Raloxifene currently holds no recorded marketing authorisation in this evidence pack (0 licences; market status: Not Marketed). No product, dosage form, or approved-indication data is available to populate this table.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: full prescribing information (warnings, contraindications) for raloxifene is currently missing from this evidence pack and is flagged as a **blocking data gap**, meaning this candidate cannot yet proceed to a formal safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications sit at evidence level L5 (TxGNN model prediction only, with no supporting clinical trials or literature). Raloxifene is not currently marketed in the UK for any indication in this evidence pack, and a blocking safety data gap (missing warnings/contraindications) prevents progression to initial safety assessment.

**To proceed, the following is needed:**
- Full prescribing information (SmPC warnings and contraindications) to unblock the safety review stage
- Confirmation of raloxifene's established original indication and mechanism of action in structured form
- Independent literature or trial search specifically for raloxifene in duodenal ulcer, to test whether the L5 signal can be upgraded
- If pursuing further, prioritise the hypoalphalipoproteinemia signal (rank 2) over duodenal obstruction/reflux (ranks 3–4), given its comparatively stronger mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

