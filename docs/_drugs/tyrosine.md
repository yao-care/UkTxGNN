---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From Unestablished Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine (DrugBank ID DB00135) is a naturally occurring amino acid; no established original indication or marketing history is recorded in the current Evidence Pack, and it does not hold any current UK marketing authorisation. The TxGNN model's top-ranked prediction is **Cauda Equina Syndrome**, but this is supported by **0 clinical trials** and only **1 unrelated case report**, and the evidence review explicitly flags it as a likely false-positive signal with no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no original indication data is recorded in the Evidence Pack |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tyrosine in this Evidence Pack (`original_moa: [Data Gap]`), and no original indication is on record. This alone limits how confidently any repurposing rationale can be constructed.

More importantly, the evidence reviewer's own assessment of this specific prediction states that there is **no mechanistic link** between tyrosine and cauda equina syndrome. The single supporting literature record concerns a case of clear cell sarcoma originating in a spinal nerve root (misdiagnosed as psammomatous melanotic schwannoma) — a tumour biology case report that has no direct connection to either tyrosine pharmacology or cauda equina syndrome pathophysiology. The reviewer explicitly characterises this as a likely TxGNN false positive.

Given the absence of MOA data, absence of an established original indication, and a rationale that itself disputes the biological plausibility of the link, this top-ranked candidate should not be interpreted as a credible repurposing signal at this stage. Of the ten candidates reviewed for tyrosine, the strongest biological rationale (though still preliminary, L4/S1) was actually seen for **postural orthostatic tachycardia syndrome** (rank 5), where tyrosine's role as a catecholamine precursor via tyrosine hydroxylase gives a mechanistically coherent — if directionally uncertain — hypothesis. This is noted here for context but falls outside the scope of the top-ranked candidate this report is structured around.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case Report | Neurosurgical Focus | Describes a clear cell sarcoma originating from the S1 nerve root, previously misdiagnosed as psammomatous melanotic schwannoma; discusses shared histogenesis with malignant melanoma. Not related to tyrosine pharmacology or cauda equina syndrome treatment. |

---

## UK Market Information

Tyrosine currently holds no UK marketing authorisation (`total_licenses: 0`, `market_status: Not marketed`). No product-level MHRA licence data is available in the Evidence Pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (cauda equina syndrome) is not supported by any clinical trial evidence and is backed by only one case report that is biologically unrelated to either the drug or the proposed indication; the evidence review itself identifies this as a probable false positive. Combined with the absence of MOA data, an unestablished original indication, and no current UK marketing authorisation, this candidate does not meet the threshold to advance beyond initial screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for tyrosine (currently High-severity data gap, DG002)
- SmPC/label warnings and contraindications data (currently Blocking data gap, DG001) before any safety pre-assessment (S1) can begin
- Establishment of tyrosine's original/approved indication history, if any, to support comparative mechanistic analysis
- If further repurposing exploration is warranted, prioritise reassessment of the postural orthostatic tachycardia syndrome signal (rank 5), which has a more coherent — though still unproven — mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

