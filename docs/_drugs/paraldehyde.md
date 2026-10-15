---
layout: default
title: Paraldehyde
parent: Model Prediction Only (L5)
nav_order: 477
evidence_level: L5
indication_count: 6
---

# Paraldehyde
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Paraldehyde: From an Unspecified Original Indication to Irritable Bowel Syndrome

## One-Sentence Summary

Paraldehyde is a historical sedative-hypnotic. No approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but there are **no clinical trials** and **no publications** supporting this prediction. Evidence is limited to model output.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text recorded in the marketing authorisation data) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Paraldehyde is a sedative-hypnotic, presumed to act as a CNS depressant, possibly through GABAergic activity. This presumption is not confirmed by the data compiled for this report.

There is no established link between this class of action and the pathophysiology of irritable bowel syndrome (visceral hypersensitivity, gut-brain axis disturbance, altered motility). The very high TxGNN score (99.97%) is a graph-based prediction only. It should be treated as a hypothesis-generating signal, not as evidence of efficacy. Anxiolytic or sedative effects might theoretically relieve stress-related symptoms, but this is speculative.

Other predicted indications were also reviewed, all with model-only support:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Cauda equina syndrome | 99.97% | L5 | A compressive, surgical emergency; a sedative would not address the cause |
| Obsolete neurogenic bladder (disease) | 99.88% | L5 | Obsolete ontology term; may be a graph artefact |
| Neurocirculatory asthenia | 99.75% | L5 | Anxiety-related; indirect symptom relief is plausible but speculative |
| Rhinitis | 99.60% | L5 | No mechanistic rationale |
| Insomnia | 99.30% | L4 | Pharmacologically consistent with a sedative-hypnotic; indirect evidence only |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for irritable bowel syndrome.

The only publication identified in the compiled data relates to the rank 6 prediction (insomnia), not irritable bowel syndrome:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1585214](https://pubmed.ncbi.nlm.nih.gov/1585214/) | 1992 | Review | South African Medical Journal | General review of sleep disorder treatment (narcolepsy, sleep apnoea and others). It is indirect and not a study of paraldehyde. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408020Q0AAACAC (BNF-style code) | Paraldehyde Injection 5 ml ampoule | Injection | Not recorded |

This is a single valid, single-ingredient product. No national MHRA or NICE-appraised indication text was available in the compiled data. The code shown follows a BNF-style format rather than a standard PL number.

---

## Safety Considerations

- **Drug Interactions:** 40 interactions were recorded. The main ones by severity are:
  - **Major:** morphine, codeine, hydrocodone, disulfiram
  - **Moderate:** ethanol, other opioid-type agents (opium), promethazine, chlorpheniramine, cetirizine, brompheniramine, metoclopramide, bupropion, dronabinol, nabilone, dextromethorphan, diazoxide, phentolamine, sibutramine, amyl nitrite
  - **Minor:** warfarin

  Many of these involve additive CNS depression, so combined use needs particular caution.

Warning and contraindication text was not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for irritable bowel syndrome rests only on a graph-based score. There are no clinical trials or publications, no plausible mechanistic link, and the drug has known tolerability and interaction concerns. Better-characterised alternatives are available.

**To proceed, the following is needed:**
- Mechanism of action data for paraldehyde
- Approved indication and full safety text (warnings and contraindications) from the SmPC and BNF
- Any preclinical or clinical evidence linking paraldehyde to irritable bowel syndrome
- A review of whether the insomnia prediction (L4) is worth pursuing as a historical or mechanistic research question only, not as a development candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

