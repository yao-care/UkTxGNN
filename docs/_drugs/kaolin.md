---
layout: default
title: Kaolin
parent: Model Prediction Only (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Kaolin: predicted new indication Thrombotic disease (evidence level L5). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Kaolin"
predicted_indications: ["thrombotic disease", "bronchitis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "vein disease", "thrombophilia", "interventricular septum aneurysm", "Jeune syndrome situs inversus", "heart disease"]
---

# Kaolin
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

# Kaolin: From an Unspecified Original Indication to Thrombotic Disease

## One-Sentence Summary

Kaolin is a naturally occurring clay mineral with a single UK product entry (Kaolin Mix), but the data compiled for this report do not record an approved indication for it.
The TxGNN model predicts it may be effective for **thrombotic disease**, yet there are **no registered clinical trials** and the retrieved publications (20) mostly describe kaolin as a laboratory reagent or an experimental haemostatic material.
Kaolin promotes clotting, so the prediction is mechanistically implausible and potentially harmful.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 94.70% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled sources. Based on known information, kaolin is a contact-pathway (factor XII) activator. It is used in vitro in activated partial thromboplastin time (aPTT) tests, lupus anticoagulant tests and kaolin-activated thromboelastography. It is a pro-coagulant, not an antithrombotic.

The high TxGNN score most likely reflects a graph association between kaolin and the coagulation pathway, not a therapeutic relationship. The retrieved literature concerns diagnostic coagulation testing in thrombotic states, not treatment with kaolin. Using a clot-promoting agent to treat thrombosis is mechanistically contradictory and could cause harm.

The same pattern applies to the other predictions. Kaolin dust is a recognised cause of pneumoconiosis (relevant to the "bronchitis" prediction), and kaolin-based products are used topically to stop bleeding. Neither supports a treatment indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved publications are mainly reviews, cohort studies and laboratory studies in which kaolin serves as an assay reagent. None tests kaolin as a treatment for thrombosis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9624740](https://pubmed.ncbi.nlm.nih.gov/9624740/) | 1997 | Review | British Journal of Biomedical Science | Reviews the pathogenesis and laboratory diagnosis of lupus anticoagulant, including the kaolin clotting time. |
| [3931480](https://pubmed.ncbi.nlm.nih.gov/3931480/) | 1985 | Review | American Journal of Obstetrics and Gynecology | Lupus anticoagulant is a marker of fetal wastage and thrombosis risk, identified using the kaolin clotting time. |
| [38142487](https://pubmed.ncbi.nlm.nih.gov/38142487/) | 2024 | Systematic review/meta-analysis | Thrombosis Research | Whole-blood viscoelastic testing and mortality in COVID-19 pneumonia. Diagnostic and prognostic, not therapeutic. |
| [33049490](https://pubmed.ncbi.nlm.nih.gov/33049490/) | 2021 | Systematic review/meta-analysis | Journal of Critical Care | Thromboelastometry/elastography parameters and mortality in sepsis. Diagnostic use only. |
| [38396728](https://pubmed.ncbi.nlm.nih.gov/38396728/) | 2024 | Cohort | International Journal of Molecular Sciences | Thromboelastography markers in COPD exacerbation versus stable phase. |
| [34861681](https://pubmed.ncbi.nlm.nih.gov/34861681/) | 2022 | Cohort | Blood Advances | Altered fibrin clot structure and factor XII consumption contribute to thrombosis risk in severe COVID-19. |
| [28452883](https://pubmed.ncbi.nlm.nih.gov/28452883/) | 2017 | Animal study | Journal of Trauma and Acute Care Surgery | Kaolin-based haemostatic dressing improved bleeding control from inferior vena cava injury in swine. Haemostasis, not thrombosis treatment. |
| [20154537](https://pubmed.ncbi.nlm.nih.gov/20154537/) | 2010 | Animal study | Journal of Trauma | Safety evaluation of kaolin-coated gauze and smectite granules for thromboembolic risk in swine. |
| [6600896](https://pubmed.ncbi.nlm.nih.gov/6600896/) | 1983 | Review | American Review of Respiratory Disease | Kaolin and the lung: occupational dust exposure causes lung disease. A harm signal. |
| [3838315](https://pubmed.ncbi.nlm.nih.gov/3838315/) | 1985 | Basic research | Journal of Biological Chemistry | Heparin cofactor II inhibition of thrombin in plasma activated with kaolin. Laboratory study only. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0104010H0AAABAB (BNF-style product code) | Kaolin Mix | Not recorded | Not recorded |

The compiled data list one valid single-ingredient entry. Dosage form, manufacturer and approved indication are not recorded, so the marketing authorisation details should be checked against the MHRA register and the BNF before any further assessment.

---

## Safety Considerations

- **Drug Interactions**: 84 interactions are recorded in the data compiled for this report. Major interactions include:
  - Dolutegravir
  - Bictegravir

  Moderate interactions include:
  - Tetracycline and doxycycline
  - Bisphosphonates (alendronic acid, risedronic acid, ibandronate)
  - Opioids (codeine, dihydrocodeine, morphine, butorphanol, benzhydrocodone)
  - Allopurinol
  - Atropine
  - Proguanil
  - Baloxavir marboxil

  Minor interactions include the beta-blockers acebutolol, atenolol, betaxolol and bisoprolol. These are consistent with kaolin's ability to adsorb or bind co-administered drugs, so spacing of doses may matter. Only a subset of the 84 interactions is shown here.
- **Occupational and inhalation risk**: The retrieved literature links chronic inhalation of kaolin dust with pneumoconiosis (kaolinosis).
- **Thrombotic risk**: Kaolin is a pro-coagulant contact activator. Intravenous kaolin has been reported to cause coagulation defects (1971 report). Kaolin-based haemostatic products carry a thromboembolic concern in animal studies.

Warnings and contraindications from product labelling are not available in the compiled data. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. No clinical trials exist, and the literature describes kaolin as a diagnostic reagent or topical haemostatic, not as a treatment for thrombosis. A pro-coagulant used to treat thrombotic disease is mechanistically implausible and potentially harmful. The other nine predicted indications (including bronchitis, thrombophilia, heart disease and vein disease) are likewise unsupported at L4 to L5.

**To proceed, the following is needed:**
- Confirmation of the approved indication, dosage form and labelling for the Kaolin Mix product from the MHRA register and BNF
- Mechanism of action data and product warnings and contraindications (currently unavailable)
- A clear mechanistic rationale for any therapeutic effect in the predicted indication, which is not currently apparent
- Pre-clinical or clinical evidence of benefit, none of which currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

