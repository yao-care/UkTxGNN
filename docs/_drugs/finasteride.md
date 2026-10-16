---
layout: default
title: Finasteride
parent: Moderate Evidence (L3-L4)
nav_order: 289
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-15
description: "Finasteride: predicted new indication Hypertrichosis (evidence level L4). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Finasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Finasteride: From Benign Prostatic Hyperplasia to Hypertrichosis

## One-Sentence Summary

Finasteride is a 5-alpha reductase inhibitor originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **no registered clinical trials** and only **4 indirect publications** (reviews and a technique paper) supporting this direction.
The evidence is weak, and the mechanistic fit is questionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (per the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Hypertrichosis (rank 2 of 6 predictions; see note below) |
| TxGNN Prediction Score | 99.99% (rank 281 overall) |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

**Note on selection of the indication:** The top-ranked prediction was Ambras type hypertrichosis universalis congenita (score 99.99%, rank 239). It has no trials or literature (L5) and no plausible mechanistic rationale, as it is a congenital condition linked to TRPS1 regulation rather than androgen-driven disease. Hypertrichosis (rank 2) is the highest-ranked prediction with any supporting literature, so it is the focus of this report. All six predictions are summarised at the end of the report.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Finasteride is generally known as a 5-alpha reductase type II (and III) inhibitor. It blocks conversion of testosterone to dihydrotestosterone (DHT). This is the basis of its use in BPH and, more widely, in male pattern hair loss.

The link to hypertrichosis is **weak**. DHT lowering is plausibly relevant to androgen-dependent hair growth, such as hirsutism. Hypertrichosis is, by definition, excess hair growth in non-androgen-dependent areas. It is usually iatrogenic (for example minoxidil, ciclosporin, diazoxide), metabolic or paraneoplastic. A DHT-lowering drug would not be expected to address these causes. Hirsutism evidence should not be extrapolated to hypertrichosis without caution.

The high TxGNN score reflects a graph-based computational prediction only. It is not evidence of clinical efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | Hirsutism and hypertrichosis in adults. Hypertrichosis affects non-androgen-dependent areas and does not need hormone monitoring, unlike hirsutism. Causes are mostly iatrogenic, metabolic, nutritional or paraneoplastic |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Ther Umsch | Review of treatments for androgenetic alopecia and hirsutism; emotional impact of hair disorders highlighted |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Hautarzt | Finasteride is noted for male pattern hair loss; laser-assisted hair removal is noted for hypertrichosis and hirsutism |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods/Instrument | Hautarzt | TrichoScan, a digital tool for hair analysis; not a treatment study |

Based on titles and abstracts, none of these publications appears to report finasteride efficacy in hypertrichosis. They give only indirect context. The full texts would need to be checked. The publications are in German or French.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0604020C0AAAAAA | Finasteride tablets 5 mg | Tablet (inferred from product name) | Not available in the data compiled |

Note that the identifier shown (0604020C0AAAAAA) looks like a BNF-style classification code rather than an MHRA product licence (PL) number. The licence record should be verified against the MHRA register. The BNF chapter 6 (endocrine) and chapter 7 (genito-urinary) classifications should be consulted for the formal positioning of 5-alpha reductase inhibitors.

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** Liver disease and gallbladder disease are flagged in the TxGNN knowledge graph. These should be confirmed against the SmPC.
- **Pregnancy:** Finasteride is contraindicated in pregnancy because of the risk of abnormal external genitalia in male fetuses. Women who are or may be pregnant should not handle crushed or broken tablets.
- **Drug Interactions:** The interaction screen returned 100 potential interactions, but all listed have an "Unknown" severity level. Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, omeprazole, metformin, morphine and glimepiride. The severity and clinical significance of these need to be verified in the BNF interactions appendix.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the prediction rests on the model alone. There are no clinical trials, and the retrieved literature does not report finasteride use in hypertrichosis. Hypertrichosis is not androgen-driven, so the mechanistic basis is weak.

**Summary of all predictions:**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 1 | Ambras type hypertrichosis universalis congenita | 99.99% | L5 | No data; congenital, not DHT-driven |
| 2 | Hypertrichosis | 99.99% | L4 | Indirect literature only; weak mechanism |
| 3 | Malformation syndrome with odontal/periodontal component | 99.99% | L5 | No mechanistic link identified |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 99.99% | L5 | No rationale; pregnancy contraindication |
| 5 | Isolated genetic hair shaft abnormality | 99.99% | L5 | Structural, not DHT-mediated |
| 6 | Familial isolated trichomegaly | 99.15% | L5 | Loose conceptual link; unsupported |

**To proceed, the following is needed:**
- Full-text review of the retrieved publications, and a wider literature search for finasteride in hypertrichosis and hirsutism
- Mechanism of action data from DrugBank to support mechanistic analysis
- SmPC warnings and contraindications (the data compiled for this report is missing these), which blocks safety screening
- Verification of the MHRA licence record, dosage form and approved indication
- Severity grading for the listed drug interactions
- A clear biological rationale for androgen-independent hair overgrowth before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

