---
layout: default
title: Carteolol
parent: Model Prediction Only (L5)
nav_order: 135
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Carteolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertension, open-angle glaucoma and ocular hypertension"
monitor_inn: "Carteolol"
predicted_indications: ["primary hereditary glaucoma"]
---

# Carteolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Carteolol: From Hypertension and Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Carteolol is a non-selective beta-blocker with intrinsic sympathomimetic activity, originally used for hypertension, open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but at present there are **no clinical trials and no publications** supporting this specific prediction; it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma and ocular hypertension (from the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carteolol is a non-selective beta-adrenergic blocker with intrinsic sympathomimetic activity. In the eye it lowers intraocular pressure (IOP) by reducing aqueous humour production. Its efficacy in open-angle glaucoma and ocular hypertension is established.

Raised IOP is the main modifiable risk factor across glaucoma subtypes, so there is a plausible mechanistic basis for use in primary hereditary glaucoma (for example, MYOC- or CYP1B1-related forms). The very high TxGNN score is likely driven by the close proximity of this condition to the approved glaucoma indications in the knowledge graph, and it should not be read as evidence of clinical benefit.

There is an important caveat. Some hereditary glaucomas, such as primary congenital glaucoma, are caused by developmental anomalies of the anterior chamber angle and are usually managed surgically. In those cases, medical IOP lowering would be an adjunct at best.

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
| 1106000K0AAABAB | Carteolol HCl Eye Drops 2% | Eye drops (per product name) | Not available in the data compiled |

The licence number above is reproduced as recorded and does not follow the usual UK "PL XXXXX/XXXX" format, so it should be checked against the MHRA register. Manufacturer, dosage form and indication text are also missing from the record. NICE appraisal and BNF classification details were not available.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from graph relationships, not from label text, so they need verification against the SmPC): bronchitis, asthma (including intrinsic and allergic asthma), pulmonary emphysema, diabetes mellitus, diabetic ketoacidosis, myasthenia gravis (including adult-onset) and other neuromuscular junction disease, atrioventricular block, congestive heart failure, heart failure, and anaphylaxis.
- **Drug Interactions** (100 interactions recorded; the first 20 are shown in the data compiled):
  - **Major**: epinephrine, dolasetron.
  - **Moderate**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, methscopolamine, hyoscyamine, atropine, dicyclomine, bupropion, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, calcium phosphate, calcium acetate.
  - **Minor**: acetylsalicylic acid, magnesium oxide.

Product-specific warnings and contraindications from the label are not available. Please refer to the SmPC and BNF, and report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5), with no trials or publications for primary hereditary glaucoma. Label-level safety information is missing, and some hereditary glaucomas are mainly treated surgically, which limits the likely benefit of an IOP-lowering drug.

**To proceed, the following is needed:**
- Mechanism of action data, to support the mechanistic-link analysis
- Label-level warnings and contraindications from the SmPC and BNF, which are currently a blocking gap for safety screening
- A literature and trial search specific to carteolol in hereditary or primary congenital glaucoma subtypes
- Clarification of the UK licence record (dosage form, manufacturer, approved indication, licence number format)
- Assessment of route compatibility (topical ophthalmic use) and of how far the prediction differs from the existing open-angle glaucoma indication
- Clinical input on which hereditary glaucoma subtypes could realistically benefit from medical IOP lowering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

