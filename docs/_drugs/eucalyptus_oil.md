---
layout: default
title: Eucalyptus Oil
parent: Moderate Evidence (L3-L4)
nav_order: 270
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Eucalyptus Oil: predicted new indication Osteoarthritis (evidence level L4). Approved use: Not available in the data compiled for this report"
---

# Eucalyptus Oil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Eucalyptus Oil: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Eucalyptus oil is a plant-derived product with one UK marketing authorisation, but no approved indication text was available in the data compiled for this report.
The TxGNN model predicts it may be useful for **osteoarthritis** (top-ranked prediction), but **no clinical trials** and only **2 publications** support this direction, and neither tests eucalyptus oil as a treatment for osteoarthritis.
The evidence is currently computational only, so the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Eucalyptus oil's main component, 1,8-cineole (eucalyptol), has reported anti-inflammatory and analgesic properties. This is plausibly relevant to joint inflammation, which is the basis for the prediction.

The two retrieved papers for osteoarthritis are about topical formulation science: a celecoxib emulgel that uses a natural oil as a vehicle, and a review of nanoemulgels for topical delivery. Neither tests eucalyptus oil as a therapeutic agent for osteoarthritis. The high TxGNN score is a computational prediction only.

**Other predicted indications.** The model also ranks several other conditions highly:

- **Rheumatoid arthritis (98.28%)**. This has the most supporting material.
  - An animal and in silico study of 1,8-cineole reported anti-arthritic effects through inflammatory pathways (IL-17, IL-10, NF-κB, 5-LOX, COX-2).
  - One clinical study examined eucalyptus inhalation for pain and quality of life in rheumatoid arthritis. This is the only direct human evidence. It addresses symptom relief, not disease modification, and its design could not be verified.
  - The remaining papers are drug-delivery studies in which eucalyptus oil is only a formulation component.
- **Gout (97.78%)**. A general anti-inflammatory rationale is conceivable, but there is no supporting evidence.
- **Osteoarthritis susceptibility, pseudoachondroplasia, primitive portal vein thrombosis, early-onset familial noncirrhotic portal hypertension, idiopathic copper-associated cirrhosis and hepatoportal sclerosis**. These are prediction only, with no identified mechanistic link. Several likely reflect proximity to the osteoarthritis node in the knowledge graph.
- **Hepatic porphyria (97.85%)**. There is no therapeutic rationale. Terpenoid components of essential oils can induce hepatic cytochrome P450 enzymes, which is a theoretical safety concern in porphyria rather than a benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications relevant to the top-ranked prediction (osteoarthritis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38409718](https://pubmed.ncbi.nlm.nih.gov/38409718/) | 2024 | Formulation study (preclinical) | Anti-inflammatory & Anti-allergy Agents in Medicinal Chemistry | Celecoxib emulgel developed using a natural oil; eucalyptus oil is not tested as a treatment for osteoarthritis |
| [37111672](https://pubmed.ncbi.nlm.nih.gov/37111672/) | 2023 | Review | Pharmaceutics | Overview of nanoemulgels for improving topical delivery of anti-inflammatory drugs |

Closest related evidence (rheumatoid arthritis, the second-ranked prediction):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36060153](https://pubmed.ncbi.nlm.nih.gov/36060153/) | 2022 | Clinical study (design to be verified) | Contemporary Clinical Trials Communications | Effect of eucalyptus inhalation on pain and quality of life in rheumatoid arthritis patients |
| [38649658](https://pubmed.ncbi.nlm.nih.gov/38649658/) | 2024 | Preclinical (in vivo and in silico) | Inflammopharmacology | Eucalyptol (1,8-cineole) showed anti-arthritic potential in a rat arthritis model, with effects on IL-17, IL-10, NF-κB, 5-LOX and COX-2 |
| [37726536](https://pubmed.ncbi.nlm.nih.gov/37726536/) | 2023 | Formulation study (preclinical) | AAPS PharmSciTech | Continentalic acid transfersomal gel for rheumatoid arthritis; eucalyptus oil used as a permeation enhancer |
| [32207921](https://pubmed.ncbi.nlm.nih.gov/32207921/) | 2020 | Formulation study (preclinical) | ACS Nano | Transdermal methotrexate nanomicelle hydrogel for rheumatoid arthritis |
| [37815044](https://pubmed.ncbi.nlm.nih.gov/37815044/) | 2024 | Formulation study (preclinical) | Macromolecular Bioscience | Tofacitinib-loaded nanoparticles for localised delivery in arthritic joints |
| [39492133](https://pubmed.ncbi.nlm.nih.gov/39492133/) | 2025 | Formulation study (preclinical) | Biomaterials Advances | Infliximab-loaded transdermal hydrogel for rheumatoid arthritis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190605000AAAVAV | Eucalyptus Oil (liquid) | Not specified | Not specified |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug interaction records were found in the data compiled for this report. One theoretical concern is that terpenoid components of essential oils may induce hepatic cytochrome P450 enzymes, which could matter in hepatic porphyria.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are driven by the model alone. No registered trials exist, and the available literature is mostly about formulation science rather than eucalyptus oil as a therapy. The only direct human study concerns symptom relief (pain and quality of life) in rheumatoid arthritis, not osteoarthritis.

**To proceed, the following is needed:**
- Confirmation of the approved indication, dosage form and route for the existing UK authorisation
- Safety data (warnings, contraindications and interactions) from the SmPC and BNF
- Mechanism of action data
- Verification of the design and results of the eucalyptus inhalation study in rheumatoid arthritis
- Clinical or well-designed preclinical studies testing eucalyptus oil or 1,8-cineole directly in osteoarthritis
- Assessment of route and formulation compatibility (for example topical versus inhaled) for any joint-related use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

