---
layout: default
title: Tinidazole
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tinidazole: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). Approved use: Giardiasis, bacterial vaginosis, vaginitis, vulvitis, vulvovaginitis…"
monitor_inn: "Tinidazole"
predicted_indications: ["ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "blunt duct adenosis of breast", "apocrine adenosis of breast", "AIDS related complex", "congenital human immunodeficiency virus", "benign mammary dysplasia"]
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

# Tinidazole: From Giardiasis and Vaginal Infections to Postmenopausal Atrophic Vaginitis

## One-Sentence Summary

Tinidazole is a 5-nitroimidazole antimicrobial, originally used for giardiasis, bacterial vaginosis, trichomoniasis and amoebiasis.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Giardiasis, bacterial vaginosis, vaginitis, vulvitis, vulvovaginitis, amoebiasis (Entamoeba histolytica) and trichomoniasis (the UK licence record contains no indication text) |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, tinidazole is a 5-nitroimidazole antimicrobial with established activity against protozoa and anaerobic bacteria, and its efficacy in vaginal infections such as bacterial vaginosis and trichomoniasis is recognised.

The prediction most likely reflects overlap with these approved vaginitis indications in the knowledge graph. Atrophic vaginitis, however, is caused by oestrogen deficiency after the menopause, not by infection. An antimicrobial mechanism therefore has no clear rationale here, and the high score should be read as a likely knowledge-graph artefact rather than a biologically grounded signal.

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

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501110G0AAABAB | Tinidazole tablets 500 mg | Tablet (not specified in the record) | Not specified in the record |

The record lists one valid single-ingredient authorisation. Dosage form, manufacturer and indication text are missing, so the MHRA and BNF entries should be checked directly.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

