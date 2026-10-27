---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 12
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Acarbose: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Acarbose"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Acarbose is an alpha-glucosidase inhibitor, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Acarbose is known to be an alpha-glucosidase inhibitor that acts locally in the gut to delay carbohydrate absorption and so reduce post-meal rises in blood glucose. Its efficacy in type 2 diabetes mellitus is established.

Focal stiff limb syndrome belongs to the stiff-person spectrum, a neuro-immunological group of disorders linked to GABAergic and glycinergic dysfunction. No credible mechanistic link to acarbose has been identified. The high score most likely reflects associations within the knowledge graph, for example shared diabetes-related autoimmunity, rather than a biological rationale.

The same pattern applies to the other top predictions, such as classic stiff person syndrome, which often co-occurs with diabetes. At most, acarbose might help manage coexisting post-meal hyperglycaemia, which is not a disease-modifying indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

## UK Market Information

The data compiled for this report show one marketed single-ingredient authorisation for acarbose 50 mg tablets. Authorisation number, dosage form, manufacturer and approved indication text were not available, so no table is shown. Please check the MHRA register and the BNF (antidiabetic drugs section) for full details.

## Cytotoxicity

Not applicable. Acarbose is not an antineoplastic drug.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model-derived associations, not from product label text): kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of liver, inflammatory bowel disease, hypoglycaemia, and injury.
- **Drug Interactions**: The interaction search returned 100 interactions in total. Examples of those listed:
  - Moderate: acetazolamide, salbutamol, aloe vera leaf, alpelisib, amprenavir, aripiprazole, asenapine, atazanavir, bedaquiline, bendroflumethiazide, betamethasone, asparaginase (both forms), benzphetamine, benzthiazide.
  - Minor: albiglutide, alclometasone (topical), lipoic acid, amcinonide, anisindione.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and no plausible mechanism links an intestinal alpha-glucosidase inhibitor to focal stiff limb syndrome. The high score most likely reflects graph-based association with diabetes.

**To proceed, the following is needed:**
- Detailed mechanism of action data for acarbose
- A mechanistic rationale connecting acarbose to GABAergic or glycinergic neuro-immunological pathways
- Preclinical or case-based evidence in stiff-person spectrum disorders
- Full UK authorisation details and label-based warnings and contraindications from the SmPC and BNF
- Review of the other predicted indications; none has direct evidence. The one with literature, pancreatic agenesis, is supported only by general diabetes papers, and acarbose would not replace insulin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

