---
layout: default
title: Tolcapone
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Tolcapone is a COMT (catechol-O-methyltransferase) inhibitor originally used as an adjunct to levodopa therapy in Parkinson's disease.
> The TxGNN model's top-ranked prediction is **Rasmussen Subacute Encephalitis**, but this is currently supported by **no clinical trials** and **no published literature**, and the model's own rationale flags it as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for tolcapone is not available as a formal record in this Evidence Pack. However, based on the model's own repurposing rationale, tolcapone is understood to be a peripheral/central COMT inhibitor acting on the dopamine metabolism pathway, and it has historically been used as an adjunct to levodopa in Parkinson's disease.

For the top-ranked candidate, **Rasmussen Subacute Encephalitis**, the mechanistic rationale provided by the model itself is weak: Rasmussen encephalitis is a T-cell-mediated autoimmune inflammatory encephalopathy with no known relationship to catecholamine metabolism. The model's high confidence score is most likely driven by co-occurrence of neurological nodes within the knowledge graph rather than genuine biological plausibility, and this is explicitly acknowledged in the supplied rationale.

Notably, among the ten candidates in this Evidence Pack, the **lowest-scoring** candidate (rank 10, "paralysis agitans, juvenile, of Hunt" — an historical term for juvenile-onset Parkinson's disease) shows the **strongest mechanistic coherence** with tolcapone's established pharmacology, since COMT inhibition would be expected to prolong levodopa/dopamine availability in this population. This illustrates that TxGNN ranking by score alone should not be taken as a proxy for clinical plausibility, and any further evaluation should prioritise mechanistically coherent candidates over the highest raw score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations are currently held for tolcapone in this dataset. Market status is recorded as **Not marketed**, with **0** total licences on file.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note from model rationale:** Several of the model's repurposing rationales (for candidates ranked 6 and 10) independently reference tolcapone's known hepatotoxicity risk, historically associated with a boxed warning in other jurisdictions. This has not been formally verified in this Evidence Pack (see data gap DG001 below) but should be treated as a material safety signal pending confirmation from the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All ten predicted indications are rated **L5** (model prediction only, no supporting clinical trials or literature), and the recommendation field in the Evidence Pack itself marks every candidate as "Hold."
- A **Blocking** data gap (DG001: missing MHRA/SmPC warnings and contraindications) prevents this drug from entering the safety initial screening stage (S1) for any indication.
- The top-ranked candidate (Rasmussen encephalitis) has a mechanistic rationale explicitly flagged as low-plausibility by the model itself, and no UK marketing authorisation currently exists for tolcapone.

**To proceed, the following is needed:**
- Formal MHRA/SmPC label data — key warnings, contraindications, and confirmed mechanism of action (currently marked as data gaps DG001 and DG002)
- Clinical or literature evidence for at least one candidate to move beyond L5
- If pursued, prioritise the mechanistically coherent candidate (juvenile-onset Parkinsonism, rank 10) over the highest-scoring but biologically weaker candidate (Rasmussen encephalitis, rank 1)
- Confirmation of tolcapone's hepatotoxicity profile before any consideration of use in vulnerable populations (e.g. Lewy body dementia, rank 6)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

