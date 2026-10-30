---
layout: default
title: L-Lysine
parent: Model Prediction Only (L5)
nav_order: 354
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "L-Lysine: predicted new indication gastroparesis (disease) (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "L-Lysine"
predicted_indications: ["gastroparesis (disease)", "congenital prothrombin deficiency", "obsolete vitamin D deficiency"]
---

# L-Lysine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## L-Lysine: From an Unspecified Original Indication to gastroparesis (disease)
{: .text-alpha }

## One-Sentence Summary

L-Lysine is an essential amino acid marketed in a single-ingredient 1 g tablet, but no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **gastroparesis**, but there are **no related clinical trials** and the only retrieved publication does not study L-Lysine as a treatment.
This prediction rests on model output alone and is not supported by actual studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. L-Lysine is an essential amino acid, and no established pharmacological pathway linking it to gastric motility could be identified from the data compiled.

The model's high score appears to be a model-based association only. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The single publication retrieved concerns delivering mesenchymal stem cells from gelatin-alginate hydrogels to the stomach lumen. It does not use L-Lysine as a therapeutic agent.

Two other predictions were also generated: congenital prothrombin deficiency (score 0.9913) and vitamin D deficiency, a term now marked obsolete (score 0.9902). Neither has any trials or literature. Lysine's role in fibrinolysis (lysine analogues such as tranexamic acid are antifibrinolytics) does not correct a prothrombin deficiency, which is treated by factor replacement. No direct mechanism links L-Lysine to vitamin D status. These are noted for context only; the report focuses on the top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical (biomaterials delivery) | Bioengineering (Basel) | Delivery of mesenchymal stem cells from gelatin-alginate hydrogels to the stomach lumen as a possible gastroparesis therapy. It does not involve L-Lysine and is not evidence for this drug. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 091101000AAFDFD | L-Lysine Tab 1g | Not stated | Not stated |

The authorisation number above is shown as it appears in the compiled data. It does not follow the usual MHRA PL format, so it should be verified against MHRA records.

## Safety Considerations

- **Disease associations flagged as potential contraindications** (from the TxGNN knowledge graph, not from product label text): kidney disease (including chronic kidney disease, chronic renal failure and end-stage renal failure), nephrolithiasis and nephrocalcinosis, acute urate nephropathy, hypercalcaemia (including humoral hypercalcaemia of malignancy), sarcoidosis, phosphorus metabolism disorders, heart and cardiovascular disease, digitalis poisoning, ventricular fibrillation, phenylketonuria and other disorders of phenylalanine metabolism, and pyoureter.

No drug interaction data were found. Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials, and the sole publication is unrelated to L-Lysine as a treatment. No mechanistic link could be identified, and the original indication and mechanism are both missing.

**To proceed, the following is needed:**
- Original indication and approved indication text for the UK authorisation (including dosage form), verified against MHRA records
- Mechanism of action data for L-Lysine
- SmPC warnings and contraindications to complete the safety review
- Any primary evidence (preclinical or clinical) linking L-Lysine to gastric motility or gastroparesis
- A review of the kidney, calcium and cardiovascular contraindication signals before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

