---
layout: default
title: Sulfasalazine
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazine: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Sulfasalazine is a well-established disease-modifying anti-rheumatic drug (DMARD) originally used for rheumatoid arthritis and inflammatory bowel disease. The TxGNN model's top-ranked prediction for this drug is **Brachydactyly-Syndactyly Syndrome**, a rare congenital skeletal malformation disorder, but this pairing is currently supported by **no clinical trials and no published literature** — it is a pure knowledge-graph similarity prediction with no biological rationale identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory dataset provided; sulfasalazine's well-established clinical uses are rheumatoid arthritis and inflammatory bowel disease (ulcerative colitis, Crohn's disease) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not provided directly for this candidate (data gap DG002). However, based on information elsewhere in the evidence pack, sulfasalazine is known to be metabolised into sulfapyridine and 5-aminosalicylic acid (5-ASA), producing anti-inflammatory and immunomodulatory effects through NF-κB inhibition and suppression of prostaglandin/leukotriene synthesis. Its established indications — rheumatoid arthritis, spondyloarthritis, and inflammatory bowel disease — all involve chronic autoimmune or inflammatory pathology.

Brachydactyly-Syndactyly Syndrome, by contrast, is a rare congenital skeletal developmental disorder with no known autoimmune or inflammatory component. There is no established pathophysiological overlap between this condition and sulfasalazine's anti-inflammatory mechanism.

The evidence pack's own repurposing rationale for this candidate states explicitly that this is "purely a knowledge-graph embedding similarity prediction with no known mechanistic link and no supporting evidence." In other words, the model's very high similarity score reflects a statistical pattern in the underlying knowledge graph rather than any identified biological plausibility. This prediction should therefore be treated as exploratory only, and not as a basis for clinical or research prioritisation without further mechanistic investigation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No UK marketing authorisations are currently recorded for Sulfasalazine in this dataset (market status: Not marketed; total licenses: 0).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this pairing is high, but Evidence Level L5 means the prediction is unsupported by any clinical trial, literature, or identified mechanistic link — the evidence pack itself notes the absence of biological plausibility between sulfasalazine's anti-inflammatory action and this congenital skeletal syndrome. Notably, other lower-scoring candidates in the same prediction set for this drug (e.g. osteoarthritis, spondyloarthropathy susceptibility) carry considerably more supporting literature and clinical precedent, and would warrant separate, dedicated evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (via DrugBank or SmPC) to assess biological plausibility
- Product label safety data — key warnings and contraindications (currently a blocking data gap preventing initial safety screening)
- A dedicated mechanistic or genetic-association study exploring any indirect pathway between sulfasalazine and skeletal developmental disorders, if this candidate is to be pursued further
- Consideration of re-prioritising evaluation toward the drug's better-evidenced predicted indications (e.g. osteoarthritis, spondyloarthropathy) rather than this top-ranked but evidence-free candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

