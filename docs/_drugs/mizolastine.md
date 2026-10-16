---
layout: default
title: Mizolastine
parent: Model Prediction Only (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mizolastine: predicted new indication Acute intermittent porphyria (evidence level L5). Approved use: Allergic rhinitis"
---

# Mizolastine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Mizolastine: From Allergic Rhinitis to Acute Intermittent Porphyria

## One-Sentence Summary

Mizolastine is a second-generation H1 antihistamine, originally used to treat allergic rhinitis and vasomotor rhinitis.
The TxGNN model predicts it may be effective for **acute intermittent porphyria**,
but there are currently **no clinical trials** and **no publications** supporting this direction. The prediction is model-derived only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis; vasomotor rhinitis (from the TxGNN knowledge graph, as no approved indication text is available for the UK product) |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, mizolastine is a second-generation H1 antihistamine that acts on the histamine H1 receptor (HRH1). Its efficacy in allergic and vasomotor rhinitis is the basis of its original use.

No mechanistic link to acute intermittent porphyria has been established. This condition is a haem biosynthesis disorder caused by porphobilinogen deaminase deficiency, and no known antihistamine pathway connects to it. The high TxGNN score is a computational prediction and should not be read as evidence of efficacy.

Safety is also a concern: some drugs are porphyrinogenic, so the safety of mizolastine in porphyria would need explicit review before any further consideration.

### Other Predicted Indications

The model also ranked the following conditions highly. All are L5 (model prediction only, no trials or publications) with a recommendation of Hold.

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Psychogenic movement disorders | 99.71% | Mizolastine has limited CNS penetration, so a role is implausible without further evidence |
| 3 | Lingual-facial-buccal dyskinesia | 99.71% | Typically dopaminergic; no dopaminergic activity documented for mizolastine |
| 4 | Chronic tic disorder | 99.71% | Speculative link via histaminergic modulation of basal ganglia (H3 pathways); weak |
| 5 | Extrapyramidal and movement disease | 99.70% | Broad category; no specific pathway identified |
| 6 | Benign shuddering attacks | 99.70% | Self-limited paediatric condition that generally needs no drug treatment |
| 7 | Primary orthostatic tremor | 99.69% | Thought to involve central oscillators; no documented effect from H1 antagonism |
| 8 | Tremor-nystagmus-duodenal ulcer syndrome | 99.69% | Extremely rare; likely reflects network proximity rather than pharmacology |
| 9 | Benign paroxysmal tonic upgaze of childhood with ataxia | 99.68% | Rare channelopathy-associated condition with no known link to H1 antagonism |
| 10 | Carbamoyl phosphate synthetase I deficiency | 99.47% | Urea cycle disorder; an antihistamine would not correct the enzyme deficiency |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010AAAAAAAA | Mizolastine Tab 10mg M/R | Modified-release tablet | Not available in the data compiled for this report |

The identifier shown is a BNF-style code (BNF chapter 3, respiratory system, antihistamines) rather than a standard PL number. Please confirm the marketing authorisation details with the MHRA.

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacological entry, which is the drug's own target (the histamine H1 receptor, HRH1). It does not describe an interaction with another medicine.
- **Porphyria-specific caution**: The suitability of mizolastine in acute porphyria has not been assessed. Porphyrinogenic potential would need explicit review before any consideration.

For warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or publications, no plausible mechanistic link to acute intermittent porphyria, and a potential porphyrinogenic safety concern. The same applies to the other nine predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data for mizolastine, to support any mechanistic-link analysis
- Warnings and contraindications from the SmPC and BNF, which are currently unavailable and block safety screening
- Approved indication text and dosage form for the UK authorisation
- A porphyria-specific safety review (porphyrinogenicity)
- Preclinical or mechanistic studies demonstrating a biological rationale for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

