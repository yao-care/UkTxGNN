---
layout: default
title: Rimexolone
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "Rimexolone"
predicted_indications: ["seborrheic dermatitis", "dermatitis"]
description: "Rimexolone: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Rimexolone
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

## Rimexolone: Seborrheic dermatitis
{: .text-alpha }

## One-Sentence Summary

Rimexolone is a synthetic corticosteroid originally used as an eye drop for uveitis and related inflammatory eye conditions.
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on corticosteroid class pharmacology alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for this drug. Based on known information, rimexolone is a synthetic glucocorticoid (glucocorticoid receptor agonist) with anti-inflammatory and immunosuppressive properties. Its use in uveitis and other ocular inflammation is established, and mechanistically it may be applicable to inflammatory skin conditions.

Topical corticosteroids are an established treatment class for seborrheic dermatitis. This makes the high prediction score biologically plausible, through shared glucocorticoid effects such as reduced release of inflammatory mediators and reduced leukocyte infiltration. A second prediction, general **dermatitis** (score 0.9934), follows the same logic.

This is a class-effect inference, not drug-specific evidence. Rimexolone is formulated only as an ophthalmic preparation, so skin penetration, dermal safety and appropriate dosing have not been characterised. Any dermatological use would need new formulation and safety work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1104010V0AAAAAA | Rimexolone 10mg/ml eye drops | Rimexolone |
| 1104010V0BBAAAA | Vexol 10mg/ml eye drops | Rimexolone |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Note: the licence number shown is as recorded in the compiled data and is not in the standard UK "PL XXXXX/XXXX" format; please verify it against the MHRA register.

<!-- review:begin uk-lic-20261106-rimexolone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Note: the licence number shown is as recorded in the compiled data and is not in the standard UK "PL XXXXX/XXXX" format; please verify it against the MHRA register. Only one valid single-ingredient authorisation is recorded." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-rimexolone-1 -->

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text):** herpes simplex virus keratitis, fungal infection of the eye, viral eye infection, ocular tuberculosis. These relate to the ophthalmic use of corticosteroids and would not necessarily transfer to dermatological use.

No drug interaction data were found.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible for the corticosteroid class, but there is no drug-specific clinical or published evidence (Evidence Level L5). The only available formulation is ophthalmic, and established topical corticosteroids already exist for seborrheic dermatitis and dermatitis.

**To proceed, the following is needed:**
- Mechanism of action data for rimexolone
- Warnings and contraindications from the SmPC and BNF, which are currently missing and block safety screening
- Preclinical data on skin penetration and dermal safety, and a suitable topical formulation and dose
- Assessment of route compatibility between the current ophthalmic product and a dermatological route
- Comparative rationale against existing topical corticosteroids and other approved treatments
- Early-phase clinical evidence in seborrheic dermatitis or dermatitis

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Only one valid single-ingredient authorisation is recorded" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

