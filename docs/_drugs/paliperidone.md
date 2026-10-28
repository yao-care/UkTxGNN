---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 474
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Paliperidone"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
description: "Paliperidone: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Not recorded in the local data"
---

# Paliperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Paliperidone: Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Paliperidone is an atypical antipsychotic, originally used to treat schizophrenia and related psychotic disorders.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but there are **no clinical trials and no publications** supporting it. The only prediction with any related studies is **treatment-refractory schizophrenia** (3 Phase 4 trials, 2 reviews), and even that evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 (retinal dystrophy); L4 (treatment-refractory schizophrenia) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Paliperidone is generally known as a dopamine D2 and serotonin 5-HT2A receptor antagonist, and its efficacy in schizophrenia is established.

**Retinal dystrophy (rank 1):** No mechanistic link is supported. The high score (0.999) is a model output only, and no trials or literature were found. The same applies to the other highly ranked predictions, which include X-linked and syndromic myopia, hydranencephaly, a congenital disorder of glycosylation, perisylvian polymicrogyria, Charcot-Marie-Tooth disease type 1G and atypical glycine encephalopathy. Most are monogenic or structural conditions in which an antipsychotic is unlikely to alter the underlying disease. A speculative dopaminergic role in eye growth has been suggested for myopia, but nothing here supports it for paliperidone.


## Clinical Trial Evidence

No trials are registered for the rank 1 prediction (retinal dystrophy with or without extraocular anomalies).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Active, not recruiting | 84 | Pharmacotherapy plus recovery-oriented programmes in treatment-resistant schizophrenia and bipolar disorder; the focus is psychosocial, not paliperidone efficacy |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Open-label randomised comparison of aripiprazole vs paliperidone/risperidone using multi-omics data in first-episode psychosis; no results available |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Exploratory immune and inflammatory response, clozapine vs non-clozapine antipsychotics; sample too small for conclusions |

## Literature Evidence

No literature was found for the rank 1 prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Esp Psiquiatr | Psychopharmacology of schizoaffective disorder; treatment relies mainly on antipsychotics, with little condition-specific evidence |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Curr Opin Psychiatry | Efficacy and tolerability of psychosocial and drug treatments in early-onset schizophrenia spectrum disorders, including dosing, switching and adverse effect monitoring |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010AEAAABAB | Paliperidone 6 mg modified-release tablets | Modified-release tablet | Not available in the data compiled |

The listed identifier follows a BNF-style code (BNF chapter 4.2.1, antipsychotic drugs) rather than a standard PL number. One valid single-ingredient authorisation is recorded.

## Safety Considerations

- **Contraindications and cautions suggested by the knowledge graph** (not label text; check against the SmPC):
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorders, myocardial infarction, coronary thrombosis
  - Neurological: epilepsy, basal ganglia disease, multiple system atrophy, focal hand dystonia, blepharospasm
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia (including familial), obesity (including monogenic), potassium deficiency
  - Haematological and other: neutropenia, agranulocytosis, haemoglobinopathy, impaired renal function, Crohn's disease and inflammatory bowel disease, female breast carcinoma
- **Drug interactions:** 100 interactions were recorded; the main ones listed are below.
  - **Major:** bupropion, morphine
  - **Moderate (examples):** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, chlorpropamide, albiglutide), anticholinergic agents (atropine, hyoscyamine, glycopyrronium), epinephrine, hydrocortisone, famotidine, loperamide, bisacodyl, lorcaserin, amphotericin B

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions (including retinal dystrophy with or without extraocular anomalies) rest on model scores alone, with no trials, no literature and no plausible mechanistic link.

**To proceed, the following is needed:**
- Mechanism of action data for paliperidone, to allow a proper mechanistic analysis
- The approved indication text and SmPC warnings and contraindications for the UK product
- Direct clinical evidence of paliperidone in treatment-refractory schizophrenia, for example trial results where paliperidone is the studied intervention
- For the other predictions, a credible biological rationale and preclinical evidence before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

