---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
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

# Acetylsalicylic Acid: From Cardiovascular Disease Prevention to Migraine with Brainstem Aura

---

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is one of the world's most widely used analgesic and antiplatelet agents, with a well-established role in the primary and secondary prevention of cardiovascular disease.
The TxGNN model predicts it may be effective for **migraine with brainstem aura** (formerly known as basilar-type migraine), with **0 registered clinical trials** and **19 publications** currently supporting this direction.
Whilst no prospective randomised trial exists for this specific migraine subtype, guideline-level evidence and a direct retrospective study provide a meaningful clinical foundation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | UK MHRA licensing data not available in current dataset; aspirin is widely authorised for analgesia, antipyresis, and antiplatelet therapy for cardiovascular prevention |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| UK Market Status | MHRA data pending (data gap; aspirin is widely available in the UK across multiple product licences) |
| Number of Marketing Authorisations | 0 in current dataset (MHRA data collection pending) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acetylsalicylic acid exerts its primary therapeutic effects through irreversible inhibition of cyclooxygenase-1 (COX-1) and COX-2 enzymes, which reduces the synthesis of prostaglandin E₂ (PGE₂) and thromboxane A₂ (TXA₂). This multi-pronged mechanism is directly relevant to migraine pathophysiology through three complementary pathways: (1) **Analgesia** — reducing prostaglandin-mediated sensitisation of the trigeminovascular system; (2) **Antiplatelet effect** — attenuating platelet aggregation and serotonin (5-HT) release during attacks, consistent with the long-established platelet hypothesis of migraine (PMID 2701286); and (3) **Potential modulation of cortical spreading depression (CSD)** — the electrophysiological substrate underlying migraine aura — via COX pathway suppression.

Migraine with brainstem aura (ICHD-3 classification) is characterised by aura symptoms originating from the brainstem or bilateral hemispheres, including dysarthria, diplopia, tinnitus, vertigo, and altered consciousness. A critical clinical consideration is that triptans — the standard acute treatment for most migraine subtypes — carry a relative contraindication in this condition due to theoretical concerns over vasoconstriction in the posterior circulation. This creates a clinically meaningful therapeutic gap that aspirin, as an antiplatelet and anti-inflammatory agent without vasoconstrictive properties, is well-positioned to address.

A retrospective study (PMID 25729594, n=203) directly evaluated low-dose aspirin as prophylactic treatment for migraine with aura, with 46.8% of patients receiving aspirin; clinically relevant efficacy and tolerability were demonstrated. The 2015 American Headache Society evidence assessment (PMID 25600718) classifies aspirin as a Level A option for acute migraine treatment. A 2025 systematic review (PMID 39989443) further evaluates the role of antithrombotic drugs — including aspirin — in migraine prevention, providing contemporary mechanistic context. A double-blind RCT (PMID 10448545) comparing intravenous lysine acetylsalicylate against subcutaneous sumatriptan in acute migraine (n=278) demonstrated comparable efficacy, providing direct interventional evidence for aspirin in migraine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acetylsalicylic acid in migraine with brainstem aura on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Study | Current Health Sciences Journal | Low-dose aspirin (ASA) evaluated for prophylaxis of migraine with aura (n=203, ICHD-II criteria); 46.8% received ASA — most directly relevant study for this indication |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Clinical Guideline | Headache | AHS evidence assessment of acute migraine pharmacotherapies; aspirin classified as Level A (established efficacy) for acute migraine treatment |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Systematic review exploring the role of antithrombotic drugs (including aspirin) as migraine preventive medication |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | Cephalalgia | Double-blind, double-dummy RCT (n=278, 17 centres): IV lysine acetylsalicylate (equivalent to 1 g ASA) vs subcutaneous sumatriptan 6 mg in acute migraine with or without aura — demonstrated comparable efficacy |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Narrative Review | Revue Neurologique | Comprehensive review of migraine with aura; cortical spreading depression as core mechanism; diagnosis per ICHD-III criteria and treatment overview |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Comparison of migraine with and without aura — pathophysiology, risk stratification, and management implications including antiplatelet approaches |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Clinical Guideline | FP Essentials | AHA/ASA stroke primary prevention guidelines; aspirin's role in vascular risk reduction is directly relevant to brainstem aura subtype given its stroke risk association |
| [2701286](https://pubmed.ncbi.nlm.nih.gov/2701286/) | 1989 | Review | Biomedecine & Pharmacotherapie | Platelet hypothesis of migraine (10-year review); mechanistic foundation for antiplatelet therapy in migraine pathogenesis |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | Heart | Clopidogrel reduces migraine with aura following transcatheter atrial shunt closure; antiplatelet mechanism confirmed in migraine with aura context |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Ubrogepant for acute migraine; contextualises aspirin and caffeine-containing analgesics as established first-line options for mild-to-moderate migraine |

---

## UK Market Information

The current evidence pack does not contain MHRA marketing authorisation data for acetylsalicylic acid (known data gap). In practice, aspirin holds numerous product licences in the UK across multiple manufacturers and formulations, including:

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|-------------------|
| MHRA data pending | Aspirin (various manufacturers) | Tablet / Dispersible tablet | Analgesia, antipyresis, antiplatelet therapy for cardiovascular prevention |

Clinicians are advised to consult the MHRA product licence database and the **British National Formulary (BNF)** — Chapter 4.7 (Analgesics) and Chapter 2.9 (Antiplatelet drugs) — for current authorised indications and SmPC information. NICE guidance on antiplatelet therapy (e.g., CG172, NG185) should also be reviewed for relevant cardiovascular indications.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

> **Note for clinical use in migraine with brainstem aura:** Clinicians should be aware that aspirin is contraindicated in children under 16 years of age (risk of Reye's syndrome), and that gastrointestinal tolerability (particularly in long-term or prophylactic dosing) should be assessed. The relative contraindication of triptans in brainstem aura makes aspirin a clinically important alternative, but this should be balanced against individual bleeding risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aspirin has a well-established mechanistic basis for migraine management (COX inhibition, antiplatelet activity, CSD modulation), is supported by guideline-level evidence (AHS 2015, Level A), and has direct retrospective evidence for migraine with aura prophylaxis. The relative contraindication of triptans in brainstem aura specifically strengthens the clinical argument for aspirin in this subtype. However, evidence is extrapolated from broader migraine with aura populations rather than prospective trials in ICHD-3–defined brainstem aura, warranting caution in formal indication expansion.

**To proceed, the following is needed:**

- Prospective randomised controlled trial or high-quality observational study specifically enrolling patients with ICHD-3–defined migraine with brainstem aura
- Resolution of MHRA data gap: retrieve current UK product licences, approved indications, and SmPC (resolve DG001)
- Full mechanism of action data confirming COX pathway relevance to brainstem aura (resolve DG002)
- Drug interaction (DDI) profile and complete contraindication list for this patient population
- Risk stratification framework for antiplatelet therapy in migraine patients (bleeding risk, renal function, concomitant NSAIDs, gastroprotection requirements)
- Assessment of whether existing UK off-label use data or NICE guidance supports this repurposing pathway without a full new regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

