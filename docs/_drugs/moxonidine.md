---
layout: default
title: Moxonidine
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Moxonidine
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

# Moxonidine: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Moxonidine is a centrally acting antihypertensive (imidazoline I1-receptor agonist), understood from the evidence pack's own contextual notes to be indicated for essential hypertension, though this is not confirmed by a formal licence record. The TxGNN model's top-ranked prediction proposes possible relevance to **Hypotrichosis Simplex of the Scalp**, but this signal is currently supported by **no clinical trials** and **no literature**, and the evidence pack's own mechanistic review concludes there is no known biological link between the drug and this rare hair-follicle disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (essential hypertension) — inferred from supporting rationale text in the evidence pack; not confirmed by a formal licence record (see Data Gaps DG001/DG002) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for moxonidine is not available in this evidence pack (flagged as Data Gap DG002, High severity). Based on the contextual information provided across the evidence pack's own rationale entries, moxonidine is known to act as a centrally acting sympatholytic agent — an imidazoline I1-receptor agonist that reduces central sympathetic outflow and systemic vascular resistance — and is described elsewhere in this same dataset as an approved treatment for essential hypertension.

For this specific predicted indication, however, the evidence pack's own repurposing rationale is explicit that **no plausible mechanistic connection exists**: hypotrichosis simplex of the scalp is a rare hereditary hair-follicle developmental disorder, and its pathophysiology has no known relationship to central sympathetic inhibition or blood-pressure regulation. No supporting clinical trials or literature were identified for this drug–disease pairing.

Taken together, this indicates the prediction is most likely a knowledge-graph embedding artefact (a statistical similarity signal) rather than a biologically grounded hypothesis. It is presented here because it is the model's highest-scoring candidate, but the score alone should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Moxonidine currently holds no marketing authorisation in the UK (0 licences on record; market status: **not marketed**). No product, dosage form, or licensed indication details are available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at evidence level L5 (model prediction only) with no supporting clinical trials, no literature, and — per the evidence pack's own mechanistic assessment — no known biological rationale linking moxonidine to hypotrichosis simplex of the scalp. There is no basis to progress this specific pairing beyond the prediction stage.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for moxonidine from DrugBank/SmPC (currently Data Gap DG002)
- Formal TFDA/MHRA labelling data, including warnings and contraindications (currently Data Gap DG001, Blocking)
- Independent dermatological/genetic mechanistic assessment before any further investment in this specific indication
- Note for prioritisation: other candidates in this batch — e.g. *malignant hypertensive renal disease* / *malignant renovascular hypertension* (L4, extension of the existing hypertension indication) and *primary hereditary glaucoma* (L4, class-effect rationale via imidazoline/α2-agonist pharmacology) — carry substantially stronger mechanistic plausibility and may warrant evaluation ahead of this top-ranked but mechanistically unsupported signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

