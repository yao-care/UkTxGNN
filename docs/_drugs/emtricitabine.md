---
layout: default
title: Emtricitabine
parent: Model Prediction Only (L5)
nav_order: 249
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Emtricitabine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Emtricitabine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Emtricitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Emtricitabine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this is an animal (non-human primate) disease, and the evidence consists of **0 clinical trials** and **20 publications**, almost all of them preclinical macaque studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the UK authorisation record has no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical studies only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) that acts on HIV reverse transcriptase. Its efficacy in HIV infection is established, and it may be mechanistically applicable to SIV.

SIV and SHIV (a chimeric simian-human virus) are closely related lentiviruses with a homologous reverse transcriptase, so the antiviral mechanism plausibly carries over. Macaque studies report protection against SIV/SHIV challenge with emtricitabine combined with tenofovir (disoproxil or alafenamide) as pre-exposure prophylaxis (PrEP).

An important caveat: SIV is a veterinary and preclinical model pathogen, not a human disease. These data are indirect support for the already approved human HIV use and are not evidence for a new human indication. The high TxGNN score probably reflects the close similarity to the approved HIV indication rather than a genuinely new therapeutic opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications are mainly macaque PrEP studies and reviews. Of the 20 retrieved, the most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal study | J Infect Dis | Oral emtricitabine plus tenofovir alafenamide protected macaques from repeated rectal SHIV exposure |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study | J Infect Dis | Emtricitabine/tenofovir disoproxil fumarate prevented vaginal SHIV infection in macaques coinfected with *Chlamydia trachomatis* and *Trichomonas vaginalis* |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal study | J Infect Dis | Oral tenofovir alafenamide/emtricitabine or tenofovir alafenamide alone against vaginal SHIV infection in macaques |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal study | AIDS Res Hum Retroviruses | Virus-like particle HIV vaccine combined with partially protective oral PrEP prevented SHIV infection in macaques |
| [21632769](https://pubmed.ncbi.nlm.nih.gov/21632769/) | 2011 | Animal study | J Virol | Intermittent Truvada prophylaxis protected against an emtricitabine-resistant (M184V) SHIV |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study | J Infect Dis | Oral emtricitabine/tenofovir disoproxil fumarate against a tenofovir-resistant (K65R) SHIV in macaques |
| [22814162](https://pubmed.ncbi.nlm.nih.gov/22814162/) | 2012 | Animal study | Jpn J Infect Dis | Double oral dose of emtricitabine/tenofovir before exposure protected macaques against highly pathogenic SHIV |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Preclinical virology | J Virol | M184V mutants emerged within 5 weeks in SIV-infected newborn macaques treated with lamivudine or emtricitabine; the mutant showed reduced fitness |
| [22964889](https://pubmed.ncbi.nlm.nih.gov/22964889/) | 2012 | Review | Curr Opin HIV AIDS | Lessons from animal models of antiretroviral prophylaxis and next steps in preclinical PrEP research |
| [22918448](https://pubmed.ncbi.nlm.nih.gov/22918448/) | 2012 | Review | Curr Opin HIV AIDS | Considerations on antiretroviral chemoprophylaxis in men who have sex with men |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010K0AAAAAA (record identifier; not a standard PL number) | Emtricitabine capsule 200 mg | Capsule (strength 200 mg) | Indication text not recorded |

The record is a single-ingredient product with valid status. BNF classification and NICE appraisal details were not available in the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from network-derived drug-disease edges, not from label text, and should be verified against the SmPC):
- Hepatic and metabolic: liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis, hypertriglyceridemia
- Viral hepatitis: chronic hepatitis B and hepatitis C virus infection
- Renal and bone: kidney disease, Fanconi renotubular syndrome, hypophosphatemia, osteomalacia, rickets
- Cardiac: long QT syndrome, torsades de pointes
- Neuropsychiatric: epilepsy, anxiety and related disorders, delusional disorder, paranoid schizophrenia

**Drug interactions** (20 recorded; the major ones are listed):
- **Major:** leflunomide, teriflunomide
- **Moderate (examples):** cobicistat, methotrexate, interferon beta-1a/1b, cladribine, clofarabine, orlistat, naltrexone

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection is a non-human disease, no clinical trials exist, and the supporting evidence is preclinical (L4) macaque work. It supports the existing human HIV indication rather than any new human use. The high TxGNN score most likely reflects similarity to the approved indication.

**To proceed, the following is needed:**
- Identification of a genuine new human indication, as SIV infection is not a human disease
- Mechanism of action data (currently unavailable)
- Complete UK authorisation details (indication text, dosage form, PL number)
- Label-based warnings and contraindications from the SmPC and BNF, to confirm the knowledge-graph signals

**Other predictions in the data (not recommended for progression):**
- *Feline acquired immunodeficiency syndrome* (score 99.92%): a veterinary indication with a single animal publication (L4); Hold.
- *Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter* (score 99.92%): no trials or literature and no plausible mechanistic link (L5); likely a computational artefact; Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

