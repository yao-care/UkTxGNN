---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Digoxin: From Heart Failure & Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside historically used to treat heart failure and atrial fibrillation/flutter. The TxGNN model predicts it may also be effective for **Prinzmetal angina** (variant angina), though this direction is currently supported only by **2 background publications** and **no registered clinical trials**. The drug is not currently authorised for sale in the UK.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure and atrial fibrillation/flutter (rate control) — established clinical use; not captured in the evidence pack's licence data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, digoxin belongs to the cardiac glycoside class (Na⁺/K⁺-ATPase inhibitors), and its efficacy in heart failure and atrial fibrillation has long been established through clinical use.

Prinzmetal (variant) angina is caused by transient coronary artery vasospasm rather than fixed atherosclerotic obstruction, and its management centres on vasodilators and autonomic/vascular tone modulation. Digoxin's known effects on cardiac autonomic tone and myocardial excitability offer a plausible, though unconfirmed, mechanistic rationale for the TxGNN link — but no digoxin-specific mechanistic or pharmacodynamic study for this indication currently exists in the evidence pack.

The two retrieved publications discuss circadian chronopharmacology of antihypertensive/anti-anginal therapy and the pathophysiology of angina decubitus, but neither directly investigates digoxin as a treatment for Prinzmetal angina. This means the prediction should be regarded as hypothesis-generating rather than evidence-supported at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta physiologica et pharmacologica Bulgarica | Discusses circadian rhythms and chronopharmacology relevant to antihypertensive/anti-anginal treatment timing; does not study digoxin directly |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Observational | Chinese medical sciences journal | Hemodynamic monitoring in 30 patients with angina decubitus, re-evaluating underlying mechanism and treatment approach; no digoxin-specific data |

## UK Market Information

Digoxin currently holds **no marketing authorisation in the UK** according to the evidence pack (market status: not marketed; 0 licences on record). No MHRA product or SmPC data is available for review.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags TFDA-equivalent warnings/contraindications as a **Blocking** data gap — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, no digoxin-specific mechanistic literature, no UK marketing authorisation, and no safety/warning data available for this drug–indication pairing. The prediction rests solely on the TxGNN model score with indirect background literature, which is insufficient to support progression.

**To proceed, the following is needed:**
- Regulatory label warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data (currently a High-severity data gap)
- Preclinical or mechanistic studies directly linking digoxin to coronary vasospasm/Prinzmetal angina
- Any clinical trial or case-series evidence specific to this drug–indication pair
- Confirmation of UK regulatory pathway, given the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

