---
layout: default
title: Voriconazole
parent: Model Prediction Only (L5)
nav_order: 613
evidence_level: L5
indication_count: 10
---

# Voriconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Voriconazole: From Invasive Fungal Infections to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Voriconazole is a triazole antifungal agent, established for the treatment of invasive fungal infections such as invasive aspergillosis. The TxGNN model predicts it may be effective for **multidrug-resistant tuberculosis (MDR-TB)**, but this signal is currently supported only by **3 case-level publications** describing coincidental fungal-TB co-infection rather than direct treatment evidence, and **no registered clinical trials** exist for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infections (e.g. invasive aspergillosis) — established use of this triazole antifungal; no UK licence-level indication text is available in this evidence pack |
| Predicted New Indication | Multidrug-resistant tuberculosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, voriconazole inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol synthesis in the fungal cell membrane. This target is specific to fungi and has no known overlap with *Mycobacterium tuberculosis*, which lacks a sterol-based cell membrane and is not susceptible to azole antifungals.

The supporting literature for this prediction consists of case reports describing patients with tuberculosis who developed a **separate, concurrent fungal infection** (aspergilloma, invasive aspergillosis, or drug-resistant fungal disease) — not evidence that voriconazole treats tuberculosis itself. In these cases, voriconazole was used to manage the fungal co-infection, while TB was treated with standard anti-tubercular agents. This pattern likely reflects a co-occurrence signal picked up by the model (TB and fungal disease frequently appear together in the same patients and publications) rather than a genuine pharmacological repurposing opportunity.

Given the absence of a plausible mechanistic link and the confounded nature of the available literature, this prediction should be treated as a hypothesis-generating signal only, not as a basis for further clinical development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case Report | Cases Journal | Diabetic patient with MDR-TB who developed concurrent aspergilloma and invasive aspergillosis; illustrates co-infection rather than voriconazole efficacy against TB |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | Case Report (in vitro) | Brazilian Journal of Microbiology | In vitro study of photodynamic inactivation against multidrug-resistant fungal pathogen causing chromoblastomycosis; unrelated to tuberculosis treatment |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Lab/Genetic Study | Virulence | Genetic diversity study of azole-resistant *Candida krusei* isolates; no tuberculosis-related content |

---

## UK Market Information

No MHRA marketing authorisation is currently held for voriconazole in this evidence pack (market status: **Not marketed**; total licences: **0**). No product, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications, and drug interaction data for voriconazole were not available in this Evidence Pack (flagged as a Blocking data gap — MHRA labelling has not yet been retrieved).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (MDR-TB) lacks a plausible mechanism of action — voriconazole's antifungal CYP51 target has no known relevance to *M. tuberculosis* — and the supporting literature reflects fungal-TB co-infection management rather than anti-tubercular efficacy. With no clinical trials and only L5 (model-prediction-only) evidence, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Resolution of Blocking data gap DG001 (MHRA/SmPC warnings and contraindications) before any safety review can begin
- Resolution of High-priority data gap DG002 (confirmed mechanism of action) to properly assess mechanistic plausibility
- Independent pharmacological or in vitro evidence of any direct anti-mycobacterial activity for voriconazole, which is not currently expected given its known mechanism
- Separate evaluation of two lower-ranked but more mechanistically coherent signals surfaced in this pack, which were miscategorised under TB-related disease labels and may warrant reformulation as distinct research questions: (1) voriconazole for CNS fungal granulomas (e.g. *Cladophialophora bantiana* infection) that clinically mimic tuberculoma, and (2) voriconazole for chronic pulmonary aspergillosis arising in lung cavities left by prior (inactive) tuberculosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

