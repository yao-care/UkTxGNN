---
layout: default
title: Fluticasone
parent: Model Prediction Only (L5)
nav_order: 302
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Fluticasone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the data compiled for this report (the products are inh…"
monitor_inn: "fluticasone"
predicted_indications: ["migraine disorder", "Prinzmetal angina", "migraine with brainstem aura"]
---

# Fluticasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Fluticasone: From Respiratory Disease (Inhaled Combination Products) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Fluticasone is an inhaled glucocorticoid, available in the UK within combination inhalers with salmeterol or formoterol.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no clinical trials** and only **1 publication** (a pharmacovigilance review of adverse events, not efficacy) in the data compiled for this report.
This prediction rests on model output alone and is not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the products are inhaled fluticasone combination inhalers) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (119 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 119 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluticasone is a glucocorticoid used in combination with long-acting beta-2 agonists (salmeterol, formoterol) in inhaled products. Its anti-inflammatory activity is established in airway disease, but this has not been shown to carry over to migraine.

Neuroinflammation has been proposed as a contributor to migraine, which is the only plausible conceptual link. However, inhaled fluticasone acts mainly locally and has low systemic bioavailability, so there is no established route by which it would reach a central neurological target. The very high score (0.9920) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same applies to the other two predictions in the data: **Prinzmetal angina** (score 0.9919) and **migraine with brainstem aura** (score 0.9909). Both are L5 with no trials or publications. Prinzmetal angina is driven by coronary vasospasm, for which calcium channel blockers and nitrates are standard, and there is no recognised pathway for fluticasone. Migraine with brainstem aura is a rare subtype, and its prediction likely reflects the same signal as migraine generally.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Review | Annals of Allergy, Asthma & Immunology | WHO pharmacovigilance review of neuropsychiatric disturbances reported with intranasal corticosteroids. It addresses adverse events, not efficacy, and if anything raises a safety signal rather than supporting therapeutic use. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1304000S0AAABAB | Fluticasone 0.005% ointment | Fluticasone propionate (Topical) |
| 1304000S0AAAAAA | Fluticasone 0.05% cream | Fluticasone propionate (Topical) |
| 0302000N0AABABA | Fluticasone 125micrograms/dose inhaler CFC free | Fluticasone propionate (Inhalation) |
| 0302000N0AABCBC | Fluticasone 250micrograms/dose inhaler CFC free | Fluticasone propionate (Inhalation) |
| 0302000N0AAAGAG | Fluticasone 25micrograms/dose inhaler | Fluticasone propionate (Inhalation) |
| 0302000N0AAAWAW | Fluticasone 2mg/2ml nebuliser liquid unit dose vials | Fluticasone propionate (Inhalation) |
| 1202010M0AAABAB | Fluticasone 400microgram/unit dose nasal drops | Fluticasone propionate (Nasal) |
| 0302000N0AAAVAV | Fluticasone 500micrograms/2ml neb liq unit dose vials | Fluticasone propionate (Inhalation) |
| 0302000N0AABHBH | Fluticasone 50micrograms/dose inhaler CFC free | Fluticasone propionate (Inhalation) |
| 1202010W0AAAAAA | Fluticasone furoate 27.5micrograms/dose nasal spray | Fluticasone furoate |
| 0302000N0AAADAD | Fluticasone propionate 100microgram inhalation pdr blist | Fluticasone propionate (Inhalation) |
| 0302000N0AAASAS | Fluticasone propionate 100micrograms/dose dry powder inhaler | Fluticasone propionate (Inhalation) |
| 0302000N0AAAEAE | Fluticasone propionate 250mcg inhalation pdr blist + dev | Fluticasone propionate (Inhalation) |
| 0302000N0AAAFAF | Fluticasone propionate 250microgram inhalation pdr blist | Fluticasone propionate (Inhalation) |
| 0302000N0AAATAT | Fluticasone propionate 250micrograms/dose dry powder inhaler | Fluticasone propionate (Inhalation) |
| 0302000N0AAAPAP | Fluticasone propionate 500microg inhalation pdr blist | Fluticasone propionate (Inhalation) |
| 0302000N0AAAQAQ | Fluticasone propionate 500microgram inhalation pdr blist | Fluticasone propionate (Inhalation) |
| 0302000N0AAAUAU | Fluticasone propionate 500micrograms/dose dry powder inhaler | Fluticasone propionate (Inhalation) |
| 0302000N0AAAAAA | Fluticasone propionate 50microg inhalation pdr blist | Fluticasone propionate (Inhalation) |
| 0302000N0AAABAB | Fluticasone propionate 50microgram inhalation pdr blist | Fluticasone propionate (Inhalation) |

Showing 20 of 119 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifiers shown are those in the compiled data and are not in the standard PL number format. Approved indication text and manufacturer details were not available.

<!-- review:begin uk-lic-20261106-fluticasone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both products are listed as valid single-entry records. The identifiers shown are those in the compiled data and are not in the standard PL number format." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 119 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-fluticasone-1 -->

---

## Safety Considerations

- **Drug Interactions**: 474 potential interactions were identified in the interaction database. Those with a defined severity include:
  - **Major**: clarithromycin (a strong CYP3A4 inhibitor, which can raise systemic corticosteroid exposure)
  - **Moderate**: aprepitant, inhaled rapid-acting human insulin
  - Many other entries (for example prednisone, triamcinolone, simvastatin, omeprazole, morphine) have no severity grading recorded.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a score from the TxGNN model (deep learning). There are no trials, and the single publication concerns adverse neuropsychiatric events, not benefit. There is no plausible mechanism by which a locally acting inhaled corticosteroid would treat migraine disorder, Prinzmetal angina or migraine with brainstem aura.

**To proceed, the following is needed:**
- Mechanism of action data and a credible pathway linking fluticasone to migraine pathophysiology
- Preclinical or clinical evidence of efficacy in migraine
- Warnings and contraindications from the SmPC and BNF, plus approved indication text for the UK products
- Assessment of route and systemic exposure, given that the available products are inhaled and migraine is a central condition
- Review of the neuropsychiatric safety signal reported with corticosteroids

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both products are listed as valid single-entry records" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

