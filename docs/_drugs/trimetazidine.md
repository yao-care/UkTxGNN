---
layout: default
title: Trimetazidine
parent: Model Prediction Only (L5)
nav_order: 643
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trimetazidine: predicted new indication Endolymphatic hydrops (Ménière's disease) (evidence level L5). Approved use: Not stated in the licence data (trimetazidine is generally used for a…"
monitor_inn: "Trimetazidine"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "endolymphatic hydrops", "active cochleovestibular Meniere disease", "active cochlear Meniere disease", "active vestibular Meniere disease", "exocrine pancreatic insufficiency", "vertigo, benign recurrent, 2", "46,XY disorder of gonadal development", "male infertility due to gonadal dysgenesis", "metastatic melanoma"]
---

# Trimetazidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Trimetazidine: From Angina Pectoris to Endolymphatic Hydrops (Ménière's Disease)

## One-Sentence Summary

Trimetazidine is a metabolic modulator marketed in the UK as a 20 mg tablet. The TxGNN model predicts it may be effective for **endolymphatic hydrops** (the pathology underlying Ménière's disease), supported by **no registered clinical trials** and **5 publications**, of which **2 are small double-blind comparisons against betahistine from 1990**.

*Note: the data compiled for this report did not include an approved indication text. The original indication of angina pectoris is taken from general knowledge of trimetazidine's use, not from the licence data.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (trimetazidine is generally used for angina pectoris) |
| Predicted New Indication | Endolymphatic hydrops (Ménière's disease) |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L2 (cautious interpretation; see below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*The top-ranked TxGNN prediction is mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies (98.83%), but it has no supporting studies (L5). Endolymphatic hydrops is the highest-ranked prediction with clinical literature, so it is the focus of this report.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, trimetazidine inhibits 3-ketoacyl-CoA thiolase. This shifts cellular energy metabolism from fatty acid oxidation towards glucose oxidation, which is thought to protect cells during ischaemia.

Ménière's disease causes recurrent vertigo, hearing loss, tinnitus and ear fullness. The proposed link is that trimetazidine protects inner-ear cellular energy metabolism and reduces ischaemia-related damage. This is plausible but unproven.

Two 1990 double-blind studies compared trimetazidine (60 mg/day) with betahistine in vestibular vertigo and Ménière's disease, which suggests some clinical activity. The studies are small and old. Their full text was not verified, and the available abstracts do not show the outcomes. Three related subtypes (active cochleovestibular, cochlear and vestibular Ménière's disease) share the same rationale, but no subtype-specific evidence is available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2240994](https://pubmed.ncbi.nlm.nih.gov/2240994/) | 1990 | RCT (double-blind) | Ann Otolaryngol Chir Cervicofac | Trimetazidine 60 mg/day vs betahistine 24 mg/day over 3 months in peripheral vertigo. 40 patients enrolled, 20 with Ménière's disease. Outcomes not available in the abstract provided. |
| [2240995](https://pubmed.ncbi.nlm.nih.gov/2240995/) | 1990 | RCT (double-blind) | Ann Otolaryngol Chir Cervicofac | Trimetazidine 60 mg/day vs betahistine 36 mg/day over 2 months in Ménière's disease. 45 patients enrolled. Outcomes not available in the abstract provided. |
| [10367069](https://pubmed.ncbi.nlm.nih.gov/10367069/) | 1999 | Review | Ann Otolaryngol Chir Cervicofac | Synopsis of clinical trials of trimetazidine 20 mg in vertigo. No abstract available. |
| [19454061](https://pubmed.ncbi.nlm.nih.gov/19454061/) | 2007 | Review | BMJ Clin Evid | General review of Ménière's disease. Describes symptoms and a fluctuating course; not specific to trimetazidine. |
| [26208913](https://pubmed.ncbi.nlm.nih.gov/26208913/) | 2016 | Basic research | Eur Arch Otorhinolaryngol | Histamine receptor expression in the human endolymphatic sac, providing the rationale for betahistine. Not specific to trimetazidine. |

A further 2015 study (PMID [26563011](https://pubmed.ncbi.nlm.nih.gov/26563011/), *B-ENT*) examined trimetazidine, betahistine and ginkgo biloba for residual dizziness after repositioning manoeuvres for benign paroxysmal positional vertigo. It is relevant to a different predicted condition (benign recurrent vertigo) and is only indirect evidence here.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206020B0AAAAAA (BNF code) | Trimetazidine HCl tablets 20 mg | Tablet | Not stated in the data compiled |

Only one authorisation was identified. The number shown is a BNF classification code rather than an MHRA PL number, and the BNF chapter code (0206, other antianginal drugs) is consistent with an antianginal use. Vertigo and Ménière's disease are not listed as approved indications in the data compiled.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug interactions were found in the data queried, and no knowledge-graph contraindications were recorded. This should not be read as evidence that none exist.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct clinical evidence is two small, old (1990) double-blind comparisons with betahistine, with no outcome data available in the abstracts, and no registered trials. The L2 grade is generous given the uncertain study quality, and the prediction remains a research question rather than an actionable repurposing candidate. Safety and licence data are also incomplete.

**To proceed, the following is needed:**
- Full-text review of the two 1990 trials (outcomes, dropout, statistical analysis, comparator dosing)
- A systematic search for newer controlled trials of trimetazidine in Ménière's disease, and a check against current NICE and ENT guidance
- Mechanism of action data confirmed from DrugBank
- SmPC warnings and contraindications, including known movement-disorder and renal-impairment cautions, reviewed for the target population
- The approved indication text and MHRA PL number for the UK product
- If evidence supports it, a prospective randomised trial against current standard care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

