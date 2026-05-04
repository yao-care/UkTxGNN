---
layout: default
title: Carbidopa
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 0
---

# Carbidopa
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

# Carbidopa: Drug Repurposing Evaluation — No New Indications Predicted

## One-Sentence Summary

Carbidopa (DrugBank ID: DB00190) is a peripheral aromatic L-amino acid decarboxylase inhibitor, used clinically in combination with levodopa for the management of Parkinson's disease and related parkinsonian syndromes.
In this evaluation cycle, the TxGNN model did **not generate any drug repurposing predictions** for Carbidopa, meaning no new candidate indications were identified.
This report serves as a baseline assessment only; resolution of multiple data gaps and a model re-query are required before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease / parkinsonian syndromes (in combination with levodopa); no UK licence data currently held in this Evidence Pack |
| Predicted New Indication | None generated in this evaluation cycle |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No predictions generated |
| UK Market Status | Not independently marketed (0 licences on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **Note on UK Market Status:** Carbidopa is not available as a standalone licensed medicine in the UK. It is commercially available only in fixed-dose combination products (e.g., co-careldopa / Sinemet®, and co-careldopa + entacapone / Stalevo®). The Evidence Pack reflects the absence of a standalone MHRA marketing authorisation, which is consistent with clinical practice.

---

## UK Market Information

No standalone MHRA marketing authorisations are held for Carbidopa. The drug is not independently marketed in the United Kingdom.

Carbidopa is available only within licensed combination products. Under BNF classification, these fall under **4.9.1 Dopaminergic drugs used in Parkinson's disease**. Prescribers and pharmacists should refer to the SmPCs for the relevant combination products (e.g., Sinemet®, Half Sinemet®, Stalevo®) for authorised indications, dosing, and safety information.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug–drug interactions) are currently held within this Evidence Pack for Carbidopa.

> Please refer to the SmPC for the relevant combination product and the BNF section **4.9.1** for full safety information. Suspected adverse reactions should be reported via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no predicted repurposing candidates for Carbidopa in this evaluation cycle, and the Evidence Pack contains critical data gaps across mechanism of action, regulatory labelling, and safety that together prevent any repurposing assessment from proceeding to the evidence-review stage.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001 (Blocking):** Obtain the current MHRA-approved SmPC (or the SmPC for a relevant combination product such as Sinemet®) to populate key warnings and contraindications. Without this, S1-level safety screening cannot be completed.
- **Resolve Data Gap DG002 (High):** Query the DrugBank API for Carbidopa's mechanism of action (DB00190). Although the peripheral DOPA decarboxylase inhibitor mechanism is well characterised in the literature, a structured MOA record is required for automated mechanistic-relevance scoring.
- **Re-run TxGNN prediction pipeline:** Once the drug record is fully populated (original indications, DrugBank categories, MOA), resubmit Carbidopa to the TxGNN knowledge-graph and deep-learning prediction modules to generate candidate indications with associated scores.
- **Consider combination-product framing:** Evaluate whether TxGNN predictions should be run for Carbidopa as part of a levodopa/carbidopa pair, given that it has no independent clinical activity and is exclusively used in combination. This may require a separate candidate record (e.g., levodopa + carbidopa as a single entity).
- **Populate UK licence data for combination products:** Retrieve MHRA licence details for co-careldopa combination products to provide a complete regulatory context for any future repurposing analysis.

---

*This report is generated for research purposes only and does not constitute medical advice. Any drug repurposing candidate identified by TxGNN requires prospective clinical validation before therapeutic application. All website pages and outputs from this system must include an appropriate YMYL disclaimer.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

