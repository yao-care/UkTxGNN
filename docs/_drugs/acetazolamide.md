---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-10-28
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Relations recorded in the knowledge graph: absence epilepsy…"
---

# Acetazolamide
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

## Acetazolamide: From Glaucoma and Altitude Sickness to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor, recorded in the knowledge graph for uses such as absence epilepsy, congestive heart failure, open-angle and angle-closure glaucoma, and altitude sickness.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia** (the top-ranked prediction), but there are **no clinical trials** and **no publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph: absence epilepsy, congestive heart failure, open-angle glaucoma, angle-closure glaucoma, altitude sickness (the UK licence record contains no indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetazolamide is a carbonic anhydrase inhibitor, a class that alters acid-base balance and fluid handling. It has long been used in conditions such as glaucoma and altitude sickness.

A speculative link to exercise-induced malignant hyperthermia would involve changes in acid-base balance affecting muscle excitation-contraction coupling. This is not supported by any study compiled for this report. The very high TxGNN score reflects a model prediction, not clinical evidence.

Other top-ranked predictions are also unsupported. For hypertrophic cardiomyopathy and cardiomyopathy, the only literature concerns heart failure in general. For intestinal obstruction and intestinal pseudo-obstruction, the literature points to a possible harm signal (acetazolamide-induced adynamic ileus).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for exercise-induced malignant hyperthermia.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000B0AAACAC | Acetazolamide Tab 250mg | Not stated | Not stated in the licence record |

The compiled data list one single-ingredient authorisation, which is currently valid. No indication text or dosage form is recorded, so the licensed indications should be checked against the current SmPC and BNF.

---

## Safety Considerations

- **Contraindications (relations recorded in the knowledge graph, not label text):** liver failure, liver disease, kidney disease, renal tubular acidosis, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), diabetes mellitus (type 1 and type 2), diabetic ketoacidosis, gout, gallbladder disease, haematological disease, respiratory failure, and pyoureter.
- **Drug Interactions:** 100 interactions were identified. Those listed include:
  - **Major:** acetylsalicylic acid (aspirin) and cisapride.
  - **Moderate:** antidiabetic agents (acarbose, acetohexamide, chlorpropamide, alogliptin, canagliflozin, dapagliflozin, albiglutide, dulaglutide), corticosteroids (dexamethasone, betamethasone, beclomethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil).
  - **Minor:** doxycycline.
- **Case-report signals from the literature:** acetazolamide-induced adynamic ileus (PMID 19653068) and non-cardiogenic pulmonary edema after intravenous use (PMID 29123889).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone. No clinical trials or publications address exercise-induced malignant hyperthermia, so the evidence level is L5. Several knowledge-graph contraindications and case-report safety signals also call for caution.

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible pharmacological link to malignant hyperthermia
- Preclinical or clinical studies that directly address the predicted disease
- Licence indication text and dosage form for the UK authorisation, plus SmPC warnings and contraindications
- A safety assessment against the recorded contraindications and interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

