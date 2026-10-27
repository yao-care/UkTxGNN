---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis (also staphylococcal infections…"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic, originally used for Gram-positive infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **no clinical trials** and only **1 publication** (an unrelated case report), so the prediction is most likely a knowledge-graph artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis (also staphylococcal infections, endocarditis, bacterial arthritis and staphylococcal pneumonia) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*Note: the data compiled for this report contain no approved indication text for the UK product. The original indications above come from the TxGNN knowledge graph.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, vancomycin inhibits bacterial cell wall synthesis by binding the D-Ala-D-Ala termini of peptidoglycan precursors in Gram-positive bacteria. Its efficacy in its original infectious indications is well established.

Diffuse scleroderma, by contrast, is an autoimmune fibrotic disease. There is no plausible mechanistic link between a cell wall synthesis inhibitor and the pathology of scleroderma. The high TxGNN score appears to be a graph-based artefact rather than a genuine repurposing signal.

For context, the other top-ranked predictions are also weak. Paratyphoid fever, salmonellosis and typhoid fever involve Gram-negative organisms that are intrinsically resistant to vancomycin. The one biologically plausible prediction is streptococcal pneumonia (rank 9, Gram-positive). However, this is an extension of existing antibacterial use rather than true repurposing, and beta-lactams remain first-line.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A man with diffuse exfoliative rash, sepsis and eosinophilia, evaluated for erythroderma. It does not address scleroderma treatment and offers no support for the prediction. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501070U0AAABAB (BNF code; no PL number available) | Vancomycin HCl capsules 250 mg | Capsule (oral) | Not available in the data compiled |

BNF classification: the code prefix 0501070 corresponds to the BNF section on other antibacterials (glycopeptide antibacterials).

---

## Safety Considerations

- **Conditions associated with contraindication (from knowledge graph, not label text):** kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder and auditory system disease.
- **Drug Interactions:** 100 interactions were identified. Those listed here include:
  - **Major:** human immunoglobulin G (intravenous), human botulinum neurotoxin A/B immune globulin, and live cholera vaccine (*Vibrio cholerae* CVD 103-HgR).
  - **Moderate (examples):** other nephrotoxic or ototoxic agents (amikacin, amphotericin B, capreomycin, carboplatin, bacitracin), NSAIDs (ibuprofen, ketorolac, diclofenac, celecoxib), cholestyramine, metformin and mesalazine.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There is no mechanistic rationale, no clinical trials and no relevant literature for diffuse scleroderma. Using vancomycin for this condition would expose patients to potential nephrotoxicity and ototoxicity without any supporting evidence of benefit.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking vancomycin to scleroderma pathophysiology, supported by preclinical data
- Confirmed mechanism of action data and UK SmPC warnings and contraindications
- Any relevant clinical or observational data on vancomycin in scleroderma
- If an antibacterial extension is of interest, streptococcal pneumonia (rank 9) is the only prediction with a plausible mechanism and would merit a separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

