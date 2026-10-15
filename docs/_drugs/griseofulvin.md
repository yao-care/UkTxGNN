---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 320
evidence_level: L5
indication_count: 5
---

# Griseofulvin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Griseofulvin: From Tinea Infections to Myiasis

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used to treat dermatophyte (tinea) infections of the skin, scalp, nails and groin.
The TxGNN model predicts it may be effective for **myiasis**, but there are currently **no registered clinical trials and no publications** supporting this direction.
The prediction rests on model output alone and has no clear mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea unguium, tinea barbae, dermatophytosis of the scalp/beard and of the groin/perianal area (the approved indication text for the UK licence is not available) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Griseofulvin is a systemic antifungal whose efficacy in dermatophyte infections is established. It is generally understood to disrupt microtubule function and mitosis in fungal cells.

Myiasis is an infestation of tissue by fly larvae. It is usually managed by larval removal, occlusion, wound debridement and care, or antiparasitic drugs such as ivermectin. No established pharmacological rationale supports griseofulvin activity against fly larvae. The high TxGNN score appears to reflect network proximity to anti-infective or anti-parasitic agents rather than biology specific to myiasis.

The other highly ranked predictions are closely related and share the same weakness:

- **Wound myiasis, creeping myiasis and furuncular myiasis** have identical scores (99.34%). This suggests the prediction is propagated through the disease hierarchy rather than reflecting subtype-specific biology.
- **Echinococcus granulosus infection** (score 99.32%) has a weak, speculative conceptual parallel. Griseofulvin binds tubulin, and benzimidazoles (albendazole, mebendazole), the standard medical therapy for cystic echinococcosis, also act on parasite tubulin. There is no evidence that griseofulvin has scolicidal or anti-cyst activity.

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
| 0502050B0AAACAC | Griseofulvin Tab 500 mg | Tablet (strength given in the product name) | Not available in the data compiled |

This is the only authorisation identified (single-ingredient product, valid). The identifier above is a drug-code-style reference, not a standard MHRA "PL" number. Please verify the licence details and indication wording against the MHRA register and the BNF.

---

## Safety Considerations

**Contraindications (from knowledge-graph drug–disease contraindication links, not label text):**
- Liver failure
- Porphyria (including inherited porphyria and porphyrin metabolism disease)
- Systemic lupus erythematosus (including paediatric SLE)
- Substance abuse/dependence
- Neutropenia and related disorders, including agranulocytosis, cyclic haematopoiesis, severe congenital neutropenia (and its genetic subtypes), Kostmann syndrome, adult idiopathic neutropenia, constitutional neutropenia and Rowell syndrome

**Drug Interactions:** The data compiled for this report list 100 interactions. The first 20 are shown below, all graded Moderate except where stated.
- **Anticoagulants and antiplatelets:** warfarin, dicoumarol, apixaban, rivaroxaban, ticagrelor (all Moderate); acetylsalicylic acid (Minor)
- **Antidiabetic agents:** saxagliptin, linagliptin, repaglinide (Moderate); liraglutide (Minor)
- **Antiemetics and related agents:** aprepitant, rolapitant, naloxegol (Moderate)
- **Antimalarials and antiparasitics:** artemether, mefloquine, praziquantel (Moderate)
- **Others:** eliglustat, nitisinone, macimorelin, fostamatinib (Moderate)

Warfarin and other anticoagulant combinations warrant particular attention. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score only (Evidence Level L5), with no clinical trials or publications. There is no credible mechanistic link between griseofulvin and fly-larval infestation, and established effective treatments exist. The near-identical scores across the myiasis subtypes suggest a hierarchy artefact rather than a real signal.

**To proceed, the following is needed:**
- Mechanism of action data for griseofulvin
- In vitro or preclinical evidence of larvicidal activity (and, for the echinococcosis prediction, protoscolex viability assays)
- Confirmation of the UK licence details (MHRA licence number, dosage form, approved indication) and the full SmPC warnings and contraindications
- A comparison against standard myiasis management (larval removal, ivermectin) to establish any unmet need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

