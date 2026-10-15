---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 345
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Isotretinoin: From Hypertensive Disorder to Malignant Renovascular Hypertension

## One-Sentence Summary

According to the knowledge graph used for this report, isotretinoin is linked to hypertensive disorders as its original indication, although it is marketed in the UK as a topical gel (0.05%) product.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (and also malignant hypertensive renal disease), but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; no approved indication text is available in the licence data) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The original indications recorded in the knowledge graph (hypertensive disorder, hypertension) are unusual for isotretinoin, which is a retinoid known mainly for treating severe acne. This suggests the drug-indication links in the graph may be erroneous or mismatched, so the prediction should be treated with caution.

The only mechanistic link that can be proposed is speculative: in preclinical settings, retinoids have been reported to influence renin-angiotensin signalling, renal vascular remodelling and renin expression. This is not supported by the data compiled for this report.

The second predicted indication, malignant hypertensive renal disease, has an identical score (99.01%). This suggests both predictions come from the same hypertension-related region of the graph rather than from independent signals. Isotretinoin's known adverse effects (teratogenicity, dyslipidaemia) also argue against an antihypertensive role without strong evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1306010M0AAAAAA | Isotretinoin Gel 0.05% | Gel | Not stated in the available data |

Note: this licence identifier is not in the standard MHRA "PL XXXXX/XXXX" format, so it should be verified against the MHRA register before any further use.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are graph relationships, not label text):

- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
- Hepatic, renal and pancreatic: liver disease, kidney disease, pyoureter, pancreatitis, gallbladder disease
- Angioedema (several forms, including hereditary angioedema)
- Inflammatory bowel disease
- Osteoporosis (including postmenopausal osteoporosis)
- Systemic lupus erythematosus (including paediatric)
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperuricaemia
- Haematological: neutropenia, agranulocytosis
- **Hypotensive disorder**

**Drug Interactions:** 98 interactions were recorded. The main ones are:

- **Major:** doxycycline, minocycline, tetracycline, vitamin A
- **Moderate:** corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), warfarin, dicoumarol, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor, ethanol, abametapir (topical)

For label-based warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone (Evidence Level L5), with no trials or publications. The recorded original indications look inconsistent with isotretinoin's actual use, and the safety profile is concerning for a severely compromised cardiovascular and renal population.

**To proceed, the following is needed:**
- Verification of the knowledge-graph indication links for isotretinoin, which may be erroneous
- Mechanism of action data (e.g. from DrugBank)
- Label-based warnings and contraindications from the SmPC and BNF, and confirmation of the licence details with the MHRA
- Preclinical or clinical evidence that retinoids affect renovascular or malignant hypertension
- A risk assessment covering teratogenicity, lipid effects, renal effects and the interaction burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

