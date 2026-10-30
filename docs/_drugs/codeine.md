---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 3
monitor_inn: "codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
last_modified_at: 2026-10-30
description: "Codeine: predicted new indication nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Codeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Codeine: Opioid analgesic → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid analgesic and antitussive that is currently marketed in the UK as a combination tablet with ibuprofen.
The TxGNN model predicts it may be relevant to **nasal cavity disease**, but there are **no registered clinical trials** and only **1 publication** (a case report describing harm rather than benefit).
Evidence is limited to the model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Codeine is a well-known opioid with antitussive and mild analgesic effects, and it is commonly used for symptom relief in upper respiratory conditions.

The high model score likely reflects shared links to nasal and upper airway conditions in the data used to train the model. However, there is no plausible mechanism by which codeine would treat structural or inflammatory disease of the nasal cavity. The only publication retrieved describes a nasal stone (rhinolith) formed around a hardened mixture of codeine and opium that had been lodged in the nose. That is a complication linked to the drug, not a therapeutic benefit. The prediction should therefore be treated as a statistical signal rather than a credible treatment hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a unilateral rhinolith formed around an impacted foreign body, which proved to be a hardened mixture of codeine and opium. It was removed under local anaesthesia. No therapeutic effect was reported. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010J0DGAAAY | Solpadeine Mig Ibuprofen/Codeine_Tab | Not recorded | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 449 interactions were identified in the data compiled for this report. Major-level interactions include **alvimopan** and **bupropion**. Moderate-level interactions include atropine, cimetidine, dexamethasone, glycopyrronium, granisetron, hyoscyamine, loperamide, dicyclomine, dronabinol and fenfluramine.

For full warnings, contraindications and dosing, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score alone. The single publication describes a complication from foreign-body opioid material in the nose, not a treatment effect, and there are no trials. No credible mechanism supports codeine for nasal cavity disease.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale for nasal cavity disease
- Any clinical or preclinical study that directly tests codeine in nasal cavity disease
- Label-based warnings and contraindications from the SmPC and BNF
- A defined target condition within nasal cavity disease, so that benefit can be weighed against opioid risks (dependence, respiratory depression)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

