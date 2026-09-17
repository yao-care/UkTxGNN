---
layout: default
title: L-Lysine
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 3
---

# L-Lysine
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

# L-Lysine: From Essential Amino Acid to Predicted Gastroparesis

## One-Sentence Summary

> L-Lysine is an essential amino acid; no established original indication or mechanism of action was supplied in this evidence pack.
> The TxGNN model predicts a possible link to **Gastroparesis**,
> but this is supported by only **1 publication** and **no clinical trials**, and closer review suggests the signal is a text-mining artefact rather than a genuine therapeutic association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no licensed indication recorded in this dataset |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for L-Lysine in this evidence pack, and no original indication is recorded, so a conventional "original indication → new indication" mechanistic bridge cannot be constructed.

More importantly, the single supporting publication (PMID 29414870) does not describe lysine as a therapeutic agent for gastroparesis at all — it describes a gelatin-**alginate** hydrogel (in which lysine-related crosslinking chemistry is used as a *material* component) for delivering mesenchymal stem cells to the stomach. Lysine appears only as part of the biomaterial, not as the treatment target or active ingredient. This strongly suggests the TxGNN score reflects textual co-occurrence rather than a genuine pharmacological relationship.

This pattern is consistent across the other top-ranked predictions in this evidence pack: the "congenital prothrombin deficiency" candidate is driven by a paper describing a pathogenic Glu→Lys **mutation** (i.e. lysine substitution *causes* disease, not treats it), and the "vitamin D deficiency" candidate has no supporting literature or trials at all and references an obsolete disease-ontology term. Taken together, these findings indicate the model has picked up on the string "Lys" rather than a biologically meaningful signal, and none of the top three predictions currently constitute a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical/Materials | Bioengineering (Basel) | Describes gelatin-alginate hydrogel delivery of mesenchymal stem cells to the stomach for gastroparesis; lysine features only as a hydrogel crosslinking component, not as the therapeutic agent or target |

---

## UK Market Information

L-Lysine currently holds no marketing authorisation on record in this dataset (0 licences; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only), there are no supporting clinical trials, and the sole literature citation does not actually support a treatment relationship — closer reading indicates the TxGNN signal is a text-mining artefact. All three top-ranked predicted indications for this drug show the same pattern, so none currently warrant progression.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action for L-Lysine (currently unavailable)
- Regulatory safety labelling (warnings/contraindications), which is currently a blocking data gap
- A genuine mechanistic hypothesis for gastroparesis independent of the identified text-mining artefact, ideally supported by preclinical pharmacology rather than materials-science literature
- Re-screening of lower-ranked TxGNN predictions, since the top three candidates all appear to be false positives driven by superficial text matching on "Lys"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

