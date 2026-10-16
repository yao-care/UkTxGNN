---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ofloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections (e.g. typhoid fever, urinary tract infection…"
---

# Ofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ofloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as urinary tract infection, bronchitis, bacterial pneumonia and typhoid fever.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but this is a purely computational prediction with **no clinical trials** and **no relevant publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (e.g. typhoid fever, urinary tract infection, bronchitis, bacterial pneumonia). The UK licence record contains no indication text, so this is taken from the knowledge-graph indication list. |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, and its efficacy in bacterial infections is well established.

For hyperamylasemia, however, no plausible mechanistic link has been identified. Hyperamylasemia is a laboratory finding with pancreatic, salivary and other non-infectious causes, and an antibacterial agent has no recognised action on these. The high TxGNN score is a graph-based prediction and should not be read as evidence of benefit.

Other predicted indications were also reviewed. Most (for example polyclonal hyperviscosity syndrome, congenital analbuminemia, monoclonal gammopathy and blood group incompatibility) have no mechanistic rationale. Only **septicemic plague** is biologically plausible, since *Yersinia pestis* is susceptible to fluoroquinolones. That is effectively an extension of the antibacterial indication, supported only by animal and in vitro studies (evidence level L4). It is not the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501120P0AAABAB (BNF code, as recorded) | Ofloxacin 400 mg tablets | Tablet | Not recorded in the data compiled |

Only one single-ingredient authorisation is recorded, and it is currently valid.

---

## Safety Considerations

**Contraindications / conditions of concern (from knowledge-graph drug–disease contraindication links, not label text):**
- Cardiac: long QT syndrome (including familial), torsades de pointes
- Neurological and neuromuscular: epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, peripheral neuropathy and other peripheral nervous system disease
- Hepatic and renal: liver failure, liver disease, drug-induced liver injury, kidney disease, impaired renal function
- Tendon and musculoskeletal: tendinitis, periarthritis, rhabdomyolysis
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Haematological: thrombocytopenia, leukopenia, anaemia
- Gastrointestinal: *Clostridium difficile* colitis, necrotising enterocolitis, gallbladder disease

**Drug interactions:** 100 interactions were identified. Major-level interactions include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Bupropion
- Chlorpropamide

Moderate-level interactions include antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, aspirin, balsalazide, bisacodyl and calcium and potassium salts.

Product-specific warnings and contraindications from the label were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of hyperamylasemia has no clinical, trial or relevant literature support and no plausible mechanism. The prediction is model-derived only (L5). The safety profile also includes several significant concerns.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking ofloxacin to hyperamylasemia, if one exists
- Label-based warnings and contraindications from the SmPC and BNF
- Mechanism of action data
- Approved indication text for the UK authorisation
- If a repurposing direction is pursued, consider septicemic plague as a better-supported research question. It would need human clinical data, and its UK regulatory and public health context would need review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

