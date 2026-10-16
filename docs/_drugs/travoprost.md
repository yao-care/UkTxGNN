---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Travoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Travoprost"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
---

# Travoprost
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

# Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical prostaglandin F2-alpha analogue, originally used to lower intraocular pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but there are **no clinical trials** and **no publications** supporting this specific prediction. It is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.99985% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, travoprost is a prostaglandin F2-alpha analogue that lowers intraocular pressure by acting on FP receptors and increasing uveoscleral outflow. Its efficacy in glaucoma and ocular hypertension is well established.

The link to visceral calciphylaxis is speculative. FP receptor agonism causes local vasodilation (seen clinically as conjunctival hyperaemia), and the model may be picking up on vascular-related terms in its knowledge graph. However, calciphylaxis is a calcific vascular disease, and there is no data showing that a topical ocular prostaglandin analogue has any therapeutic effect on it. Minimal systemic exposure after eye-drop dosing further weakens the rationale.

The other top-ranked predictions (thoracic outlet syndromes, angiodysplasia of stomach, blue toe syndrome, lymphangiectasis, spontaneous coronary artery dissection, hemangioendothelioma, and vascular disease) are likewise unsupported by clinical data. Several are mechanical or neural compression conditions with no plausible link to this drug.

---

## Clinical Trial Evidence

No clinical trials are registered for visceral calciphylaxis. Currently no related clinical trials registered.

For context, the highest-ranked prediction with any trial data is the broader category "vascular disease" (rank 5). The retrieved trials relate to travoprost's approved use or its side effects and do not test it as a treatment for vascular disease. The most relevant are shown below.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Phase 4 | Completed | 20 | Travoprost vs latanoprost effects on retinal vascular diameter and choroidal blood flow in glaucoma; indirect physiological data only, not disease-treatment evidence |
| [NCT02136589](https://clinicaltrials.gov/study/NCT02136589) | Phase 4 | Completed | 40 | NSAID pretreatment for travoprost-induced conjunctival hyperaemia; addresses a side effect |
| [NCT00047554](https://clinicaltrials.gov/study/NCT00047554) | N/A | Terminated | 336 | Five-year safety study of iris pigmentation changes with travoprost in glaucoma |
| [NCT00293800](https://clinicaltrials.gov/study/NCT00293800) | Phase 3 | Completed | 173 | Glaucoma therapy in open-angle glaucoma or ocular hypertension (original indication) |
| [NCT00672997](https://clinicaltrials.gov/study/NCT00672997) | Phase 3 | Completed | 301 | Travoprost/timolol BAC-free combination vs standard combination in glaucoma (original indication) |
| [NCT00760539](https://clinicaltrials.gov/study/NCT00760539) | Phase 3 | Completed | 87 | Travoprost/timolol BAC-free combination in glaucoma, Japanese study (original indication) |
| [NCT02140060](https://clinicaltrials.gov/study/NCT02140060) | Phase 2 | Completed | 327 | Travoprost/brinzolamide fixed combination IOP-lowering in glaucoma (original indication) |
| [NCT01510145](https://clinicaltrials.gov/study/NCT01510145) | Phase 4 | Completed | 191 | BAK-free travoprost after latanoprost monotherapy in glaucoma (original indication) |

---

## Literature Evidence

No publications were found for visceral calciphylaxis. Currently no related literature available.

Publications retrieved for the broader "vascular disease" and "hemangioendothelioma" predictions concern the approved indications and side effects, not repurposing:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25867658](https://pubmed.ncbi.nlm.nih.gov/25867658/) | 2015 | Systematic Review | Curr Med Res Opin | Efficacy and tolerability of prostaglandin-timolol fixed combinations in glaucoma |
| [22167538](https://pubmed.ncbi.nlm.nih.gov/22167538/) | 2012 | Meta-analysis | Eur J Ophthalmol | IOP-lowering and tolerability of prostaglandin-timolol fixed combinations |
| [23231442](https://pubmed.ncbi.nlm.nih.gov/23231442/) | 2013 | Meta-analysis | J Ocul Pharmacol Ther | Prostaglandin analogue and timolol fixed vs unfixed combinations in open-angle glaucoma |
| [19019922](https://pubmed.ncbi.nlm.nih.gov/19019922/) | 2009 | Systematic Review | Br J Ophthalmol | Meta-analysis of RCTs on conjunctival hyperaemia with latanoprost vs travoprost and bimatoprost |
| [31335731](https://pubmed.ncbi.nlm.nih.gov/31335731/) | 2019 | Review | Medicine | Efficacy of travoprost in glaucoma |
| [12648301](https://pubmed.ncbi.nlm.nih.gov/12648301/) | 2003 | Review | J Ocul Pharmacol Ther | Conjunctival hyperaemia with topical prostaglandins (up to 50% with travoprost) |
| [24070367](https://pubmed.ncbi.nlm.nih.gov/24070367/) | 2013 | Randomised study | J Ocul Pharmacol Ther | Bimatoprost 0.01% vs travoprost/timolol after latanoprost and timolol |
| [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/) | 2008 | Case report | J Fr Ophtalmol | Uveal effusion with exudative retinal detachment induced by topical travoprost in Sturge-Weber-Krabbe syndrome; an adverse event, not a benefit |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000AEAAAAAA | Travoprost eye drops 40 mcg/ml | Eye drops | Not stated in the data compiled for this report |

One valid single-ingredient authorisation is recorded. Please check the MHRA register and the BNF (prostaglandin analogues, glaucoma section) for the licensed indications and current product details.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (graph-derived, not label text): uveitis, iris disease, ciliary body disease, panuveitis, iritis, cystoid macular oedema, and macular retinal oedema.
- **Case report signal**: uveal effusion with exudative retinal detachment has been reported after topical travoprost in a patient with Sturge-Weber-Krabbe syndrome (PMID 19107053). This suggests caution in patients with abnormal vasculature.
- **Known class effects in the literature**: conjunctival hyperaemia (reported in up to 50% of patients on travoprost) and iris pigmentation changes.
- **Drug interactions**: 49 potential interactions were recorded, including calcitriol, pantoprazole, sucralfate, morphine, metformin, omeprazole, prednisone, prednisolone, simvastatin and aspirin. None has a graded severity in the data, so they should be interpreted with caution and checked against the BNF.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for visceral calciphylaxis rests solely on a graph-based model score. No trials or publications support it, and a topical ocular prostaglandin analogue has no plausible systemic mechanism for this condition. The same applies to all other top-ranked predictions.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and a credible mechanistic rationale for calcific vascular disease
- Preclinical or mechanistic studies showing relevance to calciphylaxis pathophysiology
- Assessment of whether a systemically relevant route or formulation would be needed, since only eye drops are marketed
- Review of the SmPC warnings and contraindications, which were not available in the data compiled for this report
- Evaluation of safety in patients with vascular abnormalities, given the Sturge-Weber-Krabbe case report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

