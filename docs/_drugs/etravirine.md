---
layout: default
title: Etravirine
parent: Moderate Evidence (L3-L4)
nav_order: 253
evidence_level: L4
indication_count: 10
---

# Etravirine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Etravirine: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used for treatment-experienced HIV-1 infection. The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a primate-only pathogen with no human clinical role — supported by **0 clinical trials** and **1 preclinical publication**, so despite a near-maximal model score this specific top-ranked signal should be read as a knowledge-graph artefact rather than an actionable human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI antiretroviral therapy in treatment-experienced adults, per trial records in the evidence pack) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Etravirine is not available in this evidence pack. Based on the information present, Etravirine is an NNRTI-class antiretroviral whose efficacy against treatment-experienced HIV-1 infection is well established; mechanistically, NNRTIs act by binding the viral reverse transcriptase enzyme, so in principle any lentivirus with a structurally similar reverse transcriptase could be susceptible.

SIV is the model's rationale here: it is a primate lentivirus that is structurally homologous to HIV-1's reverse transcriptase, so an NNRTI could theoretically show cross-activity. However, SIV is an **animal model virus used in laboratory and primate research — it does not infect humans**, so there is no realistic clinical pathway from this prediction to a human therapeutic indication. The single supporting reference is an in vitro/preclinical nanoparticle drug-delivery study that is not even specific to SIV. This combination (extremely high score, essentially no supporting evidence, non-human disease target) is a hallmark of embedding-space noise rather than a genuine repurposing opportunity.

It is worth noting that this same evidence pack contains a materially stronger, human-relevant signal further down the ranked list: **AIDS related complex** (rank 4, evidence level L2, 1 completed Phase-related trial plus 2 literature references, recommendation "Proceed with Guardrails"). That candidate sits squarely within Etravirine's known HIV-1 disease spectrum and may warrant separate evaluation, but it falls outside the scope of the rank-1 candidate discussed in this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | In vitro/Preclinical | Molecular pharmaceutics | Nanoparticle-based antiretroviral drug combinations for synergistic inhibition of cell-free and cell-cell HIV transmission; not SIV-specific and not a clinical study. |

## UK Market Information

No marketing authorisations are recorded in the evidence pack for this product. UK market status: **Not Marketed** (0 licences on file).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for this candidate is very high (99.98%), the predicted indication — SIV infection — is a non-human disease with no clinical development pathway, and it is supported only by a single, non-specific preclinical publication with no clinical trial evidence. This does not meet the threshold to advance.

**To proceed, the following is needed:**
- DrugBank-sourced mechanism of action data for Etravirine (currently missing, flagged as High severity in the evidence pack)
- MHRA/SmPC warnings, contraindications and drug interaction data (currently missing, flagged as Blocking — required before any safety pre-screen)
- If repurposing evaluation continues for this drug, redirect focus to the higher-evidence, human-relevant candidate identified in the same batch (AIDS related complex, evidence level L2), rather than the SIV signal reviewed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

