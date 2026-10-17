---
layout: default
title: Apraclonidine
parent: Model Prediction Only (L5)
nav_order: 68
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Apraclonidine: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
---

# Apraclonidine
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

# Apraclonidine: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Apraclonidine is an alpha-2 adrenergic agonist eye drop, originally used to treat open-angle glaucoma.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but at present there are **no registered clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma (from the knowledge graph; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, apraclonidine is an alpha-2 adrenergic agonist thought to lower intraocular pressure (IOP) by reducing aqueous humour production. This link relies on general knowledge rather than on the supplied data.

Open-angle glaucoma and primary hereditary glaucoma share raised IOP as a key feature, so a mechanistic overlap is plausible for forms with elevated IOP. The very high TxGNN score is likely driven by the close similarity to the existing glaucoma indication, and it is a model-based prediction only.

There are important practical limits. Primary hereditary glaucoma, including congenital and juvenile forms, is mainly managed surgically. Alpha-2 agonists carry safety concerns in infants and young children, including CNS depression, bradycardia and apnoea, which restricts any extension to paediatric hereditary forms.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1108020J0AAABAB | Apraclonidine Eye Drops 5 mg/ml | Eye drops | Not stated in the available record |

One marketed single-ingredient authorisation is recorded. The licence record does not give a UK-format PL number, so please verify the details against the MHRA register, the BNF and any NICE guidance.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text, so they need checking against the SmPC): hypertension and hypertensive disorders; blood disorders (thrombocytopenia, neutropenia, agranulocytosis, inherited aplastic anaemia, Diamond-Blackfan anaemia, blood coagulation disease, thrombocytopenic purpura); lipid disorders (hyperlipidaemia, familial hyperlipidaemia); cholestatic liver conditions (cholestasis, benign recurrent and familial intrahepatic cholestasis); active peptic ulcer disease; intracerebral haemorrhage; leukaemia; and scurvy or ascorbic acid deficiency.
- **Drug Interactions**: 60 interactions were identified, and 20 are listed in the data compiled for this report. One is rated **Major**: methylene blue. The rest shown are rated Moderate, including:
  - opioids and related agents: morphine (including liposomal), opium, loperamide, diphenoxylate, difenoxin
  - cannabinoids: dronabinol, nabilone
  - sedating or CNS-active agents: promethazine, scopolamine, ethanol
  - other agents: metoclopramide, papaverine, sibutramine, amyl nitrite, diazoxide
  - prostacyclin-pathway agents: epoprostenol, iloprost, selexipag
- **Population concern**: alpha-2 agonists are associated with CNS depression, bradycardia and apnoea in infants and young children (general pharmacology, not from the supplied label data).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or literature, giving an evidence level of L5. Paediatric safety concerns and the surgical management of hereditary glaucoma further limit practical use.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC and BNF (currently missing, and blocking safety screening)
- Mechanism of action data, for example from DrugBank
- Clarification of the approved indication text and UK authorisation number for the licensed product
- A literature and trial search for apraclonidine in hereditary or congenital glaucoma
- A defined target population (adult versus paediatric forms) with a paediatric safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

