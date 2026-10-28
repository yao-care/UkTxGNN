---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
monitor_inn: "Orlistat"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Orlistat: From Obesity to Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Orlistat is a lipase inhibitor originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be useful for **hypervitaminosis**,
but there are currently **no registered clinical trials** and **no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the UK authorisation record holds no indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not included in the data compiled for this report. From general pharmacology, orlistat inhibits gastric and pancreatic lipases and reduces dietary fat absorption by about 30%.

Fat-soluble vitamins (A, D, E and K) are absorbed together with dietary fat. Orlistat is known to lower their absorption, and this is a recognised adverse effect in obesity treatment. The model's prediction may reflect this: in theory, reducing fat-soluble vitamin uptake could help in hypervitaminosis A or D.

This reasoning has important limits:
- The high TxGNN score is a computational prediction only and has not been tested clinically.
- The proposed benefit is the reverse of a known drug-related harm, and its safety and efficacy in this setting are unproven.
- Hypervitaminosis is usually managed by stopping the vitamin source, so the unmet need for a drug is unclear.
- Orlistat could cause deficiency of other fat-soluble vitamins and steatorrhoea.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0405010P0AAAAAA (BNF-style product code; no PL number recorded) | Orlistat capsules 120 mg | Capsule (inferred from the product name) | Not recorded |

BNF chapter 4.5 (obesity) is the usual classification for orlistat, and the record above corresponds to this code. The compiled data hold no indication text or NICE appraisal information for this product.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model graph edges, not from product label text): liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorder, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, and drug-induced liver injury. The vitamin deficiency disorder signal is particularly relevant to the proposed use.
- **Drug Interactions**: 100 interactions are recorded. Examples among those listed:
  - Moderate: abacavir, lamivudine, emtricitabine, atazanavir, acarbose, albiglutide, alogliptin, canagliflozin, metformin, chlorpropamide, amiodarone, cannabidiol, asparaginase products, brentuximab vedotin, calaspargase pegol, clofarabine.
  - Minor: cholecalciferol, calcifediol, calcitriol.

Warnings and contraindications from the product label were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical or published support (evidence level L5). Its mechanistic basis is the inverse of a known adverse effect, and the clinical need is unclear because hypervitaminosis is normally managed by removing the vitamin source.

**To proceed, the following is needed:**
- Product label (SmPC) warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data
- Authorisation details (PL number, dosage form, approved indication) for the UK record
- A literature review and trial search for orlistat in hypervitaminosis, including any case reports
- A clinical rationale showing an unmet need beyond stopping the vitamin source, plus a safety assessment of fat-soluble vitamin depletion and interaction risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

