---
layout: default
title: Mizolastine
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Mizolastine
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

# Mizolastine: From H1-Antihistamine Use to Acute Intermittent Porphyria

## One-Sentence Summary

Mizolastine is a second-generation, peripherally-selective H1-antihistamine; no marketing authorisation or approved-indication text is currently recorded for it in this evidence pack, and the drug is **not currently marketed** in the UK.
The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria**, with a prediction score of **99.76%**, but **zero clinical trials and zero publications** currently support this direction — the signal rests entirely on the knowledge-graph model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — no UK marketing authorisation is on file (mechanistically characterised only as a second-generation H1-antihistamine) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the information that is available, Mizolastine is a second-generation H1-receptor antagonist with low anticholinergic activity and poor blood–brain-barrier penetration — a peripherally-selective antihistamine rather than a first-generation, centrally-active agent.

Acute intermittent porphyria is a metabolic disorder of the haem biosynthesis pathway (driven by ALA synthase / porphobilinogen deaminase activity), and there is no established pharmacological pathway connecting H1-receptor antagonism to haem metabolism. If anything, some antihistamines are handled cautiously in porphyria because of hepatic metabolic load, which represents a potential precipitating risk rather than a therapeutic rationale.

Because the original MOA record is a data gap, this mechanistic link cannot be independently verified. It is also notable that Mizolastine's other top nine TxGNN predictions in this pack cluster heavily around movement/tic disorders (e.g. psychogenic movement disorders, tardive-type dyskinesia, chronic tic disorder, extrapyramidal disease) with similarly weak or absent mechanistic support — a pattern consistent with a knowledge-graph embedding artefact (disease-ontology or shared-node clustering) rather than a genuine drug–disease biological signal. This context should temper confidence in the acute-intermittent-porphyria prediction specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: formal TFDA/MHRA warning and contraindication data for Mizolastine could not be retrieved for this evidence pack (Blocking-severity data gap) and safety review has not progressed past initial screening. Given the predicted indication is a porphyria-related condition, any future evaluation should specifically check the drug's classification in the **Drugs Database for Acute Porphyria** (Welsh Medicines Information Centre / European Porphyria Network), as inappropriate drug exposure can precipitate acute attacks in this patient group.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported by TxGNN model output alone (Evidence Level L5, decision stage S0) — there are no clinical trials, no literature, and no verified mechanistic pathway linking H1-antihistamine activity to acute intermittent porphyria.
- Mizolastine currently has no UK marketing authorisation on record, and core safety data (SmPC warnings/contraindications) needed for even a preliminary safety screen is missing (Blocking-severity data gap).

**To proceed, the following is needed:**
- Confirmed mechanism of action data for Mizolastine (High-severity data gap, DG002)
- TFDA/MHRA-sourced SmPC warnings and contraindications to enable a baseline safety assessment (Blocking-severity data gap, DG001)
- Confirmation of Mizolastine's status in the Drugs Database for Acute Porphyria before any porphyria-related use is considered
- Preclinical or mechanistic studies specifically probing any relationship between H1-receptor antagonism and haem biosynthesis, to test whether this prediction reflects a real biological signal or a knowledge-graph artefact
- Ongoing monitoring for any emerging clinical trial or literature evidence, given none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

