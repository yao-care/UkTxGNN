---
layout: default
title: Dapoxetine
parent: Moderate Evidence (L3-L4)
nav_order: 205
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Dapoxetine: predicted new indication Migraine disorder (evidence level L4). Approved use: Premature ejaculation"
monitor_inn: "Dapoxetine"
predicted_indications: ["migraine disorder", "dysthymic disorder", "migraine with brainstem aura"]
---

# Dapoxetine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Dapoxetine: From Premature Ejaculation to Migraine Disorder

## One-Sentence Summary

Dapoxetine is a short-acting selective serotonin reuptake inhibitor (SSRI), originally used to treat premature ejaculation.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **no registered clinical trials** and only **2 publications**, neither of which directly tests dapoxetine in migraine. The prediction is therefore supported by model output and class-level reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Premature ejaculation (the UK licence record contains no indication text; this is taken from the knowledge graph) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

Two other predictions were also generated: dysthymic disorder (99.14%, L5) and migraine with brainstem aura (99.11%, L5). Neither has any trials or literature, and both are rated Hold.

---

## Why is This Prediction Reasonable?

Dapoxetine is a short-acting SSRI that blocks the serotonin transporter (SERT, encoded by *SLC6A4*). It was designed for rapid onset and a short half-life, so it can be taken on demand. Detailed mechanism-of-action data for dapoxetine are not available in the data compiled for this report, so the reasoning below rests on its SSRI class.

Serotonergic dysregulation is implicated in migraine, and some SSRIs have been explored for migraine prophylaxis. This gives a plausible but indirect rationale. The high TxGNN score is a computational prediction and does not replace dapoxetine-specific evidence.

There is also a pharmacological mismatch. Migraine prophylaxis generally needs sustained, chronic exposure, whereas dapoxetine's pharmacokinetics are built for on-demand use. This weakens the case for migraine, and also for dysthymic disorder, where established SSRIs are already available. The migraine with brainstem aura prediction is a rare subtype and probably reflects its close ontology relationship to migraine disorder rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Review | Current Neuropharmacology | Reviews off-label uses of SSRIs as a class, including migraine. It does not provide dapoxetine-specific migraine data. |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Cohort | Urologia | Looks at patient compliance with dapoxetine therapy in premature ejaculation. It is relevant to the original indication, not to migraine. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704050ABAAAAAA | Dapoxetine HCl Tablets 30 mg | Tablet | Not stated in the data compiled |

Pharmacology sources indicate that dapoxetine hydrochloride (brand name Priligy) has been available in the UK since 2008. The record above is a single-ingredient product with valid status. The identifier shown appears to follow a BNF-style code rather than a standard PL number, so please confirm it against the MHRA register.

---

## Safety Considerations

- **Drug Interactions**: The only interaction record is pharmacological rather than drug-drug. Dapoxetine acts on SERT (the serotonin transporter), consistent with its SSRI activity. No specific interacting drugs are listed in the data compiled.

Please refer to the SmPC and BNF for full warnings, contraindications and interaction information, as these were not available for this report. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on a high model score and SSRI class-level inference, with no dapoxetine-specific trials or supportive literature. Its on-demand pharmacokinetic profile also fits poorly with chronic migraine prophylaxis or dysthymia.

**To proceed, the following is needed:**
- Dapoxetine-specific mechanism of action data
- Preclinical or early-phase clinical evidence in migraine, including whether on-demand dosing is relevant
- Safety information from the SmPC and BNF (warnings, contraindications, interactions), which is required before any safety screening
- Confirmation of the approved indication text and licence details with the MHRA
- A comparison against established SSRIs and standard migraine prophylaxis options
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

