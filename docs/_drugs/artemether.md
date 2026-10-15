---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: From Antimalarial Therapy to Plasmodium falciparum Malaria

## One-Sentence Summary

Artemether is an artemisinin derivative used with lumefantrine as an antimalarial combination. The TxGNN model's top-ranked predictions were not the most relevant ones: the highest-scoring prediction was acquired angioedema, which has no supporting evidence. This report evaluates the best-supported prediction, **Plasmodium falciparum malaria**, which has **31 registered clinical trials** and **20 publications** in the data compiled for this report. This is an established use of the drug rather than a novel repurposing finding.

> **Note on prediction selection:** The first-ranked prediction (acquired angioedema, score 99.90%) has no trials or literature and is graded Hold. The malaria predictions (ranks 2 and 3) are the only ones with clinical evidence, so this report focuses on rank 2, *P. falciparum* malaria.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the UK licence data compiled for this report (antimalarial use, in combination with lumefantrine) |
| Predicted New Indication | Plasmodium falciparum malaria (TxGNN rank 2) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 (at least two completed Phase 3 trials, e.g. NCT01082705, NCT00422084) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the compiled data. Based on known pharmacology, artemether is an artemisinin derivative. Its endoperoxide bridge is activated by haem iron in the parasite's food vacuole, generating free radicals that damage parasite proteins. It is used in fixed-dose combination with lumefantrine, which has a longer half-life and helps clear residual parasites.

Because artemether is already a standard antimalarial, the "prediction" of efficacy in *P. falciparum* malaria is confirmed by direct clinical evidence rather than being a new repurposing signal. The related prediction of malaria (rank 3) rests on the same mechanism.

The other eight top-ranked predictions (including acquired, hereditary and ACE-inhibitor-related angioedema, nephrogenic syndrome of inappropriate antidiuresis, conjunctivitis and scleroderma) have no trials or literature and no plausible mechanistic link. They most likely reflect network-proximity artefacts in the model. Scleroderma has only a speculative preclinical rationale for artemisinin derivatives.

---

## Clinical Trial Evidence

The 10 most relevant trials are shown below (of 31 registered).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | Completed | 1272 | Double-blind comparison of pyronaridine-artesunate versus artemether-lumefantrine in uncomplicated falciparum malaria (Africa and South East Asia) |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | Completed | 323 | Efficacy of artemisinin combination therapies in children aged 6-59 months in Tanzania |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | Completed | 361 | Azithromycin plus chloroquine versus artemether-lumefantrine (active comparator) in African children |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | Recruiting | 1680 | Triple therapy (artemether-lumefantrine-amodiaquine) versus first-line ACTs, non-inferiority design |
| [NCT02020330](https://clinicaltrials.gov/study/NCT02020330) | Phase 3 | Completed | 150 | 3-day versus 5-day course of artemether-lumefantrine in Myanmar |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | Completed | 305 | Extended-duration artemether-lumefantrine in children, including those with HIV on efavirenz |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | Completed | 340 | Versus artesunate-amodiaquine in Burkina Faso (real-life effectiveness) |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | Completed | 452 | In vivo efficacy versus artesunate-amodiaquine in Malawi |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Completed | 267 | Suspension versus tablet formulation in children under five in Kenya |
| [NCT01103830](https://clinicaltrials.gov/study/NCT01103830) | Phase 1 | Completed | 287 | QT/QTc effect of Eurartesim compared with Riamet, placebo and moxifloxacin in healthy volunteers |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Systematic review/meta-analysis | PloS one | Therapeutic efficacy of artemether-lumefantrine and other ACTs in sub-Saharan Africa |
| [33957925](https://pubmed.ncbi.nlm.nih.gov/33957925/) | 2021 | Systematic review/meta-analysis | Malaria journal | Efficacy and safety of artemether-lumefantrine in Ethiopia |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Systematic review/meta-analysis | Malaria journal | Safety of dihydroartemisinin-piperaquine versus artemether-lumefantrine in African children |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Systematic review | Malaria journal | Safety and efficacy of artemether-lumefantrine in pregnancy |
| [42174576](https://pubmed.ncbi.nlm.nih.gov/42174576/) | 2026 | Systematic review/meta-analysis | Malaria journal | Efficacy of artemether-lumefantrine in Mozambique |
| [40660279](https://pubmed.ncbi.nlm.nih.gov/40660279/) | 2025 | Efficacy study | Malaria journal | Efficacy of four ACTs in Mozambique, 2022 |
| [38741101](https://pubmed.ncbi.nlm.nih.gov/38741101/) | 2024 | Efficacy study | Malaria journal | Efficacy and tolerability of artemether-lumefantrine in Niger, 2020 |
| [38867217](https://pubmed.ncbi.nlm.nih.gov/38867217/) | 2024 | Efficacy study | Malaria journal | Efficacy and safety in central-east Ethiopia |
| [36792022](https://pubmed.ncbi.nlm.nih.gov/36792022/) | 2023 | Retrospective comparative study | Travel Med Infect Dis | Artemether-lumefantrine versus mefloquine and atovaquone-proguanil in travellers |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Molecular/resistance study | J Infect Dis | Treatment selects for pfmdr1 increased copy number; reduced efficacy has recently emerged in Africa |

---

## UK Market Information

The licence records compiled for this report do not include dosage forms or approved-indication text.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0504010AABBAAAA | Riamet tablets | Tablet (form not recorded) | Not recorded in the data compiled |
| 0504010AAAAAAAA | Artemether/Lumefantrine tablets 20 mg/120 mg | Tablet (form not recorded) | Not recorded in the data compiled |

Both entries are valid single-ingredient records and appear to correspond to BNF section 5.4.1 (antimalarials). The identifiers shown are BNF-style codes rather than PL numbers, so please confirm the PL numbers and licensed wording in the MHRA register and the SmPC.

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes and potassium deficiency disease. These are consistent with QT-prolongation concerns, and a dedicated QT study (NCT01103830) is in the trial list.
- **Drug interactions:** 95 interactions were recorded. Major interactions include clarithromycin, cobicistat, amprenavir, apalutamide, atazanavir and boceprevir. Moderate interactions include dexamethasone, miconazole, bosentan, bexarotene and armodafinil. Many involve CYP3A4 inhibitors or inducers, so review the full list before prescribing.
- **Resistance:** Reduced efficacy and treatment failure have been reported, including a UK case (PMID 38019958). Artemisinin monotherapy should be avoided.

Label warnings and contraindications were not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for *P. falciparum* malaria). All other predictions, including the top-ranked acquired angioedema, should be **Hold**.

**Rationale:**
- Multiple completed Phase 3 and Phase 4 trials and several systematic reviews support artemether-lumefantrine in uncomplicated *P. falciparum* malaria. This is an established indication, not new repurposing.
- The remaining predictions have no clinical or literature support and no plausible mechanism.

**To proceed, the following is needed:**
- Licensed indication, dosage form and PL numbers from the MHRA register and SmPC
- Label warnings and contraindications, including QT-prolongation precautions and ECG or electrolyte checks where relevant
- Detailed mechanism-of-action data from DrugBank
- A review of the 95 recorded drug interactions, particularly CYP3A4 modulators and antiretrovirals
- Use in combination therapy only, with monitoring for emerging resistance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

