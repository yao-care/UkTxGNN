---
layout: default
title: Granisetron
parent: Model Prediction Only (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "Granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Granisetron
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

## Granisetron: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist, marketed in the UK as a 1 mg tablet. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **no clinical trials and no publications** were available in the data compiled for this report. The prediction is based on the model alone.

Note: the data compiled for this report did not include an approved indication text for granisetron. The original indication is therefore not recorded. Granisetron is generally known as an antiemetic, but this is background knowledge, not data from the compiled sources.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (12 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, granisetron is a selective 5-HT3 receptor antagonist. 5-HT3 modulation has been hypothesised to influence the dopaminergic and serotonergic signalling relevant to mood regulation.

This link is speculative. The very high TxGNN score reflects a network-based model prediction, not clinical observation, and no trials or publications were found to support it. The similarity between the original and predicted indications has not been assessed.

Other predictions in the same list include Tourette syndrome (0.9952) and trichotillomania (0.9923), which also have only speculative serotonergic and dopaminergic rationales. Several others, such as acute contagious conjunctivitis, bronchitis and nephrogenic syndrome of inappropriate antidiuresis, have no plausible mechanistic link and are probably model artefacts. All have L5 evidence and a Hold recommendation.

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
| 0406000M0AAABAB | Granisetron 1mg tablets | Granisetron hydrochloride |
| 0406000M0AAAFAF | Granisetron 1mg/1ml solution for injection ampoules | Granisetron hydrochloride |
| 0406000M0AAAEAE | Granisetron 200micrograms/ml oral solution sugar free | Granisetron hydrochloride |
| 0406000M0AAADAD | Granisetron 2mg tablets | Granisetron hydrochloride |
| 0406000AFAAAAAA | Granisetron 3.1mg/24hours transdermal patches | Granisetron |
| 0406000M0AAAAAA | Granisetron 3mg/3ml solution for injection ampoules | Granisetron hydrochloride |
| 0406000M0BBABAB | Kytril 1mg tablets | Granisetron hydrochloride |
| 0406000M0BBAFAF | Kytril 1mg/1ml solution for injection ampoules | Granisetron hydrochloride |
| 0406000M0BBAEAE | Kytril 200micrograms/ml liquid paediatric | Granisetron hydrochloride |
| 0406000M0BBADAD | Kytril 2mg tablets | Granisetron hydrochloride |
| 0406000M0BBAAAA | Kytril 3mg/3ml solution for injection ampoules | Granisetron hydrochloride |
| 0406000AFBBAAAA | Sancuso 3.1mg/24hours transdermal patches | Granisetron |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Dosage form, manufacturer and approved indication text were not supplied for it. The authorisation number is shown exactly as supplied and does not follow the usual UK "PL" format, so it should be verified against the MHRA register. NICE appraisals and BNF classification were not included in the compiled data.

<!-- review:begin uk-lic-20261106-granisetron-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The compiled data lists one valid single-ingredient authorisation. Dosage form, manufacturer and approved indication text were not supplied for it." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 12 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-granisetron-1 -->

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease, sudden cardiac arrest, heart conduction disease. These point to a QT-prolongation and cardiac-conduction concern.
- **Drug Interactions** (100 interactions identified; the 20 supplied include these):
  - **Major:** fentanyl, alfentanil, tramadol, dextromethorphan, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline, anagrelide. Many of these involve QT prolongation or serotonergic effects.
  - **Moderate:** abametapir (topical), abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol.

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no registered trials or publications. The mechanistic rationale is speculative. Knowledge-graph contraindications relating to QT prolongation and cardiac conduction would matter in a psychiatric population, where interacting QT-prolonging drugs are common.

**To proceed, the following is needed:**
- A systematic literature and trial-registry search for granisetron or other 5-HT3 antagonists in bipolar mania
- Mechanism of action data and a clearer mechanistic link to mood regulation
- The approved indication text and SmPC safety information for the UK authorisation
- A cardiac safety assessment, including QT risk and interactions with common psychiatric medicines
- Preclinical or early-phase clinical data before any further evaluation

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The compiled data lists one valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

