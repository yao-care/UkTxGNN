---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Maraviroc: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Maraviroc"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

## Maraviroc: From an Unspecified Original Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Maraviroc is a CCR5 antagonist that is marketed in the UK as a 150 mg tablet; the data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but there are **no clinical trials** and **no publications** supporting this prediction.
This is a model-only prediction and should be treated as hypothesis-generating.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Maraviroc is a CCR5 antagonist. Detailed mechanism of action data are not available in the data compiled for this report, so this description reflects general knowledge of the drug class rather than a supplied source.

No established link exists between CCR5 blockade and the pathogenesis of multiple endocrine neoplasia (MEN). MEN is driven by alterations in genes such as MEN1, RET and CDKN1B. The high TxGNN score comes from knowledge-graph patterns alone and is not backed by any trial or publication. At present the prediction is not mechanistically supported.

### Other predictions reviewed

Other predicted indications with higher evidence levels are listed below for context. None has maraviroc-specific clinical data.

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| HER2 positive breast carcinoma | 99.22% | L4 | Preclinical work shows autocrine CCL5 contributes to trastuzumab resistance through ERK activation, which gives mechanistic support for CCR5 blockade. This is the most biologically supported of the predictions, and it is classed as a research question. |
| Cytomegalovirus infection | 99.23% | L4 | CMV encodes a chemokine receptor homologue (US28), so there is some plausibility. The linked paper is an observational study of immune markers in HIV, which gives only indirect context. |
| Primary cutaneous T-cell lymphoma | 99.72% | L5 | Chemokine receptors are expressed on skin-homing T cells. The only linked paper is a review on ACKR1, not on maraviroc. |
| Other predictions (acne, paediatric SLE, cutaneous B-cell lymphoma, candidiasis, complement C4A deficiency) | 99.24–99.76% | L5 | Prediction only, with no supporting maraviroc data. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010ADAAAAAA (BNF code) | Maraviroc tablets 150 mg | Tablet | Not available in the data compiled |

This is one valid single-ingredient product. The listed number is a BNF classification code, not a PL number, so the authorisation number should be confirmed against the MHRA register.

---

## Safety Considerations

**Contraindications from the knowledge graph.** These are drug–disease contraindication edges from the TxGNN knowledge graph (PrimeKG), not label text, and they should be verified against the SmPC. The conditions listed include:
- Liver and biliary disease: liver disease, drug-induced liver injury, gallbladder disease, chronic hepatitis B virus infection, hepatitis C virus infection
- Kidney disease: kidney disease, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure
- Cardiovascular disease: coronary artery disease, myocardial infarction, myocardial ischaemia, coronary thrombosis
- Orthostatic conditions: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- Other: hemoglobinopathy, pyoureter, infectious disease

**Drug interactions.** The interaction query returned 93 interactions. Examples from the first 20 records reviewed:
- **Major:** clarithromycin
- **Moderate:** aprepitant, dexamethasone, cimetidine, eliglustat, naltrexone, mannitol, clotrimazole, miconazole, papaverine, rolapitant, troglitazone, cobicistat, deferasirox, diazoxide, phentolamine, promethazine, amyl nitrite, epoprostenol, fostamatinib

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for multiple endocrine neoplasia rests on a graph-based score alone, with no trials, no literature and no plausible mechanistic link. Label-level safety data and the approved indication are also missing.

**To proceed, the following is needed:**
- The approved indication text, full SmPC warnings and contraindications for the UK product
- Mechanism of action data to support any mechanistic analysis
- Preclinical evidence linking CCR5 blockade to MEN biology
- Consideration of HER2-positive breast carcinoma as a better-supported research question, starting with preclinical validation of CCL5/CCR5 inhibition in trastuzumab resistance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

