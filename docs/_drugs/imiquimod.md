---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Common Wart to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical immune response modifier, originally used for common warts, anogenital human papillomavirus infection, superficial multifocal basal cell carcinoma and actinic keratosis.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**, with **2 clinical trials** and **9 publications** currently supporting this direction. Evidence is mostly small trials, reviews and case reports.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common wart, anogenital human papillomavirus infection, superficial multifocal basal cell carcinoma, actinic keratosis (approved indication text is not available in the UK licence record) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The compiled data assigns L1, but by the stated criteria this is not supported. The only completed Phase 3 trial is a 20-patient single-arm study, and the second Phase 3 trial was terminated after 9 participants. Neither meets the bar of two completed Phase 3 RCTs. The supporting evidence is a Cochrane systematic review and other reviews, so L3 is the more defensible grade.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, imiquimod is a Toll-like receptor 7 (TLR7) agonist. It induces local interferon-alpha, TNF-alpha and IL-12 production and promotes Th1-type cell-mediated immunity. This supports clearance of dysplastic and premalignant epithelium.

Actinic keratosis, a premalignant skin lesion, is already among imiquimod's established indications, so this prediction is largely consistent with existing use. Extension to other premalignant sites is biologically plausible. These include vulval, anal and cervical intraepithelial neoplasia, which are HPV-associated and covered by systematic reviews. The prediction is therefore best read as a broadening of an existing indication rather than a wholly new one.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label, single-arm study of imiquimod 5% cream, 3 days per week in 1 or 2 cycles, for actinic keratoses on the head. It assessed duration of effect. Small, so supportive only. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomised trial of topical imiquimod for high-grade cervical intraepithelial neoplasia, as an alternative to LLETZ excision. Terminated early with 9 participants, so it is underpowered and cannot support efficacy conclusions. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane systematic review | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a premalignant HPV-associated condition. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane systematic review | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia, where surgery has high morbidity and relapse. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, including topical field therapies. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies for non-melanoma skin cancer and precursor lesions, including imiquimod, fluorouracil and diclofenac. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful treatment of high-grade vulval intra-epithelial neoplasia with imiquimod 5% in a renal transplant recipient. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Clearance of penile bowenoid papulosis with imiquimod 5% cream, well tolerated. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical (rat) | Urol Oncol | Pharmacokinetics of TLR7 agonists given intravesically, under investigation for bladder cancer. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1307000V0AAAAAA | Imiquimod cream 5%, 250 mg sachet | Cream (recorded form not stated) | Not stated in the licence record |

This is the only authorisation in the data compiled for this report. The identifier does not follow the usual MHRA "PL" format, so please verify it against the MHRA record. NICE appraisal and BNF classification details were not available.

## Cytotoxicity

Imiquimod is an immune response modifier rather than a conventional cytotoxic, and it is applied topically. Cytotoxic handling requirements are therefore not expected to apply. Please refer to the SmPC warnings and precautions.

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** photoparoxysmal response, photosensitivity disease, autoimmune disease, graft versus host disease and sunburn.
- **Drug Interactions:** 59 potential interactions were identified, all with an unspecified severity level. Examples include warfarin, clopidogrel, prednisolone, prednisone, budesonide, hydroxychloroquine and ibuprofen. These need clinical review before any conclusions are drawn.
- **Literature safety signals:** case reports describe malignant conversion of oral papillomatosis during imiquimod treatment, erythema multiforme, lichen planopilaris, and a mucinous carcinoma arising during treatment of extramammary Paget disease. These are isolated reports, but they support careful lesion monitoring.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The prediction overlaps with an established use (actinic keratosis) and has a plausible TLR7-mediated mechanism. Systematic reviews support use in HPV-related intraepithelial neoplasia. However, the trials are small or terminated, so confirmatory evidence is lacking.

**To proceed, the following is needed:**
- Adequately powered RCTs in specific premalignant sites, particularly cervical, vulval and anal intraepithelial neoplasia
- Verified UK licence details, including approved indications, dosage form and the MHRA reference
- SmPC warnings, contraindications and mechanism of action data (currently missing)
- Review of the interaction data and a monitoring plan for autoimmune, immunosuppressed and photosensitive patients

*Other predicted indications (ranks 2–10) are not covered in detail here. They rest on L3–L5 evidence at most, such as scoping reviews, animal models and case reports, and are not recommended for progression at this stage.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

