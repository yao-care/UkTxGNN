---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 163
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ciclesonide: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma, intrinsic asthma, allergic asthma, allergic rhinitis…"
monitor_inn: "Ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis", "asthma-related traits, susceptibility to"]
---

# Ciclesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ciclesonide: From Asthma and Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid prodrug, originally used for asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but this rests on a model prediction alone, with **no clinical trials** and **no publications** currently supporting this specific direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, intrinsic asthma, allergic asthma, allergic rhinitis, vasomotor rhinitis (the licence record held no indication text) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ciclesonide is an inhaled corticosteroid prodrug. Esterases activate it to des-ciclesonide, a glucocorticoid receptor agonist with anti-inflammatory activity.

Atopic eczema is a Th2-driven inflammatory skin disease, and topical corticosteroids are an established treatment. A glucocorticoid mechanism is therefore biologically plausible. Asthma and allergic rhinitis are also Th2-type allergic conditions, which gives the original and predicted indications a shared inflammatory basis.

There are important limits. The score is a prediction only. Ciclesonide is formulated for inhalation or intranasal delivery, not for the skin, and route compatibility has not yet been assessed. "Dermatitis, atopic" (rank 3) is a synonym of atopic eczema, so the two entries should be merged to avoid double-counting.

### Other Predicted Indications

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | 2-Hydroxyethyl methacrylate sensitisation | 99.76% | L5 | Contact allergy. Corticosteroids only control symptoms, and there is no supporting evidence. |
| 3 | Dermatitis, atopic | 99.73% | L5 | Duplicate of atopic eczema. |
| 4 | Bronchitis | 99.70% | L4 | Only indirect support from a COPD guideline. |
| 5 | Contact dermatitis | 99.25% | L4 | The only publication is a safety signal, not evidence of benefit. |
| 6 | Asthma-related traits, susceptibility to | 99.13% | L5 | A genetic trait term that overlaps with the approved asthma indication. It should be excluded or reclassified. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications were found for atopic eczema. The publications below relate to other predicted indications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review (guideline) | Basic & Clinical Pharmacology & Toxicology | Finnish national guideline on diagnosis and pharmacotherapy of stable COPD. This is indirect evidence for bronchitis and does not show ciclesonide efficacy. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Systemic allergic dermatitis caused by inhaled budesonide, with patch-test cross-reactivity to ciclesonide. This is a safety signal rather than evidence of benefit. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0302000U0AAACAC | Ciclesonide inhaler 160 microgram (60 doses) | Inhalation | Not available |

The reference number follows a BNF-style code (British National Formulary section 3, respiratory system) rather than a standard PL number. One authorisation is recorded, and it is a single-ingredient product.

## Safety Considerations

- **Drug Interactions**: 63 interactions were identified. Those listed below are examples from the first 20 returned, and the full list should be checked in the BNF.
  - **Major**: cladribine.
  - **Moderate**: clarithromycin, miconazole, cobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, conivaptan, fostamatinib, inhaled insulin, topical abametapir. Several of these are CYP3A4 inhibitors that may raise corticosteroid exposure.
  - **Minor**: formoterol, salbutamol, arformoterol.
  - **Unknown severity**: omeprazole, lansoprazole, famotidine, prednisolone.
- **Disease associations flagged in the knowledge graph** (not label text): herpes simplex keratitis, adrenocortical insufficiency, Addison disease, osteoporosis, postmenopausal osteoporosis, fungal infection, dermatophytosis, ocular hypertension, glaucoma and parasitic infection. These should be verified against the SmPC.
- **Specific caution for the contact dermatitis prediction**: corticosteroids can themselves cause contact allergy, and cross-reactivity with budesonide has been reported.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications rest on model scores with no supporting trials. Atopic eczema has established corticosteroid therapy, but ciclesonide is formulated for inhalation or intranasal use and has no published evidence in this setting. The only dermatological publication points to a safety concern.

**To proceed, the following is needed:**
- Mechanism of action data, and SmPC warnings and contraindications for formal safety screening
- Route and formulation compatibility assessment, since no dermal formulation is available
- Merging of the duplicate atopic eczema and atopic dermatitis entries
- Preclinical or early clinical evidence of benefit in atopic eczema
- Comparison with existing topical corticosteroids and a review of the contact allergy cross-reactivity risk
- Completion of the licence record, including dosage form, manufacturer and approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

