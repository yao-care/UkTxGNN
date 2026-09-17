---
layout: default
title: Diflunisal
parent: High Evidence (L1-L2)
nav_order: 211
evidence_level: L2
indication_count: 10
---

# Diflunisal
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Diflunisal: From Pain and Inflammation (NSAID) to Ankylosing Spondylitis

## Note on Indication Selection

The Evidence Pack lists 10 TxGNN‑predicted indications. The single highest‑scoring one (acromesomelic dysplasia, Hunter‑Thompson type) is explicitly flagged in the model's own rationale as a likely **knowledge‑graph false positive** — no mechanistic plausibility, no trials, no literature, and a "Hold" recommendation. The same applies to ranks 2, 3, 4, 6, 7 and 9. Only **ankylosing spondylitis (rank 5)** carries real supporting evidence (a completed randomised trial plus corroborating cohort studies) and an evidence-based "Proceed with Guardrails" call. This report therefore focuses on ankylosing spondylitis as the clinically meaningful candidate, rather than the raw top-ranked score.

---

## One-Sentence Summary

> Diflunisal is a salicylate-derivative NSAID historically used for pain and inflammation; it is not currently marketed in the UK.
> Among the TxGNN model's predictions, the only indication with genuine supporting evidence is **Ankylosing Spondylitis**,
> where **1 historical randomised controlled trial** and **6 supporting publications** point to plausible efficacy — while the model's nominal top-ranked prediction is judged a graph-proximity artefact with no evidence at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from UK licensing data (drug not marketed); historically used as an NSAID analgesic/anti-inflammatory |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action text is not currently available for diflunisal. Based on the evidence assembled in this pack, diflunisal is a **salicylic acid derivative NSAID** that inhibits COX-1/COX-2 and reduces prostaglandin synthesis, giving it analgesic and anti-inflammatory activity — the same drug class as diclofenac, naproxen and pirprofen, all of which are referenced in the supporting literature for rheumatic disease.

NSAIDs are established first-line symptomatic therapy for axial spondyloarthritis, including ankylosing spondylitis (AS). Unlike most of the other TxGNN candidates in this pack (several rare skeletal dysplasias and a genetic susceptibility marker with no plausible inflammatory component), AS is an inflammatory arthropathy for which NSAID pharmacology is directly relevant — and diflunisal specifically has direct historical trial evidence in this population (see below), rather than being inferred purely from graph proximity.

The mechanistic story is therefore stronger for AS than for the model's nominal rank-1 prediction: AS shares the inflammatory/rheumatological pathway that diflunisal's pharmacology targets, whereas the higher-scoring but evidence-free predictions (skeletal dysplasias, genetic susceptibility, structural conditions) have no plausible link to COX inhibition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | RCT | Clinical Rheumatology | 12-week double-blind RCT (n=38) directly comparing diflunisal (500mg BID) vs phenylbutazone in AS; both effective, diflunisal showed more rapid analgesic onset, benefit maintained through 36-week open extension |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Cohort | Annals of the Rheumatic Diseases | 48-week study in the same diflunisal/phenylbutazone AS cohort; serum IgA correlated with disease activity (chest expansion, lumbar flexion) |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Cohort | The Journal of Rheumatology | Same AS trial cohort; assessed lung function (vital capacity) over 12–48 weeks of diflunisal vs phenylbutazone treatment |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review | Clinical Pharmacy | General NSAID-class review (diclofenac) — pharmacology/efficacy context, not diflunisal-specific |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Review | Drugs | NSAID-class review (diclofenac) covering use in AS and allied rheumatic conditions — class-level context |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Review | Drugs | NSAID-class review (pirprofen) including AS as an approved use — class-level context |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review | Drugs | NSAID-class review (naproxen) in rheumatic disease and pain states — class-level context |

---

## UK Market Information

No UK marketing authorisations currently exist for diflunisal (market status: not marketed; total licences: 0).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, directly comparative double-blind RCT (1986, n=38) plus two corroborating cohort analyses support diflunisal's efficacy in ankylosing spondylitis, and the mechanism (COX inhibition) is consistent with established NSAID use in axial spondyloarthritis. However, the evidence is decades old, from a small single trial, and diflunisal currently holds no UK marketing authorisation.

**To proceed, the following is needed:**
- UK SmPC / safety, warning and contraindication data (currently a Blocking data gap per this pack)
- Confirmation of DrugBank mechanism-of-action detail
- A contemporary systematic review or updated RCT, given the existing evidence is from the 1980s
- Regulatory pathway assessment given the drug is not currently marketed in the UK
- The remaining 9 TxGNN-predicted indications in this pack should be treated as **Hold** — they carry no clinical trial or literature support and are, per the model's own rationale, likely knowledge-graph proximity artefacts rather than genuine pharmacological signals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

