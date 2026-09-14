---
layout: default
title: Orphenadrine
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 7
---

# Orphenadrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Orphenadrine: From Antimuscarinic/Anti-Parkinsonian Use to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

> Orphenadrine's own UK-authorised original indication is not available in the current evidence pack (the drug is **Not Marketed** in the UK, 0 licences on record); supporting literature elsewhere in this pack describes it as an antimuscarinic agent used for parkinsonism and drug-induced extrapyramidal symptoms.
> The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**, with **0 clinical trials** and **15 publications** currently linked to this candidate.
> Importantly, none of the 15 publications mention orphenadrine at all — they are general ophthalmology reviews/case reports retrieved by disease-term association, not drug-specific evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK-authorised indication text available — drug is not currently marketed in the UK |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for orphenadrine is not available in this evidence pack (flagged as a High-severity data gap, DG002). Elsewhere in the same evidence base, literature associated with a different candidate indication (schizophrenia/EPS, see rank 5) describes orphenadrine as an antimuscarinic agent used for parkinsonism and to counteract neuroleptic-induced extrapyramidal symptoms — but this context does not extend to retinal or extraocular disease.

For the retinal dystrophy prediction specifically, there is no established or plausible mechanistic link presented. The relationship between an anticholinergic/antihistaminic muscle relaxant and inherited retinal dystrophy with extraocular anomalies is not supported by any pharmacological rationale in the available data.

The TxGNN score for this candidate is high (0.9929), but the accompanying literature review shows this is **not corroborated by direct evidence**: all 15 retrieved publications discuss orbital/ophthalmic conditions in general (orbital infections, diplopia, congenital ptosis, lens anomalies, Wagner-Stickler syndrome, extraocular muscle fibrosis, etc.) and **none mention orphenadrine**. This pattern is consistent with keyword co-occurrence in the underlying knowledge graph rather than a drug-disease relationship grounded in real evidence, and should be treated as a model artefact requiring caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

**Note:** The publications below were retrieved via disease-term association in the knowledge graph. None of them mention orphenadrine directly; they are included for transparency but do not constitute drug-specific evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Overview of orbital infections secondary to sinusitis; no mention of orphenadrine |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic approach to evaluating diplopia; no mention of orphenadrine |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis classification and levator muscle dystrophy; no mention of orphenadrine |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape and associated dysgenesis; no mention of orphenadrine |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler vitreoretinal degeneration and extraocular manifestations; no mention of orphenadrine |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric ocular pathologies (coloboma, ROP, Coats disease); no mention of orphenadrine |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia; no mention of orphenadrine |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | Congenital trochlear-oculomotor synkinesis case; no mention of orphenadrine |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optom Vis Sci | Case of congenital extraocular muscle fibrosis with variable synergistic divergence; no mention of orphenadrine |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case report | Arch Ophthalmol | Case series of orbital arteriovenous malformations; no mention of orphenadrine |

---

## UK Market Information

Orphenadrine currently holds **no UK marketing authorisation** (market status: Not Marketed; 0 licences on record in this evidence pack). No product, dosage form, or approved indication text is therefore available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags TFDA/SmPC-equivalent warnings and contraindications as an unresolved Blocking data gap (DG001) — a formal safety review has not yet been completed for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial evidence and no literature that specifically implicates orphenadrine in retinal dystrophy or extraocular anomalies — the retrieved publications are off-target, general ophthalmology reviews. This is an L5, model-prediction-only candidate with no mechanistic or empirical support.

**To proceed, the following is needed:**
- Orphenadrine mechanism of action data (DG002)
- TFDA/SmPC-equivalent warnings, contraindications and DDI data (DG001 — currently Blocking)
- A drug-specific mechanistic rationale connecting orphenadrine's pharmacology to retinal/extraocular pathology, or evidence directly naming the drug in this disease context
- Consideration of whether the rank-5 signal in this same evidence pack (schizophrenia/antipsychotic-induced EPS, evidence level L2, multiple RCTs and a Cochrane review) represents a more actionable, better-evidenced repurposing candidate than the top-ranked TxGNN score alone would suggest
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

