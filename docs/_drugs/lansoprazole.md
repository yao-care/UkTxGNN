---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 362
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Lansoprazole: predicted new indication Duodenogastric reflux (evidence level L5). Approved use: Gastric ulcer, peptic ulcer disease…"
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
---

# Lansoprazole
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

## Lansoprazole: From Acid-Related Upper Gastrointestinal Disease to Duodenogastric Reflux
{: .text-alpha }

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor, originally used for acid-related upper gastrointestinal conditions such as gastro-oesophageal reflux disease, peptic and duodenal ulcer, and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, but there are currently **0 clinical trials** and only **1 general review article** behind this prediction, so it rests almost entirely on a computational prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis, duodenal ulcer, Zollinger-Ellison syndrome (from the knowledge graph; no licensed indication text is available for the UK product) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 (model prediction with no actual studies; the single review is general and does not address this indication) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, lansoprazole is a proton pump inhibitor that suppresses gastric acid secretion, and its efficacy in acid-related upper gastrointestinal disease is well established.

Duodenogastric (bile) reflux is mainly driven by the reflux of duodenal contents, such as bile acids and pancreatic enzymes, into the stomach. It is not primarily a problem of acid hypersecretion. Any benefit from lansoprazole would therefore be indirect, for example by reducing the acid component of mucosal injury and symptoms in mixed reflux. It would not correct the underlying motility or pyloric dysfunction.

The very high TxGNN score most likely reflects the closeness of this condition to approved gastrointestinal indications in the knowledge graph. It is a computational prediction, not clinical validation.

A second predicted indication, duodenal obstruction (score 99.68%), has no plausible direct mechanism. It is usually a mechanical or structural problem needing endoscopic or surgical management, and it has no supporting trial or literature evidence. It is not evaluated further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General update on proton pump inhibitors. They are first-choice drugs for peptic ulcer, *Helicobacter pylori* infection, GORD, NSAID-related gastrointestinal lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux directly. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103050L0AAAAAA (BNF code, section 1.3.5 proton pump inhibitors) | Lansoprazole capsules 30 mg (gastro-resistant granules) | Capsule | Not available in the compiled data |

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text, so they need verification against the SmPC):** the model lists associations with conditions including long QT syndrome and torsades de pointes, liver disease and liver failure, kidney disease, porphyria, osteoporosis, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders, blood coagulation disorders, anaemia, *Clostridium difficile* colitis and myasthenia gravis. These graph-derived associations should be interpreted with caution.

**Drug Interactions:** 100 interactions were identified. Examples from the first 20 reviewed:
- **Major:** acalabrutinib, atazanavir
- **Moderate:** for example hydrochlorothiazide, amphotericin B, amikacin, atorvastatin, fenofibrate, apalutamide, aprepitant, bosutinib, brigatinib, bromocriptine
- **Minor:** for example acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a network-based score and a general review of PPIs. Duodenogastric reflux is driven by non-acid duodenal contents, so any benefit from lansoprazole would be indirect at best.

**To proceed, the following is needed:**
- Clinical studies (or at least observational data) of lansoprazole in duodenogastric or bile reflux
- Mechanism of action data and a clearer mechanistic rationale beyond acid suppression
- The licensed indication, dosage form and SmPC safety details for the UK product
- Verification of the graph-derived contraindications against the SmPC, followed by a formal safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

