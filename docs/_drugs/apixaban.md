---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: From Atrial Fibrillation / VTE to Migraine Disorder

## One-Sentence Summary

Apixaban (Eliquis®) is a direct oral Factor Xa inhibitor established for stroke and systemic embolism prevention in non-valvular atrial fibrillation, and for the treatment and prophylaxis of venous thromboembolism.
The TxGNN model predicts it may have utility in **Migraine Disorder**, with **1 clinical trial** and **4 publications** currently identified in support of this direction.
However, available evidence is predominantly case-report level (Evidence Level: **L4**) and includes a notable **negative signal** — apixaban appears inferior to warfarin in anticoagulant-responsive migraine subgroups — warranting a **Hold** recommendation pending further mechanistic evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Stroke and systemic embolism prevention in non-valvular AF; treatment and prophylaxis of DVT and PE |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| UK Market Status | MHRA-authorised (Eliquis®); MHRA licence data unavailable in current Evidence Pack |
| Number of Marketing Authorisations | Unavailable in current Evidence Pack |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Apixaban is a selective, reversible direct inhibitor of Factor Xa (FXa), a central serine protease in the coagulation cascade responsible for converting prothrombin to thrombin. By attenuating thrombin generation, apixaban reduces fibrin clot formation without directly inhibiting existing thrombin or platelet aggregation. Detailed mechanism of action data were not retrieved in the current Evidence Pack, but apixaban's pharmacological class and clinical profile as a DOAC are well established.

The theoretical rationale for migraine rests on two overlapping pathways. First, an epidemiological association exists between patent foramen ovale (PFO) and migraine with aura: right-to-left atrial shunting may permit paradoxical microemboli to bypass pulmonary filtration and trigger cortical spreading depression — the neurophysiological substrate of migraine aura. An anticoagulant reducing thrombus burden might, in theory, lower embolic trigger frequency. Second, FXa can activate protease-activated receptor 2 (PAR-2) on neurovascular and glial cells; inhibiting this signalling axis could modulate neurogenic inflammation relevant to migraine pathophysiology.

Crucially, however, available clinical literature presents a **negative signal specific to apixaban**. Published case reports document patients in long-term migraine remission on warfarin who experienced symptom recurrence within weeks of switching to apixaban, resolving again rapidly upon returning to warfarin. This pattern suggests that warfarin's broader multi-factor anticoagulant effect (suppressing Factors II, VII, IX, and X, and thereby achieving more complete thrombin inhibition) may be necessary for migraine suppression — and that selective FXa inhibition alone is insufficient. An alternative explanation is that FXa itself exerts a PAR-2-mediated neuromodulatory function that is paradoxically disrupted when selectively blocked. The TxGNN high prediction score most likely reflects network-level topological proximity between apixaban's drug node and migraine-related disease nodes, rather than confirmed clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Randomised trial comparing PFO transcatheter closure, oral anticoagulation (warfarin), and antiplatelet therapy for secondary stroke prevention. The anticoagulant arm used warfarin — not apixaban — and migraine was not a primary or pre-specified secondary endpoint. Provides indirect mechanistic context on PFO-associated thromboembolic pathways but no direct evidence for apixaban in migraine. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Pilot Clinical Trial | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies treated with antithrombotic therapy. Reports symptomatic improvement with anticoagulation in a defined aPL-positive subpopulation — the strongest available signal for anticoagulation in migraine, though retrospective, not specific to apixaban, and in a highly selected group. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | Case of migraine with aura worsening after initiating apixaban, with a narrative review of DOACs and headache. Authors conclude that the impact of direct oral anticoagulants on migraine frequency and severity remains unclear and that current literature is scarce and contradictory. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | A 55-year-old woman experienced complete remission of migraine with aura for 12 years on warfarin; symptoms returned within 3 weeks of switching to apixaban and resolved again within days of resuming warfarin. Represents a direct **negative comparator signal** for apixaban versus warfarin in anticoagulant-responsive migraine. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Case of vestibular migraine resolving on the combination of warfarin and topiramate. The anticoagulant implicated is warfarin, not apixaban; provides further indirect support for vitamin K antagonist — but not DOAC — anticoagulation in migraine subtypes. |

---

## Safety Considerations

Detailed SmPC warnings, contraindications, and drug interaction data were not retrieved in the current Evidence Pack. As a direct oral anticoagulant, apixaban carries an inherent and dose-dependent risk of **serious or fatal bleeding events**, including intracranial haemorrhage. Any off-label use in migraine would require a formal individual bleeding risk assessment (e.g., HAS-BLED score in the AF context), a complete review of concomitant medicines — particularly antiplatelet agents, NSAIDs, SSRIs, and other anticoagulants — and careful evaluation of renal and hepatic function.

Please refer to the **Eliquis SmPC** and **BNF Section 2.8.2** for complete prescribing information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.02%), the clinical evidence for apixaban in migraine is confined to case reports and a single small retrospective study, and — critically — includes a **direct negative comparator signal**: patients whose migraines resolved on warfarin experienced relapse when switched to apixaban. This pattern undermines the hypothesis that selective FXa inhibition is sufficient for migraine prevention and suggests the repurposing target, if valid at all, may require a different anticoagulant mechanism or a more precisely defined patient subgroup.

**To proceed, the following would be needed:**

- Preclinical mechanistic studies examining whether selective FXa inhibition produces any measurable effect in validated migraine models (e.g., cortical spreading depression frequency, PAR-2 pathway modulation in trigeminal neurovascular preparations)
- Prospective identification of a biologically defined subpopulation — such as PFO-positive migraine with aura, or antiphospholipid antibody-associated refractory migraine — where DOAC anticoagulation could be tested in a hypothesis-driven manner
- Retrospective pharmacovigilance analysis of migraine-related outcomes in patients already prescribed apixaban for approved indications, to establish real-world signal direction before considering a formal interventional study
- Retrieval of full MHRA authorisation data and Eliquis SmPC to characterise the safety envelope and applicable contraindications prior to any off-label investigation
- Direct comparison head-to-head data (apixaban vs. warfarin) in the PFO-migraine subgroup, to resolve whether the negative signal in existing case reports is reproducible at a cohort level

---

> ⚠️ **Disclaimer:** This report is intended for research evaluation purposes only and does not constitute clinical advice or a recommendation for prescribing. All drug repurposing candidates require prospective clinical validation before therapeutic application. Healthcare professionals should consult the current SmPC, BNF, and NICE guidance before any off-label use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

