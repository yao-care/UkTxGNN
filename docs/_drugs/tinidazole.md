---
layout: default
title: Tinidazole
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Tinidazole: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). Approved use: Giardiasis, bacterial vaginosis, vaginitis, vulvitis, vulvovaginitis…"
monitor_inn: "Tinidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "blunt duct adenosis of breast", "apocrine adenosis of breast", "congenital human immunodeficiency virus", "AIDS related complex", "benign mammary dysplasia"]
---

# Tinidazole
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

## Tinidazole: From Giardiasis and Vaginal Infections to Postmenopausal Atrophic Vaginitis
{: .text-alpha }

## One-Sentence Summary

Tinidazole is a 5-nitroimidazole antimicrobial, originally used for giardiasis, bacterial vaginosis, trichomoniasis and amoebiasis.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Giardiasis, bacterial vaginosis, vaginitis, vulvitis, vulvovaginitis, amoebiasis (Entamoeba histolytica) and trichomoniasis (the UK licence record contains no indication text) |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, tinidazole is a 5-nitroimidazole antimicrobial with established activity against protozoa and anaerobic bacteria, and its efficacy in vaginal infections such as bacterial vaginosis and trichomoniasis is recognised.

The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between this indication and related approved vaginitis indications, not biological evidence. Atrophic vaginitis, however, is caused by oestrogen deficiency after the menopause, not by infection. An antimicrobial mechanism therefore has no clear rationale here, and the high score should be read as a likely model artefact rather than a biologically grounded signal.

Other predictions in the same list (for example vulvar ulceration, vulvar neoplasm and benign breast conditions) also lack a credible mechanism or supporting evidence. A plausible link exists only for ulceration of an infectious or anaerobe-associated origin.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for postmenopausal atrophic vaginitis.

---

## Literature Evidence

Currently no related literature is available for postmenopausal atrophic vaginitis.

Some literature was retrieved for the fifth-ranked prediction (AIDS). It concerns tinidazole's approved antiprotozoal uses (for example trichomoniasis and amoebiasis) in people with or at risk of HIV. It does not show that tinidazole treats HIV or AIDS, and it is not evidence for the predicted indication above.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0501110G0AAABAB | Tinidazole 500mg tablets | Tinidazole |
| 0501110G0BBAAAB | Fasigyn 500mg tablets | Tinidazole |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Dosage form, manufacturer and indication text are missing, so the MHRA and BNF entries should be checked directly.

<!-- review:begin uk-lic-20261106-tinidazole-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The record lists one valid single-ingredient authorisation. Dosage form, manufacturer and indication text are missing, so the MHRA and BNF entries should be checked directly." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-tinidazole-1 -->

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): epilepsy, neutropenia, agranulocytosis, peripheral nervous system disease and peripheral neuropathy.
- **Drug interactions**: 100 interactions were identified, and the entries reviewed were all rated Moderate. Examples include ethanol, paclitaxel, capecitabine, amiodarone, ethinylestradiol, estradiol, atorvastatin, bortezomib, levodopa and several barbiturates (amobarbital, butalbital). Many of these involve cytotoxic or oncology agents.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications, and the biology of oestrogen-deficiency vaginitis does not fit an antimicrobial. There is no case for repurposing tinidazole in this setting.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, for example whether a secondary infection or dysbiosis is involved in atrophic vaginitis
- Clinical or preclinical evidence in postmenopausal atrophic vaginitis, with comparison against established treatments such as vaginal oestrogen
- Mechanism of action data and full SmPC and BNF safety information, including the missing indication and dosage form for the UK authorisation
- A review of the neuropathy, neutropenia and epilepsy signals and of the alcohol interaction
- Route compatibility assessment (currently pending)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The record lists one valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

