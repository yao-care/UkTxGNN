---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alteplase: From Acute Thromboembolic Disorders to Posterolateral Myocardial Infarction

## One-Sentence Summary

Alteplase is a recombinant tissue-type plasminogen activator (rt-PA) — a well-established thrombolytic agent with recognised clinical use in acute ischaemic stroke, pulmonary embolism, and ST-elevation myocardial infarction (STEMI); however, no UK marketing authorisation data was captured in this Evidence Pack, likely reflecting a data collection gap rather than genuine non-availability.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction**, a specific anatomical subtype of acute MI arising from occlusion of the right coronary artery or left circumflex branch,
with **0 clinical trials** and **3 publications** currently identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation data captured in this Evidence Pack (likely data collection gap; established clinical uses include acute ischaemic stroke, PE, and STEMI) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| UK Market Status | Not recorded in this Evidence Pack |
| Number of Marketing Authorisations | 0 (per data available; please verify via MHRA register) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Alteplase is a fibrin-specific recombinant tissue plasminogen activator. It binds selectively to fibrin within a thrombus and converts entrapped plasminogen to plasmin, initiating localised clot dissolution with limited systemic proteolytic activity. This mechanism underpins its well-established role in treating occlusive thromboembolic events across multiple vascular territories, including acute ischaemic stroke, massive pulmonary embolism, and STEMI.

Posterolateral myocardial infarction results from occlusion of the right coronary artery (RCA) or left circumflex artery (LCx), generating a coronary thrombus as the primary pathological event — precisely the target substrate for alteplase. The distinguishing feature of posterolateral MI relative to other STEMI subtypes is primarily electrographic (ST elevation in posterior leads V7–V9 rather than standard precordial leads), rather than any fundamental difference in underlying coagulation biology or thrombus composition. Accordingly, the drug–disease mechanistic match is essentially identical to that for anterior or inferior STEMI, where alteplase's benefit is already established. A 1998 diagnostic study (PMID 9502627) further highlights that identifying posterior ST-segment elevation is specifically important for informing thrombolysis decisions in this subgroup.

The TxGNN prediction is therefore mechanistically coherent: the model correctly identifies that alteplase's fibrinolytic mechanism is applicable wherever a fresh fibrin-rich coronary thrombus is present, regardless of the anatomical territory of infarction. The key outstanding scientific question is not whether thrombolysis works in posterolateral MI in principle, but whether outcomes data in this specific anatomical subgroup (which is historically under-represented in landmark thrombolysis trials owing to diagnostic challenges) are equivalent to those in better-studied STEMI populations. Current evidence — three small case reports and one diagnostic study — is insufficient to draw subgroup-specific conclusions.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for Alteplase in posterolateral myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9502627](https://pubmed.ncbi.nlm.nih.gov/9502627/) | 1998 | Diagnostic Study | J Am Coll Cardiol | ST elevation in posterior leads (V7–V9) during acute inferior MI identifies patients with concomitant posterior infarction; study examined whether these patients derive greater benefit from thrombolysis, providing the primary rationale for applying thrombolytics to posterolateral MI |
| [8480981](https://pubmed.ncbi.nlm.nih.gov/8480981/) | 1993 | Case Report | Ann Cardiol Angéiol | Cerebral embolism with rapidly resolving course occurred during late fibrinolysis with tPA in a patient with posterolateral MI; reviews fibrinolytic effects on left intraventricular thrombi during acute MI and highlights systemic embolism risk — a key safety signal for this subtype |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Case Report | Catheter Cardiovasc Interv | Primary PCI of unprotected left main coronary artery in a 37-year-old with posterolateral acute MI and borderline haemodynamic compromise; intracoronary reteplase (a tPA variant) facilitated mini-crush stenting, illustrating use of thrombolytics as an adjunct in high-risk posterolateral MI when anatomy precludes direct PCI |

---

## UK Market Information

No MHRA marketing authorisation records were captured for Alteplase in this Evidence Pack (market status field: not recorded; total licences: 0). This is highly likely to represent a data collection gap in the regulatory pipeline rather than genuine absence from the UK market.

> **Important note for clinicians**: Alteplase (brand name Actilyse®, Boehringer Ingelheim) is understood to hold MHRA marketing authorisation for established thromboembolic indications and is listed in the BNF under fibrinolytic drugs (BNF section: Blood clots > Fibrinolytic drugs). Clinicians should verify current indications, authorised dosing regimens, and any NICE appraisals directly via the [MHRA public register](https://products.mhra.gov.uk/) and the current BNF edition before any clinical application.

---

## Safety Considerations

Please refer to the current Alteplase SmPC and BNF monograph for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (yellowcard.mhra.gov.uk).

Key areas to review in the SmPC before any clinical use include:
- Haemorrhagic risk (intracranial, gastrointestinal, and puncture-site bleeding)
- Contraindications in patients with recent surgery, active bleeding, or uncontrolled hypertension
- Reperfusion arrhythmia monitoring requirements post-thrombolysis
- Interaction with anticoagulants and antiplatelet agents

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for alteplase in posterolateral myocardial infarction is pharmacologically sound — the target pathology (coronary fibrin thrombus) and drug mechanism (selective fibrinolysis) are identical to established STEMI indications — however, available evidence for this specific anatomical subtype comprises only three case reports and one diagnostic study, with no clinical trial data. Until subgroup-specific outcome data become available, a formal recommendation beyond the general STEMI framework cannot be made.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current MHRA marketing authorisation status, approved indications, and SmPC for Alteplase (Actilyse®) via the MHRA public product register
- **Subgroup evidence review**: Commission or identify a systematic review or meta-analysis of thrombolytic outcomes stratified by MI anatomical territory (anterior vs. inferior vs. posterior/posterolateral), using data from landmark trials (GUSTO, TAMI, ISIS-3)
- **Guideline alignment**: Determine whether current ESC or NICE guidance on STEMI management already addresses posterolateral MI as a covered subtype under the general thrombolysis recommendation, which may render a separate "repurposing" pathway unnecessary
- **Safety profile documentation**: Retrieve full SmPC contraindications, warnings, and drug interaction data to complete the safety assessment (currently flagged as a blocking data gap in this Evidence Pack)
- **Mechanism of action data**: Query DrugBank API for DB00009 to formally populate the MOA field and support mechanistic link analysis in future iterations of this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

