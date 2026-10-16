---
layout: default
title: Cysteine
parent: Moderate Evidence (L3-L4)
nav_order: 199
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
description: "Cysteine: predicted new indication Dry eye syndrome (evidence level L4). Approved use: Bronchitis, cystic fibrosis, bronchiectasis, paracetamol poisoning…"
monitor_inn: "cysteine"
predicted_indications: ["dry eye syndrome", "closed-angle glaucoma", "nasal cavity disease", "acute laryngopharyngitis", "pharyngitis", "exercise-induced malignant hyperthermia", "angle-closure glaucoma"]
---

# Cysteine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Cysteine: From Respiratory and Amyloid-Related Indications to Dry Eye Syndrome

## One-Sentence Summary

Cysteine is an amino acid, marketed in the UK as a single-ingredient product and associated with respiratory indications such as bronchitis and cystic fibrosis.
The TxGNN model predicts it may be effective for **dry eye syndrome**, but there are currently **no registered clinical trials** and the **20 publications** retrieved are almost entirely preclinical or formulation studies in which cysteine is a component rather than the therapeutic agent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, cystic fibrosis, bronchiectasis, paracetamol poisoning, amyloidosis (from the knowledge graph; no approved indication text available for the UK product) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, cysteine is a sulfur-containing amino acid with a reactive thiol group. It is a precursor of glutathione and of hydrogen sulfide/persulfide species, and it underlies the mucolytic and antioxidant activity of its derivative N-acetylcysteine.

Dry eye disease is driven in part by excess reactive oxygen species (ROS), which trigger inflammation of the lacrimal gland and ocular surface (including NLRP3 inflammasome activation and pyroptosis). An antioxidant, thiol-based compound could plausibly counter this process. The thiol group is also the basis of "thiomers" (for example thiolated chitosan), which bind to mucus and prolong retention on the ocular surface.

An important caution: the retrieved literature mainly describes cysteine as a building block in drug-delivery materials or as a feature of unrelated proteins. It does not test cysteine itself as a treatment for dry eye. The prediction is therefore a hypothesis, not a demonstrated effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved papers is a clinical trial of cysteine in dry eye. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical (formulation) | Advanced Materials | Catalase nanoparticles self-assembled with cysteine-modified chitosan, designed as eye drops to reduce ROS in dry eye disease |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical (formulation) | Int J Biol Macromol | Chondroitin sulfate–L-cysteine conjugate on lipid carriers improved corneal retention and permeation of dexamethasone |
| [41485487](https://pubmed.ncbi.nlm.nih.gov/41485487/) | 2026 | Preclinical (prodrug) | J Control Release | Superoxide-responsive persulfide prodrug designed to remove ROS in dry eye disease |
| [26606856](https://pubmed.ncbi.nlm.nih.gov/26606856/) | 2015 | Preclinical (formulation) | Ther Deliv | Hyaluronic acid modified with cysteine ethyl ester evaluated as a mucoadhesive lubricant for dry eye |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Review | J Control Release | Review of thiolated polymers (thiomers) and their improved mucoadhesion, from laboratory to market |
| [31028759](https://pubmed.ncbi.nlm.nih.gov/31028759/) | 2019 | Review | Adv Drug Deliv Rev | Review of thiolated polymers and their disulfide bonding with mucus glycoproteins |
| [36626177](https://pubmed.ncbi.nlm.nih.gov/36626177/) | 2023 | Preclinical (mechanism) | Invest Ophthalmol Vis Sci | Aquaporin 5 deficiency worsens ROS/NLRP3-mediated pyroptosis in lacrimal glands |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Mechanism / patient study | Exp Eye Res | ROS-activated NLRP3 inflammasomes initiate inflammation in hyperosmolarity-stressed corneal cells and in dry eye patients |

The remaining retrieved papers concern Sjögren's syndrome biology or unrelated compounds and do not evaluate cysteine as a treatment.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704020J0BBABAC | Cystrin Tab 5mg | Not specified | Not specified |

This is a single-ingredient product with a valid status. The identifier above appears to be a BNF-style classification code rather than a standard MHRA "PL" number, and no approved indication text or dosage form was available. The product details should be checked against the MHRA register and the SmPC.

---

## Safety Considerations

No label-based warnings, contraindications or interaction data were available. A search for drug interactions returned no results.

The knowledge graph (not label text) links cysteine with the following contraindicated conditions, which should be verified against the SmPC and BNF before any use:
- Peptic ulcer disease (including active peptic ulcer disease)
- Hypotensive disorder
- Respiratory failure
- Asthma and bronchial disease
- Oesophageal varices
- Phenylketonuria and other disorders of phenylalanine metabolism

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (for context)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Closed-angle / angle-closure glaucoma | 99.95% / 99.06% | L5 | Literature concerns SPARC proteins, not cysteine as a drug; these are duplicate entries; Hold |
| Nasal cavity disease | 99.88% | L4 | Only a 1996 study of a different combination product (tuaminoheptane plus N-acetylcysteine) in healthy volunteers; Research question |
| Acute laryngopharyngitis | 99.79% | L5 | Score only; no trials or literature; Hold |
| Pharyngitis | 99.78% | L4 | One in vitro study of N-acetylcysteine on tonsil biofilm; most papers concern a streptococcal enzyme; Research question |
| Exercise-induced malignant hyperthermia | 99.26% | L5 | No evidence of cysteine benefit; Hold |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dry eye prediction rests on a high model score and a plausible antioxidant and mucoadhesive rationale, but there are no clinical trials and no studies testing cysteine itself. The evidence is preclinical (L4), and the key safety data from the product label are missing.

**To proceed, the following is needed:**
- Mechanism of action data for cysteine (for example from DrugBank)
- The SmPC and BNF safety information (warnings, contraindications, interactions) and the approved indication and dosage form for the UK product
- Preclinical studies testing cysteine itself, in an ocular-suitable topical formulation, in dry eye models
- A review of ocular safety, tolerability and formulation stability before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

