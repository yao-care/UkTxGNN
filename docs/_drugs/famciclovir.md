---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is an oral antiviral prodrug of penciclovir, with its established efficacy in herpes zoster (shingles) and genital herpes caused by varicella-zoster virus (VZV) and herpes simplex virus (HSV). The TxGNN model's highest-scoring prediction for this drug is **Post-Infectious Neuralgia** (score 99.75%), but currently **no clinical trials and no published literature** in this evidence pack are indexed specifically against this predicted indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this evidence pack (no UK marketing authorisation data available); famciclovir's established pharmacological indications are herpes zoster and genital herpes (HSV/VZV infections) |
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as data gap DG002, High severity). Based on established pharmacological knowledge, famciclovir is the oral prodrug of penciclovir, a synthetic acyclic guanosine analogue. In cells infected with herpesviruses (HSV-1, HSV-2, VZV), viral thymidine kinase phosphorylates penciclovir to its active triphosphate form, which competitively inhibits viral DNA polymerase and halts viral DNA replication. Famciclovir's proven clinical efficacy lies in treating herpes zoster and genital herpes.

Post-infectious neuralgia is nerve pain arising after an infection, and its best-recognised clinical form is postherpetic neuralgia (PHN) — the most common long-term complication of herpes zoster reactivation. Because famciclovir treats the underlying VZV infection that causes shingles, and the related evidence collected under this drug's "chickenpox/herpes zoster" prediction (see below) shows that prompt antiviral treatment shortens zoster-associated pain and is discussed in relation to reducing postherpetic neuralgia risk, there is a plausible biological pathway connecting famciclovir's established use to this predicted indication.

However, this evidence pack currently returns **zero clinical trials and zero publications** specifically indexed against the term "post-infectious neuralgia" for famciclovir. It is not yet clear whether TxGNN's high score reflects a genuine signal carried over from the closely related, already-evidenced postherpetic neuralgia pathway, or an artefact of how the two terms are mapped in the underlying ontology. This ambiguity should be resolved before further evaluation (see Next Steps).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Famciclovir currently holds no identified marketing authorisations in this evidence pack (market status: **Not marketed**; total licences: **0**). No product-specific dosage form or indication information is available for the UK market at this time.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
With zero clinical trials or publications currently indexed against "post-infectious neuralgia" specifically, and with mechanism-of-action data flagged as an unresolved data gap, there is insufficient direct evidence to advance this prediction. The plausible mechanistic overlap with postherpetic neuralgia (an established complication of herpes zoster for which antiviral treatment has supporting evidence) has not yet been confirmed as applicable to this exact predicted term.

**To proceed, the following is needed:**
- Clarify whether "post-infectious neuralgia" in the TxGNN ontology is synonymous with postherpetic neuralgia; if confirmed, cross-reference the herpes zoster evidence already collected for famciclovir (e.g. trials NCT01327144, NCT03120962, and literature such as PMID 29431387) to reassess the evidence level
- Resolve DG001 (Blocking): obtain the UK SmPC/product information to complete the safety pre-screen (S1)
- Resolve DG002 (High): confirm detailed mechanism of action via the DrugBank API
- Confirm famciclovir's original UK indications and marketing authorisation status, since none are currently recorded in this evidence pack
- If the ontology mapping is confirmed distinct from postherpetic neuralgia, commission a targeted literature and trial search specifically for "post-infectious neuralgia" and famciclovir before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

