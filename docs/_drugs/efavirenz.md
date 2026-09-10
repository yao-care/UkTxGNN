---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Efavirenz: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for human HIV-1 infection. The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, not human, condition — supported by **2 clinical trials** and **1 publication**, but neither trial actually studies efavirenz or FIV, and the supporting literature is graded as low relevance (Grade C). This candidate should be read as a low-confidence model artefact rather than a credible repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — established from literature context in this pack; not confirmed via a structured regulatory field, as no UK/local licences are recorded |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (a veterinary indication, not a human disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, efavirenz is an NNRTI that binds directly to the HIV-1 reverse transcriptase enzyme, blocking viral replication; this is well documented across the literature entries returned for this drug (e.g. its use in the ATRIPLA combination and in RT-SHIV primate models), even though the structured `original_moa` field is empty here.

The TxGNN model's rank-1 prediction — Feline Acquired Immunodeficiency Syndrome — is mechanistically weak. FIV is caused by a lentivirus related to, but structurally distinct from, HIV-1. The single supporting publication (PMID 38031646) is a biochemical/structural comparison study concluding that NNRTIs developed against HIV-1 reverse transcriptase generally show **reduced cross-species activity** against FIV reverse transcriptase, precisely because the two enzymes are not sufficiently homologous. The two "supporting" clinical trials do not strengthen the case: both investigate dolutegravir (an integrase inhibitor, not efavirenz) in human HIV-1 populations, and were graded "C" for relevance due to drug and species mismatch.

**A note on the other candidates in this pack:** the rank-2 prediction, Simian Immunodeficiency Virus infection, has a considerably more direct mechanistic basis — efavirenz has been used experimentally in RT-SHIV macaque models where the SIV reverse transcriptase is replaced with the actual HIV-1 enzyme, so the drug's known pharmacology applies directly. It carries more literature (16 records) and a higher evidence level (L3, decision stage S1) than the rank-1 candidate, though it remains a non-human research model rather than a human clinical indication. The rank-3 candidate (a rare neurodevelopmental disorder) has no supporting trials or literature at all (L5, Hold) and no plausible mechanistic link. Taken together, none of the three top predictions currently support a human clinical repurposing pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study for dolutegravir (GSK1349572) in ART-naïve human HIV-1 patients; does not involve efavirenz or FIV (relevance graded C) |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Compared dolutegravir plus abacavir/lamivudine against Atripla (which contains efavirenz) in human HIV-1 patients; efavirenz appears only as part of the comparator arm, not as the studied drug for this indication (relevance graded C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Cohort (biochemical/structural comparison) | Journal of Veterinary Science | Compared NNRTIs (nevirapine, efavirenz, rilpivirine) against feline and human immunodeficiency virus reverse transcriptase; found no effective treatment yet established for FIV and indicates limited cross-species NNRTI activity |

---

## UK Market Information

No UK marketing authorisations are currently recorded for this candidate (0 licences on file; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (FIV) is a veterinary indication with a mechanistically weak basis — the one supporting publication itself concludes that HIV-1-targeted NNRTIs have limited cross-species activity against FIV reverse transcriptase, and neither cited clinical trial actually studies efavirenz or FIV. There is no human clinical evidence pathway here, and the drug has no active UK marketing authorisation on file.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent label warnings and contraindications (currently a blocking data gap)
- A confirmed mechanism-of-action record from DrugBank (currently a high-severity data gap)
- If a human indication is to be pursued, re-evaluation should focus on the rank-2 candidate (SIV infection / RT-SHIV models), which has a more direct pharmacological rationale, though it would still require translation from a non-human primate research model to any human clinical hypothesis
- Independent confirmation of efavirenz's original human indication and licensing status, since the structured regulatory fields in this pack are empty
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

