---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 361
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
monitor_inn: "Lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
description: "Lanreotide: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Lanreotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Lanreotide: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Lanreotide is a somatostatin analogue originally used to treat acromegaly, hyperpituitarism and pituitary gigantism.
The TxGNN model predicts it may be effective for **hypertrichosis**, but this rests on a computational score alone, with **no clinical trials** and **no publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lanreotide is a somatostatin analogue that suppresses growth hormone (GH) and insulin-like growth factor 1 (IGF-1). Its efficacy in acromegaly is established, and mechanistically it may be applicable to conditions in which the GH/IGF-1 axis influences tissue growth.

IGF-1 signalling influences hair follicle growth, so a theoretical link to hair growth disorders is conceivable. However, this link is speculative. Hypertrichosis is a heterogeneous condition (congenital, drug-induced, or secondary to endocrine or metabolic disease), so any plausible mechanism would depend on the subtype.

The other top-ranked predictions are even less convincing. They include malformation syndromes with a dental component, syndromes featuring Dandy-Walker malformation, isolated genetic hair shaft abnormalities, and Ambras-type congenital hypertrichosis. These are structural or genetic developmental conditions, not driven by the GH/IGF-1 axis. The high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803043P0AAACAC | Lanreotide injection 90 mg/0.3 mL, pre-filled syringe | Injection | Not stated in the data compiled for this report |

This identifier follows a BNF-style product code rather than a standard PL number. Please verify the authorisation details against the MHRA register.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindication-related** (these come from drug-disease graph links, not from label text): hypertensive disorder, hypertension, liver disease, gallbladder disease, cholelithiasis, cholecystolithiasis, choledocholithiasis, hyperglycaemia, hypoglycaemia, hypothyroidism, myxoedema, congenital hypothyroidism, and impaired renal function.
- **Drug Interactions**: 100 interactions were identified, and the 20 listed were all classed as Moderate. They are mainly with glucose-lowering agents, because lanreotide can alter glucose regulation.
  - Insulins, including aspart, degludec, detemir, glargine, glulisine, and human isophane and regular.
  - GLP-1 receptor agonists: albiglutide, dulaglutide, semaglutide.
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin.
  - DPP-4 inhibitors: alogliptin, linagliptin.
  - Other oral agents: acarbose, metformin, pioglitazone, chlorpropamide, glimepiride.

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a model score (0.9997), with no registered clinical trials or publications, and the mechanistic link to hypertrichosis is speculative. The Evidence Level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for lanreotide, and a clearer biological case for the GH/IGF-1 axis in hair growth disorders
- A literature and trial search for somatostatin analogues in hypertrichosis, including subtype-specific analysis (congenital versus acquired)
- SmPC-based warnings and contraindications, and the approved indication text for the UK authorisation
- Preclinical or pilot studies to test plausibility before any clinical development
- A glucose, gallbladder and thyroid monitoring plan if clinical evaluation is ever considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

