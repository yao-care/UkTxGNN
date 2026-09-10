---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) established internationally as an antiretroviral for HIV-1 infection, most often as part of fixed-dose combinations such as Truvada and Descovy. The TxGNN model's top prediction points to **Simian Immunodeficiency Virus (SIV) Infection**, an animal (macaque) disease model rather than a human indication, supported by **2 clinical trials** (both graded low relevance) and **20 publications** (mostly non-human primate PrEP/pathogenesis studies). This evidence pack does not currently support a viable human repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no UK marketing authorisation record); Emtricitabine is internationally established as an NRTI for HIV-1 infection |
| Predicted New Indication | Simian Immunodeficiency Virus Infection (animal/macaque disease model) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data was not available in this evidence pack (flagged as a data gap). Based on established pharmacological knowledge, Emtricitabine is a cytidine nucleoside analogue that inhibits HIV reverse transcriptase, and it is typically co-formulated with tenofovir as part of antiretroviral treatment or pre-exposure prophylaxis (PrEP) regimens for HIV-1.

The mechanistic rationale for the TxGNN prediction is that SIV, like HIV, is a lentivirus with a highly homologous reverse transcriptase, so a reverse-transcriptase inhibitor active against HIV would plausibly also inhibit SIV replication. Indeed, emtricitabine/tenofovir combinations are already the standard antiretroviral regimen used in macaque SIV/SHIV challenge studies.

However, this mechanistic plausibility does not translate into a genuine human repurposing opportunity: SIV infection is a disease of non-human primates used as a laboratory model for HIV research, not a condition that occurs in human patients. The second-ranked prediction (feline immunodeficiency virus, FIV) is similarly a veterinary indication in cats, with only weak, indirect evidence for efficacy against the FIV reverse transcriptase. The third-ranked prediction (a rare inherited neurodevelopmental disorder) has no supporting clinical trials or literature and no identifiable biological link to an NRTI mechanism — this is most likely a false positive arising from proximity in the model's embedding space rather than a real signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn (enrolment 0) | 0 | Study of HIV decay kinetics with raltegravir in humans, referencing comparable SIV decay kinetics in macaques; not an emtricitabine intervention study and did not enrol any participants. |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab combined with antiretroviral therapy in HIV-infected humans aiming at virological remission; emtricitabine is not the primary intervention and the trial does not involve SIV. |

Both trials were flagged as low relevance (Grade C) — they were retrieved on keyword overlap ("immunodeficiency virus") rather than genuine relevance to emtricitabine as a treatment for SIV infection. No trial in this evidence pack directly tests emtricitabine against SIV or any equivalent human indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT (human, systemic PrEP) | Pharmacotherapy | Review/RCT evidence on systemic pre-exposure prophylaxis for HIV infection in humans, underpinning the PrEP rationale later tested in animal SIV/SHIV models. |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | RCT (human PrEP) | J Infect Dis | Oral tenofovir alafenamide/emtricitabine combination evaluated against vaginal SHIV infection in macaques, informing human PrEP regimen design. |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal model (macaque) | Nature Communications | Emtricitabine/tenofovir alafenamide plus long-acting cabotegravir/rilpivirine tested for SHIV remission in macaques with early treatment initiation. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal model (macaque) | J Infect Dis | Oral emtricitabine/tenofovir alafenamide chemoprophylaxis protected macaques from rectal SHIV infection. |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal model (macaque) | J Infect Dis | Emtricitabine/tenofovir disoproxil fumarate prevented vaginal SHIV infection in macaques co-infected with Chlamydia and Trichomonas. |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal model (macaque) | J Infect Dis | Oral emtricitabine/tenofovir disoproxil fumarate protected macaques against a tenofovir-resistant (K65R) SHIV strain. |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Animal model (SIV dynamics) | J Virology | Antiretroviral therapy including emtricitabine and tenofovir used to study SIVagm dynamics in African green monkeys. |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Animal model (SIV virology) | J Virology | Emtricitabine (and lamivudine) therapy in SIV-infected macaques led to emergence of the M184V resistance mutation, mirroring human HIV resistance patterns. |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Animal/ex vivo (rectal challenge) | J Infect Dis | Vaginally administered emtricitabine/tenofovir gel evaluated against repeated rectal SHIV exposure in macaques. |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal model (vaccine + PrEP) | AIDS Res Hum Retroviruses | Combined HIV vaccine and partially protective oral PrEP (including emtricitabine) prevented SHIV infection in macaques. |

All identified literature relates to animal (macaque) models of SIV/SHIV used as HIV research surrogates, or to human PrEP studies for HIV-1 itself — none constitutes clinical evidence of emtricitabine efficacy in a human disease population corresponding to SIV infection.

---

## UK Market Information

No marketing authorisation is recorded in this evidence pack (market status: Not marketed; 0 licenses on file). Emtricitabine is internationally marketed as part of combination antiretroviral products (e.g., Truvada, Descovy, Atripla); confirmation of current UK/MHRA licensing status should be obtained directly from the MHRA product register and the BNF before any further evaluation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- None of the three top TxGNN-predicted indications constitutes a valid human repurposing target: SIV infection and feline immunodeficiency syndrome are animal/veterinary disease models rather than human conditions, and the third prediction (a rare neurodevelopmental disorder) has no supporting evidence or plausible mechanistic link, indicating a likely false positive.
- The associated clinical trial evidence is either graded as irrelevant (keyword mismatch) or drawn from non-human primate research, and no direct human clinical evidence supports a genuinely new indication.

**To proceed, the following is needed:**
- Resolve the Blocking data gap (DG001): TFDA/MHRA product label warnings and contraindications, required before any safety pre-screening (S1) can begin.
- Resolve the High-severity data gap (DG002): confirmed mechanism-of-action data from DrugBank to properly assess mechanistic relevance of any future candidate indication.
- Re-run or filter the TxGNN prediction set to exclude non-human disease ontology terms, and review lower-ranked candidates for genuine human-relevant indications.
- Confirm current UK marketing authorisation status directly with the MHRA, since this evidence pack shows no licences on file.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

