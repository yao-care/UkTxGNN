---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 397
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Metformin: Classic stiff person syndrome
{: .text-alpha }

## One-Sentence Summary

Metformin is an established oral glucose-lowering medicine, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **no registered clinical trials** and **no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metformin is a biguanide whose efficacy in type 2 diabetes is well established, and the mechanistic link to stiff person syndrome cannot be verified from the data compiled for this report.

A speculative link is that metformin activates AMPK and has immunomodulatory effects, which might bear on an autoimmune, anti-GAD-associated disorder such as stiff person syndrome. A more likely explanation for the high score is shared autoimmunity: type 2 diabetes and related diabetes types frequently co-occur with stiff person syndrome through anti-GAD65 antibodies. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than any therapeutic effect.

The second-ranked prediction, focal stiff limb syndrome, has an identical score (0.9945). This suggests it is inherited from the closely related disease node rather than from independent evidence.

**Other predicted indications (all L5, Hold, no trials or literature):**

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Focal stiff limb syndrome | 0.9945 | Score identical to rank 1; likely inherited from a related disease. No plausible direct mechanism. |
| 3 | Opsismodysplasia | 0.9940 | Caused by INPPL1 (SHIP2) loss of function, affecting PI3K/AKT signalling. Only a loose pathway-level link to metformin's AMPK/mTOR effects. |
| 4 | Thiamine-responsive dysfunction syndrome | 0.9940 | Diabetes is a feature of the condition, which probably explains the association. Metformin would treat glycaemia at most; treatment is thiamine supplementation. |
| 5 | Drug-induced localised lipodystrophy | 0.9906 | Metformin improves insulin sensitivity in systemic lipodystrophy, but this localised form is mainly a cosmetic or injection-site issue. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0601022B0AAABAB | Metformin HCl Tablets 500 mg | Tablet (inferred from product name; not stated in the record) | Not stated in the licence record |

The record is a single valid, single-ingredient product. The identifier is not in the standard MHRA "PL" format and may be a BNF-style product code, so it should be checked against the MHRA register. NICE-appraised indications could not be cross-referenced from the data compiled for this report.

## Safety Considerations

**Contraindications (from knowledge graph drug-disease edges, not label text):**
The knowledge graph links metformin to the following conditions as contraindications. The list below is grouped and summarised.
- **Hepatic and renal:** liver failure, liver disease, kidney disease
- **Cardiac:** congestive heart failure
- **Pancreatic, biliary and urinary:** pancreatitis, gallbladder disease, pyoureter
- **Endocrine:** adrenocortical insufficiency, thymus gland disease, and a large group of pituitary-related conditions (hypopituitarism, pituitary deficiency, growth hormone deficiency, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome)

These come from a model knowledge graph rather than product labelling and must be verified against the SmPC.

**Drug Interactions:**
The interaction query returned 100 records; 20 are available for this report, of which two are rated Major:
- **Major:** acetazolamide, ethanol
- **Moderate (examples):** dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acetohexamide
- **Minor (examples):** acarbose, topical hydrocortisone, topical alclometasone

Label-based warnings and contraindications were not available, so please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications for any of the five predicted indications, and the apparent link to stiff person syndrome is most plausibly explained by co-occurring autoimmune diabetes rather than a therapeutic effect.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a mechanistic assessment
- Label-based warnings and contraindications from the SmPC and BNF, as the safety screen cannot proceed without them
- A systematic literature and trial search for metformin in stiff person syndrome and related stiff-limb disorders
- Preclinical or mechanistic evidence for an effect on anti-GAD-mediated autoimmunity
- Approved indication text and dosage form for the UK licence, plus confirmation of the MHRA licence number
- Route-of-administration compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

