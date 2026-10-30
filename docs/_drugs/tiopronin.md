---
layout: default
title: Tiopronin
parent: Model Prediction Only (L5)
nav_order: 620
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Tiopronin"
predicted_indications: ["renal tubular acidosis", "adult polyglucosan body disease", "tricarboxylic acid cycle disorder", "disease of transporter activity", "pyruvate metabolism disorder", "inborn disorder of fatty acid oxidation and ketone body metabolism"]
description: "Tiopronin: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tiopronin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Tiopronin: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Tiopronin is a thiol-based agent, originally used to treat cystinuria (a condition in which cystine stones form in the kidneys and urinary tract).
The TxGNN model predicts it may be effective for **renal tubular acidosis**, but this is a computational prediction only, with **no clinical trials** and **no publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tiopronin is a thiol-based agent that forms soluble mixed disulfides with cysteine. This is the basis of its use in cystinuria, where it reduces the formation of poorly soluble cystine stones.

The link to renal tubular acidosis is loose. Renal tubular acidosis is a defect in the kidney's acid-base transport, which is not a mechanism that thiol exchange is known to address. The only connection is that both conditions involve renal tubular handling of solutes and can feature kidney stones or calcium deposition in the kidney (nephrocalcinosis).

The high TxGNN score (0.9963) is a model prediction only. It should be treated as a hypothesis for further investigation, not as evidence of benefit.

**Other predicted indications**

The model also produced other high-scoring predictions, all at evidence level L5 with no trials or literature, and all with a recommendation of Hold:

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Adult polyglucosan body disease | 0.9953 | Caused by glycogen branching enzyme (GBE1) deficiency; no known mechanism by which tiopronin would correct this |
| Tricarboxylic acid cycle disorder | 0.9948 | Speculative antioxidant rationale only |
| Disease of transporter activity | 0.9942 | Very broad category that includes cystinuria; too nonspecific to be a repurposing target |
| Pyruvate metabolism disorder | 0.9926 | No established link; speculative redox rationale |
| Inborn disorder of fatty acid oxidation and ketone body metabolism | 0.9914 | Likely reflects shared metabolic disease categories |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001030Q0AAABAB | Tiopronin tablets 250 mg | Not specified | Not specified |

Only one valid single-ingredient authorisation was identified in the data compiled for this report. Dosage form and approved indication text were not available, and the number above is the identifier recorded in the data rather than a standard MHRA PL number. Please confirm the details against the MHRA register and the BNF.

## Safety Considerations

No label-based warnings, contraindications or drug interaction data were available.

**Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links tiopronin to contraindications in the following disease groups. These should be verified against the SmPC.
- **Kidney conditions:** kidney disease, nephrotic syndrome (including familial forms), lipoid nephrosis, proteinuria, anti-glomerular basement membrane disease, granulomatosis with polyangiitis, pyoureter
- **Blood disorders:** thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including several congenital and idiopathic forms), aplastic anaemia
- **Liver and gallbladder disease**
- **Neuromuscular disorders:** myasthenia gravis, neuromuscular junction disease

The kidney and blood-related signals are particularly relevant, as renal tubular acidosis is itself a kidney condition and any trial would need close renal and haematological monitoring.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (evidence level L5), with no trials or publications, and no plausible mechanism linking tiopronin's thiol chemistry to renal tubular acidosis or the other predicted conditions. The knowledge graph also flags kidney and blood disorders as contraindications.

**To proceed, the following is needed:**
- Mechanism of action data for tiopronin, and a defined mechanistic hypothesis for renal tubular acidosis
- Preclinical or case-level evidence supporting benefit in any predicted indication
- Verified UK label information (approved indication, dosage form, warnings, contraindications and interactions) from the SmPC and BNF
- Review of the knowledge-graph contraindication signals, particularly renal and haematological, against the SmPC
- A more specific disease target, since several predictions are broad categories or ultra-rare subtypes that are difficult to test
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

