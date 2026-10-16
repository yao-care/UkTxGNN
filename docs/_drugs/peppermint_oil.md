---
layout: default
title: Peppermint Oil
parent: Model Prediction Only (L5)
nav_order: 483
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Peppermint Oil: predicted new indication Cardiovascular disease (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Peppermint oil"
predicted_indications: ["leprosy", "pneumocystosis", "coronary artery disease", "myocardial ischemia", "echinococcus granulosus infectious disease", "polyp of vocal cord", "uterine polyp", "polyp of middle ear", "cardiovascular disease", "polyp of frontal sinus"]
---

# Peppermint Oil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Peppermint Oil: From an Unspecified Original Indication to Cardiovascular Disease

## One-Sentence Summary

Peppermint oil is a long-established product marketed in the UK, but no approved indication text is available in the data compiled for this report.
The TxGNN model's highest-scoring prediction is leprosy, but the only prediction with any supporting evidence is **cardiovascular disease**, which is the focus of this report.
That evidence consists of **1 completed clinical trial** and **2 directly linked publications**, all concerning blood pressure and cardiometabolic markers rather than cardiovascular outcomes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Cardiovascular disease (the highest-ranked prediction with supporting evidence; the top-scoring prediction overall, leprosy, has none) |
| TxGNN Prediction Score | 99.13% (cardiovascular disease); leprosy 99.80% |
| Evidence Level | L3 (cardiovascular disease); L5 for all other predictions |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Peppermint oil is rich in menthol and flavonoids, and its original therapeutic use cannot be confirmed from the data compiled for this report.

A small human physiology study (PMID 30070742) found that menthol combined with gastric cooling increased cardiac parasympathetic activity in healthy volunteers, which lowered heart rate. This could plausibly affect blood pressure, and the trial team behind NCT05561543 reported earlier work suggesting oral peppermint may improve systolic blood pressure and blood lipids in healthy people.

This link is plausible but unconfirmed. The evidence concerns blood pressure and cardiometabolic risk markers, not hard cardiovascular outcomes such as myocardial infarction or stroke. The results of the completed trial are not detailed in the data supplied, so the size and direction of any effect cannot be confirmed.

The other nine top-ranked predictions have no trials or literature behind them. They are leprosy, pneumocystosis, coronary artery disease, myocardial ischaemia, echinococcosis, and four polyp-type conditions (vocal cord, uterine, middle ear, frontal sinus). The high scores for the polyp conditions appear to reflect graph similarity between related disease nodes rather than biological rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | Not applicable | Completed | 40 | Peppermint oil versus placebo on cardiometabolic outcomes in mild-to-moderate hypertension (2024–2025). Small, not a classic Phase 2/3 efficacy design; results not detailed in the data supplied |

No clinical trials are registered for the other nine predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42024666](https://pubmed.ncbi.nlm.nih.gov/42024666/) | 2026 | Randomised controlled trial report | PLoS One | Twice-daily peppermint oil supplementation on cardiometabolic outcomes in pre- and stage 1 hypertension; placebo-controlled |
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | Trial protocol | PLoS One | Protocol for the placebo-controlled trial above; hypothesis that menthol and flavonoids may offer blood pressure benefits |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Human physiology study | Experimental Physiology | Gastric cooling and menthol increased cardiac parasympathetic efferent activity in healthy volunteers |
| [25037671](https://pubmed.ncbi.nlm.nih.gov/25037671/) | 2014 | Commentary | Explore | Mentions peppermint oil for irritable bowel syndrome; not cardiovascular |

Other retrieved publications concerned formulation of unrelated antihypertensive drugs or analytical methods and are not relevant.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190601000AAAKAK | Peppermint Water Concentrated BP 1973 | Not stated | Not stated |
| 0102000T0AAAAAA | Peppermint Oil Capsules, E/C 0.2 ml | Not stated (enteric-coated capsule per product name) | Not stated |

Both entries are valid single-ingredient products. The identifiers above are as recorded in the compiled data and are not in the standard PL number format, so they should be verified against the MHRA and BNF records.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supported prediction, cardiovascular disease, rests on one small completed trial (n=40) in hypertension and a plausible but unconfirmed mechanism. This is L3 evidence, with surrogate endpoints and no confirmed results. All other predictions, including the highest-scoring one (leprosy), are computational only. Safety data are also unavailable, so the drug cannot yet be screened for safety.

**To proceed, the following is needed:**
- Published results from NCT05561543 and PMID 42024666 (effect size and direction on blood pressure and lipids)
- Safety information (warnings, contraindications, interactions) from the SmPC and BNF
- Mechanism of action data, for example from DrugBank
- Approved indication text, dosage forms and verified authorisation numbers for the two UK products
- Larger, adequately powered trials with clinical cardiovascular endpoints, if the hypertension findings are positive
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

