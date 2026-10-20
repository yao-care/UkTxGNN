---
layout: default
title: Temazepam
parent: Model Prediction Only (L5)
nav_order: 601
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Temazepam: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
---

# Temazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Temazepam: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Temazepam is a benzodiazepine hypnotic, originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially the same condition as insomnia. The prediction is supported by **no registered clinical trials** and **20 publications** (mostly guidelines and reviews). Because the predicted indication is effectively the existing one, this is not a true repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 (guidelines, systematic reviews and network meta-analyses; no completed RCTs supplied) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

Note: the data compiled for this report assigned a preliminary level of L1. No completed Phase 3 RCTs were supplied, so this report applies the stated criteria and assigns L3.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacological knowledge, temazepam is a benzodiazepine receptor agonist that positively modulates GABA-A receptors. This enhances inhibitory neurotransmission and promotes sleep onset and maintenance.

"Sleep disorder, initiating and maintaining sleep" is essentially a synonym of insomnia. The high TxGNN score (0.998) therefore reflects an existing, established use rather than a new therapeutic direction. The prediction is reasonable, but it does not extend temazepam to a new patient population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 publications supplied are mostly guidelines, reviews and drug bulletins. The table lists the 10 most relevant.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | American Academy of Sleep Medicine guideline on drug treatment of chronic insomnia in adults, assessing individual drugs |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic review / network meta-analysis | Sleep | Compares the efficacy and safety of hypnotics for insomnia in older adults |
| [32544795](https://pubmed.ncbi.nlm.nih.gov/32544795/) | 2020 | Quantitative comparison | Sleep Med | Quantitative comparison of drug efficacy for insomnia |
| [31730011](https://pubmed.ncbi.nlm.nih.gov/31730011/) | 2019 | Overview of reviews | Syst Rev | Compares effectiveness and safety of pharmacological and non-pharmacological insomnia treatments |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | Clinical trial | JAMA Intern Med | Masked taper with behavioural intervention for stopping benzodiazepine receptor agonists (relevant to deprescribing) |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Recommendations for pharmacological management of insomnia in the elderly |
| [6132933](https://pubmed.ncbi.nlm.nih.gov/6132933/) | 1983 | Sleep laboratory review | J Clin Psychopharmacol | Compares flurazepam, temazepam and triazolam; temazepam is slowly absorbed (peak at 2 to 3 hours), limiting its usefulness for sleep onset |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Critical review | J Clin Psychopharmacol | Reviews rebound insomnia after stopping short half-life benzodiazepine hypnotics |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | Pharmacology of benzodiazepine hypnotics, including temazepam |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0401010T0AAAMAM (BNF-style product code, not a PL number) | Temazepam tablets 10 mg | Tablet | Not stated in the data compiled for this report |

Temazepam sits in BNF chapter 4.1.1 (hypnotics). One product entry is recorded and it is marked valid.

---

## Safety Considerations

**Contraindications and cautions flagged by the knowledge graph** (these come from drug-disease links, not product label text, and should be checked against the SmPC):
- Respiratory: obstructive sleep apnoea, sleep apnoea syndrome, congenital central hypoventilation syndrome
- Organ impairment: kidney disease, liver disease, gallbladder disease
- Psychiatric and cognitive: anxiety disorder, neurotic disorder, dysthymic disorder, amnestic disorder, retrograde amnesia
- Substance-related: substance-related disorder, substance abuse/dependence

**Drug interactions:** The interaction screen returned 100 records. Those shown include:
- **Major:** morphine, liposomal morphine (additive central nervous system and respiratory depression)
- **Moderate:** bupropion, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide
- **Minor:** antacids such as magnesium oxide, aluminium hydroxide and calcium carbonate

The literature also highlights rebound insomnia on discontinuation, dependence and abuse potential, and the need for deprescribing, particularly in older adults.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is effectively the one temazepam already has, so this is confirmation of established use, not a new repurposing opportunity. The evidence is guidelines, reviews and meta-analyses. Safety concerns (dependence, respiratory depression, opioid co-prescription, use in older adults) require guardrails.

**To proceed, the following is needed:**
- The licensed indication text and SmPC warnings and contraindications for the UK product (not available in the data compiled for this report)
- Mechanism of action data from DrugBank
- Confirmation of the PL number and dosage form of the UK authorisation
- A review of the NICE position on short-term hypnotic use and a plan for limiting treatment duration and monitoring dependence
- Specific guidance for older adults, people with respiratory disease, and patients taking opioids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

