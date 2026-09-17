---
layout: default
title: Retapamulin
parent: Model Prediction Only (L5)
nav_order: 500
evidence_level: L5
indication_count: 10
---

# Retapamulin
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

# Retapamulin: From Impetigo to Hordeolum

## One-Sentence Summary

Retapamulin is a topical pleuromutilin antibiotic originally used to treat impetigo caused by *Staphylococcus aureus* and *Streptococcus pyogenes*. The TxGNN model predicts a possible new application in **hordeolum (stye)**, but this prediction is currently supported by **no clinical trials and no published literature**, and rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo (topical skin infection) |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data has not been retrieved for this evaluation (data gap). Based on available product knowledge, retapamulin is a pleuromutilin-class topical antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit, giving it activity against *Staphylococcus aureus* and *Streptococcus pyogenes*. It is licensed only as a topical skin preparation for impetigo.

Hordeolum (a stye) is frequently caused by staphylococcal infection of the eyelid (Zeis or Meibomian) glands, which provides a superficial mechanistic rationale for exploring an antistaphylococcal agent. However, retapamulin has no licensed ophthalmic formulation and no available data on corneal or conjunctival penetration, tolerability, or ocular safety. The mechanistic overlap (antistaphylococcal activity) is real, but the route of administration and target tissue are substantially different from the approved indication, and this is not supported by any clinical or preclinical evidence in the current dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Retapamulin does not currently hold a UK marketing authorisation, and no licensed products are recorded in this dataset.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN model score (L5), with no clinical trials, no published literature, and no ophthalmic formulation or ocular safety data available. The drug is also not currently marketed in the UK. Nine other TxGNN-predicted indications for retapamulin were reviewed alongside this one; several (e.g. cysticercosis, candidiasis, helminthiasis) show no plausible mechanistic basis given retapamulin's antibacterial-only activity, suggesting these are likely knowledge-graph false positives rather than genuine repurposing signals.

**To proceed, the following is needed:**
- SmPC/product label warnings and contraindications (currently a blocking data gap)
- Formal mechanism-of-action confirmation from DrugBank or equivalent source
- Preclinical data on ocular tolerability and corneal/conjunctival penetration if an ophthalmic formulation were to be pursued
- At minimum, in vitro or case-series evidence of efficacy against staphylococcal eyelid infection before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

