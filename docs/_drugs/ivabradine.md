---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ivabradine: predicted new indication Hypertrichosis (evidence level L5). Approved use: Not stated in the data compiled for this report"
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ivabradine: From Heart Rate Control to Hypertrichosis

## One-Sentence Summary

Ivabradine is a heart-rate-lowering medicine that has a UK marketing authorisation as a 5 mg tablet.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ivabradine inhibits HCN (hyperpolarisation-activated cyclic nucleotide-gated) channels, mainly HCN4 in the sinoatrial node, which lowers heart rate. Detailed mechanism of action data is not available in the data compiled for this report, and the approved indication text is also missing, so the relationship between the original and predicted uses cannot be assessed directly.

No direct mechanistic link between HCN channel inhibition and hypertrichosis has been established. HCN channels are expressed in some non-cardiac tissues, but a role in hair follicle biology is speculative. Ambras-type hypertrichosis, for example, is linked to genomic rearrangements near TRPS1, which is not an HCN pathway.

The very high score (99.79%) is a knowledge-graph prediction only. The other top-ranked predictions are also hair- or developmental-related conditions, and they likely share network neighbours with hypertrichosis rather than providing independent biological support. Other predictions with the same L5 evidence level and a Hold recommendation:

- Ambras type hypertrichosis universalis congenita (99.72%)
- Malformation syndrome with odontal and/or periodontal component (99.72%)
- Syndrome with a Dandy-Walker malformation as major feature (99.70%)
- Isolated genetic hair shaft abnormality (99.69%)
- Nephrogenic syndrome of inappropriate antidiuresis (99.08%)

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206030Y0AAAAAA (BNF code) | Ivabradine Tab 5mg | Tablet | Not stated |

The listed number is a BNF-style product code rather than a PL number. Ivabradine falls within BNF chapter 2 (cardiovascular system).

## Safety Considerations

**Drug Interactions**

The data compiled for this report list 100 interacting drugs, of which 20 are shown here. Several are rated **Major**:

- Aprepitant
- Clarithromycin
- Cisapride
- Clotrimazole
- Cobicistat
- Dolasetron
- Granisetron
- Levofloxacin
- Ondansetron
- Palonosetron
- Papaverine

**Moderate** interactions include famotidine, ranitidine, cimetidine, nizatidine, dexamethasone, metreleptin, miconazole and troglitazone.

Many of these are CYP3A4 inhibitors or QT-prolonging agents, so interaction review is essential before any use.

For warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by a model score alone, with no trials, no publications and no plausible mechanistic link between HCN channel inhibition and hair growth or the genetic causes of hypertrichosis.

**To proceed, the following is needed:**
- Confirmed approved indication text and licence details (the regulatory entry is incomplete)
- Mechanism of action data and a biological rationale linking HCN channels to hair follicle biology
- Preclinical evidence (for example, HCN expression in hair follicles) before any clinical work
- Safety screening using SmPC warnings and contraindications, which are not yet available
- A risk-benefit assessment for non-cardiac use, given the interaction burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

