---
layout: default
title: Ascorbic Acid
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: From Ascorbic Acid Deficiency and Scurvy to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Ascorbic acid (vitamin C) is an essential nutrient, used to treat and prevent ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation**, but there are currently **no clinical trials** and **no publications** supporting this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency; scurvy (taken from knowledge-graph indication data, as no approved indication text is recorded for the UK authorisation) |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ascorbic acid is an essential water-soluble vitamin. Its efficacy in scurvy and ascorbic acid deficiency is well established, because it replaces a missing nutrient. Mechanistically, a link to a new indication is not evident.

Non-syndromic esophageal malformation is a congenital structural defect of the oesophagus. An antioxidant and cofactor vitamin is not plausibly able to correct a developmental anatomical abnormality. The high TxGNN score most likely reflects network-level associations in the knowledge graph rather than a biological rationale. No studies were identified to support or explain the link, so the prediction should be treated as a hypothesis only.

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
| 0906031C0AAAGAG | Ascorbic Acid Tab 100 mg | Tablet | Not stated in the data compiled for this report |

Only one authorisation is recorded (single-ingredient, valid). The identifier above is shown as recorded and is not in the standard MHRA "PL" format, so it should be verified against the MHRA register before any use. Please also check BNF and NICE guidance for the current licensed indications of ascorbic acid products.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug-disease relationship data, not from product label text, so they need confirmation against the SmPC): hypertension, epilepsy, kidney disease, liver disease, gallbladder disease, peptic ulcer disease, rheumatoid arthritis, systemic lupus erythematosus (including paediatric), multiple sclerosis, allergic and vasomotor rhinitis, sarcoidosis, diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, osteitis fibrosa, anuria, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency, blood coagulation disease, sickle cell anaemia, hereditary persistence of fetal haemoglobin, primary hyperoxaluria, hereditary haemochromatosis, sunburn and pyoureter.
- **Drug Interactions**: 25 interactions were identified in total, and 20 are detailed in the data compiled for this report.
  - Moderate: amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine, aluminium hydroxide, bortezomib, deferoxamine.
  - Minor: paclitaxel, cisplatin, doxorubicin (including liposomal), pseudoephedrine, ephedrine (including nasal), ethinylestradiol, flecainide, fluphenazine, indinavir, mexiletine.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, and there is no credible mechanism linking a nutritional vitamin to a congenital structural malformation of the oesophagus. This indication is not suitable for further development in its current form.

**To proceed, the following is needed:**
- A plausible mechanistic or developmental-biology rationale, together with any preclinical evidence.
- Detailed mechanism of action data for ascorbic acid.
- Clarification of the UK authorisation record (identifier, dosage form and approved indication text).
- Review of the lower-ranked predictions for the same drug. "Injury" (supported by several Phase 2 to 4 trials) and "esophageal disease" (supported by mostly preclinical and epidemiological literature, including an animal study that reported enhanced oesophageal carcinogenesis with ascorbic acid in a reflux model) have more supporting data and may be better candidates for evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

