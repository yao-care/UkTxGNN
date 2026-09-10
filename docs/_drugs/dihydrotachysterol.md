---
layout: default
title: Dihydrotachysterol
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Dihydrotachysterol
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

# Dihydrotachysterol: From Vitamin D Analogue Therapy to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Dihydrotachysterol is a synthetic vitamin D2 analogue; structured records of its original licensed indication and mechanism of action are not available in this evidence pack. The TxGNN model's top-ranked prediction for this drug is **Obsolete Vitamin D Deficiency**, a disease term itself flagged as deprecated, with **no clinical trials and no literature** currently supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — no UK marketing authorisation exists for Dihydrotachysterol (see "Why is This Prediction Reasonable" below) |
| Predicted New Indication | Obsolete Vitamin D Deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the current dataset (flagged as a High-severity data gap, DG002, requiring DrugBank API lookup). However, literature contained elsewhere in this same evidence pack (e.g. PMID 3320562) independently describes Dihydrotachysterol2 as "a synthetic analogue of vitamin D2" that has been "used extensively in the treatment of renal osteodystrophy and hypoparathyroidism," and does not require renal 1α-hydroxylation to become active — unlike native vitamin D.

Given this, the TxGNN prediction of "Obsolete Vitamin D Deficiency" as the top-ranked candidate is mechanistically almost tautological: it reflects the drug's core pharmacological action as a vitamin D replacement agent, rather than a genuinely novel repurposing signal. The disease term itself is marked as obsolete in the underlying vocabulary (a deprecated classification, likely superseded by more specific ICD/SNOMED terms), which limits its practical use for indication-level decision-making.

Critically, no clinical trials or literature in this evidence pack directly support this specific candidate — searches against ClinicalTrials.gov, ICTRP and PubMed for "Dihydrotachysterol" + "obsolete vitamin D deficiency" all returned zero results (query log IDs 2–4). The prediction should therefore be treated as an artefact of strong mechanistic proximity rather than an independently evidenced new indication, and is not suitable for progression without further data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Dihydrotachysterol is not currently marketed in the UK. No MHRA marketing authorisations are on record for this product (0 licences), and no dosage forms or approved indication text are available for reference.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: TFDA/MHRA labelling warnings and contraindications for this drug are recorded as a Blocking data gap (DG001) and have not yet been retrieved.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction ("Obsolete Vitamin D Deficiency") has no supporting clinical trial or literature evidence, uses a deprecated disease term, and largely restates the drug's known pharmacological class rather than identifying a novel indication. Combined with the absence of MOA data, UK licensing data, and safety/contraindication data, there is insufficient basis to advance this specific candidate.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank (DG002, High severity)
- TFDA/MHRA SmPC warnings and contraindications (DG001, Blocking severity)
- Resolution of the obsolete disease-term mapping to a current, actionable diagnostic classification
- Consideration of re-scoping the primary candidate: this same evidence pack contains a substantially better-evidenced prediction — **renal osteodystrophy** (rank 7, Evidence Level L2, decision stage S2, recommendation "Proceed with Guardrails," supported by 20 literature citations including one RCT, PMID 8151464) — which may warrant its own dedicated evaluation report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

