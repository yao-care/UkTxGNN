---
layout: default
title: Idebenone
parent: Model Prediction Only (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Idebenone"
predicted_indications: ["hepatic porphyria", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "hepatoportal sclerosis", "immune-mediated necrotizing myopathy", "osteogenesis imperfecta-retinopathy-seizures-intellectual disability syndrome", "antisynthetase syndrome", "focal myositis"]
description: "Idebenone: predicted new indication Hepatic porphyria (evidence level L5). In the UK: 4 NHSBSA BNF presentation codes"
---

# Idebenone
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

## Idebenone: Hepatic porphyria
{: .text-alpha }

## One-Sentence Summary

Idebenone was originally used for Leber hereditary optic neuropathy, a mitochondrial disease of the optic nerve.
The TxGNN model predicts it may be effective for **hepatic porphyria**,
but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on a computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of idebenone as: Antioxidant and mitochondrial electron carrier ([ChEMBL CHEMBL252556 (idebenone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL252556), CC BY-SA 3.0; accessed 2026-11-19.) Idebenone is a short-chain benzoquinone that supports mitochondrial electron transport and has antioxidant activity. Its established use in Leber hereditary optic neuropathy, a mitochondrial disorder, is the basis for its original indication.

A link to hepatic porphyria is conceivable if oxidative stress or mitochondrial dysfunction contributes to liver injury in that condition. However, this is speculative. Without confirmed mechanism data and with no supporting studies, the mechanistic rationale cannot be verified.

The model also ranks several other conditions highly, all with the same lack of supporting evidence: idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, hepatoportal sclerosis, early-onset familial noncirrhotic portal hypertension, primitive portal vein thrombosis, immune-mediated necrotizing myopathy, osteogenesis imperfecta-retinopathy-seizures-intellectual disability syndrome, antisynthetase syndrome and focal myositis. Of these, the myopathy-related conditions have some indirect plausibility, because idebenone has been studied in muscle disorders such as Duchenne muscular dystrophy. That evidence is not part of the data compiled for this report, and the autoimmune nature of these conditions keeps the link speculative.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1108030ABAAABAB | Idebenone 150mg capsules | Idebenone |
| 1108030ABAAACAC | Idebenone 150mg tablets | Idebenone |
| 1108030ABAAAAAA | Idebenone 45mg tablets | Idebenone |
| 1108030ABBBAAAC | Raxone 150mg tablets | Idebenone |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier is not in the standard MHRA "PL" format, so it should be checked against the MHRA register before any reliance is placed on it. Dosage form, manufacturer and approved indication text are not recorded in the data compiled for this report.

<!-- review:begin uk-lic-20261106-idebenone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The data lists one valid single-ingredient authorisation. The identifier is not in the standard MHRA "PL" format, so it should be checked against the MHRA register before any reliance is placed on it." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-idebenone-1 -->

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (0.9992), with no registered clinical trials, no publications and no verified mechanism of action. This corresponds to evidence level L5, which is not enough to justify further investment at this stage.

**To proceed, the following is needed:**
- Mechanism of action data for idebenone, to allow a proper mechanistic-link analysis
- A literature and trial search specific to idebenone in hepatic porphyria, and in the other predicted conditions
- Safety information (warnings, contraindications and interactions) from the SmPC and BNF, which is currently missing and blocks safety screening
- Verification of the UK product details, including the licensed indication, dosage form and MHRA authorisation number
- Assessment of route and formulation compatibility with the proposed new indication

<!-- review:begin uk-lic-20261124c-idebenone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Verification of the UK marketing authorisation details, including the licensed indication, dosage form and MHRA authorisation number" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-idebenone-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "The data lists one valid single-ingredient authorisation" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL252556 (idebenone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL252556) |
| 2026-11-24 | Corrected: "Verification of the UK marketing authorisation details, including the licensed indication, dosage form and MHRA authorisation number" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

