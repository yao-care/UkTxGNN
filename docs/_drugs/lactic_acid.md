---
layout: default
title: Lactic Acid
parent: Model Prediction Only (L5)
nav_order: 357
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Lactic Acid: predicted new indication Atypical coarctation of aorta (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome"]
---

# Lactic Acid
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

## Lactic Acid: From an Unspecified Original Indication to Atypical Coarctation of Aorta
{: .text-alpha }

## One-Sentence Summary

Lactic acid is an endogenous metabolite marketed in the UK, but the data compiled for this report contain no approved indication text for it.
The TxGNN model predicts it may be effective for **atypical coarctation of aorta** with a very high score, yet there are **0 clinical trials** and **0 publications** for this prediction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Lactic acid is an endogenous metabolite (the end product of glycolysis), and no approved indication text was available for it, so the link between an original and a new indication cannot be established.

No mechanistic link was identified for this prediction. The TxGNN score is high (0.9959), but there are no trials and no literature. Atypical coarctation of aorta is a structural vascular malformation, which is managed surgically or by intervention. There is no known role for a metabolite such as lactic acid in treating it. The prediction should be regarded as a TxGNN model (deep learning) artefact until proven otherwise.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Evidence Summary |
|------|------|------|------|
| 2 | Aortic malformation | 0.9935 | 14 papers, none testing lactic acid as a therapy |
| 3 | Non-syndromic oesophageal malformation | 0.9923 | No evidence |
| 4 | Amenorrhoea | 0.9916 | 1 baboon vaginal microbiota study |
| 5 | Dry eye syndrome | 0.9913 | Biomarker, probiotic and supplement studies; none tests lactic acid |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (atypical coarctation of aorta), currently no related literature available.

For the second-ranked prediction (aortic malformation), 14 papers were retrieved, but none evaluates lactic acid as a treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | Preclinical | J Vasc Surg | Aortic wall metabolism in rabbits with coarctation and atherosclerosis |
| [23791497](https://pubmed.ncbi.nlm.nih.gov/23791497/) | 2013 | RCT | J Cardiothorac Vasc Anesth | Ultrafiltration strategy in paediatric cardiac surgery; not lactic acid therapy |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | Preclinical | Catheter Cardiovasc Interv | Poly-L-lactic acid biodegradable stent in rabbit aorta (device material) |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | Case report | Pediatr Cardiol | Absorbable poly-L-lactic acid microplate for bronchomalacia in congenital heart disease |
| [14128102](https://pubmed.ncbi.nlm.nih.gov/14128102/) | 1963 | Not classified | Minerva Pediatr | Blood lactic acid behaviour in children with congenital heart disease |

The remaining papers cover perioperative biomarkers and surgical cohorts, with lactic acid appearing only incidentally.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190600000AAATAT | Lactic Acid_Liq | Not stated | Not stated |

Only one single-ingredient authorisation is recorded, and it is currently valid. Its dosage form and approved indication were not available in the data compiled for this report, so this identifier should be verified against the MHRA register, as it does not follow the usual PL number format.

---

## Safety Considerations

- **Drug Interactions**: 17 interactions were identified. Those of moderate severity are:
  - Tetracycline-class antibiotics (doxycycline, tetracycline, minocycline, demeclocycline, oxytetracycline)
  - Salicylates (acetylsalicylic acid, sodium salicylate)
  - Sympathomimetics (ephedrine, nasal ephedrine, pseudoephedrine)
- Minor interactions involve sulfonylureas (chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide) and methotrexate.

Literature in the data also suggests lactate may have harmful roles in some settings: it is linked to immunosuppression and progression in oesophageal squamous cell carcinoma, and to choroidal neovascularisation in the eye.

For warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are supported only by the TxGNN TxGNN model (deep learning) score (evidence level L5), with no clinical trials. For the top predictions, the available literature either has no connection to lactic acid therapy or points to potential harm (oncology and ocular neovascularisation). Lactic acid has no plausible therapeutic role in structural malformations.

**To proceed, the following is needed:**
- Approved indication, dosage form and route details for the UK authorisation, verified with the MHRA
- Mechanism of action data
- Warnings and contraindications from the SmPC and BNF (a blocking gap for safety screening)
- A credible mechanistic hypothesis and preclinical evidence for any chosen indication before further investment
- Consideration of whether lower-ranked predictions with more biologically plausible links merit review instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

