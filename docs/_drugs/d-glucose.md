---
layout: default
title: D-Glucose
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# D-Glucose
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

Using no specific skill — this is a direct document-generation task per the already-specified template rules, not a coding/debugging/brainstorming task that maps to an available skill.

# D-glucose: From No Recorded Original Indication to Non-syndromic Esophageal Malformation

## One-Sentence Summary

D-glucose has no original indication recorded in the available evidence pack, and it is not currently marketed in the UK under this dataset. The TxGNN model's top prediction is that it may be relevant to **Non-syndromic Esophageal Malformation**, but this is a knowledge-graph similarity score only — **0 clinical trials** and **0 publications** currently support this specific drug–disease pairing, and the predicted condition is a congenital structural defect with no identified pharmacological mechanism for glucose to act on.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication or mechanism of action is recorded in this evidence pack |
| Predicted New Indication | Non-syndromic Esophageal Malformation |
| TxGNN Prediction Score | 84.11% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for D-glucose is not available in this evidence pack, and no original indication is on record to compare against. Unlike typical repurposing candidates, this limits any assessment of mechanistic continuity between an established use and the newly predicted one.

More importantly, the predicted indication itself — non-syndromic esophageal malformation — is a congenital structural anomaly of the oesophagus, not a metabolic or biochemical disorder. There is no known pharmacological pathway by which glucose administration would correct a structural developmental defect. The evidence pack's own rationale for this candidate states plainly that there is no clinical trial or literature evidence, and no pharmacological mechanism supporting a D-glucose intervention here.

Taken together, this ranks as a pure knowledge-graph embedding similarity score (TxGNN rank 83,553), with no biological plausibility identified to date. For context, other candidates lower in this same prediction set — for example, biotin metabolic disease (rank 5, evidence level L3) — have a clearer, mechanistically grounded rationale (glucose as supportive therapy during acute metabolic decompensation in biotin-dependent carboxylase disorders) and considerably more supporting literature and trial data. Sponsors reviewing this evidence pack may wish to prioritise those candidates over the top-ranked but mechanistically unsupported prediction discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

D-glucose has no marketing authorisations recorded in this evidence pack (0 licences) and its UK market status is "Not marketed." No product, dosage form, or authorised indication data is currently available for this substance under this dataset.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (non-syndromic esophageal malformation) has zero supporting clinical trials or literature, no identifiable pharmacological mechanism, and represents a congenital structural condition unlikely to be responsive to a metabolic substrate. Evidence level is L5 — model prediction only.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for D-glucose (currently a High-severity data gap)
- SmPC-equivalent warnings/contraindications data (currently a Blocking data gap preventing any safety pre-assessment)
- A biological plausibility review specifically addressing whether any glucose-related pathway is relevant to oesophageal structural development
- If further repurposing work continues on this drug, consideration of re-prioritising toward candidates with stronger existing evidence in this same pack, notably biotin metabolic disease (L3, multiple trials and literature identified)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

