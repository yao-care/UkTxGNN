---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Unspecified Original Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

The original licensed indication for dutasteride is not recorded in the current data pack, though the evidence pack's own mechanistic notes describe it as a type I/II 5α-reductase inhibitor that lowers dihydrotestosterone (DHT), a mechanism with established relevance to androgen-dependent conditions. The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the prediction as mechanistically implausible — the drug's known effect (reduced hair growth) runs in the opposite direction to the predicted indication (excessive hair growth).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source data (see Data Gap DG002) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.9979% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per data pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for dutasteride is marked as a data gap in this pack (DG002, High severity). However, the rationale fields attached to other predicted indications in this same evidence pack describe dutasteride as an inhibitor of type I and type II 5α-reductase, which reduces conversion of testosterone to DHT — a mechanism with well-established relevance to androgen-driven conditions such as androgenetic alopecia.

Ambras type hypertrichosis universalis congenita is a rare congenital disorder associated with chromosome 8 rearrangements, causing diffuse excessive hair growth. It is not an androgen-mediated condition, and its pathophysiology has no known connection to the 5α-reductase/DHT pathway.

Critically, the evidence pack's own repurposing rationale for this candidate states that the predicted direction is **opposite** to dutasteride's known pharmacology: dutasteride suppresses hair growth via DHT reduction, whereas hypertrichosis is a disorder of excessive hair growth. The rationale explicitly concludes there is "no mechanistic plausibility" and "no evidence," suggesting this ranking likely reflects a knowledge-graph proximity artefact (e.g. shared "hair-related" nodes) rather than a genuine pharmacological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered. ClinicalTrials.gov, ICTRP, and PubMed queries for "Dutasteride" + "Ambras type hypertrichosis universalis congenita" (dated 2026-03-26) all returned zero results (query_log IDs 2–4).

## Literature Evidence

Currently no related literature available.

## UK Market Information

No marketing authorisations are recorded in this data pack (market status: not marketed; 0 licences on file). This may reflect incomplete data collection rather than confirmed regulatory status — TFDA/MHRA product labelling data collection for this drug is listed as a Blocking data gap (DG001). Prescribers should verify current UK authorisation status directly against the MHRA products database and BNF before relying on this report.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature support dutasteride's use in Ambras type hypertrichosis universalis congenita, and the predicted mechanism directly contradicts the drug's established pharmacology (DHT suppression reduces hair growth, whereas this condition is defined by excessive hair growth). The evidence pack's own assessment treats this as a likely knowledge-graph false positive rather than a credible repurposing signal.

**To proceed, the following is needed:**
- Resolution of the Blocking data gap (DG001): TFDA/MHRA SmPC warnings and contraindications
- Resolution of the High-severity data gap (DG002): confirmed mechanism of action documentation
- Confirmation of dutasteride's original indication(s) and current UK marketing authorisation status
- If pursuing repurposing research on this drug, consider redirecting attention to candidates with plausible mechanistic grounding — e.g. rank 8, diffuse alopecia areata, currently at evidence level L4 / decision stage S1 ("Research Question") — rather than this rank 1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

