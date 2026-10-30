---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 130
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Captopril: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension, hypertensive disorder and diabetic nephropathy"
monitor_inn: "Captopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Captopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Captopril: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Captopril is an ACE inhibitor originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but there are **no registered clinical trials** and only **1 publication** (a diagnostic case report) bearing on this prediction, so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder and diabetic nephropathy (the UK licence record contains no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, captopril inhibits angiotensin-converting enzyme (ACE), reducing angiotensin II formation and blocking the renin-angiotensin-aldosterone system (RAAS). Its efficacy in hypertension and diabetic nephropathy is established.

Malignant hypertension with renal involvement is a state in which RAAS activation can drive vascular injury, so RAAS blockade is biologically plausible. However, the only retrieved publication is a case report in which captopril renography was used as a *diagnostic* test in a patient with a renal cell carcinoma. It shows no therapeutic benefit. The high TxGNN score probably reflects the disease's closeness to existing hypertension and renal indications rather than direct evidence.

There is also a safety caveat. In malignant hypertension with bilateral renal artery stenosis, ACE inhibitors can precipitate acute kidney injury.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | Positive captopril renography in a patient with a large chromophobe renal cell carcinoma but intact renal arteries. Renin-dependent hypertension resolved after nephrectomy. This is a diagnostic use, not treatment evidence. |

### Related Predictions Considered

Three other predicted indications were assessed. None has enough evidence to support progression.

- **Malignant renovascular hypertension** (score 0.9928, L4): The mechanistic rationale is strong because the condition is renin-dependent. One 1984 clinical report describes captopril in stable and malignant hypertension ([PMID 6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/)). The rest of the literature is mostly case reports, reviews and diagnostic papers. One case report ([PMID 6321850](https://pubmed.ncbi.nlm.nih.gov/6321850/)) described acute, reversible renal failure after captopril and enalapril in a patient with bilateral renal artery occlusion. This is the most plausible research question of the group, but study types were classified from titles only and are tentative.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 0.9915, L5): Only preclinical and indirect findings were retrieved, and most of the retrieved papers appear unrelated. Systemic vasodilators can also worsen ventilation-perfusion matching in hypoxic lung disease.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 0.9915, L5): No trials or literature. ACE inhibitors are not an established therapy for pulmonary arterial hypertension.

## UK Market Information

One marketing authorisation record is held, but it carries no dosage form, manufacturer or approved indication text.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051F0AAADAD | Captopril Tablets 12.5 mg | Tablet | Not stated in the available record |

## Safety Considerations

**Contraindications and cautions from the drug–disease knowledge graph** (these are model-derived associations, not label text):
- Renal and hepatic: kidney disease, liver disease, hepatic encephalopathy and coma, pancreatitis, gallbladder disease
- Angioedema of all types, including hereditary and ACE-inhibitor-related forms
- Haematological: neutropenia, agranulocytosis
- Cardiovascular: aortic stenosis and related valve disease, hypotensive disorders
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperparathyroidism, hyperuricaemia
- Connective tissue disease and systemic lupus erythematosus

**Drug Interactions:** 100 interactions were found. The sample reviewed shows mainly Moderate-level interactions with:
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
- Antidiabetic agents (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide)
- Others: bupropion, morphine, acetylsalicylic acid, dronabinol

Minor interactions were noted with aluminium hydroxide and calcium carbonate.

Please also refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model proximity and a single diagnostic case report, with no trials and no therapeutic evidence in malignant hypertensive renal disease. A renal safety concern (acute kidney injury with bilateral renal artery stenosis) also applies.

**To proceed, the following is needed:**
- Therapeutic (not diagnostic) clinical data in malignant hypertensive renal disease, for example a systematic review of ACE inhibitor use in malignant hypertension
- Mechanism of action data and UK label information (SmPC warnings, contraindications, indication text), which are missing from the data compiled for this report
- A renal safety monitoring plan, including exclusion or careful assessment of renal artery stenosis
- If a further direction is wanted, review malignant renovascular hypertension as a research question first, using full-text assessment of the retrieved papers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

