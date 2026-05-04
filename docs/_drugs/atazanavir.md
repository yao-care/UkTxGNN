---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 6
---

# Atazanavir
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

# Atazanavir: From HIV-1 Infection to AIDS-Related Complex

> **Clinical Focus Note:** The TxGNN model's two highest-ranked predictions for Atazanavir are simian immunodeficiency virus infection (SIV, rank 1, 99.98%) and feline acquired immunodeficiency syndrome (rank 2, 99.98%). Both are animal diseases without direct human clinical applicability; the high scores arise from the structural homology between HIV-1 and lentiviral proteases within the knowledge graph. This report therefore focusses on the highest-ranking **human disease** prediction with actionable clinical evidence: **AIDS-Related Complex** (rank 5, 99.71%, evidence level L1). A secondary actionable finding — congenital HIV infection (rank 6, L1) — is addressed in the Conclusion and Next Steps.

---

## One-Sentence Summary

Atazanavir (Reyataz) is an HIV-1 protease inhibitor internationally approved for the treatment of HIV-1 infection in adults and paediatric patients, though it currently holds no MHRA marketing authorisation in the United Kingdom.
The TxGNN model predicts it may be effective for **AIDS-Related Complex (ARC)** — the symptomatic pre-AIDS stage of HIV disease characterised by progressive immune dysfunction — supported by **2 completed Phase 3 clinical trials** directly studying Atazanavir and **3 published studies**.
Evidence is rated **L1**, the highest category in this evaluation framework.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (internationally approved; no current MHRA authorisation in the UK) |
| Predicted New Indication | AIDS-Related Complex (ARC) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| UK Market Status | Not currently marketed |
| Number of MHRA Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available from the current evidence pack. Based on known information, Atazanavir is an azapeptide HIV-1 protease inhibitor. It selectively binds to the catalytic site of the HIV-1 aspartyl protease, preventing post-translational cleavage of the Gag-Pol polyprotein precursor into the structural proteins and enzymes — reverse transcriptase, integrase, and protease itself — required to assemble mature, infectious viral particles. The resulting virions are morphologically aberrant and non-infectious. Atazanavir is typically administered as a pharmacokinetically boosted regimen with ritonavir (ATV/r, 300/100 mg once daily) or cobicistat, both of which inhibit CYP3A4-mediated catabolism to maintain therapeutic plasma drug concentrations.

AIDS-Related Complex (ARC) represents the clinical phase of HIV-1 infection that precedes the development of an AIDS-defining illness, characterised by CD4⁺ T-cell counts of approximately 200–500 cells/μL, persistent constitutional symptoms (fever, night sweats, weight loss, lymphadenopathy), and progressive immune dysfunction. Since Atazanavir directly targets HIV-1 replication at the protease cleavage step, its mechanism is applicable across all stages of active HIV-1 disease — the same viral enzyme exists whether a patient is in primary infection, the ARC phase, or late-stage AIDS. Suppressing plasma viraemia arrests disease progression and facilitates CD4 cell recovery, thereby preventing advancement from ARC to AIDS-defining illness.

The mechanistic link is therefore direct and well-established: this prediction reflects the drug's core pharmacological action applied to a recognised, distinct pre-AIDS disease stage rather than an entirely novel molecular target. The clinical evidence is correspondingly strong. The Phase 3 trial NCT00035932 (n=571) compared Atazanavir-based regimens against lopinavir/ritonavir in treatment-experienced HIV patients, while the PRINCE I study (NCT01099579, n=82) extended evidence into paediatric populations. The TxGNN score of 99.71% reflects the tight topological proximity of ARC and HIV nodes within the knowledge graph, and in this instance is fully supported by mechanistic biology and clinical data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | Atazanavir + ritonavir or saquinavir vs Lopinavir/ritonavir, each with tenofovir and a nucleoside, in treatment-experienced HIV patients; evaluated viral load suppression as the primary endpoint |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I: Atazanavir powder + ritonavir in HIV-infected children ≥3 months to <6 years; assessed safety, tolerability, efficacy, and pharmacokinetics in a paediatric HIV population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Retrospective Cohort | J Acquir Immune Defic Syndr | Assessed differential effects of commonly prescribed cART regimens — including Atazanavir-containing regimens — on the incidence of AIDS-defining neurological conditions in a large HIV-positive cohort |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort / Safety Analysis | AIDS Reviews | Analysed risk factors for gastrointestinal adverse events in HIV-treated and untreated patients; identified complex interaction between HIV disease stage and protease inhibitor-based ART including ATV regimens |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | In vitro / Medicinal Chemistry | Antimicrob Agents Chemother | Characterised novel CNS-targeting HIV-1 protease inhibitors with enhanced blood–brain barrier penetration against highly drug-resistant strains; provides mechanistic context for protease inhibitor utility in HIV-associated neurocognitive disorders |

---

## UK Market Information

Atazanavir currently holds **no MHRA marketing authorisation** in the United Kingdom and is not available through normal NHS pharmaceutical supply channels.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| No current MHRA authorisation | — | — | — |

> **Access in the UK:** Reyataz (atazanavir) previously held EMA centralised marketing authorisation across the EU/EEA, and EMA product information (including the current SmPC) remains accessible via the EMA website. Following Brexit, UK access requires either an MHRA Specials licence (unlicensed importation) or a named-patient supply arrangement. Prescribers should consult the BNF (atazanavir monograph, Antivirals — HIV section) and the current **BHIVA Treatment Guidelines** for recommended ART regimens. Relevant NICE Technology Appraisals for HIV should also be reviewed for commissioning guidance.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atazanavir has a robust L1 evidence base for HIV/ARC management, with multiple completed Phase 3 trials directly studying the drug and demonstrating virological efficacy; the principal barriers to UK use are regulatory in nature — the absence of an MHRA marketing authorisation requires an unlicensed medicines access pathway before clinical use can proceed.

**To proceed, the following is needed:**

- Confirmation of the appropriate MHRA unlicensed access route (Specials licence or named-patient importation) with sign-off from the responsible prescriber and hospital pharmacy
- Full review of the most recent EMA SmPC for Reyataz (including contraindications, warnings, and drug-drug interaction profile), and cross-referencing with the BNF atazanavir monograph
- Specialist HIV physician and clinical pharmacist involvement prior to initiation, particularly for CYP3A4/P-glycoprotein DDI assessment (notably: acid-reducing agents impair ATV absorption; concurrent rifampicin is contraindicated)
- Baseline and ongoing monitoring plan: CD4 count, HIV-1 RNA (viral load), FBC with differential, liver function tests, serum bilirubin, renal function (eGFR, urinalysis for renal stones), fasting lipid profile, and ECG (PR interval — especially with concomitant drugs prolonging cardiac conduction)
- **Secondary actionable finding — Congenital HIV infection (TxGNN rank 6, 99.71%, L1):** Atazanavir has a specific evidence base for use in pregnancy for prevention of mother-to-child transmission (PMTCT) and in paediatric HIV treatment, supported by the PRINCE I (NCT01099579, n=82) and PRINCE II (NCT01335698, n=160) Phase 3 studies, dedicated pharmacokinetic data in pregnant women (NCT00326716), and transplacental transfer studies confirming ATV crosses the placenta (umbilical cord/maternal plasma ratio ≈0.13–0.30). UK clinicians managing pregnant HIV-positive women should additionally consult the **BHIVA Guidelines for the Management of HIV in Pregnancy and Postpartum** and liaise with regional PMTCT specialist services.

---

*This report is intended for research and evaluation purposes only and does not constitute clinical or prescribing advice. Drug repurposing candidates require formal clinical validation before any change to patient management. All use of unlicensed medicines must comply with MHRA regulations and local NHS governance frameworks.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

