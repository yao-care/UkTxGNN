---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 293
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

Using the evidence pack as given — no skill precisely covers ad-hoc report drafting from a supplied JSON template, so proceeding directly.

# Glimepiride: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea antidiabetic agent, pharmacologically established for type 2 diabetes mellitus. The TxGNN model predicts possible relevance to **focal stiff limb syndrome**, but this evidence pack currently contains **zero clinical trials and zero publications** supporting the association, and the pack's own mechanistic review flags the score as potentially reflecting model noise rather than genuine biology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from sulfonylurea pharmacology referenced in this pack; no formal regulatory indication text was supplied) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glimepiride is not available in this evidence pack (formally recorded as a data gap, DG002). Based on general pharmacological knowledge reflected elsewhere within this same evidence pack, glimepiride is a sulfonylurea-class agent that stimulates pancreatic β-cell insulin secretion by closing the K_ATP channel (SUR1/Kir6.2 subunits) — its well-established original indication being type 2 diabetes mellitus.

For the top-ranked predicted indication, focal stiff limb syndrome, the evidence pack's own mechanistic assessment finds **no plausible biological link**. Stiff limb/stiff person syndrome is a GAD65-antibody-mediated autoimmune neurological disorder, conventionally managed with GABA-enhancing agents (e.g. diazepam, baclofen) and immunotherapy — a pathway unrelated to sulfonylurea/K_ATP channel pharmacology.

The assessment explicitly notes that the very high TxGNN score (99.75%, rank 3118) may reflect embedding noise in the knowledge graph rather than a genuine pharmacological signal. This prediction should therefore be treated as hypothesis-generating only, not as evidence of clinical plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support, sits at the lowest evidence tier (L5), and the pack's own mechanistic review considers the drug–disease link biologically implausible, with the high prediction score possibly attributable to model noise. There is no basis to progress this candidate at present.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for glimepiride (currently marked as a blocking/high-severity data gap, DG001/DG002)
- SmPC-level warnings and contraindications, currently unavailable
- Independent expert review reconciling the K_ATP-channel/insulin-secretion mechanism with the GAD65-autoimmune pathology of stiff limb/stiff person syndrome before any further investment
- Re-evaluation once (or if) clinical trial or published case evidence becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

