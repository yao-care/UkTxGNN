---
layout: default
title: Zafirlukast
parent: Model Prediction Only (L5)
nav_order: 615
evidence_level: L5
indication_count: 2
---

# Zafirlukast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Zafirlukast: From Chronic Asthma to Bronchitis

## One-Sentence Summary

Zafirlukast is a cysteinyl leukotriene receptor antagonist originally developed for the prophylaxis and treatment of chronic asthma. The TxGNN model predicts it may be effective for **Bronchitis**, with a very high prediction score, but **no clinical trials or published literature specific to bronchitis** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic asthma (prophylaxis and treatment) — not available from UK licensing records, as the drug is not marketed in the UK; this is drawn from the supporting literature in the evidence pack |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.93% (rank 1,247 of all predicted drug–disease pairs) |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for zafirlukast is not available in this evidence pack (Data Gap). Based on the supporting literature, zafirlukast is known to be a selective, competitive cysteinyl leukotriene (CysLT1) receptor antagonist, and its efficacy in chronic asthma is well established across multiple pharmacology reviews and clinical summaries.

The repurposing rationale for bronchitis is mechanistic extrapolation rather than direct evidence: cysteinyl leukotrienes (LTD4/LTE4) are known to contribute to bronchial inflammation and excessive mucus secretion. By blocking the CysLT1 receptor, zafirlukast could theoretically reduce bronchitis symptoms through the same anti-inflammatory pathway that underlies its asthma indication. However, this reasoning is extrapolated from asthma and COPD pharmacology, and there is **no direct clinical or trial evidence in a bronchitis population**.

It is worth noting that a second, lower-ranked TxGNN prediction for this drug — obstructive lung disease (COPD), score 99.17% — is supported by 20 publications, including small clinical studies examining zafirlukast's bronchodilator effect in COPD (e.g. PMID 12877822, PMID 23741166). Since bronchitis, asthma, and COPD share overlapping airway inflammation pathways, this COPD-related evidence lends some indirect mechanistic plausibility to the bronchitis prediction, but does not substitute for bronchitis-specific data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Zafirlukast currently holds no UK marketing authorisation. According to the regulatory data extracted, the medicine is not marketed in the UK (0 marketing authorisations on record).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high prediction score (99.93%) for bronchitis, there is no clinical trial or literature evidence directly supporting this specific indication (Evidence Level L5, model prediction only). The drug is also not currently marketed in the UK, and the safety data required for an initial safety screen (SmPC warnings and contraindications) is missing — this is a blocking data gap.

**To proceed, the following is needed:**
- SmPC-derived warnings, contraindications, and drug interaction data (blocking prerequisite for safety screening)
- Confirmed mechanism of action and original indication details from DrugBank/SmPC
- Bronchitis-specific preclinical or clinical evidence
- Consideration of the alternative, better-supported prediction (obstructive lung disease/COPD) as a repurposing candidate
- Clarification of UK marketing authorisation pathway, given the drug's current unlicensed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

