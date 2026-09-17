---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is a pancreatic/gastric lipase inhibitor originally used for weight management in obesity, reducing dietary fat absorption. The TxGNN model predicts it may be relevant to **Hypervitaminosis**, but this is currently supported by **0 clinical trials** and **0 publications** — it is a model prediction only, with no direct clinical or mechanistic verification available in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity (weight management) — referenced only in the mechanistic rationale; no structured original-indication or UK licence data is currently available |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for Orlistat is not available in this evidence pack (data gap, High severity). However, the model's own rationale identifies Orlistat as a **pancreatic/gastric lipase inhibitor**, which blocks intestinal hydrolysis and absorption of dietary fat, thereby lowering calorie intake — the pharmacological basis of its established use in obesity/weight management.

This same mechanism also reduces intestinal absorption of the fat-soluble vitamins (A, D, E, K), and it is well recognised clinically that Orlistat can cause fat-soluble vitamin **deficiency** as a side effect — the opposite direction to hypervitaminosis (vitamin **excess**, e.g. vitamin A toxicity). The predicted link to hypervitaminosis therefore relies on an inferential, reverse-direction hypothesis (using Orlistat's absorption-blocking property to lower excess fat-soluble vitamin levels), rather than on any direct clinical precedent captured in the evidence pack.

Given that the formal original-indication list and MOA fields are both empty/data-gapped, and the drug is not currently marketed in this jurisdiction, there is insufficient structured evidence in this pack to independently verify the mechanistic plausibility of this prediction beyond the model's own reasoning text.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Orlistat currently holds no marketing authorisation on record in this dataset (0 licences; market status: Not marketed). No UK product, formulation, or licensed-indication data is therefore available for review.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by TxGNN's model score (L5), with no clinical trials, no published literature, and no confirmed mechanism-of-action or safety data. The proposed mechanistic link to hypervitaminosis is directionally counterintuitive relative to Orlistat's well-known fat-soluble vitamin **deficiency** risk, and the drug is not currently marketed in this jurisdiction.

**To proceed, the following is needed:**
- SmPC/product labelling warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Confirmed mechanism-of-action data from DrugBank or an equivalent authoritative source (High-severity data gap)
- Independent literature or case evidence specifically addressing Orlistat's effect on hypervitaminosis (vitamin excess), not just its known deficiency-inducing effect
- Clarification of Orlistat's formal original indication(s) via structured regulatory data, since the current record is empty
- Reassessment of UK market/licensing status should marketing plans change
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

