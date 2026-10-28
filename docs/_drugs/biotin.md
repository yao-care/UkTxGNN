---
layout: default
title: Biotin
parent: Model Prediction Only (L5)
nav_order: 108
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Biotin: predicted new indication Dyspepsia (evidence level L5). Approved use: Nutritional biotin deficiency"
monitor_inn: "Biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
---

# Biotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Biotin: From Nutritional Biotin Deficiency to Dyspepsia
{: .text-alpha }

## One-Sentence Summary

Biotin is a B-vitamin, originally used to treat nutritional biotin deficiency.
The TxGNN model predicts it may be useful for **dyspepsia**, but there are currently **no registered clinical trials** and only **6 publications**, none of which tests biotin as a treatment for dyspepsia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nutritional biotin deficiency (the UK authorisation record contains no indication text) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Biotin is known to act as a cofactor for carboxylase enzymes involved in carbohydrate, fat and amino acid metabolism. Its efficacy in correcting biotin deficiency is established.

Biotin deficiency can cause gastrointestinal symptoms such as nausea and anorexia. This suggests, at most, that correcting a deficiency might relieve some digestive symptoms. It does not show that biotin treats dyspepsia in people who are not deficient. The prediction currently rests on the model score alone, with no established mechanistic link.

A second prediction, gastroparesis (score 0.9942), has no trials or literature and no clear mechanistic rationale, so it is not evaluated further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | J Dermatol | Biotin deficiency in an infant fed only an amino acid formula after a neonatal dyspepsia diagnosis. This shows a deficiency complication, not a benefit for dyspepsia. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Stomach antral endocrine cells in irritable bowel syndrome. No biotin intervention. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endosc | Endocrine cells in the stomach's oxyntic mucosa in irritable bowel syndrome. No biotin intervention. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | J Clin Pathol | Interleukin-10 in *H. pylori* gastritis. No biotin intervention. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Other | Eksp Klin Gastroenterol | A prebiotic supplement containing inulin, oligofructose, vitamins (including biotin) and minerals, studied for gut microbiota disorders in patients with lung disease on antibiotics. Not biotin-specific. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney Int | Small bowel T cells in IgA nephropathy. Not relevant to dyspepsia or biotin. |

None of these publications provides direct evidence that biotin is effective for dyspepsia.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 090602800AAAGAG | Biotin Tab 5mg | Tablet (not stated in the record) | Not stated in the available record |

The data compiled for this report list one valid single-ingredient authorisation. The listed number is not in the standard UK "PL" format, so the authorisation details should be verified against the MHRA register. NICE appraisal and BNF classification details were not available.

## Safety Considerations

The following contraindication links come from a knowledge-graph relationship database, not from product label text, so they should be confirmed against the SmPC:

- **Disease associations flagged in the knowledge graph:** kidney disease, nephrolithiasis (including SLC26A1-related susceptibility), nephrocalcinosis, acute urate nephropathy, pyoureter, sarcoidosis, hyperparathyroidism, osteitis fibrosa, hypercalcaemia, phosphorus metabolism disease, constipation disorder and lytic metastatic bone lesion. Many of these resemble warnings for calcium/vitamin D rather than biotin, so their relevance should be checked.

No drug interaction data were found.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no clinical trials, and the available literature does not test biotin in dyspepsia. No supporting mechanism has been established, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for biotin, and a plausible rationale for benefit in dyspepsia in people without deficiency
- Preclinical or early clinical studies of biotin in dyspepsia
- The SmPC warnings and contraindications for the UK product (currently missing)
- Verification of the UK authorisation details, including approved indication and dosage form
- Confirmation of the knowledge-graph contraindication signals against product labelling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

