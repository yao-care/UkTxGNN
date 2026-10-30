---
layout: default
title: Abacavir
parent: Model Prediction Only (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
monitor_inn: "ABACAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Abacavir: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease and AIDS"
---

# Abacavir
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

## Abacavir: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, a non-human primate disease.
Support is weak: **0 clinical trials** and **1 publication** (an in vitro susceptibility study) are currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease and AIDS (relations recorded in the knowledge graph; the UK licence record has no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

The evidence level is L5. The only publication is an in vitro study of HIV-2, SIV and SHIV susceptibility to anti-HIV-1 compounds. It does not directly study SIV infection as a treatment indication for abacavir in a way that supports a higher level.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Abacavir is generally understood to be a nucleoside reverse transcriptase inhibitor (NRTI). It is phosphorylated intracellularly to carbovir triphosphate, which terminates viral DNA chain elongation.

SIV is a lentivirus closely related to HIV and also relies on reverse transcriptase. Inhibition of this enzyme is therefore mechanistically plausible. However, SIV infects non-human primates and is not a human clinical indication. Its main value is as a preclinical model of HIV, so the prediction offers little repurposing value for patients.

Two other predictions were also returned:
- **Feline acquired immunodeficiency syndrome** (score 0.9979): a 2002 animal study of zidovudine, lamivudine and abacavir combined suppressed feline immunodeficiency virus (FIV) replication in vitro. The effect of abacavir alone cannot be isolated, and this is not a human indication.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (score 0.9978): no trials, no literature and no evident mechanistic link. The high score is likely a TxGNN model (deep learning) artefact and should not be read as evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Evaluated 16 approved drugs and one experimental drug against HIV-2, SIV and SHIV strains, to guide treatment and post-exposure prophylaxis. Indirect evidence only. |

For the second predicted indication (feline AIDS), one further study is available: [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) (2002, *Antiviral Research*), an animal study of combined zidovudine, lamivudine and abacavir against FIV replication in vitro.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010E0AAAAAA | Abacavir tablets 300 mg | Not stated | Not stated in the available record |

This is a single-ingredient product with valid status. The identifier appears to be a BNF-style code rather than an MHRA PL number, so the authorisation details should be checked against MHRA records.

## Safety Considerations

**Contraindications recorded in the knowledge graph** (drug-disease relations, not label text): liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, pancreatitis, gallbladder disease, lactic acidosis, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), hypertriglyceridaemia, obesity disorders, myopathy and other muscle diseases (including myositis and dermatomyositis), familial periodic paralysis, and pyoureter.

**Drug Interactions:** 93 interactions are recorded. The main ones with a rated severity are:
- Naltrexone (Moderate)
- Orlistat (Moderate)

Most of the remaining listed interactions (for example metformin, omeprazole, morphine, prednisone and vancomycin) have no severity rating.

Abacavir is also known for HLA-B*57:01-associated hypersensitivity. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indications are animal lentivirus infections, supported only by indirect in vitro or animal data and no clinical trials. They do not represent a meaningful human repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Licence indication text and dosage form for the UK product
- Label warnings and contraindications from the SmPC
- A clear human-relevant rationale before any further evaluation, as the current predictions concern non-human species or lack any supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

