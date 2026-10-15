---
layout: default
title: Piracetam
parent: Model Prediction Only (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
---

# Piracetam
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

# Piracetam: From Myoclonus to Osteoarthritis

## One-Sentence Summary

Piracetam is a racetam nootropic that is marketed in the UK and is used for myoclonus, alongside other anti-myoclonic therapies.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **no clinical trials and no publications** were found in the data compiled for this report to support this direction.
The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myoclonus, in combination with other anti-myoclonic therapies (the authorisation record contains no indication text; this is taken from the pharmacology data) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.45% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Piracetam is a racetam nootropic. Its proposed effects include changes in membrane fluidity, modulation of AMPA-type glutamate receptors, and effects on microcirculation and platelet function. The pharmacology data list GluA1, GluA2, GluA3 and GluA4 (the AMPA receptor subunits) as targets.

**This prediction is not mechanistically supported.** None of these proposed actions has a demonstrated link to cartilage degeneration or joint inflammation. The high score is most likely a product of proximity within the knowledge graph rather than a real therapeutic signal. Without mechanism data, the relationship between the original and new indication cannot be assessed.

The other top-ranked predictions show the same pattern. They are mostly joint, skeletal or connective-tissue conditions, and none has trial or literature support:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Osteoarthritis susceptibility | 98.26% | A genetic susceptibility phenotype, not a treatable condition |
| 3 | Rheumatoid arthritis | 98.02% | Piracetam's haemorheological and antiplatelet effects are not linked to autoimmune synovial inflammation |
| 4 | Pseudoachondroplasia | 97.63% | Rare skeletal dysplasia (COMP mutations); no known link |
| 5 | Hepatic porphyria | 97.55% | No rationale; would also need a porphyrinogenicity safety review |
| 6 | Gout | 97.54% | No evidence of an effect on urate metabolism |
| 7 | Brachyolmia | 97.45% | Rare skeletal dysplasia; no pharmacological link |
| 8 | Acromesomelic dysplasia, Hunter-Thompson type | 97.31% | CDMP1/GDF5 pathway; no known effect |
| 9 | Myosclerosis | 97.19% | Rare myopathy; no evidence |
| 10 | Hepatopulmonary syndrome | 97.18% | Microcirculatory effects not established as relevant |

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
| 0409030P0AAAAAA (BNF code) | Piracetam oral solution 333.3 mg/1 ml | Oral solution | Not recorded in the compiled data; pharmacology data describe UK use for myoclonus alongside other anti-myoclonic therapies |

Only one authorisation record is available. The number shown is a BNF-style product code rather than a standard PL number, so the MHRA record should be checked directly. Piracetam is not approved by the US FDA but is authorised in several other European, Asian and South American countries.

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with 4 entries. All are pharmacological target associations (AMPA receptor subunits GluA1, GluA2, GluA3 and GluA4, encoded by *GRIA1–4*), not clinical drug–drug interactions. No graded interaction levels were reported.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score. No trials or publications exist, no plausible mechanistic link to osteoarthritis has been identified, and the safety data (warnings and contraindications) are incomplete.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper assessment of any link to joint or cartilage pathology
- Systematic literature and trial searches on piracetam in osteoarthritis, including preclinical studies
- Warnings and contraindications from the current SmPC and BNF, which is a blocking gap for safety screening
- Verification of the MHRA authorisation record, including the approved indication text, dosage forms and the correct PL number
- Assessment of whether the available oral formulation suits the intended use in osteoarthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

