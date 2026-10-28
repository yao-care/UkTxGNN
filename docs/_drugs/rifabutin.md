---
layout: default
title: Rifabutin
parent: High Evidence (L1-L2)
nav_order: 540
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Rifabutin: predicted new indication HIV infectious disease (in practice… (evidence level L1). Approved use: Not stated in the UK licence data compiled for this report"
monitor_inn: "Rifabutin"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Rifabutin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Rifabutin: From Mycobacterial Infection to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Rifabutin is a rifamycin antibiotic marketed in the UK as a 150 mg capsule. It is used against mycobacterial infections. The TxGNN model predicts it may be useful for **HIV infectious disease**, with **34 clinical trials** and **20 publications** in the data compiled for this report. Rifabutin has no direct anti-HIV activity, so the realistic role is treating and preventing opportunistic mycobacterial disease (MAC, TB) in people with HIV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK licence data compiled for this report |
| Predicted New Indication | HIV infectious disease (in practice, HIV-associated opportunistic mycobacterial disease) |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L1 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

Note on evidence level: the L1 grading is taken from the data compiled for this report. The Phase 3 trials supporting it are in MAC disease or MAC prophylaxis in HIV patients, not in HIV itself.

---

## Why is This Prediction Reasonable?

Rifabutin inhibits bacterial DNA-dependent RNA polymerase (the rpoB target). It has no activity against HIV. Detailed mechanism of action data were not available in the source record, but this mechanism is well established for the rifamycin class.

People with advanced HIV are prone to opportunistic mycobacterial infections, notably *Mycobacterium avium* complex (MAC) and tuberculosis. Rifabutin has been studied both to treat and to prevent these infections. It is a weaker CYP3A inducer than rifampicin, so it is often preferred when a patient needs protease inhibitor-based antiretroviral therapy.

The TxGNN prediction is therefore best read as "HIV-associated opportunistic mycobacterial disease" rather than treatment of HIV itself. The main guardrail is managing drug interactions with antiretrovirals, including protease inhibitors, dolutegravir and cabotegravir/rilpivirine.

---

## Clinical Trial Evidence

Thirty-four trials were retrieved. The most relevant ones are listed below, with the strongest efficacy evidence first.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Clarithromycin/ethambutol with placebo or rifabutin (two doses) for MAC bacteraemia in AIDS |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Four regimens for disseminated MAC in AIDS; clarithromycin doses with ethambutol plus rifabutin or clofazimine |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Not labelled | Completed | 200 | Double-blind trial of a rifabutin regimen for MAC bacteraemia in AIDS |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2/3 | Completed | 246 | Three clarithromycin-containing regimens (with rifabutin, ethambutol or both) for disseminated MAC |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1,100 | Clarithromycin vs rifabutin vs combination for MAC prevention (CD4 ≤100) |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and rifabutin, alone or combined, for MAC prevention |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Not labelled | Completed | 750 | Double-blind, placebo-controlled rifabutin prophylaxis against MAC bacteraemia |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Not labelled | Completed | 215 | Intermittent rifabutin-based regimen for HIV-related TB (failure and relapse rates) |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Rifabutin PK with antiretroviral therapy in TB/HIV, Vietnam |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin PK with antiretroviral therapy in TB/HIV, South Africa |

Other registered trials are mostly drug interaction studies with antiretrovirals (for example indinavir, nelfinavir, efavirenz, nevirapine, maraviroc, dolutegravir and cabotegravir). They inform dosing and are not efficacy trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | Review | Int J Tuberc Lung Dis | Rifabutin as an alternative to rifampicin with protease inhibitor-based ART |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir; earlier work reported treatment-limiting neutropenia |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Rifabutin PK and safety in TB/HIV-coinfected children; earlier study stopped early for severe neutropenia |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | PK modelling | Br J Clin Pharmacol | Population PK model of dolutegravir with rifabutin |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Modelling | Clin Infect Dis | Managing interactions between long-acting cabotegravir/rilpivirine and inducers such as rifabutin |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | Review | Drug Safety | Risk-benefit assessment of MAC therapies, including rifabutin |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Review | Drugs | Practical approach to TB/HIV co-infection treatment |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectrum | TB associated with HIV infection |
| [8785257](https://pubmed.ncbi.nlm.nih.gov/8785257/) | 1996 | Review | Clin Infect Dis | Rifabutin in pulmonary TB, including HIV-infected patients |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Review | Arch Intern Med | Update on rifampicin and rifabutin drug interactions |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501090Q0AAABAB (BNF code) | Rifabutin Cap 150mg | Capsule (150 mg) | Indication text not available in the data compiled for this report |

The record holds one valid single-ingredient authorisation. The identifier above is a BNF-style product code, not a PL number, and manufacturer and approved indication details were not captured. Please check the current SmPC, the BNF and any NICE guidance for the licensed indications.

---

## Cytotoxicity

This section is omitted because rifabutin is an antimycobacterial, not an antineoplastic drug.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text):
- Thrombocytopenia
- Neutropenia
- Agranulocytosis
- *Clostridium difficile* colitis
- Perinatal necrotising enterocolitis

These agree with the severe neutropenia reported in children treated with rifabutin plus lopinavir/ritonavir (PMIDs 31139825, 33294914). Monitor full blood count.

**Drug interactions:** The interaction screen returned 100 interacting drugs; the 20 reviewed are mostly Moderate.
- **Major:** eliglustat
- **Moderate (examples):** clarithromycin, metronidazole, doxycycline, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), morphine, aprepitant, pioglitazone, saxagliptin, linagliptin and several sulfonylureas
- **Minor:** dolasetron

Trial and literature evidence shows important interactions with antiretrovirals, which need specialist review. Examples are protease inhibitors, efavirenz, nevirapine, dolutegravir, maraviroc and cabotegravir/rilpivirine. Rifabutin dosing often needs adjustment, and clarithromycin raises rifabutin exposure.

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several Phase 3 trials support rifabutin-containing regimens for preventing and treating MAC disease in people with HIV, and PK studies support its use with antiretrovirals. The benefit is against opportunistic mycobacterial infection, not HIV itself, and interaction and neutropenia risks need active management.

**To proceed, the following is needed:**
- Licensed indication text and SmPC warnings and contraindications for the UK product
- A clear definition of the target indication as HIV-associated MAC or TB, not HIV infection itself
- An antiretroviral interaction and dose-adjustment guide
- A haematological monitoring plan (full blood count, especially neutropenia), with extra caution in children
- A check of current UK guidance (BNF, NICE, BHIVA) on rifabutin in HIV-associated mycobacterial disease

**Other predicted indications:** Leprosy has preclinical and case-level evidence only (research question). Endocarditis, pneumocystosis and conjunctivitis lack supporting evidence or a plausible mechanism. Multiple endocrine neoplasia, sclerosing cholangitis, the neurodevelopmental disorder, simian immunodeficiency virus infection and feline AIDS are model predictions only. All of these should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

