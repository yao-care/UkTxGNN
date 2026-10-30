---
layout: default
title: Ciprofibrate
parent: Model Prediction Only (L5)
nav_order: 172
evidence_level: L5
indication_count: 2
monitor_inn: "Ciprofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "fibroma of prostate"]
last_modified_at: 2026-10-30
description: "Ciprofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridaemia and familial combined hyperlipidaemia"
---

# Ciprofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Ciprofibrate: From Hypertriglyceridaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Ciprofibrate is a fibrate that acts on PPAR-alpha and is used to treat hypertriglyceridaemia and mixed hyperlipidaemia.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but there are **no clinical trials** and only **1 publication** (a 2003 preclinical mouse study), which does not show a therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia and familial combined hyperlipidaemia (relations recorded in the knowledge graph; the licence text available for this report contains no indication wording) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ciprofibrate is known as a fibrate and a PPAR-alpha agonist (the target is listed in the pharmacology records), which modulates lipoprotein metabolism by lowering triglycerides and raising HDL cholesterol.

The proposed link to CETP deficiency runs through shared lipoprotein pathways. However, CETP deficiency is characterised by already markedly raised HDL cholesterol, so there is no clear therapeutic reason to give an HDL-raising drug. The only retrieved publication describes a fibrate-associated paradoxical rise in cholesterol in apolipoprotein E-deficient mice, which is not evidence of benefit in CETP deficiency. The high score is a computational prediction and should be treated as a hypothesis only.

The second-ranked prediction, fibroma of prostate (score 0.9971), has no supporting trials or literature and no identifiable mechanistic link. It is likely a product of network topology and is not pursued here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14570884](https://pubmed.ncbi.nlm.nih.gov/14570884/) | 2003 | Preclinical (animal study) | The Journal of Biological Chemistry | In apoE-deficient mice, ciprofibrate worsened hypercholesterolaemia; adenoviral SR-BI overexpression reversed this. It does not address CETP deficiency directly. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 021200010AAAAAA | Ciprofibrate Tab 100 mg | Not stated | Not stated in the available record |

The data compiled for this report show one valid single-ingredient authorisation. The licence record has no indication text, so it does not by itself confirm any approved use. Ciprofibrate is described in pharmacology sources as used for severe hypertriglyceridaemia or mixed hyperlipidaemia when a statin is contraindicated or not tolerated, and as not approved by the US FDA or EMA.

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacological target relation (ciprofibrate acting on PPAR-alpha, gene *PPARA*). It is not a drug-drug interaction with a clinical severity rating.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study directly examines ciprofibrate in CETP deficiency, so the evidence level is L5 (model prediction only). The sole publication is a preclinical study of a different condition and points to a possibly unfavourable lipid effect. The rationale is also weak, since CETP deficiency already involves raised HDL cholesterol.

**To proceed, the following is needed:**
- Independent clinical or mechanistic evidence in CETP deficiency
- Mechanism of action data
- Warnings and contraindications from the SmPC and BNF
- Licence indication text and dosage form for the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

