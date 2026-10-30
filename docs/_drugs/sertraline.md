---
layout: default
title: Sertraline
parent: Model Prediction Only (L5)
nav_order: 567
evidence_level: L5
indication_count: 8
monitor_inn: "Sertraline"
predicted_indications: ["histrionic personality disorder (disease)", "paranoid personality disorder", "schizotypal personality disorder", "schizoid personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "dependent personality disorder", "narcissistic personality disorder"]
last_modified_at: 2026-10-30
description: "Sertraline: predicted new indication Histrionic personality disorder (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Sertraline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Sertraline: Histrionic personality disorder (disease)
{: .text-alpha }

## One-Sentence Summary

Sertraline is an antidepressant of the selective serotonin reuptake inhibitor (SSRI) class.
The TxGNN model predicts it may be effective for **histrionic personality disorder**, but there are currently **no clinical trials and no publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Histrionic personality disorder (disease) |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mechanistically, it may be applicable to personality-disorder traits such as affective instability, anxiety or impulsivity.

Histrionic personality disorder is a psychiatric condition that often co-occurs with mood and anxiety disorders. The prediction probably reflects network proximity to the conditions sertraline is already linked with. No study in the data compiled for this report tests sertraline in histrionic personality disorder, so the link remains hypothetical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name |
|---------|------|
| 0403030Q0AAAAAA | Sertraline HCl_Tab 50mg |

This is a single-ingredient product with valid status. Dosage form and approved indication text are not available in the compiled record, so it cannot be used to confirm any approved indication. The listed identifier is not in the usual PL number format, so verify it against the MHRA register. It resembles a BNF-style product code (BNF section 4.3.3, selective serotonin re-uptake inhibitors).

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (not label text): epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis and serotonin syndrome.
- **Drug Interactions**: 100 interactions are recorded. Major-severity examples include bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and phentermine. Moderate-severity examples include aspirin, morphine, clarithromycin, famotidine and loperamide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a computational prediction only. There are no trials or publications for histrionic personality disorder, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or observational data directly studying sertraline in histrionic personality disorder
- Mechanism of action data to support a mechanistic link
- Label-based warnings and contraindications from the SmPC and BNF
- Licensed indication and dosage form details for the UK authorisation
- Review of the interaction burden and of the knowledge-graph contraindication signals (for example bipolar disorder and serotonin syndrome) before any use outside current indications

**Note on other predictions:** In the same data set, agoraphobia (rank 6) has considerably more supporting literature, mainly sertraline studies in panic disorder with or without agoraphobia. It would be a more evidence-supported candidate to evaluate separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

