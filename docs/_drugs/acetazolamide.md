---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Absence epilepsy, congestive heart failure…"
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "myopathic intestinal pseudoobstruction"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Acetazolamide: From Absence Epilepsy and Glaucoma to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor, originally used for conditions including absence epilepsy, congestive heart failure, glaucoma and altitude sickness.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**,
but there are **no clinical trials** and **no publications** supporting this specific prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy, congestive heart failure, open-angle and angle-closure glaucoma, altitude sickness (the UK authorisation record contains no indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetazolamide is a carbonic anhydrase inhibitor. Its efficacy in glaucoma, epilepsy, heart failure-related fluid retention and altitude sickness is established, and it may alter acid-base balance and ion handling.

A possible link to exercise-induced malignant hyperthermia, for example through changes in acid-base balance or muscle ion handling, is speculative. The data compiled for this report do not support it. The high TxGNN score (99.95%) is a computational output only and should not be read as evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For context, other predicted indications had some literature, but it is indirect:
- **Hypertrophic cardiomyopathy** (rank 2): heart failure reviews and one case report on acetazolamide for hypochloremia in advanced heart failure (PMID [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/)). None address hypertrophic cardiomyopathy directly.
- **Intestinal obstruction** (rank 8): a case report of acetazolamide-induced adynamic ileus (PMID [19653068](https://pubmed.ncbi.nlm.nih.gov/19653068/)), which is a safety signal rather than evidence of benefit.
- **Cardiomyopathy** (rank 7): a case report of non-cardiogenic pulmonary oedema after intravenous acetazolamide (PMID [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/)) and a preclinical rabbit heart study (PMID [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/)).

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000B0AAACAC | Acetazolamide Tab 250mg | Not specified | Not specified |

The compiled data list one valid single-ingredient authorisation. The identifier shown is not in the usual MHRA PL format, and the dosage form and indication fields are empty. Please verify the details against the MHRA register and the BNF.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from knowledge graph links, not from label text, and must be confirmed against the SmPC): liver disease and liver failure, kidney disease, gout, type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), respiratory failure, haematological disease, gallbladder disease, pyoureter and renal tubular acidosis.
- **Drug interactions** (100 recorded; the first 20 reviewed):
  - **Major**: acetylsalicylic acid, cisapride.
  - **Moderate**: antidiabetic agents (acarbose, acetohexamide, chlorpropamide, alogliptin, albiglutide, dulaglutide, canagliflozin, dapagliflozin), corticosteroids (beclomethasone, betamethasone, dexamethasone), amphotericin B formulations, and the laxatives bisacodyl and castor oil.
  - **Minor**: doxycycline.
- **Signals from the literature**: case reports of acetazolamide-induced adynamic ileus and non-cardiogenic pulmonary oedema after intravenous use. Cirrhosis also warrants caution because of the risk of hyperammonaemia and encephalopathy.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for exercise-induced malignant hyperthermia has no supporting trials or publications (evidence level L5), and the mechanistic link is speculative. The other top-ranked predictions have only indirect evidence, and some literature points to harm (ileus, pulmonary oedema).

**To proceed, the following is needed:**
- Mechanistic data, including the drug's mechanism of action and a plausible biological link to the predicted condition
- Preclinical or clinical evidence specific to exercise-induced malignant hyperthermia
- SmPC and BNF warnings and contraindications, and the full MHRA authorisation details (dosage form and approved indications)
- A safety review in the populations flagged by the knowledge graph (liver, kidney, diabetes, adrenal insufficiency)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

