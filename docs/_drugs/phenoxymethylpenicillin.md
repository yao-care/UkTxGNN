---
layout: default
title: Phenoxymethylpenicillin
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Phenoxymethylpenicillin: predicted new indication Epiglottitis (evidence level L5). Approved use: Streptococcal infection, pharyngitis, infectious otitis media…"
monitor_inn: "Phenoxymethylpenicillin"
predicted_indications: ["epiglottitis", "laryngitis"]
---

# Phenoxymethylpenicillin
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

# Phenoxymethylpenicillin: From Streptococcal and Respiratory Tract Infections to Epiglottitis

## One-Sentence Summary

Phenoxymethylpenicillin (penicillin V) is an oral, narrow-spectrum beta-lactam antibiotic, originally used for streptococcal infections, pharyngitis, otitis media and related respiratory and skin infections.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, pharyngitis, infectious otitis media, respiratory tract infections, erysipelas, scarlet fever (the UK licence record contains no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, phenoxymethylpenicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis. Its efficacy in streptococcal and upper respiratory tract infections is established, and mechanistically it may be applicable to bacterial infections of the supraglottic region.

Epiglottitis is a bacterial infection of the supraglottis. Historically it was caused mainly by *Haemophilus influenzae* type b, and also by *Streptococcus pneumoniae*, group A streptococci and *Staphylococcus aureus*. For the streptococcal and other penicillin-susceptible pathogens, there is a plausible antibacterial rationale. The high TxGNN score is probably driven by the drug's antibacterial class and its existing respiratory and streptococcal indications.

There are important limitations:
- Phenoxymethylpenicillin is oral and narrow-spectrum, and it is not active against beta-lactamase-producing *H. influenzae*.
- Epiglottitis is an airway emergency. It is usually managed with airway protection and intravenous broad-spectrum antibiotics such as third-generation cephalosporins, so oral penicillin V is not a suitable primary therapy.
- The 99.90% score is a computational prediction only and is not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for epiglottitis.

*For context, the second-ranked prediction, laryngitis (TxGNN score 99.85%, evidence level L4), has one related publication. It is indirect evidence only and is not about phenoxymethylpenicillin as a treatment:*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/) | 1992 | Clinical study (design to be verified) | Acta Oto-Laryngologica. Supplementum | In 106 adults with acute laryngitis, erythromycin reduced nasopharyngeal *B. catarrhalis* isolation compared with placebo. The abstract notes that phenoxymethylpenicillin had no effect on the clinical course in earlier work. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501011P0AAADAD (BNF-style product code; no PL number in the data) | Phenoxymethylpenicillin oral solution 125 mg/5 ml | Oral solution | Not recorded in the data compiled for this report |

The BNF classifies the product under section 5.1 (antibacterial drugs, penicillins). Epiglottitis is not a listed indication in the data compiled for this report.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from graph edges, not label text, and should be checked against the SmPC):
- Kidney disease
- Pyoureter
- *Clostridium difficile* colitis
- Perinatal necrotizing enterocolitis
- Infectious mononucleosis
- Chronic Epstein-Barr virus infection syndrome

**Drug Interactions:** 32 interactions were identified, and the main ones are:
- **Moderate:** doxycycline, minocycline, tetracycline, neomycin, warfarin, dicoumarol, balsalazide, picosulfuric acid, iodide I-123, iodide I-131
- **Minor:** clarithromycin
- **Unknown severity:** omeprazole, lansoprazole, simvastatin, prednisolone, dexamethasone, aspirin, clopidogrel, heparin, ibuprofen

Warnings and contraindications from the product label are not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). Phenoxymethylpenicillin is also clinically unsuitable as primary therapy for epiglottitis, because it is oral, has a narrow spectrum, and does not cover beta-lactamase-producing *H. influenzae*. In an airway emergency, standard intravenous treatment should not be delayed.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC and BNF, because safety screening cannot proceed without them
- Mechanism of action data (for example from DrugBank)
- Microbiological and epidemiological evidence of penicillin-susceptible epiglottitis, and a defined role for an oral step-down or prophylactic use
- Any published clinical evidence for penicillin V in epiglottitis
- A decision on whether the laryngitis prediction is worth pursuing, noting that its only retrieved publication does not support penicillin V
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

