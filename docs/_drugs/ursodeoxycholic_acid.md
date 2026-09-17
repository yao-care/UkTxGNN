---
layout: default
title: Ursodeoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 1
---

# Ursodeoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ursodeoxycholic Acid: From Primary Biliary Cholangitis to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a hydrophilic bile acid whose established uses relate to primary biliary cholangitis and gallstone dissolution. The TxGNN model predicts a possible role in **Homozygous Familial Hypercholesterolemia (HoFH)**, but this prediction is currently based on the model score alone, with **no supporting clinical trials or published literature**, and the mechanistic rationale itself raises significant doubts about biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary biliary cholangitis (PBC) and gallstone dissolution (drawn from the mechanistic rationale narrative; no UK licence data confirms this) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ursodeoxycholic acid is not available in this Evidence Pack (data gap). Based on the accompanying mechanistic rationale, UDCA's known pharmacology involves altering the composition of the bile acid pool, reducing biliary cholesterol saturation, and providing mild anti-apoptotic/cytoprotective effects — the basis for its use in PBC and gallstone dissolution.

However, the link to HoFH proposed by the model appears mechanistically weak, and arguably runs in the wrong direction. Cholesterol-lowering strategies that work through bile acid depletion (e.g. bile acid sequestrants) act by triggering compensatory **upregulation of the LDL receptor**. HoFH, by definition, is caused by **absent or non-functional LDL receptors** (receptor-negative or receptor-defective disease), so a mechanism dependent on LDL receptor upregulation would be expected to have little or no effect in this population.

Furthermore, UDCA is an **exogenous bile acid supplement**, not a bile acid sequestrant that depletes the bile acid pool. Its pharmacological direction is therefore essentially opposite to what would be required to drive an LDL receptor-mediated cholesterol-lowering effect. This mismatch is a key reason the evidence pack flags the rationale as "weak and direction-uncertain," and it substantially undermines confidence in the TxGNN prediction independent of the absence of clinical or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Ursodeoxycholic acid is currently recorded as **Not Marketed** in this data set, with **0 marketing authorisations** on file. No licence records are available to summarise approved indications, dosage forms, or product names.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by the TxGNN model score (Evidence Level L5), with no clinical trials or literature identified. The proposed mechanistic link is itself questionable, since HoFH's defining LDL receptor deficiency likely renders the proposed bile-acid-pool mechanism ineffective, and UDCA acts in the opposite pharmacological direction to what cholesterol lowering via this pathway would require.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for ursodeoxycholic acid (currently a data gap)
- Product label warnings and contraindications from the relevant regulatory source, needed before any safety pre-screening can proceed (currently a blocking data gap)
- Preclinical or mechanistic studies specifically evaluating UDCA in LDL receptor-negative/defective models relevant to HoFH
- Clarification of UK marketing/licensing status if repurposing is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

