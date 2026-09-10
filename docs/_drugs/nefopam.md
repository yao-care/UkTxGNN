---
layout: default
title: Nefopam
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: From Postoperative Pain Management to Lumbar Spinal Stenosis

## One-Sentence Summary

Nefopam is a centrally-acting, non-opioid analgesic that inhibits monoamine (5-HT/NE/DA) reuptake and is established for postoperative pain control. The TxGNN model predicts it may be effective for **Lumbar Spinal Stenosis** (specifically post-surgical dysesthesia and residual pain), with **1 randomised controlled trial** and **2 supporting publications** currently identified.

> **Note on other predictions**: The evidence pack also lists nine higher-ranked candidates (all cataract-related diagnoses, e.g. mature cataract, senile cataract, diabetic cataract). These carry marginally higher TxGNN scores but have **zero supporting clinical trials or literature** and remain in "pending" evaluation status. Given the absence of any corroborating evidence and no obvious mechanistic rationale for an analgesic drug in cataract pathology, this report focuses on **Lumbar Spinal Stenosis (rank 10)**, which is the only candidate with completed scoring, an evidence level assignment, and human-study support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally listed in the regulatory dataset (drug not marketed in the UK); per the model's rationale narrative, Nefopam is known for postoperative pain management |
| Predicted New Indication | Lumbar Spinal Stenosis (postoperative dysesthesia/pain adjunct) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Nefopam is not available in this Evidence Pack (flagged as a **High-severity data gap**, DG002). Based on the information present, Nefopam is a centrally-acting non-opioid analgesic that inhibits monoamine (serotonin, noradrenaline and dopamine) reuptake, and it is already used clinically for postoperative pain management and as an adjunct in neuropathic pain.

Patients undergoing surgery for lumbar spinal stenosis frequently experience postoperative dysesthesia and residual radicular pain. The proposed mechanistic link — central analgesic and anti-dysesthesia activity via monoamine modulation — is biologically plausible for this population, and this is not a prediction based on the TxGNN score alone: a double-blind RCT has already tested Nefopam specifically in this patient group and found a benefit on postoperative pain, dysesthesia and satisfaction.

However, the same evidence base flags an important safety signal: a case report describes status epilepticus attributed to Nefopam in a patient undergoing lumbar spinal stenosis surgery. This means the mechanistic rationale is credible, but any progression of this candidate must explicitly account for seizure risk, particularly in patients with a seizure history or concurrent use of other pro-convulsant agents.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no entries in `clinical_trials` or `ictrp_trials` for this indication; supporting evidence is limited to the peer-reviewed literature below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | RCT | Journal of Clinical Medicine | Double-blind RCT (n=73) of nefopam 20 mg vs. saline in lumbar spinal stenosis surgery patients; assessed effect on dysesthesia, postoperative pain and patient satisfaction |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | RCT | Zhurnal Voprosy Neirokhirurgii imeni N. N. Burdenko | Evaluated various multimodal perioperative analgesia regimens (including nefopam) in spinal stenosis surgery and their effect on failed back surgery syndrome rates |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Case Report | Journal of Korean Neurosurgical Society | Reports status epilepticus in a 71-year-old man following nefopam administration for postoperative analgesia after lumbar spinal stenosis surgery — important seizure-risk safety signal |

---

## UK Market Information

Nefopam currently holds **no MHRA marketing authorisations** and is recorded as **not marketed** in the UK (0 licenses on file). No BNF classification entry is available for this product in the current dataset.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> Note: while formal `safety.key_warnings` and `safety.contraindications` data are not yet available in this dataset (flagged as a **Blocking data gap**, DG001), the literature review above independently surfaced a seizure/status epilepticus signal associated with Nefopam that should be treated as a priority item for any future safety assessment, particularly given the elderly, post-neurosurgical target population.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One RCT and two supporting publications provide L2-level evidence for a mechanistically plausible use of Nefopam in lumbar spinal stenosis postoperative pain and dysesthesia. However, the drug is not currently marketed in the UK, mechanism-of-action data is missing, and a credible seizure-risk signal exists in the same patient population — together these warrant guardrails rather than unrestricted progression.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain formal UK/MHRA SmPC warnings, contraindications and prescribing information
- Resolve DG002 (High): confirm detailed mechanism of action from DrugBank or equivalent source
- Formal seizure-risk assessment and exclusion criteria (seizure history, concurrent pro-convulsant medication) before any clinical use in this indication
- Route-of-administration and dosage-form compatibility assessment (currently "pending" in the source data)
- Clarification of UK regulatory pathway, given the drug currently holds no marketing authorisation in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

