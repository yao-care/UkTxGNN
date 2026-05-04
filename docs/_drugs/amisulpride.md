---
layout: default
title: Amisulpride
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
---

# Amisulpride
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

# Amisulpride (DB06288): Drug Repurposing Candidate — Evaluation Incomplete

## One-Sentence Summary

Amisulpride is an atypical antipsychotic that selectively antagonises dopamine D2 and D3 receptors, established in the treatment of schizophrenia and related psychotic disorders.
The TxGNN model has **not produced any repurposing predictions** for this compound in the current evidence pack.
Critical data gaps — including absent UK regulatory records, missing mechanism of action data, and incomplete safety information — must be resolved before a formal evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Psychotic disorders (general pharmacological knowledge; not confirmed in Evidence Pack) |
| Predicted New Indication | Not available — TxGNN predictions absent |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not Assessed |
| UK Market Status | Unconfirmed — Evidence Pack reports "Not marketed"; likely a data collection error |
| Number of Marketing Authorisations | 0 (per Evidence Pack; inconsistent with known MHRA records) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological literature, amisulpride is a selective dopamine D2/D3 receptor antagonist. At low doses, it preferentially blocks presynaptic autoreceptors, which paradoxically increases dopaminergic neurotransmission; at therapeutic doses, it blocks postsynaptic D2/D3 receptors in the mesolimbic pathway, producing antipsychotic effects. Its relative selectivity for limbic over striatal dopamine receptors accounts for its lower propensity for extrapyramidal side effects compared to first-generation antipsychotics.

No TxGNN repurposing predictions are present in the current evidence pack (`predicted_indications` is empty). This suggests either that the TxGNN prediction pipeline has not yet been executed for this compound, or that amisulpride was not successfully matched to DrugBank entry DB06288 within the knowledge graph. Until predictions are generated, no mechanistic bridge between the original indication and a candidate new indication can be formally constructed within this framework.

It is worth noting that exploratory clinical interest exists in low-dose amisulpride as a treatment for postoperative nausea and vomiting (PONV), an area mechanistically distinct from its antipsychotic use; and its D3 receptor affinity has been investigated in mood and depressive disorders. These directions cannot, however, be formally assessed here without TxGNN output driving the evidence collection pipeline.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack.

---

## Literature Evidence

Currently no related literature available in this evidence pack.

---

## UK Market Information

The evidence pack reports zero UK marketing authorisations and a market status of "Not marketed." This is **inconsistent with known MHRA records**. Amisulpride (brand name Solian®, Sanofi) is a licensed medicine in the United Kingdom, holding authorisations for the treatment of acute and chronic schizophrenic disorders. Generic amisulpride products are also approved and available via the BNF (BNF section: 4.2.1 — Antipsychotic drugs).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| *Data collection error — please re-run MHRA pipeline* | Solian® (expected) | Tablets (50 mg, 100 mg, 200 mg, 400 mg) | Schizophrenia (acute and chronic) |

**Action required:** The UK regulatory data collection pipeline must be re-run for amisulpride (DB06288) to retrieve correct MHRA authorisation records before this section can be populated accurately.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

> **Note:** UK SmPC warnings, contraindications, and drug interaction data have not been retrieved for this evidence pack. This constitutes a Blocking data gap (DG001) and must be resolved before any safety-dependent clinical assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The current evidence pack contains multiple critical data gaps that collectively prevent any meaningful repurposing evaluation: TxGNN predictions are entirely absent, UK regulatory records appear to reflect a data collection failure rather than genuine market absence, and both mechanism of action and safety data are missing.

**To proceed, the following is needed:**

1. **Re-run the TxGNN prediction pipeline** — Confirm that amisulpride (DB06288) is present in the knowledge graph and re-execute prediction to populate `predicted_indications`
2. **Resolve UK regulatory data gap** — Re-query the MHRA product licence database to retrieve correct authorisation records for Solian® and any generic amisulpride products (Data Gap DG001 — Blocking)
3. **Retrieve MOA data from DrugBank** — Query the DrugBank API for DB06288 to populate mechanism of action details (Data Gap DG002 — High)
4. **Run evidence collection** — Once predictions are available, execute ClinicalTrials.gov, PubMed, and ICTRP collectors for the predicted indication(s)
5. **Complete safety assessment** — Download and parse the UK SmPC to populate warnings, contraindications, and drug–drug interaction data prior to any clinical review

---

> ⚠️ *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Healthcare professionals should refer to the current BNF and SmPC for prescribing information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

