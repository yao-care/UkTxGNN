---
layout: default
title: Methionine
parent: Moderate Evidence (L3-L4)
nav_order: 399
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Methionine: predicted new indication Acne (disease) (evidence level L4). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Methionine"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "mature cataract", "immature cataract", "nuclear senile cataract", "cortical cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "craniostenosis cataract", "diabetic cataract"]
---

# Methionine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Methionine: From Unspecified Original Indication to Acne (Disease)

## One-Sentence Summary

Methionine is an essential sulphur-containing amino acid, marketed in the UK as a 250 mg tablet, but the compiled data do not state an approved original indication.
The TxGNN model predicts it may be effective for **acne**, but there are **no clinical trials** and only **2 tangential publications** (a case report and a cohort study), and neither supports a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Methionine is an essential amino acid and a precursor of homocysteine through the methionine cycle, but the approved indication for the UK product is not recorded in the compiled data, so a link between the original use and acne cannot be established.

The retrieved literature does not support methionine as an acne treatment. One paper reports raised plasma homocysteine (a methionine-cycle metabolite) in patients taking isotretinoin for cystic acne, which suggests a drug-induced metabolic change rather than a therapeutic benefit. The other is a case report of an MTHFR mutation in a neonate, which is unrelated to acne treatment. Supplementing methionine could plausibly raise homocysteine, so the signal points towards potential harm rather than benefit. The very high TxGNN score is not backed by clinical or mechanistic data.

Other predicted indications (for example diabetic cataract, nuclear senile cataract and severe nonproliferative diabetic retinopathy) have similarly weak support. The most notable indirect signal is for diabetic cataract, where studies of methionine sulfoxide reductase B1 (MsrB1) link the repair of oxidised methionine to lens cell protection. That work concerns repair of oxidised methionine residues, not methionine supplementation, so it is best treated as a research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | Int J Dermatol | Plasma homocysteine was elevated in patients on isotretinoin for cystic acne. This is a metabolic association, not evidence of benefit from methionine. |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | A neonate with a novel MTHFR mutation presented with encephalopathy, hair loss, marfanoid features and neonatal acne. It is unrelated to acne treatment. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1902070M0AAAAAA | Methionine Tab 250mg | Not stated | Not stated |

The authorisation number is recorded as supplied in the compiled data and does not follow the usual PL format, so it should be verified against the MHRA register. No NICE-appraised or BNF classification details were available.

---

## Safety Considerations

- **Drug Interactions** (5 recorded):
  - Moderate: activated charcoal
  - Minor: ephedrine, pseudoephedrine, mexiletine, flecainide
- **Conditions flagged by the knowledge graph** (drug-disease contraindication links in the TxGNN knowledge graph, not label text, so they need verification against the SmPC):
  - Cardiovascular and metabolic: hypertension, heart disease, cardiovascular disease, hyperlipidaemia (including familial), diabetes mellitus, diabetic ketoacidosis, ventricular fibrillation, digitalis poisoning
  - Renal: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
  - Calcium and phosphorus: hypercalcaemia, humoral hypercalcaemia of malignancy, sarcoidosis, phosphorus metabolism disorder
  - Amino acid metabolism: phenylketonuria and other disorders of phenylalanine metabolism

Product-specific warnings and contraindications were not available. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, the two retrieved papers do not show benefit, and raised homocysteine suggests a possible risk rather than a therapeutic effect. The knowledge-graph safety flags (cardiovascular, renal and metabolic) add further caution.

**To proceed, the following is needed:**
- The approved indication and SmPC safety information for the UK methionine tablet
- Mechanism of action data (for example from DrugBank)
- A plausible mechanistic rationale and preclinical data for methionine in acne, including the effect on homocysteine
- Consideration of reframing the diabetic cataract signal (MsrB1 and methionine sulfoxide repair) as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

