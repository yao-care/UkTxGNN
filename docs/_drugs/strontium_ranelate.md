---
layout: default
title: Strontium Ranelate
parent: Model Prediction Only (L5)
nav_order: 578
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Strontium Ranelate: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Postmenopausal osteoporosis"
monitor_inn: "Strontium ranelate"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "thrombophilia", "severe nonproliferative diabetic retinopathy"]
---

# Strontium Ranelate
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

# Strontium Ranelate: From Osteoporosis to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Strontium ranelate was originally used to treat postmenopausal osteoporosis and osteoporosis.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**,
but **no clinical trials and no publications** currently support this prediction, so it is a model-based hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis; osteoporosis (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, strontium ranelate acts on bone remodelling, through the calcium-sensing receptor and Wnt signalling, with both bone-forming and anti-resorptive effects. Its efficacy in osteoporosis is the basis of its original use.

No established mechanistic link connects this bone activity to heparin cofactor II (SERPIND1) function. The high TxGNN score most likely reflects proximity in the knowledge graph rather than a biological rationale. In addition, strontium ranelate has been associated with an increased risk of venous thromboembolism (VTE), which runs against any benefit in a thrombophilic condition.

### Other Predicted Indications (All Hold, Evidence Level L5)

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Antithrombin deficiency type 2 | 99.72% | No known action on antithrombin or the coagulation cascade. The VTE signal is a safety concern in this prothrombotic population. |
| 3 | Factor 5 excess with spontaneous thrombosis | 99.71% | No documented effect on factor V. Use in a prothrombotic disorder would be very high-risk. |
| 4 | Thrombophilia | 99.48% | The prediction is directionally inconsistent with the known raised VTE risk. |
| 5 | Severe nonproliferative diabetic retinopathy | 99.40% | Any vascular or inflammatory rationale is speculative. Literature review and preclinical work would be needed first. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0606020X0AAAAAA (BNF code) | Strontium Ranelate suspension granules, 2 g sachet, sugar free | Granules for oral suspension (sachet) | Not available in the data compiled |

The product is classed in BNF section 6.6 (drugs affecting bone metabolism). No NICE-appraised indication was available in the data compiled.

## Safety Considerations

- **Venous thromboembolism:** Strontium ranelate has been associated with an increased VTE risk, and use is restricted in patients at risk of, or with a history of, VTE. This is particularly relevant to all the predicted thrombosis-related indications above.

No drug interaction data were found in the data compiled. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (Evidence Level L5), with no trials or publications. Four of the five predicted indications are thrombotic conditions, where the known VTE risk of strontium ranelate makes benefit implausible and harm a real concern.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic assessment
- Full SmPC warnings and contraindications for the UK product, including approved indication text and marketing authorisation details
- A literature review and preclinical evidence for any predicted indication, with diabetic retinopathy the only one without a direct safety conflict
- A formal benefit-risk assessment of the VTE signal before any clinical question is framed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

