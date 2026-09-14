---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenylalanine: From Dietary Amino Acid to Predicted Use in Sclerosing Cholangitis

## One-Sentence Summary

> Phenylalanine is an essential amino acid with no authorised UK marketing licence and no established therapeutic indication.
> The TxGNN model predicts a possible link to **Sclerosing Cholangitis** (score 99.43%), but this is a model-level prediction only —
> there are **no supporting clinical trials**, and the limited literature is largely unrelated or, in one case, points to the **opposite (pathogenic) direction**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — phenylalanine is an essential dietary amino acid with no recorded therapeutic indication |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for phenylalanine as a therapeutic agent is not available. As an essential dietary amino acid, its known biological role is as a protein building block and metabolic precursor to tyrosine and the catecholamines — it is not currently used as a treatment for any disease, and holds no UK marketing authorisation.

The predicted association with sclerosing cholangitis does not appear to be backed by a coherent mechanistic story. Of the four literature items retrieved, only one meaningfully engages with a related hepatobiliary condition — a cohort study on plasma **tyrosine** (not phenylalanine itself) and fatigue in primary biliary cirrhosis/primary sclerosing cholangitis. More importantly, one preclinical study (PMID 8000512) found that **FMLP, a synthetic peptide containing phenylalanine, actually induces small duct cholangitis in rats** — a *pathogenic*, not therapeutic, direction. This finding should be treated as a caution flag rather than supportive evidence, and it directly undermines rather than supports the repurposing hypothesis.

Given this pattern, the internal evidence review correctly classifies this candidate as **Evidence Level L5** (model prediction only, no genuine supporting studies) with a **Hold** recommendation. A second predicted indication (congenital prothrombin deficiency, score 99.26%) is even weaker: its only associated trial concerns Nitisinone — a different drug with an opposing mechanism — and the trial itself was withdrawn with zero enrolment. Neither candidate currently offers a credible mechanistic or clinical basis for repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined plasma tyrosine (not phenylalanine) and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis patients |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort/Metabolomics | Journal of Clinical and Experimental Hepatology | Serum metabolomic profiling in cholangiocarcinoma vs benign hepatobiliary disease; not specific to phenylalanine or a treatment context |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal study | Journal of Gastroenterology | **Caution flag**: FMLP (a phenylalanine-containing peptide) induced small duct cholangitis in rats — a pathogenic, not therapeutic, effect |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Methodology | Journal of Gastroenterology and Hepatology | Radioimmunoassay methodology paper on enterohepatic circulation of bacterial chemotactic peptides; no treatment relevance |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: label warnings, contraindications and DDI data for this candidate are currently a Blocking data gap — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials supporting this indication, and the literature evidence is either unrelated or — in one animal study — indicates the opposite (pathogenic) mechanistic direction. Combined with the absence of a UK marketing authorisation and a Blocking data gap on product label warnings/contraindications, this candidate does not currently meet the threshold to advance past initial screening (S0).

**To proceed, the following is needed:**
- TFDA/MHRA product label warnings and contraindications (Blocking gap — required before any safety pre-screen)
- DrugBank-sourced mechanism of action data for phenylalanine
- Independent assessment of PMID 8000512 to confirm whether it represents a genuine contraindication signal
- Completion of pending `similarity_to_original` and route-compatibility assessments
- Re-evaluation should stronger mechanistic or clinical evidence emerge; the second candidate (congenital prothrombin deficiency) can be deprioritised, as its sole associated trial concerns a mismatched drug (Nitisinone) that was withdrawn with zero enrolment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

