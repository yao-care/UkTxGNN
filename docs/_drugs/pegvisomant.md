---
layout: default
title: Pegvisomant
parent: Model Prediction Only (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pegvisomant: predicted new indication Borderline ovarian serous tumour (evidence level L5). Approved use: Acromegaly"
monitor_inn: "Pegvisomant"
predicted_indications: ["borderline ovarian serous tumor", "rete ovarii cystadenoma", "ovarian papillary cystadenoma", "pyelonephritis", "malignant ovarian Brenner tumor", "aleukemic mast cell leukemia", "ovarian mucinous cystadenofibroma", "ovarian benign neoplasm", "mucinous ovarian cystadenoma", "ovarian surface papilloma"]
---

# Pegvisomant
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

# Pegvisomant: From Acromegaly to Borderline Ovarian Serous Tumour

## One-Sentence Summary

Pegvisomant was originally used to treat acromegaly (a condition of excess growth hormone, also linked to hyperpituitarism).
The TxGNN model predicts it may be effective for **borderline ovarian serous tumour**, but there are currently **no clinical trials and no publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly; hyperpituitarism (from the knowledge graph, as no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Borderline ovarian serous tumour |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

Other top-ranked predictions all share the same L5 evidence level and a Hold recommendation: rete ovarii cystadenoma (98.60%), ovarian papillary cystadenoma (98.60%), pyelonephritis (98.57%), malignant ovarian Brenner tumour (98.56%), aleukaemic mast cell leukaemia (98.56%), ovarian mucinous cystadenofibroma (98.54%), ovarian benign neoplasm (98.54%), mucinous ovarian cystadenoma (98.53%) and ovarian surface papilloma (98.51%).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Pegvisomant is, however, generally known as a growth hormone (GH) receptor antagonist that lowers circulating IGF-1. Its efficacy in acromegaly rests on reducing the effects of excess GH.

The GH/IGF-1 axis has been implicated in the proliferation of some epithelial ovarian tumours. This gives a plausible but unverified link between the original indication and the predicted one. The high score appears to reflect a shared neighbourhood with other ovarian neoplasm terms in the knowledge graph rather than direct evidence.

Several of the other predictions are weaker still. Benign ovarian lesions are usually managed surgically, so the need for drug therapy is unclear. For pyelonephritis (a bacterial kidney infection treated with antimicrobials) and mast cell leukaemia (typically KIT-driven), no clear mechanistic rationale is apparent, and these may be knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0605010Z0AAACAC | Pegvisomant Inj 20mg Vl + Dil | Injection (vial with diluent) | Not available in the compiled data |

This identifier follows the BNF-style code format (BNF chapter 6, endocrine system) rather than a standard MHRA PL number, so the MHRA authorisation details should be verified. No NICE-appraised indication data were available.

## Safety Considerations

**Drug Interactions**: 74 potential interactions were identified. The ones listed here are all of moderate severity. The main groups are:
- **Antidiabetic agents** (the largest group): acarbose, metformin, pioglitazone, glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide, human insulin, insulin aspart. Newer agents also appear: albiglutide, dulaglutide, exenatide, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin. Pegvisomant may alter glucose control, so closer glucose monitoring and dose review may be needed when co-prescribed.
- **Other**: morphine, pegvaliase.

For all other safety information, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (98.63%) with a speculative GH/IGF-1 rationale. There are no clinical trials or publications for borderline ovarian serous tumour or any of the other nine predictions.

**To proceed, the following is needed:**
- Mechanism of action data for pegvisomant to support the mechanistic-link analysis
- Warnings and contraindications from the SmPC and BNF, which are needed before safety screening can proceed
- Approved indication text and dosage form details for the UK authorisation
- Preclinical or literature evidence linking GH receptor antagonism to ovarian epithelial tumour growth
- Assessment of the clinical need for drug therapy, since benign ovarian lesions are usually treated surgically
- Evaluation of route compatibility and similarity to the original indication, both currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

