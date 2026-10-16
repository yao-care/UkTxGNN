---
layout: default
title: Didanosine
parent: Moderate Evidence (L3-L4)
nav_order: 221
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Didanosine: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infection and AIDS"
---

# Didanosine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Didanosine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Didanosine is an antiretroviral medicine originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but this is an animal-model disease rather than a human one, and there are **no clinical trials** and only **7 publications** (mostly preclinical) behind the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, didanosine is a nucleoside reverse transcriptase inhibitor (NRTI). After conversion inside cells to its active triphosphate form, it terminates viral DNA chain elongation. Its efficacy in HIV infection is established.

Simian immunodeficiency virus (SIV) is a lentivirus closely related to HIV and uses a homologous reverse transcriptase, so activity is mechanistically plausible. A pigtail macaque study reported that didanosine rescued animals from a lethal SIV challenge, and in vitro work has examined the susceptibility of HIV-2, SIV and SHIV to antiretrovirals.

However, SIV infection is an animal model of HIV, not a human disease. Its main value is as a translational proxy for HIV, which is already an established indication. The high TxGNN score most likely reflects this close similarity to the existing indication and should not be read as independent repurposing evidence.

The other two predictions were also reviewed and do not support repurposing:
- **Feline acquired immunodeficiency syndrome (rank 2):** the two papers describe an FIV animal model and mainly report didanosine-induced sensory neuropathy and mitochondrial impairment. This is a toxicity signal, not efficacy (evidence level L4, Hold).
- **Neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter (rank 3):** no trials, no literature and no plausible mechanistic link. It is a computational hypothesis only (evidence level L5, Hold).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

All publications below are preclinical. Only the first two directly address didanosine or its activity against SIV.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9282812](https://pubmed.ncbi.nlm.nih.gov/9282812/) | 1997 | Animal study (macaque) | AIDS Res Hum Retroviruses | Didanosine, but not high-dose hydroxyurea, rescued pigtail macaques from a lethal SIV challenge |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro study | Antivir Ther | Compared the activity of 16 approved antiretrovirals and AMD3100 against HIV-2, SIV and SHIV strains |
| [11435599](https://pubmed.ncbi.nlm.nih.gov/11435599/) | 2001 | In vitro study | J Virol | Dideoxynucleoside susceptibility of human foamy virus; only zidovudine was as effective as against HIV-1 |
| [14965468](https://pubmed.ncbi.nlm.nih.gov/14965468/) | 2004 | Animal model study | DNA Cell Biol | T-cell receptor excision circles as a surrogate marker in SHIV and SIV macaque models (not didanosine-specific) |
| [15668538](https://pubmed.ncbi.nlm.nih.gov/15668538/) | 2005 | In vitro study | AIDS | Hydroxyurea has a cytostatic but not immunosuppressive effect on T lymphocytes |
| [8870848](https://pubmed.ncbi.nlm.nih.gov/8870848/) | 1996 | Animal model study | AIDS Res Hum Retroviruses | Cytokine mRNA expression in tissues during acute SIVmac251 infection in macaques |
| [9145853](https://pubmed.ncbi.nlm.nih.gov/9145853/) | 1997 | In vitro study | Antimicrob Agents Chemother | Antiviral properties of the protease inhibitor palinavir (not didanosine-specific) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010N0AAAIAI | Didanosine gastro-resistant capsules 400 mg | Capsule (gastro-resistant) | Not stated in the data compiled for this report |

The identifier shown is a BNF-style code (BNF chapter 5, infections: antiviral, HIV) rather than a standard MHRA "PL" number. Please verify the current MHRA authorisation status and indication wording directly.

## Cytotoxicity

Didanosine is an antiviral NRTI, not an antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** the TxGNN knowledge graph links didanosine to a range of conditions, including kidney disease and impaired renal function, liver disease, peripheral neuropathy, diabetes mellitus and diabetic ketoacidosis, hypertriglyceridemia, coronary artery disease, hypercalcemia, nephrolithiasis and acute urate nephropathy. These come from graph edges and must be checked against the SmPC.
- **Neurotoxicity signal:** the FIV animal model study (PMID 17616550) reported didanosine-induced sensory neuropathy with mitochondrial and neurotrophic impairment. This is relevant to any neurological indication.
- **Drug interactions (DDInter, 100 interactions recorded; examples from the list reviewed):**
  - Moderate: acetylsalicylic acid, metronidazole, levofloxacin, naltrexone, nitisinone, orlistat, rosuvastatin, simvastatin, tinidazole
  - Minor: ranitidine, doxycycline, minocycline, tetracycline
  - Unknown severity: levocarnitine, amphotericin B, pantoprazole, glimepiride, morphine, metformin

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an animal-model disease with only preclinical evidence (L4), no clinical trials, and a score that largely reflects similarity to the existing HIV indication. It offers no clear new human therapeutic use, and the neurotoxicity signal adds a safety concern.

**To proceed, the following is needed:**
- A clear human clinical rationale, as SIV and FIV are not human diseases
- Mechanism of action data and the approved indication text for the UK product
- Label-based warnings and contraindications from the SmPC and BNF to replace knowledge-graph signals
- A review of whether the model's other predictions suggest any human indication beyond HIV, given the current lack of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

