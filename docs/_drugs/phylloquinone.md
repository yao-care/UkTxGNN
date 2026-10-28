---
layout: default
title: Phylloquinone
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "Phylloquinone"
predicted_indications: ["renal tubular acidosis", "hypophosphatemic rickets", "Pendred syndrome", "autosomal recessive nonsyndromic deafness", "leukocyte adhesion deficiency", "Fraser syndrome", "temtamy preaxial brachydactyly syndrome"]
description: "Phylloquinone: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Phylloquinone
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

## Phylloquinone: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Phylloquinone (vitamin K1, also called phytomenadione) was originally used for bone and calcium-related conditions such as osteoporosis, and for congenital prothrombin deficiency.
The TxGNN model predicts it may be effective for **renal tubular acidosis**, but this is a computational prediction only, with **no clinical trials** and **no publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, phylloquinone is vitamin K1, a cofactor for gamma-carboxylation of vitamin K-dependent proteins, including bone and calcium-regulating proteins such as osteocalcin and matrix Gla protein.

Renal tubular acidosis can involve bone demineralisation and nephrocalcinosis. These overlap with phylloquinone's listed indications of nephrocalcinosis, hypercalcaemia and osteoporosis. That overlap is the plausible, but unverified, link behind the prediction.

There is no direct evidence that vitamin K affects the underlying acid-base or tubular transport defect. The prediction should be treated as a hypothesis, not a supported finding.

### Other Predicted Indications (for context)

All other predictions in the data compiled for this report are also evidence level L5 with a Hold recommendation, and none has trials or literature.

| Predicted Indication | TxGNN Score | Mechanistic Plausibility |
|------|------|------|
| Hypophosphataemic rickets | 0.9967 | Indirect link via phosphorus and bone metabolism; the core FGF23-mediated defect is not known to be affected by vitamin K |
| Pendred syndrome | 0.9956 | No clear mechanistic link |
| Autosomal recessive nonsyndromic deafness | 0.9951 | No identified mechanistic link |
| Leukocyte adhesion deficiency | 0.9947 | Unsupported by mechanism |
| Fraser syndrome | 0.9922 | Unsupported; possible signal from warfarin embryopathy overlap |
| Temtamy preaxial brachydactyly syndrome | 0.9908 | Unsupported |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0906060Q0AAAEAE (BNF-style product code, not a PL number) | Phytomenadione capsules 1 mg | Capsule | Not available |

Only one valid single-ingredient authorisation is recorded. Please refer to the SmPC and BNF for the approved indications and dosing.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph.** These come from drug-disease association edges in the TxGNN knowledge graph, not from product label text, so they should be verified against the SmPC. Conditions listed include:

- Renal and calcium/phosphate disorders: kidney disease, nephrolithiasis, nephrocalcinosis, hypercalcaemia, hyperphosphataemia, hyperparathyroidism, osteitis fibrosa, acute urate nephropathy, pyoureter, phosphorus metabolism disorders
- Metabolic and other conditions: diabetes mellitus, diabetic ketoacidosis, sarcoidosis, hypervitaminosis, constipation, arteriosclerosis obliterans, familial isolated vitamin E deficiency
- Cancers: breast, prostate, cervical and endometrial cancers, and lytic metastatic bone lesions

Several of these (kidney disease, nephrocalcinosis, hypercalcaemia) are relevant to the predicted renal indication and would need careful review.

**Drug Interactions.** The database query returned 100 interactions. Among those listed, only two were graded and both were Minor: **mineral oil** and **orlistat**, which may reduce absorption of fat-soluble vitamins. The remainder, including proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), sucralfate, metronidazole, prednisone, hydrocortisone, simvastatin and acetylsalicylic acid, have no severity grading.

Please refer to the SmPC and BNF for warnings and full interaction information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5), with no clinical trials or literature, an unverified mechanistic link, and several contraindications that overlap with renal disease. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Mechanism of action data for phylloquinone
- A systematic literature search on vitamin K in renal tubular acidosis, and on bone and nephrocalcinosis outcomes
- SmPC warnings, contraindications and approved indication text for the UK product
- Verification of the knowledge-graph contraindications against label information
- Preclinical or exploratory clinical data supporting an effect on bone or calcium handling in renal tubular acidosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

