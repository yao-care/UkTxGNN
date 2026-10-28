---
layout: default
title: Methylphenidate
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Methylphenidate: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Attention deficit hyperactivity disorder (ADHD)"
monitor_inn: "Methylphenidate"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "specific developmental disorder", "dysthymic disorder"]
---

# Methylphenidate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Methylphenidate: From Attention Deficit Hyperactivity Disorder to Faciodigitogenital Syndrome
{: .text-alpha }

## One-Sentence Summary

Methylphenidate is a central nervous system stimulant, originally used for attention deficit hyperactivity disorder (ADHD) and narcolepsy.
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome** (Aarskog-Scott syndrome), but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a purely computational signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention deficit hyperactivity disorder (ADHD); narcolepsy (no approved indication text is available in the UK licence record) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Methylphenidate is, however, widely known as a dopamine and norepinephrine reuptake inhibitor, and its efficacy in ADHD is well established.

Faciodigitogenital syndrome is an X-linked developmental disorder in which ADHD-like behavioural features can occur. A symptomatic rationale is therefore conceivable: methylphenidate could treat the attention and hyperactivity symptoms, not the underlying genetic condition. No evidence in the compiled data supports this, and no mechanistic link has been established. The very high TxGNN score should be treated as a hypothesis only.

**Other predictions considered (all lower-ranked):**
- **Chondromyxoid fibroma** (score 0.9999): no plausible mechanistic link. This is a benign cartilage-derived bone tumour, and the score is likely a TxGNN model (deep learning) artefact. No trials or literature (L5, Hold).
- **Specific developmental disorder** (score 0.9999): indirect ADHD-focused literature that largely overlaps with the existing indication (L4, Research Question).
- **Dysthymic disorder** (score 0.9911): indirect evidence from ADHD with comorbid depressive symptoms; no trial of methylphenidate in dysthymia (L4, Research Question).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for faciodigitogenital syndrome.

---

## Literature Evidence

Currently no related literature available for faciodigitogenital syndrome.

For context, the literature retrieved for the related predictions (specific developmental disorder and dysthymic disorder) is indirect. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24045603](https://pubmed.ncbi.nlm.nih.gov/24045603/) | 2013 | Cohort | Clin Neuropharmacol | Effect of methylphenidate on ADHD and mood symptoms in young people with comorbid subsyndromal depression |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Cohort | Prog Neuropsychopharmacol Biol Psychiatry | Longitudinal MRI study of cumulative methylphenidate exposure, brain structure and symptom improvement in youth with ADHD |
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Cohort | Psychiatry Clin Neurosci | Extended-release methylphenidate and dopamine/norepinephrine transporter binding in adults with ADHD (PET study) |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Review | Neuropharmacology | Neurobiology of ADHD |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Review | J Atten Disord | Overview of methylphenidate efficacy, safety and dosing in adult and juvenile brains |
| [14609500](https://pubmed.ncbi.nlm.nih.gov/14609500/) | 2003 | Observational | Curr Psychiatry Rep | Effects of antidepressants, amphetamine and methylphenidate on negative interpersonal perception in depression/dysphoria |

None of these studies addresses faciodigitogenital syndrome.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0404000M0AAAAAA | Methylphenidate HCl Tab 10mg | Not specified | Not specified |

The record is a single-ingredient, valid authorisation. Dosage form and approved indication text are not available in the data compiled for this report. Please check the current MHRA record, SmPC and BNF for authoritative details.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (derived from drug-disease relationships, not from label text), including:
- **Cardiovascular and cerebrovascular:** hypertension, coronary artery disease, myocardial infarction, stroke and cerebral infarction, sudden cardiac arrest, heart conduction disease
- **Psychiatric:** bipolar disorder, psychotic disorders including schizoaffective disorder, substance abuse/dependence, anorexia nervosa
- **Neurological:** epilepsy
- **Haematological:** thrombocytopenia, leukopenia, anaemia, haemoglobinopathy
- **Other:** glaucoma, hyperthyroidism (Graves disease, thyrotoxicosis)

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Major:** bupropion
- **Moderate:** isometheptene, ephedrine, epinephrine, and bowel preparations (polyethylene glycol with electrolytes, sodium picosulfate, sodium sulfate)
- Several others are recorded with an unclassified severity (for example metformin, morphine, omeprazole, pantoprazole, simvastatin, prednisone).

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for faciodigitogenital syndrome rests on a very high TxGNN score alone, with no clinical trials, no literature and no established mechanistic link. The knowledge-graph contraindication profile also includes several common conditions, which warrants caution.

**To proceed, the following is needed:**
- Mechanism of action data for methylphenidate, to support any mechanistic-link analysis
- Published or registered evidence (case series, trials) of methylphenidate for behavioural symptoms in faciodigitogenital syndrome
- Verified label-based warnings and contraindications from the SmPC and BNF, as these are currently missing
- Confirmation of the licensed indications and dosage forms for the UK authorisation
- Independent validation of the TxGNN signal, ideally by clinical review of whether the proposal is a genuine repurposing opportunity or simply symptomatic ADHD treatment within an existing licensed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

