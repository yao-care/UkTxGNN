---
layout: default
title: Cabergoline
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Cabergoline: predicted new indication Pituitary cancer (evidence level L5). Approved use: Hyperprolactinaemia and prolactin-producing pituitary tumours"
monitor_inn: "Cabergoline"
predicted_indications: ["progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma"]
---

# Cabergoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Cabergoline: From Hyperprolactinaemia to Pituitary Cancer

## One-Sentence Summary

Cabergoline is a dopamine D2 receptor agonist, originally used to treat hyperprolactinaemia and prolactin-producing pituitary tumours.
The TxGNN model predicts it may be effective for **Pituitary Cancer**,
with **14 registered clinical trials** and **20 publications** currently supporting this direction.
Most of this evidence concerns pituitary *adenomas* (benign tumours) rather than malignant pituitary carcinoma, so it should be interpreted with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinaemia and prolactin-producing pituitary tumours (the UK licence record contains no indication text) |
| Predicted New Indication | Pituitary cancer |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L1 (applies to adenoma populations; weaker for carcinoma) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known pharmacology, cabergoline is a dopamine D2 receptor agonist. By stimulating D2 receptors on pituitary lactotroph cells it suppresses prolactin secretion and can shrink prolactin-secreting tumours.

Many other pituitary tumours, including corticotroph and some non-functioning adenomas, also express D2 receptors. This gives a plausible reason to test cabergoline beyond prolactinoma. Laboratory work also suggests that blocking HTR2B (a serotonin receptor) may make non-functioning adenomas more sensitive to cabergoline. A 2020 review (PMID 31597135) describes newer anti-tumour mechanisms of cabergoline.

An important caveat: the trials and reviews mainly involve pituitary adenomas, largely prolactinomas, which is the already-approved use. Evidence in true pituitary carcinoma (metastatic disease) is anecdotal, so the benefit there is not established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Randomised open-label trial of cabergoline for residual non-functioning pituitary adenoma after transsphenoidal surgery; tests tumour growth control |
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | Not reported | Cabergoline for Cushing's disease due to corticotroph pituitary adenoma; D2 receptor rationale |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Randomised trial of dopamine agonist treatment in non-functioning pituitary adenomas; results pending |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline vs no treatment for 48 weeks in non-functioning adenoma; primary question is tumour size reduction |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in non-functioning and resistant adenomas; supports the mechanistic rationale |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Octreotide plus cabergoline in partially responsive acromegaly; single-arm proof of concept |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or with cabergoline in Cushing's disease |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Phase 3 | Recruiting | 70 | High-dose cabergoline in microprolactinoma (original indication; dosing and safety focus) |
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | Not applicable | Completed | 50 | Observational study of cardiac and valvular abnormalities in prolactinoma patients on long-term cabergoline |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | Recruiting | 60 | Metabolic outcomes (glucose tolerance) under dopamine agonist treatment in prolactinoma |

None of these trials studies malignant pituitary carcinoma specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | Novel anti-tumour mechanisms of cabergoline and potential broader applications |
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Diagnosis and management of pituitary adenomas |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Approach to the patient with prolactinoma |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Review | Lancet Diabetes Endocrinol | Pathogenesis, diagnosis and management of prolactin-secreting adenomas |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | Medicina (Kaunas) | Dopamine agonists as primary treatment of prolactinoma, including aggressive tumours |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline use in pituitary tumours and the debated risk of valvular disease |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Review | Pituitary | Cabergoline in acromegaly |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Preclinical | Neuro-oncology | Targeting HTR2B suppresses non-functioning adenoma growth and sensitises it to cabergoline |
| [34034260](https://pubmed.ncbi.nlm.nih.gov/34034260/) | 2022 | Review | Neuroendocrinology | MicroRNAs in dopamine agonist-resistant prolactinoma |
| [28170483](https://pubmed.ncbi.nlm.nih.gov/28170483/) | 2017 | Review | JAMA | Diagnosis and treatment of pituitary adenomas |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409010U0AAAAAA (BNF-style code, not a PL number) | Cabergoline tablets 1 mg | Not specified | Not specified in the data compiled |

This is one valid single-ingredient authorisation. Please check the current SmPC and the BNF for the licensed indications and dosing.

---

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: liver disease, gallbladder disease, heart valve disease, pulmonary fibrosis (including post-inflammatory), IgG4-related retroperitoneal fibrosis, severe pre-eclampsia and pre-eclampsia. These reflect the known fibrotic and valvular concerns with ergot-derived dopamine agonists.
- **Drug Interactions** (60 recorded in total; main ones listed):
  - **Major**: lorcaserin, clarithromycin
  - **Moderate**: metoclopramide
  - Other recorded interactions have unclassified severity (e.g. omeprazole, metformin, simvastatin, prednisolone).
- **Other signals from the literature**: a case report describes bilateral angle-closure glaucoma in a young woman taking cabergoline (PMID 21347189). Cardiac valve safety on long-term use remains debated (PMID 25732645), and psychiatric adverse reactions are increasingly recognised with dopamine agonists (PMID 41781297).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed or ongoing Phase 3 trials test cabergoline in non-functioning and corticotroph pituitary adenomas, supported by a plausible D2 receptor mechanism. However, this evidence concerns adenomas, not malignant pituitary carcinoma, where the evidence is anecdotal. Any use beyond the licensed indication should therefore be limited to specialist, closely monitored settings.

**To proceed, the following is needed:**
- Published results from the completed Phase 3 trials (NCT03271918, NCT00889525) and the ongoing NCT02288962
- Specific evidence in pituitary carcinoma or aggressive pituitary tumours, which is currently lacking
- Licensed indication text, dosage form and PL number from the current SmPC and MHRA records
- Detailed mechanism-of-action data
- A monitoring plan for cardiac valve function, fibrosis, and psychiatric and ocular adverse effects
- Review of interactions with macrolides (e.g. clarithromycin) and other major-level interacting drugs

---

*Other predictions were reviewed but not pursued: pituitary adenocarcinoma (case reports only, Hold), glaucoma (cabergoline is linked to angle-closure glaucoma, a safety concern rather than an opportunity, Hold), and progeria-short stature-pigmented nevi syndrome and spastic quadriplegic cerebral palsy (no evidence, Hold).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

