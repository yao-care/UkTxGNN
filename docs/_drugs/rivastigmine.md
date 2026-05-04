---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 1
---

# Rivastigmine
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

# Rivastigmine: From Alzheimer's Disease / Dementia to Glaucoma

## One-Sentence Summary

Rivastigmine is a carbamate-type acetylcholinesterase (AChE) inhibitor, widely established in the treatment of dementia associated with Alzheimer's disease and Parkinson's disease.
The TxGNN model predicts it may be effective for **Glaucoma**, with **3 publications** (preclinical and mechanistic studies) currently supporting this direction.
No registered clinical trials in this indication have been identified to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset — no UK marketing authorisations recorded |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per current dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Rivastigmine is a carbamate-type inhibitor of acetylcholinesterase (AChE) and butyrylcholinesterase (BuChE). By reversibly inhibiting these enzymes, it raises local concentrations of acetylcholine (ACh) — the principal neurotransmitter at cholinergic synapses. In its established neurological use, this compensates for the loss of cholinergic tone in the cerebral cortex characteristic of Alzheimer's disease.

The mechanistic case for repurposing to glaucoma follows directly from the same pharmacological action. In the anterior segment of the eye, elevated ACh activates M3 muscarinic receptors on the ciliary muscle and trabecular meshwork, increasing aqueous humour outflow and thereby reducing intraocular pressure (IOP). This is precisely the mechanism exploited by pilocarpine, the long-established miotic approved for glaucoma. Topical ocular administration of rivastigmine could, in principle, achieve therapeutically relevant IOP reduction whilst substantially limiting the systemic cholinergic adverse effects — nausea, bradycardia, and excessive secretions — that accompany oral dosing.

Although rivastigmine's pharmacology is well characterised in the published literature, formal MOA data was not retrieved in this Evidence Pack (Data Gap DG002). The mechanistic rationale above draws on the `repurposing_rationale` field within the pack and established cholinergic pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Computational / Systems Genetics | *Frontiers in Molecular Biosciences* | Systems genetics and molecular modelling of cholinergic agents for IOP reduction; identifies muscarinic M3 receptor signalling in the trabecular meshwork as a key target and highlights AChE inhibitor candidates |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Patent Review / Narrative Review | *Expert Opinion on Therapeutic Patents* | Comprehensive review of AChE inhibitors (2012–2015); explicitly documents therapeutic relevance of mild AChE inhibition in Alzheimer's disease, myasthenia gravis, and **glaucoma** |
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Animal Study (Preclinical) | *Journal of Ocular Pharmacology and Therapeutics* | Topical rivastigmine demonstrated significant IOP reduction sustained over 8 hours in normotensive rabbits; provides direct preclinical proof-of-concept for ocular administration |

---

## UK Market Information

No UK marketing authorisations for rivastigmine are recorded in the current dataset (market status: not marketed). Clinical teams should independently cross-reference the MHRA Product Information database and the current edition of the BNF to verify up-to-date authorisation and prescribing status before any clinical use or trial design is considered.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to one preclinical animal study and two mechanistic/review publications (Evidence Level L4); no human clinical trial data for rivastigmine in glaucoma has been identified, and safety data specific to topical ocular formulation is entirely absent from this Evidence Pack.

**To proceed, the following is needed:**

- Retrieve full mechanism of action (MOA) data from DrugBank to complete mechanistic analysis (Data Gap DG002)
- Review MHRA SmPC for key warnings, contraindications, and special population restrictions (Data Gap DG001)
- Assess feasibility of a topical ocular formulation (stability, excipients, pH, preservative compatibility)
- Obtain ocular pharmacokinetic data: corneal penetration, aqueous humour concentrations, and systemic absorption following topical dosing in humans
- Commission a structured literature review to identify any unpublished or grey-literature studies in glaucoma
- Design a Phase 1/2 proof-of-concept dose-escalation trial in ocular hypertension or open-angle glaucoma patients
- Evaluate cholinergic adverse-event risk profile (miosis, ciliary spasm, systemic absorption) specifically for the topical route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

