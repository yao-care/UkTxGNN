---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 317
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Glycine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Glycine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Glycine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Glycine: From Rhinitis and Upper Respiratory Tract Conditions to Nasal Cavity Disease

## One-Sentence Summary

Glycine is an amino acid that the knowledge graph links to upper-airway conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this is a model prediction only: the single registered trial is not a therapeutic study of glycine, and the two publications are not clinically relevant.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glycine's listed uses are already nasal and upper-airway conditions, so the predicted indication is close to its existing uses. A specific pharmacological link, such as a glycine receptor-mediated anti-inflammatory or cytoprotective effect, cannot be substantiated from the data compiled for this report.

The high TxGNN score (0.998) reflects proximity within the knowledge graph. Because "nasal cavity disease" is a broad category that includes rhinitis, the prediction is largely an extension of existing associations rather than a new repurposing signal.

A second prediction, **acute laryngopharyngitis** (score 99.84%), was also generated. It has no trials or publications, and is anatomically close to pharyngitis and nasopharyngitis, which likely explains the graph-based prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET/CT or PET/MRI imaging study of a new radiopharmaceutical (18F-FPPRGD2) in patients with glioblastoma, gynaecological cancers and renal cell carcinoma. It is a diagnostic imaging study and does not test glycine for nasal cavity disease; the match appears incidental. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic research | Veterinary Pathology | Lectin histochemistry of normal and herpesvirus-infected bovine nasal mucosa. This is animal tissue research on glycoconjugates and does not assess glycine as a treatment. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Basic research | Chemical & Pharmaceutical Bulletin | Oligoarginine-polymer conjugates as a mucosal adjuvant for nasal vaccination in mice. This concerns vaccine delivery materials, not glycine therapy. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 091101000AADADA | Glycine liquid, 750 mg/5 ml | Liquid | Not available |

This is the only authorisation identified, and it is a single-ingredient product with valid status. Approved indication text and dosage form details were not available in the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease associations, not taken from product label text; they should be verified against the SmPC):

- Kidney disease, including chronic kidney disease, chronic renal failure and end-stage renal failure
- Kidney stone and calcium-related conditions: nephrolithiasis, nephrocalcinosis, hypercalcaemia, hyperparathyroidism, sarcoidosis
- Phosphate and bone-related conditions: hyperphosphataemia, phosphorus metabolism disease, osteitis fibrosa, lytic metastatic bone lesions, humoral hypercalcaemia of malignancy
- Cardiovascular conditions: heart disease, cardiovascular disease, arteriosclerosis obliterans, ventricular fibrillation, digitalis poisoning
- Metabolic conditions: phenylketonuria and other disorders of phenylalanine metabolism, hypervitaminosis, acute urate nephropathy
- Other: constipation disorder, pyoureter

No drug interaction records were found.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. The one registered trial is an unrelated imaging study, the two publications are basic research without clinical relevance, and no mechanism of action data are available. The predicted indication also largely overlaps with existing associated uses, so it offers little new repurposing signal.

**To proceed, the following is needed:**
- Mechanism of action data for glycine in nasal and upper-airway tissue
- Product label warnings and contraindications for the UK authorisation, including approved indication text and dosage form
- Clinical studies (preferably randomised controlled trials) of glycine in nasal cavity disease or acute laryngopharyngitis
- Clarification of the specific disease scope behind "nasal cavity disease", given how broad the term is
- A review of the knowledge-graph contraindication signals, particularly renal and cardiovascular conditions, against the SmPC
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

