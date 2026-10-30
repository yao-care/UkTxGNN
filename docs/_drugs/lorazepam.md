---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Lorazepam"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Lorazepam: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Lorazepam
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

## Lorazepam: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Lorazepam is a benzodiazepine originally used for anxiety disorders and seizure conditions, including status epilepticus.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but **no clinical trials and no publications** support it, so it rests on model prediction alone.
Among the other predictions, **insomnia** and several **reflex seizure types** have indirect literature support only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lorazepam is a benzodiazepine that enhances GABA-A receptor-mediated inhibition, giving it anxiolytic, sedative and anticonvulsant effects.

For the top-ranked prediction, **trigeminal nerve neoplasm**, no plausible mechanistic link has been identified. Lorazepam has no known antineoplastic activity. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, lorazepam could treat symptoms such as anxiety or seizures in a patient with a cranial nerve tumour, which is supportive care rather than a repurposing indication.

The other predictions are more biologically coherent:

- **Insomnia:** GABA-A enhancement produces sedative-hypnotic effects, and lorazepam is already used for sleep disturbance and agitation. The retrieved literature is mostly indirect (insomnia drug reviews, agitation in bipolar disorder, alcohol withdrawal). Small older studies compare lorazepam with flurazepam and test different lorazepam dosing schedules in chronic insomnia. Tolerance, dependence, next-day sedation, and fall and cognitive risks (especially in older people) limit long-term use.
- **Reflex seizure types** (reading, micturition-induced, audiogenic, startle, eating, thinking and orgasm-induced seizures) and **acute encephalopathy with biphasic seizures and late reduced diffusion:** these extend lorazepam's established antiseizure use. The literature concerns general seizure management rather than these specific conditions, so this is extrapolation, not disease-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predictions.

---

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm. The most relevant publications found for the other predictions are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22335736](https://pubmed.ncbi.nlm.nih.gov/22335736/) | 2012 | RCT | N Engl J Med | Intramuscular versus intravenous benzodiazepine therapy for prehospital status epilepticus (general seizure evidence) |
| [17414241](https://pubmed.ncbi.nlm.nih.gov/17414241/) | 2007 | RCT | J Clin Psychopharmacol | IM aripiprazole versus IM lorazepam 2 mg versus placebo for acute agitation in bipolar I disorder (lorazepam used as comparator) |
| [35194860](https://pubmed.ncbi.nlm.nih.gov/35194860/) | 2022 | Systematic review/meta-analysis | Addiction | Network meta-analysis of pharmacotherapies for alcohol withdrawal |
| [38358613](https://pubmed.ncbi.nlm.nih.gov/38358613/) | 2024 | Review | CNS Drugs | Benzodiazepines are the mainstay of acute treatment of seizure clusters |
| [35971024](https://pubmed.ncbi.nlm.nih.gov/35971024/) | 2022 | Review | CNS Drugs | Routes of delivery, pharmacokinetics, efficacy and tolerability of benzodiazepines in seizures and status epilepticus |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | Overview of drugs for chronic insomnia |
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | Double-blind crossover study | J Clin Pharmacol | Lorazepam 2 mg performed better than flurazepam 30 mg on most sleep parameters in eight chronic insomniacs |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Clinical study | Int Clin Psychopharmacol | Lorazepam 0.5 mg three times daily versus 1.5 mg at night in primary insomnia |
| [11593256](https://pubmed.ncbi.nlm.nih.gov/11593256/) | 2001 | Case series | Neurol India | Five cases of photosensitive epilepsy treated with adjuvant lorazepam |
| [6127668](https://pubmed.ncbi.nlm.nih.gov/6127668/) | 1981 | Preclinical | Pol J Pharmacol Pharm | Lorazepam depressed audiogenic seizures in rodents |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0401020P0AAABAB (BNF-style product code; not a PL number) | Lorazepam tablets 1 mg | Tablet (inferred from product name) | Not stated in the data compiled for this report |

Only one authorisation is recorded. The record contains no manufacturer, dosage form field or approved indication text. NICE appraisal information is not available in the data compiled for this report.

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
The TxGNN knowledge graph links lorazepam to the following conditions as contraindications or cautions. These should be checked against the SmPC.

- Hepatic: liver failure, liver disease, hepatic encephalopathy, hepatic coma, gallbladder disease
- Respiratory and sleep: respiratory failure, obstructive sleep apnoea syndrome, sleep apnoea syndrome, congenital central hypoventilation syndrome
- Renal: kidney disease, pyoureter
- Eye: open-angle and angle-closure glaucoma
- Metabolic: inherited porphyria, porphyria and porphyrin metabolism disease
- Psychiatric: substance-related disorder and substance abuse/dependence, neurotic disorder, dysthymic disorder (the graph also lists anxiety disorder, an approved use, so this edge should be interpreted cautiously)

**Drug Interactions:** 100 interactions were identified in the DDInter database; 20 are listed in the data compiled for this report.

- **Major:** morphine, including liposomal morphine (additive CNS and respiratory depression)
- **Moderate:** bupropion, dronabinol, nabilone, teduglutide, metoclopramide, opium, sibutramine
- **Minor:** antacids and related agents (aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide)
- **Unknown severity:** calcitriol, phentermine, pantoprazole, mesalazine, acarbose

**Other considerations from the literature:**
- Withdrawal-related hyperexcitability and dependence (rodent studies)
- Propylene glycol toxicity with intravenous lorazepam
- Sedation, falls and cognitive risk in older people

Label-based warnings and contraindications are not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, trigeminal nerve neoplasm, has no trials, no literature and no plausible mechanism, so the high TxGNN score is not credible as a repurposing signal. The more plausible directions (insomnia and reflex seizures) have only indirect evidence and are classed as research questions at evidence level L4, not as candidates ready for development.

**To proceed, the following is needed:**
- Label-based warnings and contraindications from the SmPC and BNF, which are currently missing and block safety screening
- Mechanism of action data, from DrugBank or the SmPC
- The UK licensed indications and dosage form for the recorded authorisation
- For insomnia: lorazepam-specific randomised evidence, and positioning against approved hypnotics, with attention to dependence and tolerance
- For reflex seizure types: disease-specific case series or registry data
- A decision on whether to deprioritise trigeminal nerve neoplasm entirely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

