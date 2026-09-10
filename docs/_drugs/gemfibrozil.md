---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidaemia to Rheumatoid Arthritis

## One-Sentence Summary

> Gemfibrozil is a fibrate-class PPAR-α agonist historically used to manage hypertriglyceridaemia and mixed dyslipidaemia. TxGNN's top-ranked prediction flags **Rheumatoid Arthritis** as a candidate new indication (score 99.90%), but the supporting literature is indirect (based on a related fibrate, not gemfibrozil itself) and no trials exist. Two other candidates in this evidence pack — **HIV-associated dyslipidaemia** and **hypoalphalipoproteinemia** — are far better supported, with multiple RCTs testing gemfibrozil directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidaemia / hypertriglyceridaemia (fibrate class) — no formal UK licence text on file |
| Predicted New Indication | Rheumatoid Arthritis (top-ranked TxGNN candidate) |
| TxGNN Prediction Score | 99.90% (rank 1,520) |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (Research Question stage) |

**Note:** This evidence pack scores 10 candidate indications for gemfibrozil. Because signal quality varies enormously between them, the table above reflects the top-ranked candidate only — see the portfolio view below before drawing conclusions.

### Portfolio of All Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Rheumatoid arthritis | 99.90% | L4 | S1 | Research Question |
| 2 | Multiple endocrine neoplasia | 99.83% | L5 | S0 | Hold |
| 3 | HIV infectious disease *(HIV-associated dyslipidaemia)* | 99.80% | L2 | S2 | Proceed with Guardrails |
| 4 | Hypoalphalipoproteinemia | 99.77% | L2 | S3 | Proceed with Guardrails |
| 5 | Brachydactyly-syndactyly syndrome | 99.77% | L5 | S0 | Hold |
| 6 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.77% | L5 | S0 | Hold |
| 7 | Methemoglobinemia, alpha type | 99.76% | L5 | S0 | Hold |
| 8 | Obsolete familial combined hyperlipidemia | 99.71% | L5 | S0 | Hold |
| 9 | Sclerosing cholangitis | 99.70% | L4 | S1 | Research Question |
| 10 | Methemoglobin reductase deficiency | 99.70% | L5 | S0 | Hold |

Six of the ten candidates (ranks 2, 5, 6, 7, 8, 10) have **no supporting trials or literature at all** and are flagged in the underlying rationale as likely knowledge-graph noise — these are rare genetic/developmental syndromes or haematological enzyme disorders with no plausible link to a PPAR-α agonist. They are not discussed further below.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gemfibrozil is not recorded in this evidence pack as a standalone field, but the underlying pharmacology is consistent and recoverable from the rationale attached to each candidate: gemfibrozil is a **PPAR-α agonist** that directly upregulates apoA-I/apoA-II transcription (raising HDL) and lowers CETP activity and hepatic triglyceride output — the mechanism behind its established use in dyslipidaemia.

For the top-ranked candidate, **rheumatoid arthritis**, the proposed link is that PPAR-α agonism has a class-level anti-inflammatory effect — potentially via NF-κB suppression and modulation of regulatory T-cell (Foxp3) expression — that could plausibly reduce joint inflammation. However, the strongest supporting paper (PMID 41207105) tested **bezafibrate**, a pan-PPAR agonist, not gemfibrozil, and the remaining literature consists of animal models and a case report. This is a cross-drug (class-effect) inference rather than direct evidence for gemfibrozil.

By contrast, two lower-ranked but mechanistically tighter candidates deserve attention: **hypoalphalipoproteinemia** (low-HDL syndrome) is essentially gemfibrozil's core pharmacology applied to a related lipid disorder, backed by five RCTs; and **HIV-associated dyslipidaemia** (protease-inhibitor-induced hypertriglyceridaemia) is supported by RCTs testing gemfibrozil directly in HIV-positive patients — though this is metabolic-complication management, not treatment of HIV infection itself, and the disease label "HIV infectious disease" should not be read literally.

---

## Clinical Trial Evidence

### Rheumatoid Arthritis
Currently no related clinical trials registered.

### HIV-Associated Dyslipidaemia (listed under "HIV infectious disease")

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00039663](https://clinicaltrials.gov/study/NCT00039663) | Phase 1 | Completed | 75 | Assessed endothelial dysfunction as a cardiovascular risk factor in HIV patients on HAART; not a gemfibrozil efficacy trial |
| [NCT00474201](https://clinicaltrials.gov/study/NCT00474201) | N/A | Completed | 15 | PK interaction study: lopinavir/ritonavir lowers gemfibrozil blood levels in healthy volunteers, relevant to co-administration safety |
| [NCT01148004](https://clinicaltrials.gov/study/NCT01148004) | Phase 1 | Completed | 25 | PK interaction of ritonavir/lopinavir with fenofibric acid (same fibrate class, not gemfibrozil directly) |

### Hypoalphalipoproteinemia / Sclerosing Cholangitis
Currently no related clinical trials registered.

---

## Literature Evidence

### Rheumatoid Arthritis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal Study | Modern Rheumatology | Gemfibrozil + reduced-dose prednisolone matched full-dose steroid efficacy in a rat adjuvant-induced arthritis model |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Animal Study | International Immunopharmacology | Bezafibrate (pan-PPAR agonist, not gemfibrozil) attenuated experimental RA via PPAR-γ-dependent anti-inflammatory pathways |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Animal Study | Journal of Immunology | Nitric-oxide-mediated Foxp3 regulation in autoimmune models; mechanistic, not RA-specific |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Case Report | American Journal of Clinical Dermatology | Review of palmar erythema aetiologies; only tangentially relevant |

### HIV-Associated Dyslipidaemia

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12409741](https://pubmed.ncbi.nlm.nih.gov/12409741/) | 2002 | RCT | AIDS | Randomised double-blind trial of gemfibrozil for protease-inhibitor-associated hypertriglyceridaemia |
| [14640387](https://pubmed.ncbi.nlm.nih.gov/14640387/) | 2003 | RCT | Antiviral Therapy | RCT of metformin vs gemfibrozil for lipodystrophy in HIV patients on protease inhibitors |
| [23892238](https://pubmed.ncbi.nlm.nih.gov/23892238/) | 2013 | Cohort | J Acquired Immune Deficiency Syndromes | Compared fish oil, fenofibrate, gemfibrozil and atorvastatin for lowering triglycerides in HIV patients |
| [30526249](https://pubmed.ncbi.nlm.nih.gov/30526249/) | 2018 | Cohort | J American Heart Association | Trends in statin use, including contraindicated statin use, in HIV patients on ART |
| [19258558](https://pubmed.ncbi.nlm.nih.gov/19258558/) | 2009 | Cohort | Annals of Internal Medicine | Compared lipid-lowering drug response in patients with and without HIV infection |
| [14727985](https://pubmed.ncbi.nlm.nih.gov/14727985/) | 2002 | Review | American Journal of Cardiovascular Drugs | Management review of protease-inhibitor-associated hyperlipidaemia |
| [10826894](https://pubmed.ncbi.nlm.nih.gov/10826894/) | 2000 | Review | Scandinavian Journal of Infectious Diseases | Pathophysiology, prevalence and treatment of PI-associated hyperlipidaemia |
| [15535403](https://pubmed.ncbi.nlm.nih.gov/15535403/) | 2004 | Review | Antiviral Therapy | Management of dyslipidaemia in HIV patients on antiretroviral therapy |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | Review | AIDS | Role of statins and fibrates in HAART-associated hyperlipidaemia |
| [10758016](https://pubmed.ncbi.nlm.nih.gov/10758016/) | 2000 | Review | The AIDS Reader | Practical management of metabolic complications of HIV therapy, including fibrates |

### Hypoalphalipoproteinemia

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2810673](https://pubmed.ncbi.nlm.nih.gov/2810673/) | 1989 | RCT | JAMA | Crossover trial comparing lovastatin and gemfibrozil in normolipidaemic patients with low HDL |
| [10716466](https://pubmed.ncbi.nlm.nih.gov/10716466/) | 2000 | RCT | Journal of the American College of Cardiology | Randomised crossover study of gemfibrozil, niacin and combination therapy in isolated low-HDL patients |
| [8318063](https://pubmed.ncbi.nlm.nih.gov/8318063/) | 1993 | RCT | Atherosclerosis | Gemfibrozil vs lovastatin effects on postprandial lipoprotein clearance in low-HDL/high-triglyceride syndrome |
| [8267492](https://pubmed.ncbi.nlm.nih.gov/8267492/) | 1994 | RCT | Archives of Internal Medicine | Lipoprotein responses to lovastatin, gemfibrozil and niacin in normolipidaemic low-HDL patients |
| [7942933](https://pubmed.ncbi.nlm.nih.gov/7942933/) | 1994 | RCT | American Journal of Medicine | Niacin effects on fasting/postprandial lipids in normolipidaemic low-HDL patients (comparator context) |
| [8736620](https://pubmed.ncbi.nlm.nih.gov/8736620/) | 1996 | Review | Drugs | Reappraisal of gemfibrozil's pharmacology, including Helsinki Heart Study outcomes |
| [10929256](https://pubmed.ncbi.nlm.nih.gov/10929256/) | 2000 | Review | Der Internist | Review of low HDL-cholesterol management |
| [3887163](https://pubmed.ncbi.nlm.nih.gov/3887163/) | 1985 | Review | New England Journal of Medicine | Pathogenesis and management of lipoprotein disorders |
| [3541525](https://pubmed.ncbi.nlm.nih.gov/3541525/) | 1986 | Case Report | Advances in Experimental Medicine and Biology | Familial hypoalphalipoproteinemia case description |
| [7945562](https://pubmed.ncbi.nlm.nih.gov/7945562/) | 1994 | Case Report | Atherosclerosis | Homozygous Tangier disease and cardiovascular disease (severe low-HDL model) |

### Sclerosing Cholangitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33751787](https://pubmed.ncbi.nlm.nih.gov/33751787/) | 2021 | Review | Liver International | Safety review of off-label fibrate use in cholestatic liver disease |
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Review | Clinical Pharmacokinetics | DDI evaluation for cilofexor (FXR agonist), an unrelated PSC candidate drug — context only |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Data gap flagged as blocking:** TFDA/SmPC-equivalent warnings and contraindications for gemfibrozil are not yet available in this evidence pack, which prevents a formal S1 safety screen for any of the candidates above.

---

## Conclusion and Next Steps

**Decision: Hold** (drug-level, pending resolution of the blocking safety-data gap)

**Rationale:**
- The top-ranked candidate (rheumatoid arthritis) rests on indirect, cross-drug evidence (bezafibrate, not gemfibrozil) plus animal studies only — insufficient to proceed.
- The two mechanistically strongest candidates — hypoalphalipoproteinemia (L2, multiple direct RCTs) and HIV-associated dyslipidaemia (L2, direct RCTs) — would independently warrant "Proceed with Guardrails," but a Blocking data gap (missing safety/contraindication data) prevents any candidate from clearing the S1 safety gate.
- Six of the ten TxGNN candidates have zero supporting evidence and are most likely knowledge-graph noise; they should not be pursued.

**To proceed, the following is needed:**
- Retrieve gemfibrozil's SmPC/BNF warnings, contraindications and DDI profile (DG001, Blocking) — required before any S1 safety evaluation.
- Obtain a formal mechanism-of-action confirmation from DrugBank or equivalent (DG002, High) to properly assess mechanistic plausibility for RA.
- If pursuing hypoalphalipoproteinemia or HIV-associated dyslipidaemia, clarify that the intended indication is the lipid abnormality, not the underlying disease itself, and confirm current UK/NICE positioning given gemfibrozil is not currently marketed in the UK.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

