---
layout: default
title: Dimenhydrinate
parent: Model Prediction Only (L5)
nav_order: 230
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Dimenhydrinate: predicted new indication Allergic urticaria (evidence level L5). Approved use: Vertigo of central nervous system origin"
monitor_inn: "dimenhydrinate"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
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

## Dimenhydrinate: From Vertigo and Motion Sickness to Allergic Urticaria
{: .text-alpha }

## One-Sentence Summary

Dimenhydrinate was originally used for vertigo of central nervous system origin and motion sickness.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but there are currently **no registered clinical trials** and only **1 publication** (a veterinary pharmacokinetic study), so the prediction rests mainly on the model and on class-level reasoning.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vertigo of central nervous system origin; motion sickness |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

A second predicted indication, cold urticaria (score 0.9924, Evidence Level L5, Hold), is discussed briefly below.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dimenhydrinate is a salt of diphenhydramine and 8-chlorotheophylline. Diphenhydramine is a first-generation H1-receptor antagonist.

Urticaria is driven largely by histamine released from mast cells. Blocking H1 receptors is an established way to relieve its symptoms, and diphenhydramine is already used for acute allergic urticaria. Dimenhydrinate delivers diphenhydramine, so the link is biologically plausible.

There are important caveats. No direct evidence exists for dimenhydrinate itself in this indication, and the TxGNN score is a model prediction, not clinical evidence. Current guidance generally favours second-generation non-sedating antihistamines for urticaria, which limits the practical value of a sedating first-generation agent.

**Cold urticaria (secondary prediction):** This is also a histamine-mediated physical urticaria, so H1 antagonism is mechanistically plausible. No trials or publications were found for dimenhydrinate in this condition. Support rests only on the model score (0.9924) and class-level reasoning.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic study (healthy dogs, pilot) | Veterinary Dermatology | Compared diphenhydramine levels after oral and intravenous diphenhydramine and oral dimenhydrinate, and assessed effect on histamine-induced wheal formation. Dimenhydrinate has been reported to give superior oral absorption of diphenhydramine. Animal data only; not evidence of efficacy in human urticaria. |

## UK Market Information

Please verify current UK product details in the BNF and the MHRA product information.

<!-- review:begin uk-lic-20261106-dimenhydrinate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data compiled for this report list 2 valid single-ingredient authorisations, but the numbers shown are not UK MHRA product licence (PL) numbers, and dosage form and approved indication text are not available. Please verify current UK product details in the BNF and the MHRA product information." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 4 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-dimenhydrinate-1 -->

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0406000H0AAAEAE | Dimenhydrinate 12.5mg/5ml oral liquid | Dimenhydrinate |
| 0406000H0AAADAD | Dimenhydrinate 50mg tablets | Dimenhydrinate |
| 0406000ACBBAAAA | Arlevert tablets | Dimenhydrinate/cinnarizine |
| 0406000ACAAAAAA | Cinnarizine 20mg / Dimenhydrinate 40mg tablets | Dimenhydrinate/cinnarizine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

- **Conditions flagged in the knowledge graph (not label text):** The TxGNN knowledge graph links dimenhydrinate to contraindication-type relationships with the following conditions, which should be verified against the SmPC:
  - Cardiovascular: hypertension and hypotensive disorders, acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis
  - Eye: angle-closure (closed-angle) glaucoma, ocular hypertension
  - Gastrointestinal and urinary: peptic ulcer disease, pyloric stenosis, bladder neck obstruction, benign prostatic hyperplasia
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperthyroidism (including Graves disease and thyrotoxicosis), gout, hypophosphataemia
  - Liver and gallbladder disease
  - Blood disorders: thrombocytopenia, blood coagulation disease, haemoglobinopathy
  - Substance abuse/dependence
- **Drug Interactions:** 67 interactions were recorded; the 20 shown in the data include:
  - **Major:** potassium chloride and potassium citrate.
  - **Moderate:** several anticholinergic or antimuscarinic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, clidinium, trospium, propantheline, mepenzolate, methscopolamine), opioids and related agents (morphine, opium, loperamide, eluxadoline), and others (nabilone, metoclopramide, prucalopride).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The H1-antagonist mechanism of the diphenhydramine component makes the prediction plausible, but there are no clinical trials, the only publication is an animal pharmacokinetic study, and evidence is at Level L4 (allergic urticaria) and L5 (cold urticaria). Second-generation non-sedating antihistamines are already preferred for urticaria, and key safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data for dimenhydrinate (currently unavailable)
- Label warnings and contraindications from the SmPC and BNF
- Verified UK MHRA licence numbers, dosage forms and approved indications for the listed products
- Human clinical evidence (ideally randomised trials) comparing dimenhydrinate with non-sedating antihistamines in urticaria
- Assessment of the sedation and anticholinergic burden, and of relevant conditions and interactions, in the urticaria population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data compiled for this report list 2 valid single-ingredient authorisations, but the numbers shown are not UK MHRA product licence (PL) " | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

