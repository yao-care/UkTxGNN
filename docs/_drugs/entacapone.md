---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinsonism (Adjunct to Levodopa Therapy) to PLA2G6-Associated Neurodegeneration

> **Note on scope:** This evidence pack's `original_indications` field and Taiwan/UK licence records are empty, and `original_moa` is flagged as a Data Gap. The "Parkinsonism / levodopa adjunct" characterisation below is not sourced from a regulatory record in this pack — it is general pharmacological background referenced within the pack's own repurposing-rationale text (ranks 4 and 7) and is flagged there as not being database evidence.

## One-Sentence Summary

Entacapone is a peripheral COMT (catechol-O-methyltransferase) inhibitor; no confirmed original-indication record is present in this evidence pack, though it is generally known as an adjunct to levodopa/carbidopa therapy in Parkinsonism. The TxGNN model's top-ranked prediction for this drug is **PLA2G6-associated neurodegeneration**, but this is currently supported by **zero clinical trials** and **zero publications** — it is a model-score-only prediction with only an indirect mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (Data Gap). Background pharmacology suggests peripheral COMT inhibitor / levodopa-carbidopa adjunct in Parkinsonism |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% (score 0.9976, rank 2999 of full candidate set) |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (Data Gap DG002, High severity). Based on the pharmacological background referenced elsewhere in this pack, entacapone is understood to act as a peripheral COMT inhibitor, reducing peripheral metabolism of levodopa to extend its central availability and half-life — a mechanism relevant to dopaminergic pathway modulation generally.

PLA2G6-associated neurodegeneration (part of the NBIA — neurodegeneration with brain iron accumulation — family) can present with parkinsonian features in some subtypes, giving an indirect theoretical link to the dopamine pathway. However, this link is explicitly characterised in the source rationale as indirect, and is not accompanied by any trial or literature evidence.

Given the complete absence of clinical trials or published literature for this drug-disease pair, this prediction should be read as an unvalidated model output (TxGNN score only) rather than a mechanistically grounded hypothesis. Notably, other lower-ranked candidates in this same evidence pack — discussed below — carry a more direct mechanistic story and at least some indirect trial evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No MHRA marketing authorisations are present in this evidence pack (`total_licenses: 0`); entacapone is recorded as **Not marketed** in the UK within this dataset. No product, dosage form, or approved-indication text is available to tabulate.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Additional note:** This evidence pack flags TFDA-equivalent label warnings/contraindications as a **Blocking** data gap (DG001) — meaning a formal S1 safety screen cannot be completed until product-label safety data is sourced (e.g. via SmPC/label retrieval). No drug-drug interaction data was found (`ddi.query_status: not_found`).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (PLA2G6-associated neurodegeneration) has no supporting clinical trials or literature, only an indirect mechanistic rationale, and an evidence level of L5 (model prediction only) — insufficient to progress past initial screening.
- Core safety data (label warnings/contraindications) and MOA data are both flagged as gaps, so even a positive efficacy signal could not currently clear a safety screen.

**To proceed, the following is needed:**
- Retrieve entacapone's confirmed original indication and SmPC/label data (resolves DG001, Blocking)
- Confirm mechanism of action via DrugBank or primary pharmacology sources (resolves DG002)
- Targeted literature/trial search specifically for entacapone and NBIA/PLA2G6-related neurodegeneration, beyond the current negative search result
- Preclinical or mechanistic studies establishing a direct (not merely symptomatic-overlap) rationale before considering trial-stage evaluation

---

### Other Candidates in This Evidence Pack (for context)

The pack contains 10 ranked predictions for entacapone. Three carry somewhat stronger mechanistic plausibility than the top-ranked candidate, though evidence remains indirect (diagnostic/observational trials only, no therapeutic trials):

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 4 | Paralysis agitans, juvenile, of Hunt (early-onset Parkinsonism) | 99.60% | L4 | Research Question | Direct mechanistic overlap (dopaminergic pathway); no trials found |
| 7 | Lewy body dementia | 99.25% | L4 | Research Question | 1 trial (NCT04246437), but diagnostic imaging only, not therapeutic |
| 10 | Progressive supranuclear palsy–corticobasal syndrome | 99.04% | L4 | Research Question | 1 trial (NCT02994719), observational gait study only; known poor dopaminergic responsiveness in this population |

These may warrant separate evaluation if the objective is to explore entacapone specifically within parkinsonian-spectrum disorders rather than the single top TxGNN-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

