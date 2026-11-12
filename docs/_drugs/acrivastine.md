---
layout: default
title: Acrivastine
parent: Model Prediction Only (L5)
nav_order: 22
evidence_level: L5
indication_count: 1
monitor_inn: "Acrivastine"
predicted_indications: ["recalcitrant atopic dermatitis"]
last_modified_at: 2026-11-12
description: "Acrivastine: predicted new indication Recalcitrant atopic dermatitis (evidence level L5). Approved use: Allergic rhinitis"
---

# Acrivastine
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

## Acrivastine: From Allergic Rhinitis to Recalcitrant Atopic Dermatitis
{: .text-alpha }

## One-Sentence Summary

Acrivastine is a second-generation H1-receptor antagonist (antihistamine) whose recorded uses in the knowledge graph centre on allergic and catarrhal conditions such as allergic rhinitis.
The TxGNN model predicts it may be useful for **recalcitrant atopic dermatitis**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (relation recorded in the knowledge graph; the UK licence record contains no indication text) |
| Predicted New Indication | Recalcitrant atopic dermatitis |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (6 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Acrivastine belongs to the class of second-generation H1-receptor antagonists with limited sedation.

Histamine contributes to itch in atopic dermatitis, so H1 blockade offers a plausible symptomatic (anti-pruritic) rationale. However, itch in atopic dermatitis is driven largely by non-histaminergic pathways (IL-4/IL-13, IL-31, TSLP and neuroimmune signalling). Guideline-based reviews report limited benefit from H1 antihistamines, particularly in recalcitrant or moderate-to-severe disease.

The high TxGNN score is a computational prediction only. It most likely reflects network proximity to other antihistamines and to allergic or atopic conditions, rather than disease-specific evidence. At best, any benefit would be symptomatic rather than disease-modifying.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin uk-lic-20261106-acrivastine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One single-ingredient authorisation is recorded and it is currently valid. The record gives no manufacturer, dosage-form field or indication text, so the approved indication should be confirmed from the SmPC and BNF." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 6 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-acrivastine-1 -->

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0304010A0AAAAAA | Acrivastine 8mg capsules | Acrivastine |
| 0304010A0BDAAAA | Allergy Relief 8mg capsules | Acrivastine |
| 0304010A0BCAAAA | Benadryl Allergy Relief 8mg capsules | Acrivastine |
| 0304010A0BCABAC | Benadryl Allergy Relief Plus Decongestant capsules | Acrivastine |
| 0304010A0AAACAC | Pseudoephedrine 60mg / Acrivastine 8mg capsules | Acrivastine |
| 0304010A0BBAAAA | Semprex 8mg capsules | Acrivastine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** hypertension, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (including Graves disease and thyrotoxicosis). These need verification against the SmPC.
- **Drug interactions (100 recorded; main ones shown):**
  - *Major:* potassium chloride and potassium citrate.
  - *Moderate:* anticholinergic or antimuscarinic agents (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium), plus eluxadoline, loperamide, ethanol, histamine, physostigmine and promethazine.

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials or publications studying acrivastine in atopic dermatitis, so the evidence level is L5. Itch in atopic dermatitis is mostly non-histaminergic, and antihistamines have shown limited efficacy, particularly in recalcitrant disease.

**To proceed, the following is needed:**
- Clinical or observational evidence of acrivastine in atopic dermatitis, for example a pilot trial of itch outcomes
- Mechanism of action data to support the mechanistic link
- SmPC-based warnings and contraindications, to verify the knowledge-graph contraindications
- Confirmation of the licensed indication and dosage form for the UK authorisation
- Assessment of how acrivastine would add to current standard atopic dermatitis treatment (emollients, topical corticosteroids, and systemic or biological options)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One single-ingredient authorisation is recorded and it is currently valid. The record gives no manufacturer, dosage-form field or indication" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

