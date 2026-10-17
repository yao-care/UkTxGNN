---
layout: default
title: Acetylsalicylic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 19
evidence_level: L3
indication_count: 9
last_modified_at: 2026-10-15
description: "Acetylsalicylic Acid: predicted new indication Migraine with brainstem aura (evidence level L3). Approved use: Rheumatoid arthritis, migraine, myocardial infarction…"
monitor_inn: "Acetylsalicylic acid"
predicted_indications: ["migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
---

# Acetylsalicylic Acid
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

# Aspirin (Acetylsalicylic Acid): From Rheumatoid Arthritis and Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is an established analgesic and antiplatelet drug, used for conditions including rheumatoid arthritis, migraine, headache disorders, osteoarthritis and myocardial infarction.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but **no clinical trials** are registered for this exact subtype. Support comes from **20 publications**, which mostly concern migraine with aura in general.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, migraine, myocardial infarction, headache disorders, osteoarthritis (from the knowledge-graph indication list; the UK authorisation record contains no indication text) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, aspirin inhibits cyclooxygenase (COX), reducing prostaglandin-mediated neurogenic inflammation and pain. It also irreversibly inhibits platelet aggregation.

Aspirin is already used in acute migraine treatment, so the new indication is closely related to the original one. Published work suggests several routes by which it might help in migraine with aura:

- **Anti-inflammatory and analgesic action** through COX inhibition.
- **Antiplatelet effects**, which are relevant to the microembolic and patent foramen ovale (PFO) hypothesis of aura.
- **Modulation of brainstem antinociceptive reflexes**, observed in a randomised crossover study (PMID 1589237).

An important caveat is that no evidence specific to the brainstem aura subtype was found. The supporting data concern migraine with aura in general, so the prediction should be treated as a research question rather than an established use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic review | Headache | Examines the role of antithrombotic drugs in migraine prevention |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective cohort | Curr Health Sci J | Low-dose aspirin for prophylaxis of migraine with aura; 203 patients, 95 on aspirin versus other prophylaxis |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | Cephalalgia | IV aspirin lysinate versus subcutaneous sumatriptan and placebo in acute migraine (278 patients) |
| [19708964](https://pubmed.ncbi.nlm.nih.gov/19708964/) | 2009 | Guideline | Eur J Neurol | Revised EFNS guideline on drug treatment of migraine |
| [16796580](https://pubmed.ncbi.nlm.nih.gov/16796580/) | 2006 | Guideline | Eur J Neurol | EFNS guideline on drug treatment of migraine |
| [9606899](https://pubmed.ncbi.nlm.nih.gov/9606899/) | 1998 | Clinical study | Zh Nevrol Psikhiatr | Aspirin at 1000, 500 and 100 mg as preventive therapy in 105 patients with migraine without aura |
| [1589237](https://pubmed.ncbi.nlm.nih.gov/1589237/) | 1992 | Mechanistic RCT (crossover) | Pain | Aspirin activated antinociceptive brainstem reflex activity in headache patients and healthy subjects |
| [15265054](https://pubmed.ncbi.nlm.nih.gov/15265054/) | 2004 | Mechanistic | Cephalalgia | IV aspirin and zolmitriptan affect trigeminal pain processing differently during and between attacks |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT (PFO closure, not aspirin) | Eur Heart J | PFO closure in migraine with aura; relevant to the PFO hypothesis but does not test aspirin |
| [7907982](https://pubmed.ncbi.nlm.nih.gov/7907982/) | 1994 | Preclinical | Eur Neurol | Anti-migraine compounds failed to modulate cortical spreading depression in the cat |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0209000A0AAAJAJ | Aspirin Tab 75 mg | Not specified | Not specified |

Only one authorisation record is available, and its dosage form and indication text are missing. The record's number format does not follow the usual MHRA "PL" format, so it should be verified. Please check current MHRA authorisations, NICE guidance and the BNF for the full range of licensed aspirin products and indications.

---

## Safety Considerations

**Drug Interactions** (100 interactions were identified; the main ones from the data reviewed are listed below):

- **Major:** acalabrutinib, acetazolamide, ketorolac, ibuprofen, fondaparinux, trastuzumab emtansine
- **Moderate:** abciximab, nifedipine, hydrocortisone, ethanol, alendronic acid, fluvoxamine, fosinopril, gemifloxacin
- **Minor:** acebutolol, caffeine, rabeprazole, fosphenytoin, furosemide

Many of these combinations raise bleeding risk or gastrointestinal risk, and this should be assessed before any prophylactic use.

Bleeding risk is also highlighted in the literature as a general safety consideration for aspirin.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aspirin is already used for acute migraine, and a retrospective study and a 2025 systematic review support a possible prophylactic role in migraine with aura. However, there is no trial or literature specific to brainstem aura, and the available evidence is observational or mechanistic (L3). It is therefore best treated as a research question.

**To proceed, the following is needed:**
- Prospective, ideally randomised, trials of low-dose aspirin in migraine with aura, with brainstem aura subtype analysis
- Detailed mechanism of action data
- Full UK licensing, indication and dosage-form details, and SmPC and BNF warnings and contraindications
- A bleeding-risk and interaction management plan, particularly for patients taking anticoagulants, NSAIDs or other antiplatelet agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

