---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tropicamide: From Ophthalmic Mydriasis/Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting antimuscarinic agent used topically in ophthalmology to dilate the pupil and induce cycloplegia for eye examinations.
The TxGNN model predicts it may be relevant to **Cauda Equina Syndrome**, but currently **no clinical trials and no published literature** support this direction, and the model's own rationale flags the mechanistic link as implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ophthalmic mydriasis and cycloplegia (topical eye drop use; not confirmed via UK regulatory licensing data, as no licences are currently on file) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (blocking data gap, DG002). Based on general pharmacological knowledge, tropicamide is a short-acting M3/M4 muscarinic receptor antagonist administered exclusively as a topical ophthalmic solution; systemic absorption following ocular instillation is minimal.

Cauda equina syndrome is a surgical emergency caused by mechanical compression of the nerve roots below the spinal cord conus (e.g. disc herniation, tumour, trauma), requiring urgent decompressive surgery. Its pathology is mechanical, not related to cholinergic signalling. The evidence pack's own mechanistic assessment explicitly states that there is no plausible pharmacological connection between an antimuscarinic eye drop and this condition, and suggests the TxGNN score likely reflects knowledge-graph co-occurrence noise rather than a genuine biological relationship.

For context, two lower-ranked candidates in this evidence pack (neurogenic bladder and irritable bowel syndrome) do have a class-level rationale — other antimuscarinics (oxybutynin, dicyclomine) are used systemically for these conditions — but tropicamide's ultra-short half-life and topical-only formulation make systemic extrapolation to any of the three predicted indications mechanistically weak, and none is supported by trial or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Tropicamide is not currently marketed in the UK under this evaluation, and no marketing authorisations are on file.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: label warnings and contraindication data for this candidate are currently unavailable (blocking data gap, DG001), which prevents completion of the initial safety assessment stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial or literature evidence, and the model's own mechanistic rationale indicates the drug-disease link is biologically implausible given tropicamide's topical-only formulation and minimal systemic exposure. A blocking data gap in product warning/contraindication data also prevents progression to safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/MHRA label warnings and contraindications (currently blocking, DG001)
- Detailed mechanism of action data (DG002)
- Any preclinical or pharmacokinetic data supporting systemic exposure relevant to non-ophthalmic use
- Independent confirmation of mechanistic plausibility before further evidence collection is warranted, given the two lower-ranked candidates (neurogenic bladder, irritable bowel syndrome) in this pack show the same lack of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

