---
layout: default
title: Danaparoid
parent: Model Prediction Only (L5)
nav_order: 203
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
description: "Danaparoid: predicted new indication Glanzmann thrombasthenia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Danaparoid"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome"]
---

# Danaparoid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Danaparoid: From Anticoagulation to Glanzmann Thrombasthenia (Computational Prediction Only)
{: .text-alpha }

## One-Sentence Summary

Danaparoid is a heparinoid anticoagulant (a mixture of heparan sulfate, dermatan sulfate and chondroitin sulfate) with one marketing authorisation record in the data compiled for this report.
The TxGNN model predicts it may be relevant to **Glanzmann thrombasthenia**, but **no clinical trials and no publications** support this, and the biological rationale points in the opposite direction (anticoagulation would be expected to worsen bleeding).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From general pharmacology, danaparoid acts mainly through antithrombin-mediated inhibition of factor Xa, which reduces thrombin generation. It is used as an alternative anticoagulant in heparin-induced thrombocytopenia (HIT), an immune-mediated, prothrombotic condition.

Glanzmann thrombasthenia is a bleeding disorder caused by deficiency or dysfunction of platelet integrin αIIb/β3. Anticoagulation does not correct this defect and would plausibly increase bleeding risk. The high TxGNN score (0.9988) is most likely a network artefact arising from shared coagulation and platelet pathway nodes rather than a true therapeutic signal.

The other five predictions follow the same pattern. All are platelet or bleeding disorders where an anticoagulant would act in the wrong direction:

| Predicted Indication | TxGNN Score | Concern |
|------|------|------|
| Primary release disorder of platelets | 0.9988 | Granule secretion/signalling defect; anticoagulation could aggravate bleeding |
| Pseudo-von Willebrand disease | 0.9983 | GPIbα gain-of-function; no known danaparoid action on the GPIbα–VWF axis |
| Bleeding diathesis due to a collagen receptor defect | 0.9930 | Impaired collagen response; no modulation of receptor signalling |
| Haemorrhagic disorder due to constitutional thrombocytopenia | 0.9930 | Inherited low platelet number/function; HIT use does not translate |
| Scott syndrome | 0.9928 | Already reduced thrombin generation; danaparoid would reduce it further |

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
| 1314000H0AAAAAA | Heparinoid Crm 0.3% | Not stated | Not stated |

Dosage form, manufacturer and approved indication are not recorded for this authorisation. The record appears to be a topical heparinoid cream, which is not the same as the injectable danaparoid used as an anticoagulant. The licence number format also does not follow the usual MHRA "PL" pattern, so the record should be verified against the MHRA register and the BNF before any conclusions are drawn.

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified in total. The sample reviewed included the following **Major** interactions, mostly with other agents that increase bleeding risk:
  - Acetylsalicylic acid (aspirin)
  - Ibuprofen
  - Ketorolac
  - Abciximab
  - Alteplase
  - Acalabrutinib
  - Trastuzumab emtansine
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab (I-131)
- **Moderate** interactions included celecoxib, topical diclofenac, aliskiren, amiloride, sugammadex, fenfluramine, sibutramine, and iodide I-123/I-131.

Because the predicted indications are all bleeding disorders, concurrent use with antiplatelet agents or NSAIDs would be of particular concern. Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model output alone (evidence level L5), with no trials or publications. The mechanism is contrary to the proposed indications, because an anticoagulant would be expected to increase bleeding in platelet-function disorders. This is a safety concern, not just an evidence gap.

**To proceed, the following is needed:**
- Confirmation of the UK licence record, including product, dosage form and approved indication
- Mechanism of action data and SmPC/BNF safety information (warnings and contraindications)
- A biological justification for any benefit in platelet disorders, ideally from preclinical or mechanistic studies
- Review of whether other predicted indications with a more plausible link exist; the six candidates here are not recommended for further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

