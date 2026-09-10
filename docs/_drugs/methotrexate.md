---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Methotrexate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Methotrexate: From Established Chemotherapy/Immunomodulatory Use to Pulmonary Blastoma

## One-Sentence Summary

> Methotrexate is a long-established antifolate (DHFR inhibitor) used across oncology, rheumatology and dermatology, but this evidence pack contains no UK licensing or original-indication data for the drug.
> The TxGNN model predicts a possible new application in **Pulmonary Blastoma**, a rare lung malignancy,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no UK licence or original-indication data recorded |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the repurposing rationale provided, methotrexate is a dihydrofolate reductase (DHFR) inhibitor that blocks folate metabolism and thymidylate synthesis — a mechanism common to many antimetabolite chemotherapy regimens used against rapidly proliferating malignant cells.

The predicted link to pulmonary blastoma rests solely on this generic antiproliferative mechanism. There is no disease-specific mechanistic data, preclinical model, or clinical experience connecting methotrexate to pulmonary blastoma in the evidence pack — the rationale text itself notes the absence of any tumour-specific supporting evidence.

Because pulmonary blastoma is an extremely rare biphasic lung tumour and no trials or literature have been identified for this specific drug-disease pairing, the mechanistic plausibility alone (broad antimetabolite activity against dividing cells) is insufficient to support clinical extrapolation at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisation data is available in this evidence pack (market status: Not marketed; 0 licences recorded). This may reflect a gap in the source dataset rather than the drug's true regulatory status, given methotrexate's well-established global use — this should be verified directly against the MHRA/BNF before any decision is finalised.

---

## Cytotoxicity

Methotrexate is a conventional cytotoxic antimetabolite (folate antagonist / DHFR inhibitor) and is treated here as an antineoplastic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite class, folate antagonist) |
| Myelosuppression Risk | High — antimetabolite-class agents typically carry significant bone marrow suppression risk, dose- and schedule-dependent |
| Emetogenicity Classification | Low to moderate (dose-dependent; higher with high-dose intravenous regimens) |
| Monitoring Items | FBC with differential, liver function tests, renal function, folate status |
| Handling Protection | Must follow cytotoxic drug handling regulations (COSHH-compliant preparation, administration and waste disposal) |

*Note: This evidence pack contains no drug-specific toxicity dataset; the above reflects the recognised pharmacological class profile and should be confirmed against the current SmPC.*

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (pulmonary blastoma) is supported only by a TxGNN model score, with zero clinical trials and zero publications — this is Evidence Level L5 (model prediction only). In addition, blocking data gaps exist (UK/TFDA-equivalent warnings and contraindications, and detailed MOA), meaning safety cannot yet be assessed.

**To proceed, the following is needed:**
- MHRA/BNF-sourced warnings, contraindications and drug interaction data for methotrexate
- Confirmed UK marketing authorisation status (the "Not marketed" flag in this pack should be verified, as methotrexate is widely used in UK clinical practice)
- Detailed mechanism of action documentation to support or refute mechanistic relevance to pulmonary blastoma
- Any preclinical or case-level evidence specific to pulmonary blastoma before considering further evaluation

**Additional note:** This evidence pack also contains other predicted indications for methotrexate with substantially stronger evidence — notably **Hodgkin lymphoma** (Evidence Level L2, "Proceed with Guardrails", supported by an RCT and multiple Phase 2/3 trials of MTX-containing regimens such as VBM) and **rhabdomyosarcoma** (Evidence Level L2, "Proceed with Guardrails", supported by a completed Phase 2 trial and disease-specific literature). These candidates warrant separate, dedicated evaluation reports rather than being assessed under the top-ranked but poorly evidenced pulmonary blastoma prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

