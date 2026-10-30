---
layout: default
title: Buserelin
parent: Model Prediction Only (L5)
nav_order: 118
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Buserelin: predicted new indication hypertrichosis (evidence level L4). Approved use: Prostate cancer"
monitor_inn: "Buserelin"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Buserelin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Buserelin: From Prostate Cancer to hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Buserelin is a GnRH (gonadotropin-releasing hormone) agonist used to treat prostate cancer.
The TxGNN model predicts it may be effective for **hypertrichosis**,
but there are currently **no clinical trials** and only **1 publication** (a case report on a different topic), so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (based on pharmacology data; the UK licence record contains no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, buserelin is a GnRH receptor agonist. It desensitises the pituitary GnRH receptor, which lowers sex steroid levels. This is why it is used in hormone-sensitive prostate cancer.

In theory, suppressing androgens could reduce androgen-driven hair growth. However, hypertrichosis is by definition excess hair growth that is *not* androgen-dependent, so this rationale is weak. The only publication found describes Cantu syndrome (a condition featuring hypertrichosis) with hypopituitarism and concerns endocrine monitoring, not treatment with buserelin.

The link is therefore indirect. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a therapeutic effect.

**Other predicted indications (all with no trial or literature support, evidence level L5, Hold):**

| Rank | Predicted Indication | TxGNN Score | Comment |
|---|---|---|---|
| 2 | Ambras type hypertrichosis universalis congenita | 0.9969 | Genetic follicular defect (e.g. TRPS1 regulatory rearrangements); no mechanistic connection to GnRH agonism |
| 3 | Malformation syndrome with odontal and/or periodontal component | 0.9966 | Developmental structural anomalies; no plausible mechanism |
| 4 | Syndrome with a Dandy-Walker malformation as major feature | 0.9964 | Congenital brain anomaly that a drug cannot reverse; purely computational prediction |
| 5 | Isolated genetic hair shaft abnormality | 0.9962 | Structural keratin/hair shaft defects not addressed by sex steroid suppression |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Case report / Review | Endocrinology, Diabetes & Metabolism Case Reports | Case of Cantu syndrome (hypertrichotic osteochondrodysplasia) with multiple pituitary hormone deficiencies, identified after slowed growth at 13 years. Supports endocrine monitoring in this condition. It does not evaluate buserelin. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803042B0AAABAB (BNF-style product code) | Buserelin nasal spray 100 micrograms (84 doses), 10 g | Nasal spray | Not stated in the licence record |

## Cytotoxicity

Buserelin is a hormonal (GnRH agonist) therapy rather than a conventional cytotoxic agent, so no cytotoxicity-specific handling profile is presented here.

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacology entry showing that buserelin acts on the human GnRH₁ receptor (GNRHR). No drug-drug interactions were identified.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and the single publication does not test buserelin. The proposed mechanism is weak because hypertrichosis is not androgen-driven, and the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The other four predictions are also unsupported.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic analysis
- Warnings and contraindications from the SmPC/BNF, together with the approved indication text for the UK authorisation
- Evidence of any biological connection between GnRH receptor signalling and non-androgen-dependent hair growth, such as preclinical or case-level data
- Assessment of route compatibility (the nasal spray versus any route a hypertrichosis treatment would need)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

