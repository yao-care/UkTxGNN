---
layout: default
title: Vildagliptin
parent: Model Prediction Only (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Vildagliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor, an oral antidiabetic agent whose established use is the treatment of type 2 diabetes mellitus (as documented in the supporting literature within this evidence pack).
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and is based purely on knowledge-graph statistical association rather than any established biological mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from literature evidence in this pack; no formal UK licence data available) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for vildagliptin in this evidence pack (flagged as a High-severity data gap). Based on the literature evidence collected alongside the predictions, vildagliptin is known to belong to the **DPP-4 inhibitor** class of antidiabetic agents, working by prolonging the activity of endogenous incretin hormones (GLP-1 and GIP) to enhance pancreatic islet function. Its efficacy in type 2 diabetes is well documented across dozens of clinical trials in this evidence pack.

However, the predicted new indication — focal stiff limb syndrome — is an autoimmune neurological condition characterised by GABAergic neurotransmission dysfunction, most often associated with anti-GAD65 antibodies. According to the model's own repurposing rationale, **there is no known mechanistic overlap** between DPP-4 inhibition and this autoimmune/neurological pathology. The rationale explicitly states that this prediction is derived purely from statistical similarity within the knowledge graph embedding space, with zero supporting clinical trials or literature.

For context, several of the other TxGNN-predicted indications for vildagliptin (ranks 2–8, including stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and various lipodystrophies) share this same pattern: high model confidence scores but no biological or clinical rationale. By contrast, a lower-ranked candidate in this same evidence pack — type 1 diabetes mellitus (rank 10) — is supported by real mechanistic literature (e.g., glucagon counter-regulation, β-cell preservation) and a completed RCT (rapamycin plus vildagliptin), representing a substantially stronger evidence base than the top-ranked prediction discussed here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Vildagliptin currently has no marketing authorisation in the United Kingdom (market status: **Not marketed**; total authorisations: **0**). No licence records are available to summarise.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (focal stiff limb syndrome) has no supporting clinical trials or literature, and the model's own rationale confirms there is no known biological mechanism linking DPP-4 inhibition to this autoimmune neurological disorder. This is a pure statistical (L5) prediction with no clinical plausibility at present.

**To proceed, the following is needed:**
- MHRA-equivalent labelling data (warnings/contraindications) — currently a **Blocking** data gap preventing initial safety screening
- Confirmed mechanism of action (MOA) data from DrugBank — currently a **High**-severity data gap affecting mechanistic-link analysis
- Preclinical or mechanistic studies directly linking DPP-4/incretin pathways to GABAergic or autoimmune neuromuscular pathology, before any further evaluation is warranted
- If interest exists in repurposing vildagliptin more broadly, the type 1 diabetes mellitus signal (rank 10, L2 evidence, existing RCT data) represents a more scientifically grounded starting point than the top-ranked prediction discussed in this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

