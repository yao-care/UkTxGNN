---
layout: default
title: Dapoxetine
parent: Model Prediction Only (L5)
nav_order: 205
evidence_level: L5
indication_count: 3
monitor_inn: "Dapoxetine"
predicted_indications: ["migraine disorder", "dysthymic disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-30
description: "Dapoxetine: predicted new indication migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Dapoxetine
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

## Dapoxetine: Selective serotonin reuptake inhibitor (SSRI) → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Dapoxetine is a short-acting selective serotonin reuptake inhibitor (SSRI) marketed in the UK.
The TxGNN model predicts it may be useful for **migraine disorder**, but there are currently **no registered clinical trials** and **no publications that directly study dapoxetine in migraine**, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for dapoxetine is not available in the data compiled for this report. Pharmacology data identify its target as the serotonin transporter (SERT, gene SLC6A4), and it is described as a short-acting SSRI.

Serotonergic dysregulation is implicated in migraine, and some SSRIs have been explored for migraine prophylaxis. This gives a plausible but indirect rationale. The link rests on class-level inference rather than dapoxetine-specific data.

There are also reasons for caution. Dapoxetine is designed for rapid onset and a short half-life, suited to on-demand use. This fits poorly with chronic migraine prophylaxis, which generally requires sustained exposure. The high TxGNN score (0.9934) is a computational output only and is not evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The two publications retrieved do not directly study dapoxetine in migraine, so they do not support the prediction on their own.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Review | Current Neuropharmacology | Broad review of off-label uses of SSRIs as a class; not specific to dapoxetine |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Cohort | Urologia | Treatment compliance with dapoxetine in men with premature ejaculation; not related to migraine |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704050ABAAAAAA | Dapoxetine HCl Tablets 30 mg | Tablet | Not recorded in the local data |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model. No clinical trials or directly relevant publications address dapoxetine in migraine, and its on-demand pharmacokinetic profile is a poor fit for migraine prophylaxis. Evidence is therefore at level L5.

**To proceed, the following is needed:**
- Dapoxetine-specific mechanistic and pharmacokinetic data relevant to migraine
- Preclinical or clinical studies that directly examine dapoxetine in migraine
- Safety data from the SmPC and BNF, including contraindications and interactions, to support any risk assessment
- Comparison against established migraine prophylaxis options, including other SSRIs and standard-of-care agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

