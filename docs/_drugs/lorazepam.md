---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From [Indication Data Unavailable] to Trigeminal Nerve Neoplasm

## One-Sentence Summary

> Detailed original-indication data for lorazepam is not available in this evidence pack; internationally, lorazepam is a well-established benzodiazepine used for anxiety, insomnia and status epilepticus. The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm**, but this candidate currently has **no supporting clinical trials or literature**, and the model itself flags this association as likely graph noise rather than a biologically plausible signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap); lorazepam is internationally used for anxiety, insomnia and seizure control |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| UK Market Status | Not currently marketed (no MHRA licence on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lorazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, enhancing chloride ion influx to produce sedative, anxiolytic and anticonvulsant effects. Its established uses internationally include anxiety disorders, short-term insomnia, and acute seizure/status epilepticus management.

There is no known mechanistic relationship between GABA-A receptor modulation and trigeminal nerve neoplasm biology (tumour proliferation, angiogenesis or oncogenic signalling pathways). The evidence pack's own rationale for this candidate explicitly states that the high TxGNN score is likely attributable to knowledge-graph connectivity noise rather than genuine biological plausibility, and no clinical trials or literature support this indication.

**Note for reviewers:** Lower-ranked candidates in this evidence pack — particularly **insomnia (rank 2, evidence level L3)** — show a far stronger and more coherent evidence base, including 21 registered clinical trials and a well-established pharmacological class rationale. If a repurposing signal is to be pursued from this dataset, insomnia is the substantially stronger candidate and is discussed further in the Conclusion below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Lorazepam is not currently marketed under this evidence pack's regulatory dataset — no MHRA marketing authorisation numbers were found (`total_licenses: 0`). No product listings are available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Outstanding data gaps identified:**
- **TFDA-equivalent labelling (warnings/contraindications)** — Blocking severity; prevents S1 safety pre-assessment. Recommended remediation: obtain and parse the official SmPC/labelling document.
- **Mechanism of action (MOA) detail** — High severity; affects mechanistic-relevance analysis. Recommended remediation: query DrugBank directly for structured MOA data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (trigeminal nerve neoplasm) has no supporting clinical trial or literature evidence, no plausible mechanistic link, and the evidence pack itself characterises the signal as likely model noise (Evidence Level L5, decision stage S0). Combined with blocking data gaps in safety labelling and MOA, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Official product labelling (warnings, contraindications) to close DG001 before any S1 safety pre-assessment
- Structured MOA data from DrugBank to close DG002
- If pursuing this dataset further, redirect evaluation toward **insomnia (rank 2)**, which has 21 registered trials, an L3 evidence level, and a coherent class-effect mechanistic rationale — a substantially more actionable candidate than the current top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

