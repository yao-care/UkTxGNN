---
layout: default
title: Levocetirizine
parent: Model Prediction Only (L5)
nav_order: 372
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Levocetirizine"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
description: "Levocetirizine: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Levocetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Levocetirizine: Rheumatoid arthritis
{: .text-alpha }

## One-Sentence Summary

Levocetirizine is a selective histamine H1 receptor antagonist, originally used for allergic rhinitis, vasomotor rhinitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Levocetirizine is a selective histamine H1 receptor antagonist. Detailed mechanism of action data is not available in the data compiled for this report, so this description is based on the known drug class. Its efficacy in allergic and urticarial conditions comes from blocking histamine-driven symptoms.

Histamine is present in rheumatoid synovium and may contribute to vascular permeability and inflammatory signalling. This gives a plausible but unproven link between H1 blockade and rheumatoid arthritis.

The very high TxGNN score (0.9973) is a model prediction only. Allergic conditions and rheumatoid arthritis are quite different diseases, and no studies were identified to show that H1 antagonism alters the course of rheumatoid arthritis. The prediction should be treated as a hypothesis for further investigation.

*Other lower-ranked predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, score 0.9959; brachydactyly-syndactyly syndrome, score 0.9952) have no plausible mechanistic link. They are congenital developmental disorders that an antihistamine would not be expected to correct. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.*

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010ACAAAAAA | Levocetirizine Tab 5 mg | Tablet (5 mg) | Not stated in the compiled data |

The compiled data lists one valid single-ingredient authorisation. The identifier shown is in a non-PL format and should be checked against the MHRA register. The BNF classification (antihistamines, respiratory system chapter) and any NICE-appraised indications should be verified directly.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): kidney disease, pyoureter, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure. Renal impairment is a recognised consideration for levocetirizine dosing and should be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified. The examples reviewed are mostly of moderate severity, with central nervous system depressant or additive sedative effects being the most likely concern. Main examples:
  - Opioids and related agents: morphine (including liposomal), fentanyl, dihydrocodeine, opium, loperamide, diphenoxylate, difenoxin
  - Other sedating agents: ethanol, promethazine, chlorpheniramine, dronabinol, nabilone
  - Others: bupropion, metoclopramide, sibutramine, histamine, radioactive iodide (I-123, I-131)
  - Minor: hyaluronidase

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rheumatoid arthritis is supported only by a computational score. There are no clinical trials or publications, and the mechanistic link is speculative. The evidence is not sufficient to justify moving forward.

**To proceed, the following is needed:**
- Detailed mechanism of action data for levocetirizine
- A systematic literature search on histamine and H1 antagonism in rheumatoid arthritis, including preclinical and observational studies
- Confirmation of the approved indication, dosage form and authorisation details for the UK product from the MHRA register and SmPC
- Review of warnings and contraindications from the SmPC and BNF, with particular attention to renal impairment
- If preclinical rationale emerges, a proof-of-concept study design with appropriate safety monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

