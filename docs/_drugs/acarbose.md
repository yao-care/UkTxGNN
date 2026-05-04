---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acarbose: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is a well-established alpha-glucosidase inhibitor used internationally for the management of type 2 diabetes mellitus, though it does not currently hold an MHRA marketing authorisation in the United Kingdom.
The TxGNN model predicts it may have potential in **Focal Stiff Limb Syndrome**, a rare anti-GAD65-mediated autoimmune neurological condition.
At present, **no clinical trials** and **no published literature** directly support this repurposing direction — the evidence base is entirely model-driven.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 diabetes mellitus (alpha-glucosidase inhibitor; no UK MHRA authorisation on record) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| UK Market Status | Not authorised |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Acarbose is an alpha-glucosidase inhibitor that competitively inhibits intestinal brush-border enzymes responsible for carbohydrate digestion, delaying glucose absorption from the gut and blunting postprandial blood glucose peaks. Its proven clinical utility lies in reducing postprandial hyperglycaemia in type 2 diabetes, either as monotherapy or in combination.

Focal stiff limb syndrome is a rare autoimmune neurological disorder driven by anti-GAD65 antibodies. GAD65 (glutamic acid decarboxylase 65) is expressed both in GABAergic interneurones of the central nervous system and in pancreatic beta cells. The speculative mechanistic bridge proposes that Acarbose, by attenuating glucose-driven beta cell stimulation, may indirectly reduce GAD65 antigen exposure, potentially dampening the autoimmune cascade. This is an entirely theoretical pathway at the level of molecular conjecture, with no experimental validation in neural tissue, no in vivo model data, and no clinical precedent.

The TxGNN model's high confidence score most likely reflects a graph topology artefact — shared knowledge nodes connecting "diabetes," "autoimmunity," and "neurological disease" — rather than a biologically validated repurposing signal. Clinicians should treat high TxGNN scores for rare neurological autoimmune conditions with caution when direct mechanistic and empirical evidence is absent.

---

## Clinical Trials

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Acarbose does not currently hold any MHRA marketing authorisation and is not recorded as a marketed product in the United Kingdom in this Evidence Pack.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| — | — | — | No UK authorisations on record |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a knowledge graph model score with no supporting clinical trials, published literature, or validated mechanistic evidence linking Acarbose to focal stiff limb syndrome or any related anti-GAD65 autoimmune neurological condition. The biological plausibility is highly speculative, and the drug lacks UK marketing authorisation in any indication.

**To proceed beyond Hold, the following would be needed:**

- Preclinical evidence (in vitro or animal model) demonstrating any modulating effect of Acarbose on GAD65 autoantibody production or GABAergic neuronal protection
- Pharmacological MOA data from DrugBank or primary literature to evaluate whether any known off-target activity is relevant to autoimmune neuroinflammation
- MHRA marketing authorisation data (or equivalent SmPC) to establish baseline safety profile and contraindications in the UK
- A defined patient hypothesis: e.g., whether any benefit would be restricted to patients with concurrent type 2 diabetes and focal stiff limb syndrome
- Consultation with a neurologist specialising in autoimmune movement disorders to assess clinical plausibility prior to any research investment

> **Note:** This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

