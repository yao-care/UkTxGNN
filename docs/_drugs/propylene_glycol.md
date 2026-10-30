---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
monitor_inn: "Propylene glycol"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic cataract", "mature cataract", "immature cataract", "craniostenosis cataract"]
last_modified_at: 2026-10-30
description: "Propylene Glycol: predicted new indication Bronchitis (evidence level L5). Approved use: Dry eye syndrome and xerophthalmia"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Propylene Glycol: From Dry Eye Syndrome to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Propylene glycol is mainly known as a solvent and humectant, and dry eye syndrome and xerophthalmia are recorded as its original uses.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** and **3 publications** are linked to this prediction, and none of them supports a benefit.
The available signal points towards possible respiratory harm, not benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry eye syndrome and xerophthalmia (relations recorded in the knowledge graph; the UK licence record contains no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Propylene glycol is widely used as a humectant, solvent and excipient. The dry eye and xerophthalmia relations are not approved indications taken from licence text.

The prediction does not appear to have a therapeutic basis. The retrieved literature concerns inhaled propylene glycol as an e-cigarette constituent, where it is a potential airway irritant linked to respiratory harm. The third paper is a mouse study of quercetin and is unrelated to propylene glycol. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it is not supported by clinical or mechanistic evidence.

Because no cited study directly examines propylene glycol as a treatment for bronchitis, the evidence level is L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews whether chronic e-cigarette use may cause lung disease; chronic bronchitis is discussed as part of tobacco-related COPD. It does not show a benefit of propylene glycol. |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette liquids and aerosols contain airway irritants and toxicants implicated in worsening lung disease, including asthma. |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal) | Respir Res | Quercetin reduced lung inflammation in a mouse COPD model. Unrelated to propylene glycol. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190400000AAAWAW | Propylene Glycol_Liq | Not stated | Not stated |

This is a single-ingredient product with a valid status. The record contains no indication text, so no approved indication can be described from it.

---

## Safety Considerations

- **Respiratory signal:** The retrieved literature describes inhaled propylene glycol, as an e-cigarette constituent, as a potential airway irritant linked to respiratory harm. This is relevant to any proposed use in bronchitis.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials exist, and the literature points towards possible harm to the airways, not benefit. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible therapeutic rationale for bronchitis
- Direct clinical or preclinical studies of propylene glycol in bronchitis
- Review of the inhalation safety signal
- Labelled indication, dosage form and safety information for the UK-authorised product

---

### Note on other predictions

The other highest-ranked predictions (severe non-proliferative diabetic retinopathy, diabetic retinopathy and several cataract types) are also **Hold**. Most are at L5 with no trials or publications. For diabetic retinopathy, the one trial (NCT07090044) tests post-injection pain drops and not propylene glycol as a treatment. The one related publication (PMID 39006273) concerns propylene glycol mannate sulfate, a different compound. The other two are formulation studies where propylene glycol is probably an excipient. No cited study directly addresses propylene glycol as a treatment for diabetic retinopathy, so that indication is also L5 under the evidence rules.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

