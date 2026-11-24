---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Ethosuximide: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Absence epilepsy"
monitor_inn: "Ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
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

## Ethosuximide: From Absence Epilepsy to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ethosuximide is an anti-epileptic medicine originally used to treat absence epilepsy.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but currently there are **no clinical trials** and **no publications** supporting this direction; the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (10 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ethosuximide: "Ethosuximide suppresses the paroxysmal three cycle per second spike and wave activity associated with lapses of consciousness which is common in absence (petit mal) seizures. The frequency of epileptiform attacks is reduced, apparently by depression of the motor cortex and elevation of the threshold of the central nervous system to convulsive stimuli." ([DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6), label version 2026-05-25; accessed 2026-11-19.) Ethosuximide is generally understood to block T-type calcium channels in thalamic neurons, which underlies its efficacy in absence epilepsy. This is background knowledge and not drawn from the compiled data.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*) or, in some cases, *GNAS*. These produce constitutive receptor activity and water retention despite low vasopressin levels. A link between T-type calcium channel blockade and this process has not been established. Any connection, for example through renal calcium signalling or aquaporin-2 regulation, is speculative.

The very high TxGNN score (0.9991, model rank 1420) is a model-based prediction only. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be treated as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0408010I0AAAAAA | Ethosuximide 250mg capsules | Ethosuximide |
| 0408010I0AAABAB | Ethosuximide 250mg/5ml oral solution | Ethosuximide |
| 0408010I0AAAKAK | Ethosuximide 250mg/5ml oral solution sugar free | Ethosuximide |
| 0408010I0AAALAL | Ethosuximide 500mg/5ml oral solution sugar free | Ethosuximide |
| 0408010I0BBAAAA | Emeside 250mg capsules | Ethosuximide |
| 0408010I0BBABAB | Emeside 250mg/5ml syrup | Ethosuximide |
| 0408010I0BDAAAA | Epesri 250mg capsules | Ethosuximide |
| 0408010I0BDABAB | Epesri 250mg/5ml syrup | Ethosuximide |
| 0408010I0BCAAAA | Zarontin 250mg capsules | Ethosuximide |
| 0408010I0BCABAB | Zarontin 250mg/5ml syrup | Ethosuximide |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The BNF classification code (0408010) corresponds to the anti-epileptic drug section (BNF chapter 4.8.1).

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindication-related** (derived from drug-disease graph edges, not from product label text; these should be checked against the SmPC): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, haematological disease, liver disease, gallbladder disease, systemic lupus erythematosus (including paediatric), neutropenia, agranulocytosis, acute intermittent porphyria.
- **Drug Interactions**: 92 interactions were recorded. All 20 listed in the data are of moderate severity, including:
  - Central nervous system depressants and opioids: morphine (including liposomal), opium, ethanol, promethazine, chlorpheniramine
  - Cannabinoids: dronabinol, nabilone
  - Antiemetics: aprepitant, metoclopramide
  - Antimalarials: chloroquine, mefloquine, hydroxychloroquine
  - Folate-related agents: folic acid, leucovorin, levoleucovorin
  - Others: sibutramine, cobicistat, deferasirox, fostamatinib

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no clinical trials or publications, and no plausible mechanism linking ethosuximide to NSIAD has been established. The drug's knowledge-graph contraindications (kidney disease, blood disorders) also warrant caution in a renal-related condition.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a testable hypothesis linking T-type calcium channel blockade to V2 receptor or aquaporin-2 signalling
- Preclinical studies (for example, cell models carrying *AVPR2* gain-of-function variants)
- Warnings and contraindications from the SmPC and BNF, to complete safety screening
- Approved indication text and PL number for the UK products
- Assessment of route and formulation compatibility for the new indication

<!-- review:begin uk-lic-20261124c-ethosuximide-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Approved indication text and PL number for the UK authorisation" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-ethosuximide-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6) |
| 2026-11-24 | Corrected: "Approved indication text and PL number for the UK authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

