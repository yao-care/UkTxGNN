---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amlodipine: predicted new indication Brain stem infarction (evidence level L5). Approved use: Hypertension"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
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

## Amlodipine: From Hypertension to Brain Stem Infarction
{: .text-alpha }

## One-Sentence Summary

Amlodipine is a calcium channel blocker, originally used for hypertension, stroke-related and cerebrovascular disorders, and Prinzmetal angina.
The TxGNN model predicts it may be effective for **brain stem infarction**, but **no clinical trials and no publications** specific to this condition were found, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (licence indication text was not available; taken from the knowledge-graph indication list, which also includes stroke, cerebrovascular disorder, cerebral infarction and Prinzmetal angina) |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Amlodipine belongs to the calcium channel blocker class and is established for lowering blood pressure. Its blood pressure-lowering effect is the most plausible link to cerebrovascular protection.

Brain stem infarction is a sub-type of ischaemic stroke, and amlodipine is already associated with stroke, cerebral infarction and cerebrovascular disorder in the original indication list. The prediction is therefore likely to be a **sub-type of an existing indication** rather than true repurposing. Plausible links are blood pressure control and cerebrovascular protection, but no study specific to brain stem infarction supports this.

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
| 0206020A0AAAAAA (as recorded; this resembles a BNF-style product code rather than a PL number) | Amlodipine Tab 5mg | Tablet | Not stated in the data compiled |

The status is valid and the product is a single-ingredient formulation. Please check the current MHRA record and the BNF (cardiovascular system, calcium-channel blockers) for the licensed indications.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** The TxGNN knowledge graph links amlodipine to several conditions for caution or avoidance. These are not drawn from the product label and need verification against the SmPC. They include:
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Gastrointestinal: pancreatitis, gallbladder disease
  - Endocrine and metabolic: hypothyroidism, myxedema, diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, potassium deficiency disease
  - Immune and allergic: angioedema (including hereditary and RAAS-blocker-induced forms), systemic lupus erythematosus
  - Neuromuscular and haematological: myopathy, familial periodic paralysis, neutropenia, agranulocytosis
  - Cardiovascular: hypotensive disorder
- **Drug Interactions:** The interaction screen returned 100 records. The ones shown are all graded Moderate, including:
  - Corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone)
  - Aprepitant
  - Acetylsalicylic acid
  - Bupropion
  - Clarithromycin
  - Clotrimazole
  - SGLT2 inhibitors (canagliflozin, dapagliflozin)
  - Calcium salts (acetate, carbonate, chloride, citrate, gluconate, lactate and others)

Please refer to the SmPC and BNF for full warnings. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but there are no trials or publications for brain stem infarction. Amlodipine is already associated with stroke and cerebral infarction, so this is probably an extension of an existing indication rather than a new use.

**To proceed, the following is needed:**
- Clinical or observational evidence specific to brain stem or posterior circulation infarction
- Mechanism of action data to support the mechanistic-link analysis
- Product label warnings and contraindications from the SmPC and BNF, which are needed before any safety screening
- The licensed indication text and dosage form for the UK authorisation

**Note on other predictions in the data:** Intracerebral haemorrhage, a separate prediction, has stronger support. It rests on the completed Phase 3 TRIDENT trial (NCT02699645, n=1,671), which tested a single-pill combination of three low-dose antihypertensives that includes amlodipine, with results published in 2026 (PMID 42019018). That evidence supports the combination strategy for secondary prevention, not amlodipine alone, and may merit its own evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

