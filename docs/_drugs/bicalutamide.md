---
layout: default
title: Bicalutamide
parent: Model Prediction Only (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bicalutamide: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the compiled data (bicalutamide is an androgen recept…"
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Bicalutamide is a non-steroidal androgen receptor antagonist, marketed in the UK as a 50 mg tablet.
The TxGNN model predicts it may be effective for **female breast carcinoma** (specifically androgen receptor-positive, mainly triple-negative disease), supported by **1 clinical trial** and **20 publications**, mostly preclinical or review articles.

The original indication is not recorded in the data compiled for this report, so this summary is based on the drug's known class.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the compiled data (bicalutamide is an androgen receptor antagonist used in prostate cancer) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L2 (as scored in the compiled data; see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on evidence level:** the compiled data assigns L2, but the only trial is a single-arm Phase 2 combination study that is still active, and no completed randomised trial is listed. By the stated rules this is closer to L3-L4, so L2 should be treated cautiously.

The top-ranked prediction by TxGNN score is hypertrichosis (99.69%), but evidence for it is limited to a single comment letter (L4). Female breast carcinoma is the best-supported candidate, so this report focuses on it.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, bicalutamide blocks the androgen receptor (AR), and its efficacy in an androgen-driven cancer is established. Mechanistically, it may be applicable to breast cancers that express AR.

AR is expressed in a substantial proportion of breast cancers, including about 30% of triple-negative tumours (the luminal androgen receptor, or LAR, subtype) and apocrine carcinoma. These tumours have few targeted options. Preclinical work shows bicalutamide reduces proliferation and invasion in AR-positive triple-negative breast cancer cell lines. It also shows combination effects with curcumin, with ERK inhibition (via ferroptosis involving FOXC2) and with chemotherapy in inflammatory mammary cancer models.

The evidence is not uniformly positive. A phase II study of bicalutamide plus an aromatase inhibitor in ER-positive/AR-positive advanced breast cancer showed no synergy (6-month clinical benefit rate 16.7%, objective response rate 0%) and was terminated. Benefit therefore appears to depend on tumour subtype and on selecting patients by biomarker.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, not recruiting | 30 | Nivolumab plus bicalutamide and ipilimumab in metastatic HER2-negative breast cancer. Single-arm study of safety and efficacy; the combination design cannot isolate bicalutamide's contribution. Estimated completion December 2026. |

For other predicted indications, two trials were linked to multiple endocrine neoplasia (NCT03878524 and NCT02615223), but neither is specific to that condition and neither provides relevant evidence.

## Literature Evidence

The compiled data contains no randomised controlled trials for this indication. The most relevant publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase II single-arm study | The Oncologist | Bicalutamide plus aromatase inhibitor in ER+/AR+ advanced breast cancer showed no synergy (clinical benefit rate 16.7%, objective response rate 0% at 6 months); study terminated |
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | Anti-androgen therapy for TNBC, including bicalutamide and combinations with chemotherapy and immunotherapy |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treatment Reviews | AR as a potential target in luminal androgen receptor TNBC |
| [32145961](https://pubmed.ncbi.nlm.nih.gov/32145961/) | 2020 | Review | Bulletin du Cancer | AR-positive TNBC (about 30% of TNBC); biology and therapy |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clinical Breast Cancer | Apocrine carcinoma is ER-negative and AR-positive, with frequent PIK3CA/PTEN/AKT mutations |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Science China Life Sciences | Bicalutamide synergises with the ERK inhibitor GDC-0994, triggering ferroptosis via FOXC2 in TNBC |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | Preclinical | Medicine | Bicalutamide inhibits proliferation and invasion of MDA-MB-231 TNBC cells |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | Preclinical | Anti-Cancer Drugs | Bicalutamide plus curcumin had a strong effect in AR-positive TNBC |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | Preclinical (in vitro and in vivo) | Int J Mol Sci | Bicalutamide enhanced doxorubicin and docetaxel in human and canine inflammatory mammary cancer lines |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | Reappraisal of the role of AR in breast cancer |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803042A0AAAAAA | Bicalutamide Tab 50mg | Not recorded | Not recorded |

One authorisation (single-ingredient, valid) is recorded. The identifier shown is not in the standard UK PL format, and the dosage form and approved indication are blank in the compiled data. Please verify against the MHRA register, the SmPC and the BNF. NICE appraisal information was not included in the compiled data.

## Cytotoxicity

Bicalutamide is an endocrine (anti-androgen) therapy for cancer, not a conventional cytotoxic agent. Please refer to the SmPC warnings and precautions for monitoring and handling requirements.

## Safety Considerations

- **Disease associations from the knowledge graph** (these are model-derived contraindication links, not label text): liver disease, drug-induced liver injury, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, anaemia (including macrocytic anaemia) and interstitial lung disease.
- **Drug interactions:** 100 interactions were identified, and the first 20 are summarised here.
  - **Major:** cisapride and dolasetron.
  - **Moderate:** famotidine, loperamide, aprepitant, bisacodyl, budesonide (including nasal), castor oil, clarithromycin, eliglustat, glycerin, granisetron, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide and mineral oil.
  - **Minor:** metronidazole.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
AR is a plausible target in AR-positive, mainly triple-negative breast cancer, with consistent preclinical and review support and one active Phase 2 combination trial. However, there is no randomised evidence, the one clinical combination study in ER-positive disease was negative, and the compiled data lacks label-based safety information. This should remain investigational.

**To proceed, the following is needed:**
- Restriction to AR-positive disease (mainly triple-negative/LAR) with defined biomarker selection criteria
- Results from NCT03650894 and randomised data that isolate bicalutamide's contribution
- Mechanism of action data and the full SmPC and BNF safety information, which were missing from the compiled data
- Confirmation of the UK authorisation details (dosage form and approved indication)
- A hepatic and glycaemic monitoring plan, given the knowledge-graph disease associations and the interaction burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

