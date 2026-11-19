---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 345
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
description: "Isotretinoin: predicted new indication Malignant hypertensive renal disease (evidence level L5). In the UK: 12 NHSBSA BNF presentation codes"
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Isotretinoin: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (and also malignant hypertensive renal disease), but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (12 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for isotretinoin: "The exact mechanism of action of Zenatane in the treatment of severe recalcitrant nodular acne in nonpregnant patients 12 years of age and older with multiple inflammatory nodules with a diameter of 5 mm or greater who are unresponsive to conventional therapy, including systemic antibiotics is unknown. Isotretinoin, a retinoid, inhibits sebaceous gland function and keratinization." ([DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee), label version 2026-09-20; accessed 2026-11-19.) The original indications recorded in the knowledge graph (hypertensive disorder, hypertension) are unusual for isotretinoin, which is a retinoid known mainly for treating severe acne.

The only mechanistic link that can be proposed is speculative: in preclinical settings, retinoids have been reported to influence renin-angiotensin signalling, renal vascular remodelling and renin expression. This is not supported by the data compiled for this report.

The second predicted indication, malignant hypertensive renal disease, has an identical score (0.9901). Isotretinoin's known adverse effects (teratogenicity, dyslipidaemia) also argue against an antihypertensive role without strong evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1306010M0AAAAAA | Isotretinoin 0.05% gel | Isotretinoin |
| 1306020J0AAACAC | Isotretinoin 10mg capsules | Isotretinoin |
| 1306020J0AAABAB | Isotretinoin 20mg capsules | Isotretinoin |
| 1306020J0AAADAD | Isotretinoin 20mg tablets | Isotretinoin |
| 1306020J0AAAEAE | Isotretinoin 40mg capsules | Isotretinoin |
| 1306020J0AAAAAA | Isotretinoin 5mg capsules | Isotretinoin |
| 1306010I0AAACAC | Isotretinoin 0.05% / Erythromycin 2% gel | Erythromycin |
| 1306010M0BBAAAA | Isotrex 0.05% gel | Isotretinoin |
| 1306010I0BDAAAC | Isotrexin gel | Erythromycin |
| 1306020J0BBACAC | Roaccutane 10mg capsules | Isotretinoin |
| 1306020J0BBABAB | Roaccutane 20mg capsules | Isotretinoin |
| 1306020J0BBAAAA | Roaccutane 5mg capsules | Isotretinoin |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

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
The recorded original indications look inconsistent with isotretinoin's actual use, and the safety profile is concerning for a severely compromised cardiovascular and renal population.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank)
- Label-based warnings and contraindications from the SmPC and BNF, and confirmation of the licence details with the MHRA
- Preclinical or clinical evidence that retinoids affect renovascular or malignant hypertension
- A risk assessment covering teratogenicity, lipid effects, renal effects and the interaction burden

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

