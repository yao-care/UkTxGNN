---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 5
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and myocardial infarction"
---

# Atenolol
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker originally used for hypertension and myocardial infarction.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**,
but the data compiled for this report contain **no clinical trials and no publications** for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and myocardial infarction (relations recorded in the knowledge graph; no licence indication text is available for the UK product) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, atenolol is a beta-1 selective blocker that lowers blood pressure and reduces renin release. That is biologically plausible for hypertensive renal disease.

Malignant hypertensive renal disease is a severe form of hypertension with kidney involvement. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There are important caveats. Malignant hypertension with renal involvement is usually managed acutely with intravenous agents, and beta-blockers are not first line. Atenolol is cleared by the kidney, so dose adjustment is needed in renal impairment. The score is a model prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0204000E0AAAAAA | Atenolol oral solution 25mg/5ml sugar-free | Oral solution | Not stated in the available record |

This is one single-ingredient product record, listed as valid. The identifier appears to be a BNF-style product code rather than a PL number. The list is complete.

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver failure, asthma (including intrinsic and allergic asthma), type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, atrioventricular block, Raynaud disease, anaphylaxis, anuria, systemic lupus erythematosus, pancreatitis, gout, psoriasis, anxiety and related disorders, and several electrolyte or metabolic disorders (potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease). These are knowledge-graph relations and should be checked against the SmPC.
- **Drug interactions:** 100 interactions were found. Those listed include moderate-level interactions with epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acetohexamide, atropine, betamethasone, budesonide and several calcium salts. Minor interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.
- **Renal consideration:** atenolol is cleared renally, so dose adjustment is needed in renal impairment, which is directly relevant to the predicted indication.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no trial or publication studies atenolol in malignant hypertensive renal disease (Evidence Level L5). Guideline practice favours intravenous agents in the acute setting, and renal clearance adds a dosing concern.

**To proceed, the following is needed:**
- Clinical or observational studies of atenolol in hypertensive renal disease
- Mechanism of action data to support the link
- Licence indication text and SmPC safety information for the UK product
- A review of dosing and safety in renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

