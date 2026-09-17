---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Pioglitazone: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (TZD) insulin sensitiser; the supporting literature in this evidence pack consistently discusses its use in **type 2 diabetes mellitus**, though a formal UK licensed indication is not present in this dataset. The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare monogenic skeletal dysplasia, but this signal is currently supported by **zero clinical trials and zero publications**, and the model's own mechanistic annotation states there is no known biological link — this prediction should be treated as low-confidence, possible knowledge-graph noise rather than a genuine repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from supporting literature titles/abstracts; no formal UK licence indication text available in this evidence pack) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Pioglitazone is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the supporting literature that is present, Pioglitazone belongs to the thiazolidinedione class and acts as a **PPAR-γ agonist**, improving insulin sensitivity and pancreatic beta-cell function in type 2 diabetes.

For the top-ranked prediction, **Opsismodysplasia**, TxGNN's own evidence annotation is explicit that no known mechanistic relationship exists: the condition is a skeletal dysplasia caused by **INPPL1** gene mutations, with no established connection to the PPAR-γ signalling pathway. The high TxGNN score in this case is most plausibly explained by graph-embedding noise (disease-node proximity in the knowledge graph) rather than genuine pharmacological plausibility.

It is worth noting that several lower-ranked candidates in this evidence pack (e.g. drug-induced localized lipodystrophy, centrifugal lipodystrophy, idiopathic localized lipodystrophy — ranks 5–8) have a more biologically coherent rationale, since PPAR-γ is a key regulator of adipocyte differentiation and TZDs are known to alter fat distribution. However, none of these candidates currently have any supporting clinical trial or literature evidence either, and TZDs are paradoxically also *associated with* lipodystrophy-type adverse effects, which weakens rather than strengthens the case. One candidate (pancreatic agenesis, rank 9) has literature evidence, but all identified publications concern insulin-resistance management in type 2 diabetes — a pathophysiologically different, insulin-*deficient* condition where an insulin-sensitising agent would be expected to have limited benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Pioglitazone currently has **0 recorded marketing authorisations** in this evidence pack, and UK market status is **Not marketed**. TFDA/MHRA product licence and Summary of Product Characteristics (SmPC) data have not yet been retrieved (flagged as a Blocking data gap, DG001) — this must be resolved before any safety (S1) evaluation can proceed.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Opsismodysplasia) has no supporting clinical trial or literature evidence, and its own mechanistic rationale confirms no known biological link to Pioglitazone's PPAR-γ mechanism — most likely reflecting knowledge-graph noise. In addition, foundational data required for baseline evaluation (confirmed original indication, MOA, UK licensing, safety information) is currently missing from this evidence pack.

**To proceed, the following is needed:**
- TFDA/MHRA product licence and SmPC data (Blocking gap, DG001) — required before any safety (S1) evaluation
- Confirmed mechanism of action via DrugBank API (High-severity gap, DG002)
- Confirmed formal original indication and licensed indication text
- If exploring the lipodystrophy-related candidates (ranks 5–8) as an alternative direction: dedicated preclinical/mechanistic studies on PPAR-γ agonism in fat-redistribution disorders, given TZDs' known paradoxical association with lipodystrophy as an adverse effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

