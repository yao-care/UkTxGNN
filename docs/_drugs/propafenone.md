---
layout: default
title: Propafenone
parent: Moderate Evidence (L3-L4)
nav_order: 486
evidence_level: L3
indication_count: 8
---

# Propafenone
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Propafenone: From Cardiac Arrhythmia to Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)

> **Note on this evidence pack:** This dataset ("multi") screened eight TxGNN-predicted indications for propafenone. The **highest-scoring prediction (manic bipolar affective disorder, 99.80%) is not presented as the headline finding**, because its supporting literature shows the opposite direction of effect — propafenone-induced mania and psychosis, not treatment benefit. Presenting it as a "new indication" would be clinically misleading. Instead, this report leads with **CPVT**, the only candidate in the pack with genuine mechanistic and clinical support. A full screening summary of all eight candidates is provided below for transparency.

## One-Sentence Summary

Propafenone is a Class IC antiarrhythmic, most widely known for treating supraventricular arrhythmias and ventricular tachycardia by blocking cardiac sodium channels. The TxGNN model predicts it may also be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, a rare inherited arrhythmia syndrome, with **no registered clinical trials but 9 supporting publications**, including electrophysiological mechanism studies and a 35-year case report of sustained clinical benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this dataset — propafenone is a Class IC antiarrhythmic; the specific approved indication text is not available in the evidence pack |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| UK Market Status | Not Marketed (per this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, propafenone is a Class IC antiarrhythmic that blocks cardiac sodium channels; it is closely related structurally and functionally to flecainide.

The mechanistic link to CPVT is stronger than for most TxGNN predictions of this kind: multiple in-vitro electrophysiology studies (PMIDs 26121139, 21270101, 21798265) show that Class IC drugs, including propafenone (particularly its R-enantiomer, R-propafenone), directly inhibit the cardiac ryanodine receptor (RyR2) — the calcium-release channel whose mutation causes CPVT — and suppress the arrhythmogenic calcium waves that trigger the disease. This gives propafenone a plausible disease-modifying mechanism beyond simple sodium-channel blockade.

Clinically, this mechanistic rationale is supported by a single but notable case report of 35 years of effective CPVT control with propafenone (PMID 30820400), alongside several cohort studies characterising CPVT's genetics and natural history (PMIDs 35892906, 39564160, 23965883) that establish the disease context but do not directly test propafenone. No randomised controlled trial has been conducted — flecainide remains the better-evidenced Class IC option for CPVT in guidelines, and propafenone's role should be considered adjunctive or second-line pending stronger data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Cohort | Life (Basel) | Systematic review of CPVT clinical characteristics, genetics and arrhythmic outcomes in Chinese patients |
| [39564160](https://pubmed.ncbi.nlm.nih.gov/39564160/) | 2024 | Cohort | Ann Pediatr Cardiol | >10-year follow-up cohort describing long-term clinical course of CPVT |
| [23965883](https://pubmed.ncbi.nlm.nih.gov/23965883/) | 2013 | Cohort | Chin J Contemp Pediatr | Long-term outcomes and predictors of ventricular arrhythmia in CPVT, including drug response |
| [26121139](https://pubmed.ncbi.nlm.nih.gov/26121139/) | 2015 | Basic Science (in vitro) | PLoS One | RyR2 channel activity determines potency of flecainide and R-propafenone against arrhythmogenic Ca²⁺ waves |
| [21270101](https://pubmed.ncbi.nlm.nih.gov/21270101/) | 2011 | Basic Science (in vitro) | Circ Arrhythm Electrophysiol | Inhibition of cardiac RyR2 channels determines efficacy of Class I antiarrhythmics in CPVT |
| [21798265](https://pubmed.ncbi.nlm.nih.gov/21798265/) | 2011 | Basic Science (in vitro) | J Mol Cell Cardiol | Screening of Class I antiarrhythmics (including propafenone) for suppression of Ca²⁺ waves in calsequestrin-deficient myocytes |
| [30820400](https://pubmed.ncbi.nlm.nih.gov/30820400/) | 2019 | Case Report | HeartRhythm Case Rep | 35-year effective treatment of CPVT with propafenone |
| [36082968](https://pubmed.ncbi.nlm.nih.gov/36082968/) | 2023 | Case Report | Clin Exp Pharmacol Physiol | Gain-of-function RyR2 mutation (R1760W) identified in a CPVT patient |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | Delayed diagnosis of CPVT (RYR2 mutation) in a 9-year-old child |

## UK Market Information

No UK marketing authorisation is currently listed in this dataset (0 licenses recorded; market status: Not Marketed). This should be independently verified against the current MHRA product database and BNF before any clinical decision, as propafenone is licensed and marketed for arrhythmia indications in a number of other jurisdictions.

## Safety Considerations

No structured safety data (key warnings, contraindications, drug interactions) were available in this evidence pack.

- **Class-effect caution (from included literature):** Class IC antiarrhythmics, including propafenone, carry a recognised risk of proarrhythmia and conduction slowing (QRS widening) in patients with structural heart disease — illustrated in this pack by a case of propafenone-induced QRS widening in a child with arrhythmogenic right ventricular cardiomyopathy (PMID 33194879) and a report of propafenone provoking incessant ventricular tachycardia despite normal left ventricular function (PMID 8316922). This is directly relevant to any off-label use in inherited arrhythmia syndromes such as CPVT and should inform monitoring.

Please refer to the SmPC and BNF for full prescribing safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Full Screening Summary — All Predicted Indications

For transparency, all eight candidates screened in this evidence pack are listed below, ranked by TxGNN score. Note that **score does not track evidence quality or clinical direction** — see rationale column.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Rationale |
|------|----------------------|-------------|-----------------|-----------------|-----------|
| 1 | Manic bipolar affective disorder | 99.80% | L4 | **Hold — REJECTED** | Literature direction is reversed: reports describe propafenone *causing* mania/psychosis, not treating it. Likely a mis-signed drug–disease co-occurrence artefact. |
| 2 | **Catecholaminergic polymorphic ventricular tachycardia** | 99.79% | L3 | **Proceed with Guardrails** | Plausible RyR2-blockade mechanism, supported by in-vitro studies and a long-term case report. See main report above. |
| 3 | Periodic paralysis with transient compartment-like syndrome | 99.67% | L5 | Hold | No literature or trial evidence; mechanism unclear. |
| 4 | Prinzmetal angina | 99.45% | L5 | Hold | Mechanistically implausible — vasospastic angina requires vasodilation, not sodium-channel blockade; theoretical risk of harm. |
| 5 | Incessant infant ventricular tachycardia | 99.44% | L3 | Research Question | Supported by small, dated (1987–1993) case series in paediatric SVT/VT; needs contemporary safety/efficacy data. |
| 6 | Arrhythmogenic right ventricular cardiomyopathy (ARVC) | 99.42% | L3 | Research Question | Some case-level efficacy for ventricular arrhythmia suppression, but counterbalanced by reports of propafenone-induced proarrhythmia/QRS widening in this same population. |
| 7 | Nephrogenic syndrome of inappropriate antidiuresis | 99.23% | L5 | Hold | No mechanistic or literature basis. |
| 8 | Trichotillomania | 99.17% | L5 | Hold | No mechanistic or literature basis; psychiatric condition unrelated to cardiac sodium-channel activity. |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for CPVT specifically; all other candidates except ARVC and incessant infant VT are Hold)

**Rationale:**
CPVT is the only candidate with a coherent electrophysiological mechanism (RyR2 blockade) and corroborating clinical case evidence, but it rests on in-vitro data and a single long-term case report rather than controlled trials, and flecainide is the better-established Class IC agent for this indication.

**To proceed, the following is needed:**
- UK product labelling / SmPC warnings and contraindications (currently a **Blocking** data gap — required before any safety assessment)
- Confirmed mechanism of action data from DrugBank (currently a **High**-severity data gap)
- Prospective or registry-based clinical data on propafenone specifically (not flecainide) in confirmed CPVT patients
- Independent verification of current UK/MHRA marketing authorisation status, as this dataset shows none on record
- If pursuing ARVC or paediatric incessant VT as secondary indications: updated safety data addressing the proarrhythmia signal identified in the literature above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

