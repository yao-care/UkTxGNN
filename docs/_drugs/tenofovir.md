---
layout: default
title: Tenofovir
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Tenofovir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "tenofovir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Tenofovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Tenofovir: From Chronic Hepatitis B and HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Tenofovir is a nucleotide reverse transcriptase inhibitor, originally used to treat chronic hepatitis B virus infection, HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (feline AIDS, caused by feline immunodeficiency virus)**,
but the supporting evidence is limited to **2 animal studies** and **no clinical trials**. The predicted "indication" is a veterinary disease, so its relevance to human drug repurposing is low.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection; HIV infection; AIDS (the marketing authorisation indication text is not available in the data compiled for this report) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 on the strict rules above (no clinical trials; animal studies only). The source data labels this L3, but the supporting studies are preclinical animal studies rather than observational studies or systematic reviews. |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tenofovir is a nucleotide analogue that terminates viral DNA chain elongation by inhibiting reverse transcriptase. Its efficacy in HIV and hepatitis B is established.

Feline immunodeficiency virus (FIV) is a lentivirus that causes progressive immune dysfunction in cats, similar to HIV in humans. Its reverse transcriptase is homologous to that of HIV-1, so the mechanism is biologically plausible.

Two caveats apply. First, the predicted indication is a non-human disease, so the prediction adds little to human repurposing. Second, the other high-scoring predictions are not more useful: simian immunodeficiency virus infection in macaques largely confirms the already-established antiretroviral and PrEP use, and a rare neurodevelopmental disorder (score 0.9996) has no identifiable mechanistic link, no trials and no literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal study | Viruses | Combination antiretroviral therapy (dolutegravir, tenofovir, emtricitabine) evaluated for pharmacokinetics and clinical outcomes in FIV-infected domestic cats |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Animal study | Journal of Feline Medicine and Surgery | Treatment of naturally FIV-infected cats with PMPA (tenofovir); the authors note that human antiviral drugs used in cats have previously caused serious adverse effects |

For context, the related prediction of simian immunodeficiency virus infection is supported by many macaque studies (for example [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) and [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/)) showing protection against SHIV acquisition. These are preclinical and confirm the known antiretroviral mechanism rather than a new human use.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010AABBAAAA | Truvada Tab 200mg/245mg | Not available | Not available |
| 0503010AAAAAAAA | Emtricitabine/Tenofovir Tab 200mg/245mg | Not available | Not available |

Both authorisations are valid single-ingredient entries. The identifiers shown are those in the data compiled for this report and appear to be BNF-style codes rather than MHRA "PL" numbers, so they should be verified against the MHRA register.

## Safety Considerations

- **Contraindications and warnings (TxGNN model associations, not label text):** The TxGNN model (deep learning) links tenofovir to conditions including liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis, kidney disease, Fanconi renotubular syndrome, hypophosphatemia, osteomalacia, rickets, long QT syndrome, torsades de pointes, and hepatitis C virus infection. These associations come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They must be checked against the SmPC.
- **Resistance consideration:** Tenofovir-selected SIV variants were unevenly distributed across anatomical sites in macaques (PMID 14963139), which is relevant to resistance.
- **Drug interactions:** No interaction data was found.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a veterinary disease supported only by two animal studies, with no human clinical trials. The prediction has little relevance to human repurposing, and tenofovir is already established for HIV and hepatitis B.

**To proceed, the following is needed:**
- Confirmation of whether a veterinary development question is in scope, since this is outside human repurposing
- Mechanism of action data (currently unavailable)
- SmPC warnings and contraindications for the UK-authorised products, plus the approved indication text and dosage forms
- Interaction data
- If a human question is of interest, a review of the other predicted indications with a clearer human disease link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

