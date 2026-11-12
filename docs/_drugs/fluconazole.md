---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, candidiasis, vulvovaginal candidiasis…"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fluconazole is an azole antifungal, originally used to treat candidiasis (oral, oesophageal, vulvovaginal, invasive) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** were found for this indication, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, candidiasis, vulvovaginal candidiasis, oesophageal candidiasis, cryptococcal meningitis, candidaemia, disseminated candidiasis |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (29 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 29 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Fluconazole is an azole antifungal, a class that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase) and so blocks ergosterol synthesis. Its efficacy in candidiasis and cryptococcal infection is established.

The link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is usually viral (often adenoviral) or immune-mediated, so an antifungal has no clear target in its pathology. The high TxGNN score therefore appears to be a computational association and should not be read as evidence of benefit.

Other predictions in the data set for this drug (ranks 2-10) also have little support. The remainder have no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0502010B0AAAMAM | Fluconazole 100mg/50ml solution for infusion bottles | Fluconazole |
| 0502010B0AAAPAP | Fluconazole 100mg/50ml solution for infusion vials | Fluconazole |
| 0502010B0AAABAB | Fluconazole 150mg capsules | Fluconazole |
| 0502010B0AAACAC | Fluconazole 200mg capsules | Fluconazole |
| 0502010B0AAAKAK | Fluconazole 200mg/100ml infusion bags | Fluconazole |
| 0502010B0AAALAL | Fluconazole 200mg/100ml solution for infusion bottles | Fluconazole |
| 0502010B0AAAEAE | Fluconazole 200mg/100ml solution for infusion vials | Fluconazole |
| 0502010B0AAAHAH | Fluconazole 200mg/5ml oral suspension | Fluconazole |
| 0502010B0AAANAN | Fluconazole 400mg/200ml infusion bags | Fluconazole |
| 0502010B0AAAAAA | Fluconazole 50mg capsules | Fluconazole |
| 0502010B0AAADAD | Fluconazole 50mg/25ml solution for infusion vials | Fluconazole |
| 0502010B0AAAGAG | Fluconazole 50mg/5ml oral suspension | Fluconazole |
| 0502010B0BFADAB | Azocan-P 150mg capsules | Fluconazole |
| 0502010B0BGAAAB | Bell's Thrush Relief Oral 150mg capsules | Fluconazole |
| 0702020F0BGAAAP | Boots Pharmacy Thrush Duo | Clotrimazole |
| 0702020F0BBAMAN | Canesten Thrush Duo 150mg Oral capsules & External 2% cream | Clotrimazole |
| 0502010B0BDAAAB | Canesten Thrush Oral 150mg capsules | Fluconazole |
| 0502010B0BBABAB | Diflucan 150mg capsules | Fluconazole |
| 0502010B0BBACAC | Diflucan 200mg capsules | Fluconazole |
| 0502010B0BBAEAE | Diflucan 200mg/100ml solution for infusion vials | Fluconazole |

Showing 20 of 29 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier shown is a BNF-style product code (BNF section 5.2.1, azole antifungals) rather than a PL number.

<!-- review:begin uk-lic-20261106-fluconazole-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The identifier shown is a BNF-style product code (BNF section 5.2.1, azole antifungals) rather than a PL number. One valid single-ingredient authorisation is recorded." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 29 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-fluconazole-1 -->

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, kidney disease, pyoureter, liver disease, gallbladder disease.
- **Drug Interactions**: 100 interactions were identified. Notable examples:
  - **Major**: chlorpropamide.
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), proton pump inhibitors (omeprazole, rabeprazole, dexlansoprazole), famotidine, loperamide, aprepitant, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes.
  - **Minor**: amphotericin B, clarithromycin.
- A published cohort also reports that fluconazole raises tacrolimus trough levels (CYP3A4 inhibition), so dose adjustment is needed.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature, and there is no credible mechanistic link between an antifungal and a mostly viral or immune-mediated eye condition.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible mechanistic rationale for the ocular indication
- Label warnings and contraindications from the SmPC and BNF
- Preclinical or clinical evidence in punctate epithelial keratoconjunctivitis, and an assessment of route of administration (ocular versus systemic) and ocular safety

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient authorisation is recorded" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

