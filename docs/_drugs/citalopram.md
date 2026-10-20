---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Citalopram: predicted new indication Obsessive-compulsive disorder (evidence level L5). Approved use: Major depressive disorder, unipolar and endogenous depression…"
monitor_inn: "Citalopram"
predicted_indications: ["obsessive-compulsive disorder", "paranoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder"]
---

# Citalopram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Citalopram: From Depression and Anxiety Disorders to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI), originally used to treat depressive and anxiety disorders.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**,
with **4 clinical trials** (none citalopram-specific) and **16 publications** currently supporting this direction, mostly open-label studies and reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder, unipolar and endogenous depression, dysthymic disorder, anxiety disorder, neurotic disorder (from the TxGNN knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 (see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The compiled data assign L2. However, the only Phase 3 trial is not citalopram-specific, and direct citalopram evidence is limited to open-label studies and case series. The evidence is better described as lower-than-L2 for citalopram itself, and the decision below should be read with that in mind.

## Why is This Prediction Reasonable?

Detailed mechanism of action data for citalopram are not available in the data compiled for this report. Citalopram is, however, a well-characterised SSRI. Its effect in depression and anxiety is attributed to increased serotonergic neurotransmission.

Serotonergic dysfunction in cortico-striato-thalamo-cortical circuits is implicated in OCD, and SSRIs are an established first-line drug class for the disorder. Depression, anxiety and OCD frequently co-occur and respond to overlapping pharmacology, which is consistent with the very high TxGNN score.

Direct citalopram evidence is more modest. It consists of open-label paediatric and adult studies and a treatment-resistant case series. No confirmed citalopram-specific Phase 3 RCT is present in the data compiled.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Cognitive behavioural therapy added to serotonin reuptake inhibitor treatment in children with OCD who partially responded. Citalopram is not clearly the specific intervention, so the link is indirect. |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Exposure and response prevention, SSRIs, and their combination in OCD, with predictors of response in a Chinese population. Not citalopram-specific. |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Group CBT compared with fluoxetine in OCD. Indirect SSRI-class evidence only. |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | Not applicable | Completed | 43 | Pilot study of gut microbiota in OCD versus healthy controls, with 12 weeks of open-label SSRI treatment. Not an efficacy trial. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Randomised open-label trial (n=16) | Eur Psychiatry | Citalopram alone versus with clomipramine in treatment-resistant OCD |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Single-blind study | J Clin Psychopharmacol | Compared the antiobsessional efficacy of fluvoxamine, paroxetine and citalopram |
| [9395151](https://pubmed.ncbi.nlm.nih.gov/9395151/) | 1997 | Open pilot study | Acta Psychiatr Scand | 24-week open study of citalopram in OCD |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Cohort (preliminary) | CNS Drugs | Relationship between citalopram concentrations and clinical response in OCD |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label | Psychiatry Clin Neurosci | 8-week study of citalopram (mean 24 mg/day) in 15 children and adolescents with OCD |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Open trial | J Child Adolesc Psychopharmacol | 23 young people treated for 10 weeks; significant improvement in Y-BOCS/CY-BOCS scores (30 to 21) |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review/Commentary | Int Clin Psychopharmacol | Reviews citalopram for OCD |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clin Evid | Overview of OCD epidemiology, course and treatment |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Review | Curr Med Chem | Past, present and future drugs for OCD, with SSRIs central to treatment |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | Serotonin and other mechanisms in OCD |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0403030Z0AAAAAA (BNF-style product code; no PL number available) | Citalopram HCl oral drops 40 mg/ml, sugar-free | Oral drops | Not available in the data compiled |

This is a single-ingredient product with valid status. The code appears to sit within BNF section 4.3.3 (selective serotonin re-uptake inhibitors). Approved indication wording was not available, so licensed use in OCD should be checked against the current SmPC.

## Safety Considerations

**Contraindications and conditions flagged in the knowledge graph** (these come from drug-disease relationships, not product label text, so verify against the SmPC):
- Cardiac: long QT syndrome (including familial), torsades de pointes, heart disease, cardiovascular disease
- Neurological and psychiatric: epilepsy, bipolar disorder, major affective disorder
- Metabolic and organ: liver disease, gallbladder disease, potassium deficiency, blood coagulation disease
- Syndromes: serotonin syndrome, neuroleptic malignant syndrome, inappropriate ADH secretion, nephrogenic syndrome of inappropriate antidiuresis

**Drug interactions** (100 recorded; examples of the Major level shown):
- Bupropion, omeprazole, cimetidine, clarithromycin
- Cisapride, dolasetron (QT-related concern)
- Lorcaserin, dexfenfluramine, diethylpropion (serotonergic or related concern)

Moderate-level interactions include morphine, acetylsalicylic acid (bleeding risk), famotidine and loperamide. Check the full list in the BNF before prescribing.

Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
SSRIs are an established first-line drug class for OCD, and citalopram has consistent but small open-label evidence in adults and children. There is no confirmed citalopram-specific RCT in the data compiled, so confidence is moderate and should not be treated as equivalent to Phase 3 confirmation.

The other predicted indications (paranoid, schizotypal, histrionic and schizoid personality disorders) have no supporting trials and little or no relevant literature, so they are graded **Hold**.

**To proceed, the following is needed:**
- Citalopram-specific randomised controlled trial evidence in OCD (or a review of existing placebo-controlled data)
- Confirmation of the licensed indications from the current SmPC and NICE guidance
- Mechanism of action data for citalopram
- Review of QT prolongation risk, including ECG and electrolyte monitoring, and of interacting drugs
- Dose and safety considerations for children and adolescents, given the paediatric studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

