---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Gefitinib: From EGFR Mutation-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib (Iressa®) is an EGFR/HER1 tyrosine-kinase inhibitor internationally established for EGFR mutation-positive non-small cell lung cancer (NSCLC). The TxGNN model's top-ranked prediction in this batch is **Gingival Fibromatosis**, but this candidate is supported by **0 clinical trials** and **0 publications** — it is a computational signal only, with no corroborating evidence and no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack's regulatory dataset (no UK/local marketing authorisation on file); gefitinib is globally established as an EGFR-TKI for EGFR mutation-positive NSCLC, as referenced repeatedly within the accompanying literature evidence |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal mechanism-of-action field for gefitinib was flagged in this evidence pack as a data gap (DG002, High severity). However, context embedded throughout the accompanying literature evidence consistently identifies gefitinib as a first-generation EGFR (HER1) tyrosine-kinase inhibitor, blocking EGFR autophosphorylation to inhibit downstream proliferative and angiogenic signalling in EGFR-driven tumours — the basis for its established use in NSCLC.

Gingival fibromatosis, by contrast, is a benign fibrous overgrowth of gingival tissue with no established pathological connection to the EGFR signalling pathway. Notably, EGFR-TKIs are more commonly associated with *causing* mucocutaneous and oral toxicities (e.g. mucositis, paronychia) than with treating fibrous overgrowth — if anything, the known toxicity profile points away from, not towards, this indication.

The evidence pack's own analysis is explicit on this point: *"No clinical trial or literature evidence exists; gingival fibromatosis has no known direct pathological association with the EGFR pathway — this is a pure TxGNN prediction score."* This ranking should therefore be interpreted as an artefact of the model's learned embedding space (e.g. shared graph neighbours with head-and-neck-related nodes) rather than a biologically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Gefitinib holds **0 marketing authorisations** on record in this dataset, and market status is recorded as **"Not marketed."** No licence numbers, product names, or approved-indication text are available to tabulate.

---

## Cytotoxicity

Gefitinib is an antineoplastic agent (EGFR/HER1 tyrosine-kinase inhibitor used in NSCLC), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER1 tyrosine-kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — myelosuppression is not a predominant toxicity of EGFR-TKIs; literature accompanying this pack instead highlights dermatological reactions (acneiform rash), interstitial lung disease, and QT-interval prolongation as more characteristic signals |
| Emetogenicity Classification | Low (oral small-molecule targeted agent) |
| Monitoring Items | Liver function tests, ECG/QTc, respiratory symptoms (interstitial lung disease), skin toxicity, renal function |
| Handling Protection | Not a classical cytotoxic; nonetheless, many institutions apply hazardous-drug handling precautions to oral EGFR-TKIs during dispensing (e.g. under NIOSH hazardous drug lists where locally adopted) — confirm against local policy |

---

## Safety Considerations

Formal safety fields (key warnings, contraindications, drug interactions) are all unavailable in this evidence pack (DG001, Blocking severity — TFDA/SmPC label data not yet retrieved).

**Signals noted in the accompanying literature (not SmPC-sourced, for awareness only):** QT-interval prolongation (PMID 34474028), interstitial lung disease (PMID 20949670, PMID 20942679), and cutaneous toxicity (PMID 18931563) have been reported with gefitinib in its established oncology use.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Candidate Signals in This Batch

This evidence pack scored 10 predicted indications for gefitinib. Most are unsupported (L5/Hold); three reached L4/"Research Question" status because they represent anatomical subtypes of NSCLC — gefitinib's own established tumour class — rather than genuinely novel biology:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 5 | Lung hilum carcinoma | 99.86% | L4 | S1 (Research Question) | Anatomical NSCLC subtype; 1 case report only |
| 8 | Lung germ cell tumour | 99.84% | L4 | S1 (Research Question) | Sole matching trial was head-and-neck/NSCLC, not germ cell tumour |
| 9 | Pulmonary sulcus (Pancoast) neoplasm | 99.84% | L4 | S1 (Research Question) | NSCLC anatomical subtype; no subtype-specific trial |
| 1, 2, 4, 6, 7, 10 | Gingival fibromatosis, lung fibroma, lung hamartoma, lung benign neoplasm, rare genetic syndrome, junctional epidermolysis bullosa | 99.84–99.89% | L4–L5 | S0 (Hold) | No credible mechanistic link; evidence is absent or mismatched (keyword co-occurrence noise) |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate (Gingival Fibromatosis) has no clinical trial or literature support and no plausible mechanistic rationale — it does not meet the threshold to progress past S0.
- A Blocking-severity data gap (missing TFDA/SmPC safety data) independently prevents any safety pre-screening (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- Retrieval of the product label/SmPC (warnings, contraindications, DDI) to close DG001
- Formal DrugBank MOA confirmation to close DG002
- If pursuing the more mechanistically coherent NSCLC-subtype signals (ranks 5, 8, 9) instead, subtype-specific trial data or case-series evidence, since current literature is either single case reports or drawn from unrelated patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

