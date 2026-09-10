---
layout: default
title: Cyclizine
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Cyclizine
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

# Cyclizine: From Antiemetic/Antihistamine Use to Allergic Urticaria

## One-Sentence Summary

Cyclizine is a first-generation piperazine-class H1-antihistamine, classically associated with antiemetic and anti-vertigo use (its formal original-indication record is not available in this evidence pack). The TxGNN model predicts it may be effective for **Allergic Urticaria**, but this direction is currently supported by only **0 clinical trials** and **1 publication**, and that single publication does not directly study cyclizine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no UK marketing authorisation licences recorded for this drug; classically developed as an H1-antihistamine antiemetic (nausea, vomiting, vertigo/motion sickness) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known information, Cyclizine belongs to the piperazine class of first-generation H1-receptor antagonists, a pharmacological group whose efficacy in antiemetic/antihistamine use is well established, and which may mechanistically extend to allergic conditions.

Allergic urticaria is a classical H1-mediated hypersensitivity reaction, and antihistamines are the standard pharmacological class used for such conditions, so a class-level mechanistic link to cyclizine is biologically plausible. However, the one literature record retrieved for this pairing (PMID 8573923) is a mechanistic study of *solar* urticaria action spectra and does not evaluate cyclizine treatment or efficacy directly — it supports disease-mechanism context rather than drug-specific evidence.

Given the absence of any clinical trial or drug-specific efficacy literature, this prediction should currently be treated as a class-level pharmacological hypothesis rather than an evidence-backed repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8573923](https://pubmed.ncbi.nlm.nih.gov/8573923/) | 1995 | Mechanistic/physiological study (non-interventional) | Dermatology (Basel, Switzerland) | Characterises action/inhibition/augmentation spectra in solar urticaria; does not evaluate cyclizine treatment directly, provides disease-mechanism context only |

---

## UK Market Information

No UK marketing authorisations are currently on record for this drug (market status: Not marketed; total licences: 0).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: TFDA/MHRA-equivalent warnings and contraindications data are recorded as a Blocking data gap — DG001 — and drug interaction search returned no results, so no drug-specific safety details can be listed here.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on class-level pharmacological plausibility (H1-antagonism) rather than drug-specific evidence — evidence level is L4 with zero clinical trials and only one indirectly relevant, non-interventional publication. In addition, a Blocking-severity data gap (DG001: missing warnings/contraindications) currently prevents this candidate from entering the S1 safety pre-assessment stage at all.

**To proceed, the following is needed:**
- Resolve DG001: obtain SmPC/label warnings and contraindications (source: TFDA/MHRA equivalent) to unblock S1 safety pre-assessment
- Resolve DG002: obtain confirmed mechanism of action data from DrugBank
- Identify drug-specific evidence (case series, observational data, or trials) evaluating cyclizine — not just antihistamines as a class — in urticaria
- Optionally evaluate the secondary candidate "headache disorder" (rank 6, also L4/S1), which has more literature (5 papers) tied to the historical ergotamine–caffeine–cyclizine combination product (Migril), though this too lacks cyclizine-specific efficacy trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

