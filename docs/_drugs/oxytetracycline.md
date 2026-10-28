---
layout: default
title: Oxytetracycline
parent: Model Prediction Only (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Oxytetracycline"
predicted_indications: ["chronic rhinosinusitis", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "punctate epithelial keratoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "otitis externa"]
description: "Oxytetracycline: predicted new indication Chronic rhinosinusitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Oxytetracycline
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

## Oxytetracycline: Chronic rhinosinusitis
{: .text-alpha }

## One-Sentence Summary

Oxytetracycline is a tetracycline antibiotic, originally used for bacterial infections such as urinary tract infection, bronchitis, pneumonia and conjunctivitis.
The TxGNN model predicts it may be effective for **chronic rhinosinusitis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Chronic rhinosinusitis |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Oxytetracycline is a tetracycline-class antibiotic with a broad antibacterial spectrum, and its efficacy in respiratory, urinary and eye infections is established. Mechanistically, it may be applicable to chronic rhinosinusitis.

Tetracyclines are active against some bacteria that colonise the sinuses. The class has also been reported to have anti-inflammatory and matrix metalloproteinase (MMP)-inhibitory effects, which could plausibly relate to chronic sinus inflammation. This link is hypothetical. No trials or literature were found for oxytetracycline in this condition, and chronic rhinosinusitis is often not primarily driven by bacterial infection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Authorisation Identifier | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501030T0AAAJAJ (BNF-style code; BNF section 5.1.3, tetracyclines) | Oxytetracycline tablets 250 mg | Tablet | Not specified in the data compiled for this report |

The record gives a BNF-style product code rather than a standard PL number. The manufacturer and approved indication text are also not recorded, so please check the current SmPC for the licensed indications.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The TxGNN knowledge graph links oxytetracycline with contraindication or caution in the following conditions:
  - Renal: kidney disease, kidney failure, uraemia, glomerulonephritis
  - Hepatic and biliary: liver disease, gallbladder disease
  - Cardiac: atrial fibrillation, atrioventricular block, Adams-Stokes syndrome, Wolff-Parkinson-White syndrome
  - Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis
  - Metabolic and genetic: G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, potassium deficiency
  - Other: respiratory failure, pyoureter

  These are graph associations and should be checked against the SmPC.
- **Drug Interactions:** 100 interactions were identified, and 20 are shown in the data compiled for this report. Only one is rated **Major**: vitamin A.
  - Most of the others are rated **Moderate**:
    - Divalent and polyvalent cation products (calcium acetate, calcium phosphate, magnesium oxide, magnesium sulfate, magnesium chloride, zinc sulfate, zinc acetate), which are known to reduce tetracycline absorption.
    - Insulins (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular and inhaled).
    - Amoxicillin, balsalazide and potassium citrate.
  - Mannitol is rated Minor.

For full safety information, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (0.9961), with no trials or publications for chronic rhinosinusitis. The proposed link, antibacterial plus possible anti-inflammatory action, is plausible but unproven.

**To proceed, the following is needed:**
- A systematic literature search for tetracyclines (including doxycycline) in chronic rhinosinusitis, to establish whether any clinical signal exists
- Detailed mechanism of action data
- Label-based warnings and contraindications from the SmPC, and the licensed indications for the UK product
- Assessment against existing UK guidance for chronic rhinosinusitis, including whether long-term antibiotic use is appropriate in the context of antimicrobial stewardship
- Route and formulation compatibility, which is currently undetermined

**Other candidate in the data:** Otitis externa (TxGNN score 0.9927) has 17 publication records, including small randomised comparisons of topical oxytetracycline combinations (with polymyxin B and hydrocortisone). Evidence there is provisionally L3, graded on titles only. Steroid-only preparations appeared comparably effective in some studies, so the contribution of oxytetracycline is uncertain. It may be a more tractable research question than chronic rhinosinusitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

