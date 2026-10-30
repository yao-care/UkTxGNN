---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L4). Approved use: Chronic myelogenous leukaemia, BCR-ABL1 positive"
monitor_inn: "Nilotinib"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Nilotinib: From BCR-ABL1-Positive Chronic Myeloid Leukaemia to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor originally used to treat BCR-ABL1-positive chronic myeloid leukaemia.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but at present there are **no registered clinical trials** and only **1 publication** (a review) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukaemia, BCR-ABL1 positive |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general knowledge of nilotinib pharmacology, it is a tyrosine kinase inhibitor active against BCR-ABL, KIT, DDR and PDGFR (alpha and beta).

DFSP is characterised by a COL1A1-PDGFB translocation. This produces a constitutively active PDGFB ligand that drives PDGFRB signalling. Inhibiting the PDGFR pathway is therefore a biologically coherent approach. Imatinib, a closely related PDGFR-inhibiting tyrosine kinase inhibitor, is an established therapy for unresectable or metastatic DFSP, which supports plausibility at the class level.

This rationale is inferred from general pharmacology rather than from nilotinib-specific data in the compiled dataset. The very high TxGNN score is consistent with the target overlap, but it is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders, covering the role of the PDGF/PDGFR signalling pathway as a therapeutic target |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801050ASAAAAAA | Nilotinib capsules 200 mg | Capsule | Not available in the compiled data |

One valid single-ingredient authorisation was identified. The dosage form and approved indication text were not recorded in the compiled data, so the entry should be checked against the current MHRA record, the SmPC and the BNF. The listed number is not in standard PL format and should also be verified.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (the knowledge-graph contraindication list includes neutropenia, thrombocytopenia and anaemia) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Full blood count, liver function, electrolytes (potassium, magnesium), glucose and ECG for QT interval; confirm against the SmPC |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Disease-related cautions (from the TxGNN knowledge graph, not label text):** The knowledge graph links nilotinib with the following conditions, which should be verified against the SmPC:
  - Cardiovascular and QT-related: hypertension, long QT syndrome (including familial), torsades de pointes
  - Hepatic and biliary: liver disease, gallbladder disease, hyperbilirubinaemia (including Gilbert syndrome), pancreatitis
  - Haematological: thrombocytopenia, neutropenia, agranulocytosis, anaemia
  - Metabolic: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, hypophosphataemia
- **Drug Interactions:** 100 interactions were recorded; examples are shown below.
  - Major: dexamethasone, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
  - Moderate: acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), other corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone), pioglitazone, saxagliptin, loperamide, bupropion, aprepitant, bisacodyl

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link (PDGFR inhibition in a PDGFB-driven tumour) is plausible and the TxGNN score is high. However, there are no nilotinib-specific trials in DFSP and only one general review, so the evidence is limited to L4. The compiled safety data are incomplete, and the knowledge graph flags several cardiac (QT), hepatic and haematological cautions.

**To proceed, the following is needed:**
- A targeted literature search for nilotinib in DFSP (case series, phase 2 studies) and comparison with imatinib outcomes
- Mechanism of action data from DrugBank, to confirm PDGFR activity formally
- The MHRA SmPC and BNF warnings and contraindications, which are required for safety screening
- Confirmation of the authorisation details (dosage form, approved indication, licence number)
- A cardiac (QT) and drug-interaction risk plan for any proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

