---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
monitor_inn: "Norfloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-30
description: "Norfloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Norfloxacin
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

## Norfloxacin: Polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibacterial.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Norfloxacin belongs to the fluoroquinolone class, which is generally understood to inhibit bacterial DNA gyrase and topoisomerase IV.

Polyclonal hyperviscosity syndrome is driven by excess immunoglobulins, not by a bacterial process. There is no plausible mechanistic link between an antibacterial DNA gyrase inhibitor and this condition. The high TxGNN score (0.9970) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by any clinical or literature data. It should be treated as a hypothesis-generating output only.

For context, other predictions for this drug (for example hyperamylasemia, congenital analbuminemia and diffuse scleroderma) also have no supporting studies. The only prediction with a biologically plausible rationale is septicemic plague (rank 10), supported by preclinical, class-level fluoroquinolone data, and even there norfloxacin's limited systemic exposure is a concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501120Q0AAAAAA | Norfloxacin Tab 400mg | Not stated | Not stated |

The single record is a single-ingredient product with valid status. The list is complete (1 of 1). Indication text and dosage form are not available in the data compiled for this report.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: The knowledge graph records contraindication relations with the following conditions, which should be verified against the SmPC:
  - Cardiac: long QT syndrome, familial long QT syndrome, torsades de pointes
  - Neurological and psychiatric: epilepsy, peripheral neuropathy, peripheral nervous system disease, anxiety disorder, psychotic disorder, mental disorder
  - Musculoskeletal: tendinitis, rhabdomyolysis
  - Hepatic and renal: liver failure, liver disease, cirrhosis, kidney disease
  - Metabolic and haematological: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, thrombocytopenia, anaemia
- **Drug Interactions** (100 interactions recorded; examples):
  - Major: hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids, which may add to tendon risk), bupropion, chlorpropamide
  - Moderate: antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, acetylsalicylic acid, and calcium- or other polyvalent cation-containing products (calcium acetate, calcium phosphate)

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials, no publications and no plausible mechanism linking norfloxacin to polyclonal hyperviscosity syndrome. The evidence level is L5.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting fluoroquinolone activity to immunoglobulin-driven hyperviscosity
- Any preclinical or clinical study directly addressing this disease
- Mechanism of action data for norfloxacin
- Licence indication and dosage form details for the UK product
- Review of the knowledge-graph contraindication relations against the SmPC
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

