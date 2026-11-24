---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 145
evidence_level: L5
indication_count: 7
monitor_inn: "Celecoxib"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
last_modified_at: 2026-11-20
description: "Celecoxib: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In the UK: 9 NHSBSA BNF presentation codes"
---

# Celecoxib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Celecoxib: COX-2 selective NSAID → Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor (an NSAID) marketed in the UK.
The TxGNN model predicts it may be relevant to **acromesomelic dysplasia, Hunter-Thompson type**, but there are **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (9 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for celecoxib: "Celecoxib has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of celecoxib is believed to be due to inhibition of prostaglandin synthesis, primarily via inhibition of COX-2. Celecoxib is a potent inhibitor of prostaglandin synthesis in vitro." ([DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d), label version 2025-07-31; accessed 2026-11-19.) Celecoxib is known as a selective COX-2 inhibitor, which reduces prostaglandin-mediated inflammation and pain.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by mutations in *CDMP1/GDF5*, which disrupt growth signalling in bone and cartilage. COX-2 inhibition does not act on this pathway, so no established mechanistic link exists. The high score most likely reflects the model's proximity between musculoskeletal conditions rather than a true pharmacological relationship. The prediction should be regarded as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin uk-lic-20261106-celecoxib-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least one single-ingredient licence is currently valid, with no cancelled licences." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-celecoxib-1 -->

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1001010AHAAAAAA | Celecoxib 100mg capsules | Celecoxib |
| 0407041AFAAAAAA | Celecoxib 120mg/4.8ml soln unit dose bottles sugar free | Celecoxib |
| 1001010AHAAABAB | Celecoxib 200mg capsules | Celecoxib |
| 1001010AHAAADAD | Celecoxib 400mg capsules | Celecoxib |
| 1001010AHAAAEAE | Celecoxib 50mg/5ml oral suspension | Celecoxib |
| 1001010AHBBAAAA | Celebrex 100mg capsules | Celecoxib |
| 1001010AHBBABAB | Celebrex 200mg capsules | Celecoxib |
| 0407041AFBBAAAA | Elyxyb 120mg/4.8ml oral solution unit dose bottles | Celecoxib |
| 1001010AHBCAAAD | Onsenal 400mg capsules | Celecoxib |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions** (100 interactions recorded in the interaction database; examples from the listed entries):
- **Major**: eliglustat
- **Moderate**: hydrocortisone, metformin, several sulfonylureas and related antidiabetic agents (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide, nateglinide), exenatide, cimetidine, levofloxacin, metronidazole, mesalazine, balsalazide, olsalazine, naltrexone, kanamycin, fenfluramine, dexfenfluramine

Label-based warnings and contraindications are not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information, particularly for cardiovascular, gastrointestinal, renal, hepatic and asthma-related risks. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or publications, and no plausible mechanistic link between COX-2 inhibition and a *GDF5*-driven skeletal dysplasia. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic data showing a plausible role for COX-2/prostaglandin signalling in GDF5-related skeletal growth
- Preclinical studies in relevant disease models
- Label-based safety data (SmPC warnings and contraindications) for any future use in this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "At least one single-ingredient licence is currently valid, with no cancelled licences" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

