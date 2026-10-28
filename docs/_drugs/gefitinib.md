---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 313
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Gefitinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
description: "Gefitinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Not recorded in the local data"
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Gefitinib: Fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, gefitinib is a selective inhibitor of the epidermal growth factor receptor (EGFR) tyrosine kinase. Its efficacy in EGFR-mutated NSCLC is established.

A possible link to gingival fibromatosis is EGFR and growth-factor signalling in fibroblast proliferation. This is speculative: no study in the compiled data tests it, and the model's similarity assessment to the original indication is still pending. The high score (0.9989) is a computational prediction and should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801050AWAAAAAA | Gefitinib tablets 250 mg | Tablet | Not specified in the compiled data |

The identifier above is a BNF-style product code rather than a standard PL number. The compiled data contain no dosage form or indication text for this record, and no NICE-appraised indication details. Please check the current SmPC and the BNF.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC; liver function and respiratory symptoms are relevant given the contraindication signals below |
| Handling Protection | Please refer to local policy and the SmPC |

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis, and postinflammatory pulmonary fibrosis.
- **Drug Interactions**: 100 interactions were identified; the 20 listed in the compiled data are mostly moderate.
  - Acid-suppressing agents: famotidine, ranitidine, nizatidine, cimetidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole.
  - Other moderate-level interactions: clarithromycin, aprepitant, dexamethasone, naltrexone, miconazole, clotrimazole and troglitazone.
  - Interaction level unknown: calcitriol and glimepiride.

The licence-based warnings and contraindications were not available for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5), and the mechanistic link to gingival fibromatosis is speculative. The knowledge graph also flags several respiratory and hepatic contraindications, so there is no basis to progress this candidate.

**To proceed, the following is needed:**
- Mechanism of action data and a worked-through rationale linking EGFR inhibition to gingival fibromatosis
- Preclinical or early clinical studies in this condition
- Licence-level warnings and contraindications from the SmPC, with the approved indication text and dosage form for the UK authorisation
- A route and formulation assessment (route compatibility is pending)
- A benefit–risk review, given the interstitial lung disease and liver-related signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

