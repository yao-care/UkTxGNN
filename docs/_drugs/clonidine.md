---
layout: default
title: Clonidine
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Clonidine
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

Using the Evidence Pack, I selected **Tourette syndrome** (rank 5, score 99.98%, evidence level L2) as the lead predicted indication for this report rather than the raw top‑ranked hit (*faciodigitogenital syndrome*, 99.9993%), because the evidence pack's own rationale explicitly flags that top hit as a mechanistically implausible false positive (Aarskog syndrome, FGD1 mutation, no known α2‑adrenergic link, zero trials/literature, Hold/S0). Tourette syndrome is the candidate with the strongest, most clinically actionable evidence base in this pack. This judgement call is made transparent below.

---

# Clonidine: From Hypertension to Tourette Syndrome

## One-Sentence Summary

Clonidine (DrugBank DB00575) is a centrally acting alpha-2 adrenergic agonist classically used to treat hypertension. The TxGNN model predicts it may also be effective for **Tourette Syndrome**, a chronic tic disorder, with **3 clinical trials** and **19 publications** — including European clinical guidelines and a network meta-analysis — currently supporting this direction.

*Note on candidate selection: the TxGNN model's single highest-scoring prediction for Clonidine was "faciodigitogenital syndrome" (score 99.999%), but this is assessed in the evidence pack itself as a biologically implausible false positive (a rare X-linked genetic disorder with no known link to adrenergic pathways, no trials, no literature). Tourette syndrome was therefore selected as the lead candidate on the basis of evidence quality rather than raw model score. Other lower-priority candidates identified (migraine, manic bipolar disorder, trichotillomania) are noted at the end of this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension *(classic/established use; no formal marketing-authorisation indication text was available in this evidence pack — see UK Market Information below)* |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| UK Market Status | Not marketed *(per this evidence pack — recommend independent MHRA verification, see Conclusion)* |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack (data gap DG002). Based on established pharmacological knowledge, Clonidine is a centrally acting alpha-2 adrenergic receptor agonist. Its classic action — reducing sympathetic outflow from the central nervous system — underlies its long-standing use as an antihypertensive, and its efficacy in that role is well established in clinical practice.

Tourette syndrome is a neurodevelopmental tic disorder in which dysregulated noradrenergic transmission from the locus coeruleus to cortical and subcortical circuits is implicated in tic generation and associated hyperarousal. Because alpha-2 agonism dampens this same noradrenergic outflow, the mechanistic link between Clonidine's established cardiovascular action and its potential antitic effect is biologically coherent rather than incidental.

This is not solely a theoretical extrapolation: a Clonidine transdermal patch already holds regulatory approval in some markets (e.g., China) specifically for Tourette syndrome, and alpha-2 agonists (clonidine, guanfacine) are named first-line agents in tic-suppression guidelines. This gives the TxGNN prediction a substantially stronger real-world grounding than a typical model-only hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Completed | 12 | Head-to-head, double-blind crossover trial comparing levetiracetam and clonidine for tic suppression in children with Tourette syndrome. |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Unknown | 32 | Investigated whether clonidine-mediated improvement in night-time sleep reduces daytime aggression in children with Tourette syndrome and comorbid ADHD; completion/results not confirmed. |
| [NCT01172288](https://clinicaltrials.gov/study/NCT01172288) | Phase 2 | Completed | 31 | Double-blind, placebo-controlled trial of N-acetylcysteine (not clonidine) for paediatric tics; included as comparator context, noting alpha-2 agonists (clonidine, guanfacine) as an existing effective tic-suppressing drug class. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Guideline/Review | European Child & Adolescent Psychiatry | Updated European (ESSTS) clinical guidelines on pharmacological treatment of Tourette syndrome and tic disorders. |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network Meta-analysis | The Lancet Child & Adolescent Health | Compares efficacy, tolerability and acceptability of pharmacological interventions, including clonidine, for Tourette syndrome. |
| [39258554](https://pubmed.ncbi.nlm.nih.gov/39258554/) | 2024 | RCT | Clinical Neuropharmacology | Randomised, double-blind, placebo-controlled multicentre trial of a clonidine adhesive patch for Tourette syndrome. |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | RCT/Review | Psychiatry Investigation | Efficacy and safety of clonidine patch in Tourette syndrome patients with comorbid ADHD. |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | AAN comprehensive systematic review of tic treatments in Tourette syndrome and chronic tic disorders. |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic Review | Journal of Psychopharmacology | Systematic review assessing the quality of evidence for pharmacological treatment of Tourette syndrome. |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Systematic Review | Journal of Child Psychology and Psychiatry | Practitioner review of treatments for Tourette syndrome in children and young people. |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Early clinical study | The Lancet | Landmark early report: clonidine improved Tourette syndrome in children unresponsive to haloperidol. |
| [1414629](https://pubmed.ncbi.nlm.nih.gov/1414629/) | 1992 | Cohort/small trial | Advances in Neurology | Clinical experience with clonidine and clonazepam in Tourette syndrome. |
| [40392363](https://pubmed.ncbi.nlm.nih.gov/40392363/) | 2025 | Animal study | Journal of Neuroimmune Pharmacology | Mechanistic study: clonidine ameliorates neuroinflammation in a rat model of Tourette syndrome, supporting a biological basis beyond noradrenergic modulation alone. |

---

## UK Market Information

No UK marketing authorisation records are present in this evidence pack (0 licences returned, market status recorded as "Not marketed"). This is flagged as a **Blocking** data gap (DG001) in the meta section of this evidence pack, since regulatory licence and SmPC data could not be retrieved. Clonidine is widely known to have held UK licences historically (e.g., under brand names used for hypertension and migraine prophylaxis), but this could not be confirmed against current MHRA records within this dataset and **must be independently verified** before any regulatory or prescribing decision is made.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(All safety fields in this evidence pack — key warnings, contraindications, and drug-drug interactions — returned no data. This is recorded as a Blocking data gap, DG001, meaning this candidate cannot yet pass an initial safety screen. This must be resolved before any further progression.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clonidine's use in Tourette syndrome is supported by a coherent mechanistic rationale, a completed head-to-head Phase 4 RCT, a recent multicentre placebo-controlled RCT of a clonidine patch, and endorsement in European clinical guidelines and a network meta-analysis — a substantially stronger evidence base than the model's raw top-ranked hit. However, trial sizes remain small (largest direct comparative trial n=12), and this evidence pack is missing critical UK-specific regulatory and safety data, so progression should proceed cautiously and under guardrails rather than as an unconditional "Go".

**To proceed, the following is needed:**
- MHRA SmPC data — key warnings and contraindications (Blocking gap DG001; required before any formal safety pre-assessment)
- Confirmed current UK marketing authorisation status (this evidence pack shows zero licences/not marketed — verify against live MHRA data, as this appears inconsistent with Clonidine's known long-standing clinical use)
- Detailed, sourced mechanism of action data from DrugBank (High-severity gap DG002)
- A dedicated drug-drug interaction search (the DDI query in this pack returned no results, which likely reflects an incomplete search rather than a true absence of interactions)
- Paediatric-specific safety and dosing evidence, since the majority of relevant trials are in children and adolescents
- Larger-scale confirmatory RCT data, given the modest size of existing head-to-head trials

*For completeness: lower-priority candidates identified for Clonidine in this evidence pack include migraine (L2, historical 1970s–80s trials, no modern registered trials), manic bipolar affective disorder (L3, small terminated trial plus a systematic review), and trichotillomania (L4, mechanistic/animal evidence only, no direct clonidine trials). These were not selected as the lead candidate but may warrant separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

