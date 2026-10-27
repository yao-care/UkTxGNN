---
layout: default
title: Oxygen
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Oxygen: predicted new indication Dry eye syndrome (evidence level L5). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Oxygen"
predicted_indications: ["dry eye syndrome", "dermatitis", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "non-syndromic esophageal malformation", "hydroa vacciniforme, familial", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "amyopathic dermatomyositis", "esophageal disease"]
---

# Oxygen
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

## Oxygen: From Medical Oxygen Therapy to Dermatitis
{: .text-alpha }

## One-Sentence Summary

Oxygen is a medical gas marketed in the UK as a ventilation-mask product (Ventimask Mk IV 28%), and no approved indication text is recorded in the data compiled for this report.
The TxGNN model's top-ranked prediction is **dry eye syndrome**, but that prediction has no supporting trials and only indirect literature. The best-supported candidate is **dermatitis**, with **3 small clinical trials** (including 2 relevant to dermatitis) and **20 publications**, mostly preclinical or mechanistic.
Overall evidence for any predicted new indication is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Dry eye syndrome (rank 1); dermatitis (rank 2) is the best-evidenced candidate and is assessed below |
| TxGNN Prediction Score | 93.22% (dry eye syndrome); 92.34% (dermatitis) |
| Evidence Level | L5 (dry eye syndrome); L3 (dermatitis) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (dry eye syndrome); Hold overall, with dermatitis as a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available. Oxygen is a medical gas used to correct hypoxaemia, and its original indication is not recorded in the data compiled for this report.

**Dry eye syndrome (top prediction).** Oxidative stress and reactive oxygen species (ROS)-driven inflammation are well documented in dry eye disease. However, the retrieved literature describes strategies that *reduce* ROS (antioxidant micelles, nanozymes, catalase, flavonoids). None of it delivers oxygen. The link is indirect and may even run in the opposite direction, so the high TxGNN score should be read as a computational signal only.

**Dermatitis.** A more plausible rationale exists here. Hyperbaric or topically dissolved oxygen may improve tissue oxygenation, angiogenesis and wound healing, particularly in radiation-induced skin injury. Small trials have tested oxygen in radiation dermatitis, diaper dermatitis and photodamage. However, most dermatitis literature concerns ROS scavenging, which does not support oxygen delivery.

Other lower-ranked predictions (acrodermatitis chronica atrophicans, neonatal dermatomyositis, esophageal malformation, familial hydroa vacciniforme, childhood connective-tissue ILD, acne keloid, amyopathic dermatomyositis, esophageal disease) have no direct supporting evidence. Oxygen appears only as supportive respiratory care or in unrelated contexts.

---

## Clinical Trial Evidence

No clinical trials are registered for dry eye syndrome. Trials for dermatitis (rank 2) are listed below.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06158347](https://clinicaltrials.gov/study/NCT06158347) | N/A | Completed | 30 | Randomised pilot of hyperbaric oxygen to reduce radiation dermatitis in localised breast cancer. Directly relevant, but exploratory; results not provided. |
| [NCT05427760](https://clinicaltrials.gov/study/NCT05427760) | N/A | Completed | 103 | Oxygen for diaper dermatitis in neonatal intensive care infants. Relevant subtype; results and delivery method not provided. |
| [NCT00991198](https://clinicaltrials.gov/study/NCT00991198) | Phase 2 | Completed | 49 | Double-blind, placebo-controlled trial of topically dissolved oxygen cosmeceuticals for photodamage. Only indirectly relevant (photodamage, not dermatitis). |

No Phase 3 trials are present. Five trials for esophageal disease were retrieved, but they use oxygen as perioperative or procedural respiratory support (two were withdrawn with zero enrolment) and do not test treatment of esophageal disease, so they are not listed.

---

## Literature Evidence

For dry eye syndrome and dermatitis, the retrieved publications are mostly preclinical or mechanistic. Selected examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33938134](https://pubmed.ncbi.nlm.nih.gov/33938134/) | 2022 | Systematic review/meta-analysis | Acta Ophthalmol | Oxidative stress markers in dry eye disease versus healthy subjects; supports a role for oxidative stress, not for oxygen therapy. |
| [28834388](https://pubmed.ncbi.nlm.nih.gov/28834388/) | 2018 | Review | Acta Ophthalmol | Oxidative stress and ocular surface inflammation in dry eye. |
| [37026245](https://pubmed.ncbi.nlm.nih.gov/37026245/) | 2023 | Review | Indian J Ophthalmol | Contact lenses for ocular surface disease, including highly oxygen-permeable materials. |
| [35435328](https://pubmed.ncbi.nlm.nih.gov/35435328/) | 2022 | Preclinical | Adv Sci | Anti-oxidative and anti-inflammatory micelle eye drops for dry eye. |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Adv Mater | Catalase nano-formulation eye drops to remove excess ROS in dry eye. |
| [41201396](https://pubmed.ncbi.nlm.nih.gov/41201396/) | 2026 | Review | Int J Dermatol | Mechanisms, manifestations and management of radiation-induced skin injury. |
| [36551332](https://pubmed.ncbi.nlm.nih.gov/36551332/) | 2022 | Review | Biomolecules | Oxidative stress and phototherapy in atopic dermatitis. |
| [37120459](https://pubmed.ncbi.nlm.nih.gov/37120459/) | 2023 | Preclinical | Nat Commun | Hydrogel dressing combining FAK inhibition and ROS scavenging for atopic dermatitis. |
| [39425637](https://pubmed.ncbi.nlm.nih.gov/39425637/) | 2024 | Preclinical | ACS Appl Mater Interfaces | Plasma-activated hydrogel delivering reactive oxygen and nitrogen species for allergic contact dermatitis. |
| [29464127](https://pubmed.ncbi.nlm.nih.gov/29464127/) | 2017 | Case report | Case Rep Crit Care | High-flow nasal oxygen as supportive care in a pregnant woman with dermatomyositis-related interstitial pneumonia. |

No randomised controlled trial evidence for oxygen in any predicted indication was found in the retrieved literature.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 21080001017 | Oxygen Ventimask Mk IV 28% | Not recorded | Not recorded |

One valid single-ingredient authorisation is recorded. Dosage form and approved indication text are not available in the data compiled for this report. Please check the SmPC and BNF for current licensed uses.

---

## Safety Considerations

**Drug Interactions** (2 recorded, both Major):
- **Amiodarone**: Major interaction.
- **Bleomycin**: Major interaction (oxygen exposure is a recognised concern with bleomycin-related pulmonary toxicity; confirm in the BNF).

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (dry eye syndrome) has no clinical trials, and its literature concerns ROS reduction rather than oxygen delivery, so the mechanistic link is indirect and possibly contradictory. Dermatitis (L3) is the only candidate with some clinical signal, but this comes from three small, mostly non-phased trials with no reported results. It is best treated as a research question rather than a candidate for progression.

**To proceed, the following is needed:**
- Mechanism of action data and the original licensed indication for the UK product
- For dermatitis: adequately powered, randomised trials with reported outcomes, defining the delivery route (hyperbaric, topical dissolved, or other), starting with radiation dermatitis
- Route-compatibility assessment against the available UK oxygen products
- Full safety review, including the Major interactions with amiodarone and bleomycin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

