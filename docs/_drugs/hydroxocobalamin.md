---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydroxocobalamin: predicted new indication Esophageal varices without bleeding (evidence level L5). Approved use: Vitamin B12 deficiency, cyanide poisoning, pernicious anaemia"
monitor_inn: "Hydroxocobalamin"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding", "varicose disease", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "focal myositis", "inflammatory myopathy with abundant macrophages", "idiopathic eosinophilic myositis", "vitamin deficiency disorder", "congenital prothrombin deficiency"]
---

# Hydroxocobalamin
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

## Hydroxocobalamin: From Vitamin B12 Deficiency to Esophageal Varices Without Bleeding
{: .text-alpha }

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12, originally used to treat vitamin B12 deficiency, pernicious anaemia and cyanide poisoning.
The TxGNN model predicts it may be effective for **esophageal varices without bleeding**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, cyanide poisoning, pernicious anaemia (from the knowledge graph; no approved indication text is recorded for the UK product) |
| Predicted New Indication | Esophageal varices without bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydroxocobalamin is a form of vitamin B12 and a precursor of the coenzymes methylcobalamin and adenosylcobalamin. It corrects B12 deficiency and also binds cyanide, which underlies its use in poisoning.

We could not identify a plausible mechanistic link between these actions and oesophageal varices. Varices arise from portal hypertension, and hydroxocobalamin has no known effect on portal pressure or variceal pathophysiology. The high score (0.992) is a graph-based prediction and should be treated as a hypothesis-generating signal, not as evidence of benefit.

One theoretical angle is that hydroxocobalamin binds nitric oxide and could therefore raise vascular tone. This is speculative and no retrieved data support it. The same prediction score applies to oesophageal varices with bleeding, and the model's other top predictions (varicose disease, inflammatory myopathies, congenital prothrombin deficiency) also lack mechanistic support.

Note that the knowledge graph lists hypertension and hypertensive disorder as contraindication-type associations for this drug. This is not label text, but it should be considered given the cardiovascular context of the predicted indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for esophageal varices without bleeding.

The only prediction with retrieved literature was "vitamin deficiency disorder", which is largely reviews and guidelines on B12 deficiency. That overlaps with the existing licensed use and is not a novel repurposing finding.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0901020N0AAABAB (BNF-style product code, not a PL number) | Hydroxocobalamin injection 1 mg/ml, 1 ml ampoule | Injection (ampoule) | Not recorded in the data compiled for this report |

In UK practice, intramuscular hydroxocobalamin is the usual treatment for B12 deficiency (BNF chapter 9, nutrition and blood).

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: hypertensive disorder and hypertension.
- **Drug Interactions**: 32 interactions were identified in total. Those rated **Moderate** include arsenic trioxide, chloramphenicol, iodide I-131 and iodide I-123. Others, rated Unknown severity, include omeprazole, lansoprazole, ranitidine, simvastatin, prednisolone, budesonide, folic acid, valsartan and ramipril.

Warnings and contraindications from the product label were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no trials or publications, and no plausible mechanism links hydroxocobalamin to oesophageal varices. A knowledge-graph hypertension association adds a further reason for caution.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis, with preclinical data on portal pressure or variceal pathophysiology
- Mechanism of action data for hydroxocobalamin
- Label warnings and contraindications from the SmPC and BNF
- A systematic literature search specific to oesophageal varices and portal hypertension
- Review of established standard-of-care therapy (e.g. non-selective beta-blockers and endoscopic band ligation) to judge whether any unmet need exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

