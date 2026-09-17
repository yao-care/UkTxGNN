---
layout: default
title: Posaconazole
parent: Moderate Evidence (L3-L4)
nav_order: 471
evidence_level: L3
indication_count: 10
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

Using the drug-repurposing-report skill from CLAUDE.md context to structure this UK evaluation report from the Evidence Pack.

# Posaconazole: From Invasive Fungal Infections to Pneumocystosis

## One-Sentence Summary

> Posaconazole is a triazole antifungal whose established international use is prophylaxis and treatment of invasive fungal infections in immunocompromised patients (a UK-specific approved indication text is not available in this evidence pack).
> The TxGNN model predicts it may be effective for **Pneumocystosis**,
> with **2 clinical trials** and **5 publications** currently identified, though none directly test posaconazole in this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infection prophylaxis/treatment (general pharmacological knowledge; no UK-specific approved indication text on file) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, Posaconazole is a second-generation triazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol synthesis in the fungal cell membrane. Its established international role is prophylaxis and treatment of invasive fungal infections (e.g. invasive aspergillosis, candidiasis) in high-risk immunocompromised patients such as those undergoing allogeneic haematopoietic stem cell transplantation or with prolonged neutropenia.

Pneumocystosis is caused by *Pneumocystis jirovecii*, an atypical fungal organism that lacks the classical ergosterol-rich membrane targeted by triazole antifungals; standard prophylaxis and treatment (co-trimoxazole, atovaquone, dapsone/pyrimethamine) do not rely on the CYP51 pathway. The mechanistic link between posaconazole and pneumocystosis is therefore not well established in mainstream pharmacology, which limits confidence in this prediction despite the high TxGNN score.

The supporting literature identified relates mainly to posaconazole's general role in invasive fungal disease prophylaxis in haemato-oncology/transplant populations (where *Pneumocystis* risk co-exists but is not the primary target of triazole prophylaxis), rather than direct evidence of anti-*Pneumocystis* activity. The clinical trials identified evaluate broader antifungal prophylaxis strategies in the same at-risk population but do not test posaconazole specifically against pneumocystosis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, Not Recruiting | 602 | Pivotal study of IV rezafungin vs standard antimicrobial regimen (which may include posaconazole) to prevent invasive fungal disease in adults undergoing allogeneic blood and marrow transplantation. Posaconazole not the study drug. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis drug combinations after mismatched unrelated donor peripheral blood stem cell transplant; relevant population but not a direct evaluation of posaconazole for pneumocystosis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and Pneumocystis pneumonia; notes posaconazole prophylaxis has reduced invasive candidiasis in high-risk haemato-oncological patients, but does not report direct anti-*Pneumocystis* activity. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Guideline | The Lancet Infectious Diseases | British Society for Medical Mycology 2025 update on diagnosis of serious fungal disease; diagnostic focus rather than posaconazole-specific therapeutic evidence for pneumocystosis. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 clinical practice guideline for invasive pulmonary fungal disease diagnosis/management; general antifungal management context. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Retrospective cohort | Transplant Infectious Disease | Infectious complications (including fungal) in acute GVHD after liver transplantation; describes population-level infection risk, not posaconazole efficacy data. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Pharmacokinetic review | Clinical Pharmacokinetics | Review of antifungal penetration into pulmonary epithelial lining fluid; provides PK rationale but no clinical efficacy data for pneumocystosis. |

---

## UK Market Information

No UK marketing authorisations are on record for Posaconazole in this evidence pack (market status: **Not Marketed**, 0 licences). No product-level BNF or NICE-appraisal data is available to summarise.

---

## Safety Considerations

> Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this evidence pack flags a **Blocking** data gap — TFDA-equivalent warning/contraindication data is unavailable, which prevents completion of the initial safety assessment (S1 stage) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between posaconazole (a triazole antifungal acting on ergosterol synthesis) and pneumocystosis (caused by an atypical fungus not classically covered by triazole antifungals) is not well supported by the identified literature, and no clinical trial directly tests posaconazole in this indication. Combined with the absence of any UK marketing authorisation and missing safety/warning data, the evidence does not currently support progression.

**To proceed, the following is needed:**
- Confirmed UK/MHRA-approved indication text and marketing authorisation status for posaconazole
- SmPC-sourced warnings, contraindications and drug interaction data (currently a Blocking data gap)
- Verified DrugBank/pharmacological mechanism of action data
- Direct *in vitro* or clinical evidence of posaconazole activity against *Pneumocystis jirovecii*, rather than indirect population-level prophylaxis literature
- Consideration of the higher-plausibility candidate identified in this evidence pack — **vulvovaginal candidiasis** (rank 2, score 98.9%) — which is directly within posaconazole's established antifungal spectrum against *Candida* species and is supported by multiple in vitro susceptibility studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

