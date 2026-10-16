---
layout: default
title: Zonisamide
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Zonisamide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Epilepsy"
---

# Zonisamide
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

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

Zonisamide is an antiseizure medication marketed in the UK, and its original use is in epilepsy.
The TxGNN model predicts it may be effective for **Tourette syndrome** with a very high score, but **no clinical trials and no directly relevant publications** support this prediction.
The only related signal found is a review reporting that antiseizure medications can induce tic disorders.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the licence indication text was not recorded in the data compiled for this report) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, zonisamide blocks voltage-gated sodium channels and T-type calcium channels, and it is thought to have weak dopaminergic and serotonergic effects. Its efficacy in epilepsy is established, and these actions could plausibly modulate the neural circuits involved in tics.

This link is **speculative**. The high TxGNN score is a computational prediction from a knowledge graph and is not clinical evidence. The mechanistic reasoning has not been tested in Tourette syndrome. One review found during the evidence search (PMID 36005856) points the other way, as it describes antiseizure medication-induced obsessive-compulsive and tic disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Tourette syndrome.

The review "Antiseizure medication-induced obsessive-compulsive disorder and tic disorder: a pragmatic review" ([36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/), *Expert Review of Neurotherapeutics*, 2022) was retrieved under a different indication. It does not support efficacy, and it raises a possible safety signal for tic symptoms with antiseizure medications.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010ADAAAAAA | Zonisamide capsules 100 mg | Capsule | Not stated in the data compiled |

This identifier follows the BNF classification code format rather than a standard PL number, so verify it against the MHRA register. BNF chapter 4.8.1 covers antiepileptic drugs. The licence indication text and NICE-appraised indications were not available in the data compiled.

---

## Safety Considerations

**Knowledge-graph contraindication signals.** These come from drug-disease contraindication links in the TxGNN knowledge graph (PrimeKG), not from SmPC label text, and they need confirmation against the SmPC. The conditions flagged include:
- Kidney disease and nephrolithiasis, including acute urate nephropathy
- Liver disease and gallbladder disease
- Metabolic acidosis and acidosis disorders
- Neutropenia, agranulocytosis, and related congenital neutropenia syndromes
- Psychiatric conditions, including anxiety disorder, psychotic disorder, schizoaffective disorder, schizophreniform disorder, dysthymic disorder, neurotic disorder, and mental disorder broadly
- Diarrhoeal disease

**Drug interactions.** The interaction query returned 100 records, and the first 20 are summarised here.
- **Major:**
  - Metformin
  - Anticholinergic agents: atropine, hyoscyamine, scopolamine, methscopolamine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, propantheline
- **Moderate:** aprepitant, morphine, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, miconazole

**Indication-specific signals** (from other predicted indications in the same dataset):
- A case report of zonisamide-induced mania (PMID 2109869).
- The tic disorder review above.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no registered trials or supporting publications, and the only related literature suggests antiseizure medications may provoke tics. The mechanistic argument is plausible but unproven.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer mechanistic rationale for tic suppression
- A systematic literature search specific to zonisamide in Tourette syndrome and tic disorders, including any case series
- Review of the SmPC warnings and contraindications, which were not available in the data compiled
- Confirmation of the UK licence number, dosage form, and approved indication
- Preclinical or small exploratory clinical data before any formal trial is considered

**Other predictions to consider.** Several other predicted indications in the dataset have more supporting evidence, though none has registered trials supporting efficacy.
- **Absence epilepsy** (L3) has the strongest evidence. It has a clear T-type calcium channel rationale and zonisamide-specific reports (PMIDs 15847848 and 24907183), and these are likely small or retrospective studies.
- **Manic bipolar affective disorder** (L4) has indirect literature, including a pilot study in bipolar depression and a report of zonisamide-induced mania.
- **Fibromyalgia** (L4) has one withdrawn trial with zero enrolment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

