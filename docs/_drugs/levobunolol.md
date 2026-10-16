---
layout: default
title: Levobunolol
parent: Model Prediction Only (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Levobunolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Levobunolol"
predicted_indications: ["primary hereditary glaucoma", "glaucoma 1, open angle", "open angle glaucoma", "Axenfeld anomaly", "closed-angle glaucoma", "hydrophthalmos", "chronic tic disorder", "benign shuddering attacks", "extrapyramidal and movement disease", "glaucoma"]
---

# Levobunolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Levobunolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Levobunolol is a non-selective beta-blocker eye drop, originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** specific to this condition were found, so the prediction rests on the model alone.
Most of the other top-ranked predictions are the drug's existing glaucoma uses, which are well supported by the literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From established pharmacology, levobunolol is a non-selective beta-adrenergic blocker. It lowers intraocular pressure (IOP) by reducing aqueous humour production in the ciliary epithelium.

Hereditary glaucoma is also characterised by raised IOP, so IOP lowering is mechanistically plausible. However, the very high TxGNN score is probably driven by the condition's closeness to the approved glaucoma indication in the knowledge graph. No study in the data tests levobunolol in this specific condition.

The other predictions fall into three groups:
- **Existing indications:** open-angle glaucoma, "glaucoma 1, open angle" and glaucoma in general. These are established uses rather than repurposing, and they are well documented.
- **Weak or indirect glaucoma-related predictions:** Axenfeld anomaly, closed-angle glaucoma and hydrophthalmos. At most, IOP lowering would be adjunctive or symptomatic. Definitive treatment is usually surgical or procedural.
- **Likely knowledge-graph artefacts:** chronic tic disorder, benign shuddering attacks and extrapyramidal/movement disease. No credible mechanistic link or evidence was found.

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hereditary glaucoma. No registered trials were found for any of the other predicted conditions either.

## Literature Evidence

There is currently no related literature available for primary hereditary glaucoma.

For context, the following publications support levobunolol in its established glaucoma indication (open-angle glaucoma and ocular hypertension):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic review / network meta-analysis | Ophthalmology | Comparative effectiveness of first-line medicines for primary open-angle glaucoma and ocular hypertension |
| [2664628](https://pubmed.ncbi.nlm.nih.gov/2664628/) | 1989 | Randomised double-masked study | Ophthalmology | Over 4 years in 391 patients, mean IOP fell by about 7 mmHg with levobunolol 0.5% and 1% and timolol 0.5%, with little loss of effect |
| [3881032](https://pubmed.ncbi.nlm.nih.gov/3881032/) | 1985 | Comparative clinical study | Am J Ophthalmol | In 162 patients, levobunolol and timolol gave similar IOP reductions (about 8 mmHg) |
| [2892662](https://pubmed.ncbi.nlm.nih.gov/2892662/) | 1987 | Review | Drugs | Levobunolol 0.5-1% reduced IOP by about 30%, was superior to placebo, and was comparable to other beta-blockers |
| [3513594](https://pubmed.ncbi.nlm.nih.gov/3513594/) | 1986 | Double-masked trial | Am J Ophthalmol | Once-daily levobunolol was effective in 92 patients compared with timolol |
| [3883971](https://pubmed.ncbi.nlm.nih.gov/3883971/) | 1985 | Double-masked study | Arch Ophthalmol | In 42 patients, levobunolol gave significant IOP reductions versus vehicle over 3 months |
| [2883990](https://pubmed.ncbi.nlm.nih.gov/2883990/) | 1987 | Randomised double-masked study | Br J Ophthalmol | Levobunolol 0.5% and metipranolol 0.6% reduced IOP by about 7 mmHg each in 46 patients |
| [8123096](https://pubmed.ncbi.nlm.nih.gov/8123096/) | 1993 | Comparative clinical study | J Ocul Pharmacol | Levobunolol compared with dipivefrin in 38 African American patients with open-angle glaucoma |
| [8773166](https://pubmed.ncbi.nlm.nih.gov/8773166/) | 1996 | Review | Ann Pharmacother | Comparison of ocular beta-blockers on systemic effects, local tolerability and cost |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Review | Med Lett Drugs Ther | Recent overview of drugs for open-angle glaucoma |

Two related records offer only indirect support for the weaker predictions: a retrospective cohort of 163 paediatric glaucoma patients ([19491991](https://pubmed.ncbi.nlm.nih.gov/19491991/), 2009) for Axenfeld anomaly, and a study in healthy volunteers and glaucoma patients ([1481323](https://pubmed.ncbi.nlm.nih.gov/1481323/), 1992) for closed-angle glaucoma. Neither establishes levobunolol efficacy in those conditions.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000T0AAABAB | Levobunolol HCl eye drops 0.5% 0.4 ml unit dose | Eye drops | Not stated in the data compiled for this report |

This is the only authorisation recorded, and it is a valid single-ingredient product. Please check the current MHRA SmPC and BNF for the full approved indications and dosing.

## Safety Considerations

- **Contraindications suggested by drug-disease associations:** The knowledge graph links levobunolol with asthma (including intrinsic and allergic asthma), pulmonary emphysema, atrioventricular block, diabetes mellitus and diabetic ketoacidosis, myasthenia gravis and neuromuscular junction disease, and anaphylaxis. These come from the knowledge graph rather than from label text, so they should be verified against the SmPC. They are consistent with the known cautions for systemic beta-blockade (bronchospasm, bradycardia, heart block), which can occur because topical drops are partly absorbed systemically.
- **Drug Interactions:** 24 interactions were recorded, none with a severity grade. Examples include lansoprazole, omeprazole, pantoprazole, prednisone, warfarin, clopidogrel, ibuprofen, tacrolimus and metoclopramide. These should be reviewed against the BNF before use.
- **Paediatric use:** For the paediatric-type conditions (Axenfeld anomaly, hydrophthalmos), systemic absorption of a beta-blocker is a particular concern.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary predicted indication, primary hereditary glaucoma, has no trials or literature behind it, so the evidence is model prediction only (L5). The established glaucoma indications are well supported (L3, Proceed with Guardrails), but they are existing uses and not new repurposing opportunities.

**To proceed, the following is needed:**
- Any clinical data or case series on levobunolol in primary hereditary glaucoma, including paediatric safety data
- Mechanism of action data from DrugBank
- Label warnings and contraindications from the SmPC and BNF
- The approved indication text and dosage form for the UK authorisation
- Severity grading for the 24 recorded drug interactions
- Specialist ophthalmology input on whether IOP lowering has a role alongside surgical management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

