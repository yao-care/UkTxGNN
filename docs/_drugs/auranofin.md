---
layout: default
title: Auranofin
parent: Model Prediction Only (L5)
nav_order: 82
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Auranofin: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Auranofin"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Auranofin
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

## Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Auranofin is an oral gold(I) compound, originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental disorder,
but **no clinical trials** and **no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 0.9956 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, auranofin is a gold(I) compound that is known to inhibit thioredoxin reductase and modulate redox signalling and inflammation. Its efficacy in rheumatoid arthritis relates to these anti-inflammatory and immunomodulatory effects.

No mechanistic link to the pathogenesis of this rare developmental syndrome can be established from the available data. The high TxGNN score (0.9956) is a TxGNN model (deep learning) prediction only. It is not backed by any clinical trial or published study, so it should be regarded as a hypothesis rather than a finding.

A second prediction, brachydactyly-syndactyly syndrome (score 0.9924), is in the same position: a rare congenital limb malformation with no documented pathway linking it to auranofin's activity and no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1001030A0AAAAAA | Auranofin 3mg tablets | Auranofin |
| 1001030A0BBAAAA | Ridaura Tiltab 3mg tablets | Auranofin |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The licence number above is as recorded in the source data and does not follow the standard MHRA "PL" format, so it should be verified against the MHRA register before any reliance is placed on it.

<!-- review:begin uk-lic-20261106-auranofin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The single authorisation is a valid single-ingredient product. The licence number above is as recorded in the source data and does not follow the standard MHRA "PL" format, so it should be verified against the MHRA register before any reliance is placed on it." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-auranofin-1 -->

## Cytotoxicity

Auranofin is not an antineoplastic drug, and this section is not applicable.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** The TxGNN knowledge graph links auranofin with contraindications in several groups. These need to be confirmed against the SmPC.
  - Haematological: haematologic disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia
  - Renal and hepatic: kidney disease, liver disease, hepatitis, gallbladder disease
  - Skin: exanthem, exfoliative dermatitis, urticaria, angioedema, atopic eczema, dermatitis
  - Gastrointestinal: colitis, necrotizing enterocolitis
  - Respiratory: pulmonary fibrosis, postinflammatory pulmonary fibrosis
  - Metabolic and cardiovascular: diabetes mellitus, diabetic ketoacidosis, hypertension, hypertensive disorder
  - Autoimmune and other: systemic lupus erythematosus (including paediatric), Sjögren syndrome, dry eye syndrome, pyoureter
- **Drug Interactions:** 86 interactions were identified. The main ones in the data are:
  - **Major:** deferiprone, proguanil, chloroquine
  - **Moderate:** metronidazole, rosuvastatin, simvastatin, tinidazole, benznidazole, disulfiram
  - **Severity not graded:** warfarin, prednisone, prednisolone, calcitriol, folic acid, misoprostol, clarithromycin, and the proton pump inhibitors and ranitidine

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no clinical trials, no literature and no plausible mechanistic link to a rare developmental syndrome. The safety profile also indicates substantial haematological, renal, hepatic and dermatological cautions.

**To proceed, the following is needed:**
- Mechanism of action data for auranofin, and a biological rationale linking it to the pathogenesis of the predicted syndrome
- Preclinical or mechanistic studies (for example in disease models) to move beyond L5
- Label-based warnings and contraindications from the SmPC and BNF, to replace the knowledge-graph-derived list
- Verification of the UK authorisation record, including licence number, dosage form and approved indication
- Assessment of route and formulation suitability for the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The single authorisation is a valid single-ingredient product" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

