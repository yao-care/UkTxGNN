---
layout: default
title: Trihexyphenidyl
parent: Model Prediction Only (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
description: "Trihexyphenidyl: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Trihexyphenidyl
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

## Trihexyphenidyl: Attention deficit-hyperactivity disorder
{: .text-alpha }

## One-Sentence Summary

Trihexyphenidyl is a central anticholinergic (muscarinic antagonist) originally used to treat Parkinson disease and related parkinsonian and dystonic movement disorders.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are **no registered clinical trials** and only **1 loosely related publication** (a cohort study on tics with dystonia, not ADHD treatment), so this is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, trihexyphenidyl is a centrally acting muscarinic (M1-preferring) antagonist. It is thought to restore the balance between cholinergic and dopaminergic signalling in the striatum, which underlies its benefit in parkinsonism and dystonia.

ADHD is associated with dysregulation of both dopaminergic and cholinergic signalling, so a mechanistic link is conceivable. However, this rationale is speculative. The only retrieved paper describes tics associated with dystonia, a related movement phenotype, and does not test trihexyphenidyl in ADHD.

There is also a plausible counter-argument: anticholinergic drugs can cause memory impairment and confusion, which may worsen attention in people with ADHD. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Cohort | Movement Disorders | Clinical series describing patients with primary tic disorder and persistent dystonia; it characterises the syndrome and does not evaluate ADHD treatment |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409020C0AAADAD | Trihexyphenidyl HCl Tablets 2 mg | Tablet (not specified in the data) | Not specified in the data compiled for this report |

The marketing authorisation number above is as recorded in the compiled data and does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register. Please consult the BNF (antimuscarinic drugs used in parkinsonism) and the current SmPC for licensed indications.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (derived from drug-disease relationships, not from product label text, and to be confirmed against the SmPC):
- **Eye:** open-angle glaucoma, angle-closure (closed-angle) glaucoma
- **Gastrointestinal:** paralytic ileus, achalasia and megaesophagus, hiatus hernia, ulcerative colitis and inflammatory bowel disease, *Clostridium difficile* colitis, necrotizing enterocolitis, gastric ulcer
- **Genitourinary:** benign prostatic hyperplasia, kidney disease
- **Cardiovascular and respiratory:** hypertension, hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest, chronic obstructive pulmonary disease
- **Neuromuscular:** myasthenia gravis and other neuromuscular junction disease
- **Other:** liver disease, gallbladder disease

**Drug interactions:** 100 interactions were identified. The two **Major** interactions in the data reviewed are with **potassium chloride** and **potassium citrate** (relevant to gastrointestinal injury with reduced gut motility). Many **Moderate** interactions involve other anticholinergic or gut-slowing agents, including hyoscyamine, atropine, glycopyrronium, dicyclomine, scopolamine, trospium, propantheline, loperamide, morphine, and metoclopramide. Additive anticholinergic effects are the main concern.

**Relevant to the predicted indication:** anticholinergic cognitive effects (memory impairment, confusion) may worsen attention.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone. There are no clinical trials and no direct literature for ADHD, and the anticholinergic cognitive effects could be counterproductive in this population.

**To proceed, the following is needed:**
- Retrieval of the full MHRA SmPC and BNF safety data (warnings and contraindications), as the label-based safety data are currently missing
- Detailed mechanism of action data
- Preclinical or clinical evidence that muscarinic antagonism improves ADHD symptoms without worsening cognition
- Verification of the UK marketing authorisation details (number, dosage form, licensed indication)
- Note: among the other predictions, **PLA2G6-associated neurodegeneration** (L4, "Research Question") has the most plausible symptomatic link, given its overlap with parkinsonism and dystonia. It is supported only by a single case report, so any benefit would be symptomatic rather than disease-modifying.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

