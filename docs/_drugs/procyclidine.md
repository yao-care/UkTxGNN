---
layout: default
title: Procyclidine
parent: Model Prediction Only (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
---

# Procyclidine
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

# Procyclidine: From Movement-Disorder Symptom Control to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Procyclidine is referenced throughout this evidence pack's own rationale texts as an anticholinergic (antimuscarinic) agent used for motor-symptom control (e.g. Parkinsonism-type presentations); no formal original-indication or UK licence data is available. The TxGNN model's top-ranked prediction is **Rasmussen Subacute Encephalitis**, but this candidate has **zero clinical trials**, **zero published literature**, and is explicitly flagged in the evidence pack's own mechanistic rationale as lacking biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (drug not marketed in UK, no licence text available); contextual evidence in this pack points to anticholinergic use for movement-disorder symptoms |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for Procyclidine in this evidence pack. Based on the repurposing rationale text supplied alongside the predictions, Procyclidine functions as an anticholinergic (M1 muscarinic receptor antagonist) that modulates motor symptoms — consistent with its recognised pharmacological class used in Parkinsonism and drug-induced extrapyramidal symptoms.

For the top-ranked prediction, however, the evidence pack's own analysis works against the prediction rather than supporting it: Rasmussen subacute encephalitis is a T-cell-mediated autoimmune neuronal destruction disorder, and the rationale explicitly states there is **no direct mechanistic link** to anticholinergic motor-symptom modulation, describing the high TxGNN score as lacking biological plausibility.

Further down the ranked list, a small number of candidates show a more coherent mechanistic story — PLA2G6-associated neurodegeneration (rank 3) and progressive supranuclear palsy–corticobasal syndrome (rank 7) both involve dystonia/Parkinsonian motor features for which anticholinergics are a recognised symptomatic option. These are flagged as "Research Question" rather than "Hold," but still have no clinical trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Procyclidine currently holds no marketing authorisation in the UK evidence base for this pack (market status: Not Marketed; 0 licences on file). No product-level table can be produced until licensing data is obtained.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this evidence pack has a **Blocking**-severity data gap (DG001 — TFDA/UK label warnings and contraindications not yet retrieved), which prevents this candidate from entering initial safety screening (S1) until resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications sit at evidence level L5 (model prediction only), with no supporting clinical trials or literature for any of them. The top-ranked prediction, Rasmussen subacute encephalitis, is explicitly assessed within the pack as biologically implausible. Combined with the absence of UK marketing authorisation and a Blocking-severity safety data gap, this candidate is not ready to advance.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/UK SmPC warnings and contraindications (currently blocking safety screening)
- Resolve DG002: confirm mechanism of action via DrugBank API query
- If pursuing repurposing further, prioritise the mechanistically plausible "Research Question" candidates (PLA2G6-associated neurodegeneration; progressive supranuclear palsy–corticobasal syndrome) for targeted literature/case-report searches rather than the top-ranked score
- Confirm UK import/licensing pathway status, since the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

