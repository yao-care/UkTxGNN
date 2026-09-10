---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Dorzolamide
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor used to lower intraocular pressure in open-angle glaucoma and ocular hypertension. The TxGNN model predicts it may also be effective for **primary hereditary glaucoma**, with a prediction score of **99.99%**, but this specific indication currently has **no directly matching clinical trials or published literature** — the case rests entirely on mechanistic extrapolation from the drug's well-established use in open-angle glaucoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (topical carbonic anhydrase inhibitor) — no formal indication text available in this evidence pack |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (flagged internally as "Research Question") |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a data gap). Based on known pharmacology, Dorzolamide is a topical carbonic anhydrase II (CA-II) inhibitor applied to the ciliary body epithelium, where it reduces aqueous humour production and thereby lowers intraocular pressure — this is its well-established, long-standing mechanism in glaucoma management.

Primary hereditary glaucoma (largely early-onset open-angle or congenital genetic subtypes) shares the same underlying pathophysiology as typical open-angle glaucoma: impaired aqueous humour outflow leading to elevated intraocular pressure. On that basis, Dorzolamide's IOP-lowering mechanism is plausibly transferable.

However, this specific ontology term has **no direct trial or literature support** — the evidence is inferred indirectly through the large body of evidence for standard open-angle glaucoma (see ranks 6–7 in the underlying dataset, both graded L1/S3/Proceed with Guardrails), rather than any study conducted in a hereditary or congenital glaucoma population. Notably, safety and dosing in paediatric/infant populations — who make up a meaningful share of hereditary/congenital glaucoma cases — remain unvalidated for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Dorzolamide currently holds no marketing authorisation in the UK evidence pack on record (0 licences; market status: not marketed). No product-level licence details are available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (primary hereditary glaucoma) has no direct clinical trial or literature evidence — support is purely mechanistic, extrapolated from a related but pathologically distinct condition (typical open-angle glaucoma). This does not meet the threshold to proceed even under guardrails.

**To proceed, the following is needed:**
- TFDA/MHRA product labelling — warnings, precautions and contraindications (currently a blocking data gap; required before any safety pre-assessment)
- Confirmed mechanism of action data from DrugBank or equivalent source
- Dedicated clinical evidence in a hereditary/congenital glaucoma population, including paediatric safety data
- Confirmation of UK marketing authorisation status, given the current pack shows the drug as not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

