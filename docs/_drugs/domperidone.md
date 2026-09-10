---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 1
---

# Domperidone
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

# Domperidone: From Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripherally-selective dopamine D2 receptor antagonist historically used as an antiemetic and prokinetic agent (and, via prolactin stimulation, as a lactation aid). The TxGNN model predicts a possible link to **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but this prediction is currently supported by **no clinical trials and no published literature** — it rests on knowledge-graph inference alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nausea/vomiting and gastrointestinal motility disorders (based on known pharmacological class; no formal indication text available in this evidence pack) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (drug-level data gap, DG002). Based on known pharmacology, domperidone is a peripherally-selective dopamine D2 receptor antagonist acting at the chemoreceptor trigger zone and gastrointestinal tract, used clinically for its antiemetic and prokinetic effects, and separately for prolactin-mediated lactation support.

NSIAD, in contrast, is caused by gain-of-function mutations in the AVPR2 (vasopressin V2) receptor, which becomes constitutively active independent of circulating ADH. There is no established pharmacological or physiological link between dopamine D2 receptor antagonism and V2 receptor signalling, and no literature currently connects the two pathways.

On the evidence available, this prediction should be read as a knowledge-graph-derived hypothesis rather than a mechanistically grounded one. It may reflect an indirect graph association (e.g. shared downstream renal or endocrine nodes) rather than a genuine pharmacological rationale, and should be treated with appropriate caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Domperidone currently has no marketing authorisations recorded against this evidence pack, and market status is listed as not marketed. No product-level licence information is available.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN model inference (L5, S0), with no clinical trials, no literature, and no plausible shared mechanism identified between D2 receptor antagonism and the AVPR2-driven pathophysiology of NSIAD. Combined with the absence of any UK marketing authorisation, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for domperidone (DG002)
- MHRA/SmPC safety data — key warnings and contraindications (DG001)
- Preclinical or mechanistic evidence for any interaction between dopaminergic and vasopressin V2 receptor signalling
- At minimum, case-level or observational evidence before this candidate can move beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

