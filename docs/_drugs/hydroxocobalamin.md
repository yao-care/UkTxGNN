---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 2
monitor_inn: "Hydroxocobalamin"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding"]
last_modified_at: 2026-11-12
description: "Hydroxocobalamin: predicted new indication Esophageal varices with bleeding (evidence level L5). Approved use: Not recorded in the local data"
---

# Hydroxocobalamin
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

## Hydroxocobalamin: Esophageal varices with bleeding
{: .text-alpha }

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, with relations recorded in the knowledge graph for vitamin B12 deficiency, cyanide poisoning and pernicious anaemia.
The TxGNN model predicts it may be useful for **oesophageal varices with bleeding** (and, with an identical score, oesophageal varices without bleeding),
but the data compiled for this report contain **no clinical trials and no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (11 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydroxocobalamin is a form of vitamin B12. Its relations to B12 deficiency and cyanide poisoning (where it binds cyanide to form cyanocobalamin) are recorded in the knowledge graph. It has no known role in portal hypertension, variceal haemostasis or splanchnic blood-flow regulation.

No established mechanistic link to oesophageal varices could be identified. One purely speculative angle is nitric oxide scavenging: hydroxocobalamin is known to bind nitric oxide and can raise blood pressure, which might theoretically reduce portal inflow. This has not been validated, and it also raises a safety concern (systemic hypertension and vasoconstriction) in a bleeding setting.

The very high TxGNN score is a model output only. The bleeding and non-bleeding variants receive an identical score (0.9923), which suggests the prediction reflects a shared disease-node embedding rather than a signal specific to either indication. Standard care (non-selective beta-blockers and endoscopic band ligation) has an established evidence base that this prediction does not address.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0901020N0AAAMAM | Hydroxocobalamin 10mg/2ml solution for injection ampoules | Hydroxocobalamin |
| 0901020N0AAAJAJ | Hydroxocobalamin 10mg/5ml oral liquid | Hydroxocobalamin |
| 0901020N0AAAIAI | Hydroxocobalamin 150micrograms/5ml oral liquid | Hydroxocobalamin |
| 0901020N0AAAKAK | Hydroxocobalamin 15mg/5ml oral liquid | Hydroxocobalamin |
| 0901020N0AAABAB | Hydroxocobalamin 1mg/1ml solution for injection ampoules | Hydroxocobalamin |
| 0901020N0AAAHAH | Hydroxocobalamin 2mg/5ml oral liquid | Hydroxocobalamin |
| 0901020N0AAAGAG | Hydroxocobalamin 3mg/5ml oral liquid | Hydroxocobalamin |
| 0901020N0AAADAD | Hydroxocobalamin 500micrograms/5ml oral liquid | Hydroxocobalamin |
| 0901020N0BDAAAB | Cobalin-H 1mg/1ml solution for injection ampoules | Hydroxocobalamin |
| 0901020N0BEAAAM | Megamilbedoce 10mg/2ml solution for injection ampoules | Hydroxocobalamin |
| 0901020N0BBAAAB | Neo-Cytamen 1000micrograms/1ml inj ampoules | Hydroxocobalamin |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The list is complete (1 of 1).

<!-- review:begin uk-lic-20261106-hydroxocobalamin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The record is a BNF-style product code rather than a PL number, and it is a single-ingredient product with valid status. The list is complete (1 of 1)." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 11 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-hydroxocobalamin-1 -->

## Safety Considerations

- **Knowledge-graph contraindication relations** (not label text): hypertensive disorder and hypertension. This is consistent with the known pressor effect of hydroxocobalamin and is relevant to any use in a bleeding patient.
- **Drug Interactions**: 32 interactions were identified in total (DDInter). Most are of unknown severity. Those graded **Moderate** are:
  - Arsenic trioxide
  - Chloramphenicol
  - Iodide I-131
  - Iodide I-123

  Other listed interactions, all of unknown severity, include omeprazole, lansoprazole, simvastatin, loperamide, prednisolone, ranitidine, aspirin, budesonide, folic acid, valsartan, ramipril, lorazepam, citalopram, paracetamol, mirtazapine and levothyroxine.

Warnings and contraindications from the product label were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications on oesophageal varices, no plausible validated mechanism, and a theoretical safety concern (raised blood pressure) in a bleeding condition. Established treatments already exist.

**To proceed, the following is needed:**
- Mechanism of action data and a testable mechanistic hypothesis linking hydroxocobalamin to portal hypertension
- Preclinical or early clinical evidence directly addressing oesophageal varices
- Label warnings and contraindications for the UK product, with a haemodynamic safety assessment
- Review of why the bleeding and non-bleeding variants share an identical score

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The record is a BNF-style product code rather than a PL number, and it is a single-ingredient product with valid status" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

