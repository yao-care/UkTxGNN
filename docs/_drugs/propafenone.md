---
layout: default
title: Propafenone
parent: Model Prediction Only (L5)
nav_order: 524
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Propafenone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Atrial fibrillation"
---

# Propafenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Propafenone: From Atrial Fibrillation and Ventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Propafenone is a class IC antiarrhythmic, originally used for atrial fibrillation and ventricular tachycardia.
The TxGNN model's most clinically plausible prediction is **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, supported by **no registered clinical trials** and **10 publications** (mostly case-level and preclinical mechanistic studies).
The model's top-ranked prediction, manic bipolar affective disorder, is not supported; the literature points to harm rather than benefit.

> This report focuses on the CPVT prediction, which has the strongest evidence. The other predictions are summarised in the final section for completeness.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; ventricular tachycardia (the data compiled for this report contains no UK licence indication text) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia (rank 2 by TxGNN score; rank 1, manic bipolar affective disorder, is judged an artefact) |
| TxGNN Prediction Score | 99.79% (CPVT); 99.80% (manic bipolar affective disorder) |
| Evidence Level | L3 (CPVT) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails (research question only; not for clinical use outside specialist care) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, propafenone is a class IC antiarrhythmic that blocks sodium channels. Its efficacy in ventricular tachycardia is established, and mechanistically it may be applicable to CPVT.

CPVT is an inherited arrhythmia syndrome, usually caused by mutations in the cardiac ryanodine receptor (RyR2) or calsequestrin (CASQ2). These cause abnormal calcium release and arrhythmogenic calcium waves during adrenergic stress. Preclinical studies show that class I antiarrhythmics, including flecainide and R-propafenone, block open-state RyR2 channels and suppress these calcium waves. This is the core pathophysiology of CPVT.

Flecainide is the established agent in this class for CPVT. Propafenone data are limited to mechanistic studies and a case report describing 35 years of effective treatment. Propafenone is therefore best viewed as a plausible alternative or comparator, not a proven therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30820400](https://pubmed.ncbi.nlm.nih.gov/30820400/) | 2019 | Case report | HeartRhythm Case Reports | A 35-year effective treatment of CPVT with propafenone |
| [21270101](https://pubmed.ncbi.nlm.nih.gov/21270101/) | 2011 | Basic research | Circ Arrhythm Electrophysiol | RyR2 inhibition determines the efficacy of class I antiarrhythmics in CPVT |
| [26121139](https://pubmed.ncbi.nlm.nih.gov/26121139/) | 2015 | Basic research | PLoS One | RyR2 channel activity determines the potency of flecainide and R-propafenone against arrhythmogenic calcium waves |
| [21798265](https://pubmed.ncbi.nlm.nih.gov/21798265/) | 2011 | Basic research | J Mol Cell Cardiol | Class I antiarrhythmics screened for suppression of Ca2+ waves in CASQ2-deficient myocytes |
| [39564160](https://pubmed.ncbi.nlm.nih.gov/39564160/) | 2024 | Cohort | Ann Pediatr Cardiol | Long-term (>10-year) clinical course of CPVT patients |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical, genetic and arrhythmic outcomes of CPVT patients from China |
| [23965883](https://pubmed.ncbi.nlm.nih.gov/23965883/) | 2013 | Cohort | Zhongguo Dang Dai Er Ke Za Zhi | Long-term outcomes, predictors of ventricular arrhythmia and drug effects in CPVT |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Delayed diagnosis of CPVT in a child with an RYR2 mutation |
| [36082968](https://pubmed.ncbi.nlm.nih.gov/36082968/) | 2023 | Basic research | Clin Exp Pharmacol Physiol | Gain-of-function RyR2 mutation (R1760W) in CPVT |
| [42558477](https://pubmed.ncbi.nlm.nih.gov/42558477/) | 2026 | Case report | Front Pediatr | Overlap of long QT syndrome and CPVT in two children with CALM2-related calmodulinopathy |

Only the first four entries bear directly on propafenone or class I drugs in CPVT. The remainder provide disease background.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0203020R0AAAAAA | Propafenone HCl tablets 150 mg | Tablet | Not stated in the data compiled for this report |

This is a single valid single-ingredient authorisation. The number shown is a classification-style code rather than a standard MHRA PL number, so it should be checked against the MHRA register. Please refer to the BNF (cardiovascular system, antiarrhythmic drugs) and the SmPC for the authorised indications.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are graph-derived associations, not label text):
- Cardiac: long QT syndrome (including familial), torsades de pointes, myocardial infarction, coronary artery disease and atherosclerosis, hypotensive disorders
- Haematological: agranulocytosis, neutropenia (including congenital forms), haemoglobinopathy
- Other: kidney disease, liver disease, gallbladder disease, potassium deficiency, myasthenia gravis and neuromuscular junction disease

**Drug interactions** (100 interactions identified; examples shown):
- **Major:** dolasetron, eliglustat
- **Moderate:** cimetidine, clarithromycin, levofloxacin, ondansetron, palonosetron, bupropion, aprepitant, famotidine, alosetron, loperamide, lorcaserin
- **Minor:** metronidazole

Many interactions relate to QT prolongation or CYP2D6/CYP3A4 inhibition, which raise propafenone exposure or proarrhythmic risk. Check the full list against the SmPC and BNF.

**Indication-specific cautions:**
- Class IC agents carry proarrhythmia risk, especially in structural heart disease.
- Case reports describe propafenone causing QRS widening and incessant VT in arrhythmogenic right ventricular cardiomyopathy (ARVC).
- Case reports describe propafenone-associated mania and a psychosis linked to a venlafaxine interaction.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (Summary)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Manic bipolar affective disorder | 99.80% | L5 | Hold. No plausible therapeutic mechanism; literature suggests propafenone may cause mania |
| Incessant infant ventricular tachycardia | 99.44% | L3 | Research question. Older paediatric studies (e.g. PMID 8237821) report oral propafenone use; evidence is retrospective and proarrhythmia risk needs assessment |
| Arrhythmogenic right ventricular cardiomyopathy | 99.42% | L4 | Hold. Safety signals (QRS widening, provoked incessant VT); risk-benefit appears unfavourable |
| Periodic paralysis with transient compartment-like syndrome | 99.67% | L5 | Hold. Prediction only; no trials or literature |
| Prinzmetal angina | 99.45% | L5 | Hold. No anti-vasospastic mechanism; class IC agents are generally avoided in ischaemic heart disease |
| Nephrogenic syndrome of inappropriate antidiuresis | 99.23% | L5 | Hold. No mechanistic link; no trials or literature |
| Trichotillomania | 99.17% | L5 | Hold. No plausible rationale; no trials or literature |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for CPVT, as a research question only)

**Rationale:**
Preclinical studies show that propafenone suppresses RyR2-mediated calcium waves, and a long-term case report supports clinical plausibility. However, there are no registered trials, flecainide is the established agent in this class, and the evidence is at case and mechanistic level (L3). Most other predictions should be held.

**To proceed, the following is needed:**
- Detailed mechanism of action data for propafenone
- Verification of the UK licence indication text and MHRA authorisation details
- Systematic review of propafenone versus flecainide and beta-blockers in CPVT
- A structured safety assessment of proarrhythmia risk, including patient selection (exclusion of structural heart disease), ECG monitoring and interaction screening
- Expert cardiology (inherited arrhythmia) input before any prospective study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

