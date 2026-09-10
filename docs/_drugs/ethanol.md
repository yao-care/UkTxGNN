---
layout: default
title: Ethanol
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 2
---

# Ethanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ethanol: From No UK-Licensed Indication to Migraine Disorder

## One-Sentence Summary

Ethanol currently holds no UK marketing authorisation and no recorded original therapeutic indication in this evidence pack. The TxGNN model predicts a possible link to **Migraine Disorder**, with a high embedding similarity score, but this is supported only by **32 clinical trials of low/indirect relevance** and **no literature** for this specific indication — and separately retrieved literature on a closely related migraine subtype suggests ethanol may in fact be a migraine *trigger* rather than a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded — no approved indication or licence on file for Ethanol |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ethanol is not available in this evidence pack, and no original indication is on record — this is a substance with no current UK medicinal licence, so there is no established therapeutic precedent to reason from by analogy.

The TxGNN score (0.993, rank 6374 of the model's candidate space) reflects knowledge-graph embedding similarity rather than a demonstrated pharmacological mechanism. Of the 32 clinical trials retrieved for "migraine disorder," none actually test ethanol as an intervention for migraine — they were graded **C (low/indirect relevance)** and cover unrelated interventions (vestibular rehabilitation, botulinum toxin, biofeedback apps, cardiovascular cohorts, etc.) that happened to co-occur with migraine-related search terms.

More importantly, literature retrieved for the closely related subtype "migraine with brainstem aura" points in the **opposite direction** to the repurposing hypothesis: an ADH2 genotype association study (PMID 19486361) and a review of alcoholic drinks as headache triggers (PMID 23614946) both support ethanol as a recognised **migraine trigger/risk factor**, not a treatment. This is a material caveat that should weigh against the prediction rather than support it.

---

## Clinical Trial Evidence

*Trials below were retrieved under the "migraine disorder" query but assessed as low/indirect relevance (Grade C) — none involve ethanol as the study intervention. They are listed for transparency on what evidence currently exists.*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05351086](https://clinicaltrials.gov/study/NCT05351086) | Phase 1 | Completed | 26 | Safety/PK study of PUR3100 in healthy adults; not an ethanol or migraine-treatment trial |
| [NCT06517446](https://clinicaltrials.gov/study/NCT06517446) | N/A | Recruiting | 48 | Virtual-reality optokinetic stimulation for unilateral vestibular hypofunction; unrelated to ethanol |
| [NCT07207603](https://clinicaltrials.gov/study/NCT07207603) | N/A | Enrolling by invitation | 1000 | Observational cardiovascular risk cohort; not a migraine or ethanol study |
| [NCT05454826](https://clinicaltrials.gov/study/NCT05454826) | N/A | Completed | 26 | Cold application plus relaxation exercises in migraine; non-pharmacological |
| [NCT07297901](https://clinicaltrials.gov/study/NCT07297901) | N/A | Enrolling by invitation | 30 | App-based HRV breathing programme for migraine relief; non-pharmacological |
| [NCT02810015](https://clinicaltrials.gov/study/NCT02810015) | Phase 2 | Unknown | 40 | Botulinum toxin for temporomandibular myofascial disorder; unrelated to ethanol |
| [NCT06197542](https://clinicaltrials.gov/study/NCT06197542) | N/A | Completed | 54 | Manual therapy techniques for migraine trigger points; non-pharmacological |
| [NCT03757208](https://clinicaltrials.gov/study/NCT03757208) | N/A | Completed | 113 | Preoperative carbohydrate loading before day-case cholecystectomy; unrelated |
| [NCT06263920](https://clinicaltrials.gov/study/NCT06263920) | N/A | Recruiting | 360 | Observational cohort on late-onset epilepsy and subsequent stroke/dementia; unrelated |
| [NCT00109083](https://clinicaltrials.gov/study/NCT00109083) | Phase 2 | Completed | 300 | Dose-ranging study of RWJ-333369 for migraine prophylaxis; intervention is not ethanol |

An additional 22 trials were retrieved but remain unclassified (relevance "pending") in the source data; none identified so far describe ethanol as the study drug.

---

## Literature Evidence

Currently no related literature available for the "Migraine Disorder" indication specifically.

*Note: literature retrieved under the closely related "migraine with brainstem aura" indication (14 items) includes two directly ethanol-relevant papers worth flagging to reviewers — [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) (ADH2 genotype and migraine risk) and [23614946](https://pubmed.ncbi.nlm.nih.gov/23614946/) (alcoholic drinks as headache triggers) — both characterising ethanol as a migraine risk factor/trigger rather than a therapeutic agent. The remaining 12 items are genetic-association or biomarker studies (vitamin D receptor, GABA receptors, NOS3, LAG3/CD4) with no direct ethanol mechanistic link.*

---

## UK Market Information

Ethanol holds no UK marketing authorisation as a licensed medicinal product for any indication (Market status: Not marketed; 0 authorisations on record). No product-level data (PL numbers, formulations, licensed indications) are available to tabulate.

---

## Safety Considerations

Safety data for this candidate could not be assessed: key warnings, contraindications and drug-interaction data are all marked as data gaps in the evidence pack, including a **blocking gap** (missing UK/SmPC-equivalent warning and contraindication data) that prevents even a preliminary safety screen.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but it is unsupported by mechanism (MOA unknown), by direct clinical evidence (all retrieved trials are unrelated to ethanol as an intervention), or by disease-specific literature (none available). Literature on a closely related migraine subtype actually characterises ethanol as a migraine trigger, which runs counter to the repurposing hypothesis. Combined with a blocking gap in safety data, there is currently no basis to proceed beyond Hold.

**To proceed, the following is needed:**
- Ethanol's mechanism of action data relevant to migraine pathophysiology (currently a data gap)
- UK-equivalent SmPC warnings and contraindications (blocking gap — required before any S1 safety screen)
- Direct clinical or preclinical evidence testing ethanol (or a specific formulation/route) against migraine, rather than co-occurrence-derived trial matches
- Reconciliation of the conflicting signal that ethanol is an established migraine trigger, not a treatment, before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

