---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 5
---

# Cabergoline
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

# Cabergoline: From Hyperprolactinaemia to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a selective dopamine D2 receptor agonist with well-established clinical use in hyperprolactinaemia and prolactinoma management. The TxGNN model predicts it may have activity against **Pituitary Adenocarcinoma** (Rank 1, score 99.06%), though direct evidence is extremely limited, with **0 clinical trials** and only **3 publications** — none of which specifically address adenocarcinoma. A closely related prediction, **Pituitary Cancer** (Rank 3), is substantially better supported by **20 clinical trials** and **20 publications**, predominantly within pituitary adenoma management.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack (see note below) |
| Predicted New Indication | Pituitary Adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| UK Market Status | Not currently listed in Evidence Pack (requires MHRA register verification) |
| Number of Marketing Authorisations | 0 (as per current Evidence Pack data) |
| Recommended Decision | Hold |

> **Note on Original Indication:** No formal indication data was populated in this Evidence Pack. Based on established pharmacological knowledge and the clinical trial evidence retrieved, cabergoline is primarily used for hyperprolactinaemia, prolactinoma, and select other pituitary tumour subtypes. Verification against the MHRA SmPC and BNF section 6.7.1 is recommended.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, cabergoline is a selective dopamine D2 receptor agonist. It suppresses prolactin secretion from lactotroph cells of the anterior pituitary and, crucially, has demonstrated direct antitumour activity in prolactinomas — causing measurable tumour shrinkage. Corticotroph adenomas have been shown in vitro to express D2 receptors, providing a theoretical basis for suppressing ACTH-secreting pituitary tumours; this formed the rationale for the completed Phase 3 trial NCT00889525. A 2020 review (PMID 31597135) further identifies novel mechanisms including autophagy induction and autophagic cell death as contributors to cabergoline's antitumour action.

The TxGNN prediction for pituitary adenocarcinoma rests on this D2-receptor-mediated antitumour mechanism. However, a critical pathological distinction must be emphasised: **pituitary adenocarcinoma is not the same as pituitary adenoma**. Adenocarcinoma is defined specifically by the presence of craniospinal or systemic metastases, accounts for fewer than 200 documented cases globally, and exhibits aggressive biology that is poorly responsive to conventional dopamine agonist therapy. There is no direct preclinical or clinical evidence that cabergoline can overcome the dedifferentiation and metastatic biology characteristic of true pituitary carcinoma.

Of the three publications retrieved for this specific indication, PMID 20497940 concerns long-term management of ectopic ACTH hypersecretion (not adenocarcinoma), PMID 33569966 is an unrelated pancreatic adenocarcinoma case with no mechanistic connection to pituitary pathology (likely a data retrieval artefact), and PMID 41760078 addresses MEN1 syndrome with only indirect relevance. The high TxGNN score of 99.06% most likely reflects knowledge graph proximity between pituitary adenoma nodes and the broader "pituitary neoplasm" ontology category, rather than genuine adenocarcinoma-specific evidence.

---

## Clinical Trial Evidence

No clinical trials are currently registered specifically for cabergoline in pituitary adenocarcinoma.

> **Contextual Note:** The related TxGNN prediction, **Pituitary Cancer (Rank 3)**, is supported by 20 registered trials principally evaluating cabergoline in pituitary adenoma subtypes. The most clinically relevant are listed below for contextual reference, as they define the mechanistic and clinical evidence base from which the adenocarcinoma prediction derives.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | N/A | Cabergoline in Cushing's disease due to corticotroph pituitary adenoma; evaluates D2-receptor-mediated ACTH suppression |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Cabergoline for residual non-functioning pituitary adenoma (NFPA) post-transphenoidal surgery; assesses tumour control |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Randomised controlled trial of dopamine agonist treatment in NFPAs to assess growth inhibition |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline as primary therapy for NFPA; assesses tumour size reduction at 48 weeks |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or combined with cabergoline in Cushing's disease; terminated early — safety and efficacy data available |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in NFPA and resistant prolactinomas; in vitro and in vivo responsiveness to cabergoline |
| [NCT03714763](https://clinicaltrials.gov/study/NCT03714763) | N/A | Unknown | 50 | PET-MR dopamine D2 receptor imaging in NFPA to predict cabergoline therapeutic response |
| [NCT04107480](https://clinicaltrials.gov/study/NCT04107480) | Phase 4 | Recruiting | 880 | PRolaCT: three multicentre RCTs comparing surgery versus dopamine agonist as first- and second-line treatment for prolactinoma |
| [NCT01730729](https://clinicaltrials.gov/study/NCT01730729) | Early Phase 1 | Completed | 20 | Pilot Phase II trial of cabergoline in metastatic breast cancer (prolactin receptor-positive); expands oncological application beyond pituitary |
| [NCT03400865](https://clinicaltrials.gov/study/NCT03400865) | N/A | Unknown | 30 | Cabergoline combined with hydroxychloroquine/chloroquine for cabergoline-resistant prolactinomas; explores combination strategies |

---

## Literature Evidence

The following publications are drawn from the pituitary cancer evidence pool (Rank 3), as they represent the strongest available scientific basis for cabergoline's antitumour mechanism. No direct pituitary adenocarcinoma literature exists; all evidence pertains to pituitary adenoma or broader pituitary neoplasm biology.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Comprehensive review of pituitary adenoma diagnosis and management; cabergoline confirmed as first-line for prolactinomas with evidence of tumour shrinkage |
| [35902444](https://pubmed.ncbi.nlm.nih.gov/35902444/) | 2022 | Systematic Review & Meta-analysis | Pituitary | Systematic review and meta-analysis of cabergoline in non-functioning pituitary adenomas; evidence for tumour stabilisation and modest volume reduction |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | Novel mechanisms of cabergoline antitumour action; reviews autophagy induction, antiangiogenic effects, and potential broader applications beyond pituitary |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Translational Research | Neuro-oncology | HTR2B targeting suppresses NFPA growth and sensitises tumour to cabergoline via Gαq/PLC/PKCγ/STAT3 signalling axis |
| [28973192](https://pubmed.ncbi.nlm.nih.gov/28973192/) | 2017 | Translational Research | J Clin Endocrinol Metab | Cabergoline combined with chloroquine induces autophagy and autophagic cell death in pituitary tumour cells; combination overcomes resistance |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Comprehensive approach to prolactinoma management including treatment outcomes, resistance mechanisms, and gonadal implications |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | Medicina | Historical and modern management of prolactinomas; discusses multimodality therapy strategies for aggressive prolactinomas |
| [36413489](https://pubmed.ncbi.nlm.nih.gov/36413489/) | 2023 | Translational Research | J Clin Endocrinol Metab | In vitro efficacy of cabergoline in GH- and GH/PRL-secreting pituitary tumours; supports off-label use in acromegaly and broader tumour subtypes |
| [34221237](https://pubmed.ncbi.nlm.nih.gov/34221237/) | 2021 | Translational Research | Oxid Med Cell Longevity | Brusatol combined with cabergoline inhibits pituitary tumour cell proliferation in vitro and in vivo; potential for augmenting cabergoline efficacy |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline in pituitary tumour treatment and cardiac valve safety; long-term data on clinical outcomes and valvulopathy risk |

---

## UK Market Information

Based on the current Evidence Pack, no MHRA marketing authorisations for cabergoline were retrieved.

> ⚠️ **Data Verification Required:** This almost certainly reflects a data retrieval gap rather than genuine market absence. Cabergoline tablets (e.g., Dostinex® 0.5 mg, Pfizer) have historically held MHRA marketing authorisations in the United Kingdom. Prescribers and researchers should verify the current position against:
> - The **MHRA Products Register** (https://products.mhra.gov.uk/)
> - **BNF section 6.7.1** — Dopaminergic drugs used in endocrinology
> - **NICE guidance** on hyperprolactinaemia and pituitary tumour management

---

## Safety Considerations

Detailed safety data — including key warnings, contraindications, and drug interactions — were not available in this Evidence Pack.

Please refer to the current **Summary of Product Characteristics (SmPC)** and **BNF** for complete safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at https://yellowcard.mhra.gov.uk/.

> **Safety Signal Identified in Evidence Review:** Literature retrieved for the Glaucoma prediction (Rank 5) includes a case report of cabergoline-induced bilateral acute angle-closure glaucoma in a young woman (PMID 21347189), corroborated by a literature synthesis identifying cabergoline as a causative agent for drug-induced secondary angle-closure glaucoma (PMID 25943730). This should be considered a potential adverse effect requiring ocular monitoring, **not** a therapeutic application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.06% for pituitary adenocarcinoma is high, but analysis of the evidence reveals this almost certainly reflects knowledge graph artefact — specifically, ontological proximity between the well-supported pituitary adenoma nodes and the "pituitary neoplasm" category — rather than genuine biological or clinical evidence for adenocarcinoma. Pituitary adenocarcinoma is an exceedingly rare, highly aggressive entity (fewer than 200 cases documented globally) that is pathologically and prognostically distinct from pituitary adenoma, and for which no cabergoline clinical trials or direct publications exist. The three retrieved publications are either indirect, irrelevant, or misattributed. Proceeding with repurposing development for this specific indication is not justified by the current evidence base.

The more promising near-term opportunity lies in **Rank 3: Pituitary Cancer (Pituitary Adenoma)**, which carries substantial evidence from 20 clinical trials — including completed Phase 3 RCTs in non-functioning pituitary adenomas and Cushing's disease — and 20 publications including systematic reviews.

**To proceed, the following is needed:**
- Verification of current MHRA marketing authorisation status via the MHRA Products Register and BNF
- Retrieval of full MOA data from DrugBank (currently flagged as a high-severity data gap)
- Resolution of SmPC warnings and contraindications data (currently flagged as a blocking data gap)
- Ontology expert review to determine whether the TxGNN "pituitary adenocarcinoma" node genuinely represents carcinoma biology or is a knowledge graph artefact from adenoma proximity
- If the broader **Pituitary Cancer (Rank 3)** pathway is pursued, commission a formal systematic evidence review of the completed Phase 3 RCT data (NCT03271918, NCT00889525) to assess suitability for an MHRA repurposing submission or NICE evidence review request

---

*This report is for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before application. This document was generated using the TxGNN UK drug repurposing analysis pipeline (data cut-off: 2026-04-05).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

