---
layout: default
title: Inositol Nicotinate
parent: Model Prediction Only (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
monitor_inn: "Inositol nicotinate"
predicted_indications: ["vitamin deficiency disorder", "biotin metabolic disease", "non-syndromic esophageal malformation", "iron deficiency anemia", "acute urate nephropathy", "esophageal disease", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension"]
last_modified_at: 2026-10-23
description: "Inositol Nicotinate: predicted new indication Vitamin deficiency disorder (evidence level L5). Approved use: Pellagra and beriberi"
---

# Inositol Nicotinate
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

## Inositol nicotinate: From Pellagra and Beriberi to Vitamin Deficiency Disorder
{: .text-alpha }

## One-Sentence Summary

Inositol nicotinate is a hexanicotinate ester of inositol that releases nicotinic acid (niacin, vitamin B3). In the knowledge graph its recorded uses are pellagra and beriberi. The TxGNN model predicts it may be relevant to **vitamin deficiency disorder**, but **no clinical trials and no publications** were found to support this, so the prediction rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pellagra and beriberi (relations recorded in the knowledge graph; no licensed indication text is available in the UK data compiled for this report) |
| Predicted New Indication | Vitamin deficiency disorder |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, inositol nicotinate is hydrolysed in the body to release nicotinic acid (niacin, vitamin B3). Pellagra is the classic disease of niacin deficiency, so a broader "vitamin deficiency disorder" category is biologically plausible.

This is close to an extension of the drug's recorded uses rather than true repurposing. The category is broad, and niacin would only be expected to correct deficiency of niacin itself, not other vitamins. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No study of this drug in vitamin deficiency was found, and no direct study addresses the predicted disease, so the evidence level is L5.

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
| 0206040AFAAABAB (BNF-style product code; no PL number supplied) | Inositol Nicotinate Tab 750mg | Tablet | Not stated in the data compiled |

This is the only record, and it is a single-ingredient product. The data do not include approved indication text, so no licensed use can be confirmed here.

---

## Safety Considerations

No label-based warnings, contraindications or interaction data were available. The drug-interaction query returned no results.

**Relations recorded in the knowledge graph (not label text):** the knowledge graph links the drug to contraindication relations with the following conditions. These should be verified against the SmPC.
- Liver and gallbladder disease
- Peptic ulcer disease
- Gout
- Diabetes mellitus, hyperglycaemia and diabetic ketoacidosis
- Hypotensive disorder
- Thrombocytopenia and blood coagulation disease
- Cardiovascular and cerebrovascular conditions, including acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis, stroke, cerebral infarction and cerebral artery occlusion
- Haemoglobinopathy
- Hypophosphataemia
- Substance abuse or dependence

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is mechanistically plausible because the drug releases niacin, but it is essentially an extension of its recorded niacin-deficiency uses. There are no trials or publications for the predicted disease, and the safety data needed for screening are missing.
- The other nine predictions (for example biotin metabolic disease, iron deficiency anaemia, acute urate nephropathy and several hepatic or portal conditions) have no plausible supporting mechanism. Some conflict with niacin pharmacology, since niacin can raise uric acid and carries hepatotoxicity concerns. These are likely TxGNN model (deep learning) artefacts and are not recommended for further work.

**To proceed, the following is needed:**
- The SmPC and BNF warnings and contraindications for the UK product, confirming its licensed indication
- Mechanism of action data (for example from DrugBank)
- A literature search for inositol nicotinate or niacin in nutritional deficiency states
- Clarification of whether a vitamin-deficiency use adds anything beyond existing niacin or multivitamin supplementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

