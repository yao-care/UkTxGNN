---
layout: default
title: Lofexidine
parent: Model Prediction Only (L5)
nav_order: 377
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Lofexidine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Lofexidine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Lofexidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Lofexidine: From Opioid Withdrawal Management to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Lofexidine is a central alpha-2 adrenergic agonist, but no approved indication text was available in the data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but the prediction is not backed by any clinical trials, and only **1 publication** (a drug-review article) is linked to it.

<!-- review:begin uk-lic-20261106-lofexidine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Lofexidine is a central alpha-2 adrenergic agonist with one marketing authorisation recorded in the UK, but no approved indication text was available in the data compiled for this report." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-lofexidine-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lofexidine is not available in the data compiled for this report. Based on its known pharmacology, lofexidine is a central alpha-2 adrenergic receptor agonist that reduces noradrenergic outflow from the locus coeruleus. It is generally used to ease symptoms of opioid withdrawal, which is not stated in the compiled data and should be confirmed against the SmPC.

A plausible link to migraine exists because other alpha-2 agonists, such as clonidine, have been studied for migraine prophylaxis. Modulating sympathetic tone and central pain and arousal pathways could, in theory, affect migraine.

This reasoning is a hypothesis. The high TxGNN score is a computational prediction only, and no clinical evidence currently supports lofexidine for migraine.

A second prediction, **migraine with brainstem aura** (score 0.9926), appears to be inherited from the broader migraine association. No specific mechanism links lofexidine to brainstem aura pathophysiology, and no trials or publications support it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30580925](https://pubmed.ncbi.nlm.nih.gov/30580925/) | 2019 | Review | Journal of the American Pharmacists Association | Drug-review article covering baloxavir marboxil, fremanezumab-vfrm, galcanezumab-gnlm and lofexidine hydrochloride. No abstract was available, and it provides no direct evidence for lofexidine in migraine. |

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0410030D0AAAAAA | Lofexidine 200microgram tablets | Lofexidine hydrochloride |
| 0410030D0BBAAAA | BritLofex 200microgram tablets | Lofexidine hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions:** 100 interactions were recorded, and the 20 detailed entries are mostly moderate in severity. The main ones to note:

- **Major:** Dolasetron
- **Moderate (selected):**
  - Opioids and related agents: morphine, difenoxin, diphenoxylate, loperamide, naltrexone
  - Antibiotics: clarithromycin, levofloxacin
  - Cannabinoids: dronabinol, nabilone
  - Other: bupropion, palonosetron, famotidine
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
  - Laxatives and bowel preparations: bisacodyl, picosulfuric acid, sodium sulfate, polyethylene glycol (3350 with electrolytes)

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5). There are no registered trials and no publications on lofexidine in migraine. Mechanism and label safety data are missing.

<!-- review:begin uk-lic-20261106-lofexidine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The UK authorisation record lacks indication text, and mechanism and label safety data are missing." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-lofexidine-2 -->

**To proceed, the following is needed:**
- The SmPC warnings and contraindications, which are currently blocking any safety screening
- Mechanism-of-action data, for example from DrugBank
- The approved UK indication and dosage form for the authorisation
- Preclinical or clinical evidence for lofexidine in migraine, including a comparison with clonidine
- A review of cardiovascular safety (blood pressure, heart rate and QT-related interactions, such as with dolasetron), given the use in a non-withdrawal population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with one marketing authorisation recorded in the UK" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "The UK authorisation record lacks indication text, and" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

