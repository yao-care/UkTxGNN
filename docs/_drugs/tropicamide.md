---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 645
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Tropicamide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
description: "Tropicamide: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Tropicamide
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

## Tropicamide: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Tropicamide is a short-acting topical antimuscarinic originally used to produce cycloplegia and pupil dilation for eye examination.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are currently **no registered clinical trials and no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

Two other predictions were also generated: obsolete neurogenic bladder (0.9913) and irritable bowel syndrome (0.9912). Neither has clinical trial or literature support.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tropicamide is a muscarinic receptor antagonist. Pharmacology records list activity at the M2, M3, M4 and M5 receptors. It is used as a short-acting mydriatic for examining the lens, vitreous humour and retina.

Cauda equina syndrome is caused by compression of the lumbosacral nerve roots and produces bladder, bowel and sensory dysfunction. In theory, anticholinergic action could reduce detrusor overactivity. However, the primary treatment is urgent surgical decompression, and no drug is expected to treat the underlying disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The mechanistic case is also weakened by the formulation. Topical ophthalmic tropicamide gives minimal systemic exposure, so it is unlikely to reach the effect on bladder or bowel that systemic antimuscarinics achieve.

For the two other predictions, a class-level rationale exists (antimuscarinics such as oxybutynin and tolterodine for neurogenic detrusor overactivity, and dicyclomine and hyoscyamine for IBS cramping). Established antimuscarinics already cover these needs. The neurogenic bladder term is also flagged as obsolete in the ontology and should be mapped to current terminology (for example, neurogenic detrusor overactivity) before further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1105000S0AAABAB | Tropicamide Eye Drops 1% | Eye drops | Not stated in the available record |

The licence number above is as it appears in the compiled data and is not in the standard MHRA "PL" format, so it should be verified against the MHRA register.

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text):** The TxGNN knowledge graph links tropicamide with contraindication edges for the following conditions:
  - Eye: open-angle glaucoma, angle-closure (closed-angle) glaucoma, ocular hypertension
  - Cardiovascular: hypertension and hypertensive disorder, myocardial ischaemia, coronary artery disease, heart conduction disease, sudden cardiac arrest
  - Endocrine and metabolic: hyperthyroidism, Graves disease, thyrotoxicosis, diabetes mellitus, diabetic ketoacidosis

  These should be confirmed against the SmPC.
- **Drug Interactions:** 10 interactions were identified in the DDInter database, all with unclassified severity: atropine, potassium chloride, vancomycin, simvastatin, prednisolone, famotidine, warfarin, lidocaine, fluconazole and brimonidine. The anticholinergic adverse effects expected with systemic exposure (constipation, dry mouth, blurred vision) would be a concern if the drug were repurposed.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest solely on TxGNN scores (Evidence Level L5), with no trials or publications. Topical ophthalmic tropicamide has negligible systemic exposure, and existing antimuscarinics already address the plausible bladder and bowel targets.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, and SmPC warnings and contraindications for the UK product (a blocking gap for safety screening)
- Confirmation of the licence record, including dosage form and approved indication text
- Mapping of the obsolete neurogenic bladder term to current terminology
- Evidence of a feasible systemic or alternative route of administration
- A literature and trial search targeted at antimuscarinics in neurogenic bladder, IBS and cauda equina syndrome, to establish whether tropicamide adds anything over existing agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

