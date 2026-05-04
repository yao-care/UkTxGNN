---
layout: default
title: Azelastine Hcl
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 0
---

# Azelastine Hcl
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

# Azelastine HCl: Evidence Pack Incomplete — Indicative Report Only

> ⚠️ **Important Notice**: This Evidence Pack is critically incomplete. The `predicted_indications` array is empty, meaning TxGNN has not returned any repurposing predictions for this drug. The following report reflects only what could be extracted from the available data. **This report should not be used for any clinical or commissioning decision.**

---

## One-Sentence Summary

Azelastine HCl is a second-generation antihistamine (H1 receptor antagonist) commonly used for allergic rhinitis and allergic conjunctivitis.
However, the TxGNN model has **not returned any predicted new indications** for this candidate in the current Evidence Pack.
As a result, no repurposing analysis, evidence grading, or decision recommendation can be generated at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack |
| Predicted New Indication | None — prediction data absent |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not determinable |
| UK Market Status | Not recorded in Evidence Pack |
| Number of Marketing Authorisations | 0 recorded in Evidence Pack |
| Recommended Decision | **Hold** — insufficient data to proceed |

---

## Why the Report Cannot Be Completed

The Evidence Pack for Azelastine HCl contains two blocking or high-severity data gaps that prevent a full evaluation:

**DG001 — Safety Warnings and Contraindications (Severity: Blocking)**
No SmPC-equivalent warnings or contraindications were retrieved. Without this, the standard safety screening (S1) cannot be completed.
*Remediation*: Retrieve the product SmPC from the MHRA product listings and parse relevant sections.

**DG002 — Mechanism of Action (Severity: High)**
No MOA data was retrieved from DrugBank (DrugBank ID not resolved). This prevents any mechanistic rationale from being constructed for a repurposing hypothesis.
*Remediation*: Query DrugBank API using the INN "azelastine hydrochloride" and retrieve the pharmacology section.

Additionally, the `predicted_indications` field in the Evidence Pack is **empty (`[]`)**. This is the most critical gap: without at least one TxGNN prediction, no indication-specific analysis (clinical trials, literature review, safety in new indication, cytotoxicity assessment) can be generated.

---

## Safety Considerations

All safety fields in this Evidence Pack are unpopulated.

Please refer to the current SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack lacks predicted indications, a resolved DrugBank ID, MOA data, and safety information. There is no basis on which to evaluate a repurposing hypothesis.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN prediction pipeline** for Azelastine HCl to populate `predicted_indications`; verify that the drug node exists in the knowledge graph under this INN or an accepted synonym (e.g., "azelastine")
- [ ] **Resolve DrugBank ID** — query DrugBank API or manually look up DB00453; update `drug.drugbank_id` in the Evidence Pack
- [ ] **Retrieve MOA** from DrugBank pharmacology section and populate `drug.original_moa`
- [ ] **Retrieve UK market authorisations** from the MHRA Product Licence database (https://products.mhra.gov.uk/) — note that Azelastine is understood to have licensed products in the UK (e.g., nasal spray and eye drop formulations); the current Evidence Pack appears to under-report this
- [ ] **Retrieve SmPC safety data** (warnings, contraindications, interactions) and populate `safety` fields
- [ ] **Re-generate Evidence Pack** at version v5+ and resubmit for report generation

---

*This report was generated on 2026-04-04. It is based solely on the Evidence Pack provided and does not incorporate independent clinical judgement. Results are for research reference only and do not constitute medical advice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

