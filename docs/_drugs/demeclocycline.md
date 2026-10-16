---
layout: default
title: Demeclocycline
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Demeclocycline: predicted new indication Chronic ethmoidal sinusitis (evidence level L5). Approved use: Bacterial infections, including urinary tract infection, bronchitis…"
monitor_inn: "Demeclocycline"
predicted_indications: ["chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
---

# Demeclocycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Demeclocycline: From Bacterial Infections to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Demeclocycline is a tetracycline antibiotic, originally used to treat a range of bacterial infections such as urinary tract infections, bronchitis and gonorrhoea.
The TxGNN model predicts it may be effective for **chronic ethmoidal sinusitis**, but **no clinical trials and no publications** were identified in the data compiled for this report. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including urinary tract infection, bronchitis, gonorrhoea and pharyngitis (from knowledge graph indication data; no MHRA indication text available) |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, demeclocycline belongs to the tetracycline class of antibiotics. Its antibacterial efficacy in respiratory and other infections is established, and mechanistically it may be applicable to chronic ethmoidal sinusitis.

Chronic sinus inflammation can involve bacterial pathogens, so antibacterial activity is a plausible link. Tetracyclines have also been reported to have anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects, which could be relevant to chronic sinus inflammation. This remains a hypothesis. Because the original mechanism of action data is missing, the link cannot be verified from the data compiled for this report.

Two other predictions for this drug are also available, both at the same L5 level with no trials or literature:
- **Chronic rhinosinusitis** (score 99.09%): Other tetracyclines, such as doxycycline, have been studied in this condition, but no such evidence was supplied for demeclocycline, so it cannot be counted as direct support. Concerns include antibiotic resistance with long-term use, phototoxicity, and the availability of better-studied alternatives.
- **Paranasal sinus neoplasm** (score 99.05%): Any link is speculative, such as preclinical anti-proliferative or anti-angiogenic effects. The high score may partly reflect knowledge-graph proximity to sinus-related conditions rather than a true therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501030F0AAAAAA (BNF classification code; not a PL number) | Demeclocycline HCl Capsules 150 mg | Capsule | Not available in the compiled data |

The product is classified under BNF section 5.1.3 (tetracyclines).

---

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not taken from label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and diabetes insipidus (including neurohypophyseal and central forms).
- **Drug Interactions** (100 interactions were recorded; the sample reviewed includes):
  - **Major:** Vitamin A.
  - **Moderate:** Amoxicillin, balsalazide, and polyvalent cation products that can reduce tetracycline absorption (calcium phosphate, calcium acetate, magnesium oxide, magnesium sulfate, magnesium chloride, zinc sulfate, zinc acetate, potassium citrate). Several insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular and inhaled human insulin) are also listed.
  - **Minor:** Mannitol.

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high TxGNN score (L5). There are no clinical trials or publications, the mechanism of action data is missing, and label-based safety data could not be obtained. The case does not yet justify further development.

**To proceed, the following is needed:**
- Mechanism of action data for demeclocycline
- SmPC-based warnings and contraindications, and the MHRA approved indication text and PL number
- A systematic literature search for tetracycline use in chronic sinusitis, to determine whether any evidence extends to demeclocycline
- A comparison with better-studied alternatives (such as doxycycline) and an assessment of antimicrobial resistance risk with prolonged use
- Preclinical or early-phase clinical evidence before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

