---
layout: default
title: Propranolol
parent: High Evidence (L1-L2)
nav_order: 487
evidence_level: L2
indication_count: 6
---

# Propranolol
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **6** 
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

Using the report template above (no additional skill needed — this is a defined content-generation task with an explicit spec already provided).

**Note on indication selection:** Among the 6 TxGNN candidates, the top-ranked ones by raw score (distal myopathy, congenital myopathy, chondroma) have **zero evidence** and the rationale text itself states they lack biological plausibility (Hold, L5). The only candidate with real clinical evidence is **cardiomyopathy** (rank 6, L2, "Proceed with Guardrails") — driven by decades of hypertrophic obstructive cardiomyopathy (HOCM) trials. This report focuses on that candidate as the clinically meaningful one; the others are noted briefly for completeness.

---

# Propranolol: From Cardiovascular Indications to Cardiomyopathy (Hypertrophic Obstructive Subtype)

## One-Sentence Summary

> Propranolol is a non-selective beta-blocker with long-established cardiovascular uses (hypertension, angina, arrhythmias).
> The TxGNN model predicts it may be effective for **Cardiomyopathy** — most specifically hypertrophic obstructive cardiomyopathy (HOCM) —
> with **3 clinical trials** and **20 publications** currently supporting this direction, including historical double-blind RCTs.
>
> Note: TxGNN's highest-scoring candidates for this drug (distal myopathy Tateyama type, congenital myopathy with thin filament excess, chondroma) returned **no supporting evidence** and are explicitly flagged in the model rationale as lacking biological plausibility. They remain at "Hold" and are not discussed further.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in source registry (data gap); propranolol is internationally established for hypertension, angina pectoris and cardiac arrhythmias |
| Predicted New Indication | Cardiomyopathy (evidence base concentrated in hypertrophic obstructive cardiomyopathy) |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (per this dataset — see caveat under UK Market Information) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was flagged as a data gap in the structured dataset (DG002). However, the evidence base itself is explicit: propranolol is a **non-selective beta-adrenergic receptor blocker** (β1 and β2), reducing heart rate, myocardial contractility and cardiac output. In hypertrophic obstructive cardiomyopathy, this negative inotropic/chronotropic action lowers left ventricular outflow tract (LVOT) pressure gradient — the central pathophysiological problem in HOCM.

This is not a novel mechanistic leap: propranolol's classical cardiovascular indications (hypertension, angina, arrhythmia) already exploit the same beta-blockade pathway. The extension to HOCM is a **within-class, within-mechanism** application rather than a repurposing into an unrelated therapeutic area, and it is supported by clinical use dating back to the 1970s–1990s (double-blind RCTs, haemodynamic catheterisation studies, and combination therapy trials with nifedipine/disopyramide).

The evidence is weaker and more mixed for related but distinct entities — dilated cardiomyopathy (haemodynamic deterioration risk noted in some cohorts) and cirrhotic cardiomyopathy (conflicting effects on QTc vs renal/circulatory function) — so the "Proceed with Guardrails" recommendation should be understood as applying most confidently to the HOCM subtype, not cardiomyopathy as a whole.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05427474](https://clinicaltrials.gov/study/NCT05427474) | Phase 3 | Unknown | 90 | Propranolol + gabapentin for paroxysmal sympathetic hyperactivity in traumatic brain injury (ICU); indirect relevance — not cardiomyopathy itself |
| [NCT05019027](https://clinicaltrials.gov/study/NCT05019027) | Phase 4 | Enrolling by invitation | 20 | N-of-1 deprescribing trial of beta-blockers in transthyretin cardiac amyloidosis; safety/usage data rather than efficacy proof |
| [NCT04767061](https://clinicaltrials.gov/study/NCT04767061) | Phase 4 | Completed | 9 | N-of-1 deprescribing trial of beta-blockers in HFpEF; physical function outcomes |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4586631](https://pubmed.ncbi.nlm.nih.gov/4586631/) | 1973 | RCT | British Heart Journal | Double-blind trial of propranolol vs practolol in hypertrophic cardiomyopathy |
| [3673167](https://pubmed.ncbi.nlm.nih.gov/3673167/) | 1987 | RCT/Combination study | Zeitschrift für Kardiologie | Nifedipine + propranolol combination in HCM over 6–24 months |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Cohort/Haemodynamic | British Heart Journal | Haemodynamic effects of nifedipine and propranolol in HOCM |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | Cohort/Exercise study | Cardiology | Effect of propranolol and disopyramide on LV function at rest and exercise in HCM |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Cohort/Observational | Am J Cardiology | Propranolol and arrhythmia in hypertrophic cardiomyopathy |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | Cohort/Haemodynamic | British Heart Journal | Propranolol effects on myocardial oxygen consumption and haemodynamics in HOCM |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Cohort/Haemodynamic | European Heart Journal | Diastolic stiffness: propranolol vs verapamil in HCM |
| [2920304](https://pubmed.ncbi.nlm.nih.gov/2920304/) | 1989 | Cohort/Echocardiographic | Canadian J Cardiology | Disopyramide + propranolol combination in HCM |
| [3189143](https://pubmed.ncbi.nlm.nih.gov/3189143/) | 1988 | Cohort/Haemodynamic | American Heart Journal | Acute haemodynamic effects of pindolol vs propranolol in dilated cardiomyopathy |
| [8989641](https://pubmed.ncbi.nlm.nih.gov/8989641/) | 1996 | Cohort/Haemodynamic | J Cardiac Failure | Predictors of intolerance and long-term propranolol effects in dilated cardiomyopathy |

## UK Market Information

No marketing authorisation records are present in this dataset (`total_licenses = 0`, `licenses = []`). This is a **known data gap** rather than confirmation of non-availability — propranolol is a long-established generic beta-blocker, and current UK licensing status (including brand/generic products and their approved indications) should be verified directly against the MHRA product database and current BNF entry before any decision is finalised.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications and drug interaction data were all flagged as data gaps in this evidence pack — DG001, Blocking severity — and could not be summarised here.)*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The HOCM-specific evidence base is genuine and decades-deep (multiple RCTs and haemodynamic studies), giving L2 evidence strength and a clear, already-exploited mechanistic pathway. However, the safety data gap (DG001, Blocking) and absent MOA documentation (DG002) mean this cannot yet clear a full safety review, and the evidence is markedly weaker for cardiomyopathy subtypes outside HOCM (dilated, cirrhotic).

**To proceed, the following is needed:**
- SmPC/BNF-sourced warnings, contraindications and DDI data (resolves DG001, currently Blocking)
- Formal MOA documentation from DrugBank or equivalent (resolves DG002)
- Confirmation of current UK marketing authorisation status and licensed indications for propranolol
- Scoping restricted specifically to HOCM rather than cardiomyopathy broadly, given the mixed/negative signals for dilated and cirrhotic subtypes
- No further action on the three TxGNN-flagged candidates with no evidence (distal myopathy Tateyama type, congenital myopathy with thin filaments, chondroma) — these remain correctly at "Hold"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

