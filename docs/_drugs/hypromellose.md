---
layout: default
title: Hypromellose
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Hypromellose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Hypromellose: From Ophthalmic Excipient Use to Hepatic Veno-Occlusive Disease-Immunodeficiency Syndrome

## One-Sentence Summary

> Hypromellose is a cellulose-derived excipient/polymer, most commonly used as an artificial tear, ophthalmic lubricant, and tablet coating agent; it has no established systemic pharmacological or immunomodulatory activity.
> The TxGNN model predicts a possible link to **hepatic veno-occlusive disease-immunodeficiency syndrome**, a rare inherited immunodeficiency,
> but this prediction is currently supported by **no clinical trials and no literature**, and the evidence pack itself flags the score as likely knowledge-graph noise rather than a genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (Hypromellose is conventionally used as an artificial tear/ophthalmic lubricant and tablet-coating excipient; no formal indication or MOA data supplied) |
| Predicted New Indication | Hepatic veno-occlusive disease-immunodeficiency syndrome |
| TxGNN Prediction Score | 98.30% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap). Based on known information, Hypromellose is a cellulose derivative used almost exclusively as an inactive excipient — as an ophthalmic lubricant/artificial tear and as a film-coating/viscosity agent in oral formulations. It has no reported systemic absorption, immunomodulatory, or haematopoietic activity.

Hepatic veno-occlusive disease-immunodeficiency syndrome is a rare inherited disorder involving hepatic sinusoidal endothelial injury and combined immunodeficiency. There is no known pharmacological pathway by which an inert, topically/orally acting excipient such as Hypromellose could influence either hepatic sinusoidal endothelium or immune gene regulation.

The evidence pack's own rationale is explicit on this point: the high TxGNN score most likely reflects structural or co-occurrence noise in the knowledge graph — a known limitation for excipient-class "drugs" that appear across many unrelated formulations — rather than a true biological signal. This assessment is consistent across all ten ranked predictions for this drug (ranks 1–10), none of which describe a plausible mechanism, and only one (rank 8, psoriasis) has any associated trial or literature evidence, and that evidence concerns Hypromellose only as a delivery-vehicle excipient in unrelated formulations, not as an active therapeutic agent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No UK marketing authorisation is currently identified for Hypromellose in this evidence pack (market status: **Not marketed**; 0 licences on record). As an excipient/OTC ophthalmic lubricant, any UK-authorised products would need to be confirmed separately against the MHRA product database and BNF excipient listings.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: Warnings, contraindications, and drug-interaction data for this candidate are listed as an unresolved Blocking data gap in the evidence pack — a validated SmPC/PIL has not yet been obtained.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence, no plausible mechanistic link, and no UK marketing authorisation for this drug. The evidence pack itself attributes the high TxGNN score to likely knowledge-graph noise typical of excipient-class compounds, rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Resolution of the Blocking data gap: TFDA/MHRA-equivalent SmPC warnings and contraindications
- Verified mechanism of action (MOA) data from DrugBank or equivalent
- Any primary evidence (preclinical or clinical) in which Hypromellose itself — not merely a co-formulated agent — is the active intervention
- Re-evaluation of TxGNN output quality for excipient-class drug nodes before further pursuing this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

