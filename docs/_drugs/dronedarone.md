---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone is a Class III antiarrhythmic (multi-channel blocker) used for rhythm control in atrial fibrillation/atrial flutter. The TxGNN model predicts it may reduce the risk of **stroke**, with **19 clinical trials** and **20 publications** currently supporting this direction — though the evidence base includes an important safety caveat (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation / atrial flutter (per literature evidence, PMID 20730068) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data for dronedarone is not yet available in this evidence pack (data gap DG002). Based on the clinical and mechanistic evidence collected, dronedarone is a multi-channel blocker (Na⁺/K⁺/Ca²⁺) with antiadrenergic activity, approved for maintaining sinus rhythm and reducing cardiovascular hospitalisation in patients with paroxysmal or persistent atrial fibrillation.

The rationale for a stroke-prevention effect is not a new mechanism but an extension of dronedarone's existing rhythm-control indication: by maintaining sinus rhythm, the drug is thought to reduce left atrial appendage thrombus formation and therefore cardioembolic stroke risk. Supporting this, a post-hoc analysis of the pivotal ATHENA trial (PMID 22149318, tier 1) reported a reduction in stroke incidence among patients with paroxysmal/persistent AF treated with dronedarone.

However, this mechanistic link is AF-subtype dependent. The PALLAS trial (NCT01151137, Phase 3) tested dronedarone specifically in **permanent** AF with additional risk factors and was **terminated early** because of an increase in stroke and cardiovascular death — the opposite of the predicted effect. This means the therapeutic direction is only plausible in paroxysmal/persistent AF and is contraindicated in permanent AF, which materially qualifies the "Proceed with Guardrails" recommendation below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | PALLAS trial: dronedarone 400 mg BID in permanent AF with risk factors — terminated early due to increased stroke/cardiovascular death; defines a contraindicated subgroup |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Early dronedarone vs usual care in first-detected AF — positive direct comparison for improved outcomes |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1,898 | Multicentre prospective study of dronedarone efficacy, safety and quality-of-life in early rhythm control of AF |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | Early rhythm-control therapy for stroke prevention after acute ischaemic stroke with AF (drug not yet confirmed as dronedarone-specific) |
| [NCT07242326](https://clinicaltrials.gov/study/NCT07242326) | N/A | Enrolling by invitation | 1,000 | Observational registry (SNAP AF-52) assessing label-concordant oral anticoagulant dosing/adherence in elderly AF patients |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Cross-sectional observational study of NOAC management for stroke prevention in elderly NVAF patients (Spain) |
| [NCT03840291](https://clinicaltrials.gov/study/NCT03840291) | Phase 4 | Completed | 36 | Resolution of left atrial appendage thrombi with edoxaban in NVAF — indirect AF-stroke link, not a dronedarone intervention |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4 trial: early structured rhythm-control therapy (incl. antiarrhythmics) reduced AF-related complications vs usual care |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1,015 | International observational cohort comparing real-world effectiveness of dronedarone vs other antiarrhythmics |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A | Completed | 87,810 | Systematic literature review/NMA of dronedarone (Multaq®) vs sotalol safety in AF |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT post-hoc (EAST-AFNET 4) | Clin Res Cardiol | Long-term safety/efficacy of amiodarone and dronedarone for early rhythm control |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS, NEJM) | N Engl J Med | Dronedarone increased stroke/death in high-risk permanent AF — pivotal negative safety signal |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | ATHENA trial post-hoc analysis suggests decreased stroke risk with dronedarone |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Review | Curr Cardiol Rev | Overview of stroke prevention concepts/controversies in AF |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atr Fibrillation | Real-world comparison of CV events, stroke, HF, ILD and liver injury: dronedarone vs amiodarone/other antiarrhythmics |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Retrospective comparison of dronedarone vs sotalol effectiveness/safety in AF-naive veterans |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Review/Post-hoc (ATHENA) | Eur J Heart Fail | Dronedarone in AF/AFL with concomitant HFpEF/HFmrEF |
| [21930637](https://pubmed.ncbi.nlm.nih.gov/21930637/) | 2011 | Review | Am J Health Syst Pharm | Review of drug-induced heart failure, precautions and management |
| [37777298](https://pubmed.ncbi.nlm.nih.gov/37777298/) | 2023 | Review chapter | Am J Cardiol | Rate versus rhythm control strategy selection in AF management |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic/basic study | Atherosclerosis | Dronedarone shows anticoagulant/antiplatelet effects independent of antiarrhythmic action |

---

## UK Market Information

Dronedarone is currently **not marketed** in the UK (0 marketing authorisations on record in this dataset). No MHRA licence or product data is available to summarise.

---

## Safety Considerations

**Evidence-based safety signal (from clinical trial data):** The PALLAS trial (NCT01151137) was terminated early because dronedarone increased the risk of stroke and cardiovascular death in patients with **permanent** AF and additional risk factors. This restricts the plausible target population for any stroke-prevention use to paroxysmal/persistent AF, and permanent AF should be treated as a population at increased risk, not a candidate subgroup.

Formal safety data (key warnings, contraindications, drug interactions) are not yet available in this dataset (data gap DG001, blocking). Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3/4 trials and a post-hoc ATHENA analysis suggesting reduced stroke risk in paroxysmal/persistent AF, but the PALLAS trial shows a directly opposing safety signal in permanent AF. Any repurposing pathway must explicitly exclude permanent AF and cannot proceed without formal safety documentation, and the drug currently has no UK marketing authorisation.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC warnings and contraindications (DG001, blocking)
- Formal DrugBank mechanism-of-action documentation (DG002)
- Confirmation of UK licensing/import pathway, given current "Not Marketed" status
- Prospective evidence restricted to paroxysmal/persistent AF populations, explicitly excluding permanent AF per the PALLAS findings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

