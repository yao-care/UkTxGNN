---
layout: default
title: Levamisole
parent: Model Prediction Only (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Levamisole: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Ascariasis and hookworm infection (ancylostomiasis)"
monitor_inn: "Levamisole"
predicted_indications: ["drug-induced osteoporosis", "benign neoplasm of tongue", "cervical neuroblastoma", "epiglottis neoplasm", "benign neoplasm of buccal mucosa", "cystic neoplasm", "benign neoplasm of floor of mouth", "schwannoma of jugular foramen", "benign neoplasm of hypopharynx", "neoplasm of major salivary gland"]
---

# Levamisole
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

## Levamisole: From Ascariasis and Hookworm Infection to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Levamisole was originally used to treat intestinal worm infections (ascariasis and hookworm infection).
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but there are currently **no clinical trials** and **no publications** supporting this prediction; it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascariasis and hookworm infection (ancylostomiasis) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levamisole is an anthelmintic that is also recognised as an immunomodulator. Its efficacy in roundworm and hookworm infection is established, but nothing in the data compiled for this report links it mechanistically to bone metabolism or drug-induced bone loss.

The very high TxGNN score reflects a pattern in the knowledge graph rather than demonstrated biology. The model also ranked many other conditions (mostly neoplasms) with near-identical scores, so the score alone does not distinguish a credible prediction from a spurious one. At this stage the prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

For context, literature was identified for other lower-ranked predictions (for example, head and neck cancer adjuvant studies and hamster cheek pouch carcinogenesis studies). These do not support the leading prediction and are not evidence for drug-induced osteoporosis.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0505020L0AAABAB | Levamisole HCl Tab 50mg | Tablet (50 mg) | Not specified in the data compiled |

The data record one valid single-ingredient authorisation. The authorisation number is not in the standard UK PL format, and no dosage form, manufacturer or indication text was available, so the UK authorisation status should be verified against the MHRA register and the BNF.

---

## Safety Considerations

**Drug Interactions:** The interaction screen identified 73 potential interactions. Examples include:

- **Major:** deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine
- **Moderate:** ethanol, warfarin, zidovudine, azathioprine, chloramphenicol, alemtuzumab, anakinra, canakinumab, palifermin, strontium chloride Sr-89, and several live or inactivated vaccines

Many of the major interactions involve immunosuppressive or myelosuppressive agents, which is relevant given the known risk of agranulocytosis with levamisole. This risk is general pharmacological knowledge and was not drawn from label data compiled for this report.

For warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no supporting literature and no plausible mechanistic link to bone metabolism. Levamisole also carries safety concerns, including the risk of agranulocytosis and a large number of major interactions.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale connecting levamisole to bone loss
- Preclinical or observational evidence in drug-induced osteoporosis
- Warnings and contraindications from the SmPC and BNF, followed by safety screening
- Verification of the UK authorisation, including dosage form and approved indication
- Consideration of existing, well-established treatments for drug-induced osteoporosis, to judge whether any repurposing is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

