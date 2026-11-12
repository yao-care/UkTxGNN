---
layout: default
title: Zafirlukast
parent: Model Prediction Only (L5)
nav_order: 658
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Zafirlukast"
predicted_indications: ["bronchitis"]
description: "Zafirlukast: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Zafirlukast
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

## Zafirlukast: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Zafirlukast is a cysteinyl leukotriene receptor antagonist that is currently marketed in the UK.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials or publications** were found in the data compiled for this report, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From its drug class, zafirlukast is a cysteinyl leukotriene receptor (CysLT1) antagonist.

Leukotrienes contribute to airway inflammation, bronchoconstriction and mucus secretion. Blocking their receptor could plausibly reduce these features in bronchitis, so a mechanistic link exists in principle. However, the TxGNN score (0.9993) is a computational output only. No trials or literature were supplied for this indication, so the link cannot be verified from the available data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

<!-- review:begin uk-lic-20261106-zafirlukast-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The licence record carries a BNF-style code (chapter 3, respiratory system) rather than a PL number, and no approved indication text is recorded. The single licence is valid and is for a single-ingredient product." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-zafirlukast-1 -->

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0303020Z0AAABAB | Zafirlukast 20mg tablets | Zafirlukast |
| 0303020Z0BBAAAB | Accolate 20mg tablets | Zafirlukast |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified in the interaction screen. Examples of those graded Moderate include aprepitant, acetylsalicylic acid, metronidazole, budesonide (including nasal), saxagliptin, eliglustat, naltrexone, nateglinide, nitisinone, repaglinide, rosuvastatin, simvastatin and tinidazole. Sibutramine is graded Minor. Pantoprazole, mesalazine, morphine, metformin and omeprazole are of unknown grade.
- **Conditions requiring caution (from interaction and relationship data, not label text)**: liver disease, cirrhosis of liver, gallbladder disease, insomnia, anxiety, anxiety disorder, neurotic disorder and dysthymic disorder.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for bronchitis is a high TxGNN score (0.9993); no clinical trials or publications address this disease, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or observational studies of zafirlukast directly in bronchitis
- Detailed mechanism of action data
- Label-based warnings and contraindications from the SmPC and BNF
- Review of the hepatic and neuropsychiatric cautions and the moderate-grade interactions before any use in a new population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The licence record carries a BNF-style code (chapter 3, respiratory system) rather than a PL number, and no approved indication text is reco" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

