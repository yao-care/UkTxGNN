---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 512
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Prasugrel: predicted new indication Migraine disorder (evidence level L3). Approved use: Acute coronary syndrome"
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Prasugrel: From Acute Coronary Syndrome to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Prasugrel is a P2Y12 platelet inhibitor, originally used for acute coronary syndrome.
The TxGNN model predicts it may be effective for **migraine disorder** (the highest-ranked indication with any supporting evidence), with **2 clinical trials** (neither testing prasugrel directly) and **2 relevant publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome |
| Predicted New Indication | Migraine disorder (the top-ranked prediction, pulmonary hypertension, has no direct supporting evidence, so migraine is evaluated here) |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, prasugrel is a thienopyridine antiplatelet drug that acts by P2Y12 receptor antagonism. Its efficacy in acute coronary syndrome is established, and mechanistically it may be applicable to migraine in a specific subgroup.

Some people with migraine have a patent foramen ovale (PFO), a small opening in the heart wall. One proposed explanation is that small paradoxical emboli, or platelet-derived vasoactive substances such as serotonin, may trigger aura or headache. Blocking platelet activation with a P2Y12 inhibitor could therefore reduce migraine in these patients.

The supporting data are indirect. They consist of a retrospective review of thienopyridine therapy (clopidogrel and prasugrel) in migraineurs with PFO, and an open-label pilot study of ticagrelor, a related but different P2Y12 inhibitor. The high TxGNN score is a model prediction and does not by itself demonstrate efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | Recruiting | 32 | PFO-directed therapy for migraine cessation. The summary mentions prasugrel as a platelet-inhibiting option, but it is unclear whether prasugrel is the tested agent. Indirect support only. |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A (device) | Terminated | 7 | GORE CARDIOFORM septal occluder versus sham for migraine relief. Terminated early with 7 participants. Does not evaluate prasugrel. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine use (including prasugrel) in migraineurs with PFO; clinical experience suggested symptom reduction in some patients. |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | Ticagrelor (a non-thienopyridine P2Y12 inhibitor) for refractory migraine with PFO. Conducted after thienopyridines were observed to reduce migraine in some PFO patients. |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preclinical | European Journal of Pharmacology | Prasugrel showed neuroprotective, anti-seizure effects in a mouse kindling model. Only indirectly relevant to migraine. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0209000Y0AAABAB | Prasugrel Tab 10mg | Not stated | Not stated |

The data compiled for this report show one valid single-ingredient authorisation. The dosage form, manufacturer and indication text were not available, so please check the current MHRA record, SmPC and BNF.

---

## Safety Considerations

**Contraindications (from the TxGNN knowledge graph, not label text):** the graph links prasugrel with the following conditions, which should be checked against the SmPC:
- Liver failure
- Hypotensive disorder
- Blood coagulation disease
- Stroke and cerebrovascular disorders, including cerebral infarction, transient ischaemic attack and vertebrobasilar insufficiency
- Intracranial haemorrhage
- Thrombocytopenic purpura
- Injury

**Drug Interactions:** 100 interactions were recorded. Main ones:
- **Major:** deferasirox, ibritumomab tiuxetan
- **Moderate:** acetylsalicylic acid (aspirin), morphine, opium, fenfluramine, dexfenfluramine, sibutramine
- **Minor:** several proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), H2 blockers (famotidine, ranitidine, cimetidine, nizatidine) and bupropion

**Bleeding risk:** In a chronic, non-life-threatening condition such as migraine, the bleeding risk of prasugrel is a significant consideration, particularly given the stroke and intracranial haemorrhage signals above.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The evidence for migraine is limited to a small retrospective review, a pilot study of a different P2Y12 inhibitor, and trials that do not clearly test prasugrel. Prasugrel carries a notable bleeding risk, which is hard to justify in a non-life-threatening condition without stronger evidence. Other predicted indications (for example pulmonary hypertension, rheumatoid arthritis, leprosy) have only model predictions with no direct supporting evidence.

**To proceed, the following is needed:**
- Confirmation of whether prasugrel is the intervention in NCT07629635
- A randomised, controlled trial of prasugrel in migraine with PFO, with a defined bleeding-risk assessment and monitoring plan
- Mechanism of action data and full MHRA authorisation details (dosage form, indication, SmPC warnings)
- A benefit-risk comparison against established migraine treatments and alternative antiplatelets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

