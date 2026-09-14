---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 1
---

# Oxazepam
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

Using the general reporting format (no specialized skill applies — this is a direct content-generation task with an explicit template already provided in the prompt).

# Oxazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

> Oxazepam is a benzodiazepine historically used for the short-term relief of anxiety (and related conditions such as alcohol withdrawal), though the specific licensed indication text is not available in this evidence pack.
> The TxGNN model predicts it may be effective for **Insomnia**,
> with **no registered clinical trials** but **11 supporting publications** currently identified in the literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorders (benzodiazepine class use) — specific UK licensing text unavailable (data gap) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, oxazepam is a benzodiazepine that acts by potentiating GABA-A receptor activity, producing anxiolytic, sedative, and hypnotic effects. Its established use has been the short-term management of anxiety, and, in some jurisdictions, anxiety-related sleep disturbance and alcohol withdrawal.

The overlap between anxiety and insomnia is well recognised clinically — many benzodiazepines approved for anxiety are also used off-label or formally licensed for short-term insomnia, because the same GABA-ergic mechanism that reduces anxiety also promotes sleep onset and maintenance. This mechanistic and clinical overlap is the most plausible explanation for the TxGNN model linking oxazepam to insomnia, and is supported by decades of published clinical experience (see Literature Evidence below), including head-to-head comparisons with other hypnotics such as flurazepam.

No detailed DrugBank-sourced MOA record was available for this evidence pack (data gap DG002), so the above rationale relies on general class knowledge rather than pack-verified data. This should be confirmed against DrugBank/SmPC sources before clinical decision-making.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | The Annals of Pharmacotherapy | Randomised trial comparing melatonin and oxazepam for anxiety and sleep quality in STEMI patients post-PCI |
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | Clinical Trial | American Journal of Psychiatry | Oxazepam improved polysomnographically defined nocturnal sleep measures in chronic insomnia, without the daytime sleepiness seen with flurazepam |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Observational | Archives of Gerontology and Geriatrics | Evaluated effectiveness and safety of hypnotic drugs, including benzodiazepines, for insomnia in patients over 70 with comorbid depression/dementia |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | Journal of Clinical and Experimental Hepatology | Reviews management of alcohol withdrawal syndrome, where insomnia is a core symptom managed with benzodiazepines such as oxazepam |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Reviews pharmacokinetics of anxiolytic benzodiazepines, relevant to their sedative/hypnotic dosing |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Review | Psychiatrische Praxis | Survey of therapeutic practice for behavioural/sleep symptoms of dementia (BPSD), including benzodiazepine use |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Case report | JAMA | Describes withdrawal symptoms, including insomnia, after substituting short-acting oxazepam for long-acting diazepam |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Observational | PeerJ | Examined factors associated with long-term benzodiazepine/z-drug use, including sleep-related indications, in older populations |

---

## UK Market Information

Oxazepam currently has **no marketing authorisation on record** in this evidence pack — market status is "Not marketed" with 0 authorisations listed. UK availability (e.g. via named-patient/import routes, or historical licences no longer active) should be verified directly against the MHRA product database before further evaluation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

As a general class caution, benzodiazepines such as oxazepam carry recognised risks of dependence, withdrawal (as reflected in the literature above), sedation, falls in older adults, and respiratory depression when combined with other CNS depressants — but none of this could be confirmed against pack-specific warnings, contraindications, or DDI data, all of which were unavailable (data gaps DG001, and safety.key_warnings/contraindications/ddi all empty).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The drug has no current UK marketing authorisation, no registered clinical trials for the insomnia indication, and a **Blocking**-severity data gap (DG001: missing SmPC warnings/contraindications) that prevents safety pre-screening. While literature evidence is directionally supportive, it is insufficient alone to proceed.

**To proceed, the following is needed:**
- MHRA/SmPC warnings, contraindications, and drug interaction data (resolves DG001)
- Verified mechanism of action from DrugBank (resolves DG002)
- Confirmation of UK availability/import pathway, given current "not marketed" status
- Assessment of benzodiazepine-class risks (dependence, falls, sedation) specific to an insomnia indication, particularly in older adults
- Literature classification/relevance screening (currently marked "pending") to confirm study quality and refine the evidence level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

