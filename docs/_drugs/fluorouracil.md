---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Established Antimetabolite Chemotherapy to Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (5-FU) is a fluoropyrimidine antimetabolite; this evidence pack does not record a specific original indication or a UK marketing authorisation for the product under review, and detailed mechanism-of-action documentation is currently missing (data gap). The TxGNN model predicts potential efficacy against **botryoid-type embryonal rhabdomyosarcoma of the vagina**, but this is a **pure knowledge-graph prediction with zero supporting clinical trials and zero supporting publications** — the lowest tier of evidence in this framework.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no UK marketing authorisation on file) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this product is not available in the current evidence pack (data gap, DG002). Based on general pharmacological knowledge of the compound, fluorouracil is a fluoropyrimidine antimetabolite that is converted intracellularly to active metabolites which inhibit thymidylate synthase, blocking DNA synthesis in rapidly dividing cells — the same mechanistic class information appears elsewhere in this evidence pack's rationale for related rhabdomyosarcoma predictions.

Botryoid-type embryonal rhabdomyosarcoma of the vagina is a paediatric soft-tissue sarcoma subtype. Standard chemotherapy for rhabdomyosarcoma is the VAC regimen (vincristine, actinomycin D, cyclophosphamide); fluorouracil is not part of established rhabdomyosarcoma protocols. The evidence pack itself notes that even the broader rhabdomyosarcoma category (a related, higher-level prediction in this same run) is supported only by five tier-3 literature items and no clinical trials, and explicitly flags that the high TxGNN score for that group may reflect an indirect knowledge-graph association (e.g. a shared "paediatric cancer chemotherapy" node) rather than a drug–disease-specific signal.

For this specific candidate — botryoid-type embryonal rhabdomyosarcoma of the vagina — no clinical trial or literature evidence of any kind was retrieved. The prediction should therefore be read as an unvalidated model output pending independent mechanistic or clinical corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisation is currently on record for this product in this evidence pack (0 licences; market status: Not marketed).

---

## Cytotoxicity

Fluorouracil is a conventional cytotoxic antineoplastic agent (fluoropyrimidine antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions — no product-specific toxicity data available in this evidence pack |
| Emetogenicity Classification | Low to moderate (typical for fluoropyrimidine-class agents) |
| Monitoring Items | FBC with differential, renal and hepatic function; DPD (dihydropyrimidine dehydrogenase) deficiency status should be assessed before starting any fluoropyrimidine, per standard UK oncology practice |
| Handling Protection | Cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this evidence pack flags a blocking data gap (DG001) — no MHRA/manufacturer label warnings or contraindications data have been retrieved for this product, which prevents any formal safety pre-assessment (S1 stage).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a knowledge-graph similarity score (L5), with no clinical trials or literature specific to botryoid-type embryonal rhabdomyosarcoma of the vagina, and mechanistically 5-FU is not part of standard rhabdomyosarcoma treatment protocols. A blocking data gap in product safety labelling (DG001) also prevents any safety pre-assessment.

**To proceed, the following is needed:**
- Product label warnings/contraindications (DG001, blocking — required before any safety pre-assessment)
- Confirmed mechanism of action documentation (DG002)
- Disease-specific preclinical or clinical evidence for this indication (currently none identified)
- Clarification of the product's original indication and UK regulatory status, which are not recorded in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

