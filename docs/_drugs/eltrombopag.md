---
layout: default
title: Eltrombopag
parent: Model Prediction Only (L5)
nav_order: 247
evidence_level: L5
indication_count: 1
monitor_inn: "Eltrombopag"
predicted_indications: ["HIV infectious disease"]
last_modified_at: 2026-10-30
description: "Eltrombopag: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Eltrombopag
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Eltrombopag: thrombopoietin receptor agonist → HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Eltrombopag is a thrombopoietin receptor (TPO-R) agonist that stimulates platelet production.
The TxGNN model predicts it may be relevant to **HIV infectious disease**, but the supporting material is mostly indirect: **1 clinical trial** (in thrombocytopenia with chronic liver disease, not HIV) and **8 publications** (reviews, case reports, one case series and one in vitro screen), mainly on HIV-associated thrombocytopenia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, eltrombopag is a TPO-R agonist that stimulates megakaryopoiesis and haematopoietic progenitors.

The plausible link to HIV is not antiviral activity. It is the treatment of HIV-associated thrombocytopenia (HIV-related immune thrombocytopenia) and, in isolated case reports, HIV-associated bone marrow failure or aplastic anaemia. One case report also described immunomodulatory effects (fewer pro-inflammatory T helper cells, a higher T-regulatory to T-helper ratio). A single in vitro screen of approved drugs suggests possible modulation of HIV-1 proviral transcription, but this is exploratory and its clinical relevance is unclear.

The high score of 0.9926 is a computational output. It probably reflects the known association between eltrombopag and infection-related immune thrombocytopenia, and should not be read as evidence of efficacy against HIV itself. Any benefit would be supportive care for a complication, not a new antiviral mechanism.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Randomised, double-blind, placebo-controlled study of eltrombopag to reduce the need for platelet transfusion in thrombocytopenic patients with chronic liver disease undergoing elective invasive procedures. The enrolled population is not specified as HIV, so it is indirect evidence for this prediction. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Retrospective case series | J Int Assoc Provid AIDS Care | Initial experience with thrombopoietin receptor agonists, including eltrombopag, in refractory HIV-associated immune thrombocytopenia |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS | Eltrombopag used successfully without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS | Aplastic anaemia associated with HIV treated successfully with eltrombopag; immunomodulatory effects observed |
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematol Oncol Clin North Am | Infectious causes of chronic immune thrombocytopenia, including HCV, HIV and H. pylori |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Semin Hematol | Therapeutic strategies for hepatitis- and other infection-related immune thrombocytopenias |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro drug screen | Viruses | Screen of FDA-approved drugs for modulators of HIV-1 proviral transcription |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | J Coll Physicians Surg Pak | Hepatitis B leading to megaloblastic anaemia and severe thrombocytopenia (indirect) |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farm Hosp | Eltrombopag for thrombocytopenia in chronic hepatitis C, two cases (indirect) |

## Safety Considerations

- **Conditions recorded as contraindication-type relations in the model data (not label text):** kidney disease, liver disease (including acute liver failure and hepatitis), gallbladder disease, anaemia, leukopenia, myelodysplastic syndrome, thrombocytosis, hepatic vein thrombosis and Budd-Chiari syndrome, and hyperbilirubinaemia (including Gilbert syndrome). These should be checked against the current SmPC.
- **Drug Interactions:** 100 interactions were found. Most are of moderate severity and involve polyvalent cation products (calcium, magnesium and aluminium salts, iron, kaolin, attapulgite), which may reduce absorption. One Major interaction is listed (eluxadoline). Moderate interactions also include glyburide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication studies eltrombopag directly for HIV infection itself. The only trial is terminated and not HIV-specific, and the other evidence consists of case reports, a small case series, reviews and an exploratory in vitro screen. The high TxGNN score alone does not support efficacy.

**To proceed, the following is needed:**
- Verification of the enrolled population in NCT00678587
- Prospective controlled studies of eltrombopag in HIV-associated thrombocytopenia or bone marrow failure, with clear endpoints
- Mechanism of action data and confirmation of any antiviral or immunomodulatory effect
- Review of the current SmPC and BNF warnings and contraindications, particularly hepatic safety and thrombotic risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

