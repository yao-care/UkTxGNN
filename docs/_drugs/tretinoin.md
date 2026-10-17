---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tretinoin: predicted new indication Rheumatoid nodulosis (evidence level L5). Approved use: Acne, acute promyelocytic leukaemia, acquired keratosis…"
monitor_inn: "Tretinoin"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "spondyloarthropathy, susceptibility to", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
---

# Tretinoin
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

# Tretinoin: From Acne and Acute Promyelocytic Leukaemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (a retinoid, all-trans retinoic acid) was originally used for acne, acute promyelocytic leukaemia, and keratinisation disorders such as acquired keratosis and palmoplantar keratoderma.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but there are currently **0 clinical trials** and **no relevant publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, acute promyelocytic leukaemia, acquired keratosis, palmoplantar keratoderma (the MHRA licence data compiled for this report contains no indication text) |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, tretinoin is a retinoid whose efficacy in acne and acute promyelocytic leukaemia is established, and it may be mechanistically applicable to inflammatory conditions through immune modulation.

Retinoic acid is known to influence T-cell differentiation (for example the Th17/Treg balance) and inflammatory cytokine signalling. This could plausibly relate to rheumatoid disease. However, the data compiled for this report documents no direct link between tretinoin and rheumatoid nodulosis.

The prediction should therefore be regarded as speculative. The relationship between the original indications (dermatological and haematological) and the predicted indication (a rheumatoid disease manifestation) is not established by any evidence retrieved.

Other top-ranked predictions are also arthritis-related, with similar scores of about 99.8%. These are rheumatoid factor-positive polyarticular juvenile idiopathic arthritis, juvenile idiopathic arthritis, juvenile chronic polyarthritis, and a genetic susceptibility to spondyloarthropathy. This clustering suggests the model may be responding to network proximity among arthritis terms rather than to a specific biological mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for rheumatoid nodulosis.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1306010V0AAAFAF | Tretinoin Gel 0.01% | Topical gel (as named in the product record) | Not stated in the data compiled |

This is a single-ingredient product with valid status. The record carries no PL-format number, manufacturer, or indication text, so the identifier and details should be verified against the MHRA register. Note that this is a topical product, whereas the predicted systemic inflammatory indication would likely require a different route of administration; route compatibility has not been assessed.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Differentiating agent (retinoid) used in acute promyelocytic leukaemia; not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions** (100 interactions were identified; the main ones are listed):
  - **Major:** doxycycline, tetracycline, minocycline (tetracyclines), and vitamin A
  - **Moderate:** aprepitant, clarithromycin, naltrexone
  - **Minor:** levofloxacin
  - Other interactions of unclassified severity were recorded, including with calcitriol, proton pump inhibitors, mesalazine, morphine, metformin, prednisone, hydrocortisone and amphotericin B.
- **Disease associations flagged as potential contraindications** (from knowledge-graph data, not product label text): sunburn, kidney disease, liver disease, pancreatitis, gallbladder disease, congestive heart failure, diabetes mellitus and diabetic ketoacidosis, inflammatory bowel disease (including Crohn's disease), atopic eczema, osteoporosis, adrenocortical insufficiency, psychiatric disorders (anxiety, psychotic and other mental disorders), and cutaneous T-cell lymphomas (including mycosis fungoides).
- **Additional considerations for the predicted indications:** systemic retinoids carry known teratogenicity and bone and growth effects, which are particularly relevant to the juvenile arthritis and skeletal dysplasia predictions.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone (L5). No clinical trials or relevant literature support tretinoin in rheumatoid nodulosis, and the two publications retrieved for osteoarthritis (a lower-ranked prediction) are unrelated to tretinoin efficacy.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological link between retinoid signalling and rheumatoid nodulosis
- Preclinical or observational evidence in rheumatoid disease
- Verified MHRA licence details (PL number, formulation, approved indications) and an assessment of route compatibility
- A safety review covering systemic retinoid risks, particularly teratogenicity, and the major interactions listed above
- Complete warnings and contraindication data from the SmPC and BNF
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

