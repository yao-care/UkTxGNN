---
layout: default
title: Tenofovir Disoproxil
parent: Model Prediction Only (L5)
nav_order: 604
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Tenofovir Disoproxil: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Tenofovir disoproxil"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Tenofovir Disoproxil: From Chronic Hepatitis B and HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor originally used to treat chronic hepatitis B virus infection and HIV infection (including AIDS).
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this is an animal model of the existing HIV indication rather than a genuinely new human indication.
There are **no registered clinical trials** and **18 publications** (almost all preclinical macaque studies, plus a few reviews).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection; HIV infection; AIDS (the UK authorisation record holds no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, tenofovir disoproxil is a prodrug of tenofovir, a nucleotide analogue that inhibits viral reverse transcriptase. Its efficacy in HIV-1 and chronic hepatitis B is established, and mechanistically it may be applicable to closely related lentiviruses.

SIV and the chimeric SHIV viruses are close relatives of HIV with reverse transcriptases that tenofovir is expected to inhibit. This is why macaque studies of tenofovir have been widely used to test pre-exposure prophylaxis (PrEP), mother-to-child transmission prevention and antiretroviral regimens.

SIV infection is not a human clinical condition. The prediction therefore mainly confirms the drug's known antiviral activity and its value as a translational model. It does not point to a new treatment option for patients.

The other predictions are weaker still:
- **Feline acquired immunodeficiency syndrome:** a single veterinary study of combination antiretroviral therapy. It is not relevant to human repurposing.
- **Neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (score 99.95%): no evidence and no plausible mechanistic link.
- **Familial combined hyperlipidaemia** (score 99.60%): no evidence, and the disease term is marked obsolete in the ontology, so it should be remapped before any further review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Of the 18 publications, none is a randomised trial. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal study | J Infect Dis | Weekly tenofovir disoproxil fumarate (TDF) gave partial protection against repeated intrarectal SHIV challenges in macaques |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study | J Infect Dis | Emtricitabine/TDF prevented vaginal SHIV infection in macaques co-infected with *Chlamydia trachomatis* and *Trichomonas vaginalis* |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study | J Infect Dis | Oral emtricitabine/TDF was tested against a tenofovir-resistant SHIV carrying the K65R mutation in macaques |
| [24043812](https://pubmed.ncbi.nlm.nih.gov/24043812/) | 2013 | Animal study | PNAS | A TDF-eluting intravaginal ring completely protected macaques from repeated vaginal SHIV challenges |
| [27275923](https://pubmed.ncbi.nlm.nih.gov/27275923/) | 2016 | Animal study | PLoS One | A pod-intravaginal ring delivering TDF and emtricitabine protected macaques from multiple SHIV exposures |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal study | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 were evaluated in infant macaques against repeated oral SIV challenges |
| [12404171](https://pubmed.ncbi.nlm.nih.gov/12404171/) | 2002 | Animal study | J Infect Dis | Low-dose topical (oral) TDF was tested for protecting infant macaques from SIV exposures |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal study | AIDS Res Hum Retroviruses | A virus-like particle vaccine combined with partially protective oral PrEP prevented SHIV infection in macaques |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal study | J Infect Dis | In SIV-infected macaques, HAART reduced central nervous system viral replication and inflammation, but viral DNA persisted |
| [14557287](https://pubmed.ncbi.nlm.nih.gov/14557287/) | 2003 | Review | Clin Microbiol Rev | Review of the clinical potential of cidofovir, adefovir and tenofovir against DNA virus and retrovirus infections |

Further publications include reviews of PrEP (PMID 20874040, 22964889), a pharmacokinetic study of TDF in HIV-infected pregnant women and their infants (PMID 21896911) and several other macaque studies.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010H0AAAAAA | Tenofovir Disoproxil Tab 245 mg | Not recorded | Not recorded |

The data compiled for this report show one valid single-ingredient authorisation. The identifier appears to be a BNF-style product code rather than an MHRA "PL" number, so it should be checked against the MHRA register. Dosage form, manufacturer and approved indication text are not recorded, and NICE appraisal information is not available here.

---

## Safety Considerations

Safety information from product labelling and drug interaction records was not available for this report. The only data are drug–disease contraindication links from the TxGNN knowledge graph. These are model-derived associations, not label text, and should be verified against the SmPC. They include:

- **Renal and hepatic:** kidney disease, liver disease, liver failure, Fanconi renotubular syndrome, lactic acidosis, fatty liver disease, non-alcoholic steatohepatitis
- **Bone and mineral:** hypophosphataemia, osteomalacia, rickets
- **Cardiac:** long QT syndrome, torsades de pointes
- **Other:** chronic hepatitis C virus infection, hypertriglyceridaemia, obesity, epilepsy, and several psychiatric disorders

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supported prediction (SIV infection) rests entirely on preclinical macaque studies and is a model of the already-approved HIV indication, not a new human use. The remaining predictions have no evidence or are of doubtful validity.

**To proceed, the following is needed:**
- Reframing the SIV result as supporting evidence for the existing HIV indication rather than a new indication
- Remapping the obsolete hyperlipidaemia term and reviewing the other low-evidence predictions
- Mechanism of action data and label-based safety data (warnings, contraindications, interactions) from the SmPC and BNF
- Verification of the UK authorisation record (MHRA PL number, dosage form, approved indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

