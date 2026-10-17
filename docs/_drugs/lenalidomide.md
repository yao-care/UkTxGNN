---
layout: default
title: Lenalidomide
parent: High Evidence (L1-L2)
nav_order: 365
evidence_level: L2
indication_count: 6
last_modified_at: 2026-10-15
description: "Lenalidomide: predicted new indication Myeloid leukaemia (evidence level L2). Approved use: Plasma cell myeloma, mantle cell lymphoma, B-cell neoplasm…"
monitor_inn: "Lenalidomide"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "partial deletion of the long arm of chromosome 5"]
---

# Lenalidomide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **6** 
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

# Lenalidomide: From Plasma Cell Myeloma to Myeloid Leukaemia

## One-Sentence Summary

Lenalidomide is an oral immunomodulatory drug, originally used for plasma cell myeloma, mantle cell lymphoma and myelodysplastic syndrome (MDS).
The TxGNN model predicts it may be effective for **myeloid leukaemia**,
with **45 clinical trials** (mostly Phase 1/2) and **19 publications** (mainly reviews) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma, mantle cell lymphoma, B-cell neoplasm, lymphosarcoma, myelodysplastic syndrome (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Myeloid leukaemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L2 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lenalidomide is a cereblon E3 ligase modulator. It promotes degradation of the transcription factors IKZF1 and IKZF3, and of CK1α, which drives its activity in del(5q) MDS. It also activates natural killer (NK) and T cells and has anti-angiogenic effects. Detailed mechanism of action data were not available in the data compiled for this report, so this description is based on the mechanistic rationale assessed for the prediction.

Myeloid leukaemia, including acute myeloid leukaemia (AML), is biologically close to MDS, where lenalidomide is already established. MDS frequently progresses to AML, and the same pathways (cereblon-mediated degradation, immune activation) could plausibly act in myeloid malignancies.

Activity in AML without del(5q) is likely to be modest. The most sensible approaches are combination with hypomethylating agents (such as azacitidine) or chemotherapy, or use as post-remission maintenance.

---

## Clinical Trial Evidence

The data include 45 registered trials for this prediction. The 10 most relevant are listed below. The only Phase 3 trials found are NCT00843882 (an MDS trial) and NCT04490707 (AML, status unknown). No completed Phase 3 trial specifically in myeloid leukaemia was identified.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML in remission |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | Completed | 27 | Single-agent lenalidomide in relapsed/refractory AML or high-risk MDS with chromosome 5 abnormalities |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | Completed | 37 | Lenalidomide plus azacitidine in advanced MDS |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Phase 1/2 | Completed | 51 | Idarubicin and cytarabine followed by lenalidomide in RAEB-2 MDS or untreated AML; supports feasibility |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | Lenalidomide, sequential azacitidine plus lenalidomide, or azacitidine alone in older patients with newly diagnosed AML |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | Completed | 120 | Alternating lenalidomide and azacitidine maintenance in first remission in elderly AML |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2/3 | Active, not recruiting | 282 | Azacitidine with lenalidomide or vorinostat versus azacitidine alone in higher-risk MDS and CMML |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Phase 2 | Completed | 41 | Lenalidomide in older patients with untreated del(5q) AML who declined induction chemotherapy |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | Unknown | 60 | Azacitidine plus lenalidomide maintenance guided by MRD in elderly or unfit AML patients |
| [NCT01254578](https://clinicaltrials.gov/study/NCT01254578) | Phase 1 | Completed | 17 | Lenalidomide maintenance after allogeneic transplant in high-risk haematological malignancies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32899586](https://pubmed.ncbi.nlm.nih.gov/32899586/) | 2020 | Review | Cancers | Immunomodulatory drugs in AML treatment |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide as a novel AML treatment; approved in del(5q) MDS, trials ongoing in higher-risk MDS and AML |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Preclinical | Cell Mol Biol Lett | KDM5C stabilises cereblon and increases the sensitivity of AML cells to lenalidomide |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS update on diagnosis, risk stratification and management |
| [42400116](https://pubmed.ncbi.nlm.nih.gov/42400116/) | 2026 | Review | Am J Hematol | 2026 update on MDS diagnosis, risk stratification and management |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making and treatment of MDS |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | Review | Blood Cancer J | Current MDS treatment algorithm |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Overview of MDS, including progression to AML |
| [17488990](https://pubmed.ncbi.nlm.nih.gov/17488990/) | 2007 | Review | J Clin Oncol | AML and MDS in older patients |
| [22483153](https://pubmed.ncbi.nlm.nih.gov/22483153/) | 2012 | Review | Curr Cancer Drug Targets | Novel and emerging drugs for AML |

No randomised controlled trial publication specific to myeloid leukaemia was identified in the data compiled for this report.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0802040Y0AAADAD (BNF-style code) | Lenalidomide capsules 25 mg | Capsule (stated in product name) | Not available in the data compiled |

One single-ingredient authorisation is recorded as valid. The record carries a BNF-style code rather than a standard MHRA PL number, and no approved indication text or manufacturer is listed. Verify the PL number and indications against the MHRA record, the SmPC and NICE appraisals before use.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunomodulatory agent (thalidomide analogue; not a conventional cytotoxic) |
| Myelosuppression Risk | High; neutropenia and thrombocytopenia are well-recognised (knowledge-graph contraindication data list thrombocytopenia, neutropenia and agranulocytosis) |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count with differential, renal function; please refer to the SmPC warnings and precautions for the full schedule |
| Handling Protection | Please refer to the SmPC; lenalidomide is teratogenic, so pregnancy prevention requirements and careful capsule handling apply |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for these.

- **Knowledge-graph contraindication signals** (not label text): thrombocytopenia, neutropenia, agranulocytosis, pulmonary embolism, impaired renal function, cancer and embryoma.
- **Drug Interactions**: 100 potential interactions were identified. Those rated Major are **rosuvastatin** and **simvastatin**. Those rated Moderate are **eliglustat** and **naltrexone**. Many others (for example metformin, omeprazole, prednisone, morphine) have no severity grading.

Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials, mostly combination or maintenance studies in AML and high-risk MDS, together with an established MDS indication, support biological plausibility (Evidence Level L2). However, the trials are small and largely single-arm, and activity outside del(5q) disease is likely modest, so use should stay within a research setting.

**To proceed, the following is needed:**
- Randomised, adequately powered trials in myeloid leukaemia, ideally in combination with azacitidine or as post-remission maintenance
- Confirmation of MHRA authorisation details and approved indications for the UK product
- Label-based warnings and contraindications from the SmPC, and a review of the statin interactions
- A haematological monitoring plan (myelosuppression) and adherence to pregnancy prevention requirements
- Detailed mechanism of action data

---

### Note on Other Predictions

The other predicted indications are weaker and should not be prioritised:
- **Unclassified myelodysplastic syndrome** (99.43%, L3): relevance depends on del(5q); evidence is cohort and case-level only; research question.
- **Refractory cytopenia of childhood** (99.35%, L3): one Phase 1 paediatric safety study; research question.
- **Aregenerative anaemia** (99.32%, L3): indirect evidence only; research question.
- **Severe congenital hypochromic anaemia with ringed sideroblasts** (99.28%, L5) and **partial deletion of the long arm of chromosome 5** (99.27%, L5): no supporting trials or literature, likely mapping artefacts; hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

