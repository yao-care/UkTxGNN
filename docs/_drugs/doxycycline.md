---
layout: default
title: Doxycycline
parent: Moderate Evidence (L3-L4)
nav_order: 241
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Doxycycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L4). Approved use: Bronchitis, acne, bacterial pneumonia, anthrax…"
monitor_inn: "Doxycycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
---

# Doxycycline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a tetracycline antibiotic, originally used for bronchitis, acne, bacterial pneumonia, anthrax, gonorrhoea and other bacterial infections.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but the supporting evidence is very thin: **no clinical trials** and **1 publication** (a 1992 case report).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, acne, bacterial pneumonia, anthrax, gonorrhoea and other bacterial infections (taken from the knowledge-graph indication list; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, doxycycline is a tetracycline-class antibiotic with proven efficacy against a range of bacterial infections, including *Chlamydia trachomatis*, and mechanistically may be applicable to ocular surface disease.

The only publication identified describes two patients with chlamydial follicular conjunctivitis who were treated with oral tetracycline or doxycycline. Their follicles resolved, but they then developed recurrent punctate epithelial keratitis. This indicates a link to a chlamydial infection that doxycycline treats, rather than a direct benefit of the drug on the keratitis. Tetracyclines are also known to have anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects, which could plausibly help ocular surface inflammation, but this is a hypothesis and has not been tested here. The evidence is indirect and does not constitute a distinct repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two cases of chlamydial follicular conjunctivitis treated with oral tetracycline or doxycycline. Follicles resolved, but recurrent bilateral punctate epithelial keratitis followed. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BNF code 0501030Z0AAAAAA (no PL number available) | Doxycycline 40 mg modified-release capsules | Capsule (modified-release) | Not available in the data compiled for this report |

Only one valid single-ingredient authorisation is recorded. The BNF code (section 5.1.3, tetracyclines) places the product among the tetracycline antibacterials. Manufacturer and approved indication details were not available.

## Safety Considerations

- **Contraindication signals (knowledge-graph, not label text)**: *Clostridium difficile* colitis, perinatal necrotising enterocolitis, and oesophageal dyskinesia.
- **Drug Interactions**: 100 interactions were recorded; examples of those flagged as **Major** include:
  - Isotretinoin
  - Acitretin
  - Aminolevulinic acid

  Moderate interactions include aluminium hydroxide, aminophylline, amoxicillin, ampicillin and bedaquiline. Minor interactions include acetazolamide and amiloride.
- **Ocular/otic use**: an in vitro study found tetracyclines less cytotoxic to tympanic membrane fibroblasts than quinolones, so this is a consideration for any topical use, though it is not specific to the ocular indication.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only supporting evidence is a single 1992 case report in which doxycycline treated the underlying chlamydial infection. There are no trials, and the UK-authorised product (a 40 mg modified-release capsule) is not designed for ocular indications.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether anti-inflammatory or MMP-inhibiting effects are relevant to punctate epithelial keratoconjunctivitis
- Identification of controlled clinical studies (human) in non-infectious punctate keratitis
- The approved indication text and SmPC warnings and contraindications for the UK-authorised product
- Assessment of route and formulation suitability for ocular use

### Other Predicted Indications Reviewed (for context)

Other predictions were also reviewed. They are not the focus of this report.
- **Post-bacterial disorder** and **post-infectious syndrome** (evidence level L1 by trial count): the trials mainly concern doxycycline post-exposure prophylaxis for sexually transmitted infections. This is infection prevention, not treatment of a post-infectious condition, and the disease mapping is loose. Antimicrobial resistance is a concern.
- **Chronic gingivitis** (L2): there are studies of local and subantimicrobial-dose doxycycline as an adjunct to scaling and root planing, but mostly in periodontitis rather than gingivitis alone, and no trials were registered. This is the most clinically developed of the other candidates.
- **Otitis externa, post-infectious vasculitis, infective urethral stricture, exposure keratitis, Chagas cardiomyopathy**: evidence is weak, off-target or negative, so these are on hold.
- **Infection-related haemolytic uraemic syndrome**: model prediction only, with a plausible safety concern, since antibiotics are generally avoided in Shiga toxin-producing *E. coli* infection.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

