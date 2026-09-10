---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cyclophosphamide: From Established Oncology/Immunosuppressive Use to Myeloid Leukaemia

## One-Sentence Summary

Cyclophosphamide is a long-established alkylating agent used across a broad range of haematological and solid malignancies, though the specific original indication text is not recorded in this evidence pack. The TxGNN model predicts it may be effective for **Myeloid Leukaemia**, with **60 clinical trials** and **20 publications** currently identified — though most of this evidence reflects cyclophosphamide's already-established role in leukaemia conditioning and combination chemotherapy regimens rather than a genuinely novel indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory dataset (no licences or original indication text returned) |
| Predicted New Indication | Myeloid Leukaemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 (≥2 completed Phase 2/3 RCTs identified) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on general pharmacological knowledge, cyclophosphamide is an oxazaphosphorine alkylating agent that is metabolically activated in the liver to cytotoxic species which cross-link DNA, halting replication in rapidly dividing cells — a mechanism broadly applicable across haematological malignancies.

The clinical trial evidence gathered for this candidate is dominated by cyclophosphamide's use as a component of myeloablative and reduced-intensity **conditioning regimens** (e.g. busulfan/cyclophosphamide, "BuCy") and as **post-transplant cyclophosphamide (PTCy)** for graft-versus-host disease prophylaxis in patients with acute myeloid leukaemia (AML) undergoing allogeneic haematopoietic stem cell transplantation. This is important context for prescribers: rather than indicating a genuinely new mechanistic hypothesis, the high TxGNN score most likely reflects the fact that cyclophosphamide is already deeply embedded in real-world AML treatment pathways.

Because no original indication text was returned from the source regulatory dataset, it is not possible to formally assess "similarity to original indication" from this evidence pack alone. Clinicians should treat this prediction as a confirmation/consolidation signal for existing practice rather than a repurposing opportunity requiring new clinical development.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03959241](https://clinicaltrials.gov/study/NCT03959241) | Phase 3 | Completed | 431 | BMT CTN 1703: tacrolimus/methotrexate vs post-transplant cyclophosphamide/tacrolimus/MMF for GVHD prophylaxis after reduced-intensity allogeneic PBSC transplant |
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | G-CSF+decitabine+busulfan+cyclophosphamide vs busulfan+cyclophosphamide conditioning for RAEB-1/2 and AML secondary to MDS undergoing allo-HSCT |
| [NCT00186823](https://clinicaltrials.gov/study/NCT00186823) | Phase 3 | Completed | 57 | Haploidentical transplant using purified CD34+ cells for patients with hematologic malignancies (including AML) |
| [NCT02665065](https://clinicaltrials.gov/study/NCT02665065) | Phase 3 | Active, not recruiting | 153 | Iomab-B plus reduced-intensity conditioning vs conventional care in older patients with relapsed/refractory AML |
| [NCT00342316](https://clinicaltrials.gov/study/NCT00342316) | N/A (randomised) | Completed | 340 | Allogeneic transplant with reduced conditioning vs best standard chemotherapy for AML in first complete remission |
| [NCT00002547](https://clinicaltrials.gov/study/NCT00002547) | Phase 2 | Completed | 280 | Allogeneic/syngeneic marrow transplantation following combination chemotherapy for AML/MDS |
| [NCT01010217](https://clinicaltrials.gov/study/NCT01010217) | Phase 2 | Completed | 176 | Three-arm trial (haploidentical, mismatched related/unrelated, MUD) using T-cell replete allograft with high-dose post-transplant cyclophosphamide |
| [NCT00134017](https://clinicaltrials.gov/study/NCT00134017) | Phase 2 | Completed | 142 | HLA-matched related/unrelated BMT with busulfan/cyclophosphamide plus post-transplant cyclophosphamide for hematological malignancies |
| [NCT06532084](https://clinicaltrials.gov/study/NCT06532084) | Phase 2 | Recruiting | 88 | Randomised trial of sorafenib prophylaxis after allo-HSCT with post-transplant bendamustine and cyclophosphamide in high-risk myeloid malignancies |
| [NCT07249346](https://clinicaltrials.gov/study/NCT07249346) | Phase 2 | Recruiting | 124 | Low-dose post-transplant cyclophosphamide/tacrolimus/ruxolitinib for GVHD prophylaxis in myeloablative allogeneic PBSC transplantation |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Retrospective cohort | Haematologica | Genetic risk classification in 217 AML patients undergoing HCT with myeloablative conditioning and PTCy-based GVHD prophylaxis; 2-year OS 77% |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Retrospective cohort | Bone Marrow Transplantation | EBMT analysis of 1,823 AML patients: cytogenetic/molecular risk-driven conditioning intensity with post-transplant cyclophosphamide |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Retrospective cohort | European Journal of Haematology | Impact of conditioning intensity on survival in AML patients receiving ATG and post-transplant cyclophosphamide-based GVHD prophylaxis |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Comparative study | Future Oncology | Busulfan-cyclophosphamide vs fludarabine-busulfan conditioning for allogeneic transplant in AML |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort study | Cytotherapy | Prognostic factors in haploidentical transplantation with post-transplant cyclophosphamide for AML |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohort study | Transplant Immunology | Efficacy and safety of cladribine plus busulfan/cyclophosphamide intensive conditioning in relapsed/refractory AML |
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplantation | Comparison of myeloablative conditioning regimens (including Bu/Cy) in adult AML patients undergoing allo-HSCT in complete remission |
| [36097041](https://pubmed.ncbi.nlm.nih.gov/36097041/) | 2022 | Cohort study | Bone Marrow Transplantation | Non-myeloablative allogeneic transplant with fludarabine and reduced-dose cyclophosphamide in AML for older adults with comorbidities |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort study | International Journal of Molecular Sciences | Post-transplant cyclophosphamide after matched sibling/unrelated donor HSCT in paediatric AML |
| [32857869](https://pubmed.ncbi.nlm.nih.gov/32857869/) | 2020 | Review | American Journal of Hematology | NK cell alloreactivity in AML in the post-transplant cyclophosphamide era |

## UK Market Information

No UK marketing authorisation records were returned for cyclophosphamide in this dataset (0 licences on file; market status recorded as "Not marketed"). This is inconsistent with cyclophosphamide's well-established real-world availability as an oncology/immunosuppressive agent, and most likely reflects a gap in the source regulatory data feed rather than genuine absence from the UK market. Prescribers should verify current authorisation status directly via the MHRA products register and the current BNF entry before acting on this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, oxazaphosphorine/nitrogen mustard class) |
| Myelosuppression Risk | High — dose-limiting neutropenia and thrombocytopenia are well recognised across the conditioning and combination-chemotherapy regimens reviewed above; product-specific toxicity grading was not returned in this query, so please refer to the SmPC |
| Emetogenicity Classification | Moderate to high, dose-dependent (high-dose/conditioning regimens are highly emetogenic) |
| Monitoring Items | Full blood count with differential, renal and liver function, urinalysis (haemorrhagic cystitis risk), electrolytes |
| Handling Protection | Requires handling in accordance with cytotoxic drug handling regulations (e.g. COSHH and NHS cytotoxic reconstitution/administration guidance) |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the clinical trial base for cyclophosphamide in myeloid leukaemia is extensive and includes multiple completed Phase 2/3 RCTs, this evidence overwhelmingly reflects cyclophosphamide's long-established role within AML conditioning and GVHD-prophylaxis regimens rather than a novel repurposing signal. Critically, UK-specific safety labelling data (warnings, contraindications) is a **Blocking** data gap that prevents completion of an initial safety screen (S1), and no UK marketing authorisation record is present in this dataset.

**To proceed, the following is needed:**
- MHRA/SmPC safety data — warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action documentation from DrugBank (High-priority gap, DG002)
- Verification of current UK marketing authorisation status against the MHRA products register
- Clarification of the licensed original indication(s) to properly distinguish "already established use" from a genuine repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

