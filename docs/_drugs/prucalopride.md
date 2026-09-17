---
layout: default
title: Prucalopride
parent: Moderate Evidence (L3-L4)
nav_order: 490
evidence_level: L4
indication_count: 10
---

# Prucalopride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Prucalopride: From Gut-Motility Agent to Amyloidosis-Related Intestinal Dysmotility

## One-Sentence Summary

Prucalopride is described in this evidence pack as a highly selective 5-HT4 receptor agonist that promotes colonic motility; formal UK regulatory data on its original licensed indication is not available in this dataset. Of the ten TxGNN-predicted indications reviewed, the highest-scoring candidate (hypoalphalipoproteinemia, 99.8%) is flagged in its own rationale as a likely false-positive embedding artefact with no biological plausibility. The most credible signal instead points to **amyloidosis-related intestinal dysmotility**, supported by **0 clinical trials** and **2 publications**, corresponding to Evidence Level L4 (mechanism/diagnostic-context evidence only, not therapeutic evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no MHRA licence data available); pack text consistently describes Prucalopride as a colonic-motility-promoting 5-HT4 agonist |
| Predicted New Indication | Amyloidosis-related intestinal dysmotility (TxGNN term: "amyloidosis (disease)") |
| TxGNN Prediction Score | 99.62% (rank 4214) |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (framed by the source data as a "Research Question" — worth monitoring, not yet actionable) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Prucalopride is not formally recorded as a discrete field in this evidence pack (`original_moa` is a data gap). However, the rationale accompanying every predicted indication consistently describes Prucalopride as a **highly selective 5-HT4 receptor agonist** acting on intestinal smooth muscle and the enteric nervous system to **promote colonic peristalsis** — consistent with the known prokinetic drug class used for chronic gastrointestinal motility disorders.

Amyloid deposition can infiltrate the enteric nervous system and intestinal smooth muscle, producing secondary motility disorders such as chronic intestinal pseudo-obstruction (CIPO). A prokinetic 5-HT4 agonist is therefore mechanistically plausible for symptomatic management of this type of secondary dysmotility. The two supporting publications, however, address the **diagnostic** difficulty of recognising amyloidosis-related GI motility disorders (frequently misdiagnosed as functional GI disease) rather than any **therapeutic** use of prucalopride — so this remains a mechanistic hypothesis, not a validated treatment signal. The same rationale applies, with slightly weaker support, to primary (AL) amyloidosis (rank 9), which is a subtype of the same disease process.

By contrast, the single highest TxGNN-scoring prediction in this pack, hypoalphalipoproteinemia (99.8%), is explicitly assessed in the source rationale as having **no known mechanistic link** to 5-HT4 agonism or lipoprotein/HDL metabolism, and is most likely a false-positive artefact of the knowledge-graph embedding space. The remaining candidates (homozygous familial hypercholesterolaemia, duodenal ulcer, oral candidiasis, obsolete familial combined hyperlipidaemia, strongyloidiasis, HIV infection, acquired amyloid peripheral neuropathy) similarly lack mechanistic plausibility or any supporting literature/trial evidence, and are all scored L5/Hold.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Hypoalphalipoproteinemia | 99.82% | L5 | Hold (likely noise) |
| 2 | Homozygous familial hypercholesterolemia | 99.67% | L5 | Hold |
| 3 | Duodenal ulcer | 99.65% | L5 | Hold |
| 4 | Oral candidiasis | 99.64% | L5 | Hold |
| 5 | Obsolete familial combined hyperlipidemia | 99.62% | L5 | Hold |
| **6** | **Amyloidosis (disease)** | **99.62%** | **L4** | **Research Question** |
| 7 | Strongyloidiasis | 99.60% | L5 | Hold |
| 8 | HIV infectious disease | 99.60% | L5 | Hold |
| 9 | Primary amyloidosis | 99.56% | L4 | Research Question |
| 10 | Acquired amyloid peripheral neuropathy | 99.55% | L5 | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Review | Turkish Journal of Gastroenterology | Specific GI motility disorders (gastroparesis, chronic intestinal pseudo-obstruction, colonic inertia) are commonly under-recognised and misdiagnosed as functional GI disease by community physicians in Asia — diagnostic-context evidence only, no treatment data on prucalopride |
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case Report | Cureus | Case of amyloidosis presenting as chronic intestinal pseudo-obstruction in a 61-year-old man, diagnosed after multiple negative work-ups and laparotomies — illustrates the disease mechanism but does not evaluate prucalopride therapy |

---

## UK Market Information

Prucalopride is recorded as **not marketed** in the UK within this evidence pack, with **0 marketing authorisations** on file. No product name, formulation, or approved indication text is available to report at this time (MHRA SmPC verification is listed as a blocking data gap — see Conclusion).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the ten TxGNN-predicted indications reach clinical evidence levels (L1–L3). The highest-scoring prediction (hypoalphalipoproteinemia) is assessed by the underlying rationale itself as a likely false-positive signal with no biological plausibility. The only mechanistically coherent candidate — amyloidosis-related intestinal dysmotility — is supported solely by diagnostic-context literature (a review and a case report), with no clinical trials and no direct evidence of prucalopride's therapeutic effect in this population.

**To proceed, the following is needed:**
- MHRA SmPC warnings, precautions and contraindications (blocking data gap, DG001)
- Formal DrugBank-sourced mechanism-of-action record (DG002)
- Targeted literature/trial search specifically for prucalopride use in amyloidosis-associated CIPO or gastroparesis
- Confirmation of UK marketing/licensing status, given the "not marketed" flag in this pack
- Re-assessment of the eight L5/Hold candidates only if new knowledge-graph signal, mechanistic rationale, or literature emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

