---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 285
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Fentanyl is a potent mu-opioid receptor agonist, available in the UK as a transdermal patch.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **no clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is generally known as a mu-opioid receptor agonist, but the approved indication for the listed product is not recorded here.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which cause water retention even when vasopressin is undetectable. Opioids can influence vasopressin release centrally, and SIADH-like effects have been reported with opioids. However, this would not correct a receptor-level, vasopressin-independent defect.

**No established mechanistic link was identified.** The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (for example, those involving water-balance or vasopressin-related pathways), not biological evidence. Fentanyl may in fact worsen water retention or hyponatraemia, which is a safety concern rather than a benefit.

A second prediction, **Tourette syndrome** (score 0.9905), was also generated. Its rationale is weak and speculative. The endogenous opioid system modulates striatal dopamine, but there is no clinical evidence for fentanyl in tic suppression. Its abuse liability, respiratory depression, tolerance and dependence make it unsuitable for a chronic neurodevelopmental condition. It is also evidence level L5 with a recommendation of Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407020A0AAAEAE | Fentanyl Transdermal Patch 25mcg/hr | Transdermal patch | Not available in the data compiled |

The product code above is the BNF-style identifier recorded for this product. It is not a PL number. Only one authorisation (single-ingredient, valid) is recorded.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease contraindication links from the TxGNN knowledge graph, not from label text). Those most relevant to this report include:
  - Respiratory and airway: chronic obstructive pulmonary disease, asthma (intrinsic and allergic)
  - Cardiovascular: hypertension, hypotensive disorder, orthostatic hypotension, long QT syndrome, torsades de pointes
  - Hepatic, renal and gastrointestinal: liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease, inflammatory bowel disease
  - Neurological and psychiatric: multiple system atrophy, basal ganglia disease, anxiety disorder, substance abuse/dependence
  - Other: benign prostatic hyperplasia, potassium deficiency disease
- **Drug interactions**: 100 interactions were identified (DDInter). Examples:
  - *Major*: alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dolasetron, fenfluramine, granisetron, lorcaserin
  - *Moderate*: atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycopyrronium, hyoscyamine
- **Concern specific to the predicted indication**: fentanyl may worsen water retention or hyponatraemia.

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5), with no clinical trials or publications. The proposed mechanism is not plausible for a receptor-level defect, and fentanyl's safety profile (including possible worsening of hyponatraemia) argues against pursuing this indication.

**To proceed, the following is needed:**
- Original approved indication and SmPC-based warnings and contraindications for the UK product
- Mechanism of action data
- Evidence of a plausible mechanistic link to AVPR2-mediated water retention (preclinical or mechanistic studies)
- Safety assessment of effects on sodium and water balance
- Review of the Tourette syndrome prediction only if supporting clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

