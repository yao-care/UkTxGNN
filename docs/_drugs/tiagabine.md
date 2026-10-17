---
layout: default
title: Tiagabine
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Tiagabine: predicted new indication Visual epilepsy (evidence level L5). Approved use: Partial epilepsy"
---

# Tiagabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Tiagabine: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

Tiagabine is a GABA reuptake inhibitor, originally used as add-on treatment for partial epilepsy.
The TxGNN model predicts it may be effective for **visual epilepsy**,
but there are currently **no registered clinical trials** and only **general reviews** among the **18 publications** identified, none specific to this condition. The prediction rests mainly on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy (from the TxGNN knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L5 (model prediction with no condition-specific studies; the compiled data rate it L4 on the basis of mechanism reviews) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled record. From general pharmacological knowledge and the reviews listed below, tiagabine selectively inhibits the GABA transporter GAT-1, which raises synaptic GABA levels and increases inhibition in the brain. It is established as add-on therapy for partial (focal) seizures.

Visual epilepsy (for example, seizures with visual symptoms, or occipital or photosensitive epilepsy) plausibly falls within the focal seizure spectrum. This gives a mechanistic overlap with the approved indication.

The very high TxGNN score probably reflects how close this disease is to partial epilepsy in the knowledge graph, rather than independent evidence. There are also caveats. Visual field defects are mainly associated with vigabatrin, and tiagabine appears to carry a much lower risk, but this still deserves attention in patients with visual symptoms. One review also describes tiagabine and other GABAergic drugs sometimes worsening seizures, particularly in generalised epilepsies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomised trials specific to visual epilepsy were identified. The main publications are listed below, with guidelines and reviews prioritised.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline / Systematic Review | Neurology | AAN/AES update on the efficacy and tolerability of newer antiepileptic drugs in new-onset epilepsy |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Mechanisms of action of currently used antiseizure drugs |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Review | J Neurol Neurosurg Psychiatry | Visual field effects of vigabatrin and tiagabine (no abstract available) |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Review | Pediatric Neurology | Visual adverse effects of antiepileptic drugs, including changes in visual fields and colour vision |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Review | Epilepsia | Tiagabine inhibits GABA reuptake; effective as add-on therapy for partial seizures; predictable pharmacokinetics and no relevant effect on other antiepileptic drug levels |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Review | Seminars in Pediatric Neurology | Effective against partial seizures in adults and adolescents; preliminary paediatric data encouraging |
| [26210064](https://pubmed.ncbi.nlm.nih.gov/26210064/) | 2015 | Review | Epilepsy & Behavior | Drug-induced status epilepticus; GABAergic antiepileptics, including tiagabine, may exacerbate seizures |
| [12479659](https://pubmed.ncbi.nlm.nih.gov/12479659/) | 2002 | Case series | Bipolar Disorders | Tiagabine in treatment-refractory bipolar disorder (not relevant to epilepsy) |
| [12205797](https://pubmed.ncbi.nlm.nih.gov/12205797/) | 2002 | Review | Archives de Pédiatrie | Tiagabine among drugs effective in partial epilepsies |
| [11520318](https://pubmed.ncbi.nlm.nih.gov/11520318/) | 2001 | Review | Epilepsia | Epileptic encephalopathies (general background) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010ABAAAAAA (BNF code, not a PL number) | Tiagabine tablets 5 mg | Tablet | Indication text not available in the compiled data; BNF chapter 4.8.1 (antiepileptic drugs) |

## Safety Considerations

- **Conditions linked to contraindication in the knowledge graph** (derived from the TxGNN graph, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease.
- **Drug Interactions**: 97 interactions were identified in the DDInter database. Those rated Moderate include:
  - aprepitant
  - morphine (including liposomal)
  - dronabinol
  - nabilone
  - metoclopramide
  - opium

  Many others are rated Unknown, including pantoprazole, omeprazole, lansoprazole, metformin, doxycycline, prednisone, ondansetron, simvastatin and rosiglitazone.
- **Visual effects**: The literature flags visual field effects of antiepileptic drugs (mainly vigabatrin, with a lower risk for tiagabine). This is particularly relevant if the drug is considered for patients with visual symptoms.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and mechanistic plausibility alone. There are no trials or condition-specific studies for visual epilepsy, and the high score probably reflects its closeness to partial epilepsy in the knowledge graph.

**To proceed, the following is needed:**
- Clinical or observational data specifically in visual, occipital or photosensitive epilepsy
- Confirmed mechanism of action data and label warnings and contraindications from the SmPC and BNF
- Approved indication text and PL number for the UK authorisation
- A visual safety assessment, including visual field monitoring, in the target population
- A review of the moderate-level interactions, particularly with opioids and cannabinoids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

