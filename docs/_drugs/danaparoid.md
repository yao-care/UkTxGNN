---
layout: default
title: Danaparoid
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 6
---

# Danaparoid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Danaparoid: From Anticoagulation (HIT) to Glanzmann Thrombasthenia

## One-Sentence Summary

Danaparoid is a heparinoid anticoagulant conventionally used to manage heparin-induced thrombocytopenia (HIT), where its mechanism is Factor Xa/IIa inhibition to reduce clot formation. The TxGNN model's top prediction is **Glanzmann Thrombasthenia**, a congenital bleeding disorder — but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the drug's mechanism runs in the opposite direction to what the disease requires.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heparin-induced thrombocytopenia (HIT) / anticoagulation, based on known clinical use — no MHRA-approved indication text is present in this dataset |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from official sources for this candidate (marked as a data gap). However, from known pharmacology, Danaparoid is a heparinoid that acts primarily via antithrombin-mediated inhibition of Factor Xa (with minor Factor IIa activity), reducing the blood's clotting capacity. It is clinically used for anticoagulation in patients with HIT.

Glanzmann Thrombasthenia is a congenital bleeding disorder caused by a defect in the platelet GPIIb/IIIa receptor, which impairs platelet aggregation. Patients with this condition already have **reduced**, not excessive, clotting capacity. Administering an anticoagulant such as Danaparoid would not correct the underlying receptor defect and could plausibly **worsen bleeding risk** rather than treat the disease.

This mismatch suggests the high TxGNN score most likely reflects a directional artefact in the knowledge graph — the model appears to be picking up "drug–platelet pathway" node proximity without distinguishing between a *pro-coagulant deficiency* (which needs pro-haemostatic treatment) and an *anticoagulant therapy* (which treats excessive clotting). The same pattern applies to the other five predicted indications in this evidence pack (primary platelet release disorder, pseudo-von Willebrand disease, collagen receptor defect bleeding diathesis, constitutional thrombocytopenia, and Scott syndrome) — all are congenital bleeding/platelet disorders where an anticoagulant is mechanistically contraindicated rather than therapeutic.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Danaparoid is currently **not marketed** under this evidence pack's regulatory dataset, and no marketing authorisation record is available (0 licences on file). No product/dosage form information can be provided.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags TFDA-equivalent labelled warnings/contraindications as a **Blocking** data gap (DG001) and mechanism-of-action detail as a **High** severity data gap (DG002) — neither is available for independent verification at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only — no clinical trials or literature identified for any of the 6 candidate indications), and the drug's known mechanism (anticoagulation) is directionally opposed to the therapeutic need in Glanzmann Thrombasthenia and the other candidate diseases (all bleeding/platelet-function disorders). There is a plausible risk of harm rather than benefit if pursued clinically.

**To proceed, the following is needed:**
- Resolution of the Blocking data gap (DG001): official labelled warnings/contraindications for Danaparoid
- Resolution of the High-severity data gap (DG002): confirmed mechanism of action detail, to formally assess mechanistic plausibility
- A mechanistic review of why TxGNN is scoring anticoagulants highly against congenital bleeding disorders, to determine whether this reflects a systematic direction-of-effect issue in the knowledge graph
- Independent pharmacological or expert clinical review before this candidate is considered for any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

