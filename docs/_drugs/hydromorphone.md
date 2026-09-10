---
layout: default
title: Hydromorphone
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 6
---

# Hydromorphone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Hydromorphone: From Severe Pain Management to Pharyngitis

## One-Sentence Summary

Hydromorphone is a potent opioid analgesic (μ-opioid receptor agonist) used for management of moderate-to-severe pain. The TxGNN model predicts it may be effective for **Pharyngitis**, but the 6 clinical trials returned by the evidence search largely involve different drugs (palifermin, methadone) rather than hydromorphone itself, and no supporting literature was identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (opioid analgesic class use inferred from mechanism notes only) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for hydromorphone is not available in this evidence pack. Based on information within the evidence itself, hydromorphone is a strong μ-opioid receptor agonist providing systemic analgesia; it has no established anti-infective or anti-inflammatory activity.

Pharyngitis is predominantly a viral or bacterial infective/inflammatory condition of the throat. There is no pharmacological pathway by which a systemic opioid analgesic would treat the underlying disease process, only its symptom (pain).

Critically, of the 6 clinical trials returned by the search for this drug–disease pair, only 2 actually involve hydromorphone, and none study hydromorphone as a treatment for pharyngitis — they concern post-tonsillectomy pain control or unrelated conditions (GVHD-associated oral mucositis, foot/ankle surgery anaesthesia). The remaining trials involve palifermin or methadone, not hydromorphone. This pattern suggests the prediction and its associated trial evidence likely arose from a knowledge-graph entity mapping artefact (anatomical overlap with "pharynx"/"throat" terms) rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00189488](https://clinicaltrials.gov/study/NCT00189488) | Phase 2 | Completed | 155 | Palifermin (not hydromorphone) vs placebo for acute GVHD/oral mucositis — drug mismatch, not directly relevant |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Phase 2 | Completed | 66 | Methadone vs fentanyl/hydromorphone for pain after paediatric tonsillectomy — pain control study, not a pharyngitis treatment trial |
| [NCT00109031](https://clinicaltrials.gov/study/NCT00109031) | Phase 3 | Completed | 47 | Palifermin dosing schedule for oral mucositis prevention — drug mismatch, not directly relevant |
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Early Phase 1 | Completed | 189 | RCT of hydromorphone vs fentanyl for pain control after tonsillectomy/adenotonsillectomy in children — involves the target drug but addresses post-surgical pain, not pharyngitis as a disease |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Phase 4 | Recruiting | 440 | Single-dose intraoperative methadone vs fentanyl/hydromorphone for paediatric tonsillectomy pain — drug and indication mismatch |
| [NCT02996591](https://clinicaltrials.gov/study/NCT02996591) | Phase 4 | Completed | 36 | Spinal vs general anaesthesia with nerve blocks for foot and ankle surgery — unrelated to pharyngitis or hydromorphone's proposed use |

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisation is currently recorded for Hydromorphone in this evidence pack (market status: Not marketed; 0 licences on file).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for using hydromorphone in pharyngitis is not plausible (systemic opioid analgesic vs. an infective/inflammatory throat condition), and the clinical trial evidence returned is largely a mismatch — most trials involve different drugs (palifermin, methadone) or unrelated surgical pain indications rather than hydromorphone treating pharyngitis directly. No supporting literature exists. This pattern is consistent with a knowledge-graph mapping artefact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- MHRA-approved product labelling / SmPC data (DG001, blocking) — required before any safety assessment can proceed
- Confirmed mechanism of action data from DrugBank (DG002, high priority)
- A revised, disease-specific literature and trial search to rule out the entity-mapping artefact before further evaluation

**Note:** This evidence pack also contains a considerably stronger repurposing signal elsewhere in the ranked list — hydromorphone for **headache disorder** (rank 5, TxGNN score 99.65%, Evidence Level L2, decision stage S2, "Research Question"), supported by a completed Phase 4 RCT directly comparing hydromorphone to prochlorperazine + diphenhydramine for acute migraine (NCT02389829) and 17 literature records including a 2026 American Headache Society guideline update. Reviewers may wish to prioritise that candidate over pharyngitis for further evaluation, noting that current migraine guidelines position opioids only as a last-resort option due to medication-overuse headache and dependence risk.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

