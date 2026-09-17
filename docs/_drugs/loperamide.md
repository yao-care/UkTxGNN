---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Antidiarrhoeal Use to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide (DrugBank DB00836) is a peripherally-restricted opioid-receptor agonist conventionally used to reduce intestinal motility. The TxGNN model assigns its highest score to **Acute Contagious Conjunctivitis**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the underlying evidence pack explicitly flags it as likely knowledge-graph noise rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset — `original_indications` is empty and no UK licences are recorded |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no formal mechanism-of-action record is available in the drug-level fields (flagged as data gap DG002). However, the model's own rationale confirms that loperamide acts as a peripherally-restricted μ-opioid receptor agonist, working on the myenteric plexus of the gut to suppress peristalsis — a mechanism specific to gastrointestinal motility.

There is **no known mechanistic pathway** connecting opioid-receptor-mediated gut motility suppression to acute contagious conjunctivitis, which is driven by ocular surface infection and local inflammatory/immune processes. Despite the very high TxGNN similarity score (rank 778 of the model's output), the prediction is accompanied by no corroborating clinical trials or literature evidence whatsoever.

Taken together, this pattern — an extremely high score with a biologically implausible mechanism and a complete absence of external evidence — is characteristic of a **false-positive signal generated via unrelated intermediate nodes** in the knowledge graph, rather than a genuine repurposing opportunity. This assessment is consistent with the evidence pack's own scoring: decision stage S0, recommendation Hold.

**Context from other candidates in this evidence pack:** none of the remaining nine predicted indications materially strengthen the case for repurposing loperamide:
- **Amebic dysentery** (rank 2, L4) is supported only by a case report ([PMID 17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/)) describing loperamide use *causing* fulminant amoebic colitis — a **negative safety signal**, not supportive evidence, because antimotility agents can delay clearance of invasive pathogens.
- **Conjunctivitis** (rank 3, L5) cites two clinical trials that on inspection concern azithromycin for trachoma, unrelated to loperamide — a data-linkage mismatch, not real evidence.
- **Gastroduodenitis** (rank 4, L3) has a single 1986 non-English observational article suggesting symptomatic benefit for diarrhoea associated with functional GI disorders — plausible as symptom relief only, not disease-modifying, and too dated/weak to support action.
- Ranks 5–10 (various conjunctival conditions and Angelucci syndrome) have no evidence at all and share the same implausible mechanistic profile as rank 1.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acute Contagious Conjunctivitis.

---

## Literature Evidence

Currently no related literature available for Acute Contagious Conjunctivitis.

---

## UK Market Information

According to this evidence pack, loperamide has **no marketing authorisations on record** (market status: "not marketed"; total licences: 0). This is at odds with loperamide's well-known availability in the UK (e.g. as Imodium, OTC and POM presentations) and should be **verified directly against the MHRA product register** before this dataset is relied upon for any regulatory or commercial decision.

---

## Safety Considerations

Formal key warnings, contraindications, and drug-interaction data are not available in this evidence pack (flagged as data gap DG001, severity: Blocking — TFDA label/warnings not yet retrieved).

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

One relevant safety signal did emerge from the literature review, though it relates to a different candidate indication (amebic dysentery) rather than the top-ranked prediction: a published case report links loperamide use to fulminant amoebic colitis in the setting of invasive intestinal infection ([PMID 17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/)). This underscores that antimotility agents carry a plausible mechanism for harm in invasive enteric infections and should not be assumed safe by default in any GI-infection-adjacent repurposing indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (acute contagious conjunctivitis) has no clinical or literature support and no plausible mechanistic link to loperamide's known pharmacology; it is best interpreted as a knowledge-graph artefact. No other candidate in the top 10 reaches a level of evidence sufficient to justify further investment, and one candidate (amebic dysentery) carries an identified safety concern rather than supportive evidence.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/MHRA label warnings and contraindications before any safety-relevant evaluation can proceed
- Resolve DG002: obtain formal DrugBank/SmPC mechanism-of-action data to properly assess mechanistic plausibility for any future candidate
- Verify actual UK marketing-authorisation status directly with MHRA, as the "not marketed" / 0-licence record in this dataset appears inconsistent with known market presence
- If further TxGNN-driven repurposing screening is pursued for this drug, prioritise candidates with independent literature or trial corroboration over score magnitude alone, given the demonstrated rate of noise/mismatch in this batch (ranks 1, 3, 5–10)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

