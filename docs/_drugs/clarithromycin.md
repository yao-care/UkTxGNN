---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 176
evidence_level: L5
indication_count: 5
monitor_inn: "Clarithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
last_modified_at: 2026-10-28
description: "Clarithromycin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Infectious otitis media, bacterial pneumonia…"
---

# Clarithromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Clarithromycin: From Respiratory and Ear Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic, with relations recorded in the knowledge graph for infections such as otitis media, pneumonia, sinusitis and streptococcal or staphylococcal infection.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **0 clinical trials** and only **1 publication** (a case report) for this prediction, so the evidence is very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Infectious otitis media, bacterial pneumonia, streptococcal and staphylococcal infections, maxillary sinusitis (relations recorded in the knowledge graph; the UK licence record contains no indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clarithromycin is a macrolide antibiotic, and its activity against respiratory and ear, nose and throat bacterial infections is recorded in the knowledge graph. Mechanistically, it is not clear why it would be applicable to hyperamylasemia.

The only publication linked to this prediction is a 2004 Japanese case report of *Mycobacterium abscessus* lung infection complicated by primary macroamylasemia. Clarithromycin was used there as an anti-mycobacterial agent. Hyperamylasemia was not the treatment target, and the association is most likely incidental to the infection or to a comorbidity. The high score of 0.9935 is a computational output and is not backed by clinical data.

Because this case report does not study clarithromycin as a treatment for hyperamylasemia, the evidence level is L5 (model prediction only).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai Zasshi | A 76-year-old man with *M. abscessus* lung infection and primary macroamylasemia. Clarithromycin was part of the anti-mycobacterial treatment. Hyperamylasemia was a coexisting condition, not a treatment target. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501050B0AAAAAA | Clarithromycin Tab 250mg | Not stated | Not stated in the licence record |

The data compiled for this report list one single-ingredient authorisation, with a status of valid. Please check the SmPC and BNF (macrolides, infections section) for the authorised indications.

---

## Safety Considerations

**Contraindication-type relations recorded in the knowledge graph** (these come from graph relations, not from label text, and should be checked against the SmPC):
- Cardiac rhythm: long QT syndrome, torsades de pointes, ventricular tachycardia (including catecholaminergic polymorphic and incessant infant forms)
- Liver and biliary: liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic forms), gallbladder disease
- Porphyria: porphyria, inherited porphyria, porphyrin metabolism disease
- Kidney: kidney disease, pyoureter
- Neuromuscular: myasthenia gravis (including adult-onset), neuromuscular junction disease
- Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis
- Bone: osteoporosis, postmenopausal osteoporosis, bone fracture
- Infection: infectious mononucleosis, chronic Epstein-Barr virus infection syndrome

**Drug Interactions:** The interaction screen returned 100 interacting drugs in total; the first 20 are summarised here.
- **Major:** abemaciclib, fentanyl, acalabrutinib
- **Moderate:** abametapir (topical), abiraterone, paclitaxel, acarbose, tramadol, famotidine, formoterol, nifedipine, adenosine, trastuzumab emtansine, flunisolide, afatinib, ethinylestradiol, hydrocortisone
- **Minor:** dolutegravir, zidovudine, loratadine

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single case report in which hyperamylasemia was a coexisting condition, and there are no trials. The evidence is model prediction only (L5), and there is no plausible mechanism or clinical rationale for treating hyperamylasemia with clarithromycin.

**To proceed, the following is needed:**
- Mechanism of action data for clarithromycin and a testable hypothesis linking it to hyperamylasemia
- Clinical or observational studies that directly examine hyperamylasemia as a treatment target
- Label-based warnings and contraindications from the SmPC, to replace the graph-derived safety relations
- Full licence details (dosage form and approved indications) for the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

