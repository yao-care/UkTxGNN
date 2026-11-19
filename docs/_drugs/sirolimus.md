---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 570
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-20
monitor_inn: "Sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). In the UK: 10 NHSBSA BNF presentation codes"
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sirolimus is an mTOR inhibitor that is marketed in the UK.
The TxGNN model predicts it may be effective for **liposarcoma**, with a prediction score of 0.9989.
Currently there is **1 registered clinical trial** (completed, no published results) and no published study that tests sirolimus in liposarcoma, so the evidence is limited to model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (10 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for sirolimus: "Sirolimus in FYARRO is an inhibitor of mechanistic target of rapamycin kinase (mTOR, previously known as mammalian target of rapamycin). mTOR, a serine threonine kinase, is downstream of the PI3K/AKT pathway, controls key cellular processes such as cell survival, growth, and proliferation, and is commonly dysregulated in several human cancers. In cells, sirolimus binds to the immunophilin, FK Binding Protein-12 (FKBP-12), to generate an immunosuppressive complex." ([DailyMed: Fyarro (sirolimus) prescribing information, Aadi Bioscience, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9bb784-53e2-46f9-a65d-1c6c2a230eaf), label version 2026-09-09; accessed 2026-11-19.) Sirolimus is known as a mammalian target of rapamycin (mTOR) inhibitor. Activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, and preclinical models suggest that mTOR inhibition can slow tumour growth. This provides a plausible biological rationale for testing sirolimus in liposarcoma.

This rationale remains theoretical. The supporting literature consists mainly of reviews of sarcoma therapy and transplant cancer-risk data, none of which show that sirolimus works against liposarcoma.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus combined with cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. No published or posted results; no control arm, and the effect cannot be attributed to sirolimus alone. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | In renal transplant recipients, sirolimus after early cyclosporine withdrawal reduced cancer risk. This is not a liposarcoma study. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agents for advanced sarcomas. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments of rare connective tissue tumours and sarcomas. |

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0802020U0AAADAD | Sirolimus 1mg tablets | Sirolimus |
| 0802020U0AAACAC | Sirolimus 1mg/ml oral solution sugar free | Sirolimus |
| 0802020U0AAAEAE | Sirolimus 2mg tablets | Sirolimus |
| 0802020U0AAAGAG | Sirolimus 2mg/g gel | Sirolimus |
| 0802020U0AAAFAF | Sirolimus 500microgram tablets | Sirolimus |
| 0802020U0BCAAAG | Hyftor 2mg/g gel | Sirolimus |
| 0802020U0BBAFAF | Rapamune 0.5mg tablets | Sirolimus |
| 0802020U0BBADAD | Rapamune 1mg tablets | Sirolimus |
| 0802020U0BBACAC | Rapamune 1mg/ml oral solution | Sirolimus |
| 0802020U0BBAEAE | Rapamune 2mg tablets | Sirolimus |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Moderate-to-major interactions are recorded, including Major interactions with amphotericin B, mesalazine, balsalazide and clarithromycin. Moderate interactions include acarbose, metformin, pioglitazone, alogliptin, canagliflozin, hydrocortisone, dexamethasone, budesonide, cimetidine and aprepitant.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered liposarcoma-related trial is a single-arm combination study with no published results, and no published study tests sirolimus in liposarcoma. The prediction is therefore supported by the model score and general mTOR biology alone (evidence level L5).

**To proceed, the following is needed:**
- Publication or release of results from NCT02821507, ideally separating liposarcoma outcomes and the contribution of sirolimus from cyclophosphamide
- Preclinical or early clinical data for sirolimus specifically in liposarcoma
- Detailed mechanism of action data
- Safety review against the SmPC and BNF, including interaction management in patients receiving cytotoxic chemotherapy

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fyarro (sirolimus) prescribing information, Aadi Bioscience, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9bb784-53e2-46f9-a65d-1c6c2a230eaf) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

