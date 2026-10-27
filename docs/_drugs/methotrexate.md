---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). Approved use: Acute lymphoblastic leukaemia, rheumatoid arthritis, psoriasis…"
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Methotrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Methotrexate: From Acute Lymphoblastic Leukaemia to Pulmonary Blastoma
{: .text-alpha }

## One-Sentence Summary

Methotrexate is an antifolate medicine originally used for acute lymphoblastic leukaemia, rheumatoid arthritis, psoriasis, mycosis fungoides and non-Hodgkin lymphoma.
The TxGNN model predicts it may be effective for **pulmonary blastoma** (top-ranked prediction), but **no clinical trials and no publications** were found for this specific condition, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukaemia, rheumatoid arthritis, psoriasis, non-Hodgkin lymphoma and related conditions (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Methotrexate is generally known as an antifolate that inhibits dihydrofolate reductase (DHFR) and so interferes with DNA synthesis in rapidly dividing cells. It is already used in several haematological and other malignancies, which is why a model that learns from drug-disease networks may extend it to other tumours.

For pulmonary blastoma specifically, the data do not support a specific link. The score appears to reflect a general "antiproliferative drug, malignant lung tumour" signal. Pulmonary blastoma is a very rare lung tumour, and no trials or publications were retrieved.

Other predictions in the same list have more supporting material and may be better starting points for further work:

- **Hodgkin lymphoma** (score 99.32%, evidence level L3): methotrexate-containing VBM (vinblastine, bleomycin, methotrexate) chemotherapy has been used in early-stage disease. However, most of the 44 listed trials are mixed haematological studies in which methotrexate is a supportive or backbone drug, for example graft-versus-host disease prophylaxis.
- **Rhabdomyosarcoma** (score 99.25%, evidence level L3): a phase 2 trial of high-dose methotrexate in children and adolescents with high-risk disease (PMID 9329466) is the closest direct evidence, but it is old and there are no phase 3 data.
- **Primary pulmonary lymphoma** (score 99.45%, evidence level L4): methotrexate is already used in non-Hodgkin lymphoma, so applicability is plausible, but the retrieved literature is mostly case reports and reviews, with no pulmonary-specific trial.
- **Small cell lung carcinoma** (score 99.43%, evidence level L4): methotrexate featured in older SCLC combination regimens, but the retrieved trials concern non-small cell lung cancer.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary blastoma.

---

## Literature Evidence

Currently no related literature available for pulmonary blastoma.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001030U0AAABAB | Methotrexate tablets 2.5 mg | Tablet (not specified in the data) | Not available in the data compiled |

Only one single-ingredient authorisation is recorded, and it is currently valid. The identifier shown is as recorded in the data and is not in the usual PL number format, so it should be verified against the MHRA register. Please check the current SmPC and BNF for the authorised indications and dosing.

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
The pulmonary blastoma prediction has a high model score (99.45%) but no trials, no publications and no mechanistic evidence specific to this tumour (evidence level L5). Methotrexate is also a high-toxicity cytotoxic drug, so a prediction alone is not enough to justify progression.

**To proceed, the following is needed:**
- Detailed mechanism of action data for methotrexate, and a tumour-specific rationale for pulmonary blastoma.
- A targeted literature search, including case series, for methotrexate in pulmonary blastoma.
- SmPC and BNF warnings, contraindications and approved indication text for the UK authorisation (these are currently missing).
- Consideration of whether Hodgkin lymphoma or rhabdomyosarcoma, which have more supporting evidence, should be prioritised over this prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

