---
layout: default
title: Amiloride Hcl
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 0
---

# Amiloride Hcl
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

# Amiloride HCL: Repurposing Evaluation — Evidence Pack Incomplete, No Prediction Generated

---

## One-Sentence Summary

Amiloride HCL is a well-established potassium-sparing diuretic with a long clinical history, typically used in the management of oedema and hypertension. However, this evidence pack contains **no TxGNN-generated repurposing predictions**, and multiple critical data fields — including UK marketing authorisation records, mechanism of action, and safety data — are either absent or flagged as gaps. A substantive repurposing recommendation **cannot be made** on the basis of this evidence pack alone; remediation of data gaps is required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in evidence pack |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable — no predicted indication available |
| UK Market Status | Not marketed (per evidence pack — see note below) |
| Number of Marketing Authorisations | 0 (per evidence pack — likely a data quality issue) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Quality Note:** Amiloride is a long-established compound that is expected to hold UK marketing authorisations. A result of zero licences strongly suggests a data ingestion or mapping failure at source, rather than a true absence from the UK market. This must be investigated before any regulatory conclusions are drawn.

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction has been generated for Amiloride HCL in this evidence pack. Therefore, a formal mechanistic rationale for a new indication cannot be presented at this time.

Currently, detailed mechanism of action data is not available within the evidence pack. Based on known pharmacological information, Amiloride HCL is a potassium-sparing diuretic that acts by blocking epithelial sodium channels (ENaC) in the distal nephron, reducing sodium reabsorption whilst preserving potassium. Its established use in oedema management associated with heart failure and hypertension has been well documented since its introduction in the 1960s.

Mechanistically, ENaC blockade has attracted research interest in conditions beyond the kidney — most notably in cystic fibrosis (where airway ENaC overactivity contributes to mucociliary dysfunction) and in certain oncological contexts. However, without a formal TxGNN prediction or curated evidence, these observations remain speculative for the purposes of this report and should not be used to guide clinical decision-making.

---

## Clinical Trial Evidence

No predicted indication is available in this evidence pack. Clinical trial evidence cannot be retrieved or presented without a defined target indication.

Currently no related clinical trials are linked to a repurposing indication for this drug in the evidence pack.

---

## Literature Evidence

No predicted indication is available in this evidence pack. Literature evidence cannot be retrieved or presented without a defined target indication.

Currently no related literature is available within this evidence pack.

---

## UK Market Information

The evidence pack records **zero UK marketing authorisations** for Amiloride HCL. This is inconsistent with the drug's known regulatory history and is likely the result of a data pipeline error (e.g., failed DrugBank ID linkage — `drugbank_id` is null in the evidence pack).

| Item | Status |
|------|--------|
| MHRA Licences on Record | 0 (evidence pack) |
| DrugBank ID | Not resolved |
| Recommended Action | Re-run MHRA product licence lookup using INN "amiloride" and cross-reference BNF section 2.2.3 (Potassium-sparing diuretics) |

---

## Safety Considerations

All safety fields in this evidence pack are flagged as data gaps. No warnings, contraindications, or drug interaction data are available from this source.

Please refer to the SmPC and BNF (Section 2.2.3) for full safety information on Amiloride HCL. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack is critically incomplete: no TxGNN repurposing prediction has been generated, the UK marketing authorisation data appears erroneous, and all safety fields are absent. Proceeding with any repurposing evaluation in the current state would be premature and potentially misleading.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping** — `drugbank_id` is null; this is likely the root cause of missing MOA, safety, and regulatory data. Query DrugBank using the INN "amiloride" to retrieve the correct identifier (expected: DB00594).
- **Re-ingest UK licensing data** — Re-run the MHRA licence lookup with a corrected DrugBank ID or direct INN search to populate UK marketing authorisation records.
- **Retrieve mechanism of action (MOA)** — Query DrugBank API for Amiloride HCL's pharmacology record (ENaC blocker / potassium-sparing diuretic) to enable mechanistic plausibility analysis.
- **Retrieve SmPC safety data** — Download and parse the current MHRA SmPC to populate key warnings, contraindications, and drug interactions.
- **Re-run TxGNN prediction pipeline** — Once the DrugBank ID and regulatory data are resolved, re-run the TxGNN model to generate repurposing candidates with confidence scores.
- **Re-submit evidence pack** — Once all blocking data gaps (DG001, DG002) are remediated, resubmit for a full evaluation report.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation prior to any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

