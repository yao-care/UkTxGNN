---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 373
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis
{: .text-alpha }

## One-Sentence Summary

Levodopa is a dopamine precursor, originally used to treat Parkinson's disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **no clinical trials and no publications** currently support this direction; the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease and related parkinsonian syndromes |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (85 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 85 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for levodopa: "Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease." ([DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb), label version 2026-07-20; accessed 2026-11-19.) Based on general pharmacology, levodopa is converted to dopamine in the central nervous system and treats motor syndromes caused by dopamine deficiency.

Rasmussen encephalitis is a rare, chronic, unilateral inflammatory brain disease. It involves T-cell-mediated neuroinflammation, progressive hemispheric atrophy and intractable focal seizures, including epilepsia partialis continua. Its pathology is immune-mediated rather than primarily dopaminergic.

The most plausible explanation for the prediction is that the TxGNN model (deep learning) learned a similarity between related diseases. Hemiparkinsonism-hemiatrophy syndrome, one of levodopa's listed original indications, shares features such as unilateral hemispheric atrophy. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a therapeutic effect. Dopaminergic therapy would not be expected to change the immune-driven course or the seizures of Rasmussen encephalitis. The mechanistic rationale is therefore weak and unsupported at present.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0409010I0AAAKAK | Levodopa 100mg/5ml oral liquid | Levodopa |
| 0409010I0AAAJAJ | Levodopa 125mg/5ml oral suspension | Levodopa |
| 0409010I0AAAMAM | Levodopa 25mg/5ml oral suspension | Levodopa |
| 0409010I0AAAFAF | Levodopa 500mg tablets | Levodopa |
| 0409010N0BGAAAE | Apodespan PR 50mg/200mg tablets | Co-careldopa (Carbidopa/levodopa) |
| 0409010N0BEAAAG | Caramet 25mg/100mg CR tablets | Co-careldopa (Carbidopa/levodopa) |
| 0409010N0BEABAE | Caramet 50mg/200mg CR tablets | Co-careldopa (Carbidopa/levodopa) |
| 0409010K0AAAIAI | Co-beneldopa 12.5mg/50mg capsules | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAAMAM | Co-beneldopa 12.5mg/50mg dispersible tablets sugar free | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAANAN | Co-beneldopa 12.5mg/50mg/5ml oral suspension | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAAJAJ | Co-beneldopa 25mg/100mg capsules | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAALAL | Co-beneldopa 25mg/100mg dispersible tablets sugar free | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAAFAF | Co-beneldopa 25mg/100mg modified-release capsules | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAAHAH | Co-beneldopa 25mg/100mg/5ml oral liquid | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAAPAP | Co-beneldopa 25mg/6.25mg/5ml oral suspension | Co-beneldopa (Benserazide/levodopa) |
| 0409010K0AAAKAK | Co-beneldopa 50mg/200mg capsules | Co-beneldopa (Benserazide/levodopa) |
| 0409010N0AAAAAA | Co-careldopa 10mg/100mg tablets | Co-careldopa (Carbidopa/levodopa) |
| 0409010N0AAAJAJ | Co-careldopa 10mg/100mg/5ml oral suspension | Co-careldopa (Carbidopa/levodopa) |
| 0409010N0AAAYAY | Co-careldopa 10mg/40mg/5ml oral suspension | Co-careldopa (Carbidopa/levodopa) |
| 0409010N0AAADAD | Co-careldopa 12.5mg/50mg tablets | Co-careldopa (Carbidopa/levodopa) |

Showing 20 of 85 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier shown is not in the standard MHRA PL format, so the authorisation details should be verified against the MHRA register. BNF classification and NICE appraisal information were not available in the data compiled.

<!-- review:begin uk-lic-20261106-levodopa-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Only one authorisation is recorded (single-ingredient, valid). The identifier shown is not in the standard MHRA PL format, so the authorisation details should be verified against the MHRA register." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-levodopa-1 -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Only one authorisation is recorded (single-ingredient, valid)" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

