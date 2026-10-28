---
layout: default
title: Tolfenamic Acid
parent: Model Prediction Only (L5)
nav_order: 626
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Tolfenamic Acid: predicted new indication Headache disorder (evidence level L5). Approved use: Acute migraine"
monitor_inn: "Tolfenamic acid"
predicted_indications: ["headache disorder", "tendinitis", "rheumatoid arthritis", "trigeminal autonomic cephalalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "fibromyalgia", "exostosis", "inclusion body myositis"]
---

# Tolfenamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tolfenamic Acid: From Migraine to Headache Disorder
{: .text-alpha }

## One-Sentence Summary

Tolfenamic acid is a fenamate NSAID (non-steroidal anti-inflammatory drug) that is already used in the UK for acute migraine.
The TxGNN model predicts it may be effective for **headache disorder**, with **no registered clinical trials** but **20 publications** (mostly migraine studies from 1979 to 2004) supporting this direction.
This prediction largely overlaps with the existing migraine use, so it is not a true repurposing finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine (the licence record compiled for this report has no indication text; the migraine indication comes from pharmacology reference data) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 (several randomised double-blind studies, but none are registered Phase 3 trials; based on titles and abstracts only) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, tolfenamic acid is a potent inhibitor of prostaglandin biosynthesis through cyclooxygenase inhibition, and it has also been reported to affect leukotriene pathways. Prostaglandins sensitise nociceptors and are involved in vasodilatation, oedema and platelet aggregation, all of which are thought to contribute to migraine attacks. The pharmacology data also list AKR1C3 as a human target.

The predicted "headache disorder" is a broad category that includes migraine, where tolfenamic acid is already used. The randomised studies cited below support its use in both acute attacks and prophylaxis. Its relevance to other headache types, such as trigeminal autonomic cephalalgias, is not supported by direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. Most of the studies pre-date trial registry requirements, so the published literature below is the main source of evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT | Acta Neurol Scand | Double-blind crossover comparison of tolfenamic acid (200 mg and 400 mg) with paracetamol in common migraine |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT | Acta Neurol Scand | Prophylaxis: tolfenamic acid and propranolol both significantly reduced attacks versus placebo |
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT | Cephalalgia | Tolfenamic acid with caffeine or metoclopramide in migraine attacks |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | Randomised controlled trial | Headache | Rapid-release tolfenamic acid had a comparable effect to oral sumatriptan in acute migraine (141 patients) |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | Randomised controlled trial | Medicina (Kaunas) | Prophylaxis: tolfenamic acid 300 mg versus pizotifen in 192 patients |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | Randomised crossover trial | Acta Neurol Scand | Tolfenamic acid versus propranolol for prophylaxis in 76 patients; both drugs were effective |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | Randomised crossover trial | Lancet | As effective as ergotamine during migraine attacks, with less nausea |
| [7051739](https://pubmed.ncbi.nlm.nih.gov/7051739/) | 1982 | Randomised crossover trial | Acta Neurol Scand | Prophylaxis: significantly better than placebo for attack number, duration and severity |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacol Toxicol | Review of tolfenamic acid in acute and prophylactic treatment of migraine |
| [10234467](https://pubmed.ncbi.nlm.nih.gov/10234467/) | 1999 | Retrospective study | Cephalalgia | Adding tolfenamic acid to sumatriptan reduced migraine recurrence |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407041U0AAABAB (BNF code) | Tolfenamic Acid tablets 200 mg | Tablet | Not stated in the data compiled; reference data describe UK approval for acute migraine |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry, which lists AKR1C3 as a human target of tolfenamic acid. No clinically graded drug-drug interactions were identified in the data compiled.
- Tolfenamic acid can delay absorption during a migraine attack. In one small study, rectal metoclopramide did not change this.
- Tolfenamic acid carries the usual NSAID class cautions, such as gastrointestinal, cardiovascular and renal risks. One rheumatoid arthritis study reported serious side-effects including leukopenia.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomised, double-blind studies support tolfenamic acid for acute and prophylactic migraine treatment, and the drug is already marketed in the UK. However, the evidence is old, unregistered and based on abstracts, and the prediction mostly restates an existing use rather than a new one.

**To proceed, the following is needed:**
- Full-text review of the key randomised studies to confirm the findings
- The licensed indication wording and the SmPC warnings and contraindications for the UK product
- Mechanism of action data
- Clarification of which non-migraine headache types (if any) are of interest, since no direct evidence exists for trigeminal autonomic cephalalgias

---

## Other Predicted Indications (Brief Note)

- **Rheumatoid arthritis** (score 0.9970): The literature includes randomised double-blind comparisons against phenylbutazone, aspirin and ibuprofen, showing symptomatic benefit rather than disease modification. This is an established NSAID-type use rather than a novel finding (Proceed with Guardrails).
- **Tendinitis, trigeminal autonomic cephalalgia, myositis fibrosa, idiopathic granulomatous myositis, fibromyalgia, exostosis, inclusion body myositis and osteoarthritis susceptibility**: Model prediction only, with no trials or literature in the data compiled (Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

