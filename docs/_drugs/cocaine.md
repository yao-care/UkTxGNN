---
layout: default
title: Cocaine
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine: From No UK-Authorised Indication to Cauda Equina Syndrome

## One-Sentence Summary

Cocaine (DrugBank DB00907) currently holds no UK marketing authorisation, and no original indication is recorded in this evidence pack. The TxGNN model predicts a possible association with **Cauda Equina Syndrome**, but this is supported by only **1 tangentially related publication** and **no clinical trials**, and the evidence itself has been flagged by the pipeline's own rationale as a likely computational artefact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no UK marketing authorisation on record) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cocaine is not available in this evidence pack, which limits any assessment of biological plausibility for this predicted indication. No original indication is on record either, so no direct comparison between a prior approved use and cauda equina syndrome can be made.

The single supporting publication (PMID 31528422) is a case report and literature review of cauda equina syndrome arising from lumbosacral disc pathology. Critically, the article's content does not discuss cocaine administration or any therapeutic application of cocaine — the pipeline's own repurposing rationale notes this explicitly, describing the link as likely arising from embedding co-occurrence noise in the knowledge graph rather than a pharmacological relationship.

Given the absence of mechanistic data, the absence of clinical trials, and a reviewer-flagged concern that the sole literature match is off-topic, this prediction should be treated as unverified model output rather than a credible repurposing hypothesis at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case Report/Review | Surgical Neurology International | Case report and literature review of distal cauda equina syndrome caused by lumbosacral disc pathology; the article does not mention cocaine use or treatment. |

## UK Market Information

Cocaine has no UK marketing authorisation on record (0 licences; market status: Not marketed).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature support does not actually discuss cocaine, and the pipeline's own analysis assesses the association as likely computational noise rather than a real signal; there are no clinical trials, no UK marketing authorisation, and no mechanism-of-action data to substantiate biological plausibility.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC warnings and contraindications (currently a Blocking-severity data gap preventing entry to safety pre-assessment)
- Mechanism of action (MOA) data from DrugBank or equivalent source
- Independent literature or trial evidence directly linking cocaine to cauda equina syndrome, to confirm or rule out the current signal as spurious
- Route of administration and dosage form compatibility assessment, given cocaine's controlled-substance status and lack of current UK licensing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

