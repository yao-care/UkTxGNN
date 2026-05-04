---
layout: default
title: Ciclosporin
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 0
---

# Ciclosporin
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

# Ciclosporin: Drug Repurposing Evaluation — Insufficient Data for Assessment

## One-Sentence Summary

Ciclosporin is a well-established calcineurin inhibitor immunosuppressant; however, the current evidence pack contains **no original indication data**, **no predicted new indications** from the TxGNN model, and **no regulatory or safety information**. A meaningful repurposing evaluation cannot be completed until critical data gaps are resolved.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack |
| Predicted New Indication | No TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No predictions generated |
| UK Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Ciclosporin is a known calcineurin inhibitor that suppresses T-cell activation and is widely used internationally for the prevention of organ transplant rejection, treatment of severe psoriasis, atopic dermatitis, rheumatoid arthritis, and nephrotic syndrome.

However, as the TxGNN model has generated **no predicted indications** for this candidate, there is no repurposing hypothesis to evaluate at this time. The absence of predictions may be due to a failure in DrugBank ID mapping (the `drugbank_id` field is null), which would prevent the model from linking Ciclosporin to the knowledge graph.

Before any mechanistic plausibility assessment can be made, the drug must first be correctly mapped to its DrugBank identifier (DB00091) and the prediction pipeline re-run.

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication available for evidence search.

## Literature Evidence

Currently no related literature available — no predicted indication available for evidence search.

## UK Market Information

No marketing authorisation data is available in the evidence pack. **Note:** Ciclosporin is in fact widely authorised and marketed in the United Kingdom under multiple brand names (e.g., Sandimmun, Neoral, Capimune, Deximune). The absence of data here reflects a gap in the evidence pack rather than a true lack of UK market presence. This should be rectified by querying MHRA and BNF sources directly.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Note:** The evidence pack flagged the following blocking data gaps:
> - **DG001** (Blocking): SmPC warnings and contraindications have not been retrieved. Source: Regulatory authority website; remedy by downloading and parsing SmPC PDFs.
> - **DG002** (High): Mechanism of action data is missing. Source: DrugBank; remedy by querying the DrugBank API with the correct identifier.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack is critically incomplete — there is no DrugBank ID mapping, no TxGNN prediction output, no original indication data, and no safety information. Without a predicted new indication, no repurposing evaluation can proceed.

**To proceed, the following is needed:**
- **DrugBank ID resolution**: Map Ciclosporin to its correct DrugBank identifier (DB00091) and confirm linkage in the knowledge graph
- **Re-run TxGNN prediction pipeline**: Once the DrugBank mapping is established, execute the KG and DL prediction models to generate candidate indications
- **Populate original indication data**: Extract approved indications from MHRA marketing authorisations and BNF entries
- **Retrieve safety data**: Obtain SmPC warnings, contraindications, and drug interaction profiles
- **UK regulatory data**: Query MHRA for current marketing authorisation status, as Ciclosporin is known to be marketed in the UK despite the evidence pack showing otherwise

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

