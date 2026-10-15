---
layout: default
title: Methyl Aminolevulinate
parent: Model Prediction Only (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Methyl Aminolevulinate
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

# Methyl Aminolevulinate: From Its Licensed Dermatological Use to Acne (Disease)

## One-Sentence Summary

Methyl aminolevulinate (MAL) is a topical photosensitiser prodrug used in photodynamic therapy (PDT) of the skin, marketed in the UK as Metvix cream 16%.
The TxGNN model's top-ranked prediction was hereditary haemochromatosis, but that prediction has no supporting evidence. The best-supported candidate is **acne (disease)**, which has **2 completed Phase 2 trials** and **8 publications**, mostly reviews.
This report therefore focuses on acne and briefly compares the other predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the literature describes approved use in actinic keratosis, basal cell carcinoma and Bowen's disease) |
| Predicted New Indication | Acne (disease). Rank 1 by score was hereditary haemochromatosis, but it has no evidence, so the best-supported prediction is presented here |
| TxGNN Prediction Score | Acne: 99.81% (hereditary haemochromatosis, rank 1: 99.86%) |
| Evidence Level | L2 (acne) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold for hereditary haemochromatosis; Proceed with Guardrails (research question only) for acne |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known information, MAL is a prodrug that is converted to protoporphyrin IX (PpIX) through the haem biosynthesis pathway. After illumination with red light, PpIX generates reactive oxygen species that destroy the target cells.

For acne, MAL is taken up by sebaceous glands and *Cutibacterium acnes*, where it is converted to PpIX. Light activation may reduce sebaceous gland activity and bacterial load. This is a plausible extension of MAL-PDT from hyperproliferative skin lesions to a pilosebaceous disease.

Several other predictions (psoriasis, common wart) have a similar rationale. Others lack one. Hereditary haemochromatosis, Wilson disease, iron metabolism disease and drug-induced osteoporosis are systemic metabolic or bone conditions, and a topical photodynamic agent has no plausible role in them. Their high scores likely reflect the link between the haem pathway and iron handling in the knowledge graph rather than a treatable mechanism.

---

## Clinical Trial Evidence

Trials for acne:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00594425](https://clinicaltrials.gov/study/NCT00594425) | Phase 2 | Completed | 150 | MAL-PDT in moderate to severe facial acne vulgaris. Open-label dose-escalation phase followed by a blinded, randomised, vehicle-controlled dose-response phase. Results were not provided. |
| [NCT00673933](https://clinicaltrials.gov/study/NCT00673933) | Phase 2 | Completed | 20 | Blinded, randomised, intra-individual, vehicle-controlled multicentre study of MAL-PDT in skin type V or VI with acne vulgaris. Results were not provided. |

No registered trials were found for the other predicted indications.

---

## Literature Evidence

Acne:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22949035](https://pubmed.ncbi.nlm.nih.gov/22949035/) | 2013 | Retrospective cohort | Photochem Photobiol Sci | Real-life off-label MAL-PDT in 20 Italian departments (inflammatory and aesthetic indications) |
| [38243786](https://pubmed.ncbi.nlm.nih.gov/38243786/) | 2024 | Review | J Cutan Med Surg | PDT is approved for actinic keratoses and low-risk non-melanoma skin cancers, with emerging indications |
| [15888131](https://pubmed.ncbi.nlm.nih.gov/15888131/) | 2005 | Review | Photodermatol Photoimmunol Photomed | PDT benefit is also evident in inflammatory dermatoses, including acne vulgaris |
| [20944910](https://pubmed.ncbi.nlm.nih.gov/20944910/) | 2010 | Review | An Bras Dermatol | MAL is approved for actinic keratosis, basal cell carcinoma and Bowen's disease |
| [23986167](https://pubmed.ncbi.nlm.nih.gov/23986167/) | 2013 | Review | J Drugs Dermatol | MAL-PDT has efficacy similar to ALA-PDT with a shorter incubation time |
| [16566733](https://pubmed.ncbi.nlm.nih.gov/16566733/) | 2006 | Review | J Environ Pathol Toxicol Oncol | MAL is postulated to have the highest selectivity in topical PDT |
| [28809342](https://pubmed.ncbi.nlm.nih.gov/28809342/) | 2013 | Review | Materials (Basel) | Overview of dye sensitisers, including use in acne vulgaris |
| [17598868](https://pubmed.ncbi.nlm.nih.gov/17598868/) | 2007 | Case series | Photodermatol Photoimmunol Photomed | Seven patients with chronic folliculitis in acne-prone skin successfully treated with MAL-PDT |

Other predictions with some literature (reviews, retrospective analyses and case reports only; ALA-based and combination-technique studies confound attribution to MAL):
- **Common wart:** case reports and a 51-patient case series of recalcitrant warts treated with MAL-PDT ([19614904](https://pubmed.ncbi.nlm.nih.gov/19614904/), [31209587](https://pubmed.ncbi.nlm.nih.gov/31209587/)), a retrospective analysis ([22949076](https://pubmed.ncbi.nlm.nih.gov/22949076/)), and a randomised trial of PDT versus trichloroacetic acid in condylomata ([34333146](https://pubmed.ncbi.nlm.nih.gov/34333146/)).
- **Psoriasis:** reviews and a retrospective off-label analysis ([22949035](https://pubmed.ncbi.nlm.nih.gov/22949035/)). No MAL-specific efficacy has been established.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1308010X0BBAAAA | Metvix Cream 16% | Not stated | Not stated |
| 1308010X0AAAAAA | Methyl-5-Aminolevulinate Cream 16% | Not stated | Not stated |

Both authorisations are valid single-ingredient products. Dosage form and indication text were not available in the compiled data. Please check the current MHRA record, the SmPC and the BNF.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): photosensitivity disease and photoparoxysmal response.
- **Drug Interactions:** no interactions were found in the compiled data.

Please refer to the SmPC and BNF for full warnings and contraindications. Trial outcome data on adverse events such as pain and erythema were not provided. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold for hereditary haemochromatosis and the other systemic predictions; Proceed with Guardrails (research question only) for acne**

**Rationale:**
- Hereditary haemochromatosis ranks highest on score but has no trials or literature, and a topical PDT agent is not a plausible systemic therapy. It should be held.
- Acne has two completed Phase 2 trials, but no results, no Phase 3 confirmation, and mostly review-level literature. It is a credible research question rather than a ready-to-adopt indication.

**To proceed, the following is needed:**
- Published results (efficacy and adverse events) from NCT00594425 and NCT00673933
- Phase 3 or other confirmatory randomised evidence in acne
- The licensed indication, dosage form and label safety information from the SmPC and BNF
- Mechanism of action data for MAL
- A review of the photosensitivity contraindication signals in the intended population
- Further evidence before pursuing common wart or psoriasis, which currently rest on case reports, retrospective analyses and reviews
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

