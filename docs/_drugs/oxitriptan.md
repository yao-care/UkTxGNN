---
layout: default
title: Oxitriptan
parent: Model Prediction Only (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Oxitriptan
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

# Oxitriptan: From an Unspecified Original Indication to Insomnia

## One-Sentence Summary

Oxitriptan (5-hydroxytryptophan, 5-HTP) is the immediate precursor of serotonin, and a UK marketing authorisation exists for a 50 mg capsule, but no approved indication text was available in the data compiled for this report.
The TxGNN model predicts it may be effective for **insomnia**, with **no clinical trials** and **no publications** currently supporting this specific prediction.
The evidence is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, oxitriptan is the direct precursor of serotonin, which is in turn converted to melatonin. This offers a plausible link to sleep regulation through serotonergic and melatonergic pathways.

The original indication could not be identified, so the relationship between it and insomnia cannot be assessed. The related predictions, sleep disorder (initiating and maintaining sleep; score 98.10%), anxiety (98.06%), anxiety disorder (97.67%) and dysthymic disorder (96.31%), rest on the same serotonergic rationale. These are mechanistic hypotheses only. No trial or publication directly evaluating oxitriptan for insomnia was provided.

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

For context, one trial was linked to a lower-ranked prediction, irritable bowel syndrome (score 97.41%):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00731003](https://clinicaltrials.gov/study/NCT00731003) | Not applicable | Completed | 60 | Studied serotonergic modulation (acute tryptophan depletion and 5-HTP administration) of intestinal permeability and visceral hypersensitivity in healthy individuals and IBS patients. Mechanistic design, not an efficacy trial. Results not available. |

## Literature Evidence

Currently no related literature available for insomnia.

The only publication linked to any prediction is a 1990 review of a different drug, clomipramine (PMID [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/), *Drugs*). It covers obsessive compulsive disorder and panic disorder and does not evaluate oxitriptan, so it is not counted as clinical support.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0403040R0AAAFAF | Oxitriptan Cap 50mg | Capsule (50 mg) | Not available |

This identifier is a BNF-style product code rather than a standard PL number. It sits under BNF section 4.3.4 (antidepressant drugs, other). No manufacturer or approved indication text was available.

## Safety Considerations

- **Drug Interactions**: 17 interactions were identified. Those rated **Major** are:
  - Serotonergic and related agents: lorcaserin, fenfluramine, sibutramine, doxepin (including topical doxepin)
  - 5-HT3 antagonists: dolasetron, palonosetron, ondansetron, granisetron
  - Other: methylene blue, procarbazine

  Those rated **Moderate** are morphine, codeine, hydrocodone, cyproheptadine, ozanimod and ifosfamide. Serotonin syndrome is the main concern with serotonergic combinations.

Please refer to the SmPC and BNF for warnings and contraindications, which were not available in the data compiled for this report. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction has a high model score but no supporting trials or publications (L5). Warnings, contraindications, mechanism data and the approved indication are all missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- SmPC or BNF warnings and contraindications for the marketed product
- The approved indication and manufacturer details for the existing authorisation
- Mechanism of action data (for example from DrugBank)
- A literature and trial search specific to oxitriptan/5-HTP in insomnia and sleep disorders
- A review of the serotonergic and 5-HT3 antagonist interactions, with a monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

