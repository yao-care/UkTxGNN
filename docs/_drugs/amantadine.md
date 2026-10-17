---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Amantadine: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson's disease"
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Amantadine: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is originally used to treat Parkinson's disease and related parkinsonian and movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **no clinical trials** and **no publications** supporting this specific prediction; the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (the data compiled for this report contain no approved indication text for the UK authorisation; the original indication is taken from the knowledge graph) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amantadine is used in Parkinson's disease and other parkinsonian and movement disorders, and its efficacy there is established. Mechanistically, it may be applicable to Rasmussen encephalitis.

One plausible but unverified link is amantadine's NMDA receptor antagonism. Glutamate receptor-mediated excitotoxicity and autoimmunity against GluR3 have been proposed in Rasmussen encephalitis. This is a hypothesis only and is not supported by evidence in the data compiled for this report.

## Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Transaldolase deficiency | 99.27% | L5 | No trials or literature. No clear mechanistic link to dopaminergic or NMDA activity; the score likely reflects knowledge-graph proximity. |
| 3 | Myelitis | 99.24% | L3 | Indirect evidence from post-polio syndrome fatigue; reviews suggest weak or negative evidence. |
| 4 | PLA2G6-associated neurodegeneration | 99.23% | L4 | One case report in a different disease (PKAN); extrapolation is indirect. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Rasmussen subacute encephalitis.

For context, the literature retrieved for the lower-ranked prediction **myelitis** is mostly about post-polio syndrome, an indirect link:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25984923](https://pubmed.ncbi.nlm.nih.gov/25984923/) | 2015 | Cochrane systematic review | Cochrane Database Syst Rev | Treatment for post-polio syndrome; effectiveness of pharmacological treatment not established |
| [21328301](https://pubmed.ncbi.nlm.nih.gov/21328301/) | 2011 | Cochrane systematic review | Cochrane Database Syst Rev | Earlier version of the above review; same conclusion on unproven pharmacological treatment |
| [7611638](https://pubmed.ncbi.nlm.nih.gov/7611638/) | 1995 | RCT | Ann N Y Acad Sci | Double-blind, placebo-controlled trial of amantadine for fatigue in post-polio syndrome (23 patients completed 6 weeks) |
| [16879288](https://pubmed.ncbi.nlm.nih.gov/16879288/) | 2006 | Guideline | Eur J Neurol | EFNS guideline on diagnosis and management of post-polio syndrome |
| [2039376](https://pubmed.ncbi.nlm.nih.gov/2039376/) | 1991 | Case series | Arch Neurol | Post-polio fatigue treated with amantadine |

For **PLA2G6-associated neurodegeneration**, the only paper is [31366412](https://pubmed.ncbi.nlm.nih.gov/31366412/) (2019, Can J Neurol Sci), a case report on amantadine for gait dysfunction in PKAN, a different disease.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409010B0AAAAAA | Amantadine HCl capsules 100 mg | Capsule | Not stated in the data compiled for this report |

The dosage form and indication text are not recorded for this authorisation. The identifier is not in the standard MHRA PL number format and should be checked against the MHRA register and the BNF.

## Safety Considerations

- **Conditions linked to contraindication in the knowledge graph** (not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, epilepsy, kidney disease, pyoureter, congestive heart failure, psychotic disorders (including schizophreniform and schizoaffective disorder), mental disorder, melanoma, angle-closure glaucoma, substance-related disorders, atopic eczema and dermatitis.
- **Drug Interactions**: 93 interactions recorded. Notable examples:
  - **Major**: bupropion.
  - **Moderate**: anticholinergic and antimuscarinic agents (atropine, hyoscyamine, scopolamine, dicyclomine, glycopyrronium, clidinium, propantheline, trospium, mepenzolate, methscopolamine), metoclopramide, and bowel preparations (polyethylene glycol with electrolytes, picosulfuric acid, sodium sulfate).

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Rasmussen encephalitis prediction rests only on a high TxGNN score, with no trials or publications. The proposed NMDA-antagonism link is a hypothesis. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for amantadine
- Preclinical or case-level evidence in Rasmussen encephalitis (e.g. GluR3 and NMDA-related models)
- Label warnings, contraindications and approved indication text for the UK authorisation
- Review of the contraindication-linked conditions (epilepsy, renal disease, psychosis), particularly as Rasmussen encephalitis is characterised by epilepsy
- If myelitis is pursued instead, verification of the 1995 RCT population, bearing in mind the Cochrane reviews found no established benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

