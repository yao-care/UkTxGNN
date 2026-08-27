---
layout: default
title: Felbinac
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Felbinac
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

Using the report template supplied in the system prompt (this is a direct authoring task against the given Evidence Pack — no codebase skill applies here, since the instructions for structure/rules are already fully specified inline).

A note before the report: the evidence pack's `original_indications` array is empty and `original_moa` is flagged `[Data Gap]`, so I have **not** filled those from memory (per the "no guessing, cite the source" rule). Where the pack's own `repurposing_rationale` text incidentally reveals pharmacological facts about felbinac (e.g. "non-selective COX-1/COX-2 inhibitor", "currently only approved for topical treatment of local musculoskeletal pain"), I've used that — it's data present in the pack, not recalled training knowledge. This is flagged explicitly below as an additional data gap alongside DG001/DG002.

---

# Felbinac: From Topical Musculoskeletal Pain Relief to Brachyolmia-Amelogenesis Imperfecta Syndrome

## One-Sentence Summary

Felbinac appears in this evidence pack as a topical NSAID (non-selective COX-1/COX-2 inhibitor) used for localised muscle and joint pain — this is inferred from the model's own mechanistic notes, as the structured original-indication and MOA fields were not populated. TxGNN's top-ranked prediction is **Brachyolmia-Amelogenesis Imperfecta Syndrome**, a rare inherited skeletal/dental syndrome, but this is currently supported by **0 clinical trials** and **0 publications**, and the pack's own rationale text flags the association as most likely a knowledge-graph artefact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (0 UK licences on file); narrative rationale text describes felbinac as a topical NSAID for musculoskeletal pain |
| Predicted New Indication | Brachyolmia-amelogenesis imperfecta syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The `original_moa` field for felbinac is a data gap in this pack (DG002). However, the mechanistic rationale text attached to several of the other candidate indications (ranks 6, 9, 10) consistently identifies felbinac as a **non-selective COX-1/COX-2 inhibitor** — i.e. a conventional topical NSAID that reduces local inflammation and pain by inhibiting prostaglandin synthesis. That same rationale text notes felbinac is "currently only approved for topical treatment of local musculoskeletal pain," which is the closest thing to an original-indication statement available in this pack.

Brachyolmia-amelogenesis imperfecta syndrome, by contrast, is a rare inherited syndrome combining short-trunk skeletal dysplasia with defective tooth enamel formation. Its pathology is developmental/structural (abnormal structural proteins or developmental gene function), not inflammatory. There is no shared disease biology between a topical anti-inflammatory analgesic and a congenital structural dysplasia syndrome.

Critically, the evidence pack's own repurposing rationale for this prediction states this explicitly: it attributes the very high TxGNN score (0.9999) to **similarity between skeletal-related node embeddings in the knowledge graph**, not to any real pharmacological or causal relationship. Combined with the complete absence of clinical trial or literature evidence (see below), this top-ranked prediction should be read as a **hypothesis-generating artefact of the model**, not a credible repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trial or literature evidence exists for felbinac in this indication, and the model's own mechanistic rationale explicitly flags the prediction as a likely knowledge-graph embedding artefact rather than a genuine pharmacological signal.
- Felbinac's UK licensing (0 marketing authorisations on file), safety labelling (DG001, Blocking), and mechanism of action (DG002, High) are all unresolved data gaps that would need to be closed before any further evaluation, regardless of indication.

**To proceed, the following is needed:**
- MHRA-approved product labelling (SmPC) — warnings, contraindications, DDI data (DG001, Blocking)
- Verified mechanism of action from DrugBank or equivalent primary source (DG002, High)
- Confirmation of felbinac's actual original licensed indication(s) and UK marketing status (currently absent from this pack)
- If repurposing is to be pursued at all for felbinac, the four lower-ranked candidates with at least a class-level NSAID rationale — spondyloarthropathy susceptibility (rank 6), rheumatoid nodulosis (rank 7), RF-positive polyarticular JIA (rank 9), and JIA (rank 10), all scored L4/"Research Question" — are mechanistically more plausible starting points than this top-ranked syndrome, though all still lack felbinac-specific trial or literature evidence and would require dedicated study before any decision beyond Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

