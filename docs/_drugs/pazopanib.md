---
layout: default
title: Pazopanib
parent: Model Prediction Only (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pazopanib: predicted new indication Renal cell carcinoma associated with neuroblastoma (evidence level L5). Approved use: Renal cell carcinoma and soft tissue sarcoma"
monitor_inn: "Pazopanib"
predicted_indications: ["ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
---

# Pazopanib
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

# Pazopanib: From Renal Cell Carcinoma and Soft Tissue Sarcoma to Renal Cell Carcinoma Subtypes

## One-Sentence Summary

Pazopanib is a multi-targeted tyrosine kinase inhibitor, originally used for renal cell carcinoma and soft tissue sarcoma.
The TxGNN model gives its highest prediction score to **renal cell carcinoma associated with neuroblastoma**, but this subtype has no supporting studies. The best-supported prediction in the data is **unclassified renal cell carcinoma**, with **6 publications** (including one Phase 2 study) and no registered trials. The predicted indication with the most trial evidence is **liposarcoma**, with **6 clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma and soft tissue sarcoma (from the knowledge-graph indication data; the UK authorisation record has no indication text) |
| Predicted New Indication | Renal cell carcinoma associated with neuroblastoma (top-ranked prediction) |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 for the top-ranked prediction (model prediction only). Other predictions range from L2 to L5 (see below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold for the top-ranked prediction. Research Question for liposarcoma, unclassified RCC, fibroblastic neoplasm and DFSP |

**Summary of the ten predicted indications**

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Renal cell carcinoma associated with neuroblastoma | 99.63% | L5 | Hold |
| 2 | Unclassified renal cell carcinoma | 99.63% | L3 | Research Question |
| 3 | RCC with Xp11.2 translocation/TFE3 fusion | 99.63% | L5 | Hold |
| 4 | Liposarcoma | 99.59% | L2 | Research Question |
| 5 | Childhood kidney cell carcinoma | 99.54% | L5 | Hold |
| 6 | Ovarian myxoid liposarcoma | 99.51% | L5 | Hold |
| 7 | Heart fibrosarcoma | 99.37% | L5 | Hold |
| 8 | Fibroblastic neoplasm | 99.35% | L2 | Research Question |
| 9 | Kidney fibrosarcoma | 99.33% | L5 | Hold |
| 10 | Dermatofibrosarcoma protuberans (DFSP) | 99.29% | L2 | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, pazopanib inhibits VEGFR, PDGFR and c-Kit, which drive tumour blood vessel growth and cell proliferation. Its efficacy in renal cell carcinoma and non-adipocytic soft tissue sarcoma is established.

Most of the high-scoring predictions are extensions of these two approved areas. The renal subtypes (unclassified RCC, TFE3-fusion RCC, childhood kidney carcinoma) probably score highly because of their link to the parent RCC indication. Non-clear-cell and unclassified tumours are less dependent on VEGF than clear-cell disease. The single-arm Phase 2 study and retrospective series nevertheless show activity.

For the sarcoma-related predictions, the rationale differs by histology:
- **Liposarcoma:** Adipocytic tumours were excluded from the pivotal Phase 3 sarcoma trial because of lower activity. Dedicated Phase 2 data are modest and results are mixed.
- **Fibroblastic neoplasm:** PDGFR and VEGFR signalling is implicated in solitary fibrous tumour and desmoid-type fibromatosis, and Phase 2 data exist in solitary fibrous tumour.
- **DFSP:** The COL1A1-PDGFB fusion drives constitutive PDGFR signalling, which pazopanib inhibits. This gives a strong mechanistic rationale, particularly for imatinib-resistant disease.

The very rare site-specific predictions (ovarian myxoid liposarcoma, heart fibrosarcoma, kidney fibrosarcoma) and the RCC subtypes associated with neuroblastoma, Xp11.2/TFE3 fusion and childhood onset have no supporting studies in the data. They are most likely propagated from the broader RCC and sarcoma associations.

---

## Clinical Trial Evidence

The table below shows trials for **liposarcoma**, the prediction with the most direct trial evidence. No registered trials were found for the top-ranked prediction or for unclassified RCC.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable or metastatic liposarcoma. Most direct evidence |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib in relapsed advanced or metastatic liposarcoma, assessing activity and tolerability |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Randomised, double-blind comparison of gemcitabine with or without pazopanib in refractory soft tissue sarcoma |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib plus oral topotecan in metastatic or non-resectable soft tissue and bone sarcomas |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Completed | 140 | Neoadjuvant pazopanib with radiation therapy, with or without chemotherapy, in non-rhabdomyosarcoma soft tissue sarcoma. Not liposarcoma-specific |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Risk-adapted study including maintenance pazopanib in paediatric non-rhabdomyosarcoma soft tissue sarcoma |

**Other predicted indications with trials:**

| Trial Number | Indication | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) | Fibroblastic neoplasm | Phase 2 | Completed | 96 | Single-agent pazopanib 800 mg daily in unresectable or metastatic solitary fibrous tumour and extraskeletal myxoid chondrosarcoma |
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | DFSP | Phase 2 | Terminated | 23 | Pazopanib in unresectable, locally advanced DFSP. Terminated early, so evidence is limited |
| [NCT02601209](https://clinicaltrials.gov/study/NCT02601209) | DFSP | Phase 1/2 | Terminated | 151 | TAK-228 (sapanisertib) versus pazopanib in advanced sarcoma. DFSP is at most a small subset |

NCT02180867 (fibroblastic neoplasm and DFSP) and NCT06239272 (DFSP) also appear under other predictions.

---

## Literature Evidence

**Unclassified renal cell carcinoma (rank 2)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2 (single-arm) | Cancer Res Treat | Open-label multicentre study of the efficacy and safety of pazopanib in non-clear-cell RCC |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Italian PANORAMA study of first-line pazopanib efficacy and toxicity in non-clear-cell RCC |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clin Genitourin Cancer | Outcomes of pazopanib in metastatic non-clear-cell RCC |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world study | Ecancermedicalscience | Compares sunitinib and pazopanib first-line in non-clear-cell and sarcomatoid RCC |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospective cohort | Eur Urol Oncol | IMDC real-world comparison of contemporary and traditional first-line therapies in non-clear-cell RCC |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Cohort | Clin Genitourin Cancer | Carcinoma of unknown primary with RCC features treated with targeted therapy |

**Liposarcoma (rank 4)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 | Expert Opin Investig Drugs | Pazopanib in advanced intermediate- or high-grade liposarcoma |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 | Br J Cancer | Pazopanib with oral topotecan in metastatic soft tissue and bone sarcomas |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncol Res Treat | Established and experimental systemic options for advanced liposarcoma |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Curr Treat Options Oncol | Systemic therapy options for dedifferentiated liposarcoma |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Commentary | Lancet Oncol | Pazopanib for advanced liposarcoma |

**Fibroblastic neoplasm (rank 8)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25269954](https://pubmed.ncbi.nlm.nih.gov/25269954/) | 2014 | Preclinical and clinical | Eur J Cancer | Preclinical and clinical activity of pazopanib in solitary fibrous tumour |
| [29614488](https://pubmed.ncbi.nlm.nih.gov/29614488/) | 2018 | Retrospective | Oncology | Efficacy and safety of pazopanib in recurrent or metastatic solitary fibrous tumour |
| [38759389](https://pubmed.ncbi.nlm.nih.gov/38759389/) | 2024 | Multicentre real-world | Eur J Cancer | Real-world use of pazopanib and sorafenib in desmoid tumours |
| [41791137](https://pubmed.ncbi.nlm.nih.gov/41791137/) | 2026 | Retrospective series | Clin Neurol Neurosurg | Pazopanib for recurrent CNS solitary fibrous tumours |

**Dermatofibrosarcoma protuberans (rank 10)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | 2021 | Phase 2 | J Invest Dermatol | Multicentre Phase 2 study of pazopanib in unresectable DFSP |
| [34066400](https://pubmed.ncbi.nlm.nih.gov/34066400/) | 2021 | Retrospective | Cancers | Long-term outcomes of neoadjuvant imatinib or pazopanib followed by surgery in locally advanced DFSP |
| [37592448](https://pubmed.ncbi.nlm.nih.gov/37592448/) | 2023 | Preclinical | Cancer Sci | Pazopanib identified as a potential inhibitor of the COL1A1-PDGFB fusion gene |
| [27988943](https://pubmed.ncbi.nlm.nih.gov/27988943/) | 2017 | Case report | J Dermatol | Partial response to pazopanib in metastatic fibrosarcomatous DFSP |

No literature was supplied for the other six predictions.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801050AZAAABAB (BNF-style product code, not a PL number) | Pazopanib tablets 400 mg | Tablet | Indication text not available in the data compiled for this report |

One valid single-ingredient authorisation is recorded. Please check the current SmPC and NICE appraisals for the licensed indications.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC. Liver function, blood pressure, thyroid function and ECG/electrolytes are suggested by the contraindication and interaction data below |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

SmPC warnings and contraindications were not available in the data compiled for this report.

- **Conditions flagged in the knowledge graph (not label text):**
  - Cardiovascular: hypertension, long QT syndrome (including familial), torsades de pointes, myocardial infarction, coronary thrombosis.
  - Liver: liver failure, drug-induced liver injury, hyperbilirubinaemia (including Gilbert syndrome).
  - Endocrine and metabolic: hypothyroidism, potassium deficiency, hypercalcaemia, phosphorus metabolism disorders.
  - Bleeding and gastrointestinal: intracerebral haemorrhage, active peptic ulcer disease, pancreatitis, diarrhoeal disease.
  - Kidney and blood: proteinuria, nephrocalcinosis, haemoglobinopathy.
- **Drug interactions:** 100 interactions were recorded. Those listed below are from the first 20 entries, so the list is not exhaustive.
  - **Major:** acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole), clarithromycin, and dolasetron.
  - **Moderate:** pioglitazone, saxagliptin, loperamide, aprepitant, dexamethasone, budesonide, bisacodyl, magnesium oxide, polyethylene glycol with electrolytes, and eliglustat.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (renal cell carcinoma associated with neuroblastoma) and other predictions with no supporting studies. **Research Question** for liposarcoma, unclassified RCC, fibroblastic neoplasm and DFSP.

**Rationale:**
- The top three scores (99.63%) are driven by model propagation from the approved RCC indication, and the top-ranked entity has no trials or publications (L5).
- The most credible leads are subtype extensions with Phase 2 data:
  - Unclassified RCC (L3): a single-arm Phase 2 study and retrospective series.
  - DFSP (L2): a dedicated Phase 2 study with a strong mechanistic basis, though imatinib remains the standard.
  - Fibroblastic neoplasm (L2): Phase 2 data in solitary fibrous tumour.
  - Liposarcoma (L2): Phase 2 results that are modest and histology-dependent.
- None of these meets the L1 standard of at least two completed Phase 3 RCTs.

**To proceed, the following is needed:**
- Mechanism of action data, and SmPC warnings and contraindications (the safety data gap is flagged as blocking for safety screening).
- Approved indication text and PL numbers for the UK authorisation, to confirm what is already licensed.
- Appraisal of the DFSP and unclassified RCC Phase 2 data against current standard therapies (imatinib for DFSP; established first-line options for non-clear-cell RCC).
- A cardiovascular, hepatic and interaction monitoring plan, particularly for QT-prolonging and acid-suppressing co-medications.
- Review of NICE guidance and local sarcoma or renal multidisciplinary team input before any off-label use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

