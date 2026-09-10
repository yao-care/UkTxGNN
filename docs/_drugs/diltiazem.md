---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diltiazem: From Hypertension and Coronary Vasospasm to Ischaemic Stroke Susceptibility

## One-Sentence Summary

Diltiazem is a non-dihydropyridine calcium channel blocker whose confirmed original indication is not recorded in this dataset, though its mechanism of action (blood pressure control and coronary vasospasm reduction) is documented. The TxGNN model assigns a high score to **"obsolete susceptibility to ischemic stroke"** — however, this is a susceptibility/trait node flagged as *obsolete* in the underlying knowledge graph, not a recognised clinical diagnosis, and it is currently supported by **zero clinical trials and zero publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset (no licences on file); mechanistic notes indicate use in hypertension and coronary vasospasm control |
| Predicted New Indication | Ischaemic stroke susceptibility (an obsolete graph node, not a standard clinical diagnosis — see caveat below) |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Diltiazem is an L-type calcium channel blocker. Per the mechanistic notes provided, its main pharmacological effects are reduction of vascular smooth muscle tone, blood pressure control, and suppression of coronary artery spasm. On this basis, there is a plausible theoretical link between blood pressure/cerebrovascular vasospasm control and ischaemic stroke risk reduction.

However, this link should be treated with caution for two reasons. First, the predicted "indication" — **"obsolete susceptibility to ischemic stroke"** — is a susceptibility/trait node in the knowledge graph that has itself been marked *obsolete*, rather than a treatable clinical diagnosis. This weakens the causal relevance of the prediction considerably, regardless of the score. Second, a formal, structured mechanism-of-action record for Diltiazem is a data gap in this evidence pack (DG002), so the mechanistic rationale above cannot yet be cross-checked against a validated source.

Given both the target-entity ambiguity and the missing MOA documentation, this prediction should currently be regarded as a hypothesis-generating signal only, not as evidence of therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Diltiazem is not currently marketed in the UK according to this dataset, and no marketing authorisations are on record (0 licences). No UK product-level information (formulation, licensed indications) is therefore available in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: full prescribing warnings, contraindications and drug interaction data for Diltiazem are marked as a Blocking data gap in this pack and have not yet been retrieved — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 — this is a model prediction only, with no supporting clinical trials or literature, and the predicted target is an obsolete susceptibility node rather than a defined clinical indication.
- Safety review cannot proceed: SmPC-level warnings and contraindications are a **Blocking** data gap (DG001), so this candidate cannot yet pass initial safety screening.

**To proceed, the following is needed:**
- Retrieval of SmPC/product warnings and contraindications from the relevant regulatory source (Blocking gap, DG001)
- A validated mechanism-of-action record from DrugBank or equivalent (DG002)
- Clarification of whether "ischemic stroke susceptibility" corresponds to any actionable, non-obsolete clinical entity before further evidence search is commissioned
- Confirmation of UK marketing/licensing status, since none is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

