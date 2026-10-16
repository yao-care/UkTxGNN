---
layout: default
title: Crotamiton
parent: Model Prediction Only (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Crotamiton: predicted new indication Trombiculiasis (evidence level L5). Approved use: Scabies, Norwegian scabies…"
---

# Crotamiton
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

# Crotamiton: From Scabies to Trombiculiasis

## One-Sentence Summary

Crotamiton is a topical scabicide and antipruritic, originally used to treat scabies (including Norwegian scabies) and other mite infestations.
The TxGNN model predicts it may be useful for **trombiculiasis** (chigger infestation), but there are currently **no registered clinical trials and no publications** in the data compiled for this report, so support is from the model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Scabies, Norwegian scabies, mite infestation (the approved indication text for the listed authorisation is not available) |
| Predicted New Indication | Trombiculiasis |
| TxGNN Prediction Score | 96.24% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for crotamiton. It is described as a scabicidal agent with an unknown mechanism. As a general antipruritic, it has been reported to inhibit the TRPV4 (transient receptor potential vanilloid 4) channel, which is expressed in the skin and in primary sensory neurons. This may explain its itch-relieving effect.

Trombiculiasis is a pruritic dermatitis caused by mite larvae (chiggers). Scabies is also a mite infestation, so the two conditions share a pathology of mite-related skin irritation and itch. Crotamiton's scabicidal and antipruritic activity therefore gives a plausible, though indirect, link.

This link rests on shared pathology rather than a defined molecular target. The prediction should be treated as a research hypothesis. Crotamiton's antipruritic action could relieve symptoms, but there is no evidence yet that it treats the infestation itself.

Other top-ranked predictions (for example lymph node palisaded myofibroblastoma, abdominal cystic lymphangioma and sacrum chordoma) have no plausible mechanistic link to crotamiton and are likely artefacts of the graph-based model. They are not pursued in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1303000I0AAAAAA | Crotamiton Cream 10% | Cream (topical) | Not stated in the compiled data |

The compiled data list one valid single-ingredient authorisation. Its dosage form, manufacturer and approved indication text are not provided, and the authorisation number is not in the usual MHRA PL format, so it should be verified against the MHRA register before use.

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The TxGNN knowledge graph records a drug-disease contraindication link with **dermatitis**. This is not drawn from product labelling and should be checked against the SmPC, particularly as trombiculiasis is itself a dermatitis.
- **Drug Interactions**: No conventional drug-drug interactions were identified. The only pharmacology entry is crotamiton's inhibitory action on its target, TRPV4.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trombiculiasis is mechanistically plausible because it is a mite-related itchy dermatitis, but it rests only on the TxGNN score. There are no trials or publications, the mechanism of action is incompletely defined, and a knowledge-graph contraindication with dermatitis needs to be resolved.

**To proceed, the following is needed:**
- A systematic literature search for crotamiton use in trombiculiasis (chigger bites) and related mite-induced itch
- Clarification of the dermatitis contraindication signal against the UK SmPC
- Full authorisation details from the MHRA register (PL number, dosage form, approved indication)
- Mechanism of action data, including confirmation of the TRPV4 antipruritic effect and any acaricidal activity against chigger larvae
- A small exploratory clinical study, if the literature review is supportive, focusing on symptom relief
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

