---
layout: default
title: Phenothrin
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Phenothrin
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

# Phenothrin: From Topical Ectoparasiticide Use to Aleutian Mink Disease

## One-Sentence Summary

Phenothrin is a pyrethroid-class topical insecticide/ectoparasiticide (used for external pest and flea control); no formal indication text or licensed UK product exists in this evidence pack. The TxGNN model predicts a possible link to **Aleutian mink disease**, but this is a model-only signal — **no clinical trials, no literature, and no supporting mechanism** currently back it up.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented — described only as a topical pyrethroid ectoparasiticide (flea/insect control); no approved indication text on file |
| Predicted New Indication | Aleutian mink disease |
| TxGNN Prediction Score | 97.21% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Phenothrin is not available in this evidence pack (flagged as a High-severity data gap, DG002). What is known from the supporting rationale text is that Phenothrin is a pyrethroid that acts on **insect sodium channels** and is used exclusively as a topical, external ectoparasiticide — it has no documented systemic pharmacology in mammals.

Aleutian mink disease is caused by a **parvovirus** and produces its pathology through immune-complex deposition, not through any pathway plausibly modulated by an insect neurotoxin. The evidence pack's own mechanistic assessment explicitly states there is **no known biological rationale** connecting Phenothrin to this disease.

Taken together with the fact that all ten of the top TxGNN predictions for this drug carry the same L5/Hold status and similarly worded disclaimers (several explicitly describing themselves as "prediction noise" arising from graph-structural proximity rather than pharmacology), this candidate should be read as a **low-confidence, structural artefact** of the knowledge graph rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Phenothrin currently holds **no UK marketing authorisation** (0 licences on record), so no MHRA product entry or SmPC exists to reference for this candidate.

## Safety Considerations

No structured safety data is available in this evidence pack — key warnings, contraindications and drug interaction data are all unpopulated (flagged as a Blocking data gap, DG001). Because there is no UK-authorised product, no SmPC exists to consult. Any future development would require ground-up toxicology and safety assessment (e.g. from pesticide regulatory dossiers) before this candidate could enter a formal safety review stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only (L5) prediction with zero clinical trial or literature support, an explicit lack of biological mechanism connecting the drug to the disease, and no UK marketing presence to build a safety case on. The evidence pack itself argues against pharmacological plausibility.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain regulatory labelling/warnings and contraindications before any safety review can start
- Resolve DG002 (High): confirm a verified mechanism of action via DrugBank or primary pharmacology literature
- Independent preclinical evidence for any antiviral or immunomodulatory activity relevant to parvovirus-driven disease
- Clarify translational relevance, given the predicted indication is a veterinary (mink) disease rather than a human condition
- Given all 10 ranked predictions for this drug share the same unsupported L5/Hold profile, treat this entire candidate batch as low priority pending stronger signal from an updated TxGNN run or new evidence sources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

