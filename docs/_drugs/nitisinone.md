---
layout: default
title: Nitisinone
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Tyrosinaemia to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone was originally used to treat hereditary tyrosinaemia. The TxGNN model predicts it may be effective for **renal tubular acidosis**, but **no clinical trials and no publications** currently support this direction. This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tyrosinaemia (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the rationale in the data, nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD) and is used in hereditary tyrosinaemia type 1. In that condition, renal tubular dysfunction (Fanconi-type proximal tubulopathy) is a recognised feature.

The link to renal tubular acidosis is therefore indirect. Treatment may improve tubular function secondary to tyrosinaemia, but nothing suggests it treats primary renal tubular acidosis. The high TxGNN score most likely reflects network proximity to tyrosinaemia-associated tubulopathy rather than a validated mechanism.

Other predictions are weaker still. These include galactosaemia, glycogen storage disease, serpin-related disorders (alpha-1 antitrypsin deficiency and C1 inhibitor deficiency), Griscelli syndrome and X-linked chronic granulomatous disease. Most share only liver-disease or metabolic-network features with tyrosinaemia, and none has a plausible direct mechanism. For galactosaemia and glycogen storage disease, the only support is general paediatric hepatology reviews.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature is available for renal tubular acidosis.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0908010AFAAAAAA | Nitisinone capsules 2 mg | Capsule | Not available in the compiled data |

The data compiled for this report lists one valid single-ingredient authorisation. The authorisation number appears to be a non-MHRA format, so it should be checked against the MHRA product database. Dosage form and indication text are missing. NICE appraisal and BNF classification information is not included in the compiled data.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): kidney disease, pyoureter, thrombocytopenia, leukopenia, hypophosphataemia and tyrosinaemia. These are database associations and need confirming against the SmPC.
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Most of those listed are of moderate severity, with armodafinil rated minor. Examples include:
  - amiodarone
  - amlodipine
  - nifedipine
  - ibuprofen
  - dexamethasone
  - pioglitazone
  - isotretinoin
  - abiraterone
  - apalutamide
  - aprepitant
  - atazanavir
  - baricitinib
  - bexarotene
  - bicalutamide
  - aldesleukin
  - amobarbital
  - avatrombopag
  - abametapir (topical)
  - ginger

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it (evidence level L5), and the proposed link to renal tubular acidosis is indirect and secondary to tyrosinaemia. Label-based safety data are also missing. The other nine predictions are similarly unsupported or only weakly supported by indirect reviews (L4–L5).

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic analysis
- SmPC warnings and contraindications for the UK product, to complete safety screening
- Confirmation of the UK authorisation details (MHRA licence number, dosage form, approved indication)
- Evidence that nitisinone affects primary renal tubular acidosis, such as preclinical or mechanistic studies, or case series
- Review of renal and haematological safety signals (kidney disease, thrombocytopenia, leukopenia, hypophosphataemia) in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

