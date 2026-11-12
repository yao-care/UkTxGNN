---
layout: default
title: Norgestimate
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "norgestimate"
predicted_indications: ["zinc, elevated plasma"]
description: "Norgestimate: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Not recorded in the local data"
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

## Norgestimate: Zinc, elevated plasma
{: .text-alpha }

## One-Sentence Summary

Norgestimate is a progestin, used in combination with ethinylestradiol, originally associated with acne and with postmenopausal conditions such as osteoporosis and atrophic vaginitis.
The TxGNN model predicts it may be relevant to **elevated plasma zinc**, but there are **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norgestimate is a progestin that is normally combined with ethinylestradiol in oral contraceptive products.

No established mechanistic link to elevated plasma zinc has been identified. The only support is the high TxGNN TxGNN model (deep learning) score. Oral contraceptive oestrogens are known to raise serum copper and may modestly alter circulating zinc. This is a general hormonal effect on trace-element binding proteins rather than a documented therapeutic action.

Elevated plasma zinc is also a laboratory finding rather than a disease with a clear treatment target, so the indication itself is questionable. Any apparent link is speculative and unsupported by evidence. Similarity to the original indications has not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0703010G0BFAAAC | Cilest 35microgram/250microgram tablets | Combined ethinylestradiol 35mcg |
| 0703010G0BHAAAC | Cilique 250microgram/35microgram tablets | Combined ethinylestradiol 35mcg |
| 0703010G0AAACAC | Ethinylestradiol 35microgram / Norgestimate 250microgram tab | Combined ethinylestradiol 35mcg |
| 0703010G0BGAAAC | Lizinna 250microgram/35microgram tablets | Combined ethinylestradiol 35mcg |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

BNF classification lies within chapter 7 (obstetrics, gynaecology and urinary-tract disorders), section 7.3.1 (combined hormonal contraceptives), as indicated by the code prefix 0703010. Dosage form and approved indication text were not available in the data compiled for this report.

<!-- review:begin uk-lic-20261106-norgestimate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The product is a single-ingredient-listed authorisation record that is currently valid. BNF classification lies within chapter 7 (obstetrics, gynaecology and urinary-tract disorders), section 7.3.1 (combined hormonal contraceptives), as indicated by the code prefix 0703010." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 4 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-norgestimate-1 -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The product is a single-ingredient-listed authorisation record that is currently valid" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

