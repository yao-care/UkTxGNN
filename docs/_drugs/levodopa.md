---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 373
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson's disease and related parkinsonian syndromes"
monitor_inn: "Levodopa"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor, originally used to treat Parkinson's disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **no clinical trials and no publications** currently support this direction; the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease and related parkinsonian syndromes |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, levodopa is converted to dopamine in the central nervous system and treats motor syndromes caused by dopamine deficiency.

Rasmussen encephalitis is a rare, chronic, unilateral inflammatory brain disease. It involves T-cell-mediated neuroinflammation, progressive hemispheric atrophy and intractable focal seizures, including epilepsia partialis continua. Its pathology is immune-mediated rather than primarily dopaminergic.

The most plausible explanation for the prediction is an indirect link in the knowledge graph. Hemiparkinsonism-hemiatrophy syndrome, one of levodopa's listed original indications, shares features such as unilateral hemispheric atrophy. This looks like a network-proximity artefact rather than evidence of a therapeutic effect. Dopaminergic therapy would not be expected to change the immune-driven course or the seizures of Rasmussen encephalitis. The mechanistic rationale is therefore weak and unsupported at present.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409010I0AAAKAK | Levodopa liquid, 100 mg/5 ml | Oral liquid | Not stated in the data compiled |

Only one authorisation is recorded (single-ingredient, valid). The identifier shown is not in the standard MHRA PL format, so the authorisation details should be verified against the MHRA register. BNF classification and NICE appraisal information were not available in the data compiled.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): 
  - Neurological: epilepsy, multiple system atrophy, drug-induced dyskinesia
  - Cardiovascular: orthostatic hypotension, postural orthostatic tachycardia syndrome, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease
  - Psychiatric: psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, anxiety disorder, neurotic disorder, dysthymic disorder
  - Eye: open-angle glaucoma, angle-closure glaucoma
  - Gastrointestinal: peptic ulcer disease, gastric ulcer, diarrhoeal disease
  - Metabolic: diabetes mellitus, diabetic ketoacidosis
  - Other: kidney disease, liver disease, gallbladder disease, pyoureter, melanoma, haemoglobinopathy

  Epilepsy is particularly relevant, because Rasmussen encephalitis is characterised by intractable seizures.

- **Drug Interactions**: 100 interactions were recorded. The main ones (moderate unless stated) are:
  - Sympathomimetics: epinephrine, ephedrine
  - Anticholinergics and antispasmodics: atropine, hyoscyamine, methscopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate
  - Others: bupropion, metronidazole, pyridoxine, iron, metoclopramide
  - Minor: antacids, including aluminium hydroxide, calcium carbonate, magaldrate and magnesium salts

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score. There are no trials or publications, the mechanism is unsupported, and Rasmussen encephalitis is immune-mediated rather than dopamine-deficient. Seizure-related safety concerns add further caution.

**To proceed, the following is needed:**
- Mechanism of action data and a documented rationale linking dopaminergic therapy to Rasmussen encephalitis
- Preclinical or observational evidence in Rasmussen encephalitis
- SmPC and BNF warnings and contraindications, particularly regarding seizure threshold
- Verification of the UK marketing authorisation record, including approved indication and dosage form
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

