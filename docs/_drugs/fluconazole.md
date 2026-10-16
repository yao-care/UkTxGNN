---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, candidiasis, vulvovaginal candidiasis…"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "Plasmodium falciparum malaria", "allergic urticaria", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "pneumocystosis", "blood group incompatibility", "premalignant hematological system disease", "papular urticaria"]
---

# Fluconazole
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

# Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an azole antifungal, originally used to treat candidiasis (oral, oesophageal, vulvovaginal, invasive) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** were found for this indication, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, candidiasis, vulvovaginal candidiasis, oesophageal candidiasis, cryptococcal meningitis, candidaemia, disseminated candidiasis |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Fluconazole is an azole antifungal, a class that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase) and so blocks ergosterol synthesis. Its efficacy in candidiasis and cryptococcal infection is established.

The link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is usually viral (often adenoviral) or immune-mediated, so an antifungal has no clear target in its pathology. The high TxGNN score therefore appears to be a computational association and should not be read as evidence of benefit.

Other predictions in the data set for this drug (ranks 2-10) also have little support. The most plausible are Plasmodium falciparum malaria (in vitro data only, evidence level L4) and pneumocystosis (biologically plausible as a fungal organism, but no direct fluconazole data). The remainder have no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0502010B0AAAAAA | Fluconazole Capsules 50 mg | Capsule | Indication text not available |

The identifier shown is a BNF-style product code (BNF section 5.2.1, azole antifungals) rather than a PL number. One valid single-ingredient authorisation is recorded.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, kidney disease, pyoureter, liver disease, gallbladder disease.
- **Drug Interactions**: 100 interactions were identified. Notable examples:
  - **Major**: chlorpropamide.
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), proton pump inhibitors (omeprazole, rabeprazole, dexlansoprazole), famotidine, loperamide, aprepitant, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes.
  - **Minor**: amphotericin B, clarithromycin.
- A published cohort also reports that fluconazole raises tacrolimus trough levels (CYP3A4 inhibition), so dose adjustment is needed.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature, and there is no credible mechanistic link between an antifungal and a mostly viral or immune-mediated eye condition.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible mechanistic rationale for the ocular indication
- Label warnings and contraindications from the SmPC and BNF
- Preclinical or clinical evidence in punctate epithelial keratoconjunctivitis, and an assessment of route of administration (ocular versus systemic) and ocular safety
- If the programme is to continue, consider prioritising other predictions, such as Plasmodium falciparum malaria (confirmatory in vitro work) or pneumocystosis (comparison against standard care)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

