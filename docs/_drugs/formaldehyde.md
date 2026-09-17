---
layout: default
title: Formaldehyde
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Formaldehyde
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

# Formaldehyde: From Tissue Fixative to a Predicted Signal for Diffuse Cutaneous Leishmaniasis

## One-Sentence Summary

Formaldehyde has no approved therapeutic indication recorded in this evidence pack; in the source literature it appears almost exclusively as a laboratory tissue-fixation and specimen-preservation reagent. The TxGNN model nonetheless assigns a very high prediction score to **Diffuse Cutaneous Leishmaniasis**, but this is supported by only **1 publication** (and **0 clinical trials**), and that publication is a diagnostic-methodology study rather than treatment evidence — so the signal should be read as low-confidence and largely artefactual.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — no approved therapeutic indication on record. Formaldehyde is known clinically as a tissue fixative, disinfectant and antiseptic reagent rather than a systemic medicine |
| Predicted New Indication | Diffuse Cutaneous Leishmaniasis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for formaldehyde as a systemic therapeutic agent. Based on the evidence pack, formaldehyde is not associated with any approved indication, and no pharmacological rationale linking it to leishmaniasis treatment has been identified.

There is no established clinical or mechanistic relationship between formaldehyde and Diffuse Cutaneous Leishmaniasis. The single supporting publication (PMID 9830259) compares detection rates of *Leishmania* parasites in formalin-fixed, ethanol-fixed and frozen skin specimens using PCR and Southern blotting — this is a diagnostic-specimen-preservation methodology study, not evidence of therapeutic efficacy. Formaldehyde's appearance alongside "leishmaniasis" in this literature reflects its routine use as a histology fixative for biopsy samples, not a drug-disease treatment relationship.

Mechanistically, this prediction is unlikely to be applicable. TxGNN's knowledge-graph embeddings can be driven by frequent textual co-occurrence (e.g. "formalin-fixed leishmaniasis specimen") rather than genuine pharmacological association, and that appears to be the case here. Formaldehyde is also widely recognised as a systemic and mitochondrial toxin with carcinogenic potential, which further reduces its plausibility as a candidate for treating a chronic parasitic skin condition requiring prolonged administration. This should be treated as a hypothesis-generating artefact of the model rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9830259](https://pubmed.ncbi.nlm.nih.gov/9830259/) | 1998 | Methodology/Comparative | The Journal of Dermatology | Compared *Leishmania* parasite detection rates by PCR/Southern blotting across formalin-fixed, ethanol-fixed and frozen skin biopsy specimens (16 of 19 cases cutaneous leishmaniasis); formaldehyde used solely as a specimen-fixation reagent, not as a treatment |

## UK Market Information

Formaldehyde currently holds no UK marketing authorisations and is not marketed for any therapeutic indication in this dataset.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) — the single supporting reference is a diagnostic-specimen-fixation study, not therapeutic evidence, and no mechanism of action, clinical trial data, or UK marketing authorisation exists to support this signal. Formaldehyde's known systemic toxicity further weighs against pursuing this indication.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DrugBank/pharmacology review) establishing biological plausibility for anti-leishmanial activity
- Independent verification that the TxGNN score is not an artefact of literature co-occurrence (formalin-as-fixative bias)
- Preclinical or in vivo efficacy data specific to *Leishmania* species
- Toxicology and safety assessment (SmPC/TFDA equivalent), given formaldehyde's recognised carcinogenic and cytotoxic profile
- Route of administration and formulation feasibility assessment, as none is currently defined
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

