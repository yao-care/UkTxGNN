---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Salbutamol
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

## Salbutamol: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is an established beta-2 adrenergic agonist marketed in the UK.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (94 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 94 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Salbutamol belongs to the beta-2 adrenergic agonist class, and its established efficacy in its licensed airway use is not in question.

Any rationale for papillary conjunctivitis is speculative. Beta-2 agonism could plausibly reduce mast cell mediator release or ocular vascular congestion, both of which feature in allergic eye inflammation. This has not been tested for this condition, and no study in the compiled data addresses it. The very high model score should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin uk-lic-20261106-salbutamol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One valid single-ingredient licence is recorded, and no cancelled licences. The record carries no manufacturer details." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 94 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-salbutamol-1 -->

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0301011R0AABUBU | Salbutamol 100micrograms/dose breath actuated inh CFC free | Salbutamol |
| 0301011R0AAADAD | Salbutamol 100micrograms/dose breath actuated inhaler | Salbutamol |
| 0301011R0AACCCC | Salbutamol 100micrograms/dose dry pdr inhalation cartridge | Salbutamol |
| 0301011R0AABZBZ | Salbutamol 100micrograms/dose dry powder inhaler | Salbutamol |
| 0301011R0AAAAAA | Salbutamol 100micrograms/dose inhaler | Salbutamol |
| 0301011R0AAAPAP | Salbutamol 100micrograms/dose inhaler CFC free | Salbutamol |
| 0301011R0BVAAAX | Salbutamol 2.5mg/2.5ml neb liq unit dose Steripoule vials | Salbutamol |
| 0301011R0AACDCD | Salbutamol 2.5mg/2.5ml nebuliser liquid unit dose ampoules | Salbutamol |
| 0301011R0AAAXAX | Salbutamol 2.5mg/2.5ml nebuliser liquid unit dose vials | Salbutamol |
| 0301011R0BPACAV | Salbutamol 200 Cyclocaps | Salbutamol |
| 0301011R0AAAKAK | Salbutamol 200microgram inhalation powder blisters | Salbutamol |
| 0301011R0AAAVAV | Salbutamol 200microgram inhalation powder capsules | Salbutamol |
| 0301011R0AAAQAQ | Salbutamol 200micrograms/dose dry powder inhaler | Salbutamol |
| 0301011R0AAAZAZ | Salbutamol 2mg tablets | Salbutamol |
| 0301011R0AABGBG | Salbutamol 2mg/5ml oral solution sugar free | Salbutamol |
| 0301011R0BPADAW | Salbutamol 400 Cyclocaps | Salbutamol |
| 0301011R0AAALAL | Salbutamol 400microgram inhalation powder blisters | Salbutamol |
| 0301011R0AAAWAW | Salbutamol 400microgram inhalation powder capsules | Salbutamol |
| 0301011R0AABMBM | Salbutamol 4mg modified-release capsules | Salbutamol |
| 0301011R0AABEBE | Salbutamol 4mg modified-release tablets | Salbutamol |

Showing 20 of 94 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The data compiled for this report records 100 interacting drugs, and the first 20 returned are summarised here.
  - **Moderate**: antidiabetic agents (acarbose, albiglutide, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin), epinephrine, clarithromycin, cisapride, famotidine, bisacodyl, castor oil, isometheptene and diethylpropion.
  - **Minor**: corticosteroids (hydrocortisone, beclometasone, betamethasone, budesonide, dexamethasone).

Warnings and contraindications from the product label are not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no directly relevant literature, and only a speculative mechanistic link, which places it at evidence level L5.

**To proceed, the following is needed:**
- Preclinical and clinical evidence directly studying salbutamol in papillary conjunctivitis
- Mechanism of action data and a clearer mechanistic rationale for ocular use
- An assessment of a suitable route and formulation
- Label-based safety information, including ocular safety and relevant interactions

<!-- review:begin uk-lic-20261106-salbutamol-2 -->

> **Review correction (2026-11-06)**: Originally stated: "An assessment of a suitable route and formulation, since the only UK licence recorded is an inhalation product" Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 94 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-salbutamol-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient licence is recorded, and no cancelled licences. The record carries no manufacturer details" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "since the only UK licence recorded is an inhalation product" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

