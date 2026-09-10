---
layout: default
title: Fluphenazine
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Fluphenazine
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

# Fluphenazine: From Schizophrenia to Manic Bipolar Affective Disorder

> **Note on indication selection:** This Evidence Pack lists ten TxGNN-ranked candidate indications for fluphenazine (ranks #1–#9 by raw score: retinal dystrophy, syndromic/X-linked myopia subtypes, hydranencephaly, a glycosylation disorder, Charcot-Marie-Tooth disease, a cortical malformation syndrome, and glycine encephalopathy). The pack's own `repurposing_rationale` fields flag every one of these as having **no known mechanistic link** to fluphenazine's pharmacology and **zero supporting trials or literature** — consistent with `evidence_level: L5` and `recommendation: Hold` for all nine. These appear to be knowledge-graph artefacts rather than genuine repurposing signals, so leading with them would be misleading. The tenth-ranked candidate, **manic bipolar affective disorder**, is the only one with a coherent mechanistic rationale, real-world literature, and an evidence-supported `L3 / Proceed with Guardrails` scoring — this report focuses on that candidate.

## One-Sentence Summary

Fluphenazine is a first-generation (typical) phenothiazine antipsychotic, established for schizophrenia and related psychoses. The TxGNN model — supported by clinical literature rather than raw prediction score alone — points to **manic episodes in bipolar affective disorder** as a mechanistically plausible and already partially evidenced extension of use, with **20 supporting publications** but **no registered clinical trials** identified in this pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the supplied UK licence data (schizophrenia and other psychoses is the established indication for this phenothiazine antipsychotic) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% (rank 647 of the model's overall output, but the most evidence-supported candidate among those returned) |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the structured dataset (flagged as a data gap: DG002). Based on established pharmacological knowledge, fluphenazine is a phenothiazine-class typical antipsychotic that acts principally as a **dopamine D2 receptor antagonist**, with additional antagonism at D1, α1-adrenergic and H1-histaminergic receptors.

Acute mania in bipolar affective disorder is associated with mesolimbic dopaminergic hyperactivity, which is the same pathway targeted by D2-antagonist antipsychotics. Other typical and atypical antipsychotics sharing this mechanism — haloperidol, chlorpromazine, risperidone — are already established treatments for acute mania, and long-acting injectable (LAI) formulations (including fluphenazine decanoate) are used off-label in bipolar maintenance to improve adherence. This makes the fluphenazine-to-bipolar-mania signal a **within-class extrapolation from proven pharmacology**, rather than a novel, unsupported hypothesis — which distinguishes it clearly from the other nine candidates in this pack.

Two of the retrieved publications describe fluphenazine specifically in bipolar disorder (a case series on off-label use in comorbid substance abuse, and a case report of neuroleptic malignant syndrome during fluphenazine decanoate maintenance), while the remainder address the broader LAI-antipsychotic class in bipolar mania, lending indirect but consistent support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26243837](https://pubmed.ncbi.nlm.nih.gov/26243837/) | 2015 | Systematic Review + Expert Consensus | Clin Psychopharmacol Neurosci | Systematic review and expert consensus supporting LAI antipsychotics, including fluphenazine decanoate, for maintenance treatment of bipolar disorder |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | Retrospective Cohort | J Affective Disorders | Addition of LAI antipsychotics during manic episodes was associated with reduced rehospitalisation in bipolar disorder |
| [22494448](https://pubmed.ncbi.nlm.nih.gov/22494448/) | 2012 | Review | CNS Drugs | Reviews efficacy/safety of first- and second-generation depot antipsychotics for bipolar maintenance treatment |
| [30129771](https://pubmed.ncbi.nlm.nih.gov/30129771/) | 2018 | Comparative Effectiveness Study | J Comp Eff Res | LAI antipsychotic initiation associated with lower hospitalisation risk in bipolar I disorder |
| [36779113](https://pubmed.ncbi.nlm.nih.gov/36779113/) | 2023 | Case Report | Cureus | Off-label fluphenazine used to manage bipolar disorder with comorbid substance abuse; described as effective with community-based monitoring |
| [34353834](https://pubmed.ncbi.nlm.nih.gov/34353834/) | 2021 | Case Report | BMJ Case Reports | Neuroleptic malignant syndrome occurring in a bipolar disorder patient maintained on fluphenazine decanoate depot — safety signal |
| [37345508](https://pubmed.ncbi.nlm.nih.gov/37345508/) | 2023 | Review | Expert Opin Pharmacother | Practical guidance on switching to/from LAI antipsychotics, relevant to fluphenazine depot use in severe mental illness |
| [28112539](https://pubmed.ncbi.nlm.nih.gov/28112539/) | 2017 | Review | J Child Adolesc Psychopharmacol | Reviews LAI antipsychotic use in children and adolescents, limited evidence base |
| [27028966](https://pubmed.ncbi.nlm.nih.gov/27028966/) | 2016 | Review/Case Series | J Child Adolesc Psychopharmacol | Case series on LAI antipsychotic efficacy in adolescents |
| [20851282](https://pubmed.ncbi.nlm.nih.gov/20851282/) | 2010 | Case Report | Gen Hosp Psychiatry | Case report of antipsychotic-induced stuttering, noting fluphenazine among agents previously implicated |

---

## UK Market Information

Fluphenazine currently holds no active UK marketing authorisations in this dataset (market status: not marketed). No licence records were available to summarise product names, dosage forms or approved indication text.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

One literature-derived signal worth noting: a 2021 case report ([34353834](https://pubmed.ncbi.nlm.nih.gov/34353834/)) described neuroleptic malignant syndrome in a bipolar disorder patient on fluphenazine decanoate depot — this is consistent with the known class risk of NMS with typical antipsychotics and should be factored into any monitoring plan.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (established D2-antagonist class effect in mania) and is supported by observational cohort data and expert consensus on LAI antipsychotics — including fluphenazine specifically — in bipolar disorder. However, no registered clinical trials, no UK marketing authorisation, and no structured safety/DDI data were available, so this cannot proceed without further work.

**To proceed, the following is needed:**
- Formal safety review via SmPC/BNF and Yellow Card data, since structured warnings, contraindications and DDI data were not available (DG001)
- Confirmation of mechanism of action from DrugBank or equivalent primary source (DG002)
- A pathway to UK marketing authorisation or specials/import route, given the drug is not currently marketed in the UK
- Consideration of a prospective or registry-based study, since existing evidence is observational/case-level rather than trial-based
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

