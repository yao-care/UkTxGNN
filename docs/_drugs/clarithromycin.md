---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 5
---

# Clarithromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the evidence pack provided, here is the evaluation report.

---

# Clarithromycin: From Bacterial Infection to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Clarithromycin is a macrolide antibacterial; the specific original indication text was not captured in this evidence pack, and detailed mechanism-of-action data is also missing. The TxGNN model predicts a possible link to **Polyclonal Hyperviscosity Syndrome**, but **no clinical trials and no literature** currently support this specific pairing — this is a model-only signal that requires substantial further validation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack — original indication text was not captured (Clarithromycin is a macrolide antibacterial; confirm exact licensed wording via SmPC) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (no current MHRA marketing authorisation on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Clarithromycin is not available in this evidence pack. Based on general pharmacological knowledge, Clarithromycin is a macrolide-class antibacterial with established antibacterial and immunomodulatory activity (including suppression of pro-inflammatory cytokines); however, no confirmed molecular pathway links it to Polyclonal Hyperviscosity Syndrome in the data reviewed.

Polyclonal Hyperviscosity Syndrome results from excessive polyclonal immunoglobulin production causing increased blood viscosity, and is typically seen in autoimmune disease, chronic infection, or HIV-related conditions. Clarithromycin's antibacterial and anti-inflammatory mechanisms have no direct known relationship to the plasma-cell/B-cell immunoglobulin overproduction that underlies this condition.

Any plausible effect would most likely be **indirect** — for example, by controlling an underlying chronic infection that is itself driving polyclonal immunoglobulin production — rather than a direct pharmacological effect on the disease process. The evidence pack itself characterises this link as speculative and lacking specific molecular mechanistic support. This should be regarded as a low-confidence, hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Clarithromycin currently holds **no MHRA marketing authorisation** in this dataset (market status: Not marketed; 0 licences on record). No product-level UK licensing details (PL numbers, product names, dosage forms) are available to report.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: key warnings, contraindications and drug-interaction data were not available in this evidence pack. Retrieval of product warning/contraindication data (via SmPC) is flagged as a **Blocking** data gap (DG001) that must be resolved before any formal safety pre-assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (Polyclonal Hyperviscosity Syndrome) is supported only by the TxGNN model score (Evidence Level L5) — there are no clinical trials or literature connecting Clarithromycin to this condition, and the proposed mechanistic link is explicitly characterised as speculative.
- A **Blocking** data gap (missing product warnings/contraindications, DG001) currently prevents this candidate from entering a formal safety pre-assessment (S1), and mechanism-of-action data (DG002) is also missing, limiting confidence in the mechanistic rationale.
- Clarithromycin is not currently marketed in the UK per the data reviewed, removing the option of near-term off-label use under an existing authorisation.

**To proceed, the following is needed:**
- SmPC-derived warnings and contraindications for Clarithromycin (resolves Blocking gap DG001)
- Confirmed mechanism-of-action data from DrugBank (resolves High-priority gap DG002)
- Independent preclinical or clinical evidence directly linking Clarithromycin to the pathophysiology of Polyclonal Hyperviscosity Syndrome
- Confirmation of the original licensed indication text and current UK marketing-authorisation status

---

### Supplementary Note: Other Candidates in This Evidence Pack

This evidence pack contains four additional TxGNN-predicted indications for Clarithromycin, ranked 2–5. Most (Hyperamylasemia, Congenital Analbuminemia, Blood Group Incompatibility) are similarly Evidence Level L4–L5 with weak or incidental supporting data and a "Hold" recommendation.

One candidate stands out: **Punctate Epithelial Keratoconjunctivitis** (rank 4, TxGNN score 99.11%) reached decision stage **S1 ("Research Question")** rather than S0/Hold. Its rationale notes that macrolide-class antibacterials (e.g., azithromycin, doxycycline) already have precedent for treating meibomitis-related keratoconjunctivitis via anti-inflammatory effects on the meibomian glands, and one supporting publication (PMID 38472959) discusses meibomitis-related keratoconjunctivitis treatment outcomes — though it is not yet confirmed whether that study used Clarithromycin specifically or a related macrolide (a class-effect distinction that needs full-text verification). This candidate may warrant separate, closer follow-up ahead of the primary candidate discussed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

