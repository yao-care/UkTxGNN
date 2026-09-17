---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Tamsulosin is a selective alpha-1A adrenergic receptor antagonist, clinically established for the management of benign prostatic hyperplasia (BPH) and associated lower urinary tract symptoms.
> The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair-growth disorder,
> but this prediction is currently supported by **no clinical trials** and **no published literature** — the evidence pack itself flags this as a likely knowledge-graph artefact rather than a pharmacologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) — inferred from repurposing rationale text; no formal UK/MHRA licence data available in this pack |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% (raw score 0.99996) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (marked as a data gap). Based on known pharmacology, tamsulosin is a selective alpha-1 adrenergic receptor antagonist acting predominantly on the alpha-1A subtype found in prostatic and bladder-neck smooth muscle, and its efficacy in BPH is well established in clinical practice.

However, the evidence pack's own mechanistic assessment explicitly finds **no known biological link** between this alpha-1 blockade and Ambras type hypertrichosis universalis congenita, a rare congenital disorder associated with chromosomal rearrangements near 8q and dysregulation of the EDNRB regulatory region. The assessment attributes the high TxGNN score to indirect node connectivity in the knowledge graph (e.g. shared skin-appendage gene co-expression noise) rather than a genuine pharmacological mechanism.

This pattern is consistent across the top 10 predicted indications for this candidate: 8 of the 10 (including hypertrichosis, hypotrichosis, alopecia areata, isolated hair-shaft abnormalities, and unrelated developmental syndromes such as Dandy-Walker malformation and odontal/periodontal malformation syndromes) are explicitly flagged in the source rationale as lacking any credible mechanistic basis. The two exceptions with any literature at all — "alopecia" (rank 9) — are discussed below and are also assessed as non-supportive. Overall, this candidate should be treated as a low-confidence, exploratory prediction rather than a mechanistically plausible repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (Ambras type hypertrichosis universalis congenita).

*For context: the evidence pack also lists 2 papers under the lower-ranked "alopecia" indication (rank 9, TxGNN score 99.81%), but both are assessed as non-supportive of a tamsulosin–alopecia link:*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Review/Case series | JAMA Dermatology | Investigates suicidality and psychiatric adverse events associated with **finasteride** (a 5-alpha reductase inhibitor, mechanistically unrelated to tamsulosin) in alopecia/BPH patients |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Cohort | Cornea | Examines meibomian gland morphology in men with BPH; unrelated to scalp hair growth |

Both papers were retrieved only because the study populations overlapped with BPH patients, not because they evaluate tamsulosin's effect on hair growth or loss. They do not constitute mechanistic or clinical evidence for this repurposing candidate.

---

## UK Market Information

Tamsulosin (DB00706) is currently recorded as **Not Marketed** in this evidence pack, with 0 marketing authorisations listed. No licence-level product, dosage form, or indication data is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: key warnings, contraindications, and drug interaction data are recorded as data gaps in this evidence pack (see "To proceed" below) and could not be summarised here.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 10 top-ranked TxGNN predictions for this candidate are rated evidence level L4–L5 with no clinical trials and, apart from two tangentially related papers, no supporting literature. The evidence pack's own mechanistic review explicitly characterises the top prediction as lacking biological plausibility and likely reflecting knowledge-graph noise rather than a genuine drug-disease signal.
- Additionally, a **Blocking**-severity data gap exists for TFDA/MHRA product warnings and contraindications, which prevents this candidate from entering safety pre-screening (Stage S1) regardless of the indication signal.

**To proceed, the following is needed:**
- Official SmPC/product-label warnings and contraindications (currently blocking safety evaluation)
- Verified mechanism of action (MOA) data from DrugBank or equivalent source
- Independent mechanistic or preclinical evidence directly linking alpha-1 adrenergic antagonism to hair-growth pathways, before any further clinical validation is considered
- Confirmation of UK market/licensing status, given the drug is currently recorded as not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

