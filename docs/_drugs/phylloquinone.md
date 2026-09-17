---
layout: default
title: Phylloquinone
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 9
---

# Phylloquinone
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

Using no additional skill — this is a direct content-generation task with a fully specified template already in the prompt, so I'll produce the report directly from the evidence pack.

# Phylloquinone: From Undocumented Original Indication to Renal Tubular Acidosis

## One-Sentence Summary

> The evidence pack contains no confirmed original indication or mechanism-of-action data for Phylloquinone (Vitamin K1, DrugBank ID DB01022).
> The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**,
> but this is supported by **0 clinical trials** and **0 publications** — the prediction rests on model score alone, and the model's own rationale notes no known biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Phylloquinone, and no original indication is recorded in the evidence pack. This absence of baseline pharmacological and clinical context makes it difficult to independently assess whether the predicted association is mechanistically plausible.

The evidence pack's own repurposing rationale for this candidate is explicit on this point: renal tubular acidosis is primarily driven by defects in renal tubular acid–base transport proteins (e.g. SLC4A1, ATP6V0A4/B1), whereas Phylloquinone's known biology (γ-glutamyl carboxylase cofactor, acting on clotting factors and osteocalcin) has no established overlap with this pathway. The rationale text states this prediction "purely reflects a TxGNN graph embedding score, with no biological theory in support."

The same pattern holds across all nine predicted indications in this evidence pack (renal tubular acidosis, hypophosphataemic rickets, Pendred syndrome, non-syndromic deafness, NAD(P)HX dehydratase deficiency, leukocyte adhesion deficiency, hypermanganesaemia with dystonia, Fraser syndrome, and Temtamy preaxial brachydactyly syndrome) — each rationale explicitly notes the absence of a credible mechanistic link. This candidate set should be regarded as exploratory model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

No marketing authorisations are recorded in the evidence pack. Phylloquinone is not currently marketed in the UK under this evaluation (0 licences on record).

## Safety Considerations

A Blocking data gap (TFDA product-label warnings/contraindications not yet retrieved) currently prevents completion of the S1 safety pre-screen for this candidate. No drug interaction data are on record.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications are L5 (model-score-only, no clinical trials or literature), and the top-ranked candidate's own mechanistic rationale explicitly states there is no known biological link between Phylloquinone's pharmacology and renal tubular acidosis. A Blocking data gap also prevents completion of the mandatory safety pre-screen.

**To proceed, the following is needed:**
- TFDA product-label warnings and contraindications (Blocking gap DG001)
- Confirmed mechanism of action via DrugBank (High-priority gap DG002)
- Documentation of Phylloquinone's original approved indication(s)
- Independent clinical or literature evidence for renal tubular acidosis (or any other candidate indication) before progressing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

