---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is an alpha-1A/1D adrenergic antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are **0 clinical trials** and **0 supporting publications** for this indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (the licence record holds no approved indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Tamsulosin is generally known as an alpha-1A/1D adrenoceptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which relieves urinary symptoms in BPH.

Ambras-type hypertrichosis is a rare developmental disorder. It is linked to chromosome 8q23 rearrangements that affect regulation of the *TRPS1* gene. No plausible mechanism connects alpha-1 adrenergic blockade to this condition, and the original mechanism data are missing, so the link cannot be cross-checked. The high score most likely reflects proximity in the knowledge graph, not a therapeutic rationale.

The other top-ranked predictions are mostly hair or congenital malformation conditions: hypertrichosis, hair shaft abnormalities, hypotrichosis, alopecia areata and migraine with brainstem aura. None has trial or literature support, and none has a recognised mechanistic basis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For context, the ninth-ranked prediction, alopecia, returned two publications. Neither supports tamsulosin as a treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Cohort / pharmacovigilance | JAMA Dermatology | Suicidality and psychological adverse events with finasteride, a different drug; not tamsulosin efficacy |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Cross-sectional | Cornea | Meibomian gland changes in men with BPH; unrelated to hair loss |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704010U0AAAAAA (BNF-style code, not a PL number) | Tamsulosin HCl capsules 400 microgram modified-release | Modified-release capsule | Not stated in the data compiled for this report |

## Safety Considerations

- **Conditions flagged as contraindications or cautions in the knowledge graph** (these are graph associations, not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism and intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified. One is rated Major: **clarithromycin**. Moderate-rated examples include bupropion, aprepitant, morphine, cimetidine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, miconazole, clotrimazole, fenfluramine and opium.
- **Other considerations**: Tamsulosin can cause orthostatic hypotension and dizziness. This matters for any new population, including patients with migraine.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by the model score only (L5). No trials or publications exist, and no plausible mechanism links alpha-1 blockade to Ambras-type hypertrichosis. Pursuing this indication is not justified on current data.

**To proceed, the following is needed:**
- Mechanism of action data for tamsulosin, to allow a proper mechanistic assessment
- Preclinical or mechanistic evidence linking alpha-1A/1D antagonism to hair follicle or *TRPS1* biology
- The licence's approved indication text and dosage form, and the full SmPC warnings and contraindications
- Review of the lower-ranked predictions for any with a stronger biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

