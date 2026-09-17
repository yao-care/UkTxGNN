---
layout: default
title: Metyrapone
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Metyrapone
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

# Metyrapone: From Adrenal Function Testing to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

> Metyrapone is an 11β-hydroxylase (CYP11B1) inhibitor, established for hypothalamic-pituitary-adrenal (HPA) axis testing and management of Cushing's syndrome.
> The TxGNN model predicts a possible link to **Exercise-Induced Malignant Hyperthermia**,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic review found no plausible pharmacological basis for the association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenal function (HPA axis) testing / Cushing's syndrome *(sourced from evidence-pack mechanistic notes; not confirmed via a formal indications record)* |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the formal `original_moa` field. Based on information contained elsewhere in the evidence pack, Metyrapone inhibits 11β-hydroxylase (CYP11B1) in the adrenal cortex, blocking cortisol synthesis; clinically it is used to test HPA axis function and to manage Cushing's syndrome.

Exercise-induced malignant hyperthermia and the related conditions predicted by the model (malignant hyperthermia susceptibility, King-Denborough syndrome, central core myopathy, multiminicore disease, centronuclear myopathy, familial periodic paralysis, renal tubular acidosis, and anaesthesia-induced malignant hyperthermia) are caused primarily by **RYR1** (and occasionally **CACNA1S**) mutations, which lead to abnormal calcium release from the sarcoplasmic reticulum in skeletal muscle. This is a fundamentally different biological pathway from adrenocortical steroidogenesis.

The evidence pack's own mechanistic review of all ten ranked candidates concludes that the high TxGNN scores most likely arise from indirect knowledge-graph proximity (for example, via shared "stress/steroid response" or "electrolyte/endocrine" intermediate nodes) rather than genuine pharmacological overlap. No candidate has any supporting clinical, preclinical, or literature evidence, and several rationales explicitly flag a theoretical risk that metyrapone could worsen electrolyte disturbance rather than help (e.g. renal tubular acidosis). This is a mechanistically weak, model-only signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Metyrapone currently holds **no active UK marketing authorisations** in this evidence pack (market status: Not Marketed; 0 licenses on file). No dosage form or licensed-indication data are available for review.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags a Blocking data gap — TFDA/SmPC warnings and contraindications for metyrapone have not yet been retrieved, so no drug-specific safety statements can be made at this stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, decision stage S0) with no supporting clinical trials or literature, and the evidence pack's own mechanistic analysis finds no credible biological link between cortisol-synthesis inhibition and RYR1-driven malignant hyperthermia/myopathy pathology. A blocking data gap on safety (TFDA/SmPC warnings) further precludes any safety assessment.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action data for metyrapone (currently marked as a data gap)
- TFDA/SmPC warnings and contraindications (Blocking gap — required before any S1 safety screening)
- Preclinical (in vitro/in vivo) evidence exploring any plausible interaction between adrenal steroidogenesis and RYR1-mediated calcium signalling, before this candidate can advance beyond L5
- Continued monitoring for emerging literature or trial registrations, given the complete current absence of clinical/observational evidence across all ten predicted indications in this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

