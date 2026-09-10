---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Antiplatelet Therapy to Migraine Disorder

## One-Sentence Summary

> Clopidogrel is a P2Y12 ADP-receptor antiplatelet agent, established for prevention of atherothrombotic events such as myocardial infarction, ischaemic stroke and peripheral arterial disease.
> The TxGNN model predicts it may also be effective for **Migraine Disorder** — particularly in patients with a patent foramen ovale (PFO) or atrial septal defect (ASD) — with **8 clinical trials** (including two completed RCTs directly testing clopidogrel) and **20 publications** currently supporting this direction.
> A closely related, slightly higher-scoring prediction, **migraine with brainstem aura**, shares the same mechanistic story but has considerably less mature direct evidence (0 registered trials) and is noted separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of atherothrombotic events (post-MI, ischaemic stroke, peripheral arterial disease, acute coronary syndrome) — general clinical knowledge; no UK licence/indication text was returned in this evidence pack |
| Predicted New Indication | Migraine Disorder (PFO/ASD-associated subgroup) |
| TxGNN Prediction Score | 99.44% (model rank 5445 of candidates) |
| Evidence Level | L1 |
| UK Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails (conditional — see Blocking gap below) |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for clopidogrel is flagged as a **Blocking/High-severity data gap** in this evidence pack (DG002 — MOA not yet retrieved from DrugBank). Based on the evidence that *is* available, clopidogrel is a thienopyridine P2Y12 ADP-receptor antagonist that irreversibly inhibits platelet activation and aggregation — the mechanism underlying its established antiplatelet use.

Two convergent lines of evidence support a link between P2Y12 inhibition and migraine. First, preclinical work shows P2Y12 receptors are expressed on microglia in the trigeminal nucleus caudalis, and P2Y12-mediated microglial activation via the RhoA/ROCK pathway has been implicated in chronic migraine pathophysiology (PMID 31722730; PMID 34363208, nitroglycerin-induced migraine model). Second — and with much stronger clinical support — a substantial proportion of migraineurs, especially those with aura, have a PFO or ASD. Platelet activation and paradoxical micro-embolisation through this right-to-left shunt are hypothesised to trigger cortical spreading depression, and the clearest clinical signal comes from the CANOA randomised trial, which showed adding clopidogrel to aspirin after transcatheter ASD closure significantly reduced new-onset migraine attacks (PMID 26551304, 32965476).

Importantly, this mechanistic and clinical evidence is specific to the **PFO/ASD-associated migraine subgroup**, not migraine in general. The closely related prediction "migraine with brainstem aura" (TxGNN score 99.44%, rank 5399) reflects the same underlying biology but currently has no registered clinical trials, placing it at an earlier evidentiary stage (L2, "Research Question") than migraine disorder (L1, "Proceed with Guardrails").

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA study: clopidogrel + aspirin vs aspirin alone for prevention of new-onset migraine after transcatheter ASD closure — the most direct completed RCT of clopidogrel for this indication |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSURE I: PFO closure vs anticoagulant/antiplatelet therapy (including clopidogrel-class agents) for stroke recurrence prevention; migraine was a secondary endpoint |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial evaluating clopidogrel specifically for migraine relief in patients with right-to-left shunt |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING study: PFO closure vs medical therapy (including antiplatelets) for migraine relief |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1000 | COMPETE study: anticoagulation vs antiplatelet vs standard migraine therapy in patients with PFO |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | High-risk PFO closure vs medical therapy for migraine headache |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | GORE CARDIOFORM device trial for PFO closure and migraine relief; terminated early, device- not drug-focused |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3300 | Broad EMR-based pragmatic neurology registry; not clopidogrel-specific |

*(Migraine with brainstem aura currently has no registered clinical trials.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA trial: clopidogrel + aspirin reduced new-onset migraine after transcatheter ASD closure vs aspirin alone |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT | JAMA Cardiology | CANOA 1-year follow-up: benefit attenuates after clopidogrel is stopped at 3 months |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT | Cephalalgia | Pilot randomised controlled study of clopidogrel as prophylactic treatment for migraine |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Review | Headache | Systematic review of antithrombotic drugs' role in migraine prevention |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Review | Indian J Thorac Cardiovasc Surg | Systematic review of new-onset headache after transcatheter ASD closure |
| [38109984](https://pubmed.ncbi.nlm.nih.gov/38109984/) | 2024 | Review | American Heart Journal | Study design/rationale for COMPETE trial comparing antithrombotic vs migraine-specific therapy in PFO |
| [31722730](https://pubmed.ncbi.nlm.nih.gov/31722730/) | 2019 | Preclinical/Mechanistic | J Neuroinflammation | P2Y12 receptor mediates microglial activation via RhoA/ROCK pathway in chronic migraine mouse model |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after transcatheter PFO/ASD closure |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | J Investig Med | Clopidogrel as effective complementary prophylactic for drug-refractory migraine with PFO |
| [34363208](https://pubmed.ncbi.nlm.nih.gov/34363208/) | 2021 | Preclinical/Mechanistic | British Journal of Pharmacology | P2Y12 receptor involvement in nitroglycerin-induced migraine model in mice |

---

## UK Market Information

No MHRA marketing authorisation records were returned in this evidence pack (market status: **Not marketed**; total licences on file: 0). Clopidogrel is a long-established, widely available UK generic medicine in its licensed antiplatelet indications, but specific product/PL numbers and current SmPC indication wording should be verified directly against the MHRA Products database before any patient-facing use.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: retrieval of clopidogrel's UK label warnings and contraindications is logged as a **Blocking** data gap (DG001) in this evidence pack — it must be resolved before a safety assessment can be completed. Incidental literature signals worth flagging for that review include bleeding-related events with clopidogrel combined with other agents (e.g. intracerebral haemorrhage with celecoxib + clopidogrel, PMID 11793622; spontaneous haemarthrosis with clopidogrel + aspirin, PMID 12624808).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(conditional on resolving the Blocking safety data gap below)*

**Rationale:**
- Migraine disorder is supported by L1 evidence: two completed RCTs (CANOA and its 1-year follow-up) plus a dedicated Phase 4 trial testing clopidogrel directly in shunt-associated migraine.
- The efficacy signal is specific to the **PFO/ASD-associated migraine subgroup**, not migraine broadly — any repurposing pathway should be scoped to this population, not a general migraine label.
- Despite strong efficacy evidence, DG001 (missing UK label warnings/contraindications) is a **Blocking** gap that prevents completion of the initial safety screen (S1) and must be resolved before this candidate can advance further.

**To proceed, the following is needed:**
- Retrieve MHRA SmPC warnings and contraindications for clopidogrel (resolves DG001)
- Retrieve DrugBank mechanism-of-action record (resolves DG002)
- Confirm and document PFO/ASD status as an eligibility criterion for the target population
- Verify current UK marketing authorisation / PL numbers, since none were returned in this evidence pack
- Complete a bleeding-risk DDI screen (particularly NSAIDs and other antiplatelets/anticoagulants) given signals in the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

