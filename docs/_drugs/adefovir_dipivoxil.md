---
layout: default
title: Adefovir Dipivoxil
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 9
monitor_inn: "Adefovir dipivoxil"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "hepatitis C virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection"]
last_modified_at: 2026-10-30
description: "Adefovir Dipivoxil: predicted new indication chronic hepatitis C virus infection (evidence level L5). Approved use: Not recorded in the local data"
---

# Adefovir Dipivoxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Adefovir dipivoxil: nucleotide analogue reverse transcriptase/polymerase inhibitor → chronic hepatitis C virus infection
{: .text-alpha }

## One-Sentence Summary

Adefovir dipivoxil is an oral nucleotide analogue antiviral that is marketed in the UK. The TxGNN model predicts it may be useful for **chronic hepatitis C virus infection**, but the data compiled for this report contain **no clinical trials** and **no publications** that directly study adefovir in this disease. The prediction is supported by model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | chronic hepatitis C virus infection |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Adefovir dipivoxil is a prodrug of adefovir, an acyclic nucleotide phosphonate that inhibits viral DNA polymerase/reverse transcriptase. This is its established mechanism against hepatitis B virus (HBV) and retroviruses.

Hepatitis C virus (HCV) is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, a different enzyme. No mechanistic link between adefovir and HCV has been established. The retrieved publications are general viral hepatitis reviews and HBV-focused papers, not studies of adefovir activity against HCV. The high score probably reflects closeness of viral hepatitis nodes in the model's network rather than pharmacology, so the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered for chronic hepatitis C virus infection.

## Literature Evidence

The publications retrieved are mainly general reviews of viral hepatitis treatment. None reports adefovir activity in HCV infection. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | Overview of chronic viral hepatitis treatment; adefovir discussed in the hepatitis B context |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Not classified | Dig Dis | Established and emerging viral hepatitis therapies; adefovir listed as licensed for hepatitis B only |
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Not classified | Recent Pat Anti-Infect Drug Discov | Pegylated interferons for chronic hepatitis B; adefovir among approved HBV drugs |
| [16107195](https://pubmed.ncbi.nlm.nih.gov/16107195/) | 2005 | Not classified | Expert Rev Anti Infect Ther | Peginterferon alfa-2a for hepatitis B; adefovir monotherapy described as unsatisfactory |
| [15918324](https://pubmed.ncbi.nlm.nih.gov/15918324/) | 2004 | Not classified | Lijec Vjesn | Treatment and prevention of viral hepatitis |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline/Consensus | Orv Hetil | Hungarian consensus guideline for hepatitis B, C and D |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Not classified | Med Chem | Bicyclol for chronic hepatitis B and C; not related to adefovir |
| [24797262](https://pubmed.ncbi.nlm.nih.gov/24797262/) | 2014 | Not classified | Viral Immunol | Cytokine profiles and HBeAg seroconversion after stopping antiviral therapy in hepatitis B |
| [31572002](https://pubmed.ncbi.nlm.nih.gov/31572002/) | 2019 | Not classified | Cancer Manag Res | Nucleos(t)ide analogue therapy and survival in HBV-related small hepatocellular carcinoma |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503030B0AAAAAA | Adefovir Dipivoxil Tab 10mg | Not recorded | Not recorded |

The local data show one valid single-ingredient authorisation. The BNF classification code appears to be embedded in the record number (section 5.3.3.2, chronic hepatitis B antivirals), but the indication text is not recorded.

## Safety Considerations

- **Contraindications and warnings (label text):** Not available in the data compiled for this report. Please refer to the SmPC and BNF.
- **Drug Interactions:** 25 potential interactions were identified, none with a graded severity. Examples include pantoprazole, omeprazole, lansoprazole, rabeprazole, ranitidine, famotidine, morphine, warfarin, heparin, ibuprofen, prednisolone, kanamycin and potassium chloride. Review each combination against the SmPC and BNF.
- **Other cautions:** Renal toxicity is a recognised dose-limiting effect of adefovir, and the literature describes kidney injury during long-term therapy. Lactic acidosis and liver disease (fatty liver, steatohepatitis) are also relevant concerns for this drug class. Monitor renal function.

Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications of adefovir in chronic hepatitis C, and there is no plausible mechanism, since HCV is an RNA virus not targeted by this DNA polymerase inhibitor. Direct-acting antivirals already exist for HCV.

**To proceed, the following is needed:**
- Laboratory evidence of anti-HCV activity (for example replicon assays)
- A defensible mechanistic rationale for activity against NS5B or other HCV targets
- Mechanism of action data and label safety information (warnings, contraindications) for the UK product
- A benefit-risk assessment that addresses nephrotoxicity against current HCV standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

