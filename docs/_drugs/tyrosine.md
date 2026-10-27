---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tyrosine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the available marketing authorisation data"
monitor_inn: "Tyrosine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "aqueous misdirection", "traumatic glaucoma", "neovascular glaucoma"]
---

# Tyrosine
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

## Tyrosine: From an Unspecified Original Indication to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Tyrosine is an amino acid and catecholamine and thyroid hormone precursor. The data compiled for this report do not record a specific approved indication for it.
The TxGNN model ranks **cauda equina syndrome** as its top prediction, but **no clinical trials and no publications** support this direction (Evidence Level L5, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available marketing authorisation data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Tyrosine is a dietary amino acid and a known precursor of catecholamines (dopamine, noradrenaline) and of thyroid hormones. No approved original indication is recorded in the data compiled for this report, so a link between an established use and the predicted one cannot be drawn.

Cauda equina syndrome is a compressive neurological emergency treated surgically. There is no clear mechanistic link between tyrosine and this condition. The high score is a graph-based prediction only and should not be read as evidence of benefit.

**Other predictions reviewed (all rated L5 except where noted, all Hold):**

| Rank | Predicted Indication | Score | Comment |
|---|---|---|---|
| 2 | Neurogenic bladder (obsolete term) | 99.55% | Speculative link via catecholamine control of the bladder. No evidence, and the disease term is ambiguous. |
| 3 | Angle-closure glaucoma | 99.54% | No direct mechanism. Retrieved papers are association or descriptive studies only. |
| 4 | Hyperthyroidism | 99.51% | Tyrosine is a thyroid hormone substrate, so benefit is mechanistically doubtful and it may be counterproductive. |
| 5 | Postural orthostatic tachycardia syndrome | 99.46% | Catecholamine precursor, which is plausible, but the only paper is a case report using a tyrosine hydroxylase inhibitor (opposite pharmacology). Evidence Level L4. |
| 6 | Hyperthyroxinemia | 99.46% | Tyrosine is a thyroxine precursor, so lowering thyroxine is unlikely. |
| 7 | Resistance to thyroid hormone (TRβ mutation) | 99.40% | Receptor-level defect that a hormone substrate would not correct. |
| 8 | Aqueous misdirection | 99.35% | No plausible mechanism. |
| 9 | Traumatic glaucoma | 99.35% | No direct mechanism. |
| 10 | Neovascular glaucoma | 99.32% | No direct mechanism. Standard care is anti-VEGF therapy, laser and surgery. |

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome.

For completeness, one trial was found for a lower-ranked prediction (hyperthyroidism):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Not applicable | Not yet recruiting | 150 | Placebo-controlled trial of a zinc, selenium and L-tyrosine supplement to prevent thyrotoxicosis in adults with the SEPP1 r25191G/A polymorphism and raised TPOAb. Tyrosine is not the sole intervention, so it gives no direct evidence. |

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

The most relevant items found for other predictions are shown below. None tests tyrosine as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Stress-related chronic fatigue syndrome responding to alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor. Indirect and pharmacologically opposite to tyrosine (POTS prediction). |
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Front Med | Plasma amino acid changes associated with ocular parameters in early primary angle-closure glaucoma. An association study, not a treatment study. |
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | General review of hyperthyroidism causes, diagnosis and management. |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma causes and treatment. No tyrosine content. |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Basic research | Endocrinology | Novel thyroid hormone receptor beta mutations impairing ligand binding. No tyrosine intervention. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 091101000AAFEFE | L-Tyrosine Cap 500mg | Not recorded | Not recorded |

This record is a single valid single-ingredient authorisation. Its number does not follow the standard MHRA "PL XXXXX/XXXX" format, so the product details should be verified against the MHRA register and the BNF.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug interaction records were found in the data compiled for this report. Because tyrosine is a thyroid hormone and catecholamine precursor, the thyroid-related predictions in particular would need careful safety assessment before any evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions rest on model scores alone (L5, with one L4 for POTS). None has supporting trials or literature showing benefit from tyrosine. For several, particularly the thyroid conditions, the mechanism argues against benefit.

**To proceed, the following is needed:**
- Product label information (approved indications, warnings, contraindications) for the authorised tyrosine product, which is currently missing and blocks safety screening
- Mechanism of action data
- A clearly defined original indication to anchor the repurposing rationale
- Direct clinical or mechanistic evidence for tyrosine in any candidate indication. POTS, with its catecholamine rationale, would be the most plausible one to explore first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

