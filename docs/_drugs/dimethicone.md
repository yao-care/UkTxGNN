---
layout: default
title: Dimethicone
parent: Moderate Evidence (L3-L4)
nav_order: 216
evidence_level: L4
indication_count: 10
---

# Dimethicone
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

# Dimethicone: From Antiflatulent Use to Insomnia

## One-Sentence Summary

Dimethicone (simethicone) is an inert silicone-based antifoaming agent, traditionally used to relieve gastrointestinal bloating and, in surgical ophthalmic formulations, as a vitreous tamponade. The TxGNN model predicts it may be effective for **Insomnia**, but this is currently supported by only **1 loosely related clinical trial** and **no published literature**, and the model's own mechanistic rationale finds no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation on record in this evidence pack. (Dimethicone is generally known as an antiflatulent/antifoaming agent and, separately, as a surgical intraocular tamponade material.) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, dimethicone is a chemically and biologically inert silicone polymer that is not absorbed systemically, does not cross the blood–brain barrier, and has no recognised central nervous system activity. It has no established interaction with the neurotransmitter pathways implicated in sleep regulation (GABA, melatonin, histamine).

The single clinical trial associated with this prediction (NCT04872946) evaluated an oral/topical skin-health regimen and was not designed to assess sleep outcomes; its apparent link to insomnia is most likely a coincidental co-occurrence (the product studied may have contained unrelated sleep-supporting ingredients alongside dimethicone), rather than evidence of therapeutic effect. The model's own repurposing rationale explicitly states there is no known mechanistic pathway connecting dimethicone to insomnia.

It is also worth noting that several of the model's other top-ranked predictions for this drug (various cataract subtypes) appear to reflect a reversed causal relationship — silicone oil tamponade is a well-documented *cause* of cataract as a surgical complication, not a treatment for it. This raises broader concern that the underlying knowledge-graph edges for dimethicone may have been learned in the wrong causal direction, which further weakens confidence in the insomnia signal as well.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | Phase NA | Completed | 74 | Evaluated an oral and topical regimen for skin health (redness, sensitivity, reactivity). Not designed to assess insomnia or sleep outcomes; relevance to this indication graded C (coincidental co-occurrence, not evidence of efficacy). |

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

This product currently holds no UK marketing authorisations (market status: **Not marketed**; 0 licences on record).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There is no plausible mechanistic basis for dimethicone in insomnia, the only associated clinical trial is unrelated in design and purpose, and no supporting literature exists. Combined with signs that the underlying knowledge-graph relationships for this drug may be learned in a reversed causal direction (as seen with the cataract predictions), the evidence does not support progression at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for dimethicone (currently a blocking-adjacent High-severity data gap)
- UK/MHRA SmPC warnings, contraindications and interaction data (currently a Blocking data gap, DG001)
- Insomnia-specific preclinical or clinical evidence directly evaluating dimethicone (or its formulations) against sleep outcomes
- Independent verification of the knowledge-graph edge direction for this drug given the apparent cause/treatment confusion seen elsewhere in its prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

