---
layout: default
title: Etravirine
parent: Model Prediction Only (L5)
nav_order: 269
evidence_level: L5
indication_count: 8
monitor_inn: "Etravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-30
description: "Etravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease and AIDS"
---

# Etravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Etravirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **no clinical trials** and **no publications** that directly study this condition, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease and AIDS (relation recorded in the knowledge graph; the UK licence record contains no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, etravirine is an NNRTI that inhibits HIV-1 reverse transcriptase, and its use in HIV infection is recorded in the knowledge graph.

Feline immunodeficiency virus (FIV) is a lentivirus, which is why a model that relies on network similarity to HIV and AIDS would rank it highly. However, the reverse transcriptase of FIV differs structurally from that of HIV-1, and NNRTIs are generally poorly active against it. The high score therefore most likely reflects similarity to the original HIV indication rather than demonstrated activity. This should be regarded as a weak, unconfirmed hypothesis. Feline AIDS is also a veterinary condition, so human prescribing guidance does not directly apply.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For context, the second-ranked prediction (simian immunodeficiency virus infection) has one linked paper, which is an in vitro study of nanoparticle-based antiretroviral combinations against HIV. It does not study this predicted disease and is not evidence for it:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical (in vitro) | Molecular Pharmaceutics | Nanocarrier-delivered antiretroviral combinations assessed for synergistic inhibition of cell-free and cell-to-cell HIV transmission |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010AFAAAAAA | Etravirine Tab 100mg | Not stated | Not stated in the licence record |

The identifier shown appears to be a BNF-style classification code rather than a PL number. The record is a single-ingredient product and is listed as valid. The indication text is absent, so no approved indication can be confirmed from these data.

## Safety Considerations

- **Knowledge-graph contraindication relations** (not label text): chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease, and peripheral neuropathy. These should be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified in the interaction database. Most of those listed are of moderate severity, including:
  - Proton pump inhibitors and H2 blockers: omeprazole, rabeprazole, cimetidine (minor for ranitidine)
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Antidiabetic agents: pioglitazone, saxagliptin, linagliptin, glimepiride, chlorpropamide
  - Others: clarithromycin, metronidazole, aprepitant, eliglustat, naloxegol, naldemedine, dronabinol

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no trials or publications on feline acquired immunodeficiency syndrome, and known differences between FIV and HIV-1 reverse transcriptase make activity unlikely. The high score appears to reflect similarity to the original HIV indication. Other predictions for this drug (simian immunodeficiency virus infection, benign tumours, a rare neurodevelopmental disorder, obsolete familial combined hyperlipidaemia) are also unsupported by any direct evidence.

**To proceed, the following is needed:**
- Direct in vitro or in vivo data on etravirine activity against FIV reverse transcriptase
- Mechanism of action data and SmPC warnings and contraindications for the UK product
- Confirmation of the licensed indication text, dosage form and PL number
- A veterinary regulatory and pharmacological assessment, since the target condition is not a human disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

