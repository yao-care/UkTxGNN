---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 274
evidence_level: L5
indication_count: 9
monitor_inn: "Famciclovir"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
last_modified_at: 2026-11-12
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). Approved use: Not recorded in the local data"
---

# Famciclovir
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

## Famciclovir: Nucleoside analogue antiviral (prodrug of penciclovir) → post-infectious neuralgia
{: .text-alpha }

## One-Sentence Summary

Famciclovir is an oral antiviral that is converted in the body to penciclovir, which blocks herpesvirus DNA replication.
The TxGNN model predicts it may be useful for **post-infectious neuralgia**, but the evidence is thin: **1 related clinical trial** is registered, it tests a different drug (oxycodone), and **no publications** are linked to this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (8 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. From general pharmacology, famciclovir is a prodrug of penciclovir. Penciclovir is phosphorylated by viral thymidine kinase and then inhibits viral DNA polymerase, so it acts mainly against herpesviruses such as herpes simplex virus and varicella-zoster virus.

Post-infectious neuralgia, in practice usually postherpetic neuralgia, is nerve pain that follows a herpes zoster episode. A plausible argument is that treating the acute viral infection early could reduce nerve damage and so lower the later risk of neuralgia. This is a theoretical link only. Antivirals act on the virus, not directly on established neuropathic pain, and no study in the data compiled for this report tests famciclovir for preventing or treating this condition.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Tests early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the studied intervention, so this is indirect context only. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0503021E0AAABAB | Famciclovir 125mg tablets | Famciclovir |
| 0503021E0AAAAAA | Famciclovir 250mg tablets | Famciclovir |
| 0503021E0AAADAD | Famciclovir 500mg tablets | Famciclovir |
| 0503021E0AAACAC | Famciclovir 750mg tablets | Famciclovir |
| 0503021E0BBABAB | Famvir 125mg tablets | Famciclovir |
| 0503021E0BBAAAA | Famvir 250mg tablets | Famciclovir |
| 0503021E0BBADAD | Famvir 500mg tablets | Famciclovir |
| 0503021E0BBACAC | Famvir 750mg tablets | Famciclovir |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Dosage form, manufacturer and approved indication text are not recorded in the local data, so no further detail can be reported here.

<!-- review:begin uk-lic-20261106-famciclovir-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One valid single-ingredient authorisation is recorded for famciclovir (Famciclovir tablet 125 mg). Dosage form, manufacturer and approved indication text are not recorded in the local data, so no further detail can be reported here." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 8 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-famciclovir-1 -->

---

## Safety Considerations

- **Drug Interactions**: 84 potential interactions are recorded in the interaction database, all with an unclassified severity level. Examples include calcitriol, doxycycline, metformin, omeprazole, morphine, simvastatin and prednisolone. Their clinical significance has not been graded.

For warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no trial or publication directly studies famciclovir in post-infectious neuralgia. The only linked trial tests oxycodone, so the evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Clinical studies of famciclovir for preventing or treating postherpetic neuralgia, for example a comparison of early antiviral treatment against standard care
- Detailed mechanism-of-action data
- Warnings and contraindications from the current SmPC and BNF
- Review of the unclassified interaction records, especially for common co-medications

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient authorisation is recorded for famciclovir (Famciclovir tablet 125 mg)" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

