---
layout: default
title: Mazindol
parent: Model Prediction Only (L5)
nav_order: 384
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
description: "Mazindol: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
monitor_inn: "Mazindol"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny", "postural orthostatic tachycardia syndrome", "pentosuria", "lethal polymalformative syndrome, Boissel type"]
---

# Mazindol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Mazindol: From Obesity to Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Mazindol is a sympathomimetic appetite suppressant, originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the UK licence record contains no approved indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. From general pharmacology, mazindol is a sympathomimetic appetite suppressant that inhibits catecholamine (norepinephrine and dopamine) reuptake. Its efficacy in obesity rests on reduced appetite.

No plausible mechanistic link to hypervitaminosis could be identified. Vitamin excess and its clearance are unrelated to catecholamine reuptake inhibition. The very high TxGNN score is therefore best read as a TxGNN model (deep learning) artefact rather than a biologically grounded signal.

Other predictions in the same list include:
- **Proximal 16p11.2 microdeletion syndrome** (score 1.0000): this has a weak, indirect rationale, because the deletion is associated with severe early-onset obesity. The drug would not address the neurodevelopmental features of the syndrome.
- **Postural orthostatic tachycardia syndrome** (score 0.9960): norepinephrine reuptake inhibition has some biological plausibility. However, the same sympathomimetic action could worsen tachycardia and raise blood pressure, so the safety direction is uncertain.
- **Obsolete hypertelorism, frontorhiny, pentosuria and lethal polymalformative syndrome (Boissel type)**: no plausible mechanism; the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

None of these has supporting trials or literature.

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
| 0405020N0AAABAB (BNF-style product code; no PL number in the compiled data) | Mazindol Tab 1mg | Tablet | Not stated in the compiled data |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries (the 20 shown in the data compiled for this report include the following).
  - **Major**: tramadol, bupropion, methylene blue, lorcaserin.
  - **Moderate** (examples): sympathomimetics and bronchodilators (phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, arformoterol, isometheptene); opioids (fentanyl, alfentanil); antidiabetic agents (acarbose, alogliptin, pioglitazone, albiglutide); amitriptyline; amifampridine; and ethanol.
- **Class-related caution**: Because mazindol is a sympathomimetic, additive cardiovascular effects (raised heart rate and blood pressure) should be considered. This is a pharmacological expectation, not data from the compiled record.

Warnings and contraindications from the product label were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypervitaminosis is supported only by a model score, with no trials, no literature and no plausible mechanism. The evidence level is L5, and the drug's sympathomimetic profile and major interactions argue for caution.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic-link analysis
- Label warnings and contraindications (SmPC/BNF) to complete safety screening
- Confirmation of the UK authorisation details (PL number, dosage form, approved indication)
- Any preclinical or clinical evidence linking mazindol to vitamin excess or clearance
- If a repurposing direction is wanted, consider re-prioritising candidates with a more plausible rationale (for example, the obesity-related 16p11.2 microdeletion syndrome or postural orthostatic tachycardia syndrome), each requiring its own evidence review and cardiovascular safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

