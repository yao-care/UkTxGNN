---
layout: default
title: Acenocoumarol
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 3
---

# Acenocoumarol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Acenocoumarol: From Pulmonary Embolism and Thrombophilia to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Acenocoumarol is a vitamin K antagonist anticoagulant, originally used for pulmonary embolism and thrombophilia.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**,
but there are currently **no clinical trials and no publications** supporting this specific prediction, so it rests on model output and general anticoagulation rationale alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism; thrombophilia (from the TxGNN knowledge graph, as no approved indication text is available for the UK licence) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Acenocoumarol is a vitamin K antagonist. It inhibits VKORC1 and so reduces the synthesis of functional vitamin K-dependent clotting factors II, VII, IX and X. Note that detailed mechanism of action data was not available in the data compiled for this report; this description reflects the drug class's well-established pharmacology.

Heparin cofactor II deficiency is an inherited thrombophilia in which thrombin inhibition by dermatan sulfate and heparin is impaired, creating a prothrombotic state. Acenocoumarol is already used in thrombophilia and pulmonary embolism, and long-term oral anticoagulation is a plausible approach to preventing thrombosis in thrombophilic states.

This link is inferred from general anticoagulation logic and the model prediction. No condition-specific studies were identified, so the rationale should be treated as a hypothesis.

Two other related predictions were also generated, both with the same limitation (model prediction only, no trials or literature):
- **Factor 5 excess with spontaneous thrombosis** (score 99.78%)
- **Antithrombin deficiency type 2** (score 99.77%)

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0208020H0AAAAAA | Acenocoumarol Tab 1mg | Not specified | Not specified |

The licence is recorded as a valid single-ingredient product. The data compiled for this report did not include a UK PL number, dosage form or approved indication text, so these should be verified against the MHRA register and the BNF.

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 potential interacting drugs, none with a severity grade (all recorded as "Unknown"). Examples include acetylsalicylic acid, metronidazole, omeprazole, pantoprazole, lansoprazole, simvastatin, rosuvastatin, prednisolone, dexamethasone, hydrocortisone and metformin. As a vitamin K antagonist, acenocoumarol requires INR monitoring, and any of these combinations should be checked against the SmPC and BNF.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (L5 evidence), with no trials or publications for heparin cofactor 2 deficiency. The mechanistic argument is plausible but generic, and the safety data needed for screening are incomplete.

**To proceed, the following is needed:**
- Targeted literature search for vitamin K antagonist use in heparin cofactor II deficiency, and in the related antithrombin and factor V conditions
- Verified mechanism of action data
- UK licence details (PL number, dosage form, approved indication) and the SmPC warnings and contraindications
- Severity grading of the identified drug interactions
- Clinical expert review of whether thrombosis risk in this rare condition would justify long-term anticoagulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

