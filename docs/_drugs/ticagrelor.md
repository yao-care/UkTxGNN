---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 616
evidence_level: L5
indication_count: 9
monitor_inn: "Ticagrelor"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "fibrocartilaginous embolism"]
last_modified_at: 2026-10-23
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Acute coronary syndrome"
---

# Ticagrelor
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

## Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis
{: .text-alpha }

## One-Sentence Summary

Ticagrelor is an oral antiplatelet medicine, recorded in the knowledge graph as being used for acute coronary syndrome and peripheral arterial disease.
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**, with **2 clinical trials** (one large Phase 3 trial that is still ongoing) and **2 publications** directly addressing this condition.
None of these studies has yet reported results showing that ticagrelor works in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (relation recorded in the knowledge graph; no approved indication text is available in the UK licence data compiled for this report) |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

**Note on the evidence level.** The data compiled for this report scored this prediction as L1. That score does not hold up. The only Phase 3 trial directly studying intracranial atherosclerosis (CAPTIVA) is still ongoing and has no results. The other directly relevant trial is a small, non-phased pilot study. The directly relevant literature consists of a single-centre cohort study and a trial design paper. No completed Phase 3 RCT in this disease has been cited. A strict reading of the evidence rules therefore places this at **L5**, with the strongest signal being an ongoing Phase 3 trial. The larger body of RCT evidence for ticagrelor relates to coronary and other ischaemic disease, not to this prediction. I have also moved the recommendation from "Proceed with Guardrails" to "Hold" until results are available.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a reversible P2Y12 receptor antagonist. It blocks ADP-mediated platelet activation and aggregation, which reduces the formation of clots in arteries.

Symptomatic intracranial atherosclerotic stenosis is driven largely by platelet-mediated thrombosis and by emboli breaking off from narrowed arteries. Blocking platelet activation is therefore mechanistically plausible. Ticagrelor's activity does not depend on CYP2C19 activation, unlike clopidogrel. This may matter in populations with a high frequency of CYP2C19 loss-of-function variants, including many East Asian patients. The main trade-off is bleeding, and intracranial haemorrhage is a particular concern in this setting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Phase 3 | Active, not recruiting | 1683 | Tests whether rivaroxaban, ticagrelor or both are superior to clopidogrel for lowering 1-year ischaemic stroke, intracerebral haemorrhage or vascular death in intracranial atherosclerotic stenosis. No results yet. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | Not applicable | Recruiting | 100 | Pilot trial of genotype-guided P2Y12 inhibitor selection (including ticagrelor) versus clopidogrel in symptomatic intracranial atherosclerotic disease. No results yet. |

Many other ticagrelor trials exist in coronary artery disease and acute coronary syndrome. They do not address the predicted indication and are not listed here.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | J Neurointerv Surg | Experience with ticagrelor 60 mg twice daily plus aspirin versus standard aspirin and clopidogrel for intracranial stenting. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial design paper | Int J Stroke | Describes the design and early progress of the CAPTIVA trial, which compares other dual antithrombotic regimens with clopidogrel plus aspirin. |

Related evidence in stroke more broadly (not specific to intracranial atherosclerosis) includes [34708996](https://pubmed.ncbi.nlm.nih.gov/34708996/) (NEJM 2021, RCT of ticagrelor versus clopidogrel in CYP2C19 loss-of-function carriers with stroke or TIA). It supports the general plausibility of the approach but does not study this disease directly.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0209000Z0AAAAAA | Ticagrelor tablet 90 mg | Tablet | Not stated in the data compiled for this report |

Only one single-ingredient authorisation is listed in the compiled data, and it carries no indication text. Please check the current SmPC, the BNF (antiplatelet drugs, cardiovascular system chapter) and any NICE guidance for the licensed indications.

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (not label text): liver failure, liver disease, gallbladder disease and intracranial haemorrhage. The last is especially important for a prediction in cerebrovascular disease.
- **Drug interactions** (100 recorded; examples from the compiled list):
  - **Major:** clarithromycin.
  - **Moderate:** acetylsalicylic acid (aspirin), morphine, simvastatin, dexamethasone, budesonide, aprepitant, saxagliptin, rolapitant, miconazole and others.
  - **Minor:** naloxegol, prucalopride.

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and a large Phase 3 trial (CAPTIVA) is under way. However, no completed study has shown benefit or acceptable safety of ticagrelor in intracranial atherosclerosis, and the bleeding risk (including intracranial haemorrhage) is a real concern. Evidence strength is therefore L5 for this specific indication.

**To proceed, the following is needed:**
- CAPTIVA results, particularly the ticagrelor arm's rates of ischaemic stroke and intracerebral haemorrhage compared with clopidogrel
- Results from the genotype-guided pilot trial and larger cohort data in intracranial stenting
- Mechanism of action data and label-based warnings and contraindications to complete safety screening
- Confirmation of the licensed indications on the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

