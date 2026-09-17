---
layout: default
title: Zonisamide
parent: Model Prediction Only (L5)
nav_order: 620
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

Zonisamide is an antiepileptic drug used as adjunctive or monotherapy treatment for partial-onset seizures in epilepsy. The TxGNN model predicts it may be effective for **Tourette Syndrome**, but this specific prediction is currently supported by **no clinical trials** and **no published literature** — the model's confidence score is high, yet there is no direct clinical evidence, and related literature elsewhere in this evidence pack raises the opposite concern (that antiseizure medications may induce tic disorders rather than treat them).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset seizures) — no formal marketing authorisation on record in this evidence pack; use as an antiepileptic drug is referenced in the supporting literature below |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Zonisamide (marked as a data gap in this evidence pack). Based on information captured elsewhere in this pack's literature evidence, Zonisamide is a benzisoxazole-derivative antiepileptic drug used as adjunctive or monotherapy treatment for partial-onset seizures, acting through sodium channel blockade and T-type calcium channel inhibition, with additional effects on glutamatergic and dopaminergic signalling.

The rationale offered for the Tourette syndrome prediction is that Zonisamide's sodium/T-type calcium channel blockade resembles topiramate, an antiepileptic drug with some published evidence for tic suppression. On this basis, TxGNN infers a theoretical mechanistic link between Zonisamide and tic disorders.

However, this mechanistic plausibility is undermined by two important caveats. First, no clinical trial or publication in this evidence pack directly evaluates Zonisamide in Tourette syndrome or tic disorders — the prediction is score-driven only. Second, other literature captured in this evidence pack under a related indication (PMID 36005856, a pragmatic review of antiseizure medication-induced obsessive-compulsive disorder and tic disorder) reports that antiseizure medications as a class may **induce or worsen** tics and OCD symptoms — the opposite of the therapeutic direction proposed here. This raises the possibility that the mechanistic signal picked up by TxGNN reflects a safety concern rather than a treatment opportunity, and should be treated with caution rather than as supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Zonisamide currently holds no marketing authorisation on record in this evidence pack (total licenses: 0; market status: **Not marketed**). No dosage forms or approved indication text are available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score for Tourette syndrome is high, the evidence level is L5 — there are no clinical trials or published literature directly supporting this indication. Furthermore, related literature in this evidence pack flags a plausible reverse safety signal (antiseizure medications inducing tic/OCD symptoms) rather than confirming therapeutic benefit, and Zonisamide is not currently marketed in the jurisdiction reviewed here. The evidence does not currently justify progression beyond a research hypothesis.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data to properly assess pharmacological relevance to tic disorders (currently a data gap, marked High severity)
- Regulatory safety label data — key warnings and contraindications (currently a data gap, marked **Blocking** severity; required before any initial safety assessment can proceed)
- Dedicated clinical studies or case series specifically evaluating Zonisamide in Tourette syndrome/tic disorders, to resolve the directionality uncertainty raised by PMID 36005856
- Drug-drug interaction data (currently not found)
- Consideration of other candidates in this same evidence pack with comparatively stronger (though still mixed) evidence — notably manic bipolar affective disorder (L2, one placebo-controlled RCT) and absence epilepsy (L3, supported by case series and broader AED trial data) — which may warrant review ahead of the top TxGNN-scored candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

