---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
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

# Propylene Glycol: From Dry Eye Syndrome to Bronchitis

## One-Sentence Summary

Propylene glycol is a solvent and humectant, originally associated with the treatment of dry eye syndrome and xerophthalmia.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** and only **3 publications** were found, and none of these supports a therapeutic benefit. The retrieved literature instead points towards a potential respiratory harm signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry eye syndrome; xerophthalmia (from the TxGNN knowledge graph, as no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propylene glycol is a solvent and humectant used in ophthalmic and other preparations. Its use in dry eye relates to lubrication and moisture retention at the ocular surface.

No plausible therapeutic link to bronchitis could be identified. The retrieved literature describes propylene glycol as a constituent of e-cigarette liquids that may be associated with airway irritation and lung disease. This is a potential harm signal rather than a benefit. The high TxGNN score is not supported by clinical evidence and is likely an artefact of knowledge-graph propagation.

Other predictions (for example diabetic retinopathy and several types of cataract) have also been reviewed. None has a credible mechanism or supportive clinical evidence. Some retrieved studies concern a different compound (propylene glycol mannate sulfate) or use propylene glycol only as a formulation excipient, which is likely name-matching noise.

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews whether chronic e-cigarette use may cause lung disease, including chronic bronchitis and COPD; a potential harm signal, not evidence of benefit |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette liquids and aerosols contain airway irritants implicated in worsening lung disease, including asthma |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal) | Respir Res | Quercetin reduced lung inflammation in a COPD mouse model; unrelated to propylene glycol |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190400000AAAWAW | Propylene Glycol (liquid) | Not specified | Not specified |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials for bronchitis, no plausible mechanism, and the available literature suggests possible airway irritation rather than benefit.

**To proceed, the following is needed:**
- Mechanism of action data to assess any biological link to bronchitis
- Product-level information, including approved indication text and dosage form for the UK authorisation
- Warnings and contraindications from the SmPC and BNF, to allow safety screening
- Any evidence from controlled studies of propylene glycol itself in respiratory disease, particularly given the inhalation safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

