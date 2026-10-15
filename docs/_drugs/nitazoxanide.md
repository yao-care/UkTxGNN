---
layout: default
title: Nitazoxanide
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Nitazoxanide
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

# Nitazoxanide: From Giardiasis and Cryptosporidiosis to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Nitazoxanide is an antiparasitic drug originally used to treat giardiasis and cryptosporidiosis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Giardiasis, cryptosporidiosis (the authorisation record supplied contains no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 97.82% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nitazoxanide is a thiazolide antiparasitic with broad antiprotozoal, antibacterial and antiviral activity. Its efficacy in giardiasis and cryptosporidiosis is established.

Polyclonal hyperviscosity syndrome is caused by raised polyclonal immunoglobulin levels thickening the blood. No plausible mechanism links nitazoxanide to this condition, and the high score most likely reflects patterns in the knowledge graph rather than a pharmacological rationale. The prediction should therefore be regarded as a hypothesis only.

Other top-ranked predictions (for example hyperamylasemia, congenital analbuminemia, monoclonal gammopathy and plague) are likewise unsupported by any trial or publication in the data compiled for this report. Nitazoxanide has some preclinical anticancer reports, which give a speculative link to haematological conditions, but this is not backed by the data supplied.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501070ABAAAAAA (BNF code) | Nitazoxanide tablets 500 mg | Tablet | Indication text not available in the data compiled |

The identifier shown is a BNF-style product code rather than an MHRA PL number. The BNF classification (section 5.4.8 range, antiprotozoal drugs) should be confirmed against the current BNF entry.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-derived associations, not label text): kidney disease, pyoureter, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis.
- **Drug Interactions**: 22 interactions were recorded, all rated Moderate. The main groups are:
  - Sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide)
  - Coumarin anticoagulants (warfarin, dicoumarol)
  - Benzodiazepines (clorazepic acid, diazepam, estazolam, flurazepam, lorazepam, midazolam, oxazepam, quazepam)
  - Lidocaine, methotrexate and phenytoin

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no trials, no publications and no plausible mechanistic link to polyclonal hyperviscosity syndrome. Safety signals (hepatic and renal disease, diabetes, and interactions with warfarin and sulfonylureas) add further caution.

**To proceed, the following is needed:**
- Mechanism of action data for nitazoxanide, and a defined mechanistic hypothesis for hyperviscosity
- Preclinical or clinical evidence in the predicted indication
- The MHRA SmPC, including indication, warnings and contraindications, to complete safety screening
- Confirmation of the UK authorisation details (PL number, dosage form and approved indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

