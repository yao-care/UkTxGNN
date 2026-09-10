---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF), an established treatment for reducing the duration and severity of neutropenia and for mobilising peripheral blood stem cells. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but this direction is currently supported by only **1 indirectly related publication** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neutropenia / peripheral blood stem cell mobilisation (established use of G-CSF; no UK licence record is present in this evidence pack) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, filgrastim is a recombinant G-CSF that stimulates proliferation and differentiation of the granulocyte lineage and mobilises haematopoietic stem cells into peripheral blood — it does not act on the platelet dense/alpha-granule release pathway that defines "primary release disorder of platelets" (a platelet secretion/storage-pool type disorder).

The single supporting publication is a cohort study of peripheral blood stem cell mobilisation in healthy donors, which incidentally notes that G-CSF perturbs blood cell subsets (including platelets) as a known side effect — it is not a therapeutic study of any platelet-release disorder. The high TxGNN score most likely reflects embedding proximity between "hematopoietic/bone marrow"-related disease nodes in the knowledge graph, rather than a genuine pharmacological link.

Across all ten TxGNN-predicted indications for filgrastim in this evidence pack (all platelet- or coagulation-related disorders), the pipeline's own rationale consistently flags absent or contradictory mechanistic support, and where clinical trials do appear (e.g. Scott syndrome, platelet-type bleeding disorder), they are haematopoietic stem cell transplantation or oncology trials in which G-CSF is used incidentally as a mobilisation/supportive agent — not as a treatment for the predicted disease itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort | Frontiers in Immunology | Study of G-CSF-mediated peripheral blood stem cell mobilisation in healthy donors; notes preferential mobilisation of lymphocyte subsets. Does not investigate a platelet release disorder as a treatment target — relevance is indirect (G-CSF's known effect on blood cell subsets). |

---

## UK Market Information

No UK marketing authorisation is recorded for filgrastim in this evidence pack (market status: not marketed; 0 licences on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no completed clinical trial and only one indirectly relevant, non-therapeutic publication supporting use of filgrastim in primary release disorder of platelets. The proposed mechanistic link is weak — G-CSF acts on granulocyte production and stem cell mobilisation, not the platelet granule-release pathway implicated in this disease — and the pipeline's own analysis attributes the high TxGNN score to knowledge-graph embedding proximity rather than pharmacological plausibility.

**To proceed, the following is needed:**
- A verified UK/MHRA licence record and SmPC for filgrastim (this evidence pack has none)
- Confirmed mechanism of action data linking G-CSF to platelet granule release or storage-pool function
- Preclinical or case-level evidence specifically studying filgrastim in platelet release disorders, rather than incidental trial overlap from unrelated haematopoietic stem cell transplant/oncology studies
- Full safety/contraindication data (key warnings, contraindications, DDI), currently unavailable in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

