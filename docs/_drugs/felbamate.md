---
layout: default
title: Felbamate
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 2
---

# Felbamate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Felbamate: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Felbamate is an anticonvulsant originally used in the management of epilepsy (specific licensed indications are not recorded in the current evidence pack). The TxGNN model predicts it may also be effective for **Trigeminal Neuralgia**, a prediction supported by **1 case report and 4 further publications**, though no clinical trials are currently registered. A second, higher-scoring prediction for trigeminal nerve neoplasm carries no supporting evidence at all and is treated as exploratory only (see note below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the source data (Felbamate is generally recognised as an antiepileptic/anticonvulsant) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.18% (rank 7,051) |
| Evidence Level | L3 (limited — single case report plus narrative review literature; no controlled trials) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Note on a second prediction:** TxGNN also scores Felbamate highly for "trigeminal nerve neoplasm" (99.62%, rank 4,187), which is a slightly higher score than the neuralgia prediction. However, this candidate has **zero** supporting clinical trials, ICTRP records, or literature. It most likely reflects a knowledge-graph node-similarity artefact (shared "trigeminal" terminology) rather than a genuine pharmacological signal, and is not considered further in this report (Evidence Level L5).

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Felbamate is an anticonvulsant; anticonvulsant drugs as a class are well established in the management of neuropathic and paroxysmal pain conditions such as trigeminal neuralgia, because the abrupt, paroxysmal nature of neuralgic pain shares pathophysiological features with seizure activity (both involve abnormal, hyperexcitable neuronal firing).

The supporting literature reflects this class effect directly: carbamazepine is described as the established drug of choice for trigeminal neuralgia, with baclofen, phenytoin and sodium valproate also effective, and a preclinical rat study explicitly lists felbamate alongside carbamazepine, phenytoin and lamotrigine as an anticonvulsant effective against neuropathic pain and trigeminal neuralgia. One case report goes further, describing felbamate directly relieving trigeminal neuralgia pain.

Taken together, this is a mechanistically plausible repurposing signal consistent with a recognised drug-class effect, but the clinical evidence base is thin — it rests on a single historical case report (1995) and supporting review/preclinical literature, with no prospective or controlled human studies to date.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Review | CNS Drugs | Guide to anticonvulsant drug choice in trigeminal neuralgia; carbamazepine is the drug of choice, with baclofen, phenytoin and sodium valproate also effective |
| [8877250](https://pubmed.ncbi.nlm.nih.gov/8877250/) | 1996 | Review | Clinical Pharmacokinetics | Review of clinically significant pharmacokinetic interactions with carbamazepine, relevant background when anticonvulsants are combined or substituted in neuralgia management |
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Case report | The Clinical Journal of Pain | Analgesic efficacy of felbamate evaluated in trigeminal neuralgia; felbamate reported to relieve neuralgic pain |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Case report | The Annals of Pharmacotherapy | Reports a case of felbamate-induced delayed anaphylaxis — a relevant safety signal rather than an efficacy finding |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Preclinical (animal study) | Indian Journal of Pharmacology | Rat model comparing carbamazepine, gabapentin and lamotrigine for neuropathic pain; notes felbamate among anticonvulsants effective in neuropathic pain and trigeminal neuralgia, with variable efficacy |

---

## UK Market Information

No UK marketing authorisation is currently recorded for Felbamate in the source data (market status: **Not marketed**; total licences: **0**). As a result, no product/formulation details (BNF classification, dosage form, authorised indication text) are available to report.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Additionally, the literature search surfaced a historical case report of **felbamate-induced delayed anaphylaxis** (PMID 7633024). This is not part of the structured safety dataset but is flagged here as a signal warranting attention during any future safety evaluation — felbamate is also independently known to carry serious haematological and hepatic warnings in other jurisdictions, which should be confirmed via primary regulatory sources before further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (trigeminal neuralgia) is mechanistically plausible and supported by a recognised anticonvulsant class effect, but the direct evidence is limited to a single 30-year-old case report and narrative reviews, with no clinical trials or ICTRP-registered studies identified.
- Felbamate has no current UK marketing authorisation (0 licences), and two data gaps block progression: TFDA/SmPC warnings and contraindications are entirely missing (**Blocking** — required for initial safety screening), and the mechanism of action is undocumented (**High** severity).

**To proceed, the following is needed:**
- SmPC/product warnings, contraindications and drug interaction data (currently a blocking gap)
- Confirmed mechanism of action data from DrugBank or another authoritative source
- Confirmation of Felbamate's original licensed indication(s), which are not currently recorded
- Any prospective, controlled, or registry-based studies of felbamate in trigeminal neuralgia, to move beyond single-case-report evidence
- Clarification of whether the "trigeminal nerve neoplasm" prediction reflects a genuine signal or a knowledge-graph artefact, before any further action on that candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

