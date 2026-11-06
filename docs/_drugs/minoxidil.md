---
layout: default
title: Minoxidil
parent: Model Prediction Only (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
monitor_inn: "Minoxidil"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pseudopelade of Brocq", "pulmonary arterial hypertension", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "primary hereditary glaucoma", "pulmonary arterial hypertension associated with chronic hemolytic anemia", "pulmonary arterial hypertension associated with connective tissue disease"]
last_modified_at: 2026-11-06
description: "Minoxidil: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension and alopecia"
---

# Minoxidil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Minoxidil: From Hypertension to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Minoxidil is a vasodilator, with hypertension and hair loss (alopecia) recorded as its original uses in the knowledge graph.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a rare hereditary hair loss disorder.
Evidence is limited to **3 small case-level reports** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and alopecia (relations recorded in the knowledge graph; the UK licence record contains no indication text) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (17 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 17 |
| Recommended Decision | Hold |

The three reports on hypotrichosis simplex are case reports or case-level combination-therapy studies. They would otherwise suggest L3, but the rules do not allow L1 to L4 here: the data compiled for this report contains no clinical trial and no controlled or observational study directly assessing minoxidil alone for this disease. I have therefore assigned L5 and treated the case reports as supportive anecdotes.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature retrieved, minoxidil is a potassium channel opener. Its active metabolite, minoxidil sulfate, relaxes vascular smooth muscle, which explains its blood-pressure-lowering effect. In hair follicles it is thought to prolong the anagen (growth) phase, enlarge follicles and act on dermal papilla cells.

Hypotrichosis simplex of the scalp is a hereditary disorder with reduced hair density, so a drug that stimulates follicle growth is plausible. The score of 1.0000 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

An important caveat is that all three retrieved reports used minoxidil together with other treatments (growth factors, botanic extracts, or platelet-rich plasma). The contribution of minoxidil alone cannot be separated out.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case report/series | Dermatologic Therapy | Hereditary hypotrichosis simplex of the scalp treated with oral minoxidil plus growth factors |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case report (combination therapy) | Frontiers in Genetics | An 8-year-old boy with CDSN-variant disease treated with botanic extracts plus minoxidil |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case report | Journal of Dermatological Treatment | A 14-year-old patient treated with platelet-rich plasma injection plus topical minoxidil 2%, described as successful |

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0205010N0AAACAC | Minoxidil 10mg tablets | Minoxidil |
| 1309000H0AAAKAK | Minoxidil 2% gel | Minoxidil |
| 1309000H0AAAAAA | Minoxidil 2% solution | Minoxidil |
| 0205010N0AAAAAA | Minoxidil 2.5mg tablets | Minoxidil |
| 1309000H0AAALAL | Minoxidil 5% foam | Minoxidil |
| 1309000H0AAAJAJ | Minoxidil 5% solution | Minoxidil |
| 0205010N0AAABAB | Minoxidil 5mg tablets | Minoxidil |
| 1309000H0BCAAAA | Boots Hair Loss Treatment Regular Strength 2% solution | Minoxidil |
| 0205010N0BBACAC | Loniten 10mg tablets | Minoxidil |
| 0205010N0BBAAAA | Loniten 2.5mg tablets | Minoxidil |
| 0205010N0BBABAB | Loniten 5mg tablets | Minoxidil |
| 1309000H0BBAFAK | Regaine for Men 2% gel | Minoxidil |
| 1309000H0BBAGAL | Regaine for Men Extra Strength 5% scalp foam | Minoxidil |
| 1309000H0BBABAJ | Regaine for Men Extra Strength 5% scalp solution | Minoxidil |
| 1309000H0BBAAAA | Regaine for Men Regular Strength 2% solution | Minoxidil |
| 1309000H0BBAHAL | Regaine for Women Once a Day 5% scalp foam | Minoxidil |
| 1309000H0BBADAA | Regaine for Women Regular Strength 2% solution | Minoxidil |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

This is the only record found (a single-ingredient product), and it is identified by a BNF-style code rather than a PL number.

---

## Safety Considerations

**Contraindications recorded in the knowledge graph** (disease relations, not label text) include:
- Cardiovascular: myocardial infarction, coronary thrombosis, heart disease, cardiovascular disease, stroke and cerebrovascular disorders, cerebral infarction
- Pericardial: pericarditis, pericardial effusion, haemopericardium, cardiac tamponade
- Blood pressure and autonomic: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- Tumours: phaeochromocytoma and related tumours (adrenal, sympathetic paraganglioma)
- Other: kidney disease, haemoglobinopathy, scalp dermatosis

**Drug interactions** (DDInter, 100 recorded in total; examples at Moderate level):
- Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
- Others: bupropion, morphine, opium, dronabinol, nabilone, sapropterin

Package-insert warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the supporting evidence is three small case-level reports, all using minoxidil in combination with other treatments, and there are no registered trials. The knowledge graph also lists many cardiovascular and pericardial contraindications, which matter for any oral use.

**To proceed, the following is needed:**
- Controlled or observational studies assessing minoxidil alone in hypotrichosis simplex of the scalp
- Mechanism of action data and SmPC warnings and contraindications
- A UK licence record with indication text, and a decision on route (topical versus low-dose oral)
- A cardiovascular safety plan if oral minoxidil is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

