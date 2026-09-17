---
layout: default
title: Lactic Acid
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Lactic Acid
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

Using no specific skill — this is a direct report-generation task following the given template exactly.

# Lactic Acid: From No Recorded Indication to Atypical Coarctation of Aorta

## One-Sentence Summary

Lactic acid (DrugBank DB04398) is an endogenous metabolic intermediate with no recorded therapeutic indication and no UK marketing authorisation in this evidence pack.
The TxGNN model predicts it may be effective for **Atypical Coarctation of Aorta**, but this ranks among the model's highest-confidence predictions with **zero clinical trials** and **zero publications** supporting it — the model itself flags this as a likely false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record — lactic acid is an endogenous metabolite, not an approved medicinal product in this dataset |
| Predicted New Indication | Atypical Coarctation of Aorta |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lactic acid. Based on the information provided, lactic acid is an endogenous glycolysis product rather than a drug developed against a specific indication — there is no recorded original indication to compare against, and no UK marketing authorisation exists.

The TxGNN model assigned a very high score (0.9959) to "atypical coarctation of aorta," but this is unsupported by any clinical trial or literature evidence. The evidence pack's own annotation explicitly raises concern that this is a **high-connectivity artefact**: as a ubiquitous endogenous metabolite, lactic acid is linked to an unusually large number of nodes in the knowledge graph, which can inflate TxGNN scores without reflecting a genuine pharmacological relationship. There is no plausible mechanistic pathway connecting exogenous lactic acid administration to correction of a structural congenital aortic malformation.

For context, nine other candidates were reviewed in this evidence pack (ranks 2–10). Two reached a somewhat firmer evidence tier (L4) — "aortic malformation" and "eye disease" — but in both cases the literature concerned lactate's *endogenous* pathological role (e.g., promoting choroidal neovascularisation, myopia progression via histone lactylation, tumour immune evasion) rather than any therapeutic benefit of administering lactic acid. No candidate in the pack — including the top-ranked one — has trial or literature evidence of lactic acid being tested as a treatment. Overall, this candidate set does not support a repurposing hypothesis at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Lactic acid holds **no UK marketing authorisation** on record in this evidence pack (0 licenses; market status: Not marketed). There is no product information to summarise.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> Note: TFDA/MHRA-equivalent labelling data (warnings, contraindications) is currently a **Blocking** data gap for this candidate, meaning no formal safety evaluation (S1 stage) can proceed until this is sourced.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trial or literature support, and the model's own annotation identifies it as a probable false positive driven by lactic acid's high connectivity as a common metabolite in the knowledge graph, not a genuine mechanistic signal. With no mechanism of action data, no original indication, and no UK marketing authorisation, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Mechanism of action data for lactic acid (DG002) to assess any plausible biological rationale
- Regulatory labelling/warnings data (DG001 — currently blocking) before any safety-stage review
- Independent, non-KG-based validation to rule out the suspected high-connectivity artefact before further work
- If pursued at all, the "eye disease" (rank 9) and "aortic malformation" (rank 2) candidates warrant closer scrutiny only as research questions into lactate biology, not as therapeutic repurposing candidates — the current evidence points to lactate as a pathological driver rather than a treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

