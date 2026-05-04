---
layout: default
title: Rituximab
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 0
---

# Rituximab
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

# Rituximab: Evaluation On Hold — Evidence Pack Critically Incomplete

## One-Sentence Summary

Rituximab (DrugBank: DB00073) is a well-established anti-CD20 monoclonal antibody with known oncological and autoimmune indications.
However, the Evidence Pack generated for this candidate (TW-DB00073-multi, v4, dated 2026-04-04) contains **no predicted new indications**, **no UK marketing authorisation records**, and **no safety data**, making a standard drug repurposing evaluation impossible at this stage.
This report documents the data gaps and outlines the remediation steps required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in Evidence Pack (pipeline failure) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | N/A — no predictions present |
| UK Market Status | Returned as "Not Marketed" — likely a data pipeline error |
| Number of Marketing Authorisations | 0 — likely a data pipeline error |
| Recommended Decision | **Hold** |

> **⚠️ Data Integrity Warning:** Rituximab is currently marketed in the United Kingdom under multiple brand names (including MabThera, Truxima, and Rixathon) with valid MHRA marketing authorisations. A return of zero licences and "Not Marketed" status strongly indicates a failure in the MHRA data ingestion pipeline, not an accurate reflection of UK market reality. Results in this Evidence Pack should not be acted upon until the pipeline is re-run and verified.

---

## Why is This Prediction Reasonable?

No predicted indication is available in this Evidence Pack, so a standard mechanistic rationale linking an original indication to a repurposed target cannot be provided.

For contextual background: Rituximab is a chimeric anti-CD20 monoclonal antibody that selectively depletes CD20-positive B lymphocytes via antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct apoptosis induction. Its established clinical profile spans B-cell haematological malignancies (non-Hodgkin's lymphoma, chronic lymphocytic leukaemia) and systemic autoimmune conditions (rheumatoid arthritis, granulomatosis with polyangiitis, microscopic polyangiitis, and pemphigus vulgaris). Given this immunomodulatory breadth, TxGNN would ordinarily be expected to generate predictions for further B-cell–mediated autoimmune or lymphoproliferative conditions. However, no such predictions exist in the current Evidence Pack and none can be evaluated here.

Detailed mechanism of action data was flagged as a data gap (DG002, severity: High) and has not been retrieved from DrugBank despite a reported successful API query. This inconsistency requires investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## UK Market Information

The data pipeline returned no marketing authorisation records for Rituximab. This contradicts known MHRA registration status and is considered a pipeline failure.

The following products are known to hold UK marketing authorisations based on general pharmacological knowledge (**for reference only — not sourced from this Evidence Pack and must be independently verified against the MHRA register before clinical use**):

| Product Name | Dosage Form | Notes |
|-------------|-------------|-------|
| MabThera (Roche) | Concentrate for solution for infusion | Reference biological medicinal product |
| Truxima (Celltrion Healthcare) | Concentrate for solution for infusion | Biosimilar |
| Rixathon (Sandoz) | Concentrate for solution for infusion | Biosimilar |
| Riximyo (Sandoz) | Concentrate for solution for infusion | Biosimilar |

*These entries are drawn from background knowledge and have not been verified for this report. They must not be treated as confirmed regulatory information.*

---

## Cytotoxicity

Rituximab is used in oncological indications and meets the criteria for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Anti-CD20 chimeric monoclonal antibody (not conventional cytotoxic) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions; B-cell depletion and associated cytopenias are expected |
| Emetogenicity Classification | Please refer to the SmPC; emetogenicity is generally low compared to conventional cytotoxics |
| Monitoring Items | Please refer to the SmPC for full monitoring requirements (full blood count, immunoglobulins, infusion-related reactions, hepatitis B reactivation screening) |
| Handling Protection | Treat as cytotoxic agent; follow local pharmacy and nursing protocols for preparation and administration |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Rituximab (candidate ID: TW-DB00073-multi, v4) contains blocking-level data gaps that prevent any substantive repurposing evaluation — no predicted indications have been generated, UK market authorisation data is absent, and safety information is entirely missing. Proceeding on this basis would carry unacceptable analytical risk.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Re-run MHRA data ingestion to retrieve UK marketing authorisations for Rituximab and all biosimilar entries; validate against the MHRA Product Licence register
- **[Blocking]** Re-run the TxGNN prediction pipeline for DB00073 to generate `predicted_indications`; investigate why the pipeline produced an empty array despite a successful DrugBank query
- **[High — DG002]** Retrieve mechanism of action data from DrugBank API for DB00073; the `query_log` reports a successful result (result_count: 1) yet `original_moa` remains unpopulated — the field mapping logic should be reviewed
- **[High]** Retrieve SmPC safety data (key warnings, contraindications, and drug interactions) from the MHRA/electronic Medicines Compendium (emc)
- Reconcile the `original_indications: []` field with the DrugBank query result — investigate whether the successful API response is being correctly parsed and mapped
- Once predictions are available, reassess evidence level, cytotoxicity, and safety sections with complete data before circulating to clinical stakeholders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

