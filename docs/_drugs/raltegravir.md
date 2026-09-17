---
layout: default
title: Raltegravir
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Raltegravir is a well-established HIV-1 integrase strand transfer inhibitor (INSTI); the evidence pack itself does not confirm its original licensed indication or mechanism of action.
> The TxGNN model's top prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** with a score of **99.78%**, but the underlying evidence — two Phase 3 clinical trials in human HIV-1 patients — has been explicitly flagged by the source analysis as an unrelated, text-matching false positive, not genuine cross-species evidence.
> No literature or trials support this prediction directly; the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (`original_indications` field empty; Raltegravir is generically known as an HIV-1 integrase inhibitor, but this was not captured in the pack) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a Blocking-severity data gap for TFDA/MHRA warnings and a High-severity gap for MOA). Based on generally established pharmacological knowledge, Raltegravir belongs to the integrase strand transfer inhibitor (INSTI) class, used in combination antiretroviral therapy for HIV-1 infection.

The TxGNN model's top-ranked prediction — Feline Acquired Immunodeficiency Syndrome (FIV) — has a superficial mechanistic rationale: FIV is a lentivirus, as is HIV, and both depend on an integrase enzyme to insert viral DNA into the host genome. However, the two clinical trials attached as "supporting evidence" (NCT01231516, NCT01227824) are in fact head-to-head Phase 3 trials comparing Raltegravir with Dolutegravir in **human** HIV-1-infected adults, not FIV-infected cats. Both trials were graded **C (low relevance)** in the source analysis, with the explicit conclusion that this is a knowledge-graph embedding artefact caused by textual similarity between "immunodeficiency syndrome" terms, rather than real cross-species evidence. No feline-specific trial, veterinary literature, or pharmacokinetic data for cats is present anywhere in the evidence pack.

Two lower-ranked predictions from the same run are worth noting for context, though outside the scope of this report's primary indication: **Simian Immunodeficiency Virus (SIV) infection** (rank 2, L3, "Research Question" stage) is genuinely supported by multiple non-human primate studies — but this reflects Raltegravir's established role as a research tool in SIV/macaque models of HIV, not a new human therapeutic indication. **A rare neurodevelopmental disorder** (rank 3, L5) has no supporting trials or literature at all and rests purely on a speculative interferonopathy hypothesis. None of the three top predictions constitute an actionable new human indication at this time.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Dolutegravir vs Raltegravir in antiretroviral-experienced, integrase-inhibitor-naïve **human** HIV-1 adults — not related to feline disease; graded C relevance (false-positive text match) |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs Raltegravir in antiretroviral-naïve **human** HIV-1 adults — not related to feline disease; graded C relevance (false-positive text match) |

**Note:** Neither trial provides genuine support for the predicted indication (FIV). They are included here only because they were linked by the TxGNN evidence pipeline; both are confirmed unrelated to feline disease.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No marketing authorisations are recorded in the evidence pack (`total_licenses: 0`, `licenses: []`; market status: Not marketed).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Feline Acquired Immunodeficiency Syndrome) is not a viable human repurposing candidate — it is a companion-animal disease, and the source analysis has already identified the supporting trials as a text-matching false positive with no genuine mechanistic or clinical linkage. No literature or veterinary evidence exists to support this direction. The next-best prediction (SIV infection) is a non-human primate research model application rather than a new human indication, and the third (a rare neurodevelopmental disorder) has zero supporting evidence.

**To proceed, the following is needed:**
- TFDA/MHRA SmPC warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action and original licensed indication for Raltegravir (currently a High-severity data gap)
- Re-run of the TxGNN prediction pipeline with species/organism filtering to exclude non-human disease terms from the human drug repurposing candidate list
- If SIV-related research applications are of interest, a separate evaluation scoped explicitly as a non-human primate research tool, not a clinical repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

