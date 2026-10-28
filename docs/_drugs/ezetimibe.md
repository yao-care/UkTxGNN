---
layout: default
title: Ezetimibe
parent: Model Prediction Only (L5)
nav_order: 273
evidence_level: L5
indication_count: 1
monitor_inn: "Ezetimibe"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Ezetimibe: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hyperlipidaemia"
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ezetimibe: From Hyperlipidaemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Ezetimibe is a cholesterol-absorption inhibitor, with relations recorded in the knowledge graph for hyperlipidaemia, familial hypercholesterolaemia and sitosterolemia.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**,
but **no clinical trials** and **no publications that directly study this condition** were found, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidaemia (relation recorded in the knowledge graph; the licence record contains no indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9909 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From general knowledge, ezetimibe inhibits NPC1L1-mediated intestinal cholesterol absorption and lowers LDL-C.

CETP deficiency is a rare genetic condition characterised by markedly raised HDL-C, with LDL-C usually normal or low. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, since both conditions involve lipoprotein regulation. There is no direct mechanistic rationale for a therapeutic benefit. CETP deficiency is mainly a biochemical phenotype and is not a recognised condition requiring LDL-lowering therapy, so the prediction may reflect a similarity learned by the model rather than a real unmet clinical need.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The two publications retrieved concern lipid-lowering in general and do not study CETP deficiency in patients treated with ezetimibe.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Review | European Heart Journal | Overview of molecular targets for lipid lowering, covering LDL-C, triglycerides, apoB and Lp(a) in residual cardiovascular risk. |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Animal study | International Journal of Molecular Sciences | Heterozygous Ldlr-deficient hamster model used to evaluate a PCSK9 antibody in hyperlipidaemia and atherosclerosis. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0212000L0AAAAAA | Ezetimibe Tab 10 mg | Not stated | Not stated in the licence record |

The data compiled for this report contain one single-ingredient authorisation, currently valid. Please check the current MHRA record and the BNF for the full licensed indications.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: contraindication relations are recorded for pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis and nodular fasciitis. These must be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified. Those graded Moderate are:
  - Chenodeoxycholic acid
  - Eluxadoline
  - Rosuvastatin
  - Simvastatin

  Other listed interactions (for example pantoprazole, metformin, omeprazole, morphine and vancomycin) have an unknown severity grade.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or directly relevant publications exist, there is no clear mechanistic rationale, and CETP deficiency is not an established condition needing LDL-lowering treatment.

**To proceed, the following is needed:**
- Evidence that CETP deficiency has a clinical need for lipid-lowering treatment
- Studies that directly examine ezetimibe in CETP deficiency
- Mechanism of action data and a mechanistic rationale
- Licensed indication, dosage form and SmPC safety information for the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

