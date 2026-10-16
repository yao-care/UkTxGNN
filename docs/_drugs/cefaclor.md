---
layout: default
title: Cefaclor
parent: Model Prediction Only (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefaclor: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, tonsillitis, streptococcal infection…"
---

# Cefaclor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Cefaclor: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefaclor is a second-generation cephalosporin antibiotic, originally used for bacterial infections such as urinary tract infection, pharyngitis, tonsillitis and pneumonia.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **no clinical trials** and **no publications** supporting this prediction, and the prediction appears to be a network artefact.
The only prediction in the top 10 with a body of direct literature is **gonococcal urethritis** (6 publications, mostly from 1979–1997), which is an extension within the antibacterial class rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, tonsillitis, streptococcal infection, respiratory tract infection, pharyngitis, pneumonia (the MHRA licence record does not include indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 97.70% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, cefaclor is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections of the respiratory and urinary tracts is established.

For **hyperamylasemia**, no plausible mechanistic link was identified. Hyperamylasemia is a laboratory finding rather than an infectious disease, and an antibacterial has no recognised role in treating it. The high TxGNN score appears to be an artefact of network propagation. Several other top-ranked predictions (polyclonal hyperviscosity syndrome, monoclonal gammopathy, congenital analbuminemia, premalignant haematological disease and blood group incompatibility) show the same pattern and have no mechanistic rationale.

Some lower-ranked predictions are biologically more coherent:
- **Gonococcal urethritis (score 97.48%)**: plausible, as cefaclor inhibits penicillin-binding proteins and has in vitro activity against *Neisseria gonorrhoeae*. However, current guidance favours ceftriaxone because of rising resistance, so modern relevance is limited.
- **Uterine inflammatory disease and xanthogranulomatous pyelonephritis**: indirectly plausible as infectious conditions (cefaclor is already used for urinary tract infections), but there is no direct evidence. Cefaclor has limited anaerobic coverage, and pyelonephritis of this type is usually managed surgically.
- **Ureaplasma urethritis**: biologically implausible, as *Ureaplasma* lacks a cell wall and beta-lactams are expected to be intrinsically ineffective.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia, or for any of the other top-10 predicted indications.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For reference, the following publications relate to the rank 4 prediction, gonococcal urethritis. They are historical and do not support the primary prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6225482](https://pubmed.ncbi.nlm.nih.gov/6225482/) | 1983 | Randomised comparative study | Br J Vener Dis | 400 men randomised to spectinomycin, cefamandole or cefaclor (3 g, with or without probenecid). Cure rates were 98.9% (spectinomycin), 70.8% (cefamandole), 95.8% (cefaclor + probenecid) and 89.6% (cefaclor alone) |
| [116373](https://pubmed.ncbi.nlm.nih.gov/116373/) | 1979 | Randomised trial | Sex Transm Dis | Cefaclor 2, 3 and 4 g, with or without probenecid, given daily for three days in men with uncomplicated gonococcal urethritis |
| [121455](https://pubmed.ncbi.nlm.nih.gov/121455/) | 1979 | Clinical study | Postgrad Med J | 40 men with uncomplicated gonococcal urethritis treated with a 1 g loading dose of cefaclor; good in vitro activity against *N. gonorrhoeae* |
| [9582471](https://pubmed.ncbi.nlm.nih.gov/9582471/) | 1997 | Clinical study | Genitourin Med | Reassessed cefaclor as an alternative to third-generation cephalosporins in developing-world settings |
| [6400040](https://pubmed.ncbi.nlm.nih.gov/6400040/) | 1984 | Clinical study | Med J Malaysia | Single-dose oral cefaclor in men with uncomplicated gonococcal urethritis |
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Case series (different drug) | Curr Med Res Opin | Primarily on cefetamet pivoxil; cefaclor used only as a comparator, so this is indirect evidence |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501021A0AAAEAE | Cefaclor capsules 500 mg | Capsule (not stated in the record) | Not stated in the record |

The authorisation record available for this report does not include the indication text, manufacturer or a standard PL number. Please confirm details against the MHRA record and the BNF (cephalosporins, section 5.1.2).

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (these are graph-derived, not label text): *Clostridium difficile* colitis and perinatal necrotising enterocolitis.
- **Drug interactions**: 69 interactions were identified. Those graded Moderate are:
  - Balsalazide
  - Picosulfuric acid
  - Magnesium hydroxide
  - Aluminium hydroxide

  Many others (for example pantoprazole, omeprazole, lansoprazole, cimetidine, metformin, morphine, doxycycline, prednisone, simvastatin) have an unknown severity grade.

For warnings and full contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hyperamylasemia, has no clinical trials, no literature and no plausible mechanism, so it is best regarded as a model artefact (evidence level L5). Gonococcal urethritis has some historical clinical data (L3) but is an in-class extension of limited modern relevance, given resistance and the use of ceftriaxone.

**To proceed, the following is needed:**
- Mechanism of action data to support any mechanistic-link analysis
- SmPC warnings and contraindications for UK-licensed cefaclor products, plus the indication text, dosage form and manufacturer for the MHRA authorisation
- For gonococcal urethritis, a review of current UK guidance and local resistance data before any further consideration
- For the non-infectious predictions, no further work unless a credible mechanistic hypothesis emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

