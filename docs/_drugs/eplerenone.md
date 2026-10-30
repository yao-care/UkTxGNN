---
layout: default
title: Eplerenone
parent: Model Prediction Only (L5)
nav_order: 254
evidence_level: L5
indication_count: 4
monitor_inn: "Eplerenone"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-30
description: "Eplerenone: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension"
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Eplerenone: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism
{: .text-alpha }

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor antagonist.
The TxGNN model predicts it may be useful for **pulmonary hypertension with unclear multifactorial mechanism**, but **no clinical trials and no publications** specifically support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (a relation recorded in the knowledge graph; no licence indication text is available) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eplerenone blocks the mineralocorticoid receptor (MR), the target of aldosterone. Aldosterone/MR signalling is linked to vascular remodelling, fibrosis and inflammation. Detailed mechanism-of-action data were not available for this report, so this description is a general inference.

Eplerenone is linked with hypertension, which is systemic blood-pressure disease. Pulmonary hypertension is a disease of the lung circulation. The two share a vascular element, and MR-driven remodelling could plausibly matter in both. This is a general mechanistic argument, not demonstrated evidence.

The very high TxGNN score (0.9950) is a computational prediction. The disease label "unclear multifactorial mechanism" is also broad, which makes a specific mechanistic argument harder. No similarity analysis between the original and predicted indications has been completed.

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
| 0202030X0AAAAAA | Eplerenone Tab 25mg | Not recorded | Not recorded |

This is a single-ingredient product with valid status. The dosage form and approved indication text are not recorded in the data compiled for this report. Please check the current SmPC and BNF entry for licensed indications.

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (not taken from label text): liver disease, gallbladder disease, diabetic nephropathy, and impaired renal function disease. Hyperkalaemia risk in renal impairment is a particular consideration.
- **Drug Interactions** (DDInter; 100 interactions in total, 20 reviewed here):
  - **Major**: aprepitant, clarithromycin, clotrimazole, potassium chloride, potassium citrate, potassium bicarbonate.
  - **Moderate**: corticosteroids (hydrocortisone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), acetylsalicylic acid, bupropion, miconazole, dronabinol, nabilone.

Label warnings and contraindications were not available for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or publications on this disease entry, so the evidence level is L5. Safety concerns include renal impairment and potassium-raising interactions.

**To proceed, the following is needed:**
- A focused literature review for pulmonary hypertension and MR antagonists. A separately listed prediction, pulmonary hypertension owing to lung disease and/or hypoxia, has mainly preclinical papers. These do not directly support this prediction and would need individual appraisal.
- Clarification of which pulmonary hypertension subtype is meant, given the broad "unclear multifactorial mechanism" label.
- Detailed mechanism-of-action data and label-based warnings and contraindications.
- Licensed indication and dosage form details for the UK authorisation.
- A safety plan covering potassium and renal function monitoring and the major interactions above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

