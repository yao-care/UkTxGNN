---
layout: default
title: Meptazinol
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Meptazinol"
predicted_indications: ["insomnia (disease)"]
description: "Meptazinol: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Meptazinol
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

## Meptazinol: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Meptazinol is a partial mu-opioid agonist with cholinergic activity, marketed in the UK as a tablet; the data compiled for this report do not record a specific approved indication.
The TxGNN model predicts it may be effective for **insomnia**, but there are **no clinical trials** and **no publications** supporting this direction.
The evidence rests on the model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, meptazinol is a partial mu-opioid agonist with additional cholinergic activity. It is used as an analgesic, although its approved indication is not recorded in the authorisation data available here.

A mechanistic rationale for insomnia is weak. Sedation is a side effect of opioids, not a therapeutic rationale, and opioids can disrupt sleep architecture. The high TxGNN score (0.9963) should therefore be treated as a hypothesis-generating signal only.

Other predicted indications were also reviewed. All have the same lack of trial evidence:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|

---

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia or for any of the other predicted indications.

---

## Literature Evidence

Currently no related literature available for insomnia.

They are indirect evidence only, and their titles alone were available, so study design and outcomes could not be verified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7117680](https://pubmed.ncbi.nlm.nih.gov/7117680/) | 1982 | Randomised, double-blind trial (101 surgical patients) | J Int Med Res | Meptazinol-hyoscine was compared with an Omnopon-hyoscine premedication. Both reduced blood pressure and respiratory rate to a similar extent and produced similar sedation, which the authors interpreted as satisfactory alleviation of anxiety. |
| [6135885](https://pubmed.ncbi.nlm.nih.gov/6135885/) | 1983 | Clinical study (unclassified) | Lancet | Meptazinol-midazolam combination for postoperative analgesia and sedation. Effects may be confounded by midazolam, a benzodiazepine. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0407020L0AAAAAA | Meptazinol 100mg/1ml solution for injection ampoules | Meptazinol hydrochloride |
| 0407020L0AAABAB | Meptazinol 200mg tablets | Meptazinol hydrochloride |
| 0407020L0BBABAA | Meptid 100mg/1ml solution for injection ampoules | Meptazinol hydrochloride |
| 0407020L0BBAAAB | Meptid 200mg tablets | Meptazinol hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier shown does not follow the usual PL number format, so it should be verified against MHRA and BNF sources.

<!-- review:begin uk-lic-20261106-meptazinol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One valid single-ingredient authorisation is recorded. The record does not include manufacturer, dosage form detail or indication text. The identifier shown does not follow the usual PL number format, so it should be verified against MHRA and BNF sources." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 4 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-meptazinol-1 -->

---

## Safety Considerations

Safety data (warnings, contraindications, drug interactions) could not be retrieved for this drug. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Points to consider from general opioid pharmacology, which are not drawn from label data:
- Opioids can disrupt sleep architecture and cause respiratory depression, which is a particular concern for any hypnotic use.
- Opioid use in infants carries significant safety concerns, which is relevant to the paediatric torticollis prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on the model score alone (Evidence Level L5). There are no trials or publications, and the pharmacology argues against benefit, because opioids can impair sleep quality.

**To proceed, the following is needed:**
- Confirmation of the approved indication and SmPC from MHRA and BNF sources
- Mechanism of action data and a plausible biological rationale linking meptazinol to sleep regulation
- Safety information (warnings, contraindications, interactions), including respiratory depression and dependence risk
- Preclinical or early-phase clinical evidence in insomnia, ideally with polysomnography outcomes

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient authorisation is recorded. The record does not include manufacturer, dosage form detail or indication text" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

