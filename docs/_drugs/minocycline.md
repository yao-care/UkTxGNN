---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Minocycline
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

# Minocycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a broad-spectrum tetracycline-class antibiotic, originally used to treat bacterial infections through inhibition of bacterial protein synthesis. The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but currently **no clinical trials and no published literature** support this specific prediction — it is a model-generated hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (tetracycline-class antibiotic) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for minocycline is not available in this evidence pack. Based on known pharmacology, minocycline is a tetracycline-class antibiotic that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit. Independent of its antibacterial activity, tetracyclines also possess anti-inflammatory, anti-matrix-metalloproteinase (anti-MMP), and anti-apoptotic properties, which have been explored in non-infectious ophthalmic and dermatological contexts.

The original indication (bacterial infections) and the predicted new indication (a corneal surface disorder) are mechanistically distant, but a class-level precedent exists: doxycycline, a closely related tetracycline, is already used off-label as adjunctive therapy for corneal epithelial disease because of its anti-inflammatory and anti-MMP effects rather than its antibacterial action. This provides a plausible theoretical rationale for minocycline in punctate epithelial keratoconjunctivitis.

However, this rationale is extrapolated entirely from class effect. No minocycline-specific preclinical, trial, or case-report evidence for this indication exists in the current evidence pack, so the mechanistic plausibility should be treated as a hypothesis to be tested, not as supportive evidence in itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations are recorded for minocycline in this evidence pack (market status: **not marketed**; total licences: **0**). No product, dosage form, or approved-indication data are available to tabulate.

---

## Safety Considerations

Formal safety fields (key warnings, contraindications, drug interactions) are not available in this evidence pack. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Additional note from the evidence pack:** although not part of the formal safety dataset, one of the other TxGNN-predicted indications for minocycline (rank 4, "postinfectious vasculitis") was explicitly flagged as a **negative safety signal rather than a repurposing opportunity** — long-term minocycline use is a recognised cause of ANCA-associated vasculitis and drug-induced lupus-like syndrome. This should be borne in mind in any onward safety assessment of minocycline generally, independent of the keratoconjunctivitis prediction discussed here.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (punctate epithelial keratoconjunctivitis) is supported only by a TxGNN model score (L5, decision stage S0) with no corroborating clinical trials or literature. A blocking data gap also exists for MHRA/SmPC warnings and contraindications (DG001), which prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- MHRA/SmPC warnings, contraindications, and interaction data for minocycline (currently blocking — DG001)
- Confirmed mechanism-of-action documentation, ideally via DrugBank (DG002)
- Preclinical or in vitro evidence specifically evaluating minocycline (not just class-level doxycycline data) in corneal epithelial disease
- If preclinical signal is positive, a small pilot/observational study before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

