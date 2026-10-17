---
layout: default
title: Norgestimate
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Norgestimate: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
monitor_inn: "norgestimate"
predicted_indications: ["zinc, elevated plasma"]
---

# Norgestimate
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

# Norgestimate: From Acne and Menopausal Conditions to Elevated Plasma Zinc

## One-Sentence Summary

Norgestimate is a progestin, used in combination with ethinylestradiol, originally associated with acne and with postmenopausal conditions such as osteoporosis and atrophic vaginitis.
The TxGNN model predicts it may be relevant to **elevated plasma zinc**, but there are **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne; postmenopausal osteoporosis; osteoporosis; atrophic vulva; postmenopausal atrophic vaginitis (from the knowledge graph, as no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norgestimate is a progestin that is normally combined with ethinylestradiol in oral contraceptive products.

No established mechanistic link to elevated plasma zinc has been identified. The only support is the high TxGNN knowledge-graph score. Oral contraceptive oestrogens are known to raise serum copper and may modestly alter circulating zinc. This is a general hormonal effect on trace-element binding proteins rather than a documented therapeutic action.

Elevated plasma zinc is also a laboratory finding rather than a disease with a clear treatment target, so the indication itself is questionable. Any apparent link is speculative and unsupported by evidence. Similarity to the original indications has not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0703010G0AAACAC (NHS BNF code) | Ethinylestradiol/Norgestimate tablets 35 micrograms/250 micrograms | Tablet | Not stated |

The product is a single-ingredient-listed authorisation record that is currently valid. BNF classification lies within chapter 7 (obstetrics, gynaecology and urinary-tract disorders), section 7.3.1 (combined hormonal contraceptives), as indicated by the code prefix 0703010. Dosage form and approved indication text were not available in the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are model-derived drug–disease links, not label text, and should be checked against the SmPC):

- Cardiovascular and metabolic: hypertensive disorder, hypertension, diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hypertriglyceridaemia
- Hepatic and biliary: liver disease, gallbladder disease
- Renal: kidney disease, pyoureter, nephrocalcinosis
- Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- Metabolic and endocrine: inherited porphyria, porphyria, porphyrin metabolism disease, hypothyroidism, myxoedema, congenital hypothyroidism, hypercalcaemia, humoral hypercalcaemia of malignancy, phosphorus metabolism disease
- Immunological and respiratory: systemic lupus erythematosus (including paediatric), asthma (intrinsic and allergic)
- Oncological: female breast carcinoma

**Drug Interactions:** 38 interactions were recorded. Major-level interactions among those listed include:

- Sugammadex
- Griseofulvin
- Bexarotene
- Brigatinib
- Dabrafenib
- Encorafenib

Moderate-level interactions include metreleptin, miltefosine, adalimumab, alefacept, anakinra, asparaginase *Escherichia coli*, canakinumab, certolizumab pegol, cladribine, emapalumab, enasidenib and entrectinib. Minor-level interactions include rosuvastatin and ethanol.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no plausible mechanistic link. Elevated plasma zinc is a laboratory finding rather than a treatable disease, so the proposed indication is itself questionable.

**To proceed, the following is needed:**
- Mechanism of action data for norgestimate
- Label warnings and contraindications from the SmPC and BNF, as these are currently missing and block safety screening
- Evidence that elevated plasma zinc is a clinically meaningful treatment target
- Any preclinical or observational data linking norgestimate to zinc handling
- Approved indication text and dosage form for the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

