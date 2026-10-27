---
layout: default
title: Etilefrine
parent: Model Prediction Only (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etilefrine: predicted new indication Alopecia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Etilefrine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "benign prostatic hyperplasia (disease)", "osteoarthritis", "headache disorder", "phaeochromocytoma", "sympathetic paraganglioma", "trigeminal autonomic cephalalgia"]
---

# Etilefrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Etilefrine: From Hypotension to Alopecia (Top Prediction), with Headache Disorder as the Only Indication Showing Any Evidence
{: .text-alpha }

## One-Sentence Summary

Etilefrine is an alpha/beta-adrenergic agonist (sympathomimetic) marketed in the UK as a 5 mg tablet. The TxGNN model predicts it may be effective for **alopecia** (score 97.6%), but there are **no clinical trials** and **no publications** supporting this prediction. The only indication with any literature is **headache disorder**, which has a single 1985 study whose full results could not be verified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 97.61% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Etilefrine is known to be an alpha/beta-adrenergic agonist (sympathomimetic) that acts on vascular smooth muscle. A mechanistic link to hair growth has not been established.

For alopecia, the pharmacology does not obviously support a benefit. Alpha-1 agonism could in theory reduce scalp perfusion through vasoconstriction. The high TxGNN score is a computational prediction, probably driven by network similarity to other hair-disorder terms rather than by biological evidence.

The other top-ranked predictions show the same pattern:

- **Other hair disorders** (hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata): no plausible pathway links adrenergic agonism to genetic hair-loss mechanisms or to the autoimmune process in alopecia areata.
- **Benign prostatic hyperplasia:** BPH treatment relies on alpha-1 antagonists. An agonist would be expected to worsen outflow symptoms and could precipitate urinary retention. This is a safety concern, not a repurposing opportunity.
- **Phaeochromocytoma and sympathetic paraganglioma:** these tumours secrete catecholamines. A sympathomimetic risks hypertensive crisis and arrhythmia, so etilefrine would be contraindicated.
- **Osteoarthritis and trigeminal autonomic cephalalgia:** no direct mechanistic link or clinical evidence.
- **Headache disorder:** vascular tone modulation is relevant to migraine, giving a plausible but speculative link (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was available for the top-ranked prediction (alopecia). The only publication in the data relates to the rank 7 prediction, headache disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2864937](https://pubmed.ncbi.nlm.nih.gov/2864937/) | 1985 | Double-blind trial (inferred from title) | Arzneimittel-Forschung | 3-month trial in 24 hypotensive patients with migraine comparing etilefrine pivalate 20 mg, dihydroergotamine 5 mg and placebo. The abstract reports fewer migraine attacks with both active treatments than with placebo, with reduced attack duration, intensity and analgesic use. Only a truncated abstract was available, so design details and effect sizes cannot be verified. |

Note that the study used etilefrine pivalate in a small, hypotensive population, so it does not directly transfer to other headache types or to the UK tablet formulation.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0207010G0AAAAAA | Etilefrine HCl 5 mg tablets | Tablet | Not available in the data compiled for this report |

The listed identifier follows a BNF-style code rather than a standard PL number, and the approved indication text was not available.

## Safety Considerations

Based on the pharmacology of the drug class and the rationale for the predictions:

- **Cardiovascular:** sympathomimetics can cause hypertensive crisis and arrhythmia, particularly in catecholamine-secreting tumours (phaeochromocytoma, paraganglioma).
- **Urinary:** an adrenergic agonist may worsen outflow obstruction and precipitate urinary retention in men with benign prostatic hyperplasia.
- **Headache:** systemic adrenergic agonists can themselves cause headache, so the benefit-risk balance in headache disorders is uncertain.

No drug interaction records were found in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction rests on a model score alone (L5), with no trials or publications, and the pharmacology (potential scalp vasoconstriction) does not support a benefit. Several other top predictions (BPH, phaeochromocytoma, paraganglioma) point to safety concerns rather than opportunities. The only signal is a small, unverified 1985 migraine study, which at most justifies a research question rather than development.

**To proceed, the following is needed:**
- Mechanism of action data for etilefrine, and a plausible biological rationale for any new indication
- The approved indication text and SmPC warnings and contraindications for the UK product
- For headache disorder: retrieval and critical appraisal of the full 1985 paper, followed by a search for more recent controlled studies
- For alopecia: preclinical evidence (for example, hair follicle models) before any clinical consideration
- A route and formulation assessment, since a topical or systemic approach has not been evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

