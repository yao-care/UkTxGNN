---
layout: default
title: Fluocinonide
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
description: "Fluocinonide: predicted new indication Alopecia mucinosa (evidence level L5). Approved use: Inflammatory skin conditions, including atopic eczema…"
monitor_inn: "Fluocinonide"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "alopecia areata", "Quinquaud's folliculitis decalvans", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome"]
---

# Fluocinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Fluocinonide: From Dermatitis and Inflammatory Skin Conditions to Alopecia Mucinosa
{: .text-alpha }

## One-Sentence Summary

Fluocinonide is a high-potency topical corticosteroid, originally used for inflammatory skin conditions such as eczema, dermatitis, and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for hair-loss disorders; the highest-ranked prediction with any supporting evidence is **alopecia areata**, with **1 indirectly related clinical trial** and **1 publication** (a case report).
Direct evidence for fluocinonide in the predicted indication is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory skin conditions, including atopic eczema, contact dermatitis, seborrheic dermatitis, neurodermatitis, discoid lupus erythematosus (the UK authorisation record contains no indication text) |
| Predicted New Indication | Alopecia mucinosa (top-ranked); alopecia areata (top-ranked prediction with any supporting evidence) |
| TxGNN Prediction Score | 0.9961 (alopecia mucinosa); 0.9959 (alopecia areata) |
| Evidence Level | L5 for alopecia mucinosa (model prediction only); L4 for alopecia areata (indirect evidence only) |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold (alopecia mucinosa); Hold, framed as a research question (alopecia areata) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, fluocinonide is a high-potency topical corticosteroid with anti-inflammatory and immunosuppressive actions. Its efficacy in inflammatory dermatoses is established, and mechanistically it may be applicable to inflammatory hair-follicle disorders.

The predicted indications fall mainly into the alopecia group, and their plausibility varies considerably:

- **Alopecia areata** is an autoimmune, T-cell-mediated attack on hair follicles. Topical and intralesional corticosteroids are an established treatment class, so local immunosuppression is biologically coherent. The retrieved evidence does not, however, test fluocinonide directly.
- **Alopecia mucinosa (follicular mucinosis)** is an inflammatory follicular disorder. A mechanistic rationale exists and topical corticosteroids are used empirically, but no trials or publications were found.
- **Folliculitis decalvans** is a neutrophilic scarring alopecia with a bacterial component. Corticosteroids might help as an adjunct, but antibiotics are the primary therapy.
- **Telogen effluvium** is mainly a non-inflammatory, trigger-driven shedding disorder, so the link to a corticosteroid is weak.
- **Rare genetic or immunodeficiency syndromes** (hereditary hypotrichosis with recurrent skin vesicles, alopecia antibody deficiency, alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome) have no plausible mechanistic link to a topical steroid. Their high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related alopecia diseases, not biological evidence.

---

## Clinical Trial Evidence

No clinical trials were found for alopecia mucinosa. For alopecia areata, one trial was retrieved, and it studies a different condition:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicentre prospective study comparing treatment outcomes between groups, using before-and-after photographs, in central centrifugal cicatricial alopecia (CCCA). CCCA is a scarring alopecia, not alopecia areata, and the role of fluocinonide is not confirmed. Indirect support only. |

No ISRCTN or EU Clinical Trials Register entries were identified. No trials were found for the other predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | Journal of the American Academy of Dermatology | Four cases of congenital alopecia areata followed for 3 to 5 years. Hair loss had prolonged quiet periods, and treatments included minoxidil 2% and a range of topical agents. It does not establish the efficacy of fluocinonide. |

No literature was found for the other predicted indications.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1304000P0AABABA | Fluocinonide Ointment 0.05% | Ointment (per product name) | Not recorded in the data compiled for this report |

One valid single-ingredient authorisation is recorded; there are no combination products and none have been cancelled. The data compiled for this report do not include NICE-appraised indications or BNF classification details. Please check the current MHRA records and the BNF.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen identified 64 potential interacting drugs, but none has a graded severity (all are listed as "Unknown"). Examples include other corticosteroids (triamcinolone, prednisone, budesonide, dexamethasone, fluticasone), cyclosporine, clopidogrel, acetylsalicylic acid, ibuprofen, and several acid-suppressing drugs (omeprazole, lansoprazole, famotidine). These should be treated as unverified signals and checked against the SmPC and BNF.
- **Conditions flagged in the knowledge graph**: Drug-disease contraindication links (not label text) include hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, Cushing syndrome, adrenal gland hyperfunction, and various pituitary hormone deficiency disorders. These are consistent with the systemic effects of corticosteroids and should be considered if substantial absorption occurs (for example, extensive use, occlusion, or use on broken skin).

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest almost entirely on the TxGNN score. The only retrieved trial concerns a different alopecia and the only publication is a case report, so alopecia areata is best treated as a research question rather than a supported indication. Alopecia mucinosa has a plausible rationale but no evidence at all.

**To proceed, the following is needed:**
- Mechanism of action data for fluocinonide
- Label warnings and contraindications from the SmPC and BNF (not available in the data compiled for this report)
- Approved indication text and dosage form for the UK authorisation
- Direct comparative or controlled studies of topical fluocinonide in alopecia areata or alopecia mucinosa
- Confirmation of whether fluocinonide was a studied treatment in NCT04207931
- Assessment of scalp application, including route suitability and the risk of systemic absorption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

