---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Clindamycin
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

Using the evidence pack for **Clindamycin (DB01190) → Punctate epithelial keratoconjunctivitis** (rank 1 predicted indication), here is the evaluation report.

---

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic conventionally used against anaerobic and Gram-positive bacterial infections; detailed original-indication and mechanism-of-action data were not available in this evidence pack. The TxGNN model predicts a very high association with **punctate epithelial keratoconjunctivitis** (score 99.97%), but this is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review flags the prediction as likely a knowledge-graph proximity artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (data gap); Clindamycin is generically indicated for anaerobic and Gram-positive bacterial infections |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Clindamycin is not available in this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacology, Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit, and it is effective against anaerobic and Gram-positive organisms. No original-indication text was supplied here, so a direct like-for-like comparison with the predicted indication cannot be made from the pack alone.

Punctate epithelial keratoconjunctivitis is, however, predominantly a **viral** (notably adenoviral), **dry-eye**, or **toxic/reactive** corneal epithelial condition rather than a primary bacterial infection. Clindamycin's antibacterial mechanism has no established direct mode of action against these underlying processes. The evidence pack's own mechanistic analysis explicitly notes that the very high TxGNN score most likely reflects the proximity of "ophthalmic disease" nodes within the knowledge graph, rather than a true pharmacological relationship — and no clinical trial or literature evidence was found to counter this concern.

On this basis, the mechanistic rationale for this specific prediction is weak, and it should be treated as a hypothesis-generating signal only, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Clindamycin currently holds **no marketing authorisation** recorded in this evidence pack, and market status is listed as **not marketed**. No product, dosage form, or approved-indication data are available for tabulation. Should marketing status change or licence data become available, this section should be repopulated from the MHRA product register and cross-checked against the BNF entry for Clindamycin.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications, and drug–drug interaction data were all recorded as data gaps in this evidence pack — including a Blocking-severity gap on TFDA/MHRA label warnings and contraindications — so no drug-specific safety details can be reported at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this is unsupported by any clinical trial or literature evidence (Evidence Level L5 — model prediction only), and the mechanistic review itself concludes that the predicted disease's pathology (largely viral/non-infectious) is not addressed by Clindamycin's antibacterial mechanism. Combined with the Blocking-severity data gap on safety labelling and the drug's current non-marketed status in the UK, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed original indication and full mechanism-of-action data for Clindamycin (currently missing)
- MHRA/SmPC warnings, contraindications, and interaction data (Blocking data gap — required before any safety assessment)
- Targeted literature/trial search specifically on ocular or anti-infective use of Clindamycin in keratoconjunctivitis to test whether the TxGNN signal reflects a genuine secondary-infection use case
- Independent mechanistic review to rule out knowledge-graph node-proximity bias, given the reviewer's own concern that this result may be an artefact
- Re-evaluation of the other nine ranked candidates in this pack, several of which (e.g. exposure keratitis, rank 2) show marginally stronger — though still indirect — literature support and may warrant priority over this top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

