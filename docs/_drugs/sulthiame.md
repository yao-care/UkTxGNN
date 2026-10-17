---
layout: default
title: Sulthiame
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sulthiame: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the available authorisation data"
monitor_inn: "sulthiame"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "neurocirculatory asthenia", "anaphylaxis", "food-dependent exercise-induced anaphylaxis", "familial mitral valve prolapse", "mitral valve prolapse (disease)", "MVP1", "autonomic nervous system disease"]
---

# Sulthiame
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

# Sulthiame: From an Unspecified Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Sulthiame is a carbonic anhydrase inhibitor that is marketed in the UK, but the data compiled for this report do not state its original indication.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available authorisation data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, sulthiame is a carbonic anhydrase inhibitor. However, the authorisation records provided contain no approved indication text, so the relationship between its original use and the predicted indication cannot be assessed.

Cauda equina syndrome is typically a structural, compressive condition of the lower spinal nerve roots, and management is generally surgical. No plausible mechanistic link between carbonic anhydrase inhibition and this condition can be established from the available data. The high score (99.97%, model rank 816) is a computational signal only and should not be read as evidence of efficacy.

Other top-ranked predictions show the same pattern: none has clinical or literature support. These include obsolete neurogenic bladder (99.94%), irritable bowel syndrome (99.86%), neurocirculatory asthenia (99.79%), anaphylaxis (99.72%), food-dependent exercise-induced anaphylaxis (99.62%), three mitral valve prolapse entries (familial, general and MVP1, 99.4% to 99.5%) and autonomic nervous system disease (99.35%). The mitral valve prolapse and anaphylaxis entries overlap heavily and probably reflect a shared graph-neighbourhood signal rather than independent evidence. The "obsolete neurogenic bladder" term is flagged as obsolete in the ontology and would need mapping to a current term before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010Y0AAAAAA | Sultiame Tab 50mg | Not stated | Not stated |
| 0408010Y0BBABAB | Ospolot Tab 200mg (Import) | Not stated | Not stated |

Both records are listed as valid single-ingredient products. The identifiers shown are the codes in the compiled data, not confirmed MHRA product licence (PL) numbers, and no dosage form or indication text was available. Please check the current BNF and MHRA records for the authorised indications.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug interaction records were found in the data compiled for this report, and no contraindicated diseases were identified from the knowledge graph. This should not be taken as evidence of safety.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no publications and no data-supported mechanism. The original indication, warnings and contraindications are also missing, so a safety screen cannot yet be done.

**To proceed, the following is needed:**
- Authorised indications, dosage forms and SmPC safety information (warnings, contraindications) for both UK products
- Mechanism of action data, for example from DrugBank
- A systematic literature and trial registry search (including ISRCTN and EU CTR) for sulthiame in cauda equina syndrome and the other predicted conditions
- Mapping of the obsolete neurogenic bladder term to a current ontology term
- Consideration of whether a more clinically plausible candidate among the lower-ranked predictions is worth prioritising, given the weak rationale for the top prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

