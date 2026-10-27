---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mecasermin: predicted new indication Monosomy X (evidence level L5). Approved use: Growth hormone insensitivity syndrome"
monitor_inn: "Mecasermin"
predicted_indications: ["monosomy X", "Wolman disease with hypolipoproteinemia and acanthocytosis", "esophageal varices with bleeding", "esophageal varices without bleeding", "autosomal ichthyosis syndrome with fatal disease course", "Gaucher disease", "varicose disease", "congenital pulmonary lymphangiectasia", "cholesteryl ester storage disease"]
---

# Mecasermin
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

## Mecasermin: From Growth Hormone Insensitivity Syndrome to Monosomy X
{: .text-alpha }

## One-Sentence Summary

Mecasermin is recombinant human insulin-like growth factor 1 (IGF-1), originally used for growth hormone insensitivity syndrome and Laron syndrome.
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**, but there are currently **no registered clinical trials and no publications** in the data compiled for this report. The prediction is therefore based on computational modelling alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Growth hormone insensitivity syndrome; Laron syndrome (from the knowledge graph, as the UK authorisation record has no indication text) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mecasermin is a recombinant form of IGF-1, the main mediator of growth hormone effects on growth. Its efficacy in growth hormone insensitivity (where the body cannot respond adequately to growth hormone) is established, and mechanistically it may be applicable to other conditions with short stature.

Monosomy X (Turner syndrome) is characterised by short stature, so involvement of the IGF-1 axis is biologically plausible. However, Turner syndrome is usually treated with growth hormone, which works through an intact growth hormone receptor. There is no clear reason, from the data compiled, to expect mecasermin to add benefit. The very high TxGNN score (0.996) is a computational signal only and is not backed by clinical evidence here.

Other predictions in the top 10 (for example Wolman disease, Gaucher disease, oesophageal varices, varicose disease and cholesteryl ester storage disease) have no identified mechanistic link to IGF-1 and appear to be driven by proximity in the knowledge graph. The one exception is growth hormone insensitivity syndrome with immune dysregulation 2 (STAT5B-related), which is closely related to the existing indication. It is better viewed as an extension of the current label than as true repurposing, and it warrants a targeted literature review. It would not address the immune component of the condition.

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
| 0607040A0AAAAAA | Mecasermin injection 10 mg/1 ml, 4 ml vial | Injection | Not stated in the data compiled |

The identifier above is a BNF-style product code (BNF section 6.7.4 area), not a standard MHRA PL number. The authorisation number, dosage form detail and indication text should be verified against the MHRA register and the current SmPC.

---

## Safety Considerations

**Drug Interactions**

A total of 24 interactions were recorded, all graded Moderate. The main concern is additive blood glucose lowering (risk of hypoglycaemia) with antidiabetic agents:

- **Sulfonylureas:** chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide
- **Meglitinide:** nateglinide
- **Insulins:** human (regular, isophane, zinc, zinc extended, inhaled), aspart (including protamine), degludec, detemir, glargine, glulisine and lispro (including protamine)

Mecasermin has insulin-like glucose-lowering effects, so close glucose monitoring is advisable if it is combined with any of these. Only 20 of the 24 recorded interactions were listed in the data compiled.

Please refer to the SmPC and BNF for warnings and contraindications, as these were not available in the data compiled. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no clinical trials or publications, and the mechanistic argument is weak because Turner syndrome patients have an intact growth hormone receptor and already have an established treatment.

**To proceed, the following is needed:**
- A systematic literature search for IGF-1 therapy in Turner syndrome, and for STAT5B-related growth hormone insensitivity as a possible label extension
- Mechanism of action data for mecasermin
- Full warnings and contraindications from the SmPC (a safety screening cannot be completed without them), including consideration of IGF-1's mitogenic effects
- The approved indication text and a verified MHRA authorisation record for the UK product
- Comparison against current standard care (growth hormone) to define any unmet need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

