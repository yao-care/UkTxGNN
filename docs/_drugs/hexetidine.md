---
layout: default
title: Hexetidine
parent: Model Prediction Only (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Hexetidine
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

# Hexetidine: From Topical Oral Antisepsis to Interventricular Septum Aneurysm

## One-Sentence Summary

Hexetidine is a topical antimicrobial agent (referenced in the evidence base as an oral anti-plaque/antiseptic agent); this evidence pack contains no formal record of a licensed original indication or mechanism of action. The TxGNN model's top-ranked prediction links it to **Interventricular Septum Aneurysm**, but this is supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic review flags it as a likely false-positive signal from the model's embedding space rather than a biologically plausible connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no licences, no formal indication text; known non-formal use as a topical oral antibacterial/anti-plaque agent per literature context) |
| Predicted New Indication | Interventricular Septum Aneurysm |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Hexetidine is not available in this evidence pack. Based on the limited information present, Hexetidine appears to function as a topical antimicrobial/antiseptic agent (its use as an anti-plaque agent is referenced in the wider literature search below), with no identified cardiac structural or myocardial pharmacological target.

The evidence pack's own repurposing rationale for this top-ranked candidate is explicit and cautionary: it states that Hexetidine has "no cardiac structural/myocardial target or systemic pharmacological action, and no explicable mechanism linking it to interventricular septum aneurysm," concluding this is judged to be **a false positive arising from proximity in the model's embedding space** rather than a genuine signal.

This pattern holds across the full top-10 ranked list: nine of the ten candidates (congenital cardiac defects, craniofacial malformation syndromes, chromosomal deletions) carry rationale text explicitly stating "no mechanistic relevance" to a topical antimicrobial. The tenth candidate (a rare glycosylation disorder) returned two literature hits, but both concern Hexetidine's established use as an oral anti-plaque agent and a decontamination agent in leukaemia patients — unrelated to the disease label itself, and the evidence pack itself classifies this as a "label/topic mismatch" rather than direct supporting evidence. **No candidate in this batch reaches beyond L4/L5 evidence.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (Interventricular Septum Aneurysm). (Note: two indirect, non-supportive publications were found for a lower-ranked, unrelated candidate — see rationale above.)

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every candidate indication in this batch — including the top-ranked prediction — carries only L4/L5 evidence, no clinical trial support, and the evidence pack's own mechanistic review explicitly flags the top prediction as a probable false positive from model embedding-space proximity rather than genuine pharmacological plausibility. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/MHRA product labelling (warnings, contraindications) — currently missing and blocking any safety pre-screening (S1)
- Confirmed mechanism of action data from DrugBank or an equivalent source
- Independent pharmacological or in-vitro plausibility check before treating any of these TxGNN predictions as a genuine repurposing lead, given the explicit false-positive assessment already recorded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

