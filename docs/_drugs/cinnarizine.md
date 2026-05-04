---
layout: default
title: Cinnarizine
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 0
---

# Cinnarizine
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

# Cinnarizine: Drug Repurposing Evaluation — Insufficient Data for Assessment

## One-Sentence Summary

Cinnarizine (DrugBank ID: DB00568) is a piperazine-derivative calcium channel blocker and antihistamine historically used for vertigo, motion sickness, and peripheral vascular disorders. The TxGNN model has **not generated any predicted new indications** at this time, and the current evidence pack contains **no clinical trials** and **no publications** to support a repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current dataset |
| Predicted New Indication | None predicted |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; no actual studies available |
| UK Market Status | Not marketed (per current dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **Note on UK Market Status:** Cinnarizine is in fact available in the United Kingdom (e.g. Stugeron, Cinnarizine 15 mg tablets — available over the counter for motion sickness and as a prescription medicine for vestibular disorders). The current dataset does not yet reflect MHRA marketing authorisation data. This data gap should be remediated before any further evaluation.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, cinnarizine is a selective calcium channel blocker (T-type) and histamine H1-receptor antagonist. It reduces the excitability of the vestibular apparatus and is used clinically for the symptomatic treatment of vertigo, tinnitus, nausea, and vomiting of vestibular origin, as well as motion sickness and peripheral vascular disorders (e.g. Raynaud's phenomenon).

No TxGNN prediction has been generated for cinnarizine. This may be due to incomplete mapping of cinnarizine to the knowledge graph, absence of regulatory indication data in the current dataset, or insufficient graph connectivity to produce a confident repurposing signal. Without a predicted indication, no mechanistic plausibility assessment can be performed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the evidence pack.

---

## Literature Evidence

Currently no related literature available in the evidence pack.

---

## UK Market Information

No marketing authorisation records are present in the current dataset.

> **Action required:** MHRA marketing authorisation data for cinnarizine should be obtained. Cinnarizine products (e.g. Stugeron 15 mg tablets, PL 00242/0349) are known to hold valid UK marketing authorisations. The BNF lists cinnarizine under section 4.6 (Drugs used in nausea and vertigo). This data gap must be filled before proceeding.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for cinnarizine is substantially incomplete. No TxGNN predicted indications have been generated, no regulatory data has been mapped, no mechanism of action data is recorded, and no safety information is available. A meaningful repurposing evaluation cannot be conducted with the current dataset.

**To proceed, the following is needed:**

- **UK regulatory data (Blocking):** Obtain MHRA marketing authorisation records and approved indications for cinnarizine products, including BNF classification
- **Mechanism of action data (High priority):** Query DrugBank API for full MOA, targets (calcium channel, H1 receptor), and pharmacodynamic profile
- **Safety data (Blocking):** Extract key warnings, contraindications, and drug interactions from the SmPC and BNF monograph
- **TxGNN knowledge graph mapping:** Verify that cinnarizine (DB00568) is correctly mapped in the knowledge graph (node.csv) and has adequate connectivity (kg.csv) to generate repurposing predictions
- **Re-run prediction pipeline:** Once data gaps are filled, re-execute `run_kg_prediction.py` to generate candidate indications

---

*This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

