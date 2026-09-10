---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Haloperidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Haloperidol: From Schizophrenia to Manic Episode of Bipolar Disorder

## One-Sentence Summary

Haloperidol is a first-generation antipsychotic classically used to treat schizophrenia and other psychotic disorders. Among ten TxGNN-predicted indications reviewed for this candidate, only one — **manic episode of Bipolar Affective Disorder** — is supported by real-world clinical evidence (**9 clinical trials** and **20 publications**), with **3 completed Phase 3 RCTs** using haloperidol as an active comparator. The other nine higher-ranked TxGNN predictions (e.g. congenital glycosylation disorders, X-linked myopia, hydranencephaly) were explicitly flagged in the evidence pack as lacking any plausible mechanistic link and are treated as likely knowledge-graph embedding noise; they are not carried forward in this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / psychotic disorders (general drug-class knowledge; no `original_indications` or UK licence text was present in this evidence pack) |
| Predicted New Indication | Manic episode of Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| UK Market Status | Not marketed (per this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Screening note:** the evidence pack ranked nine other candidate indications higher by raw TxGNN score (0.9986–0.9991), but each carries an explicit rationale of "no mechanistic link" / "likely false positive from sparse-node embedding noise" and zero supporting trials or literature (Evidence Level L5, decision stage S0, Hold). Manic Bipolar Affective Disorder, despite a marginally lower TxGNN score, is the only prediction with a coherent mechanism and independent clinical evidence, so it is the sole indication evaluated in detail below.

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Haloperidol was flagged as a data gap in this evidence pack (DG002). However, the repurposing rationale attached to this prediction supplies the relevant pharmacology: Haloperidol is a potent D2 dopamine receptor antagonist (with additional D1, α1-adrenergic and sigma receptor activity). The dopamine hypothesis of mania holds that acute manic episodes involve dopaminergic hyperactivity, and D2 blockade is the core pharmacological basis by which antipsychotics relieve manic symptoms.

Both the drug's classical use (psychotic disorders) and the predicted new use (bipolar mania) are CNS/psychiatric conditions sharing overlapping dopaminergic pathophysiology, which is consistent with Haloperidol's long-standing off-label and guideline-supported use in acute mania alongside mood stabilisers.

It is important to note, however, that this is **not a genuinely novel indication**: Haloperidol has been used clinically for acute mania/bipolar disorder for decades and appears as an active comparator or add-on therapy across multiple international guidelines and trials. The evidence here should be read as **confirmation of an established use** rather than a new pharmacological hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs placebo vs Haloperidol in manic episodes of Bipolar I disorder; Haloperidol used as active comparator, assessing 12-week maintenance of effect versus Risperidone. |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs placebo vs Haloperidol as add-on therapy to mood stabilisers for manic episodes of bipolar disorder. |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Placebo- and Haloperidol-controlled trial of Olanzapine in manic or mixed episodes of Bipolar I disorder; confirms Olanzapine efficacy with Haloperidol as active comparator arm. |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic plus adherence-focused behavioural programme for chronic psychotic disorders in Tanzania; covers manic-spectrum patients but Haloperidol not the primary intervention. |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A (observational) | Recruiting | 200 | Observational study of antenatal antipsychotic exposure (may include Haloperidol) on maternal psychiatric course and infant development; safety-relevant, not an efficacy trial. |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate-Amisulpride vs Valproate-Haloperidol in bipolar I manic episode; Haloperidol included as the comparator combination arm. |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient/fish-oil supplementation as adjunct in bipolar disorder; no direct Haloperidol arm, low relevance. |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs placebo in acute mania; Haloperidol not an intervention arm, disease-area relevance only. |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs conventional antipsychotics (cost/efficacy) in acute mania in Sweden; terminated early, small sample, Haloperidol not clearly an arm. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomised, double-blind, placebo- and Haloperidol-controlled study confirming Olanzapine efficacy/safety in Japanese patients with manic/mixed Bipolar I episodes. |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Archives of General Psychiatry | Double-blind controlled trial of lithium plus Haloperidol vs placebo plus Haloperidol in excited schizo-affective patients; modest but significant benefit of combination. |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | Journal of Clinical Psychiatry | Double-blind controlled comparisons of clonazepam vs lithium vs Haloperidol in acute mania. |
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic Review / Network Meta-analysis | Molecular Psychiatry | Network meta-analysis of double-blind RCTs comparing efficacy, tolerability and safety of pharmacological treatments (including Haloperidol) for acute bipolar mania. |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Review | BMJ Mental Health | Compares antipsychotic dose equivalents (including Haloperidol) between acute mania and schizophrenia. |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based review of mania treatment options, including antipsychotic choice. |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Refractory bipolar disorder review; recommends adding Haloperidol, risperidone, olanzapine, quetiapine or aripiprazole to partial responders on lithium/valproate/carbamazepine. |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | Journal of Clinical Psychopharmacology | Systematic review of antipsychotic-induced extrapyramidal side effects in bipolar disorder and schizophrenia, relevant to Haloperidol's tolerability profile. |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | Retrospective Study | Journal of Affective Disorders | Retrospective analysis of long-acting injectable antipsychotics added during manic episodes and impact on rehospitalisation. |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Mechanistic Study | Neuropsychobiology | Compares lithium vs lithium+Haloperidol effects on leukocyte Gαs protein levels in bipolar affective disorder, exploring downstream signalling mechanisms. |

---

## UK Market Information

No UK marketing authorisation records are present in this dataset for Haloperidol (market status recorded as "Not marketed", 0 licences on file as of the 2026-08-31 data cutoff). This should be independently verified against the current MHRA product register and BNF before any regulatory conclusions are drawn, since Haloperidol is a long-established molecule and the absence of a licence record here may reflect a data-collection gap (see Conclusion, "To proceed" list) rather than genuine unavailability.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs (NCT00253162, NCT00253149, NCT00129220) using Haloperidol as an active comparator, plus a 2022 network meta-analysis of RCTs in acute bipolar mania, together meet the L1 evidence bar. This is not a novel pharmacological hypothesis but confirmation of an already-established clinical use, so guardrails should focus on formalising the safety and regulatory picture rather than proof-of-concept.

**To proceed, the following is needed:**
- TFDA/MHRA SmPC warnings, contraindications and drug-interaction data (currently a Blocking data gap, DG001) before any Stage 1 safety assessment can proceed
- Formal, sourced mechanism-of-action documentation for Haloperidol (DG002)
- Verification of current UK marketing authorisation status, since this evidence pack shows zero licences on file, which should be reconciled against the MHRA product register
- Confirmation of whether this use case is intended to support existing clinical practice (as the evidence suggests) rather than a new licensing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

