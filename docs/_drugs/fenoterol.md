---
layout: default
title: Fenoterol
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Fenoterol: predicted new indication Multiple system atrophy (evidence level L5). Approved use: Not stated in the licence data compiled for this report (fenoterol is…"
monitor_inn: "fenoterol"
predicted_indications: ["multiple system atrophy", "postural orthostatic tachycardia syndrome", "variably protease-sensitive prionopathy", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "sinoatrial block", "sinoatrial node disease"]
---

# Fenoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fenoterol: From Bronchodilation to Multiple System Atrophy
{: .text-alpha }

## One-Sentence Summary

Fenoterol is a selective beta-2 adrenergic agonist used as a bronchodilator, and it is marketed in the UK in combination with ipratropium.
The TxGNN model predicts it may be effective for **multiple system atrophy**, but **no clinical trials and no publications** currently support this direction.
The prediction is computational only, and the mechanistic rationale is weak and potentially unfavourable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (fenoterol is generally used as a bronchodilator) |
| Predicted New Indication | Multiple system atrophy |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Pharmacological data show that fenoterol binds beta-1, beta-2 and beta-3 adrenoceptors, and it is known as a beta-2 agonist used as a bronchodilator.

In multiple system atrophy (MSA), a theoretical link could involve modulation of autonomic or neuroinflammatory pathways through beta-2 receptors. However, beta-2 agonism causes vasodilation and could worsen orthostatic hypotension, a core feature of MSA. The mechanistic rationale is therefore weak and may be unfavourable. The high TxGNN score reflects a network-based computational prediction rather than a defined biological pathway.

### Other Predicted Indications

All of the following are prediction-only (L5), with no trials or literature, and all are rated Hold.

| Rank | Predicted Indication | TxGNN Score | Mechanistic Comment |
|------|------|------|------|
| 2 | Postural orthostatic tachycardia syndrome | 0.9961 | Vasodilation and reflex tachycardia would be expected to aggravate symptoms; safety concern |
| 3 | Variably protease-sensitive prionopathy | 0.9954 | No clear link between beta-2 agonism and prion pathology |
| 4 | Open-angle glaucoma | 0.9943 | Class-level effects on aqueous humour dynamics are partially plausible; systemic fenoterol is not an ocular agent |
| 5 | Raynaud disease | 0.9941 | Vasodilation is the most coherent mechanism; limited by systemic effects and no clinical data |
| 6 | Primary hereditary glaucoma | 0.9937 | Often structural in origin; pharmacological IOP lowering is less likely to be disease-modifying |
| 7 | Sinoatrial block | 0.9935 | Chronotropic rationale exists, but arrhythmia risk and better established options (atropine, pacing) |
| 8 | Sinoatrial node disease | 0.9925 | Proarrhythmic and ischaemic risk; pacemaker implantation is standard of care |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0301040M0BBABAB (BNF code) | Duovent Neb Soln 4ml Ud Vl | Nebuliser solution | Not stated in the data compiled |
| 0301040M0AAAAAA (BNF code) | Fenoterol/Ipratropium Inhaler 100/40mcg (200 doses) | Inhaler | Not stated in the data compiled |

Both products are classed under BNF section 3.1.4 (bronchodilators) based on the code prefix. The identifiers above are BNF codes rather than MHRA PL numbers, and approved indication text was not available.

## Safety Considerations

- **Drug Interactions (pharmacology):** Fenoterol binds beta-1, beta-2 and beta-3 adrenoceptors. No interacting drugs with severity ratings were identified in the data compiled.
- **Class-level concerns relevant to the predictions:** Systemic beta-2 agonism can cause tachycardia, tremor and hypokalaemia, and may worsen orthostatic hypotension.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All eight predictions are supported only by a computational score, with no trials or publications. For the top prediction (multiple system atrophy), and for postural orthostatic tachycardia syndrome, the pharmacology suggests possible harm rather than benefit. Raynaud disease is the most mechanistically coherent candidate but still lacks any clinical data.

**To proceed, the following is needed:**
- Complete safety data from the SmPC and BNF (warnings and contraindications), which are currently missing and block safety screening
- Detailed mechanism of action data
- Approved indication text and dosage form for the UK authorisations
- A systematic literature and trial search, with Raynaud disease as the priority candidate
- A mechanistic and safety review of cardiovascular effects (orthostatic hypotension, tachycardia, arrhythmia) before considering any neurological or cardiac indication
- Assessment of route compatibility, since current products are inhaled or nebulised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

