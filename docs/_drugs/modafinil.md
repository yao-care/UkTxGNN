---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 1
---

# Modafinil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Modafinil: From Narcolepsy-Related Excessive Daytime Sleepiness to Insomnia

## One-Sentence Summary

Modafinil is a wake-promoting agent originally used to treat excessive daytime sleepiness associated with narcolepsy, obstructive sleep apnoea, and shift work sleep disorder. The TxGNN model predicts it may also be effective for **Insomnia**, and the evidence pack contains **29 clinical trials** and **19 publications** linked to this signal — but only a small minority of these directly target insomnia as a primary treatment endpoint; most concern excessive daytime sleepiness or fatigue in unrelated comorbid conditions. Given this, the evidence currently available is thin and mechanistically counter-intuitive, supporting a cautious **Hold** at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available UK licensing data (no marketing authorisations on file); per the evidence pack's mechanistic notes, modafinil is described as indicated for narcolepsy, obstructive sleep apnoea-related sleepiness, and shift work sleep disorder |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for modafinil is currently a data gap in this pack (DG002). Based on the information available, modafinil is a central nervous system stimulant/wake-promoting agent, working through dopamine reuptake inhibition and modulation of the hypothalamic orexin (hypocretin) system. Its established pharmacological effect is to **promote wakefulness**, which is why it is used for narcolepsy, obstructive sleep apnoea-related sleepiness, and shift work sleep disorder.

This creates a notable tension with the predicted indication. Insomnia is characterised by difficulty falling asleep or maintaining sleep — the pharmacological opposite of what a wake-promoting drug is designed to do. There is no obvious mechanistic pathway by which a stimulant would relieve insomnia; if anything, the theoretical risk runs the other way, with wake-promoting agents potentially worsening sleep-onset or sleep-maintenance difficulty.

Consistent with this, the trials and literature actually retrieved for this candidate mostly investigate modafinil (or armodafinil) as an **adjunct for residual daytime sleepiness or fatigue** in other primary conditions — bipolar depression, cancer-related fatigue, Parkinson's disease, chemotherapy after-effects — rather than as a direct treatment for insomnia itself. This pattern is consistent with the TxGNN knowledge graph having linked modafinil to insomnia through a shared "sleep disorder" node cluster (i.e., comorbidity-driven association) rather than through a genuine, evidence-supported treatment mechanism. This is an important caveat for interpreting the high TxGNN score, and is the main driver of the Hold recommendation below.

---

## Clinical Trial Evidence

*29 trials were identified in total; the 10 most relevant (those with an explicit relevance assessment) are listed below.*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | Examined modafinil's effect on daytime functioning and sleep in patients with **primary insomnia**, alone or combined with CBT-I. The most directly relevant trial in this set, but its endpoint was residual daytime impairment rather than core insomnia symptoms (sleep onset/maintenance). |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Completed | 18 | 8-week RCT of modafinil in stable bipolar disorder targeting circadian rhythm and cognitive dysfunction, not insomnia itself; very small sample. |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | Completed | 399 | Adjunctive armodafinil (150 mg/day) vs placebo for major depression associated with bipolar I disorder; likely targeted fatigue/sleepiness in partial responders rather than insomnia. |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | Completed | 257 | Adjunctive armodafinil (150 mg/day) in bipolar I depression; probable fatigue/sleepiness endpoint study, not a primary insomnia trial. |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I ± armodafinil for insomnia and fatigue following chemotherapy in breast cancer patients; armodafinil used as an adjunct to behavioural therapy, not as primary insomnia treatment. |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot study of brief behavioural therapy for insomnia (BBT-I) ± armodafinil in breast cancer patients; armodafinil supports daytime function rather than treating insomnia directly. |
| [NCT00678691](https://clinicaltrials.gov/study/NCT00678691) | Phase 4 | Completed | 55 | 8-week double-blind study of armodafinil augmentation for fibromyalgia-related fatigue; link to insomnia is indirect via the fatigue–sleep relationship. |
| [NCT03620253](https://clinicaltrials.gov/study/NCT03620253) | Phase 3 | Terminated | 9 | Assessed modafinil's pro-cognitive effect in remitted depression with residual cognitive impairment; terminated early, not an insomnia trial. |
| [NCT07295834](https://clinicaltrials.gov/study/NCT07295834) | Phase 2 | Not yet recruiting | 70 | Planned feasibility RCT of modafinil vs placebo for fatigue in inflammatory bowel disease; targets fatigue rather than insomnia. |
| [NCT06646822](https://clinicaltrials.gov/study/NCT06646822) | N/A | Active, not recruiting | 1500 | Cross-sectional survey of stimulant drug use/misuse among university students; an observational pharmacovigilance study unrelated to insomnia treatment. |

---

## Literature Evidence

*19 publications were identified in total; the 10 highest-tier (Systematic Review/Review, followed by Case Series) are listed below. No RCTs specific to insomnia were identified.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | Parkinsonism & Related Disorders | Systematic review/meta-analysis of pharmacological treatments for daytime sleepiness and sleep disorders in Parkinson's disease; modafinil discussed for excessive daytime sleepiness, not insomnia. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Review (Evidence-Based Guideline) | Movement Disorders | MDS evidence-based review of non-motor symptom treatments in Parkinson's disease, including modafinil for daytime sleepiness. |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | Expert Opinion on Pharmacotherapy | Overview of pharmacological/non-pharmacological management of PD-related sleep disturbances; positions modafinil within excessive daytime sleepiness management, not insomnia therapy. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review | Drugs | Evidence-based review of approved and investigational uses of modafinil, summarising RCT data mainly for narcolepsy, sleep deprivation, and EDS-related conditions. |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Review (Meta-analysis) | PLoS ONE | Systematic review and meta-analysis of modafinil for fatigue and excessive daytime sleepiness in neurological disorders; found inconsistent efficacy data and no insomnia-specific outcome. |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Revue Neurologique | Review of narcolepsy with cataplexy; notes modafinil as first-line EDS treatment, and mentions sleep-maintenance insomnia as a narcolepsy feature rather than a treatment target. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Reviews pitolisant's place in narcolepsy therapy relative to modafinil; comparative context only. |
| [26317009](https://pubmed.ncbi.nlm.nih.gov/26317009/) | 2014 | Review | Journal of Neurodegenerative Diseases | Review of multidisciplinary motor neuron disease management; modafinil mentioned only peripherally for fatigue. |
| [20082966](https://pubmed.ncbi.nlm.nih.gov/20082966/) | 2009 | Review | Parkinsonism & Related Disorders | Review of excessive daytime sleepiness in Parkinson's disease; modafinil noted as the only available, partially effective treatment for PD-related sleepiness. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case Series | American Journal of Hospice & Palliative Care | Small, uncontrolled case series showing modafinil reduced fatigue in Charcot-Marie-Tooth disease type 1A; fatigue, not insomnia, was the endpoint. |

---

## UK Market Information

Modafinil currently holds **no UK marketing authorisation** recorded in this evidence pack — market status is logged as "Not marketed" with zero licences on file. Given that modafinil is a long-established, internationally used molecule, this is a notable gap that should be independently verified against the MHRA products database and current BNF entries before any regulatory conclusions are drawn, rather than assumed to reflect the true UK licensing position.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications, and drug interaction data were not available in this evidence pack — this is logged as a Blocking data gap, DG001, preventing initial safety screening (S1).)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Modafinil's core pharmacology (wakefulness promotion) is directionally at odds with an insomnia indication, and the clinical trial and literature evidence located for this candidate almost entirely addresses excessive daytime sleepiness or fatigue in unrelated comorbid conditions rather than insomnia itself. Combined with the absence of MOA, UK licensing, and safety data, the evidence level for this candidate is L4 and does not yet support progression.

**To proceed, the following is needed:**
- Verification of modafinil's actual UK MHRA licensing status and SmPC, given this pack shows zero authorisations (a result that itself needs confirming)
- Mechanism of action data from DrugBank/SmPC (DG002)
- Key warnings and contraindications data to clear the S1 safety screen (DG001, currently Blocking)
- Dedicated trials in patients with primary insomnia (not comorbid EDS/fatigue populations) to determine whether a genuine treatment effect exists, or whether this signal is a knowledge-graph artefact from shared "sleep disorder" node clustering
- A defined drug interaction profile, particularly for concomitant sleep-affecting medications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

