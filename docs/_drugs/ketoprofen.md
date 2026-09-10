---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a long-established NSAID (propionic acid derivative) used for pain and inflammation associated with musculoskeletal conditions such as rheumatoid arthritis and osteoarthritis. The TxGNN model predicts it may be relevant to **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal dysplasia, but this prediction is currently supported by **no clinical trials and no published literature**, and the model's own rationale flags it as likely a knowledge-graph proximity artefact rather than a genuine mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain and inflammation (general NSAID class use — e.g. rheumatoid arthritis, osteoarthritis); no UK-specific marketing authorisation on file in this evidence pack |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, ketoprofen is a propionic acid derivative NSAID that inhibits COX-1/COX-2 to reduce prostaglandin synthesis, providing analgesic and anti-inflammatory effects. Its established efficacy is in inflammatory and painful musculoskeletal conditions.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal disorder caused by GDF5 gene mutations, resulting in structural limb malformation. This is a developmental/structural condition rather than an inflammatory or pain-mediated pathology, so there is no obvious biological rationale connecting it to ketoprofen's COX-inhibition mechanism.

The evidence pack's own repurposing rationale is explicit on this point: it assesses the high TxGNN score as potentially arising from proximity bias in the knowledge graph (e.g. shared "skeletal/joint" nodes) rather than a true mechanistic connection. This prediction should therefore be treated with considerable caution and is not, on current evidence, a credible repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No UK marketing authorisation is currently on record for ketoprofen in this evidence pack (market status: **Not marketed**, 0 licences held). No product-specific information (brand, dosage form, licensed indication) is available to tabulate.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is evidence level L5 — a model output with no supporting clinical trials or literature, and the mechanistic rationale itself suggests the score may reflect knowledge-graph bias rather than a genuine biological link. There is also a blocking data gap on UK/MHRA safety labelling (warnings, contraindications), meaning this candidate cannot yet pass an initial safety screen regardless of efficacy considerations.

**To proceed, the following is needed:**
- MHRA/SmPC warnings and contraindications data (currently a blocking gap)
- Confirmed mechanism of action data from DrugBank or equivalent source
- Any preclinical or case-level evidence specifically linking ketoprofen to skeletal dysplasia pathophysiology, to justify moving beyond model-only prediction

**Note:** Two other candidates in this evidence pack (not the top-ranked prediction) carry a more plausible mechanistic basis and may warrant separate follow-up as research questions rather than this rank-1 candidate: *spondyloarthropathy, susceptibility to* (L3, literature-supported, NSAIDs are a recognised class-level symptomatic treatment) and *juvenile arthritis due to defect in LACC1* (L4, inflammatory joint disease with class-level NSAID plausibility). Neither has ketoprofen-specific trial or literature confirmation, but both are mechanistically more coherent than the rank-1 result reported above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

