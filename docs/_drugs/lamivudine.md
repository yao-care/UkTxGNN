---
layout: default
title: Lamivudine
parent: Model Prediction Only (L5)
nav_order: 359
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Lamivudine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Lamivudine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "chronic hepatitis C virus infection"]
---

# Lamivudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Lamivudine: From Chronic Hepatitis B and HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lamivudine is a nucleoside reverse transcriptase inhibitor originally used to treat chronic hepatitis B and HIV infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection in cats)**, with **no registered clinical trials** and **3 veterinary publications**.
This is an animal disease, so the prediction has limited relevance to human drug repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection; HIV infection; AIDS (the UK licence record contains no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (observational veterinary data only; no human trials) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lamivudine is a nucleoside reverse transcriptase inhibitor (NRTI). Its efficacy in HIV and hepatitis B is established, and mechanistically it may be applicable to other lentiviruses that rely on a similar reverse transcriptase.

Feline immunodeficiency virus (FIV) is a lentivirus that causes an AIDS-like illness in cats. Its reverse transcriptase is related to that of HIV-1, so an NRTI effect is biologically plausible. Some reverse transcriptase inhibitors active against HIV are also active against FIV.

However, the supporting studies are veterinary and indirect to human use. Only titles and partial abstracts were available, so the study designs could not be fully verified. The prediction is therefore best treated as a research question rather than a human repurposing opportunity.

Other predictions in the data were weaker:
- **Simian immunodeficiency virus infection** (evidence level L4, Hold): supported only by macaque and in vitro studies. Lamivudine is already approved for HIV in humans, so this is not a distinct human indication.
- **Chronic hepatitis C virus infection** (L4, Hold): likely a false-positive signal from literature that mentions HBV and HCV together. Lamivudine has no recognised activity against HCV.
- **Two further predictions** (a neurodevelopmental disorder and an obsolete hyperlipidaemia term): model prediction only, with no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohort (veterinary) | Viruses | Compared zidovudine alone and with interferon-α, lamivudine or valproic acid in naturally FIV-infected cats over one year, assessing clinical status, viral load and CD4+/CD8+ ratios |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohort (veterinary) | Journal of Feline Medicine and Surgery | Long-term (5–6 years) antiretroviral therapy follow-up in FIV-infected cats, starting with zidovudine |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Preclinical | Antiviral Research | Combined zidovudine, lamivudine and abacavir suppressed in vitro FIV replication; FIV is a recognised animal model for HIV |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010Q0AAADAD (BNF-style code; not a PL number) | Lamivudine 100 mg tablets | Tablet | Not stated in the available record |

## Cytotoxicity

Lamivudine is an antiviral, not an antineoplastic drug, so this section does not apply.

## Safety Considerations

**Conditions linked to lamivudine in the knowledge graph** (these are graph associations, not label text, and should be checked against the SmPC):
- Liver: liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis
- Kidney: kidney disease
- Pancreas and gallbladder: pancreatitis, gallbladder disease
- Muscle: myopathy, muscular disease, skeletal muscle disease, myositis, dermatomyositis, familial periodic paralysis
- Blood: neutropenia, agranulocytosis, anaemia, macrocytic anaemia
- Metabolic: lactic acidosis, hypertriglyceridaemia, obesity disorders
- Other: pyoureter

**Drug interactions:** 100 potential interactions were recorded. The ones graded Moderate are:
- Lactitol
- Mannitol
- Naltrexone
- Orlistat
- Sorbitol

Many others have an unknown severity grade, including metformin, cimetidine, omeprazole, pantoprazole, lansoprazole, morphine, vancomycin, amphotericin B, and rosiglitazone.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an animal disease, supported only by veterinary cohort and in vitro data, with no clinical trials. It therefore does not represent a human repurposing opportunity. Lamivudine is already established for HIV and hepatitis B.

**To proceed, the following is needed:**
- A decision on whether a veterinary development pathway is of interest, as this falls outside human repurposing
- Detailed mechanism of action data
- Full-text review of the veterinary studies to verify design and outcomes
- Approved indication text and licence details for the UK product, plus SmPC warnings and contraindications
- Review of higher-priority human-relevant predictions, if any are identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

