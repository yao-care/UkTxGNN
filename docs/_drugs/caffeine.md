---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Headache and migraine disorders, allergic and vasomotor rhinitis…"
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "acute laryngopharyngitis", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
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

## Caffeine: From Headache and Migraine Disorders to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Caffeine is a methylxanthine used in headache and migraine disorders and in combination products for cold, pharyngitis and rhinitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials** and only **3 publications** (a review, a formulation study and an animal study, none showing treatment of nasal disease) support this direction.
Other predicted indications, such as hypnic headache and neuralgia, have somewhat stronger indirect support and may be better research priorities.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Headache and migraine disorders, allergic and vasomotor rhinitis, common cold, pharyngitis (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (preclinical and mechanistic evidence only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, caffeine is a methylxanthine that antagonises adenosine receptors and inhibits phosphodiesterase. It may also interact with bitter taste receptors in airway epithelium.

Caffeine is already used in combination products for allergic and vasomotor rhinitis, so a link to nasal conditions is biologically plausible. However, the supporting evidence is indirect. The one nasal-related study examined a nasal gel as a delivery route for cognition after sleep deprivation, not as treatment for nasal disease. The prediction is therefore best regarded as a hypothesis, not an established direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in airway tissues including the nasal cavity; their pharmacology and role in human airways are reviewed |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation/Preclinical | Current Drug Delivery | Nasal caffeine thermo-sensitive in situ gel developed to enhance cognition after sleep deprivation (a delivery route, not nasal disease treatment) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited lung tumorigenesis in rats given a tobacco-specific carcinogen (not relevant to nasal disease) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0404000E0AAAKAK | Caffeine solution 25 mg/5 ml | Not specified | Not specified |

The record shows one valid single-ingredient product. The identifier appears to be a BNF-style product code (not a PL number), and no manufacturer, dosage form or indication text is available. Please check the MHRA and BNF entries directly.

---

## Safety Considerations

- **Contraindications and cautions (from the knowledge graph, not label text):** The knowledge graph links caffeine to caution or contraindication in several conditions. These include:
  - Cardiovascular: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, long QT syndrome.
  - Neurological and psychiatric: epilepsy, insomnia, anxiety disorders.
  - Respiratory and gastrointestinal: COPD, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis.
  - Hepatic, renal and metabolic: liver disease and liver failure, kidney disease, porphyria, hypothyroidism.
  - Other: gallbladder disease, thrombocytopenia.
- **Drug Interactions:** 75 interactions were identified. The main examples are listed below; the full list should be checked in the BNF.
  - **Major:** cocaine (nasal and topical).
  - **Moderate:** alosetron, obeticholic acid, abametapir (topical), adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole, duloxetine.
  - **Minor:** acetylsalicylic acid, cimetidine, atazanavir, disulfiram.
- **Other considerations:** Retrieved literature raises cardiovascular concerns with stimulant use and medication-overuse headache with analgesic combinations.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials and the supporting literature is indirect, with only a nasal delivery formulation study and an airway review. The label-based safety data are also incomplete.

**To proceed, the following is needed:**
- A defined target condition within "nasal cavity disease" (for example, allergic or vasomotor rhinitis, where caffeine is already used in combinations)
- Controlled clinical or well-designed preclinical evidence in nasal disease
- Mechanism of action data and label-based warnings and contraindications from the SmPC and BNF
- Confirmation of the product's dosage form, approved indication and route compatibility

**Other predicted indications of note:**
- **Hypnic headache** (score 99.17%): reviews and case series describe caffeine as a first-line option, but no controlled trials exist. This is classed as a research question and is the best-supported alternative.
- **Neuralgia** and **trigeminal autonomic cephalalgia** (L4): preclinical support and related headache literature, but no caffeine-specific trials.
- **Thrombotic disease** and **vein disease**: evidence is indirect, the direction of effect is unclear, and there are cardiovascular safety concerns. Both are on Hold.
- **Acute laryngopharyngitis, papillary conjunctivitis, glossodynia and coccygodynia** (L5): model predictions only, with no supporting studies.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

