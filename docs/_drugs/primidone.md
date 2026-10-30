---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 519
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Primidone"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Primidone: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Primidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Primidone: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Primidone is an anticonvulsant originally used to treat epilepsy, including generalised tonic-clonic and partial seizures.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **no clinical trials** and **no publications** supporting it. The most plausible non-seizure candidate in the data compiled for this report is **trigeminal neuralgia**, which has only indirect evidence (**0 clinical trials**, **6 publications**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primidone is an anticonvulsant that is metabolised to phenobarbital and phenylethylmalonamide (PEMA). Its efficacy in epilepsy is established, but no mechanistic basis for anti-tumour activity in trigeminal nerve neoplasm is supported by the data compiled for this report.

The high TxGNN score (0.9999) is a computational prediction only. Any benefit in a trigeminal nerve tumour would be speculative, for example symptomatic relief of neuropathic pain rather than a treatment effect on the tumour.

Other predictions in the list are more coherent with the drug's pharmacology:

- **Reflex seizure types** (thinking, orgasm-induced, eating, micturition-induced, audiogenic, startle and reading seizures) fall within the established antiseizure scope of primidone. These are better regarded as extensions of the existing epilepsy indication than as true repurposing.
- **Trigeminal neuralgia** is a neuropathic pain condition treated with sodium-channel-blocking antiseizure drugs (carbamazepine is first-line), so a class-based rationale exists. A 2026 preclinical paper implicates TRPM3 in orofacial neuropathic pain, but the data do not show that primidone acts on TRPM3. This is classed as a research question.
- **Beta-ketothiolase deficiency** (an inborn error of ketone and isoleucine metabolism) has no supported mechanistic link and no evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, either for trigeminal nerve neoplasm or for any of the other predicted indications.

---

## Literature Evidence

**For the top-ranked prediction (trigeminal nerve neoplasm):** Currently no related literature available.

The publications below relate to lower-ranked predictions and provide indirect evidence only. None demonstrates primidone efficacy in the predicted condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs used outside epilepsy; evidence mostly from case series and small trials, needing confirmation in large phase III trials (trigeminal neuralgia) |
| [41806836](https://pubmed.ncbi.nlm.nih.gov/41806836/) | 2026 | Preclinical (mouse) | Cell Rep Med | TRPM3 mediates spontaneous pain and allodynia in a trigeminal neuropathic pain model (trigeminal neuralgia) |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Case report | Zhonghua Yi Xue Za Zhi | Startle epilepsy presenting as drop attacks in a 3.5-year-old boy; primidone efficacy not shown in the data (startle epilepsy) |
| [116632](https://pubmed.ncbi.nlm.nih.gov/116632/) | 1979 | Case report | Arch Neurol | Drawing-induced myoclonic seizures, a reflex epilepsy (reading and micturition-induced seizures) |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Review | Clin Neurosci | Primidone (500–1,000 mg/day) listed among useful drugs for cortical myoclonus (reading seizures) |
| [9068876](https://pubmed.ncbi.nlm.nih.gov/9068876/) | 1996 | Review | Baillieres Clin Neurol | Overview of established antiepileptic drugs including primidone (micturition-induced seizures) |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Preclinical (mouse) | Neurol Psychiatr | Effects of phenobarbital, phenytoin and primidone on brain enzyme activity in audiogenic epilepsy (audiogenic seizures) |
| [19054416](https://pubmed.ncbi.nlm.nih.gov/19054416/) | 2009 | Cohort | Epilepsia | Initial epilepsy care in older US veterans; not specific to thinking seizures (thinking seizures) |
| [4525036](https://pubmed.ncbi.nlm.nih.gov/4525036/) | 1974 | Case report (veterinary) | J Am Vet Med Assoc | Long-term primidone therapy in a dog; not human evidence (eating seizures) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BNF code 0408010U0AAABAB | Primidone tablets 250 mg | Tablet | Not available in the data compiled; primidone sits in BNF chapter 4.8.1 (control of epilepsy) |

The product is marketed as a single-ingredient, valid authorisation. The identifier shown above is a BNF product code rather than a PL number, and the manufacturer and approved indication text were not available.

---

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence):** The following were flagged:
  - Porphyria, including inherited porphyria and porphyrin metabolism disease
  - Kidney disease and liver disease
  - Gallbladder disease
  - Blood disorders: thrombocytopenia, neutropenia (including severe congenital forms), agranulocytosis, leukopenia, pancytopenia, anaemia (including macrocytic anaemia)
  - Substance abuse or dependence
  - Sleep apnoea syndromes and congenital central hypoventilation syndrome
  - Anxiety, neurotic and dysthymic disorders

  These should be verified against the SmPC.
- **Drug Interactions:** 100 interactions were recorded; the first 20 are summarised here.
  - **Major:** morphine and eliglustat.
  - **Moderate:** doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, calcifediol, calcitriol, pioglitazone, bupropion, aprepitant, metronidazole, canagliflozin, saxagliptin, difenoxin, diphenoxylate and dronabinol.
  - **Minor:** cimetidine.

  Primidone's conversion to phenobarbital makes it an enzyme inducer, which is consistent with the many interactions listed.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, rests on a model score alone, with no trials, no literature and no plausible mechanism (L5). The seizure-type predictions are largely extensions of the existing epilepsy indication, and the evidence for them is indirect, old or preclinical (L4–L5). Trigeminal neuralgia is the most plausible non-seizure candidate, but it remains a research question with no primidone-specific trials.

**To proceed, the following is needed:**
- Mechanism of action data for primidone and its metabolites (phenobarbital, PEMA)
- SmPC-based warnings and contraindications, and UK licence indication text, to confirm the current authorisation
- For trigeminal neuralgia: a systematic review or a pilot study of primidone against first-line carbamazepine, including any NICE guidance on neuropathic pain
- For reflex seizures: case series or registry data showing primidone response in the specific seizure types, since these may fall within the existing epilepsy indication
- For trigeminal nerve neoplasm and beta-ketothiolase deficiency: no further investment unless a credible mechanistic rationale emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

