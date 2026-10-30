---
layout: default
title: Methionine
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
monitor_inn: "Methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "nuclear senile cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "immature cataract", "craniostenosis cataract", "mature cataract", "tetanic cataract", "diabetic cataract"]
last_modified_at: 2026-10-30
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Methionine
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

## Methionine: From No Recorded Original Indication to Acne (Disease)
{: .text-alpha }

## One-Sentence Summary

Methionine is an essential sulfur-containing amino acid. The data compiled for this report contain no approved indication text for it in the UK.
The TxGNN model predicts it may be effective for **acne (disease)**, but there are **0 clinical trials** and **2 publications** (a case report and a cohort study), neither of which tests methionine as a treatment. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available. Methionine is an essential amino acid that is a precursor of homocysteine, cysteine and S-adenosylmethionine, and it is involved in methylation and sulfur metabolism. No approved indication text was available, so the relationship between an original indication and acne cannot be described.

The two retrieved papers do not show that methionine treats acne. One reports raised plasma homocysteine in patients taking isotretinoin for cystic acne. The other is a case report of an MTHFR mutation in a neonate with, among other features, neonatal acne. Both relate to methionine/homocysteine metabolism only indirectly. The very high TxGNN score is a model output without clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | Int J Dermatol | Plasma homocysteine was elevated in patients on isotretinoin for cystic acne; methionine was not tested as a treatment |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | Neonate with a novel MTHFR mutation, encephalopathy, hair loss, marfanoid features and neonatal acne; no methionine treatment effect shown |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1902070M0AAAAAA | Methionine Tab 250mg | Not stated | Not stated |

The licence record lists no dosage form or approved indication text, so no approved use can be described from it.

---

## Safety Considerations

**Contraindications recorded in the knowledge graph** (these are drug–disease relations in the TxGNN knowledge graph, not label text) include:
- Cardiovascular: hypertension, hypertensive disorder, heart disease, cardiovascular disease, hyperlipidaemia, familial hyperlipidaemia, ventricular fibrillation, digitalis poisoning
- Renal: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hypercalcaemia, humoral hypercalcaemia of malignancy, sarcoidosis, phosphorus metabolism disease, phenylketonuria, disorders of phenylalanine metabolism

**Drug Interactions** (5 recorded):
- Activated charcoal: Moderate
- Ephedrine, pseudoephedrine, mexiletine, flecainide: Minor

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trial or publication tests methionine for acne, so the evidence level is L5. The knowledge-graph contraindication list is also extensive.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking methionine to acne
- Approved indication and label text from the UK licence record, plus SmPC warnings and contraindications
- Any controlled clinical data on methionine in acne
- A safety assessment covering the cardiovascular, renal and metabolic conditions listed above

---

## Other Predicted Indications (Summary)

None of the following has a clinical trial. All are recommended as Hold, except diabetic cataract, which is a research question only.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Severe nonproliferative diabetic retinopathy | 1.0000 | L5 | Prediction only; no literature |
| 3 | Nuclear senile cataract | 1.0000 | L5 | Laboratory papers show methionine oxidation in cataractous lenses; none studies methionine as a treatment |
| 4 | Diabetes mellitus type 2 associated cataract | 1.0000 | L5 | Prediction only |
| 5 | Cortical cataract | 1.0000 | L5 | Lens biology and metabolomics papers only |
| 6 | Immature cataract | 1.0000 | L5 | Prediction only |
| 7 | Craniostenosis cataract | 1.0000 | L5 | Prediction only; rare syndromic condition |
| 8 | Mature cataract | 1.0000 | L5 | One crystallin photoaggregation study, unrelated to methionine treatment |
| 9 | Tetanic cataract | 1.0000 | L5 | Prediction only |
| 10 | Diabetic cataract | 1.0000 | L5 | Review of homocysteine in eye disease and laboratory studies of methionine sulfoxide reductase B1 (MsrB1) in lens cells; none tests methionine administration |

For diabetic cataract, the MsrB1 findings (PMIDs [22713178](https://pubmed.ncbi.nlm.nih.gov/22713178/), [23270945](https://pubmed.ncbi.nlm.nih.gov/23270945/)) and the homocysteine review ([26343924](https://pubmed.ncbi.nlm.nih.gov/26343924/)) show involvement of the methionine redox system, not a benefit of methionine supplementation. Raised homocysteine is associated with eye disease, so supplementation carries a plausible safety concern. A research question is warranted only on the repair-pathway biology.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

