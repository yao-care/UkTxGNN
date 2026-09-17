---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 202
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a RANKL-targeting monoclonal antibody used to treat osteoporosis, and this evidence pack currently shows no active UK marketing authorisation on file for it. The TxGNN model predicts a possible new role in **Severe Nonproliferative Diabetic Retinopathy**, with a prediction score of **99.63%**, but this specific prediction is currently supported by **zero clinical trials** and **zero publications** — it is a pure model inference extrapolated from a related, weaker-evidenced prediction (general diabetic retinopathy).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (identified from literature evidence; no formal UK licence text is present in this pack) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this pack (`original_moa: [Data Gap]`), but the underlying evidence entries do give a partial mechanistic picture: Denosumab is a monoclonal antibody against RANKL, blocking the RANK/RANKL/OPG axis that is central to osteoclast-mediated bone turnover — its established basis of use in osteoporosis.

The pack's own repurposing rationale extends this mechanism to the eye: the OPG/RANKL system is also expressed in retinal vascular endothelium and pericytes, and RANKL signalling has been implicated in the angiogenesis and pericyte apoptosis seen in diabetic retinopathy. The severe nonproliferative subtype prediction is explicitly derived from this same logic applied to a related, less advanced disease stage (plain "diabetic retinopathy", TxGNN score 99.23%, rank 6788), which itself carries only indirect, low-grade supporting evidence (one Grade-C-relevance safety trial and two cohort-level publications — see Related Evidence below).

For severe nonproliferative diabetic retinopathy specifically, no trial or literature evidence exists in this pack at all. The mechanistic link is therefore a second-order extrapolation — plausible on biological grounds, but currently untested in this specific patient population or disease stage.

**Related evidence (for context only, not for this specific subtype):** The broader "diabetic retinopathy" prediction is supported by NCT00925600 (a Phase 3 ocular-safety substudy of Denosumab in prostate cancer patients — Grade C relevance, not a retinopathy efficacy trial) and two cohort/registry publications (PMID 38899553, PMID 36960265) on diabetes-related outcomes with Denosumab. None of this evidence directly addresses severe nonproliferative disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Denosumab currently has no UK marketing authorisation on record in this evidence pack (market status: **Not marketed**, 0 licences held). No product, dosage form, or licensed indication text is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a Level 5 (model-prediction-only) candidate with no clinical trial or literature evidence specific to severe nonproliferative diabetic retinopathy, and the drug has no current UK marketing authorisation to build on. There is nothing here yet to justify advancing beyond the prediction stage.

**To proceed, the following is needed:**
- SmPC warnings, precautions and contraindications from MHRA (flagged as a blocking data gap in this pack)
- A confirmed mechanism-of-action record from DrugBank (flagged as a high-priority data gap)
- Disease-stage-specific clinical or preclinical evidence for severe nonproliferative diabetic retinopathy, rather than relying solely on the general diabetic retinopathy extrapolation
- Confirmation of UK licensing status/route of administration, since the drug is currently unlicensed here
- If evidence accrues, re-evaluation of the related "diabetic retinopathy" (rank 2) candidate in parallel, as it currently carries marginally stronger (though still low-grade) supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

