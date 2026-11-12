---
layout: default
title: Penciclovir
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Penciclovir: predicted new indication Fascioliasis (evidence level L5). Approved use: Herpes labialis"
monitor_inn: "Penciclovir"
predicted_indications: ["fascioliasis"]
---

# Penciclovir
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

## Penciclovir: From Herpes Labialis to Fascioliasis
{: .text-alpha }

## One-Sentence Summary

Penciclovir is a topical antiviral originally used to treat herpes labialis (cold sores).
The TxGNN model predicts it may be effective for **fascioliasis**, but there are currently **no clinical trials** and **no publications** supporting this prediction, and no plausible biological mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes labialis |
| Predicted New Indication | Fascioliasis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (3 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, penciclovir is a guanosine nucleoside analogue. After phosphorylation by viral thymidine kinase, it inhibits herpesvirus DNA polymerase. This explains its efficacy in herpes labialis.

Fascioliasis is a liver fluke (trematode) infection. Flukes have no viral thymidine kinase and no herpesvirus-like DNA polymerase, so there is no plausible mechanistic link to penciclovir. The high score of 0.9906 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of efficacy.

The other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|

None of these predictions has supporting trials or publications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1310030L0AAAAAA | Penciclovir 1% cream | Penciclovir |
| 1310030L0BCAAAA | Fenistil Cold Sore 1% cream | Penciclovir |
| 1310030L0BBAAAA | Vectavir Cold Sore 1% cream | Penciclovir |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Penciclovir is marketed in the UK as a single-ingredient topical product. Please verify the authorisation details against the MHRA register and the BNF.

<!-- review:begin uk-lic-20261106-penciclovir-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data compiled for this report contain only one authorisation, and its record is incomplete (no dosage form, manufacturer or indication text). Please verify the authorisation details against the MHRA register and the BNF." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 3 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-penciclovir-1 -->

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There is no clinical, preclinical or literature support, and no plausible mechanism links a herpesvirus-specific, thymidine-kinase-dependent nucleoside analogue to a parasitic fluke infection. Established anthelmintic treatments act through unrelated targets.

**To proceed, the following is needed:**
- Any in vitro or in vivo evidence of anti-*Fasciola* activity, together with a proposed mechanism
- Detailed mechanism of action data for penciclovir
- Confirmation of authorisation details (dosage form, indication, manufacturer) from the MHRA register
- Review of the SmPC for safety information, as no warnings or contraindications were available
- Assessment of route compatibility: penciclovir is a topical cream, whereas fascioliasis requires systemic exposure

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data compiled for this report contain only one authorisation, and its record is incomplete (no dosage form, manufacturer or indication t" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

