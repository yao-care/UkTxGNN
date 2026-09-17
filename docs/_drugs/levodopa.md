---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Levodopa is a dopamine precursor established for the treatment of Parkinson's disease and related movement disorders.
> The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**,
> but currently **no clinical trials** and **no published literature** support this direction — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (established pharmacological use; formal licensing/indication text not available in this evidence pack) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (data gap). Based on known pharmacology, levodopa is a dopamine precursor that crosses the blood–brain barrier and is decarboxylated to dopamine, replenishing striatal dopamine deficits in Parkinson's disease and other movement disorders.

Rasmussen subacute encephalitis is a rare, typically unilateral, progressive autoimmune/inflammatory encephalitis driven by T-cell–mediated neuronal destruction and chronic cortical inflammation. There is no established pharmacological pathway linking dopamine replacement to the immune-mediated processes underlying Rasmussen encephalitis.

Given the absence of any supporting clinical trials or literature, the high TxGNN score most likely reflects topological similarity between neurological disease nodes in the knowledge graph — both conditions sit within the "neurological disorder" region of the graph — rather than a genuine, mechanistically grounded relationship. Without original indication and MOA data confirmed from an authoritative source, this link cannot currently be substantiated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Levodopa (as this candidate/product) currently has no UK marketing authorisations on record; market status is "Not marketed." No authorisation numbers, product names, or approved indication text are available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) — there are no clinical trials, no supporting literature, and no plausible mechanistic link between dopamine replacement therapy and an autoimmune encephalitis. A blocking safety data gap (TFDA/MHRA-equivalent SmPC warnings and contraindications) also prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- SmPC/product label warnings, precautions, and contraindications (blocking gap — required before any S1 safety screening)
- Confirmed mechanism of action data from an authoritative source (e.g. DrugBank API)
- Independent mechanistic or preclinical rationale connecting dopaminergic pathways to Rasmussen encephalitis pathology
- Any emerging case reports, observational data, or trial registrations in this indication before re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

