---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Naproxen: From NSAID Therapy to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a well-established non-steroidal anti-inflammatory drug (NSAID); however, this evidence pack contains no data on its originally licensed indication in this jurisdiction. The TxGNN model predicts a possible association with **Brachydactyly-Syndactyly Syndrome**, a rare congenital skeletal disorder, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the drug's own mechanistic rationale explicitly flags the biological link as implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on general pharmacological knowledge, Naproxen belongs to the propionic acid derivative class of NSAIDs, acting via non-selective inhibition of COX-1/COX-2 to reduce prostaglandin synthesis, and is conventionally used for pain and inflammation-related conditions.

The predicted new indication, brachydactyly-syndactyly syndrome, is a rare congenital skeletal malformation typically linked to genetic disruption of bone morphogenetic protein signalling (e.g. GDF5/CDMP1 pathways) during embryonic development — a structural/developmental disorder, not an inflammatory or pain-mediated condition. The evidence pack's own rationale states there is no known mechanistic link between NSAID-mediated COX inhibition and this congenital pathology.

Notably, ranks 2–4 in this evidence pack show the same pattern: all four top predictions are rare congenital skeletal/developmental syndromes (colobomatous microphthalmia-rhizomelic dysplasia, acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome), each with a documented rationale stating weak or absent biological plausibility. This clustering suggests the prediction may reflect embedding-space similarity among rare skeletal disorders in the knowledge graph rather than a genuine pharmacological signal, and should be treated as a hypothesis-generating output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

No marketing authorisations are recorded for this candidate in the current evidence pack (market status: Not Marketed, 0 licenses on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: TFDA/SmPC warnings and contraindications data are flagged as a Blocking data gap (DG001) in this evidence pack and must be resolved before any safety initial assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has Evidence Level L5 (model prediction only, no supporting clinical trials or literature), and the mechanistic rationale itself concludes there is no known biological basis linking NSAID activity to this congenital skeletal syndrome. Combined with a Blocking data gap on safety warnings/contraindications, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/SmPC product warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data (High priority gap, DG002)
- Independent biological plausibility assessment for BMP/GDF5-pathway disorders
- Any preclinical or case-level evidence supporting a link between NSAIDs and congenital skeletal dysplasias, before further investment in this direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

