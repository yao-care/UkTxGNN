---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 315
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (no approved indication text is available in the UK authorisation data) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, glimepiride is a sulfonylurea that blocks pancreatic K-ATP channels and stimulates insulin secretion. Its efficacy in type 2 diabetes is established.

No mechanistic link to focal stiff limb syndrome is supported. This is a rare autoimmune or neurological disorder involving the GABAergic and glycinergic systems, and a sulfonylurea has no known action on these pathways. The high score (0.997) most likely reflects a knowledge-graph association with diabetes-related autoimmunity, such as anti-GAD antibodies, rather than a therapeutic rationale.

The other top-ranked predictions show the same pattern. Classic stiff person syndrome (score 99.75%) is linked to diabetes through anti-GAD65 autoimmunity. Opsismodysplasia (99.74%) touches insulin signalling through SHIP2, but only speculatively. Thiamine-responsive dysfunction syndrome (99.73%) includes diabetes as a feature. The localised lipodystrophies (99.5–99.6%) are probably artefacts of the insulin-treatment context. Pancreatic agenesis (99.55%) is biologically implausible, because glimepiride needs residual functioning beta cells. None of these has supporting trials or relevant literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (focal stiff limb syndrome).

The only publication retrieved for any of the top predictions concerns pancreatic agenesis (rank 9) and is not relevant to treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/) | 2003 | Review / diagnostic imaging study | European Journal of Endocrinology | Pitfalls in endosonographic imaging of suspected insulinomas; concerns misleading pancreatic nodules, not drug treatment |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0601021A0AAAAAA (as recorded; not in standard PL format) | Glimepiride tablets 2 mg | Tablet | Not stated in the data compiled |

Glimepiride is a single-ingredient product with one valid authorisation and none cancelled. In the BNF it falls under drugs used in diabetes (sulfonylureas). Please check the current SmPC and any NICE guidance for the full approved indications.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from model graph data, not from label text, and should be verified against the SmPC):
- Kidney disease and liver disease
- Congestive heart failure
- Gallbladder disease
- Pituitary hormone deficiencies, including hypopituitarism and Sheehan syndrome
- Hypogonadotropic hypogonadism and Kallmann syndrome
- Osteoporosis, including postmenopausal osteoporosis
- Thymus gland disease and infectious disease

**Drug Interactions:** The interaction screen returned 100 interactions, and 20 are shown in the data compiled. Most are of moderate severity. Examples:
- Beta-agonists and sympathomimetics: salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine
- Acebutolol (a beta-blocker)
- Acid suppressants: famotidine, ranitidine
- NSAIDs: ibuprofen, ketorolac
- Hydrochlorothiazide and acetazolamide
- Hydrocortisone and ethinylestradiol
- Albiglutide
- Ethanol
- Acitretin and nitazoxanide

Topical corticosteroids (hydrocortisone, alclometasone) were rated minor.

Product-label warnings were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. There are no clinical trials or relevant publications, and there is no plausible mechanism linking a sulfonylurea to focal stiff limb syndrome. The score likely reflects graph proximity to diabetes and anti-GAD autoimmunity.

**To proceed, the following is needed:**
- Confirmed mechanism of action data and a credible biological rationale for stiff limb syndrome
- A systematic literature search for any preclinical or clinical signal
- Review of SmPC warnings and contraindications to complete the safety assessment
- The approved indication text and dosage form for the UK authorisation
- Preclinical or mechanistic studies before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

