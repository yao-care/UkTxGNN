---
layout: default
title: Menotropins
parent: Model Prediction Only (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Menotropins: predicted new indication Peptic esophagitis (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Menotropins"
predicted_indications: ["peptic esophagitis", "postural orthostatic tachycardia syndrome", "esophageal disease", "Raynaud disease", "non-syndromic esophageal malformation", "esophageal ulcer", "His bundle tachycardia", "sinoatrial block", "progressive familial heart block", "sinoatrial node disease"]
---

# Menotropins
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Menotropins: From Gonadotropin Therapy to Peptic Esophagitis
{: .text-alpha }

## One-Sentence Summary

Menotropins is a urinary-derived gonadotropin (FSH/LH) preparation used to stimulate follicular development and spermatogenesis. The TxGNN model predicts it may be effective for **peptic esophagitis**, but **no clinical trials and no publications** currently support this direction, and no plausible biological mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the UK licence record contains no indication text) |
| Predicted New Indication | Peptic esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, menotropins is a urinary-derived FSH/LH gonadotropin that acts on gonadal FSH and LH receptors to stimulate follicular development and spermatogenesis.

No plausible mechanistic link to peptic esophagitis has been identified. Oesophageal mucosal injury from acid reflux is not known to involve gonadotropin signalling. The high TxGNN score most likely reflects knowledge-graph topology rather than biological rationale, and should be treated as a computational output only.

The other top-ranked predictions show the same pattern. Most are oesophageal terms (oesophageal disease, oesophageal ulcer, oesophageal malformation), which likely cluster together through graph proximity. The remainder are cardiovascular or autonomic conditions (postural orthostatic tachycardia syndrome, Raynaud disease, sinoatrial block, His bundle tachycardia, progressive familial heart block, sinoatrial node disease), none with a supporting mechanism or evidence. For Raynaud disease, gonadotropin therapy can raise oestrogen levels and carries thromboembolic risk, so it could plausibly be unfavourable in vascular disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0605010N0AAAEAE (BNF code) | Menotrophin injection 75 units, 1:1 vial + diluent | Injection (powder and solvent) | Not stated in the data compiled |

The single listed entry is a single-ingredient product classed as valid. BNF chapter 6.5.1 (hypothalamic and anterior pituitary hormones) is the relevant classification. The record gives a BNF-style product code rather than a PL number.

---

## Safety Considerations

**Drug Interactions:**
- **Ganirelix** (Moderate): interaction recorded in the DDI database. Ganirelix is a GnRH antagonist often used alongside gonadotropins in fertility treatment, so clinical review of combined use is advisable.

No warning or contraindication text was available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications, no plausible mechanism linking gonadotropin signalling to peptic esophagitis, and key regulatory and safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking gonadotropin activity to oesophageal mucosal disease
- Approved indication and warning/contraindication text from the SmPC and BNF
- Preclinical or observational evidence supporting any benefit in peptic esophagitis
- Route and formulation compatibility assessment (currently an injectable product)
- Comparison against established treatments (for example, proton pump inhibitors) before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

