---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
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

# Ibuprofen: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a non-steroidal anti-inflammatory drug (NSAID), originally used for inflammatory and degenerative joint conditions, headache and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **no clinical trials and no publications** supporting this prediction. It rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy, headache disorder, patent ductus arteriosus (from the knowledge graph; the UK authorisation record has no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ibuprofen is a non-selective cyclooxygenase (COX) inhibitor with analgesic and anti-inflammatory effects, and its efficacy in arthritis is well established.

Hunter-Thompson type acromesomelic dysplasia is a rare genetic skeletal disorder linked to variants in *GDF5* (CDMP1) and impaired cartilage formation. COX inhibition would not be expected to correct this developmental defect. The high score (0.997) most likely reflects the closeness of skeletal and joint terms in the knowledge graph to the approved arthritis indications, rather than a defined biological pathway. At most, ibuprofen might offer symptomatic pain relief, which is not disease modification.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.71% | No mechanistic link; genetic skeletal and enamel disorder |
| 3 | Myosclerosis | 99.68% | Possible symptomatic relief only; no evidence on fibrosis |
| 4 | Brachyolmia | 99.67% | No mechanistic link; genetic skeletal dysplasia |
| 5 | Brachydactyly-syndactyly syndrome | 99.66% | No mechanistic link; congenital malformation |
| 6 | Pseudoachondroplasia | 99.66% | Speculative symptomatic joint pain relief only (COMP variants; secondary osteoarthritis) |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.60% | No mechanistic link; developmental syndrome |

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

