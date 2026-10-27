---
layout: default
title: Inositol Nicotinate
parent: Model Prediction Only (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Inositol Nicotinate: predicted new indication Vitamin deficiency disorder (evidence level L5). Approved use: Pellagra, beriberi"
monitor_inn: "Inositol nicotinate"
predicted_indications: ["vitamin deficiency disorder", "biotin metabolic disease", "non-syndromic esophageal malformation", "iron deficiency anemia", "acute urate nephropathy", "esophageal disease", "hepatoportal sclerosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension"]
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

## Inositol Nicotinate: From Pellagra and Beriberi to Vitamin Deficiency Disorder
{: .text-alpha }

## One-Sentence Summary

Inositol nicotinate is a niacin (vitamin B3) ester, with knowledge-graph indications of pellagra and beriberi.
The TxGNN model predicts it may be relevant to **vitamin deficiency disorder**,
but **no clinical trials and no publications** were identified in the data compiled for this report, so the prediction rests on model output and pharmacological reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pellagra, beriberi (from the TxGNN knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Vitamin deficiency disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (the data compiled for this report labels this prediction L4, but with no trials, literature or mechanistic studies, L5 is the appropriate level under the rules) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known pharmacology, inositol nicotinate is a hexanicotinate ester of inositol that releases niacin after hydrolysis. Pellagra, one of its original indications, is a niacin deficiency, and so is itself a vitamin deficiency disorder.

The high score for the broader category of vitamin deficiency disorder is therefore plausibly driven by this closely related indication, rather than by an independent signal. The link is indirect: no studies were provided showing that this drug corrects vitamin deficiency states in practice, and it is not clear that a slow-release niacin ester is a suitable way to treat deficiency compared with standard nicotinamide or niacin replacement.

Other predictions in the list (for example biotin metabolic disease, esophageal conditions and several liver disorders) show no credible mechanistic link and appear to reflect graph proximity or shared scores. Some, such as acute urate nephropathy, are mechanistically contradictory, because niacin tends to raise serum uric acid. They are not evaluated further here.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206040AFAAABAB (BNF-style product code; a PL number was not supplied) | Inositol Nicotinate Tablets 750 mg | Tablet | Not stated in the data available |

The product sits within the BNF cardiovascular chapter (section 2.6.3, peripheral vasodilators), based on the product code. Dosage form and indication text were not supplied, and no NICE-appraised indication was identified.

## Safety Considerations

- **Conditions flagged as contraindications or cautions in the knowledge graph** (derived from graph edges, not label text, so they should be checked against the SmPC):
  - Liver and biliary: liver disease, gallbladder disease
  - Metabolic: diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, gout, hypophosphataemia
  - Gastrointestinal: peptic ulcer disease
  - Haematological and bleeding: thrombocytopenia, blood coagulation disease, haemoglobinopathy
  - Cardiovascular and cerebrovascular: hypotensive disorder, acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis, stroke, cerebrovascular disorder, cerebral infarction, cerebral artery occlusion, brainstem infarction
  - Other: substance abuse/dependence
- **Drug interactions:** No interaction data were found.

Several of these cautions (gout, liver disease, diabetes) are relevant to any new use in a nutritional-deficiency population. Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and an indirect pharmacological link through niacin. There are no clinical trials or publications, and the safety data are incomplete.

**To proceed, the following is needed:**
- A literature and trial search specific to niacin-ester use in niacin or other vitamin deficiency states
- Mechanism of action and pharmacokinetic data (niacin release from the ester) to show it is suitable for deficiency treatment
- The SmPC, including approved indication, dosage form and formal warnings and contraindications, to complete safety screening
- A comparison with standard niacin/nicotinamide replacement to establish any added value
- Review of the knowledge-graph cautions (liver disease, diabetes, gout, peptic ulcer, cardiovascular disease) against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

