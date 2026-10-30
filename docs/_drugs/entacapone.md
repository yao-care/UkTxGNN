---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease and related parkinsonian syndromes"
monitor_inn: "Entacapone"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Entacapone is a COMT inhibitor, originally used as an add-on treatment for Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but **no clinical trials and no publications** currently support this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian syndromes (the licence record in the compiled data has no indication text) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, entacapone inhibits catechol-O-methyltransferase (COMT), which prolongs the activity of levodopa. Its efficacy in Parkinson disease is established.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism. Where the parkinsonian features are prominent, a symptomatic benefit from levodopa potentiation is plausible in theory. The high TxGNN score probably reflects this shared parkinsonism phenotype rather than any disease-modifying effect. It is a computational prediction only and should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409010V0AAAAAA | Entacapone Tab 200 mg | Tablet (200 mg, from product name) | Not stated in the compiled data |

The compiled data lists one valid single-ingredient authorisation. The identifier shown follows a non-MHRA format, so the PL number should be checked against the MHRA register. The BNF and NICE guidance should be consulted for the approved indication.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from network relationships, not from label text, and must be checked against the SmPC):
- Neurological and psychiatric: multiple system atrophy, drug-induced dyskinesia, epilepsy, psychotic disorder, schizophreniform disorder, schizoaffective disorder, anxiety disorder, neurotic disorder, dysthymic disorder, mental disorder
- Cardiovascular: orthostatic hypotension, postural orthostatic tachycardia syndrome, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease
- Organ disease: liver disease, kidney disease, gallbladder disease, pyoureter
- Gastrointestinal: gastric ulcer, peptic ulcer disease, diarrhoeal disease
- Eye: open-angle glaucoma, angle-closure glaucoma
- Metabolic and other: diabetes mellitus, diabetic ketoacidosis, melanoma, haemoglobinopathy

**Drug Interactions:** 82 interactions were recorded. Those graded Moderate include:
- Epinephrine (including ophthalmic and topical forms)
- Morphine (including liposomal) and opium
- Dronabinol and nabilone
- Metoclopramide
- Iron

Interactions with unknown severity grading include pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin and potassium chloride.

Hepatotoxicity warnings are also noted for the COMT inhibitor class, with tolcapone carrying the more serious signal. This is particularly relevant in mitochondrial and metabolic diseases.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Rasmussen subacute encephalitis | 0.9973 | L5 | No clear mechanistic link |
| 3 | Myelitis | 0.9963 | L5 | No mechanistic rationale or data |
| 4 | Juvenile paralysis agitans (Hunt) | 0.9960 | L5 | Largely overlaps with existing Parkinson indications |
| 7 | Lewy body dementia | 0.9925 | L5 | Only indirect preclinical signals; one imaging trial (NCT04246437) does not test entacapone |
| 10 | PSP-corticobasal syndrome | 0.9904 | L5 | Poor levodopa response expected; linked trial is observational gait analysis |

The remaining predictions (ranks 5, 6, 8 and 9: transaldolase deficiency, lethal infantile mitochondrial myopathy, fructose-1,6-bisphosphatase deficiency, and a polymicrogyria syndrome) have no plausible mechanistic link and no evidence.

Of these, Lewy body dementia is the only one with any preclinical signal. It could be framed as a research question rather than a development candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for PLA2G6-associated neurodegeneration has a high model score but no trials, no literature and only a theoretical symptomatic rationale. The evidence is at level L5.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Case series or natural-history data on levodopa and COMT inhibitor response in PLA2G6-related dystonia-parkinsonism
- Verification of the MHRA authorisation (PL number, dosage form, approved indication) and SmPC safety information
- A hepatic and cardiovascular safety review, given the knowledge-graph contraindication signals
- For Lewy body dementia, a check whether entacapone itself was tested in the in vitro study (PMID 23913715)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

