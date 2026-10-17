---
layout: default
title: Budesonide
parent: Moderate Evidence (L3-L4)
nav_order: 113
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Budesonide: predicted new indication Atopic eczema (evidence level L4). Approved use: Crohn's disease, inflammatory bowel disease, asthma, allergic rhinitis"
monitor_inn: "Budesonide"
predicted_indications: ["atopic eczema", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Budesonide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Budesonide: From Crohn's Disease and Asthma to Atopic Eczema

## One-Sentence Summary

Budesonide is a glucocorticoid originally used for Crohn's disease, inflammatory bowel disease, asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but **no clinical trials** are registered for this indication, and the only directly relevant publication is a **preclinical formulation study**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, asthma, allergic rhinitis (UK licence indication text not available) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, budesonide is a glucocorticoid with broad anti-inflammatory and immunosuppressive activity. Its efficacy in inflammatory conditions of the gut and airways is established.

Atopic eczema is a Th2-driven inflammatory skin disease. Corticosteroids are a mainstay of treatment for it, so a mechanistic link is plausible. However, the data compiled for this report do not show direct clinical evidence for budesonide in this condition.

Note that the model also lists "dermatitis, atopic", which is the same disease and has been merged into this assessment. The second-ranked prediction, **bronchitis** (score 99.81%, Phase 2 and 4 trials, evidence level L2), has considerably stronger supporting evidence. It may be a more productive repurposing direction and is worth evaluating separately.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema.

---

## Literature Evidence

No randomised or clinical efficacy studies of budesonide in human atopic eczema were found. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical formulation study | Gels | Budesonide-loaded pH-sensitive nanoparticles in hydrogels developed for local therapy of paediatric atopic dermatitis; formulation work only |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Clinical study (safety) | Pediatric Dermatology | Knemometry in 14 children with atopic dermatitis treated with topical budesonide, assessing short-term growth effects |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Laboratory study | Int Immunopharmacol | Budesonide, unlike tacrolimus, affected immune functions of normal human keratinocytes |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review (safety) | Neuroimmunomodulation | Intranasal corticosteroids and adrenal suppression |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid allergy in patients with asthma |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Patch-test study | Contact Dermatitis | Budesonide is a marker for corticosteroid hypersensitivity; allergy trend decreasing |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Case report | Cureus | Steroid-induced angioedema and urticaria in a patient with atopic dermatitis |

Most other retrieved papers concern contact sensitisation, eosinophilic oesophagitis or veterinary dermatology, and do not support efficacy in this indication.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0105020A0AAACAC (BNF-style product code, not a PL number) | Budesonide capsules 3 mg (enteric-coated pellets) | Capsule (modified release) | Not available in the data compiled |

The product is in the BNF gastrointestinal chapter, consistent with its use in inflammatory bowel disease. No topical formulation for atopic eczema appears in the data.

---

## Safety Considerations

**Contraindications (knowledge graph associations, not label text):** The knowledge graph links budesonide with the following conditions, which should be checked against the SmPC:
- Cardiovascular and metabolic: hypertension, congestive heart failure, hyperglycaemia
- Hepatobiliary: liver disease, gallbladder disease
- Neurological: epilepsy
- Infection: measles, herpes simplex virus keratitis
- Endocrine: hypopituitarism and related pituitary deficiency disorders, growth hormone deficiency, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome
- Metabolic: urea cycle disorders (carbamoyl phosphate synthetase I deficiency, citrullinaemia, hyperargininaemia)

**Drug Interactions:** 100 interactions were identified. Examples:
- **Major:** adalimumab, fosamprenavir
- **Moderate:** zidovudine, isotretinoin, acebutolol, ketorolac, nifedipine, ibuprofen, ethinylestradiol, fluvoxamine, alemtuzumab, aldesleukin
- **Minor:** formoterol, salbutamol

**Topical use concerns from the literature:**
- Growth and bone turnover effects in children treated with topical corticosteroids
- Adrenal suppression
- Contact allergy to corticosteroids, for which budesonide is a recognised marker

Report suspected adverse reactions via the Yellow Card Scheme. Please refer to the SmPC and BNF for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is very high (99.96%), but the evidence is limited to model prediction, a plausible glucocorticoid mechanism and one preclinical formulation paper. There are no registered clinical trials, and many established topical corticosteroids already exist for atopic eczema.

**To proceed, the following is needed:**
- A systematic search for clinical studies of topical budesonide in atopic eczema, including in children
- Mechanism of action data and UK licence indication text
- Confirmation of an available topical formulation, as the only UK product identified is an oral enteric-coated capsule
- A comparison against existing standard topical corticosteroids, with a safety plan covering growth, adrenal suppression and contact allergy
- Consideration of prioritising the **bronchitis** prediction, where Phase 2 and 4 trial data already exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

