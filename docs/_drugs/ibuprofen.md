---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Ibuprofen
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

## Ibuprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a non-steroidal anti-inflammatory drug (NSAID), originally used for inflammatory and degenerative joint conditions, headache and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **no clinical trials and no publications** supporting this prediction. It rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ibuprofen is a non-selective cyclooxygenase (COX) inhibitor with analgesic and anti-inflammatory effects, and its efficacy in arthritis is well established.

Hunter-Thompson type acromesomelic dysplasia is a rare genetic skeletal disorder linked to variants in *GDF5* (CDMP1) and impaired cartilage formation. COX inhibition would not be expected to correct this developmental defect. The high score (0.9974) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, ibuprofen might offer symptomatic pain relief, which is not disease modification.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 0.9971 | No mechanistic link; genetic skeletal and enamel disorder |
| 3 | Myosclerosis | 0.9968 | Possible symptomatic relief only; no evidence on fibrosis |
| 4 | Brachyolmia | 0.9967 | No mechanistic link; genetic skeletal dysplasia |
| 5 | Brachydactyly-syndactyly syndrome | 0.9966 | No mechanistic link; congenital malformation |
| 6 | Pseudoachondroplasia | 0.9966 | Speculative symptomatic joint pain relief only (COMP variants; secondary osteoarthritis) |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9960 | No mechanistic link; developmental syndrome |

All seven predictions have no registered trials and no literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010J0AAACAC | Ibuprofen oral suspension 100 mg/5 ml | Oral suspension | Not stated in the data compiled |

Ibuprofen is classed in the BNF as a non-steroidal anti-inflammatory drug. The authorisation number above is in a format that does not look like a standard MHRA PL number, so it should be verified against the MHRA register. The wider UK ibuprofen product range, including NICE-appraised uses, was not captured in the data compiled for this report.

## Safety Considerations

**Contraindications and cautions flagged by the knowledge graph** (these come from drug-disease links in the knowledge graph, not from product label text, and must be checked against the SmPC):

- **Cardiovascular and cerebrovascular:** hypertension, hypotension, stroke, cerebrovascular disorder, cerebral infarction, myocardial infarction
- **Gastrointestinal:** peptic ulcer disease, inflammatory bowel disease, gallbladder disease
- **Renal and hepatic:** kidney disease, liver disease, liver failure
- **Haematological:** thrombocytopenia, blood coagulation disease
- **Respiratory and neurological:** chronic obstructive pulmonary disease, epilepsy
- **Endocrine and metabolic:** diabetes mellitus, diabetic ketoacidosis, hypothyroidism, potassium deficiency
- **Other:** systemic lupus erythematosus, benign prostatic hyperplasia, substance abuse/dependence

**Drug interactions** (100 interactions were found; the first 20 returned are summarised here):

- **Major:** acetylsalicylic acid
- **Moderate:** corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, aprepitant, balsalazide, fenfluramine, dexfenfluramine, kanamycin, levofloxacin
- **Minor:** famotidine, ranitidine, cimetidine

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications, and no plausible mechanism by which COX inhibition would modify these genetic developmental disorders. Long-term NSAID use also carries gastrointestinal, renal and cardiovascular risks.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale linking COX inhibition to the target disease
- Preclinical or clinical evidence in the predicted indication
- Verified UK product details (dosage form, approved indication, authorisation number) and SmPC safety data
- A benefit-risk assessment for long-term NSAID use in the affected paediatric and adult populations, if symptomatic pain relief is the only goal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

