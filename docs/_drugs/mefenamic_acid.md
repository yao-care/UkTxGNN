---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Mefenamic Acid: From Pain and Inflammation to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class NSAID pharmacologically established for pain and inflammatory conditions through COX-1/COX-2 inhibition, though its formal regulatory indication text is not present in this evidence pack. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 registered clinical trials** but **20 supporting publications**, including several historical randomised controlled trials directly evaluating mefenamic acid in RA patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap); pharmacologically classified as an analgesic/anti-inflammatory NSAID (fenamate class) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information from the evidence pack, mefenamic acid is a fenamate-class non-steroidal anti-inflammatory drug (NSAID), a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis, producing analgesic and anti-inflammatory effects. Its efficacy in pain and inflammatory conditions is well established in the pharmacological literature, and this mechanism maps directly onto the pathology of rheumatoid arthritis, which is driven by prostaglandin-mediated joint inflammation.

Because RA is fundamentally an inflammatory joint disease, a COX inhibitor with proven anti-inflammatory and analgesic activity is mechanistically well suited to symptomatic RA management. This is reinforced by multiple historical double-blind trials (1966–1979) directly comparing mefenamic acid against other NSAIDs (ibuprofen, sulindac, flurbiprofen, aspirin, phenylbutazone) in RA patients, several of which report comparable efficacy for pain, joint tenderness, and morning stiffness. This body of older but consistent clinical evidence supports the biological plausibility of the TxGNN prediction, even though no modern registered clinical trials exist for this specific drug-indication pairing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT | Current Medical Research and Opinion | Double-blind crossover trial (n=24): mefenamic acid, flurbiprofen and sulindac all significantly superior to placebo for pain score, joint tenderness, and morning stiffness in RA |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | J Int Med Res | Randomised double-blind within-patient study (n=40): mefenamic acid and ibuprofen showed comparable analgesic/anti-inflammatory effect in RA, with similar mild side-effect profile |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT | The Medical Journal of Australia | Double-blind crossover trial: mefenamic acid (1500mg/day) compared favourably with ibuprofen (1200mg/day) in RA; side effects mild, mainly gastrointestinal |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Cohort/Clinical Study | Annals of the Rheumatic Diseases | Early clinical study establishing mefenamic acid's use in rheumatoid arthritis |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Review of the clinical place of mefenamic acid in RA treatment |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | Clinical Study | British Medical Journal | Mefenamic acid and flufenamic acid compared with aspirin and phenylbutazone in rheumatoid arthritis |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | Clinical Study | Annals of the Rheumatic Diseases | Assessment of drugs in RA outpatients; comparison of mefenamic and flufenamic acids with phenylbutazone and aspirin |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Clinical Study | The Journal of Rheumatology | Evaluation of analgesic action across 10 antirheumatic drugs in 684 RA patients using a validated pain-charting method |
| [29548675](https://pubmed.ncbi.nlm.nih.gov/29548675/) | 2018 | Observational (Case-crossover) | The American Journal of Cardiology | Cardiovascular safety signal: evaluated stroke/MI risk with non-selective NSAIDs (incl. mefenamic acid) in RA patients (n=5,921) |
| [23611159](https://pubmed.ncbi.nlm.nih.gov/23611159/) | 2014 | Formulation Study | Pharmaceutical Development and Technology | Development of a time-controlled triple-concentric release mefenamic acid tablet formulation targeted at RA |

---

## UK Market Information

Mefenamic acid is currently **not marketed** in the UK according to this evidence pack, with **0 marketing authorisations** on record. No licensed product information is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: TFDA/MHRA-equivalent warning and contraindication data for this drug is currently a **Blocking** data gap, meaning a full safety (S1) evaluation cannot yet be completed.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical double-blind RCTs (1966–1979) support mefenamic acid's efficacy in rheumatoid arthritis, and the COX-inhibition mechanism is directly relevant to RA's inflammatory pathology (Evidence Level L2). However, the drug currently has no UK marketing authorisation and lacks formal safety labelling data, so guardrails are required before any clinical progression.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data via DrugBank query (currently a High-severity data gap)
- Assessment of UK licensing pathway, given zero current marketing authorisations
- Modern comparator trial data, as existing RA evidence predates current NSAID cardiovascular/GI safety standards (most trials are 1966–1979)
- Review of the 2018 cardiovascular safety signal (PMID 29548675) alongside any RA-specific cardiovascular risk-benefit assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

