---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin: From Clostridium difficile Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

> Fidaxomicin is a narrow-spectrum, gut-targeted antibiotic developed for **Clostridioides difficile infection (CDI)**, based on the mechanistic context available in this evidence pack (no UK marketing authorisation is currently on record).
> The TxGNN model predicts it may be effective for **Staphylococcal Scalded Skin Syndrome (SSSS)**,
> but **no clinical trials and no supporting literature** currently exist for this specific indication, and the evidence pack itself flags the mechanistic link as weak, likely knowledge-graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in UK licensing data (no MHRA marketing authorisation on record); evidence-pack rationale indicates fidaxomicin's established target is *Clostridioides difficile* infection |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only; no trials or literature) |
| UK Market Status | Not marketed (no licence currently held) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fidaxomicin is not available in this evidence pack. Based on the contextual information present, fidaxomicin is a narrow-spectrum macrolide-class antibiotic with very low systemic absorption — it remains largely confined to the gastrointestinal tract, which is why it is used against *C. difficile* there rather than as a systemically distributed antibacterial.

SSSS, by contrast, is a **systemic, toxin-mediated skin disease** caused by exfoliative toxins produced by *Staphylococcus aureus*, requiring a drug that reaches therapeutic concentrations in the skin/bloodstream, together with confirmed anti-staphylococcal killing activity. The evidence pack's own mechanistic analysis for this candidate states that fidaxomicin's minimal systemic absorption and its unestablished efficacy against *S. aureus* make this pairing pharmacologically implausible, and assesses it as likely **knowledge-graph noise** rather than a genuine biological signal.

Taken together, the mechanistic rationale for this prediction is weak: there is no shared target pathway between fidaxomicin's known site of action (colonic lumen, anaerobic Gram-positive/​*C. difficile*-directed activity) and the systemic anti-staphylococcal exposure that SSSS treatment would require.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this evidence pack flags UK product-label warnings/contraindications as a **Blocking** data gap (DG001) — safety cannot be formally assessed until this is resolved.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5), and the evidence pack's own mechanistic assessment concludes the drug–disease link is pharmacologically weak and likely a knowledge-graph artefact rather than a genuine repurposing signal. No further action is warranted on this indication without new supporting data.

**To proceed, the following is needed:**
- TFDA/MHRA product-label warnings and contraindications (Blocking gap, DG001) — required before any S1 safety screening can occur
- Confirmed mechanism of action data (High-priority gap, DG002)
- In vitro or in vivo evidence of fidaxomicin activity against *S. aureus* exfoliative-toxin-producing strains
- Pharmacokinetic data demonstrating systemic/dermal exposure sufficient for SSSS treatment
- If pursuing repurposing further, evaluate the higher-evidence candidate in this pack instead — *Staphylococcus aureus* pneumonia (rank 8, L4) — which has at least one supporting literature reference, though still only a narrative review, not primary data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

