---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 553
evidence_level: L5
indication_count: 3
---

# Tapentadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tapentadol: From Moderate-to-Severe Pain to Migraine Disorder

## One-Sentence Summary

> Tapentadol is a centrally-acting opioid analgesic with a mu-opioid agonist and noradrenaline reuptake inhibition (NRI) component, used to treat moderate-to-severe pain. The TxGNN model predicts a possible effect in **Migraine Disorder**, but this direction is currently supported only by indirect literature (**0 clinical trials**, **2 general migraine-treatment reviews that do not evaluate tapentadol directly**) and is contradicted by major headache-medicine guidance advising against opioid use in migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe pain (opioid analgesic) — not explicitly recorded as a discrete field in the Evidence Pack; detailed original indication/MOA data are flagged as gaps (DG002) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tapentadol is not available in this Evidence Pack (data gap DG002). Based on the information that is available, tapentadol acts as a mu-opioid receptor agonist combined with a noradrenaline reuptake inhibition (NRI) component. This dual mechanism is used clinically to manage moderate-to-severe pain, and the NRI element is pharmacologically related to descending pain-modulation pathways — a system also implicated in migraine pathophysiology (similar to how SNRIs are sometimes used off-label in migraine prevention).

On this basis, the TxGNN model has identified a theoretical mechanistic overlap between tapentadol's pain-modulating pathway and migraine, which likely explains the high prediction score (99.67%).

However, this mechanistic plausibility is substantially offset by a significant negative signal already captured in the Evidence Pack: major headache-medicine guidelines (AHS/AAN) explicitly recommend **against** using opioid analgesics, including tapentadol, in migraine treatment. This is due to the well-established risk of medication-overuse headache (MOH) and the absence of evidence that opioids outperform existing migraine-specific therapies (triptans, NSAIDs, CGRP-targeted agents). This guideline-level caution is an important counterweight to the model's high score and is the primary reason evidence strength remains low despite the strong prediction signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tapentadol in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews dipyrone (metamizole), not tapentadol, for postoperative/migraine pain; included for general analgesic-in-migraine context only |
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews sumatriptan plus naproxen for acute migraine; establishes triptan/NSAID combinations as effective standard-of-care, not tapentadol |

**Note:** Neither publication evaluates tapentadol directly. They are included because they were the top-ranked literature matches in the Evidence Pack, and are presented here for transparency; they should be regarded as background context rather than direct supporting evidence.

---

## UK Market Information

Tapentadol currently has **no UK marketing authorisation** on record in this Evidence Pack (0 licenses, market status: Not marketed). No product-specific authorisation table can be produced at this time.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** Key warnings, contraindications, and drug–drug interaction data for tapentadol were not available in this Evidence Pack (flagged as a Blocking data gap, DG001). This gap must be resolved before any formal safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials or drug-specific literature support the use of tapentadol in migraine; the evidence base is model-prediction-only (L5).
- The mechanistic rationale is directly contradicted by established headache-medicine guidance (AHS/AAN) against opioid use in migraine due to medication-overuse headache risk.
- Tapentadol has no UK marketing authorisation, and a Blocking safety data gap (product warnings/contraindications) prevents entry into formal safety evaluation.

**To proceed, the following is needed:**
- Product labelling / SmPC data (warnings and contraindications) to resolve the Blocking gap (DG001)
- Detailed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Direct clinical or pharmacoepidemiological evidence evaluating tapentadol specifically in migraine populations
- Drug–drug interaction data, currently returned as "not found"

**Additional note:** Two lower-ranked predictions for tapentadol (migraine with brainstem aura; migraine susceptibility) were also generated by TxGNN but carry even weaker evidentiary support — one has zero associated literature or trials, and the other is linked to a genetic-susceptibility phenotype rather than an active disease state suitable for pharmacological intervention. Neither changes the overall Hold recommendation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

