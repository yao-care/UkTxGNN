---
layout: default
title: Cyproheptadine
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 1
monitor_inn: "Cyproheptadine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-11-24
description: "Cyproheptadine: predicted new indication Nasal cavity disease (evidence level L5). In the UK: 4 NHSBSA BNF presentation codes"
---

# Cyproheptadine
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

## Cyproheptadine: Antihistamine and serotonin antagonist → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Cyproheptadine is an antihistamine with serotonin-antagonist activity that is marketed in the United Kingdom.
The TxGNN model predicts it may be relevant to **nasal cavity disease**, but **no clinical trials and no publications** were found in the data compiled for this report, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for cyproheptadine: "Cyproheptadine is a serotonin and histamine antagonist with anticholinergic and sedative effects. Antiserotonin and antihistamine drugs appear to compete with serotonin and histamine, respectively, for receptor sites." ([DailyMed: Cyproheptadine Hydrochloride Solution (cyproheptadine hydrochloride) prescribing information, Method Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1acfd050-6c07-a269-e063-6394a90a77e8), label version 2025-10-21; accessed 2026-11-19.) Cyproheptadine belongs to the antihistamine class, and its mechanism is generally understood to involve histamine H1 receptor and serotonin receptor antagonism. This general pharmacology is not drawn from the compiled data, so it should be checked against the SmPC.

The model's prediction is likely driven by the drug's established use in nasal and allergic conditions. However, "nasal cavity disease" is a very broad category. It covers many different conditions with different causes, so the mechanistic link cannot be assessed meaningfully until a specific disease is defined (for example, a particular type of rhinitis).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0304010K0AAADAD | Cyproheptadine 2mg/5ml oral liquid | Cyproheptadine hydrochloride |
| 0304010K0AAABAB | Cyproheptadine 4mg tablets | Cyproheptadine hydrochloride |
| 0304010K0AAAFAF | Cyproheptadine 4mg/5ml oral liquid | Cyproheptadine hydrochloride |
| 0304010K0BBAAAB | Periactin 4mg tablets | Cyproheptadine hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The codes shown are NHSBSA BNF presentation codes, not MHRA PL numbers, so MHRA licence details should be checked in MHRA sources.

<!-- review:begin uk-lic-20261106-cyproheptadine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The data compiled for this report show one valid single-ingredient licence record. The authorisation number is not in the MHRA "PL" format, so the record should be verified against MHRA sources." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-cyproheptadine-1 -->

---

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 recorded interactions. Examples include:
  - **Major**: potassium chloride and potassium citrate.
  - **Moderate**: anticholinergic or antimuscarinic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate), opioids and related agents (morphine, loperamide, opium, eluxadoline), cannabinoids (dronabinol, nabilone), metoclopramide and fenfluramine.
  - Only the first 20 of the 100 recorded interactions are available here.
- **Conditions of concern recorded in the data**: The compiled data flag possible caution in people with hypertension, peptic ulcer disease, benign prostatic hyperplasia, ocular hypertension, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis) and bladder neck obstruction. These are not taken from label text and must be confirmed against the SmPC.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is for a broad, non-specific category, and no trials or publications were found, so it rests on the model score alone (evidence level L5).

**To proceed, the following is needed:**
- Define a specific nasal disease (for example a particular type of rhinitis) in place of "nasal cavity disease"
- Search for clinical trials and literature on that specific disease
- Obtain mechanism of action data
- Retrieve the SmPC warnings and contraindications, and verify the UK product details against MHRA data

<!-- review:begin uk-lic-20261124d-cyproheptadine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Retrieve the SmPC warnings and contraindications, and verify the licence record against MHRA data" Corrected wording only: the text described this site's UK market data as MHRA licences, marketing authorisations, licence numbers or licence records, or rested on a UK licence status. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902): these are NHS prescribing codes, not MHRA licences, they carry no indication text, and MHRA licence status is not included. The wording was changed to BNF prescribing codes (or the unsupported premise was removed); the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124d-cyproheptadine-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "The data compiled for this report show one valid single-ingredient licence record" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cyproheptadine Hydrochloride Solution (cyproheptadine hydrochloride) prescribing information, Method Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1acfd050-6c07-a269-e063-6394a90a77e8) |
| 2026-11-24 | Corrected: "Retrieve the SmPC warnings and contraindications, and verify the licence record against MHRA data" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

