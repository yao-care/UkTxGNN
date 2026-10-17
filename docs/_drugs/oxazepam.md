---
layout: default
title: Oxazepam
parent: Moderate Evidence (L3-L4)
nav_order: 467
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-15
description: "Oxazepam: predicted new indication Insomnia (evidence level L3). Approved use: Alcohol withdrawal delirium"
monitor_inn: "Oxazepam"
predicted_indications: ["insomnia (disease)"]
---

# Oxazepam
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

# Oxazepam: From Alcohol Withdrawal Delirium and Anxiety to Insomnia

## One-Sentence Summary

Oxazepam is a short-acting benzodiazepine, originally used for anxiety and alcohol withdrawal delirium.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **no registered clinical trials** and **10 publications** (only 2 directly comparative studies of oxazepam in sleep or anxiety), so the direction rests mainly on a computational prediction and older literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alcohol withdrawal delirium; anxiety (the UK licence record contains no indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, oxazepam is a short-acting benzodiazepine. Drugs of this class enhance GABA-A receptor-mediated inhibitory neurotransmission, producing anxiolytic and sedative-hypnotic effects. This mechanistic description is inferred from the drug class rather than from the supplied data.

Anxiety and insomnia frequently occur together, and benzodiazepines are used to treat both. Sleep disturbance is also a common feature of alcohol withdrawal. The prediction is therefore biologically plausible, particularly for insomnia accompanied by anxiety.

The very high TxGNN score is a computational output and is not clinical evidence in its own right.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The most relevant publications are listed first. Several retrieved papers are only indirectly related (for example, reviews of other drugs or conditions) and are omitted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | Clinical trial (comparative) | Am J Psychiatry | Oxazepam and flurazepam both improved some polysomnographic measures of sleep in 14 patients with chronic insomnia. Flurazepam caused substantial daytime sleepiness, whereas oxazepam did not. Some rebound effects were reported with oxazepam. |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | Randomised clinical trial | Ann Pharmacother | Compared melatonin with oxazepam for anxiety and sleep quality after primary PCI for STEMI, a setting in which benzodiazepines are often used but carry adverse effects and interaction risks. |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Study / review | Arch Gerontol Geriatr | Examined the effectiveness and safety of hypnotics in 60 people over 70 with insomnia and comorbid depression, dementia or behavioural disturbance. |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Observational | PeerJ | Long-term benzodiazepine and z-drug use in older adults is associated with increasing age, female sex and poorer psychological and physical health, raising concerns about inappropriate use. |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Clinical report | JAMA | Withdrawal syndrome in two patients after switching from a long-acting to a short-acting benzodiazepine (including oxazepam), persisting for at least one month. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Overview of the pharmacokinetics of anxiolytic drugs. |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | J Clin Exp Hepatol | Management of alcohol withdrawal syndrome in alcoholic liver disease, in which insomnia is an early symptom (indirect relevance). |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0401020T0AAABAB (BNF code; no PL number supplied) | Oxazepam tablets 10 mg | Tablet | Not stated in the data compiled |

BNF code 0401020T0 places oxazepam among the anxiolytics (BNF chapter 4.1.2).

---

## Safety Considerations

**Contraindications and risk conditions (from the TxGNN knowledge graph, not label text):**
The knowledge graph links oxazepam to contraindications in the following groups. Label wording should be confirmed in the SmPC.
- **Respiratory:** respiratory failure, sleep apnoea syndromes, congenital central hypoventilation syndrome, lung disease
- **Hepatic and renal:** liver disease, kidney disease, gallbladder disease
- **Metabolic:** porphyria and other porphyrin metabolism disorders
- **Psychiatric:** psychotic disorders, schizophreniform and schizoaffective disorders, personality disorders, intermittent explosive disorder, dysthymic disorder, neurotic and anxiety disorders (as listed in the graph)
- **Substance-related:** substance abuse/dependence
- **Cardiovascular:** hypotensive disorders

**Drug Interactions:** 100 interactions were identified. Examples from the first 20 reviewed:
- **Major:** morphine, including liposomal morphine (additive central nervous system and respiratory depression)
- **Moderate:** bupropion, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide
- **Minor:** antacids and mineral products (magnesium oxide, magnesium carbonate, magnesium hydroxide, calcium carbonate, aluminium hydroxide, magaldrate)
- Several further interactions (such as calcitriol, glimepiride, mesalazine, doxycycline and clotrimazole) have no assigned severity.

The literature also highlights dependence, withdrawal and rebound effects, and inappropriate long-term use in older adults.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and has a very high model score, but there are no registered trials and only limited, older, small-scale direct evidence for oxazepam in insomnia. Label-level safety data are also missing, and dependence and withdrawal risks are well recognised for benzodiazepines.

**To proceed, the following is needed:**
- Licensed indication text, dosage form and PL number from the MHRA record
- SmPC warnings and contraindications to confirm the knowledge-graph findings
- Mechanism of action data from DrugBank
- Controlled trials of oxazepam versus current insomnia options (including those recommended by NICE) with attention to rebound, dependence and daytime impairment
- A comparison with existing UK guidance on short-term hypnotic use to establish whether oxazepam adds value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

