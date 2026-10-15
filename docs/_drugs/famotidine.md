---
layout: default
title: Famotidine
parent: Moderate Evidence (L3-L4)
nav_order: 275
evidence_level: L4
indication_count: 10
---

# Famotidine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Famotidine: From Gastric Ulcer to Duodenogastric Reflux

## One-Sentence Summary

Famotidine is a histamine H2-receptor antagonist, originally used to treat gastric and duodenal ulcers, gastro-oesophageal reflux disease and related acid-driven conditions.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, but only **2 small or indirect publications** and **no registered clinical trials** support this direction.
Several other top-ranked predictions (such as peptic ulcer disease) largely overlap with existing labelled uses and are not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, gastro-oesophageal reflux disease, oesophagitis, dyspepsia, duodenal ulcer, Zollinger-Ellison syndrome (the MHRA licence record compiled for this report contains no indication text) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on established pharmacology, famotidine blocks H2 receptors on gastric parietal cells and reduces gastric acid secretion. Its efficacy in acid-related disease such as ulcers and reflux is well established.

Duodenogastric reflux is the backflow of bile and duodenal contents into the stomach. Acid suppression may ease symptoms or mucosal injury, but it does not correct the underlying motility problem. The mechanistic link is therefore partial and symptomatic, not disease-modifying.

The graph-based prediction probably reflects the close proximity of this condition to ulcer and reflux disease in the knowledge graph. Evidence is thin: one cohort study in critically ill patients and one Russian-language report on early gastroduodenal reflux disease.

**Other predictions in the data (for context):**

| Predicted Indication | Evidence Level | Comment |
|------|------|------|
| Peptic ulcer disease | L1 | Overlaps with the labelled indication; 8 registered trials, several showing famotidine is inferior to pantoprazole for secondary prevention in aspirin or thienopyridine users |
| Gastroduodenitis | L3 | Mostly ulcer-focused evidence overlapping the labelled use |
| Gastrojejunal ulcer | L3 | Famotidine was the comparator in a small Phase 4 trial |
| Peptic ulcer perforation | L3 | Famotidine inferior to pantoprazole for preventing recurrent aspirin-related ulcers; perforation itself is surgical |
| Active peptic ulcer disease | L4 | On-label overlap, not a new indication |
| Multiple endocrine neoplasia | L4 | Indirect; addresses acid hypersecretion in Zollinger-Ellison syndrome only |
| Duodenal obstruction | L5 | No clear mechanistic link |
| Abnormality of glucagon secretion | L5 | No evidence; computational prediction only |
| Acne | L5 | No evidence; computational prediction only |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Cohort | World J Gastroenterol | Investigated the effect of famotidine on gastro-oesophageal and duodeno-gastro-oesophageal reflux in critically ill patients and possible mechanisms |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Review | Eksp Klin Gastroenterol | Famotidine 20 mg twice daily in early-stage gastroduodenal reflux disease, assessed clinically and endoscopically |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103010H0AAAAAA (BNF-style code) | Famotidine tablets 20 mg | Tablet | Not stated in the data compiled for this report |

Famotidine is marketed in the UK, with one valid single-ingredient authorisation recorded. Please check the current SmPC and BNF (section 1.3, antisecretory drugs) for authorised indications and doses.

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** kidney disease and impaired renal function, liver disease, gallbladder disease, nephrolithiasis, hypercalcaemia and related calcium or phosphorus disorders, hyperparathyroidism, sarcoidosis, diarrhoeal disease, constipation, and gastric cancers and neoplasms. These graph associations need verification against the SmPC; in particular, gastric malignancy should be excluded before acid suppression in patients with alarm symptoms.
- **Drug interactions:** 100 interactions were identified, mostly of moderate severity. Examples include abiraterone, acalabrutinib, tramadol, salbutamol, alfuzosin, aminophylline, amiodarone, amisulpride, amitriptyline, apomorphine and aripiprazole. Minor interactions include alendronic acid and aluminium hydroxide.
- **Literature signals:** a case report of delirium after switching from cimetidine to famotidine (PMID 11573854).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The duodenogastric reflux prediction has a high model score but rests on two small or indirect publications and no registered trials. Acid suppression would at most relieve symptoms and does not address the underlying cause. The strongest-scoring evidence in the data (peptic ulcer disease) is on-label use, where famotidine is often inferior to a proton pump inhibitor for secondary prevention.

**To proceed, the following is needed:**
- Controlled clinical studies of famotidine specifically in duodenogastric (bile) reflux, with symptom and endoscopic or histological endpoints
- Comparison against proton pump inhibitors or other standard care
- Detailed mechanism of action data
- Full SmPC warnings and contraindications for the UK-authorised product, including the approved indication text
- Verification of the knowledge-graph contraindications (renal, hepatic and calcium-related conditions) and a dose-adjustment plan for renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

