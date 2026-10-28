---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 297
evidence_level: L5
indication_count: 9
monitor_inn: "Fluoxetine"
predicted_indications: ["paranoid personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "schizotypal personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "manic bipolar affective disorder", "phobic disorder", "Ohdo syndrome and variants"]
last_modified_at: 2026-10-23
description: "Fluoxetine: predicted new indication Paranoid personality disorder (evidence level L5). Approved use: Relations recorded in the knowledge graph : major depressive disorder…"
---

# Fluoxetine
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

## Fluoxetine: From Major Depressive Disorder to Paranoid Personality Disorder
{: .text-alpha }

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) with known uses in depressive, anxiety, obsessive-compulsive and eating disorders. The TxGNN model (deep learning) predicts it may be useful in **paranoid personality disorder**, but **no clinical trials** and only **7 publications** were found, none of which tests fluoxetine in this condition. The prediction currently rests on the model score alone, which may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph (not licence text): major depressive disorder, bulimia nervosa, obsessive-compulsive disorder, anxiety disorder, bipolar disorder and others. The UK licence record compiled for this report contains no indication text. |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Fluoxetine is known as an SSRI. Its efficacy in depression and related conditions is recorded in the knowledge graph. Mechanistically, it may plausibly apply to the anxiety, mood and impulsivity symptoms that often co-occur with personality disorders.

Paranoid personality disorder belongs to the cluster A personality disorders, which also include schizoid and schizotypal disorders. Serotonergic modulation could affect some of the associated symptoms. However, no study identified here tests fluoxetine specifically in paranoid personality disorder. The available literature consists of reviews and comorbidity studies. These cover borderline personality disorder, depression with coexisting personality disorders, and a general review of drug treatment in cluster A disorders. The very high TxGNN score is a computational prediction, not clinical evidence.

**Evidence level reasoning:** The pack's own scoring lists L4. Under the evidence rules, L1 to L4 require a study that directly addresses the predicted disease itself. The cluster A review is about drug treatment in this group of disorders but provides no fluoxetine-specific data for paranoid personality disorder. The evidence level is therefore L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | Reviews drug treatment in cluster A personality disorders (paranoid, schizoid, schizotypal). These patients tend to be isolated and have reduced quality of life. |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review | JAMA | Review of borderline personality disorder, a different personality disorder. It affects about 0.7% to 2.7% of US adults and is linked to marked social and work impairment. |
| [12524634](https://pubmed.ncbi.nlm.nih.gov/12524634/) | 2003 | Cohort | Comprehensive Psychiatry | Among 183 depressed patients in a randomised fluoxetine versus nortriptyline trial, 30 had borderline personality disorder. They had earlier, more chronic depression and more suicide attempts. |
| [12214786](https://pubmed.ncbi.nlm.nih.gov/12214786/) | 2002 | Review | Psychological Medicine | Assessed personality disorder diagnoses in depressed outpatients before and after fluoxetine, looking at whether diagnostic change tracked depressive improvement. |
| [17637578](https://pubmed.ncbi.nlm.nih.gov/17637578/) | 2000 | Cohort | CNS Spectrums | Social anxiety and premorbid personality disorders in paranoid schizophrenia patients treated with clozapine. This is a different condition and drug. |
| [21371699](https://pubmed.ncbi.nlm.nih.gov/21371699/) | 2011 | Cohort | Comprehensive Psychiatry | Compared characteristics of depression starting in childhood, adolescence or adulthood. Not specific to this indication. |
| [26703328](https://pubmed.ncbi.nlm.nih.gov/26703328/) | 2016 | Review | J Dev Behav Pediatr | Case-based discussion of psychiatric diagnoses in polycystic ovarian syndrome. Not specific to this indication. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form |
|---------|------|------|
| 0403030E0AAAAAA (identifier as listed; it is not in PL number format) | Fluoxetine hydrochloride capsules 20 mg | Capsule (taken from the product name) |

No approved indication text, dosage form field or manufacturer is recorded in the licence data compiled for this report. This is a single-ingredient product.

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (these come from graph relations, not label text, and must be checked against the SmPC): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver failure and liver disease, cirrhosis, epilepsy, bipolar disorder and major affective disorder, gallbladder disease, diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, benign prostatic hyperplasia, neutropenia, agranulocytosis, blood coagulation disease, hyperlipidaemia and hypertriglyceridaemia, obesity disorders, female breast carcinoma, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction and coronary thrombosis.
- **Drug interactions:** 100 interactions were recorded, and 20 were available for review. The **Major** ones are bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and cisapride. Moderate interactions include aspirin, morphine, clarithromycin, famotidine, loperamide, several laxatives and sulfonylureas (chlorpropamide, acetohexamide).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There are no registered trials and no fluoxetine-specific studies in paranoid personality disorder, so the evidence level is L5 and the high score is a model prediction only.

**To proceed, the following is needed:**
- Mechanism of action data to support the proposed link.
- Fluoxetine-specific clinical studies in paranoid personality disorder, or at least in cluster A personality disorders.
- Review of the SmPC warnings and contraindications, which are missing from the data compiled for this report.
- A UK licence indication text and dosage form record.

**Note on other predictions:** Other predicted indications in the same data have stronger support and may be better priorities to evaluate. Agoraphobia has literature on panic disorder, including a network meta-analysis and fluoxetine-specific studies. Phobic disorder has a completed Phase 3 trial in childhood social phobia, though the fluoxetine arm needs confirming.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

