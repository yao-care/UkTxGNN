---
layout: default
title: Tiopronin
parent: Model Prediction Only (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
---

# Tiopronin
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

# Tiopronin: From Cystinuria to Renal Tubular Acidosis

## One-Sentence Summary

> Tiopronin is a thiol-containing compound reported in the evidence pack as being used clinically for cystinuria to reduce urinary cystine excretion.
> The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**,
> but currently **0 clinical trials** and **0 publications** directly support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystinuria (referenced in mechanistic rationale; not formally recorded in structured licensing data) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Tiopronin in this Evidence Pack. Based on the accompanying rationale, Tiopronin is a thiol (sulfhydryl-containing) compound whose known clinical use is in cystinuria, where it undergoes thiol-disulphide exchange with cystine to form more soluble mixed disulphides, thereby reducing renal cystine stone formation. This mechanism is centred on renal tubular cystine transport and binding chemistry, not on acid-base regulation.

Renal tubular acidosis, by contrast, is driven by dysfunction of tubular ion-handling machinery — principally H⁺-ATPase and HCO₃⁻/Cl⁻ exchangers — rather than by cystine handling. The evidence pack itself flags this gap explicitly, noting there is "no direct correspondence" between Tiopronin's known pharmacology and the acid-base transport defects underlying renal tubular acidosis. The mechanistic link is therefore speculative, arising from graph-based similarity in the TxGNN knowledge graph rather than from a demonstrated shared biological pathway.

Of the ten TxGNN-predicted indications provided, only one (rank 6, "disease of transporter activity" — a broad ontology category rather than a discrete clinical diagnosis) is supported by any literature, and even that literature describes basic mitochondrial and channel biology rather than disease-specific therapeutic evidence. This overall pattern — high TxGNN similarity scores paired with an absence of clinical or mechanistic corroboration — is consistent with an L5 evidence tier across the candidate set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Tiopronin does not currently hold any marketing authorisation in the United Kingdom (0 authorisations on record; market status: Not marketed). No product-specific formulation, dosage form, or approved indication text is available at this time.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (renal tubular acidosis) is supported only by TxGNN model similarity (Evidence Level L5), with no clinical trials or literature evidence, and the drug's own rationale note assesses the mechanistic link as speculative and lacking a direct biological correspondence. In addition, the drug is not marketed in the UK and lacks basic safety documentation (SmPC-derived warnings and contraindications are currently unavailable, flagged as a blocking gap), so it cannot proceed to safety screening.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) data (e.g. from DrugBank) to properly evaluate mechanistic plausibility
- SmPC/product label warnings, contraindications, and drug interaction data — required before any safety assessment can begin
- Confirmation of the drug's actual licensed indication(s), since the current dataset lists none
- If further exploration is pursued, prioritise the "disease of transporter activity" candidate (rank 6), which is the only one with supporting literature (L4), over the top-ranked renal tubular acidosis candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

