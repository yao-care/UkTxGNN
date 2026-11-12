---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 12
evidence_level: L5
indication_count: 9
monitor_inn: "Acarbose"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-11-12
description: "Acarbose: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Acarbose: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Acarbose is an intestinal alpha-glucosidase inhibitor, recorded in the knowledge graph for type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but **no clinical trials and no publications** directly study this condition, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; no licence indication text is available) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Acarbose is generally understood to be an intestinal alpha-glucosidase inhibitor that delays carbohydrate digestion and so reduces postprandial glucose rises. It has minimal systemic absorption.

The data compiled for this report found no identifiable mechanistic link to classic stiff person syndrome. The score of 0.9965 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same reasoning applies to the next-ranked prediction, focal stiff limb syndrome (score 0.9965), a focal variant of the stiff person spectrum. Other lower-ranked predictions were also reviewed (thiamine-responsive dysfunction syndrome, opsismodysplasia, several localised lipodystrophies and pancreatic agenesis). None showed a plausible disease-modifying mechanism, and all remain at evidence level L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

For the ninth-ranked prediction, pancreatic agenesis, 11 papers were retrieved. They concern type 2 diabetes, insulin autoimmune syndrome, heart failure and glucose metabolism, and animal models. None addresses pancreatic agenesis, so they are indirect and do not raise its evidence level.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0601023A0AAABAB | Acarbose 100mg tablets | Acarbose |
| 0601023A0AAAAAA | Acarbose 50mg tablets | Acarbose |
| 0601023A0BBADAB | Glucobay 100mg tablets | Acarbose |
| 0601023A0BBACAA | Glucobay 50mg tablets | Acarbose |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Dosage form and indication text are not available in the compiled data. The identifier is not in the usual MHRA "PL" format, so it should be checked against the MHRA register.

<!-- review:begin uk-lic-20261106-acarbose-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The record lists one single-ingredient authorisation, currently valid. Dosage form and indication text are not available in the compiled data." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 4 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-acarbose-1 -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** contraindication-type relations were recorded for kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of liver, inflammatory bowel disease, hypoglycaemia and injury. These need verification against the SmPC.
- **Drug Interactions:** 100 interactions were identified. Those listed include:
  - Moderate: acetazolamide, salbutamol, aloe vera leaf, alpelisib, amprenavir, aripiprazole, asenapine, asparaginase (Erwinia chrysanthemi and Escherichia coli), atazanavir, bedaquiline, bendroflumethiazide, benzphetamine, benzthiazide, betamethasone.
  - Minor: albiglutide, alclometasone (topical), lipoic acid, amcinonide, anisindione.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The evidence level is L5.

**To proceed, the following is needed:**
- A mechanistic hypothesis explaining how a gut-restricted alpha-glucosidase inhibitor could affect stiff person syndrome
- Preclinical or clinical studies directly addressing the predicted disease
- Mechanism of action data and SmPC/BNF warnings and contraindications, which are currently missing
- Licence indication and dosage form details for the UK authorisation

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The record lists one single-ingredient authorisation, currently valid" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

