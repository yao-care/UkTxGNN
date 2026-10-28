---
layout: default
title: Sirolimus
parent: High Evidence (L1-L2)
nav_order: 570
evidence_level: L2
indication_count: 7
last_modified_at: 2026-10-15
monitor_inn: "Sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L2). Approved use: Not recorded in the local data"
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **7** 
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

Sirolimus is an mTOR inhibitor, originally associated with renal cell carcinoma and lymphangioleiomyomatosis (LAM).
The TxGNN model predicts it may be effective for **liposarcoma**, but this is supported by only **1 completed single-arm Phase 2 trial** (combination regimen) and **mostly review-level literature**.
A stronger and more clinically actionable signal in the same output is for **lymphangiomyoma/LAM**, which is better regarded as an on-label or near-label use than true repurposing (see the final section).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L2 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold (research question; see rationale) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sirolimus inhibits mTOR (mammalian target of rapamycin), a kinase that drives cell growth, proliferation and angiogenesis. Its efficacy has been demonstrated in LAM, a disease driven by constitutive mTORC1 activation.

Activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, including liposarcoma. This provides a plausible biological rationale for mTOR inhibition. However, the clinical evidence is limited. The only trial is a single-arm study of sirolimus combined with another agent, so any effect cannot be attributed to sirolimus alone. The supporting literature consists mainly of reviews and transplant cancer-risk data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre study of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. No control arm; results are not included in the data compiled for this report. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | In renal transplant recipients, early cyclosporine withdrawal with sirolimus was associated with reduced cancer risk. Not sarcoma-specific. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agents in advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening and immunosuppressive drug effects in renal transplant patients |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohort | Fam Cancer | Clinical spectrum of PTEN hamartoma tumour syndrome |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Case report | Diagn Pathol | Fibro-adipose vascular anomaly and the mTOR pathway; sirolimus context |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0802020U0AAADAD (BNF-style product code, not a PL number) | Sirolimus tablets 1 mg | Tablet (not specified in the data) | Not specified in the data |

## Safety Considerations

**Contraindication-related associations (from the knowledge graph, not label text):** The graph links sirolimus with caution in several conditions, including hypertension, kidney disease, liver disease, hyperglycaemia and diabetes, hyperlipidaemia and hypertriglyceridaemia, interstitial lung disease, active infections (including cytomegalovirus infection and pneumocystosis), cancer, stroke/cerebrovascular disorders, hyperbilirubinaemia and pericardial effusion. These should be verified against the SmPC.

**Drug Interactions:** 100 interactions were listed. Major interactions include:
- Clarithromycin
- Amphotericin B (including the lipid complex formulation)
- Mesalazine
- Balsalazide

Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, pioglitazone, alogliptin, acarbose, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), cimetidine and aprepitant. Sirolimus is also subject to CYP3A4/P-gp interactions.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold (treat as a research question)**

**Rationale:**
The liposarcoma prediction has a high model score but rests on one single-arm combination trial and indirect literature, so sirolimus's own contribution is unproven. The L2 grade reflects trial phase rather than strength of effect.

**To proceed, the following is needed:**
- Published results of NCT02821507, ideally with liposarcoma-specific outcomes
- Controlled evidence of sirolimus monotherapy or a clear attribution of effect
- Mechanism of action data and the UK SmPC safety information (the licence record lacks indication text and warnings)
- A safety monitoring plan covering infection, hyperlipidaemia, pneumonitis and interaction management, with therapeutic drug monitoring

---

### Other Predictions of Note

| Predicted Indication | Score | Evidence Level | Recommendation | Comment |
|---|---|---|---|---|
| **Lymphangiomyoma (LAM)** | 0.9979 | L5 | Proceed with Guardrails | Phase 3 MILES trial ([NCT00414648](https://clinicaltrials.gov/study/NCT00414648), n=89, completed) and an active Phase 3 early-disease trial ([NCT03150914](https://clinicaltrials.gov/study/NCT03150914)). Consistent with the original LAM indication, so on-label or near-label rather than true repurposing. |
| Benign PEComa | 0.9980 | L5 | Research Question | Case reports and cohorts; mechanistically coherent (TSC1/TSC2 loss) |
| Lung PEComa | 0.9963 | L5 | Research Question | Evidence mostly LAM-derived and indirect |
| Uterine corpus PEComa, ovarian myxoid liposarcoma, Xp11.2/TFE3 renal cell carcinoma, unclassified renal cell carcinoma, renal cell carcinoma associated with neuroblastoma, vulva sarcoma | 99.6–0.9980 | L5–L5 | Hold | Model prediction only, or no direct evidence |

Note that the DrugBank-style mechanism data and licence indication text were unavailable, so the original-indication listing relies on the knowledge graph.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

