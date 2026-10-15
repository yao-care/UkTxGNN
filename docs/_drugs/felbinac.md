---
layout: default
title: Felbinac
parent: Model Prediction Only (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Felbinac
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

# Felbinac: From Osteoarthritis to Brachyolmia-Amelogenesis Imperfecta Syndrome

## One-Sentence Summary

Felbinac is a topical non-steroidal anti-inflammatory drug (NSAID) originally used for osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **brachyolmia-amelogenesis imperfecta syndrome**, but **no clinical trials and no publications** currently support this prediction, so it rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis and arthropathy (from the TxGNN knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Brachyolmia-amelogenesis imperfecta syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, felbinac is a topical NSAID that works by inhibiting cyclooxygenase (COX) enzymes and reducing prostaglandin-driven inflammation and pain. Its use in osteoarthritis and arthropathy is established, and it is applied locally to musculoskeletal sites.

The predicted condition is a rare genetic skeletal and dental disorder (related to LTBP3). It has no known COX-driven inflammatory mechanism. The high TxGNN score most likely reflects proximity in the knowledge graph to the original joint and bone indications, not a biological rationale. At best, any benefit would be speculative symptom relief rather than disease modification.

Other top-ranked predictions show the same pattern:

- **Genetic skeletal dysplasias** (acromesomelic dysplasia Hunter-Thompson type, brachyolmia, pseudoachondroplasia): no disease-modifying rationale.
- **Myosclerosis**: only a speculative link at the level of symptom relief.
- **Inflammatory joint conditions** (spondyloarthropathy susceptibility, rheumatoid nodulosis, juvenile idiopathic arthritis and its rheumatoid factor-positive polyarticular subtype): NSAIDs are used for symptom control, so these are more plausible. However, the topical formulation has no supporting evidence in these settings, and disease management relies mainly on other treatments.
- **Combined immunodeficiency due to moesin deficiency**: no rationale for an NSAID benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1003020M0AAAAAA | Felbinac Gel 3% | Gel (topical) | Not available in the data compiled for this report |

The authorisation number above is shown as recorded in the compiled data and does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score. There are no clinical trials or publications, and the proposed conditions have no plausible COX-inhibition mechanism. The more biologically plausible predictions (juvenile idiopathic arthritis, spondyloarthropathy) are also unsupported by evidence for the topical formulation.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic assessment
- Approved indication text and SmPC safety information (warnings and contraindications) for the UK product
- Any preclinical, observational or clinical evidence for felbinac in the predicted conditions
- If pursuing a more plausible target, a review of inflammatory joint conditions such as juvenile idiopathic arthritis, including paediatric safety and route suitability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

