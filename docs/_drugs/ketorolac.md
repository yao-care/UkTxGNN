---
layout: default
title: Ketorolac
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Ketorolac: predicted new indication Headache disorder (evidence level L5). Approved use: Atopic, papillary and vernal conjunctivitis"
---

# Ketorolac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Ketorolac: From Allergic Conjunctival Conditions to Headache Disorder

## One-Sentence Summary

Ketorolac is a non-steroidal anti-inflammatory drug (NSAID), originally associated with allergic and inflammatory conjunctival conditions (atopic, papillary and vernal conjunctivitis).
The TxGNN model predicts it may be effective for **headache disorder** (chiefly migraine and tension-type headache),
with **17 clinical trials** and **19 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic, papillary and vernal conjunctivitis (from the TxGNN knowledge graph; no approved indication text is available for the UK authorisations) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L1 (see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 3 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Several completed Phase 3/4 trials and multiple systematic reviews and meta-analyses exist. However, most of the compiled trials are small, are paediatric or emergency-department studies, and use parenteral or intranasal ketorolac rather than the oral or ophthalmic products authorised here. The L1 grade should be read with that caveat.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, ketorolac is a non-selective COX-1/COX-2 inhibitor. By reducing prostaglandin synthesis, it dampens peripheral and central sensitisation and neurogenic inflammation, both of which contribute to migraine and tension-type headache pain.

Its original conjunctival indications also rest on prostaglandin-driven inflammation, so the same anti-inflammatory action links the old and new indications. Parenteral ketorolac is already used in emergency department headache care, and this supports the biological plausibility of the prediction.

Two other predictions were generated, but they are much weaker:
- **Rosacea conjunctivitis** (score 99.40%): no trials or literature were found, so this remains speculative (Evidence Level L5, Hold).
- **Trigeminal autonomic cephalalgia** (score 99.39%): evidence is indirect, one related trial was withdrawn with no enrolment, and cluster headache generally responds poorly to standard NSAIDs (Evidence Level L4, Research Question).

## Clinical Trial Evidence

The table shows the 10 most relevant of the 17 trials, prioritising direct ketorolac studies that were completed.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Double-blind, placebo-controlled study of intranasal ketorolac for acute migraine |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | IV valproate vs IV metoclopramide vs IV ketorolac for acute migraine |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Metoclopramide/diphenhydramine vs ketorolac alone for tension-type headache |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | IV ketorolac plus metoclopramide for paediatric migraine in the emergency department |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Intranasal vs IV ketorolac for paediatric migraine (non-inferiority) |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs ketorolac for tension-type headache |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Terminated | 41 | Intranasal ketorolac plus oral adjuncts vs IV ketorolac for paediatric migraine |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | Intranasal ketamine vs standard therapy for primary headache in the emergency department |
| [NCT02681211](https://clinicaltrials.gov/study/NCT02681211) | Not applicable | Unknown | 80 | Auricular acupuncture vs IV migraine medications for paediatric status migrainosus |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systematic review/meta-analysis | Acad Emerg Med | Efficacy of parenteral ketorolac in acute migraine |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systematic review/meta-analysis | Adv Clin Exp Med | IV ketorolac vs metoclopramide in adult migraine |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Systematic review | Headache | Effectiveness of parenteral ketorolac in acute migraine; conflicting evidence noted |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 American Headache Society update on parenteral treatments for acute migraine in the emergency department |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/evidence assessment | Headache | American Headache Society assessment of acute migraine pharmacotherapies |
| [34822214](https://pubmed.ncbi.nlm.nih.gov/34822214/) | 2022 | RCT | Acad Emerg Med | Intranasal vs IV ketorolac for migraine in children |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | IV metoclopramide alone vs with added ketorolac in paediatric migraine |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurol Sci | IV dexamethasone, metoclopramide, ketorolac and chlorpromazine compared for migraine pain relief |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Systematic review | Headache | Parenteral treatment of episodic tension-type headache |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | IM ketorolac vs meperidine and hydroxyzine in acute migraine |

## UK Market Information

The three authorisations below are listed in the data compiled for this report. No dosage form, manufacturer or approved indication text is available for them, and the identifiers shown are not in the standard UK "PL" format, so they should be verified against the MHRA register.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1501042E0BBACAC | Toradol Oral Tab 10mg | Oral tablet (per product name) | Not available |
| 110802070BBAAAA | Acular Ophth Soln 0.5% | Ophthalmic solution (per product name) | Not available |
| 110802070AAAAAA | Ketorolac Trometamol Eye Drops 0.5% | Eye drops (per product name) | Not available |

Most of the supporting headache evidence concerns parenteral and intranasal ketorolac. The authorised products listed here are oral and ophthalmic, so route compatibility with the predicted indication has not been established.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease links, not from label text, so they must be confirmed against the SmPC):
- Cardiovascular and cerebrovascular: hypertension, heart disease and cardiovascular disease, myocardial infarction, coronary thrombosis, stroke, cerebral infarction
- Gastrointestinal: active peptic ulcer disease, gastric ulcer, inflammatory bowel disease
- Bleeding and haematological: blood coagulation disorders, haemophilia, anaemia, haemoglobinopathy
- Renal and hepatic: impaired renal function, liver disease, gallbladder disease
- Respiratory: asthma (including allergic and intrinsic asthma)
- Metabolic and other: diabetes mellitus, diabetic ketoacidosis, rheumatoid arthritis
- Ocular: dry eye syndrome

**Drug interactions:** 222 interactions are recorded. Examples of those listed:
- **Major:** acetylsalicylic acid
- **Moderate:** corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide), exenatide, levofloxacin, kanamycin, balsalazide, fenfluramine and dexfenfluramine
- **Minor:** H2 blockers (famotidine, ranitidine, cimetidine), linaclotide

A published case report also describes lithium toxicity when ketorolac was co-administered with lithium.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 to 4 trials, systematic reviews and guideline assessments support parenteral and intranasal ketorolac in acute migraine and tension-type headache. However, the evidence concerns routes and settings that differ from the oral and ophthalmic products authorised in the UK, and the safety profile in this population needs careful control.

**To proceed, the following is needed:**
- Confirmation of the approved indications and SmPC warnings and contraindications for the UK products, as these were not available for this report
- A decision on route and formulation, since the headache evidence is mainly for IV, IM and intranasal use
- Review of UK guidance (NICE and BNF) on NSAID use in migraine and tension-type headache
- Detailed mechanism of action data from DrugBank
- A safety monitoring plan covering gastrointestinal, renal and cardiovascular risks, bleeding risk and interacting medicines (especially aspirin, other NSAIDs, corticosteroids and lithium)
- Evidence for the lower-ranked predictions (rosacea conjunctivitis and trigeminal autonomic cephalalgia) before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

