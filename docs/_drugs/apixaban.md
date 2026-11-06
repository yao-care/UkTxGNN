---
layout: default
title: Apixaban
parent: Model Prediction Only (L5)
nav_order: 67
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-06
monitor_inn: "Apixaban"
predicted_indications: ["migraine disorder"]
description: "Apixaban: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Apixaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Apixaban: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Apixaban is an oral anticoagulant that directly inhibits factor Xa. The TxGNN model predicts it may be relevant to **migraine disorder**, but the evidence is weak: only **1 clinical trial** (indirect, not migraine-focused) and **3 publications** (two case reports and one retrospective study) were found. None of these supports apixaban as a migraine treatment, so the evidence level is **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9902 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Apixaban is known as a direct factor Xa inhibitor, which reduces thrombin generation and clot formation.

The only proposed link to migraine is a hypothesis: in a subset of people with migraine with aura, paradoxical embolism (for example through a patent foramen ovale) or a hypercoagulable state (for example antiphospholipid antibodies) might contribute to attacks, so anticoagulation could in theory help. There is no established mechanism supporting factor Xa inhibition as a migraine treatment, and the available case reports point in contradictory or unfavourable directions. The model score should therefore be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compared patent foramen ovale closure, anticoagulants and antiplatelet therapy for preventing stroke recurrence. Migraine was not the primary endpoint and apixaban was not specifically studied, so this is indirect evidence only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Looked at response to antithrombotic therapy in refractory migraine with antiphospholipid antibodies; apixaban was not clearly the agent tested. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura remitted on warfarin, returned within 3 weeks of switching to apixaban, and settled again once warfarin was resumed. No benefit seen with apixaban. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report with literature review | The Neurologist | Migraine with aura worsened after starting apixaban; the literature on direct oral anticoagulants in migraine is described as scarce and controversial. |

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0208020Z0AAACAC | Apixaban 1mg/ml oral suspension sugar free | Apixaban |
| 0208020Z0AAAAAA | Apixaban 2.5mg tablets | Apixaban |
| 0208020Z0AAABAB | Apixaban 5mg tablets | Apixaban |
| 0208020Z0BBAAAA | Eliquis 2.5mg tablets | Apixaban |
| 0208020Z0BBABAB | Eliquis 5mg tablets | Apixaban |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

The BNF classification code for this record is 0208020Z0 (oral anticoagulants).

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Examples of those graded **Major** include acetylsalicylic acid (aspirin), cobicistat, deferasirox, ibritumomab tiuxetan and tositumomab. Examples graded **Moderate** include clarithromycin, dexamethasone, aprepitant, miconazole, clotrimazole and sugammadex.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study supports apixaban for migraine. The two case reports describe migraine with aura that worsened, or did not resolve, on apixaban, and the single Phase 3 trial is not migraine-focused. The high TxGNN score is not backed by clinical evidence, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic data supporting a role for factor Xa inhibition in migraine
- Prospective studies that directly examine apixaban in migraine, ideally in defined subgroups (for example migraine with aura and PFO or antiphospholipid antibodies)
- Review of the bleeding risk of anticoagulation in a non-thrombotic condition such as migraine

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

