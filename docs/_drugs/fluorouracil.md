---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluorouracil: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Not stated in the UK authorisation record. Knowledge-graph indication…"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-beta-thalassemia disease syndrome"]
---

# Fluorouracil
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

# Fluorouracil: From Gastric Cancer and Skin Conditions to Rhabdomyosarcoma

## One-Sentence Summary

Fluorouracil is an antimetabolite chemotherapy, originally used for conditions such as superficial basal cell carcinoma, actinic keratosis, colorectal metastases, pancreatic adenocarcinoma and gastric cancer.
The TxGNN model predicts it may be effective for **rhabdomyosarcoma**, with the top-ranked prediction being botryoid-type embryonal rhabdomyosarcoma of the vagina.
Evidence is very weak: **no clinical trials** and only **4 publications** (mostly old, indirect reports) for the main rhabdomyosarcoma prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation record. Knowledge-graph indications include superficial multifocal basal cell carcinoma, actinic keratosis, metastatic colon cancer, pancreatic adenocarcinoma and gastric cancer |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina (rank 1); the broader disease, rhabdomyosarcoma, is rank 2 and is the only rhabdomyosarcoma entry with literature |
| TxGNN Prediction Score | 99.75% (rank 1); 99.74% for rhabdomyosarcoma |
| Evidence Level | L5 for the rank 1 prediction (model prediction only); L4 for rhabdomyosarcoma |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fluorouracil is a thymidylate synthase inhibitor and antimetabolite that disrupts DNA and RNA synthesis in rapidly dividing cells. Its efficacy in gastrointestinal and skin malignancies is established, and mechanistically it may be applicable to other highly proliferative tumours.

Rhabdomyosarcoma is a fast-growing paediatric soft tissue sarcoma, so an antimetabolite is plausible in principle. However, fluorouracil is not a standard agent in rhabdomyosarcoma regimens, which typically use vincristine, actinomycin D and cyclophosphamide. The high TxGNN scores for several rhabdomyosarcoma subtypes (vaginal, parameningeal, prostate, bile duct) probably reflect a shared disease cluster in the knowledge graph rather than independent evidence.

The remaining predictions are weaker still. For sickle cell-haemoglobin C disease and related syndromes, the only rationale is speculative fetal haemoglobin induction (analogous to hydroxyurea). Fluorouracil's myelosuppression makes this a poor risk-benefit proposition when established alternatives exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications relating to rhabdomyosarcoma (rank 2):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Rep Oncol Med | Young adult with lingual rhabdomyosarcoma. Cisplatin plus 5-fluorouracil was given as second-line therapy and the disease progressed; a later vincristine/actinomycin D-based regimen was used. Does not support fluorouracil benefit |
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Adjuvant chemotherapy for childhood sarcomas, including rhabdomyosarcoma. General multi-agent overview; fluorouracil's contribution cannot be isolated |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | Overview of curable cancers with chemotherapy, including childhood rhabdomyosarcoma. Indirect |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | Childhood nasopharyngeal carcinoma series. Different tumour type; of limited relevance |

For extrahepatic bile duct rhabdomyosarcoma (rank 6), the one supplied item, [83901](https://pubmed.ncbi.nlm.nih.gov/83901/) (1978, Can J Surg), concerns bile duct carcinoma, a different histology. For liver sarcoma (rank 7), the retrieved literature is mostly colorectal cancer reviews and animal or laboratory studies, with no clear fluorouracil-specific effect in sarcoma.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1308010Y0AAAAAA | Fluorouracil cream 5% | Not stated | Not stated |

One valid single-ingredient authorisation is recorded. Dosage form and approved indication details were not available, so please check the current MHRA record, the SmPC and the BNF.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. Knowledge-graph links to neutropenia, leukopenia, thrombocytopenia and agranulocytosis indicate this is a relevant concern |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Full blood count, liver and renal function; consider DPD status before systemic use |
| Handling Protection | Follow local cytotoxic drug handling policies for systemic preparations |

---

## Safety Considerations

- **Contraindications and cautions (knowledge-graph links, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, diarrhoeal disease, active peptic ulcer disease, pharyngitis, stomatitis, and dihydropyrimidine dehydrogenase (DPD) deficiency.
- **Drug Interactions**: 100 interactions were identified. Those with a stated severity:
  - Moderate: metronidazole, tinidazole
  - Minor: cimetidine, levofloxacin
  - Other listed interactions (for example omeprazole, pantoprazole, lansoprazole, metformin, morphine) have no severity grading.

Label warnings were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest almost entirely on model scores. There are no registered trials, and the limited literature is old, indirect or shows no fluorouracil benefit in rhabdomyosarcoma. Fluorouracil is not part of standard rhabdomyosarcoma treatment, and its toxicity makes the sickle cell predictions unattractive.

**To proceed, the following is needed:**
- A systematic search for fluorouracil-specific rhabdomyosarcoma data (preclinical and clinical), including screening the full set of liver sarcoma records
- Mechanism of action data and SmPC warnings and contraindications
- Comparison against standard rhabdomyosarcoma regimens to define any plausible role
- A UK route and formulation assessment, since the only recorded authorisation is a 5% cream
- A DPD deficiency testing and myelosuppression monitoring plan for any systemic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

