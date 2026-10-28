---
layout: default
title: Felodipine
parent: Model Prediction Only (L5)
nav_order: 279
evidence_level: L5
indication_count: 5
monitor_inn: "Felodipine"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-23
description: "Felodipine: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension"
---

# Felodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Felodipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism
{: .text-alpha }

## One-Sentence Summary

Felodipine is a calcium channel blocker used for hypertension, though the UK licence record compiled for this report carries no indication text.
The TxGNN model predicts it may be useful for **pulmonary hypertension with unclear multifactorial mechanism**,
but **no clinical trials** and **no publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (relation recorded in the knowledge graph; the licence record contains no indication text) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Number of Approvals | 1 licence record (single-ingredient product) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Felodipine is a dihydropyridine L-type calcium channel blocker. It relaxes vascular smooth muscle and lowers systemic vascular resistance.

Because the drug dilates blood vessels, an effect on the pulmonary circulation is biologically plausible, which may explain the high model score. However, calcium channel blockers help only a small subset of patients with pulmonary arterial hypertension, namely those who are vasoreactive. "Pulmonary hypertension with unclear multifactorial mechanism" is a heterogeneous, loosely defined entity. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Licence Identifier | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| 0206020F0AAACAC | Felodipine Tab 10mg M/R | Modified-release tablet (from product name) | Valid, single-ingredient |

The record gives no approved indication text, so the table does not state how the product is licensed.

---

## Safety Considerations

**Contraindication-type relations recorded in the knowledge graph** (these are graph edges, not label text, and should be checked against the SmPC): kidney disease, liver disease, gallbladder disease, angioedema (including hereditary and acquired forms), neutropenia, agranulocytosis, aortic stenosis and other aortic valve disease, hypotensive disorder, hypertrophic cardiomyopathy, renal artery obstruction, myocardial infarction, coronary artery disease, atherosclerosis, connective tissue, bone and cartilage disease, and haemoglobinopathy.

**Drug Interactions** (100 interactions in total; the data compiled lists 20, of which 19 are Moderate and 1 is Major):
- **Major:** dolasetron
- **Moderate, examples:** cimetidine, clarithromycin, aprepitant, bupropion, morphine, acetylsalicylic acid, canagliflozin, dapagliflozin, empagliflozin, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)

**Disease-specific concern:** systemic vasodilators in hypoxic lung disease can worsen ventilation-perfusion matching and gas exchange.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies felodipine in this predicted condition, so the evidence level is L5 and the high TxGNN score is not enough to justify further action. The hypoxic-lung-disease concern adds to the case for caution.

**To proceed, the following is needed:**
- Mechanism of action data for felodipine
- Direct clinical or well-designed preclinical studies in a defined pulmonary hypertension group (for example, vasoreactive pulmonary arterial hypertension)
- A review of the SmPC and BNF warnings and contraindications, as the data compiled for this report holds no label-based safety text
- An assessment of the effects on gas exchange and right ventricular function in patients with lung disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

