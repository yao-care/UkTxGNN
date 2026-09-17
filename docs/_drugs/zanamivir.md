---
layout: default
title: Zanamivir
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a neuraminidase inhibitor developed for the treatment of influenza, acting on the influenza virus surface neuraminidase enzyme. The TxGNN model's top-ranked prediction suggests possible efficacy in **Pyelonephritis**, but this candidate currently has **no supporting clinical trials** and **no supporting literature**, and the internal mechanistic review flags the prediction as a likely false positive arising from knowledge-graph embedding co-occurrence rather than genuine biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (inferred from the drug's documented neuraminidase-inhibitor mechanism; not formally recorded in the available UK regulatory dataset for this candidate) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Zanamivir is not formally recorded in this Evidence Pack (flagged as a data gap). However, the rationale annotations accompanying every one of the ten TxGNN predictions in this pack consistently and independently describe Zanamivir as a neuraminidase inhibitor that acts specifically on the influenza virus's surface neuraminidase enzyme — consistent with its established clinical use as an anti-influenza agent.

Pyelonephritis, by contrast, is predominantly a bacterial ascending urinary tract infection. There is no known pathogenic mechanism involving viral neuraminidase in this condition, and no structural or pathway overlap between the influenza neuraminidase target and the bacterial processes underlying pyelonephritis. The internal mechanistic assessment concludes that this pairing lacks a plausible biological link and most likely reflects a knowledge-graph embedding artefact (co-occurrence-driven false positive) rather than a genuine repurposing signal.

This assessment is reinforced by the complete absence of supporting clinical trials or literature for this specific drug–disease pair, and by the fact that the same pattern (high TxGNN score paired with an explicitly implausible mechanistic rationale) recurs across all ten ranked predictions in this Evidence Pack — including dengue susceptibility, aspergillosis susceptibility, Legionnaires' disease susceptibility, and Schistosoma mansoni infection susceptibility, none of which share any plausible mechanistic pathway with a neuraminidase inhibitor.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Zanamivir currently has no marketing authorisations on record in this dataset (market status: **Not marketed**; total licences: **0**). No authorised UK product information is available for cross-reference against the predicted indication.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** This Evidence Pack flags TFDA-equivalent label warnings/contraindications as a **Blocking** data gap — safety data for this candidate has not yet been retrieved and must be obtained before any further evaluation (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (Pyelonephritis) has an L5 evidence level (model prediction only), zero supporting clinical trials, zero supporting literature, and an internal mechanistic review that explicitly identifies it as a probable false positive.
- All ten ranked predictions in this Evidence Pack show the same pattern — high TxGNN scores with mechanistically implausible rationales — indicating the overall candidate signal for this drug is weak at this stage.
- Zanamivir is not currently marketed in the relevant jurisdiction (0 marketing authorisations), and formal mechanism-of-action and safety-label data are both missing.

**To proceed, the following is needed:**
- Retrieval of official label warnings/contraindications (currently a Blocking data gap; source: regulatory label PDF, e.g. TFDA/MHRA equivalent)
- Formal mechanism-of-action data from DrugBank or an equivalent source
- Independent confirmation of a plausible biological mechanism linking neuraminidase inhibition to pyelonephritis before any further evidence collection is warranted
- If no such mechanism can be established, this candidate should be deprioritised in favour of higher-ranked candidates with actual clinical or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

