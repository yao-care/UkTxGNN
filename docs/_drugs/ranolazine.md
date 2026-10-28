---
layout: default
title: Ranolazine
parent: Model Prediction Only (L5)
nav_order: 536
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Ranolazine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Ranolazine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
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

## Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ranolazine is a modified-release tablet marketed in the UK; the data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with a very high score, but there are **no clinical trials** and **no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Ranolazine's generally known pharmacology includes inhibition of the late sodium current, some effect on the hERG potassium current, and partial inhibition of fatty acid oxidation. No established link between these actions and NSIAD has been identified.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor gene (*AVPR2*, R137C/L). These cause constitutive receptor activation and unregulated insertion of aquaporin-2 into collecting duct cells. A connection through renal sodium handling or cAMP signalling is conceivable but purely speculative and unsupported by data.

The high score (0.9965 for nephrogenic syndrome of inappropriate antidiuresis) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206030Z0AAABAB (BNF code) | Ranolazine 500 mg modified-release tablets | Modified-release tablet | Not stated |

Note: the identifier shown is a BNF-style product code rather than an MHRA PL number. BNF chapter 2 (cardiovascular system) classification is indicated by the code prefix.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug–disease edges in the TxGNN knowledge graph, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, pyoureter, cirrhosis of the liver. These are relevant given that the proposed new indication involves a renal condition.
- **Drug interactions** (100 recorded; selected examples):
  - **Major:** aprepitant, dexamethasone, clarithromycin, dolasetron, eliglustat
  - **Moderate:** famotidine, metformin, loperamide, bisacodyl, budesonide, canagliflozin, dapagliflozin, empagliflozin
  - **Minor:** bupropion, lorcaserin, cimetidine

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score. There are no trials or publications, no established mechanistic link, and the knowledge graph flags kidney disease and QT-related contraindications. The evidence level is L5.

**To proceed, the following is needed:**
- Confirmation of the original licensed indication from the MHRA SmPC
- Mechanism of action data and a testable hypothesis linking ranolazine to V2 receptor/aquaporin-2 signalling
- Preclinical or in vitro evidence in NSIAD-relevant models
- Review of the SmPC warnings and contraindications, particularly QT prolongation and renal/hepatic impairment
- Assessment of interaction risk, especially with CYP3A4 and P-gp inhibitors such as clarithromycin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

