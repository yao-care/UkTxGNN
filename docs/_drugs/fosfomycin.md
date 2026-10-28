---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 306
evidence_level: L5
indication_count: 8
monitor_inn: "fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-23
description: "Fosfomycin: predicted new indication Uterine inflammatory disease (evidence level L5). Approved use: Urinary tract infection"
---

# Fosfomycin
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

## Fosfomycin: From Urinary Tract Infection to Uterine Inflammatory Disease
{: .text-alpha }

## One-Sentence Summary

Fosfomycin is an antibiotic whose recorded use in the knowledge graph is urinary tract infection, and the UK data lists it as a 3 g sachet of fosfomycin trometamol. The TxGNN model predicts it may be useful for **uterine inflammatory disease**, but only **2 clinical trials** and **1 publication** were retrieved, and none of them studies this disease directly. The evidence is therefore weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (relation recorded in the knowledge graph; no licence indication text was available) |
| Predicted New Indication | Uterine inflammatory disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Fosfomycin is generally understood to inhibit MurA, an enzyme in the early steps of bacterial cell wall (peptidoglycan) synthesis. It is active against many common urinary pathogens.

The link to the predicted indication is plausible but indirect. Uterine and pelvic infections can involve bacteria from the genitourinary tract, so an antibiotic active against those organisms could in principle help. The model's high score probably reflects this overlap between urinary and genitourinary conditions.

The supporting material does not test this idea. The two trials are general paediatric pharmacokinetic studies, and the one paper concerns cystitis in women with endometriosis, which is a urinary condition rather than a uterine one. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pharmacokinetics of understudied drugs given to children as standard care. Not specific to fosfomycin or uterine disease. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Pharmacokinetics, pharmacodynamics and safety of understudied drugs in children and young adults. No efficacy endpoint for uterine inflammation. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohort | J Obstet Gynaecol | Dienogest-related cystitis in women with endometriosis after laparoscopic surgery. Concerns a urinary condition, not uterine inflammatory disease. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501130D0AAAAAA (identifier as listed; not a PL number) | Fosfomycin Trometamol 3 g sachet | Not stated | Not stated |

One single-ingredient record is listed, and its status is valid. No indication text was supplied, so the approved indication cannot be confirmed from the data compiled for this report. Please check the current SmPC and BNF.

---

## Safety Considerations

- **Contraindication-type relations in the knowledge graph** (these are graph relations, not label text): kidney disease, pyoureter, *Clostridium difficile* colitis and perinatal necrotizing enterocolitis.
- **Drug Interactions** (3 recorded):
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

No label-based warnings or contraindications were available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No cited study directly addresses uterine inflammatory disease, so the evidence level is L5 despite the high model score.
- The retrieved trials are general paediatric pharmacokinetic studies, and the one paper concerns a urinary condition.

**To proceed, the following is needed:**
- Clinical or microbiological studies of fosfomycin in uterine or pelvic infection.
- Confirmed mechanism of action data and the licensed indication text and dosage form from the SmPC.
- Label-based warnings and contraindications to replace the knowledge-graph relations.
- Consideration of a better-supported prediction from the same analysis: **pyelitis** (upper urinary tract infection). It has a Phase 2/3 RCT of intravenous fosfomycin in complicated UTI and acute pyelonephritis ([PMID 30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/)). It is largely an extension of the existing urinary use rather than a new therapeutic area.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

