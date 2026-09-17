---
layout: default
title: Sulfamethoxypyridazine
parent: Model Prediction Only (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
---

# Sulfamethoxypyridazine
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

Using no additional skills — this is a direct documentation task governed entirely by the prompt's own template, which I'll follow exactly.

# Sulfamethoxypyridazine: From Antibacterial Use to Gout

## One-Sentence Summary

> Sulfamethoxypyridazine is a long-acting sulfonamide antibacterial (dihydropteroate synthase inhibitor); detailed original-indication and UK marketing data are not available in this evidence pack.
> The TxGNN model predicts a possible association with **Gout**, but this prediction is currently supported by **no clinical trials** and **no literature**, and is explicitly flagged as having no known mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no UK marketing authorisation data available; the drug is described elsewhere in this evidence pack only as a long-acting sulfonamide antibacterial |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured `original_moa` field for this drug (flagged as a High-severity data gap, DG002). Based on contextual information provided elsewhere in this evidence pack, sulfamethoxypyridazine is a **long-acting sulfonamide antibacterial** that inhibits dihydropteroate synthase, blocking bacterial folate synthesis — a mechanism relevant to treating bacterial infection, not urate metabolism.

The evidence pack's own assessment of this specific prediction states explicitly that **there is no known mechanistic link** between this antibacterial mode of action and urate metabolism or gout-related inflammatory pathways. The TxGNN score of 98.48% is therefore a pure knowledge-graph pattern-match rather than a pharmacologically plausible hypothesis, and is not corroborated by any clinical trial or published literature.

For context, among the ten predictions generated for this drug, the only candidate with substantive supporting evidence is **bronchitis** (rank 9, evidence level L2), reflecting the drug's genuine historical use in the 1960s–70s for infective exacerbations of chronic bronchitis. Gout, by contrast, sits at the opposite end of the evidence spectrum and should not be interpreted as a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

Sulfamethoxypyridazine currently holds **no marketing authorisation in the UK** (0 licences on record; market status: not marketed). No product name, dosage form, or approved indication text is available for extraction.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (gout) has a high TxGNN score but is backed by zero clinical trials, zero literature, and no known mechanistic link — the evidence pack itself flags this as evidence level L5 with no supportive rationale. Combined with the absence of UK marketing authorisation and a Blocking-severity data gap on labelling warnings/contraindications, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/UK labelling data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed original mechanism of action and original indication documentation — currently a High-severity data gap (DG002)
- Any mechanistic or preclinical rationale connecting sulfonamide antibacterial activity to urate metabolism, if this candidate is to be pursued further
- Consideration of whether **bronchitis** (rank 9, L2 evidence, historical RCT support) is a more appropriate candidate for further evaluation than gout
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

