---
layout: default
title: Gamolenic Acid
parent: Model Prediction Only (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Gamolenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Gamolenic Acid: From No UK-Authorised Indication to Insomnia (Predicted)

## One-Sentence Summary

Gamolenic acid (gamma-linolenic acid, GLA, DrugBank DB13854) currently holds no marketing authorisation in the United Kingdom and no original indication or mechanism-of-action data is recorded in this evidence pack. The TxGNN model predicts a possible effect on **Insomnia**, but this is supported by only **1 clinical trial** (rated as unrelated to either the drug or the indication) and **0 publications**, indicating the signal is currently unvalidated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no UK licences on record and no original indication data captured (data gap) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gamolenic acid is not available in this evidence pack, and the drug has no recorded UK marketing authorisation or original indication, which limits any standard MOA-to-indication plausibility assessment.

The only clinical trial linked to this candidate — NCT07233148 (Healing ALS Registry Observational Study, HAROS) — is an observational registry for people with ALS, MND or PLS. It has no direct connection to gamolenic acid or to insomnia; the evidence pipeline itself rated its relevance as grade C ("不相關試驗" / not relevant), noting it was surfaced by the automated search without a genuine mechanistic or clinical link.

On balance, this appears to be a case of a high TxGNN confidence score unsupported by corroborating trial or literature evidence — a likely false-positive signal rather than a genuine biological hypothesis. Worth flagging separately: within the same evidence pack, the **rheumatoid arthritis** prediction (rank 4) is backed by substantially stronger evidence (evidence level L2, two completed trials directly testing GLA, and 20 supporting publications including RCTs), consistent with GLA's established role as a precursor of anti-inflammatory dihomo-gamma-linolenic acid (DGLA) and prostaglandin E1. That signal may merit independent evaluation outside the scope of this insomnia-focused report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07233148](https://clinicaltrials.gov/study/NCT07233148) | N/A | Recruiting | 1000 | Observational monthly registry for people with ALS, MND or PLS, tracking ALSFRS-R scores, symptoms, diet, supplements and therapies. Not designed to evaluate gamolenic acid or insomnia; flagged as unrelated (grade C) by the evidence pipeline. |

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Gamolenic acid is not currently marketed in the United Kingdom. No MHRA marketing authorisations are on record (0 licences).

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) were available in this evidence pack, and as gamolenic acid is unlicensed in the UK, no SmPC currently exists to consult. Any future safety assessment would need to draw on DrugBank monograph data, published literature, and international product information (e.g. evening primrose oil/borage oil-derived GLA products) before proceeding further. Should the drug be used or supplied in the UK, suspected adverse reactions should still be reported via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.93%), the only associated clinical trial is unrelated to both gamolenic acid and insomnia, there is no supporting literature, and no mechanism-of-action data exists to establish biological plausibility. This is evidence level L5 — a model prediction with no corroborating clinical or preclinical support.

**To proceed, the following is needed:**
- Mechanism-of-action data for gamolenic acid (DG002 — query DrugBank API)
- TFDA/MHRA label warnings and contraindications (DG001 — required before any S1 safety screening)
- Genuine preclinical or clinical evidence linking GLA to sleep-onset or sleep-maintenance pathways
- Consideration of the rheumatoid arthritis signal (rank 4, evidence level L2) as a separate, better-supported candidate for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

