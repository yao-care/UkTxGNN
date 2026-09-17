---
layout: default
title: Digitoxin
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Digitoxin
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

# Digitoxin: From Cardiac Glycoside Therapy to Prinzmetal Angina

## One-Sentence Summary

Digitoxin is a digitalis-class cardiac glycoside; the evidence pack does not record its original indication text, but its embedded pharmacological notes describe it as a Na⁺/K⁺-ATPase inhibitor and positive inotrope (the class historically used in heart failure and rhythm control). The TxGNN model's top-ranked prediction for this drug is **Prinzmetal angina** (score 97.86%), but **no clinical trials and no publications** currently support this specific link — it is a model-score-only candidate, and the evidence pack's own mechanistic review flags a plausible safety conflict rather than a supporting rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (flagged as a blocking data gap — MOA and indication data pending DrugBank/regulatory verification) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 97.86% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for digitoxin is not yet available in this evidence pack (logged as a High-severity data gap). Based on the information that is present, digitoxin is a cardiac glycoside that inhibits Na⁺/K⁺-ATPase, producing a positive inotropic effect — the pharmacological basis for its traditional use in heart failure and certain arrhythmias.

For the top-ranked candidate, Prinzmetal angina, the link is weak. Prinzmetal (vasospastic) angina is caused by coronary artery smooth-muscle spasm, not by impaired myocardial contractility, so there is no obvious mechanistic bridge from Na⁺/K⁺-ATPase inhibition to relief of coronary vasospasm. The evidence pack's own rationale goes further and notes a potential *conflict*: cardiac glycosides can provoke arrhythmias, which runs counter to the treatment goals for this indication. In short, this candidate is a pure TxGNN score output without mechanistic, preclinical, or clinical corroboration.

It is worth noting that other candidates within the same evidence pack — rheumatoid arthritis, thrombotic disease, and hyperthyroidism — carry more (though still preliminary, L4) literature support, including pharmacokinetic interaction data and studies of related cardiac glycosides (e.g. periplogenin). These are not the subject of this report but may warrant separate evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Digitoxin currently holds no UK marketing authorisations (0 licenses on record); market status is recorded as **not marketed**. No product-level dosage form or licence data is available for inclusion.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on the TxGNN model score (L5, S0), with zero clinical trials or publications specific to Prinzmetal angina, and the available mechanistic reasoning points toward a potential safety conflict (arrhythmogenic risk) rather than therapeutic rationale.

**To proceed, the following is needed:**
- Resolution of the blocking data gap: TFDA/MHRA SmPC warnings and contraindications (DG001)
- Confirmed mechanism-of-action and original indication data from DrugBank (DG002)
- Preclinical or mechanistic evidence specifically linking digitoxin (not related glycosides alone) to coronary vasospasm before any further evaluation stage is considered
- If pursuing repurposing further, consider prioritising the better-evidenced candidates in this pack (rheumatoid arthritis, hyperthyroidism) over Prinzmetal angina
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

