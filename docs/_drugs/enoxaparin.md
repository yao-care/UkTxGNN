---
layout: default
title: Enoxaparin
parent: Model Prediction Only (L5)
nav_order: 250
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Enoxaparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "Enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
---

# Enoxaparin
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

## Enoxaparin: From Pulmonary Embolism and Disseminated Intravascular Coagulation to Protein C Deficiency Thrombophilia
{: .text-alpha }

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin, originally used for conditions including pulmonary embolism, disseminated intravascular coagulation (DIC) and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but **no clinical trials or publications** were identified in the data compiled for this report, so the prediction rests on model output and general pharmacology alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (knowledge-graph indications; no approved indication text available for the UK product) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The following is therefore based on general pharmacology rather than supplied data. Enoxaparin is a low-molecular-weight heparin. It enhances antithrombin activity and mainly inhibits factor Xa, with weaker inhibition of thrombin.

Severe autosomal recessive protein C deficiency leads to uncontrolled thrombin generation and thrombosis, including neonatal purpura fulminans. Because enoxaparin limits coagulation activation independently of the protein C pathway, anticoagulation is mechanistically plausible. The drug's existing indications in purpura fulminans, acquired purpura fulminans and DIC share this underlying pathophysiology.

The very high TxGNN score (0.996) is likely driven by this proximity within the knowledge network. It is a hypothesis-generating signal, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0208010D0AAABAB (BNF-style product code; PL number not available) | Enoxaparin Inj 100mg/ml 0.4ml Pfs | Prefilled syringe (injection) | Not available |

Enoxaparin sits within the BNF anticoagulants section (parenteral anticoagulants). No NICE-appraised indication for protein C deficiency was identified in the data compiled.

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report.

- **Knowledge-graph contraindication signals** (from drug–disease network edges, not label text): liver failure, haematological disease, thrombocytopenia (including heparin-induced thrombocytopenia), blood coagulation disorders, haemophilia, antithrombin III deficiency, Glanzmann thrombasthenia and qualitative platelet defects, intracranial and intracerebral haemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease, biliary tract disease, obstructive jaundice, infective endocarditis (including subacute bacterial endocarditis), osteoporosis (including postmenopausal), and retinal disease (including diabetic and hypertensive retinopathy, retinitis, diabetic cataract), and arteriosclerosis obliterans.
- **Drug interactions**: 100 interactions were recorded; 20 were provided for review. Major-level interactions include:
  - Antiplatelets and thrombolytics: acetylsalicylic acid, abciximab, alteplase
  - NSAIDs: ketorolac, ibuprofen
  - Others: deferasirox, acalabrutinib, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab (including I-131)
  - Moderate-level interactions include: fenfluramine, dexfenfluramine, sibutramine, sugammadex, aliskiren, radioiodine (I-123, I-131), topical diclofenac and ophthalmic ketorolac.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible and the TxGNN score is high, but there are no trials or publications for this indication, and label-based safety and mechanism data are missing. Evidence is at L5 (model prediction only).

**To proceed, the following is needed:**
- A literature and trial search specific to enoxaparin (and other LMWHs) in severe congenital protein C deficiency, including case series and neonatal purpura fulminans reports
- Mechanism of action data and SmPC warnings and contraindications for the UK product
- Authorisation details (PL number, dosage form, approved indication) for the UK product
- Review against existing standard of care in protein C deficiency (such as protein C concentrate and oral anticoagulation) and specialist haematology input
- A safety review addressing bleeding risk, thrombocytopenia and the paediatric/neonatal population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

