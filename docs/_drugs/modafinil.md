---
layout: default
title: Modafinil
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Modafinil: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Narcolepsy (including narcolepsy with cataplexy)"
monitor_inn: "Modafinil"
predicted_indications: ["insomnia (disease)"]
---

# Modafinil
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

# Modafinil: From Narcolepsy to Insomnia

## One-Sentence Summary

Modafinil is a wake-promoting medicine, originally used to treat narcolepsy and excessive daytime sleepiness.
The TxGNN model predicts it may be relevant to **insomnia**, but the link is indirect, supported by only **2 small clinical trials** (one terminated with 2 participants) and **no publications directly demonstrating efficacy in insomnia**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy (including narcolepsy with cataplexy) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction with only very weak supporting studies) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Modafinil is generally understood to promote wakefulness through dopamine transporter inhibition and effects on wake-promoting brain circuits. It is established for excessive daytime sleepiness, not for inducing sleep.

The link to insomnia is indirect and partly paradoxical. Modafinil can worsen insomnia as an adverse effect. The very high TxGNN score most likely reflects the drug's closeness to sleep-wake disorders in the knowledge graph (narcolepsy, shift work sleep disorder, sleep disturbance in neurological disease) rather than a true therapeutic effect on insomnia.

Any plausible benefit would be limited to daytime function and sleep/wake regulation in specific groups, such as older adults, people with Parkinson's disease, or those with neurological conditions and fatigue. It would not extend to primary insomnia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Modafinil for sleep/wake disturbances in older adults. Terminated after only 2 participants, so no interpretable results. |
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | Effects of modafinil, alone or with cognitive behavioural therapy for insomnia (CBT-I), on daytime functioning and insomnia severity. Small study with no results provided, so it does not establish efficacy. |

---

## Literature Evidence

None of the publications below tests modafinil for insomnia directly. They concern related sleepiness and fatigue conditions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic review/meta-analysis | PloS one | Assessed modafinil for fatigue and excessive daytime sleepiness in neurological disorders; earlier trials gave inconsistent results. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic review/meta-analysis | Parkinsonism & related disorders | Pharmacological options for daytime sleepiness and sleep disorders in Parkinson's disease; few clinical trials available. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review | Drugs | Evidence-based review of approved and investigational uses of modafinil, based on placebo-controlled trials. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Review | Movement Disorders | Movement Disorder Society evidence review of treatments for non-motor symptoms of Parkinson's disease. |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | Expert Opinion on Pharmacotherapy | Management of sleep disturbances in Parkinson's disease. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Burden and management of shift work sleep disorder. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case series | Am J Hosp Palliat Care | Modafinil reduced fatigue in Charcot-Marie-Tooth disease type 1A. |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Revue neurologique | Overview of narcolepsy with cataplexy, including sleep maintenance insomnia as a feature. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0404000R0AAAAAA | Modafinil Tab 100mg | Not specified | Not specified |

One valid single-ingredient authorisation is recorded. Dosage form and approved indication text are not available in the compiled data, so please check the current SmPC, the BNF and any relevant NICE guidance.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from drug-disease network links, not from product label text, and need verification against the SmPC):
- Cardiovascular: hypertension, acute coronary syndrome, myocardial infarction, myocardial ischaemia, coronary artery disease, mitral valve prolapse, postural orthostatic tachycardia syndrome
- Psychiatric: anxiety disorder, psychotic disorder, schizoaffective disorder, dysthymic disorder, substance abuse/dependence, and mental disorders in general
- Other: liver failure, haemoglobinopathy

**Drug interactions** (100 recorded in total; examples from the first 20 shown):
- Moderate: omeprazole, esomeprazole, rabeprazole, dexamethasone, cisapride, eliglustat, linagliptin
- Minor: hydrocortisone, pioglitazone, aprepitant, cimetidine, clarithromycin, and others

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by relevant clinical evidence. The only insomnia-related trials are one terminated study (2 participants) and one small study without reported results. Modafinil is a wake-promoting drug that can itself worsen insomnia, so the prediction is best treated as a research question rather than a treatment opportunity.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer rationale for any benefit in insomnia
- Published results from NCT00124384, or new well-designed randomised trials in a defined population (for example, older adults or people with neurological disease and daytime impairment)
- Full UK licence details (dosage form, approved indication) and the SmPC warnings and contraindications
- A safety review covering the cardiovascular and psychiatric signals above and the interaction profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

