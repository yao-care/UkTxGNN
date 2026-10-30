---
layout: default
title: Amorolfine
parent: Model Prediction Only (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Amorolfine: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Onychomycosis (fungal nail infection)"
monitor_inn: "Amorolfine"
predicted_indications: ["drug-induced osteoporosis", "disease of retroperitoneum", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal cystic lymphangioma", "celiac trunk compression syndrome", "abdominal ectopic pregnancy", "lymph node palisaded myofibroblastoma", "sacrum chordoma", "urethral disease"]
---

# Amorolfine
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

## Amorolfine: From Fungal Nail Infection to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Amorolfine is a topical morpholine antifungal, used as a nail lacquer for fungal nail infections (onychomycosis).
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Onychomycosis (fungal nail infection); the UK authorisation record compiled for this report contains no indication text |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. Based on known pharmacology, amorolfine inhibits two enzymes in fungal ergosterol biosynthesis (sterol delta-14 reductase and delta-7,delta-8 isomerase). This damages the fungal cell membrane, which explains its efficacy in nail infections.

This mechanism has no established link to bone metabolism. Systemic exposure after topical application is minimal, so there is no plausible route by which it could affect bone. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other nine predictions (for example disease of retroperitoneum, lumbar spinal stenosis, sacrum chordoma and urethral disease) show the same pattern. All are Evidence Level L5, none has any trial or publication, and none has a mechanistic rationale. The pharmacology records show one target annotation, Nav1.7 (SCN9A), but no bioactivity data are given, and it does not support any of these predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1310020A0AAAAAA | Amorolfine HCl Nail Lacquer Kit 5% 5 ml | Nail lacquer (kit) | Not stated in the available record |

Note: the authorisation number above is shown as it appears in the compiled data and is not in the standard MHRA "PL XXXXX/XXXX" format, so it should be verified against the MHRA register. Please also confirm the NICE and BNF classification (BNF section on antifungal nail preparations) directly from the BNF.

---

## Safety Considerations

**Drug Interactions**
- The interaction query completed with one pharmacology record: amorolfine is annotated against the voltage-gated sodium channel Nav1.7 (SCN9A). No interaction severity level is given and no clinically relevant drug-drug interaction is reported.

No warnings or contraindications are available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5). There are no trials or publications, no plausible mechanism, and negligible systemic exposure from topical use. A high TxGNN score here should not be read as a pharmacological signal.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking amorolfine to bone metabolism (currently none)
- Confirmation of the original indication, dosage form and authorisation details from the MHRA register and SmPC
- Warnings and contraindications from the SmPC and BNF
- Evidence that a systemically active formulation would be feasible and safe, as the current topical product is unsuitable for this indication
- Reprioritisation of the candidate list, since none of the ten predictions has supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

