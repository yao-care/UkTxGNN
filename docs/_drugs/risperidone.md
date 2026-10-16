---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Risperidone: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). Approved use: Schizophrenia, bipolar disorder, autism spectrum disorder"
---

# Risperidone
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

# Risperidone: From Schizophrenia and Bipolar Disorder to Familial Horizontal Gaze Palsy with Progressive Scoliosis

## One-Sentence Summary

Risperidone is an atypical antipsychotic originally used for schizophrenia, bipolar disorder and irritability associated with autism.
The TxGNN model predicts it may be effective for **familial horizontal gaze palsy with progressive scoliosis** (an ultra-rare genetic disorder), but there are **no clinical trials and no publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, bipolar disorder, autism spectrum disorder (from the knowledge graph; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Risperidone is known to act mainly by blocking dopamine D2 and serotonin 5-HT2A receptors, and its efficacy in schizophrenia, bipolar disorder and autism-related irritability is established.

The predicted condition is an ultra-rare genetic disorder (ROBO3-related) of hindbrain axon guidance. It involves abnormal eye movements and progressive scoliosis. D2/5-HT2A antagonism has no plausible bearing on this pathophysiology, and no mechanistic link could be identified.

The very high TxGNN score most likely reflects proximity to neurodevelopmental terms in the knowledge graph rather than a real therapeutic signal. The prediction should therefore be treated as a model artefact unless independent evidence emerges.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 040201030AAAAAA (as recorded; not in standard MHRA PL format) | Risperidone tablets 1 mg | Tablet | Not stated in the licence record |

The record shows one valid single-ingredient authorisation. Dosage form is inferred from the product name, and no approved indication text is available. Verify the authorisation details against the MHRA database, the SmPC and the BNF before any further work.

## Safety Considerations

- **Contraindications and cautions flagged in the knowledge graph** (these come from drug-disease relationship data, not from label text, and should be checked against the SmPC):
  - **Cardiovascular and cerebrovascular:** heart disease, cardiovascular disease, heart conduction disease, myocardial infarction, sudden cardiac arrest, stroke and cerebrovascular disorder, cerebral infarction, hypotensive disorder, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy.
  - **Metabolic:** diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, hyperlipidaemia (including familial), obesity (including monogenic).
  - **Haematological:** neutropenia, agranulocytosis, haemoglobinopathy.
  - **Hepatic and biliary:** liver disease, liver failure, gallbladder disease.
  - **Other:** epilepsy, female breast carcinoma.
- **Drug interactions** (100 interactions were identified; the data compiled for this report list 20, including the following):
  - **Major:** bupropion, morphine.
  - **Moderate:** acarbose, metformin, alogliptin, albiglutide, canagliflozin, famotidine, epinephrine, hydrocortisone, amphotericin B (including lipid complex), atropine, hyoscyamine, glycopyrronium, clidinium, loperamide, lorcaserin, bisacodyl.
  - **Minor:** ranitidine.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and no plausible mechanistic link to a disorder of axon guidance. Risperidone also carries substantial cardiometabolic and neurological cautions. There is no basis to progress this indication.

**To proceed, the following is needed:**
- Independent preclinical or mechanistic evidence linking D2/5-HT2A antagonism to the disease biology
- Any published case-level or clinical data in patients with this condition
- Verified MHRA authorisation details (indication text, dosage form, PL number)

**Note on other predictions in the data compiled for this report:** the first-ranked prediction above is the weakest. Other candidates have more substantial support, notably adjunctive use in treatment-resistant **major affective (depressive) disorder**. That candidate has two completed Phase 3 trials (NCT00095134, n=630; NCT00044681, n=258) plus systematic reviews and meta-analyses, and is assessed as L1 with a "Proceed with Guardrails" recommendation. If the aim is to find a viable repurposing direction for risperidone, a separate report on that indication would be the more productive next step.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

