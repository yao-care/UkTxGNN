---
layout: default
title: Terlipressin
parent: Model Prediction Only (L5)
nav_order: 566
evidence_level: L5
indication_count: 10
---

# Terlipressin
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

# Terlipressin: From No UK-Licensed Indication to Open-Angle Glaucoma

## One-Sentence Summary

Terlipressin is not currently marketed in the UK, and this Evidence Pack does not record an established original indication or mechanism of action (both flagged as data gaps). The TxGNN model predicts potential efficacy in **Open-Angle Glaucoma**, but this is a pure model-derived hypothesis with **no supporting clinical trials or literature**, and the underlying pharmacology is more consistent with raising intraocular pressure than lowering it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no UK marketing authorisation and no original indication recorded in this Evidence Pack |
| Predicted New Indication | Open-Angle Glaucoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Terlipressin in this Evidence Pack (flagged as a High-severity data gap, DG002). What is known is that Terlipressin is a synthetic analogue of vasopressin and acts as a selective agonist at the V1 vasopressin receptor, producing splanchnic and systemic vasoconstriction — a property historically exploited in conditions such as variceal bleeding and hepatorenal syndrome, though this Evidence Pack does not itself document a confirmed original indication.

For the predicted indication of open-angle glaucoma, the repurposing rationale supplied with this candidate is explicitly cautionary rather than supportive: V1 receptor agonism could theoretically influence intraocular pressure via vascular effects, but there is no known mechanism by which Terlipressin would *lower* intraocular pressure. If anything, V1 agonist activity is more plausibly associated with *raising* intraocular pressure, which runs counter to the therapeutic direction required in glaucoma management. No clinical or literature evidence has been identified to support this indication, and this candidate should be interpreted as a statistical knowledge-graph association rather than a mechanistically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Detailed warning and contraindication data for Terlipressin could not be retrieved for this Evidence Pack (flagged as a Blocking-severity data gap, DG001), and this itself prevents progression into the S1 safety pre-screening stage for any predicted indication of this drug.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has an Evidence Level of L5 — a TxGNN model prediction with zero supporting clinical trials or literature — and the accompanying mechanistic rationale actively argues against biological plausibility (V1 agonism is more likely to raise, not lower, intraocular pressure). There is no basis to advance this indication beyond hypothesis generation.

**To proceed, the following is needed:**
- Terlipressin's original approved indication(s) and confirmed mechanism of action (currently unavailable in this Evidence Pack)
- MHRA/manufacturer SmPC data on warnings, contraindications, and drug interactions (currently a Blocking data gap)
- Preclinical or pharmacodynamic data specifically examining Terlipressin's effect on intraocular pressure, to resolve the directional conflict noted above
- Any real-world, case-report, or registry evidence in glaucoma populations, none of which currently exists

**Note for reviewers:** Among the 10 candidates in this Evidence Pack, rank 3 ("pulmonary hypertension" in the setting of cirrhosis/portopulmonary hypertension) has materially stronger support — 4 clinical trials and ~20 literature records, with several directly reporting reductions in pulmonary vascular resistance after Terlipressin administration (Evidence Level L4, decision stage S1, "Research Question"). If the objective is to identify the most viable repurposing direction for Terlipressin rather than strictly the top-ranked TxGNN score, that candidate warrants a separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

