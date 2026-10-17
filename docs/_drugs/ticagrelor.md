---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Acute coronary syndrome"
monitor_inn: "Ticagrelor"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "ischemic disease", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is a reversible P2Y12 platelet inhibitor, originally used for acute coronary syndrome and peripheral arterial disease.
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**, with **2 related clinical trials** (one large Phase 3 trial still in progress) and **2 publications** currently supporting this direction.
The strongest evidence in the data compiled for this report lies in the broader category of ischaemic disease, where ticagrelor already has substantial randomised trial support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome; peripheral arterial disease; intermittent claudication (MHRA indication text not available in the data compiled; taken from knowledge graph indication edges) |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 by study design (a Phase 3 RCT exists, but it is not yet complete and has no results, so efficacy is unconfirmed) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a reversible P2Y12 receptor antagonist that reduces platelet aggregation and thrombus formation. Its efficacy in acute coronary syndrome and peripheral arterial disease is established, and mechanistically it may be applicable to intracranial arteriosclerosis.

Intracranial atherosclerotic stenosis shares the same platelet-driven atherothrombotic pathophysiology as coronary and peripheral arterial disease. Antiplatelet therapy is already the standard treatment, and the current approach (clopidogrel plus aspirin, then aspirin alone) still leaves a high risk of recurrent stroke. Ticagrelor is not affected by CYP2C19 loss-of-function variants, which reduce clopidogrel activation. This is a potential advantage in this population, supported by the CHANCE-2 trial in stroke/TIA patients who carry these variants.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Phase 3 | Active, not recruiting | 1,683 | Tests whether rivaroxaban, ticagrelor or both are superior to clopidogrel for lowering 1-year ischaemic stroke, intracerebral haemorrhage or vascular death in intracranial atherostenosis. No results yet; the antiplatelet arm may not be ticagrelor-specific. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | Not applicable | Recruiting | 100 | Pilot study of genotype-guided P2Y12 inhibitor selection (including ticagrelor) vs conventional clopidogrel in symptomatic intracranial atherosclerotic disease. Low power; no results yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | J Neurointerv Surg | Experience with ticagrelor 60 mg twice daily plus aspirin 81 mg compared with aspirin plus clopidogrel for intracranial stenting. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial design paper | Int J Stroke | Describes the design and early progress of CAPTIVA, which tests alternative dual antithrombotic regimens against clopidogrel plus aspirin. |

**Supporting evidence from the broader ischaemic disease prediction (rank 4):** large RCTs in related vascular settings include THEMIS in stable coronary disease with diabetes ([31475798](https://pubmed.ncbi.nlm.nih.gov/31475798/)), TWILIGHT in high-risk PCI patients ([31556978](https://pubmed.ncbi.nlm.nih.gov/31556978/)), PEGASUS-TIMI 54 in prior myocardial infarction ([25773268](https://pubmed.ncbi.nlm.nih.gov/25773268/)), CHANCE-2 in stroke/TIA with CYP2C19 loss-of-function ([34708996](https://pubmed.ncbi.nlm.nih.gov/34708996/)), and a post-CABG ACS trial ([40888737](https://pubmed.ncbi.nlm.nih.gov/40888737/)). These largely overlap with the approved ACS indication, so they are indication extensions rather than novel repurposing.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0209000Z0AAAAAA | Ticagrelor tablets 90 mg | Tablet (not specified) | Indication text not available in the data compiled |

Please check the current MHRA-approved indications and BNF classification (antiplatelet drugs, cardiovascular system) in the SmPC.

---

## Safety Considerations

- **Contraindications (from knowledge graph, not label text):** liver failure, liver disease, gallbladder disease, intracranial haemorrhage. These must be verified against the SmPC. Intracranial haemorrhage is especially relevant to a cerebrovascular indication.
- **Drug Interactions (100 interactions recorded; selected examples):**
  - **Major:** clarithromycin.
  - **Moderate:** aspirin (acetylsalicylic acid), morphine, simvastatin, dexamethasone, budesonide, aprepitant, saxagliptin, miconazole, rolapitant.
  - **Minor:** naloxegol, prucalopride.
- **Bleeding risk** is the main guardrail, particularly when ticagrelor is combined with aspirin or anticoagulants.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and a large Phase 3 trial (CAPTIVA) is testing ticagrelor-containing regimens directly in intracranial atherostenosis. However, results are not yet available, and the intracranial haemorrhage contraindication signal means the benefit-risk balance depends on careful patient selection.

**To proceed, the following is needed:**
- CAPTIVA results, in particular ticagrelor-specific outcomes
- Detailed mechanism of action data
- Label-based warnings and contraindications from the SmPC and BNF
- Confirmation of the MHRA-approved indication text and dosage form for the authorised product
- A bleeding-risk management plan, including exclusion of patients with prior intracranial haemorrhage and review of interacting drugs (e.g. strong CYP3A4 inhibitors such as clarithromycin)

**Other predictions (not recommended at present):** Monckeberg arteriosclerosis, priapism, May-Thurner syndrome, livedo reticularis, mesenteric vascular occlusion, vascular ectasia, angiodysplasia and venous thromboembolism have little or no direct evidence and weak mechanistic rationale. Angiodysplasia is a bleeding lesion, so the prediction conflicts with ticagrelor's pharmacology and raises a safety concern. All are rated **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

