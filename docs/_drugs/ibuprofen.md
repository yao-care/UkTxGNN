---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From Established NSAID Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID); no UK regulatory record of its licensed indication was returned in this evidence pack. The TxGNN model predicts a possible link to **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare skeletal dysplasia, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no UK licence records were returned in this evidence pack |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this ibuprofen record is not available (DrugBank MOA field returned a data gap). The evidence pack's own mechanistic annotation does note that ibuprofen's established pharmacology is COX-1/COX-2 inhibition, underpinning its analgesic and anti-inflammatory effects.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare, genetically determined skeletal dysplasia associated with disrupted BMP/GDF5 signalling. There is no established biological pathway connecting COX enzyme inhibition to this developmental bone disorder.

The rationale text accompanying this prediction explicitly states that the high TxGNN score likely reflects embedding clustering among skeletal-disease nodes in the knowledge graph, rather than a genuine pharmacological signal, and characterises it as a high-risk false positive. All six other top-ranked candidates for this drug (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) follow the same pattern: rare skeletal/developmental syndromes with no plausible mechanistic link, no clinical trials, and no literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations were found for this drug in the evidence pack (total_licenses = 0). Ibuprofen is widely available as a generic OTC and prescription NSAID in the UK market generally, but no product-specific licence data was returned in this dataset — please verify current authorisation status via the MHRA product database or BNF before any further action.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: The evidence pack flags TFDA-equivalent warnings/contraindications as a blocking data gap — this must be resolved before any safety-stage (S1) review can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (Evidence Level L5), and the prediction pipeline's own mechanistic analysis identifies it as a probable knowledge-graph artefact rather than a genuine pharmacological signal. All seven top-ranked predicted indications for this drug share the same pattern — rare skeletal/developmental syndromes with no biological plausibility relative to ibuprofen's COX-inhibitory mechanism.

**To proceed, the following is needed:**
- Confirmed original indication and marketing authorisation status (currently absent from this evidence pack)
- Verified mechanism of action data from DrugBank or an equivalent pharmacology reference
- Resolution of the blocking safety data gap (warnings/contraindications) before any S1 safety review
- Independent biological plausibility assessment (preclinical or mechanistic literature) before this candidate is reconsidered beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

