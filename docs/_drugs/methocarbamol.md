---
layout: default
title: Methocarbamol
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Methocarbamol
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

# Methocarbamol: From Skeletal Muscle Spasm to Cauda Equina Syndrome

## One-Sentence Summary

> Methocarbamol is a centrally-acting skeletal muscle relaxant; however, this evidence pack does not contain formal original-indication or mechanism-of-action data for the drug.
> The TxGNN model predicts a possible link to **Cauda Equina Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the score as likely unreliable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (flagged as a Blocking/High-severity data gap — see DG001/DG002) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for methocarbamol is not available in this evidence pack (DG002, High severity). This is a significant gap: without MOA data, it is not possible to construct a credible pharmacological link between methocarbamol and cauda equina syndrome, which is a neurosurgical emergency typically requiring urgent decompressive surgery rather than pharmacotherapy.

The TxGNN model itself flags this prediction as low-confidence despite the numerically high score (0.9998). The model's evidence layer notes that scores in this range fall within a "saturation band" seen across many unrelated disease predictions for this drug, which reduces their discriminative value. No clinical trials, ICTRP records, or PubMed literature were retrieved that directly connect methocarbamol to cauda equina syndrome.

Taken together, there is currently no mechanistic, preclinical, or clinical rationale to support this prediction. The same pattern — high TxGNN score, but no corroborating mechanistic or evidentiary support — is seen across all ten of the top predicted indications for this drug in this evidence pack (see table below), which suggests the ranking may reflect model artefact rather than genuine biological signal for methocarbamol specifically.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|----------------------|-------------|-----------------|------|
| 1 | Cauda equina syndrome | 99.98% | L5 | No mechanistic link identified |
| 2 | Irritable bowel syndrome | 99.98% | L5 | No mechanistic link identified |
| 3 | Panuveitis | 99.96% | L5 | No mechanistic link identified |
| 4 | Anaphylaxis | 99.96% | L5 | Only tangential literature (arthropod bite review) |
| 5 | Iris disease | 99.94% | L5 | No mechanistic link identified |
| 6 | Uveitis | 99.93% | L5 | No mechanistic link identified |
| 7 | Ventricular tachycardia | 99.93% | L5 | Literature is an unrelated case (canine lamotrigine toxicity) |
| 8 | Food-dependent exercise-induced anaphylaxis | 99.93% | L5 | No mechanistic link identified |
| 9 | Conjunctivitis | 99.93% | L5 | No mechanistic link identified |
| 10 | Obsolete bundle branch block | 99.93% | L5 | Target disease term is itself flagged as obsolete ontology |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

*(Note: for completeness, one tangentially relevant reference was retrieved under the rank 4 prediction — anaphylaxis, not the primary rank 1 prediction reported here — a 1998 review on arthropod bite management ([PMID 20086833](https://pubmed.ncbi.nlm.nih.gov/20086833/)) which mentions methocarbamol as one of several agents used for widow spider bite systemic reactions. This does not constitute direct evidence for the rank 1 predicted indication.)*

---

## UK Market Information

Methocarbamol has no marketing authorisations recorded in this evidence pack (market status: **not marketed**; 0 licenses on file). No product, dosage form, or approved-indication data is available to cross-reference against the predicted indication.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(No key warnings, contraindications, or drug interaction data were available in this evidence pack — all fields are flagged as data gaps, including a Blocking-severity gap for TFDA label warnings/contraindications, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on a TxGNN model score with no supporting mechanism-of-action data, no clinical trial evidence, and no relevant literature. The model's own evidence annotation flags the score as falling in a low-confidence saturation range, and this pattern repeats across all ten top-ranked predicted indications for this drug — indicating the signal is not yet distinguishable from noise for methocarbamol specifically.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain methocarbamol SmPC/label warnings and contraindications before any safety pre-screening (S1) can begin
- Resolve DG002 (High): obtain confirmed mechanism-of-action data to assess mechanistic plausibility against cauda equina syndrome
- Targeted literature/trial search specifically for methocarbamol AND cauda equina syndrome (or related neurogenic/compressive myelopathy conditions), since none was returned by the automated collectors
- Independent review of whether the TxGNN score saturation pattern reflects a genuine signal or a modelling artefact before committing further evaluation resources to this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

