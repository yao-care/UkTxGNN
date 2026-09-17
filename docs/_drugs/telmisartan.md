---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB), a drug class originally and widely used to treat hypertension. The TxGNN model predicts it may be effective for **Prinzmetal Angina**, but currently there are **no clinical trials** and **no publications** in this Evidence Pack that directly support this specific prediction — it is a model-only association at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (established ARB-class indication; not itself documented in this Evidence Pack, as `taiwan_regulatory.licenses` is empty) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap). Based on established pharmacological knowledge, Telmisartan is an angiotensin II receptor blocker (AT1 antagonist), a class whose efficacy in essential hypertension is well proven through lowering blood pressure and improving vascular endothelial function.

However, the link between this mechanism and Prinzmetal (variant) angina is weak. As noted in the Evidence Pack's own rationale: *"Telmisartan is an AT1 receptor antagonist that could theoretically influence coronary artery spasm indirectly through blood pressure reduction and improved vascular endothelial function. However, the principal pathophysiology of Prinzmetal angina is excessive coronary smooth muscle contraction, which has no direct correlation with ARB pharmacology. This is a pure TxGNN-predicted association, with no supporting mechanistic literature or clinical data."*

In other words, this prediction currently rests entirely on the knowledge-graph model's statistical association (score 99.98%, graph rank 511) rather than on any biological or clinical evidence trail.

**Note for reviewers:** This Evidence Pack is a multi-indication candidate covering 10 TxGNN-ranked predictions for Telmisartan. The top-ranked prediction by score (Prinzmetal angina, covered above) has the weakest evidence base of the set. By contrast, the pack's 9th-ranked prediction — **intracerebral hemorrhage** — carries the strongest evidence (L2, decision stage S2, "Proceed with Guardrails"), supported by a completed Phase 3 trial (NCT02699645, TRIDENT, n=1,671) and multiple mechanistic studies on AT1-blockade reducing oxidative stress and vasospasm. Reviewers assessing this candidate holistically may wish to prioritise that indication for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

---

## UK Market Information

Telmisartan does not currently hold any marketing authorisation recorded in this Evidence Pack (market status: **Not marketed**; 0 authorisations on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns an extremely high association score (99.98%) between Telmisartan and Prinzmetal angina, but no clinical trials, no literature, and no established mechanistic pathway currently support this link — the pathophysiology of coronary vasospasm does not correspond directly to ARB pharmacology. This remains a pure model-level (L5) prediction and does not meet the threshold for safety pre-screening (Stage S1).

**To proceed, the following is needed:**
- Preclinical/mechanistic studies specifically evaluating Telmisartan (or ARBs as a class) in coronary artery vasospasm models
- Clinical evidence (case series, observational studies, or trials) in a Prinzmetal angina population
- Detailed mechanism of action (MOA) data from DrugBank or SmPC
- UK marketing authorisation and SmPC data (currently none on file) to enable safety pre-screening
- Consider reprioritising evaluation toward **intracerebral hemorrhage** within this candidate set, given its substantially stronger existing evidence base (L2, Phase 3 RCT support)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

