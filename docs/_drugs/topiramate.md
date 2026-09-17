---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 9
---

# Topiramate
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Topiramate is a broad-spectrum antiepileptic drug (AED), with literature evidence in this pack confirming established use in epilepsy and migraine prophylaxis, though no structured original-indication or marketing authorisation data was captured for this Evidence Pack.
The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm**, but this candidate is currently supported by **0 clinical trials** and **0 publications**.
The evidence pack's own mechanistic assessment flags this prediction as a likely false positive arising from knowledge-graph node proximity rather than genuine pharmacological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (no marketing authorisation record); literature evidence indicates established use in epilepsy and migraine prophylaxis |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per this Evidence Pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for topiramate as a structured field in this Evidence Pack (data gap DG002). However, the literature evidence collected under other predicted indications in this pack consistently describes topiramate as a broad-spectrum antiepileptic drug acting through sodium-channel blockade, GABA-A receptor potentiation, and AMPA/kainate glutamate receptor antagonism — a neuromodulatory profile used to reduce neuronal excitability in epilepsy and migraine.

There is no established pharmacological or clinical relationship between this neuromodulatory mechanism and tumour growth inhibition in trigeminal nerve neoplasms. Unlike other predicted indications in this pack (e.g. reflex epilepsy subtypes), which share a plausible mechanistic link to topiramate's anticonvulsant activity, a trigeminal nerve neoplasm has no known biological pathway connecting it to sodium-channel or GABAergic modulation.

Critically, the evidence pack's own repurposing rationale for this candidate explicitly states that the prediction is likely a **false positive caused by knowledge-graph node proximity**, not a genuine biological signal. This is corroborated by the complete absence of clinical trials or literature evidence, and the model assigns this candidate the lowest evidence level (L5) and decision stage (S0), with a "Hold" recommendation already embedded in the source scoring.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

No UK marketing authorisation entries were identified in this Evidence Pack for topiramate; market status is recorded as "not marketed" with 0 licences on record. This should be independently verified against the MHRA public register and BNF, as this gap may reflect incomplete data capture rather than genuine absence of UK authorisation.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (trigeminal nerve neoplasm) has no supporting clinical trials or literature (evidence level L5, decision stage S0), and the pack's own mechanistic analysis identifies it as a probable false positive driven by knowledge-graph node proximity rather than plausible biology.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for topiramate (data gap DG002)
- MHRA/SmPC warnings and contraindications (data gap DG001)
- Independent target/pathway validation of the knowledge-graph signal before any further evaluation of this specific candidate
- Confirmation of current UK marketing authorisation status, as the "not marketed / 0 licences" record in this pack should be verified against the MHRA register
- Consideration of alternative TxGNN-predicted indications in the same evidence pack with materially stronger support — notably **visual epilepsy** (rank 2, evidence level L2, decision stage S2, "Research Question"), backed by a completed Phase 3 RCT (n=750) and multiple Cochrane systematic reviews within the idiopathic generalised epilepsy spectrum — which may represent a more credible repurposing lead than the top-ranked candidate evaluated here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

