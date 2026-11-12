---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
monitor_inn: "bacitracin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
last_modified_at: 2026-11-12
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Bacitracin
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

## Bacitracin: topical polypeptide antibacterial → punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Bacitracin is a topical polypeptide antibacterial that is marketed in the UK in ointment products.
The TxGNN model predicts it may be relevant to **punctate epithelial keratoconjunctivitis**, but there are currently **no clinical trials and no publications** directly studying this condition, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bacitracin is a polypeptide antibacterial that acts mainly against Gram-positive organisms and is used topically. Mechanistically, it could be relevant where a bacterial component is present on the ocular surface.

The predicted condition sits close to other ocular surface conditions in the model's data, which probably explains the high score. However, punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or non-infectious (for example toxic), and an antibacterial would be expected to offer limited benefit in those cases. The score therefore most likely reflects proximity to related eye conditions rather than a distinct, validated mechanism. No mechanistic validation is possible with the data available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

<!-- review:begin uk-lic-20261106-bacitracin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both authorisations are currently valid, and the data compiled for this report contain no indication text for them. Both are classed as single-ingredient records, but the second product name suggests a polymyxin/bacitracin preparation, so it should be checked against the product label before drawing conclusions about bacitracin alone." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 4 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-bacitracin-1 -->

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1310011W0BCAAAB | Polyfax ointment | Polymyxins |
| 1103010Q0BBAAAA | Polyfax ophthalmic ointment | Polymyxin B sulphate |
| 1103010Q0AAAAAA | Polymyxin B 10,000units/g / Bacitracin 500units/g eye oint | Polymyxin B sulphate |
| 1310011W0AAABAB | Polymyxin B 10,000units/g / Bacitracin 500units/g ointment | Polymyxins |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 84 interactions were identified in the data compiled for this report. Those classed as major include:
  - Kanamycin
  - Neomycin
  - Streptomycin
  - Deferasirox
  - Iodinated contrast agents (diatrizoate, iodipamide, iodixanol, iohexol)

  Moderate interactions include mesalazine, balsalazide, olsalazine, sulfasalazine, exenatide, vancomycin and picosulfuric acid. Interaction relevance depends strongly on route and extent of systemic exposure, which is low with topical use.
- **Conditions flagged for caution in the data**: kidney disease, myasthenia gravis and other neuromuscular junction disorders, and several ocular conditions (including herpes simplex virus keratitis, viral and fungal eye infections, open-angle glaucoma and ocular hypertension). These come from relationship data, not from label text, and should be verified against the SmPC.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication directly studies bacitracin in punctate epithelial keratoconjunctivitis, so the evidence level is L5. The condition is frequently viral or non-infectious, where an antibacterial is unlikely to help, and the high score appears to reflect similarity to other eye conditions.

**To proceed, the following is needed:**
- Mechanism of action data for bacitracin
- Evidence on the proportion of punctate epithelial keratoconjunctivitis with a bacterial component
- Licence indication text, dosage forms and SmPC safety information for the UK products
- Clinical or observational data in this specific condition, ideally separating bacitracin from combination products

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both authorisations are currently valid, and the data compiled for this report contain no indication text for them. Both are classed as sing" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

