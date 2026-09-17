---
layout: default
title: Lisinopril
parent: Moderate Evidence (L3-L4)
nav_order: 349
evidence_level: L4
indication_count: 10
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Lisinopril: From ACE Inhibitor Therapy to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor (ACEI) with well-established class-wide benefits in hypertension, heart failure, and post-myocardial infarction ventricular remodelling. The TxGNN model predicts potential efficacy specifically in **posterolateral myocardial infarction**, but this anatomical MI subtype currently has **no dedicated clinical trials or published literature**, relying instead on indirect extrapolation from general post-MI ACEI trial evidence (e.g. SAVE, AIRE, TRACE).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (ACE inhibitor class; hypertension, heart failure, and post-MI use referenced in rationale text, but no formal indication text supplied) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (no licences on file in evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lisinopril in this evidence pack (data gap DG002). Based on the information referenced within the evidence pack's own rationale, Lisinopril belongs to the **ACE inhibitor (ACEI)** class, acting via inhibition of the renin-angiotensin-aldosterone system (RAAS). This mechanism underlies its established benefit in reducing post-MI ventricular remodelling and mortality — an effect that is broadly recognised as a **class effect** across ACEIs, supported by landmark trials such as SAVE, AIRE, and TRACE.

The link between general post-MI use and the specific predicted indication (posterolateral MI) is therefore mechanistically plausible but not empirically demonstrated: the pivotal trials establishing ACEI benefit after myocardial infarction did **not stratify outcomes by infarct anatomical location**. As a result, there is no direct evidence confirming that the class benefit extends equally to posterolateral infarcts specifically, as opposed to anterior, inferior, or other territories.

In short, the TxGNN score reflects strong network-level similarity between Lisinopril's known cardiovascular activity and the disease node for posterolateral MI, but this should be interpreted as a **hypothesis-generating signal** rather than confirmed efficacy for this specific anatomical subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (posterolateral myocardial infarction) has zero direct clinical trial or literature support — the mechanistic rationale rests entirely on indirect extrapolation from general post-MI ACEI class-effect data, which does not stratify by infarct location. This corresponds to evidence level L4 (mechanism/class-effect only, decision stage S1), insufficient to support progression without further validation.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent product labelling (warnings and contraindications) — currently a **blocking** data gap (DG001) preventing any S1 safety pre-assessment
- Confirmed mechanism of action detail specific to Lisinopril (DG002)
- Subgroup or anatomically-stratified analysis of existing post-MI ACEI trial data (e.g. SAVE/AIRE/TRACE) to assess applicability to posterolateral infarcts specifically
- UK-specific marketing authorisation and licensing data, as none is currently on file
- Route-of-administration compatibility assessment (currently marked "pending" in evidence pack)

---

### Note: Other Candidate Indications in This Evidence Pack

This evidence pack (`TW-DB00722-multi`) contains 10 TxGNN-predicted indications for Lisinopril, most of which (ranks 1–8, 10) have no supporting clinical trial or literature evidence (L4–L5, decision stage S0/S1, recommendation "Hold"). One notable exception is **rank 9, chronic pulmonary heart disease** (cor pulmonale), which has two small historical cohort studies specifically on lisinopril (PMID 14524095, PMID 17047621) and reaches evidence level L3 with a "Research Question" recommendation at decision stage S2 — this may warrant separate evaluation as a more promising candidate than the top-ranked prediction discussed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

