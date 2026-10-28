---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-28
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma, bronchitis, pulmonary emphysema and related airway diseases"
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a methylxanthine bronchodilator, originally used for asthma and other chronic airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**, but the data compiled for this report contain **no clinical trials** and **no publication that directly studies theophylline in thrombotic disease**, so this remains a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema and related airway diseases (relations recorded in the knowledge graph; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on general pharmacology, theophylline is a non-selective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. Raising cyclic AMP (cAMP) in platelets could in principle reduce platelet aggregation, which gives a plausible but unproven link to thrombosis.

The link is not straightforward. Adenosine signalling has antithrombotic effects, so adenosine receptor antagonism could work against any benefit, and the net direction is uncertain. The relationship between the original respiratory indications and thrombotic disease is also not established in the data (similarity analysis is pending).

The very high TxGNN score (0.9962) is a computational prediction only and is not backed by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved publications are mostly background or methodological papers, not studies of theophylline treating thrombotic disease. A selection is shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, an antiplatelet drug; does not study theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Prostaglandins, platelets and atherosclerosis; prostacyclin raises platelet cAMP and inhibits aggregation (background mechanism) |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory | General Pharmacology | Milrinone and adenosine inhibit human platelet response through cAMP; does not study theophylline |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Methodological | British Journal of Haematology | Radioimmunoassay for platelet factor 4; theophylline used only as a component of the anticoagulant sample tube |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Observational | Inflammatory Bowel Diseases | Platelet-leukocyte aggregates in inflammatory bowel disease; not about theophylline |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Observational | Rheumatology (Oxford) | Platelet and neutrophil activation in Behçet's disease; not about theophylline |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Clinical (non-indexed abstract) | Minerva Cardioangiologica | Theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy; a vascular, not thrombotic, condition and a different compound |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Clinical (non-indexed abstract) | Cardiologia Pratica | Cardiocirculatory effects of a theophylline nicotinate derivative in cerebral and peripheral angiopathies; different compound |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Analytica Chimica Acta | Aptasensor for theophylline detection; no relevance to thrombosis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0301030S0AAAMAM | Theophylline Tab 200mg M/R (modified-release tablet) | Not recorded | Not recorded in the licence record |

This record appears to be a prescribing-classification style code rather than a standard PL number. Please check the MHRA register and the BNF (respiratory system, bronchodilators) for the authorised indications.

---

## Safety Considerations

**Knowledge-graph contraindication relations** (these come from the knowledge graph, not from label text, and should be checked against the SmPC): hypertension, liver failure and liver disease, epilepsy, anxiety and other neurotic disorders, porphyria, kidney disease, thrombocytopenia, neutropenia and agranulocytosis, hypothyroidism, peptic ulcer disease, open-angle glaucoma, psychotic disorders, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, gallbladder disease, and dermatitis herpetiformis.

**Drug interactions** (100 recorded; examples):
- **Major:** bupropion
- **Moderate:** clarithromycin, cimetidine, famotidine, ranitidine, omeprazole, rabeprazole, doxycycline, tetracycline, minocycline, hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, activated charcoal, and some bowel-preparation products
- **Minor:** ephedrine

Theophylline has a narrow therapeutic window. Please refer to the SmPC and BNF for full safety information, including serum level monitoring. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies theophylline in thrombotic disease, so the evidence level is L5. The mechanistic link (cAMP elevation in platelets versus adenosine antagonism) points in uncertain directions, and the high TxGNN score is not supported by clinical data.

**To proceed, the following is needed:**
- Mechanism of action data and a clear analysis of the net effect on platelet function
- Preclinical or ex vivo platelet aggregation studies with theophylline at clinically relevant concentrations
- Clinical evidence in a defined thrombotic condition
- Review of safety against the listed contraindications and interactions, and the official SmPC warnings (not available in the compiled data)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

