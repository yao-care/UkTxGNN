---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Risperidone: From Schizophrenia to Major Affective Disorder

## One-Sentence Summary

Risperidone is an atypical antipsychotic originally developed for schizophrenia, acting through dopamine D2 and serotonin 5-HT2A receptor antagonism to reduce psychotic symptoms.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (encompassing bipolar disorder and treatment-resistant major depression), the highest-evidence prediction across six candidate indications in this analysis.
This direction is currently supported by **36 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs and a Cochrane systematic review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia (data not retrieved from dataset; based on established clinical knowledge) |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| UK Market Status | No marketing authorisation records found in current dataset |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note for clinicians**: The regulatory data in this Evidence Pack appears to originate from a Taiwan FDA source and may not accurately reflect current MHRA authorisation status. Risperidone (Risperdal® and generics) is in fact authorised and widely used in the United Kingdom. All prescribing decisions must be based on current MHRA records, the relevant SmPC, and BNF guidance.

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrieved via the automated DrugBank query for this Evidence Pack. However, based on established pharmacology, Risperidone is a second-generation (atypical) antipsychotic characterised by potent antagonism at dopamine D2 and serotonin 5-HT2A receptors, with additional activity at D3, D4, α1/α2-adrenergic, and H1 histamine receptors. The drug's 5-HT2A:D2 antagonism ratio — higher than typical antipsychotics — underpins its improved tolerability and broader spectrum of action beyond psychosis alone.

Major affective disorder encompasses bipolar I/II disorder and treatment-resistant major depressive disorder (TRD), both characterised by dysregulation of the monoaminergic systems that Risperidone modulates. In mania, hyperdopaminergic activity within the mesolimbic circuit drives elevated mood and impulsivity; D2 blockade directly attenuates this state. In TRD, failure to respond to serotonin reuptake inhibition may reflect insufficient serotonergic post-synaptic signalling; Risperidone's 5-HT2A antagonism disinhibits serotonin release and enhances the effect of co-administered SSRIs or SNRIs — a strategy termed augmentation therapy. The partial 5-HT1A agonism further addresses anxiety comorbidity prevalent in affective disorders.

The TxGNN prediction is well-supported by a substantial clinical evidence base. Multiple completed Phase 3 RCTs directly tested Risperidone in bipolar I disorder (NCT00391222, n=585; NCT00057681, n=379) and in TRD augmentation (NCT00095134, n=630; NCT00044681, n=258). A Cochrane systematic review (PMID 21154393) and recent network meta-analyses confirm Risperidone's position among second-generation antipsychotics used in major depression. Collectively, this mechanistic plausibility combined with robust Phase 3 data provides the strongest justification for the L1 evidence designation across all six TxGNN predictions in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Double-blind, placebo-controlled multicentre RCT evaluating Risperidone LAI monotherapy vs placebo for prevention of mood episode recurrence in Bipolar I disorder; oral olanzapine used as active validity comparator |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind RCT: adjunctive Risperidone vs placebo in MDD with sub-optimal response to antidepressant therapy; one of the largest Phase 3 augmentation trials specifically for TRD |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | TEAM (Treatment of Early Age Mania) study: three-arm comparison of lithium, valproate, and Risperidone for mania in children and adolescents with bipolar disorder |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Phase 3 RCT assessing efficacy, safety, and long-term maintenance effect of Risperidone augmentation of SSRI monotherapy in treatment-resistant depression (young and older adults) |
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | Completed | 453 | Double-blind, placebo-controlled Phase 3 RCT of Licarbazepine adjunctive to atypical antipsychotics (including Risperidone) for acute manic episodes in Bipolar I disorder |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Phase 3 RCT with multimodal MRI assessment comparing Risperidone vs Divalproex Sodium for paediatric bipolar disorder; examined neural circuit changes pre- and post-treatment |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Double-blind, placebo-controlled trial: Risperidone monotherapy in ambulatory bipolar disorder with comorbid moderately severe anxiety and lifetime panic or generalised anxiety disorder |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Completed | 46 | Preliminary controlled Phase 3 trial of Valproate vs Risperidone in young children (aged 3–7 years) with bipolar disorder; provides characterisation data for very early-onset cohort |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Double-blind pilot RCT directly comparing Risperidone vs Olanzapine as add-on to a failed SSRI in treatment-resistant depression; evaluated relative efficacy and tolerability |
| [NCT00571688](https://clinicaltrials.gov/study/NCT00571688) | Phase 4 | Completed | 50 | Phase 4 RCT: Risperidone Consta (LAI) every 2 weeks vs treatment as usual for prevention of symptomatic relapse and rehospitalisation in bipolar disorder |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Network Meta-analysis | J Affect Disord | Systematic review and NMA comparing augmentation agents in adult TRD; provides head-to-head indirect comparisons of Risperidone against other SGA and non-SGA augmentation strategies |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review / Meta-analysis | Psychological Medicine | Comprehensive meta-analysis examining antipsychotics as both monotherapy and adjunctive therapy in MDD; first to cover both treatment modalities in a single analysis |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Systematic Review | Cochrane Database Syst Rev | Cochrane review of second-generation antipsychotics for MDD and dysthymia; evaluates whether addition of antipsychotics to antidepressants induces remission; includes Risperidone data |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review / Meta-analysis | J Psychopharmacol | Meta-analysis of augmentation and combination approaches for early-stage TRD; assesses current evidence for concomitant pharmacological strategies in the ~50% of MDD patients who fail first-line treatment |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Systematic Review / Meta-analysis | J Psychopharmacol | Comparative analysis of SGAs (including Risperidone), esketamine, and lithium as combination treatments for MDD; evaluates relative efficacy and tolerability across compound classes |
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Ann Intern Med | Risperidone for treatment-refractory MDD: multicentre randomised trial; published in a high-impact general medicine journal; provides pivotal direct efficacy evidence for TRD augmentation |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Population-based Study | J Clin Psychiatry | Nationwide population-based study comparing aripiprazole, olanzapine, quetiapine, and Risperidone augmentation for MDD using Taiwan National Health Insurance data; real-world effectiveness evidence |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | Meta-analysis of 17 RCTs (n=3,807 participants) assessing efficacy and tolerability of antidepressant augmentation with atypical antipsychotics; includes Risperidone-specific subgroup data |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Review | Ann Pharmacother | Targeted review of Risperidone as augmentation for MDD; evaluates evidence specifically for patients who fail adequate antidepressant monotherapy |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Review / Treatment Guideline | Acta Psychiatr Scand | Evidence-based treatment review for bipolar mania with clinical recommendations on selection of mood stabilisers and antipsychotics, including Risperidone; supports clinical positioning |

---

## UK Market Information

No marketing authorisation records were returned for Risperidone in the current dataset (0 registered licences).

> **Important data quality notice**: This dataset reports zero MHRA licences for Risperidone, which does not reflect the actual UK market. Risperidone has long-standing MHRA authorisations under the brand name Risperdal® (Janssen-Cilag) and as multiple generic products. UK-authorised indications include schizophrenia, moderate to severe manic episodes associated with bipolar disorder, and short-term treatment of aggression in patients with Alzheimer's dementia (under specific conditions). Clinicians must consult the current MHRA Product Licence Register and the relevant SmPC directly. BNF section 4.2.1 (Antipsychotic drugs) provides prescribing guidance. The regulatory data in this Evidence Pack requires urgent verification before use in any formulary or commissioning decision.

---

## Safety Considerations

No safety data were retrieved by the automated evidence collection system for this analysis (all fields returned as data gaps with no active drug–drug interaction records identified).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

> **Attention**: Risperidone has a well-characterised safety profile that clinicians must independently review prior to any prescribing or policy decision. Key areas of concern include extrapyramidal symptoms (particularly at higher doses), metabolic effects (weight gain, dyslipidaemia, hyperglycaemia, new-onset diabetes), hyperprolactinaemia, QTc prolongation, cerebrovascular events (particularly in elderly patients with dementia, where Risperidone carries an MHRA black triangle warning and a restricted indication), orthostatic hypotension, and neuroleptic malignant syndrome. Monitoring requirements (FBC, lipids, fasting glucose, weight, blood pressure, and prolactin) should be reviewed in the current SmPC.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs, a Cochrane systematic review, and several network meta-analyses establish L1 evidence for Risperidone in major affective disorder (bipolar I disorder and treatment-resistant depression), and the mechanistic rationale — D2 and 5-HT2A receptor modulation directly addressing monoaminergic dysregulation in affective illness — is well-founded. However, Risperidone is not a novel repurposing candidate in the classic sense; this analysis primarily quantifies and consolidates evidence for a use pattern already established in clinical practice.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current MHRA authorisation status and licensed indications; the dataset shows 0 UK licences, which is inconsistent with known market reality and must be corrected before any regulatory pathway work
- **Full SmPC safety review**: Comprehensive assessment of contraindications, drug interactions (particularly with QTc-prolonging agents, CYP2D6 inhibitors, and CNS depressants), and special population guidance (elderly, pregnancy, renal/hepatic impairment)
- **Indication scoping**: Define whether the target is bipolar I mania, bipolar maintenance, TRD augmentation, or all three — as evidence strength, approved populations, and monitoring requirements differ across these sub-indications
- **NICE guidance alignment**: Review NICE CG185 (Bipolar Disorder in Adults), NICE CG90 (Depression in Adults), and any relevant Technology Appraisals to determine if a formal commissioning or formulary process is required
- **Pharmacoeconomic assessment**: If the intent is to commission a new or expanded formulary indication, a cost-effectiveness analysis aligned with NHS England / NHSE Midlands formulary standards will be required
- **Formal MOA data retrieval**: Obtain full DrugBank record and SmPC pharmacodynamics section to complete the mechanistic evidence file

---

*This report is generated for research and informational purposes only. It does not constitute clinical advice, a prescribing recommendation, or a regulatory submission. All repurposing candidates require formal clinical validation before therapeutic application. This document should be read in conjunction with current MHRA authorisation data, BNF guidance, and applicable NICE technology appraisals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

