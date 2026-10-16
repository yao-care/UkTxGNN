---
layout: default
title: Etoposide
parent: Model Prediction Only (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etoposide: predicted new indication Ewing sarcoma (evidence level L5). Approved use: Small cell lung carcinoma and testicular germ cell tumours"
---

# Etoposide
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

# Etoposide: From Small Cell Lung Carcinoma to Ewing Sarcoma

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor, originally used for small cell lung carcinoma and testicular germ cell tumours.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, the highest-ranked prediction with substantial supporting evidence,
with **34 registered clinical trials** and **20 publications** currently supporting this direction.
This is closer to an established, guideline-supported use than a novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small cell lung carcinoma and testicular germ cell tumours (the MHRA indication text is not available in the data compiled for this report; the original indications are taken from the TxGNN knowledge graph) |
| Predicted New Indication | Ewing sarcoma (top-ranked prediction: well-differentiated fetal adenocarcinoma of the lung; Ewing sarcoma is the best-supported) |
| TxGNN Prediction Score | 99.84% for Ewing sarcoma (99.94% for the rank 1 prediction, well-differentiated fetal adenocarcinoma of the lung) |
| Evidence Level | L1 (Ewing sarcoma) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

**Other predictions in brief:**

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Well-differentiated fetal adenocarcinoma of the lung | 99.94% | L4 | Hold |
| Primary pulmonary lymphoma | 99.94% | L4 | Hold |
| Pulmonary blastoma | 99.94% | L4 | Research question |
| **Ewing sarcoma** | **99.85%** | **L1** | **Proceed with Guardrails** |
| Rhabdomyosarcoma | 99.79% | L1 | Proceed with Guardrails |
| Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.80% | L4 | Research question |
| Parameningeal embryonal rhabdomyosarcoma | 99.76% | L4 | Research question |
| Embryonal / extrahepatic bile duct rhabdomyosarcoma; prostate embryonal rhabdomyosarcoma | 99.74–99.76% | L4–L5 | Hold |

The detailed evidence below focuses on Ewing sarcoma, the best-supported prediction. Rhabdomyosarcoma is also well supported and is summarised briefly.

---

## Why is This Prediction Reasonable?

Etoposide is a topoisomerase II inhibitor. It causes DNA double-strand breaks and so kills rapidly dividing tumour cells. Detailed mechanism of action data is not available in the data compiled for this report, but this is the well-recognised pharmacology of the drug.

Etoposide is already used in small cell lung carcinoma and germ cell tumours, which are chemosensitive cancers. Ewing sarcoma is also highly chemosensitive. Laboratory work in the literature notes that Ewing sarcoma cells are particularly sensitive to genotoxic agents such as etoposide, because the EWS-FLI1 fusion causes R-loops and impairs BRCA1-mediated DNA repair.

Ifosfamide plus etoposide is a standard backbone of Ewing sarcoma chemotherapy. Randomised phase 3 trials (including a New England Journal of Medicine study of adding ifosfamide and etoposide to standard therapy) and a consensus guideline support this use. The same combination is active in rhabdomyosarcoma, although etoposide's individual contribution to multi-drug regimens is hard to isolate.

---

## Clinical Trial Evidence (Ewing Sarcoma)

Of 34 registered trials, the most relevant are listed below (all combination regimens, so etoposide's isolated contribution cannot be separated).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: randomised comparison of chemotherapy regimens with or without radiotherapy, surgery or stem cell support in Ewing sarcoma |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Interval-compressed chemotherapy intensification in Ewing sarcoma and related tumours |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to standard 5-drug chemotherapy (including etoposide) in non-metastatic Ewing sarcoma |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification versus standard treatment in non-metastatic Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multi-agent chemotherapy (including etoposide) in metastatic Ewing sarcoma |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | Not stated | EICESS 92: randomised comparison of combination chemotherapy regimens plus surgery and radiotherapy |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | Not stated | Combination chemotherapy including etoposide and ifosfamide, followed by resection and radiotherapy, in peripheral PNET/Ewing sarcoma |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy, radiotherapy and consolidation in metastatic Ewing sarcoma |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Intensive therapy with growth factor support in metastatic Ewing sarcoma/PNET |
| [NCT00014313](https://clinicaltrials.gov/study/NCT00014313) | Phase 2 | Terminated | 3 | Weekly cisplatin with oral etoposide in metastatic Ewing sarcoma/PNET; terminated with very few patients |

---

## Literature Evidence (Ewing Sarcoma)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma/PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (phase 3) | Lancet | EE2012: comparison of two chemotherapy strategies (European versus US standard) in newly diagnosed Ewing sarcoma |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (alternating VDC and ifosfamide-etoposide) in localised Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (phase 3) | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | Euro Ewing 2012 protocol |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus guideline | Cancer | National Ewing Sarcoma Tumor Board consensus recommendations |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management and collaborative approaches in Ewing sarcoma |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Overview of Ewing sarcoma treatment and outcomes |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Retrospective study | Sarcoma | Oral etoposide in 33 adolescent and adult patients with relapsed or refractory Ewing sarcoma |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Laboratory study | Nature | EWS-FLI1 causes R-loops and blocks BRCA1 repair, explaining sensitivity to etoposide |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801040D0AAAAAA (BNF-style code; a PL number is not available) | Etoposide capsules 50 mg | Capsule | Not available in the data compiled for this report |

Only one valid single-ingredient authorisation is recorded, and no cancelled authorisations. Please check the current SmPC for the licensed indications, and note that Ewing sarcoma use may be off-label for this oral formulation.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor, epipodophyllotoxin) |
| Myelosuppression Risk | High (leukopenia, neutropenia and thrombocytopenia are listed among the knowledge-graph contraindications/cautions) |
| Emetogenicity Classification | Low to moderate (oral); please refer to the SmPC |
| Monitoring Items | FBC with differential, liver and renal function |
| Handling Protection | Must follow local cytotoxic drug handling regulations |

---

## Safety Considerations

Product-label warnings and contraindications were not available in the data compiled for this report. The following comes from knowledge-graph drug-disease links and interaction records, not from label text.

- **Conditions flagged in the knowledge graph (caution or contraindication):** thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic anaemia), interstitial lung disease, pulmonary fibrosis, impaired renal function, acidosis/metabolic acidosis, and drug-induced liver injury.
- **Drug interactions (100 recorded; examples):**
  - *Moderate:* aprepitant, rolapitant, metronidazole, tinidazole, eliglustat, rosuvastatin, simvastatin.
  - *Minor:* levofloxacin.
  - *Level unknown:* cimetidine, pantoprazole, doxycycline, amphotericin B, morphine, among others.
- **Additional guardrails from the predictions:** secondary leukaemia risk, and paediatric dose management in Ewing sarcoma and rhabdomyosarcoma.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Ewing sarcoma and rhabdomyosarcoma). **Hold** for the other predictions.

**Rationale:**
- Multiple randomised phase 3 trials and a consensus guideline support ifosfamide-etoposide-based chemotherapy in Ewing sarcoma, giving L1 evidence. This is an established combination-regimen use more than a new discovery, and etoposide's individual contribution cannot be separated from the regimen.
- Rhabdomyosarcoma has similar L1 support. The lung-related predictions (fetal adenocarcinoma, pulmonary lymphoma, pulmonary blastoma) and the site-specific rhabdomyosarcoma subtypes rest on case reports or indirect evidence only, or on no studies at all, and should be treated as research questions.

**To proceed, the following is needed:**
- The full MHRA SmPC (indications, warnings, contraindications), as the product label data was missing
- Mechanism of action data from DrugBank to support the mechanistic analysis
- Confirmation of the licensed route and formulation versus the route used in Ewing sarcoma regimens (the UK record lists oral capsules only, while the trial regimens commonly use intravenous etoposide)
- A myelosuppression monitoring plan and a dosing/DDI management plan, including paediatric and young adult populations
- Review by a specialist sarcoma multidisciplinary team against current NICE and national guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

