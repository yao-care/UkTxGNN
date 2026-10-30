---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
monitor_inn: "Aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-30
description: "Aztreonam: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, Pseudomonas aeruginosa infection…"
---

# Aztreonam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Aztreonam: From Gram-Negative Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, recorded in the knowledge graph for gram-negative infections such as urinary tract infection, Pseudomonas aeruginosa infection, peritonitis and Escherichia coli infection.
The TxGNN model's top-ranked prediction is **hyperamylasemia**, but **no clinical trials and no publications** support it, and no plausible mechanistic link has been identified.
The better-supported (though still limited) candidate in this list is **gonococcal urethritis**, with 6 publications (one 2020 single-arm open-label trial and several 1980s studies).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, Pseudomonas aeruginosa infection, peritonitis, rhinoscleroma, Escherichia coli infection, endometritis (relations recorded in the knowledge graph; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, aztreonam is a monobactam that inhibits bacterial penicillin-binding protein 3 (PBP3) and acts against gram-negative bacteria.

For hyperamylasemia, there is no plausible link. Amylase elevation is not an infective process that a cell-wall-targeting antibacterial would be expected to correct. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The second and third predictions (polyclonal hyperviscosity syndrome and congenital analbuminemia) are similarly implausible, as aztreonam has no action on immunoglobulin or albumin biology.

Among the other predictions, **gonococcal urethritis** is biologically plausible, since aztreonam has in vitro activity against *Neisseria gonorrhoeae*. However, this is a close extension of its existing antibacterial spectrum rather than a novel repurposing, and aztreonam-resistant gonococci have been reported.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia (and none for any of the other top-10 predicted indications).

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For context, the literature retrieved for the most evidence-supported alternative prediction, gonococcal urethritis, is below. These do not support the lead prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm open-label trial | Antimicrob Agents Chemother | Single intramuscular 2 g aztreonam dose tested for *N. gonorrhoeae*, motivated by ceftriaxone-resistance concerns |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical study | Antimicrob Agents Chemother | Aztreonam 1 g IM vs spectinomycin 2 g IM: no failures with either drug in uncomplicated gonorrhoea |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical study | Genitourin Med | Single 1 g IM dose cleared infection in 61 men and 26 women at all sites except one pharyngeal infection |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro / effectiveness study | J Infect Dis | Activity against penicillin-resistant gonococci |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic and therapeutic study | Hinyokika Kiyo | Single-dose aztreonam therapy for gonorrhoeal infections |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance surveillance | J Infect Chemother | Emergence of cephem- and aztreonam-highly-resistant non-β-lactamase-producing gonococci |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501023A0AAAFAF | Aztreonam powder and solvent for nebuliser solution, 75 mg vial with device | Nebuliser solution (powder and solvent) | Not stated in the available record |

Only one single-ingredient authorisation is listed. The record does not include approved indication text, so no approved indications can be stated from it.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: contraindication relations are recorded for kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and bronchial disease. These should be verified against the SmPC.
- **Drug Interactions**: 27 interactions were identified in total. Those graded Moderate are picosulfuric acid, dicoumarol and warfarin (monitor anticoagulant effect). Others, graded Unknown, include vancomycin, amikacin, metronidazole, amphotericin B, tacrolimus, heparin, aciclovir, fluconazole, morphine, ondansetron and several proton pump inhibitors (omeprazole, pantoprazole, lansoprazole).

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Hyperamylasemia has no supporting trials or publications and no plausible mechanism, so the evidence level is L5 (model prediction only). The same applies to the other highest-scoring predictions.

**To proceed, the following is needed:**
- Mechanism of action data and UK label text (warnings, contraindications, approved indications) for the listed product
- If a repurposing question is pursued, refocus on gonococcal urethritis, which would need modern comparative trial data, resistance surveillance and a review against current UK gonorrhoea guidance
- For hyperamylasemia, a clear biological hypothesis before any further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

