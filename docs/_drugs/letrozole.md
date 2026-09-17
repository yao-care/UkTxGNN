---
layout: default
title: Letrozole
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: From Breast Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Letrozole is a third-generation aromatase inhibitor already established for the treatment of hormone receptor-positive (HR+) breast cancer. TxGNN's top-ranked prediction for this drug is **Female Breast Carcinoma**, supported by an unusually large body of evidence — **60+ clinical trials and 20 publications**. However, this "predicted new indication" is functionally identical to letrozole's well-known existing use, and the evidence pack itself flags a significant data inconsistency that must be resolved before this candidate can be treated as a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap). Letrozole (Femara) is widely known as an aromatase inhibitor for HR-positive breast cancer, but this could not be confirmed from the supplied dataset. |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| UK Market Status | "Not marketed" per evidence pack — flagged as inconsistent with letrozole's well-established global/UK marketing status; requires verification |
| Number of Marketing Authorisations | 0 (data gap — see note below) |
| Recommended Decision | **Hold — Data Verification Required** |

---

## Why is This Prediction Reasonable?

Letrozole is a third-generation, non-steroidal aromatase inhibitor. It blocks the conversion of androgens to oestrogens, lowering both circulating and intratumoural oestrogen levels, thereby suppressing the proliferation of ER-positive breast cancer cells. This is a well-established, extensively validated mechanism.

**Important caveat:** the disease TxGNN has "predicted" here — Female Breast Carcinoma — is not a novel indication. It is letrozole's core, already-approved use (marketed globally as Femara). This is not repurposing in the proper sense of the term. The evidence pack's own scoring rationale explicitly notes this: `original_indications` is empty and `market_status` is recorded as "not marketed", both of which are inconsistent with letrozole's known regulatory history. This strongly suggests a data-pipeline gap (e.g. missing linkage between the drug record and its approved-indication source) rather than a genuine model-driven discovery.

In practical terms, the very large trial and literature base found for this "candidate" reflects letrozole's decades of clinical use in breast cancer — not new supporting evidence for an unmet need. We recommend treating this candidate as a **data quality flag** rather than a repurposing opportunity, and correcting the source records for original indication and UK licensing status before any further evaluation proceeds.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00330317](https://clinicaltrials.gov/study/NCT00330317) | Phase 3 | Completed | 300 | Neoadjuvant letrozole in postmenopausal HR+ primary breast cancer; assessed duration of treatment for tumour regression to permit breast-conserving surgery |
| [NCT00673335](https://clinicaltrials.gov/study/NCT00673335) | Phase 3 | Completed | 170 | Letrozole vs placebo for breast cancer prevention in postmenopausal BRCA1/BRCA2 carriers |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3B | Completed | 301 | Everolimus + exemestane (4EVER trial) in ER+ postmenopausal women progressing on non-steroidal AI (letrozole-class) therapy |
| [NCT00003140](https://clinicaltrials.gov/study/NCT00003140) | Phase 3 | Completed | 5,187 | Landmark MA.17 trial: letrozole vs placebo in women completing ≥5 years of adjuvant tamoxifen |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | Completed | 4,172 | Letrozole vs anastrozole as adjuvant treatment in HR+/node-positive postmenopausal breast cancer |
| [NCT00754845](https://clinicaltrials.gov/study/NCT00754845) | Phase 3 | Completed | 1,918 | Letrozole vs placebo in women who completed 5 years of adjuvant aromatase inhibitor therapy (MA.17-related extension) |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Active, not recruiting | 4,486 | POETIC: perioperative aromatase inhibitor therapy plus Ki67-guided treatment individualisation |
| [NCT04964934](https://clinicaltrials.gov/study/NCT04964934) | Phase 3 | Active, not recruiting | 315 | Switching to next-generation oral SERD (camizestrant) vs continuing letrozole/anastrozole + CDK4/6 inhibitor in ESR1-mutated HR+/HER2- metastatic breast cancer |
| [NCT03306472](https://clinicaltrials.gov/study/NCT03306472) | Phase 2 | Completed | 198 | PIONEER: pre-operative window study of letrozole plus megestrol acetate vs letrozole alone in ER+ breast cancer |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | Completed | 108 | Neoadjuvant letrozole in postmenopausal women with ER+ ductal carcinoma in situ (DCIS) |

*Note: these trials reflect letrozole's established evidence base in breast cancer treatment generally, rather than evidence for a distinct new indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | New England Journal of Medicine | BIG 1-98 landmark trial comparing letrozole with tamoxifen as adjuvant therapy in postmenopausal HR+ early breast cancer |
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Research and Treatment | Overall survival results from PALOMA-1: palbociclib + letrozole vs letrozole alone as first-line therapy in ER+/HER2- advanced breast cancer |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | RCT | Computational and Mathematical Methods in Medicine | Efficacy, safety and prognosis of sequential tamoxifen–letrozole therapy vs letrozole monotherapy |
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT | The Lancet Oncology | CORALLEEN: neoadjuvant ribociclib + letrozole vs chemotherapy in luminal B early breast cancer |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Overview of letrozole pharmacology, toxicity and potential therapeutic effects |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacodynamic, pharmacokinetic, efficacy and safety review of letrozole |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh, Scotland) | Development of letrozole and its use in advanced and neoadjuvant breast cancer |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opinion on Pharmacotherapy | Comparative review of anastrozole, letrozole and exemestane in early breast cancer |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opinion on Pharmacotherapy | Present and future role of letrozole in breast cancer treatment |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | Review | Women's Health Issues | Clinical implications and remaining questions from the Letrozole Breast Cancer Trial |

---

## UK Market Information

No marketing authorisation records were returned in this evidence pack (`total_licenses: 0`, `market_status: "Not marketed"`). This is flagged as a **data gap requiring verification**: letrozole is internationally well established as an approved medicine (brand name Femara) for HR-positive breast cancer, and this status should be independently confirmed against the MHRA product database (dmd/SPC repository) before this evidence pack is used for decision-making. Corresponding BNF classification (endocrine therapy, aromatase inhibitor) should also be added once source data is corrected.

---

## Cytotoxicity

Letrozole is an antineoplastic agent by therapeutic classification (aromatase inhibitor, endocrine/hormonal breast cancer therapy), though it is **not** a conventional cytotoxic chemotherapeutic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/endocrine therapy (non-cytotoxic aromatase inhibitor) |
| Myelosuppression Risk | Low — aromatase inhibitors do not act on rapidly dividing marrow precursors; please refer to the SmPC warnings and precautions for confirmation |
| Emetogenicity Classification | Low |
| Monitoring Items | Bone mineral density (long-term oestrogen suppression), lipid profile, liver function; please refer to the SmPC for full monitoring requirements |
| Handling Protection | Standard oral medicine handling; not subject to cytotoxic drug handling regulations (non-cytotoxic hormonal agent) |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold — Data Verification Required**

**Rationale:**
Although the evidence base for letrozole in breast cancer is very strong (L1, multiple completed Phase 3 RCTs), this "predicted new indication" duplicates letrozole's already-established, globally approved use. The evidence pack itself flags that `original_indications` is empty and UK market status is recorded as "Not marketed" — both inconsistent with known reality — indicating a data-pipeline gap rather than a genuine repurposing signal. Proceeding on the current dataset risks presenting an already-approved use as a novel discovery.

**To proceed, the following is needed:**
- Verification and correction of letrozole's original/approved indication data in the source pipeline
- Confirmation of current UK/MHRA marketing authorisation status and licence numbers (data gap DG001)
- Retrieval of detailed mechanism of action (MOA) data from DrugBank (data gap DG002)
- TFDA/MHRA product label (SmPC) warnings and contraindications for a proper S1 safety screen (data gap DG001, Blocking)
- Re-run of the disease-ontology mapping step to confirm whether "female breast carcinoma" reflects a distinct clinical entity from letrozole's existing indication, or is an artefact of graph proximity to the drug's known edges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

