---
layout: default
title: Benzydamine Hcl
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 0
---

# Benzydamine Hcl
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

# Benzydamine HCL: Repurposing Assessment — Insufficient Data for Full Evaluation

---

## One-Sentence Summary

Benzydamine HCL is a locally-acting non-steroidal anti-inflammatory compound with anaesthetic and analgesic properties, widely recognised under the brand name Difflam in the United Kingdom for oropharyngeal conditions.
The current Evidence Pack contains **no TxGNN-predicted new indications**, and critical data fields — including mechanism of action, original indication, and safety profile — are all absent.
**A full repurposing evaluation cannot be completed at this stage; immediate data remediation is required before any progression decision can be made.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model pipeline incomplete; no predictions generated |
| UK Market Status | Not marketed (per Evidence Pack — see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Note on UK market status:** The Evidence Pack records zero active MHRA marketing authorisations. This should be verified directly against the [MHRA Product Licence Register](https://products.mhra.gov.uk/), as Benzydamine HCL preparations (e.g., Difflam oral spray and mouthwash) are known to hold MHRA authorisations in practice. A data retrieval gap or pipeline scope limitation may account for this discrepancy.

---

## Why a Full Assessment Cannot Yet Be Completed

No TxGNN prediction is present in this Evidence Pack, so no mechanistic bridge to a new indication can be evaluated.

Benzydamine HCL is understood to act locally at sites of inflammation via inhibition of prostaglandin biosynthesis and stabilisation of cell membranes, with additional local anaesthetic properties. However, the Evidence Pack flags the mechanism of action as a data gap, and without a confirmed DrugBank ID the pharmacological detail required to assess target-indication plausibility is unavailable.

Once a TxGNN prediction is generated and MOA data are retrieved from DrugBank, the "Why is This Prediction Reasonable?" section can be completed in full.

---

## Clinical Trial Evidence

No predicted indication is available in the current Evidence Pack. Clinical trial evidence cannot be presented until a target indication is defined and the evidence collection pipeline is re-run.

---

## Literature Evidence

No predicted indication is available in the current Evidence Pack. Literature evidence cannot be presented until a target indication is defined.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three prerequisite inputs for a repurposing evaluation — a TxGNN-predicted indication, a confirmed mechanism of action, and a complete safety profile — are absent. Proceeding without these would produce an assessment of no clinical or scientific value.

**To proceed, the following actions are required:**

- **Resolve DrugBank ID** — Search DrugBank for "benzydamine" or "benzydamine hydrochloride" to obtain the correct DrugBank ID and populate MOA, pharmacology, categories, and toxicity fields
- **Retrieve MHRA SmPC** — Download and parse the SmPC for a Benzydamine HCL product (e.g., Difflam) from the [MHRA website](https://products.mhra.gov.uk/) to populate original indications, approved dosage forms, key warnings, and contraindications
- **Re-run TxGNN pipeline** — With the correct DrugBank ID in place, re-run the KG and DL prediction steps to generate scored repurposing candidates
- **Verify UK market status** — Cross-check the MHRA Product Licence Register to correct the current "not marketed" classification if MHRA authorisations exist
- **Collect supporting evidence** — Once a predicted indication is available, run the ClinicalTrials.gov, EU Clinical Trials Register (EU CTR), ISRCTN, and PubMed collectors to populate the clinical trial and literature evidence sections
- **Complete safety profile** — Re-query DDI databases (e.g., DrugBank DDI, Liverpool DDI Checker) after the DrugBank ID is confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

