---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 401
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Methotrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Methotrexate: Pulmonary blastoma
{: .text-alpha }

## One-Sentence Summary

Methotrexate is an antifolate medicine originally used for acute lymphoblastic leukaemia, rheumatoid arthritis, psoriasis, mycosis fungoides and non-Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **pulmonary blastoma** (top-ranked prediction), but **no clinical trials and no publications** were found for this specific condition, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (152 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 152 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Methotrexate is generally known as an antifolate that inhibits dihydrofolate reductase (DHFR) and so interferes with DNA synthesis in rapidly dividing cells. It is already used in several haematological and other malignancies, which is why a model that learns from drug-disease networks may extend it to other tumours.

For pulmonary blastoma specifically, the data do not support a specific link. The score appears to reflect a general "antiproliferative drug, malignant lung tumour" signal. Pulmonary blastoma is a very rare lung tumour, and no trials or publications were retrieved.

Other predictions in the same list have more supporting material and may be better starting points for further work:

- **Hodgkin lymphoma** (score 0.9932, evidence level L3): methotrexate-containing VBM (vinblastine, bleomycin, methotrexate) chemotherapy has been used in early-stage disease. However, most of the 44 listed trials are mixed haematological studies in which methotrexate is a supportive or backbone drug, for example graft-versus-host disease prophylaxis.
- **Rhabdomyosarcoma** (score 0.9925, evidence level L3): a phase 2 trial of high-dose methotrexate in children and adolescents with high-risk disease (PMID 9329466) is the closest direct evidence, but it is old and there are no phase 3 data.
- **Primary pulmonary lymphoma** (score 0.9945, evidence level L4): methotrexate is already used in non-Hodgkin lymphoma, so applicability is plausible, but the retrieved literature is mostly case reports and reviews, with no pulmonary-specific trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary blastoma.

---

## Literature Evidence

Currently no related literature available for pulmonary blastoma.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1001030U0AAACAC | Methotrexate 10mg tablets | Methotrexate |
| 1001030U0AACECE | Methotrexate 10mg/0.2ml inj pre-filled disposable devices | Methotrexate |
| 1001030U0AABFBF | Methotrexate 10mg/0.2ml inj pre-filled syringes | Methotrexate |
| 0801030P0AAFNFN | Methotrexate 10mg/0.4ml inj pre-filled disposable devices | Methotrexate |
| 0801030P0AAFHFH | Methotrexate 10mg/0.4ml inj pre-filled syringes | Methotrexate |
| 1001030U0AABBBB | Methotrexate 10mg/1ml inj pre-filled syringes | Methotrexate |
| 1001030U0AAAHAH | Methotrexate 10mg/5ml oral liquid | Methotrexate |
| 1001030U0AACDCD | Methotrexate 12.5mg/0.25ml inj pre-filled disposable devices | Methotrexate |
| 1001030U0AABKBK | Methotrexate 12.5mg/0.25ml inj pre-filled syringes | Methotrexate |
| 0801030P0AAFPFP | Methotrexate 12.5mg/0.5ml inj pre-filled disposable devices | Methotrexate |
| 0801030P0AAFJFJ | Methotrexate 12.5mg/0.5ml inj pre-filled syringes | Methotrexate |
| 1001030U0AAAKAK | Methotrexate 12.5mg/5ml oral liquid | Methotrexate |
| 1001030U0AAASAS | Methotrexate 12mg/5ml oral liquid | Methotrexate |
| 1001030U0AACCCC | Methotrexate 15mg/0.3ml inj pre-filled disposable devices | Methotrexate |
| 1001030U0AABGBG | Methotrexate 15mg/0.3ml inj pre-filled syringes | Methotrexate |
| 0801030P0AAFQFQ | Methotrexate 15mg/0.6ml inj pre-filled disposable devices | Methotrexate |
| 0801030P0AAFKFK | Methotrexate 15mg/0.6ml inj pre-filled syringes | Methotrexate |
| 1001030U0AABCBC | Methotrexate 15mg/1.5ml inj pre-filled syringes | Methotrexate |
| 1001030U0AAARAR | Methotrexate 15mg/5ml oral liquid | Methotrexate |
| 1001030U0AABVBV | Methotrexate 17.5mg/0.35ml inj pre-filled disposable devices | Methotrexate |

Showing 20 of 152 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier shown is as recorded in the data and is not in the usual PL number format, so it should be verified against the MHRA register. Please check the current SmPC and BNF for the authorised indications and dosing.

<!-- review:begin uk-lic-20261106-methotrexate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Only one single-ingredient authorisation is recorded, and it is currently valid. The identifier shown is as recorded in the data and is not in the usual PL number format, so it should be verified against the MHRA register." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 152 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-methotrexate-1 -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, antifolate class) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (the knowledge graph lists leukopenia, thrombocytopenia and anaemia as contraindicated conditions, which is consistent with a marrow-suppression risk) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions (typically FBC, liver and renal function) |
| Handling Protection | Please refer to the SmPC warnings and precautions; follow local cytotoxic drug handling policy |

---

## Safety Considerations

- **Contraindicated conditions (knowledge graph, not label text):** liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, leukopenia, anaemia (including macrocytic anaemia), peptic ulcer disease and gastric ulcer, ulcerative colitis, inflammatory bowel disease, stomatitis, interstitial lung disease, pulmonary fibrosis (including postinflammatory), immune system disease, substance abuse/dependence, and pyoureter. These come from drug-disease network edges and must be checked against the SmPC.
- **Drug interactions:** 100 interactions were recorded. The examples listed in the data compiled include the following.
  - **Major:** rabeprazole, amoxicillin, acetylsalicylic acid.
  - **Moderate:** acarbose, doxycycline, tetracycline, clarithromycin, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, mesalazine, balsalazide, pioglitazone, amphotericin B, bupropion, chenodeoxycholic acid.
  - **Minor:** potassium citrate.
- **Literature signal:** methotrexate-associated lymphoproliferative disorders have been reported in patients treated for rheumatoid arthritis.

Label warnings and contraindications were not available in the data compiled. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary blastoma prediction has a high model score (0.9945) but no trials, no publications and no mechanistic evidence specific to this tumour (evidence level L5). Methotrexate is also a high-toxicity cytotoxic drug, so a prediction alone is not enough to justify progression.

**To proceed, the following is needed:**
- Detailed mechanism of action data for methotrexate, and a tumour-specific rationale for pulmonary blastoma.
- A targeted literature search, including case series, for methotrexate in pulmonary blastoma.
- SmPC and BNF warnings, contraindications and approved indication text for the UK authorisation (these are currently missing).
- Consideration of whether Hodgkin lymphoma or rhabdomyosarcoma, which have more supporting evidence, should be prioritised over this prediction.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Only one single-ingredient authorisation is recorded, and it is currently valid" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

