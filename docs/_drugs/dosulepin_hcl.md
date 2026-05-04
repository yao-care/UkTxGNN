---
layout: default
title: Dosulepin Hcl
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 0
---

# Dosulepin Hcl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Dosulepin HCl: Repurposing Assessment on Hold — Critical Data Gaps Prevent Evaluation

## One-Sentence Summary

Dosulepin hydrochloride (also known as dothiepin) is a tricyclic antidepressant (TCA) historically used in the treatment of depression and anxiety-related conditions.
The current Evidence Pack contains **no TxGNN repurposing predictions**, no UK marketing authorisation records, and no safety data, making a formal repurposing assessment impossible at this stage.
Immediate remediation of **two critical data gaps** is required before this candidate can enter the evaluation pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — TxGNN pipeline returned no candidates |
| UK Market Status | Not marketed (0 authorisations recorded) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why Cannot This Assessment Be Completed?

The Evidence Pack for Dosulepin HCl is critically incomplete at every layer of the evaluation framework. The TxGNN prediction pipeline returned no repurposing candidates (`predicted_indications: []`), meaning no new indication has been algorithmically proposed. Without a target indication, the core structure of a repurposing report — mechanism-to-indication mapping, clinical trial search, literature review — cannot be executed.

Based on published pharmacological literature, Dosulepin HCl belongs to the tricyclic antidepressant (TCA) class. TCAs act primarily by inhibiting the reuptake of serotonin and noradrenaline in the central nervous system, with additional activity at muscarinic (anticholinergic), histamine H₁, and alpha-adrenergic receptors. It was formerly one of the most widely prescribed antidepressants in the United Kingdom under the brand name **Prothiaden**, particularly favoured where depression co-occurred with anxiety and insomnia.

However, MHRA has issued specific guidance highlighting that dosulepin carries a **higher risk of cardiotoxicity and death in overdose** compared to other antidepressants, which has substantially restricted its use in the UK over the past two decades. This safety profile is directly relevant to any repurposing evaluation and the complete absence of structured safety data from the Evidence Pack is a **blocking issue**.

The DrugBank query (Query Log ID 1, run 2026-03-27) returned 1 result, confirming drug identity can be resolved — however, the DrugBank ID was not populated in the Evidence Pack, which has likely prevented the TxGNN knowledge graph from correctly mapping this candidate and generating predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

> The DrugBank query confirmed drug identity but the DrugBank ID field remains null, which is the most likely reason the TxGNN pipeline was unable to generate predictions or retrieve associated evidence. Resolving the DrugBank ID is the critical path item.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## UK Market Information

No UK marketing authorisations are recorded in the current Evidence Pack.

> **Important note for healthcare professionals**: Dosulepin HCl was previously marketed in the UK as **Prothiaden** (formerly by Knoll/Abbott). The absence of marketing authorisation records in this Evidence Pack likely reflects a data retrieval issue rather than confirmed non-authorised status. Current MHRA registration status should be verified directly via the [MHRA Products database](https://products.mhra.gov.uk/) before drawing regulatory conclusions. The BNF also provides current prescribing guidance on dosulepin where it remains available under specialist supervision.

---

## Safety Considerations

The Evidence Pack contains no structured safety data for this candidate.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Identified data gaps requiring urgent remediation:**

| Gap ID | Item | Severity | Remediation |
|--------|------|----------|-------------|
| DG001 | MHRA SmPC — warnings and contraindications | **Blocking** | Retrieve SmPC from MHRA Products database |
| DG002 | Mechanism of action (MOA) | High | Query DrugBank API once DrugBank ID is confirmed |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline generated no repurposing predictions for Dosulepin HCl, and the Evidence Pack is critically incomplete across all evaluation domains — regulatory, mechanistic, and safety. No evidence-based repurposing assessment can be conducted in this state. The most likely root cause is the null DrugBank ID preventing correct knowledge graph node mapping.

**To proceed, the following is needed:**

- **[Blocking]** Confirm DrugBank ID for Dosulepin HCl via the DrugBank API (INN: dosulepin; synonym: dothiepin) and populate the `drugbank_id` field — this is the most likely cause of the empty `predicted_indications` array
- **[Blocking]** Retrieve current MHRA SmPC for Dosulepin HCl/Prothiaden, including full warnings, contraindications, and approved indications
- **[High]** Populate mechanism of action (MOA) from DrugBank once ID is confirmed
- **[High]** Re-run the TxGNN prediction pipeline once DrugBank node mapping is resolved
- **[Medium]** Obtain structured drug-drug interaction (DDI) data once DrugBank ID is confirmed
- **[Advisory]** Given MHRA's established cardiac safety concerns with TCAs — particularly in overdose — any future repurposing indication should include a formal benefit-risk assessment addressing cardiovascular monitoring requirements

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Suspected adverse reactions should be reported via the [MHRA Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

