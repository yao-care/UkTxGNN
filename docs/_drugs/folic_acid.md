---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 303
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin deficiency disorder"
monitor_inn: "Folic acid"
predicted_indications: ["biotin metabolic disease"]
---

# Folic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Folic Acid: From Folic Acid Deficiency Anaemia to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid is a water-soluble B vitamin, originally used to treat vitamin deficiency and folate-deficiency anaemia.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**, but **no clinical trials** and only **general vitamin review literature** (20 publications, none directly testing this use) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; folic acid deficiency anaemia (approved indication text not available in the UK licence data) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, folic acid is a B vitamin that acts as a cofactor in one-carbon metabolism. Its efficacy in folate-deficiency anaemia is well established.

Folic acid and biotin are both water-soluble B vitamins involved in cellular metabolism, so a shared nutritional or metabolic pathway is plausible. The high TxGNN score reflects proximity in a knowledge graph, which is a computational association and not evidence of treatment benefit.

There are important reasons for caution. Folate does not substitute for biotin in biotin-dependent carboxylases, for example in holocarboxylase synthetase or biotinidase deficiency, where the standard treatment is biotin supplementation. The literature supplied contains general vitamin reviews and gives no direct evidence that folic acid treats biotin metabolic disease. The prediction should therefore be regarded as a hypothesis with weak mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomised trials were identified. The most relevant publications are reviews of vitamin-responsive and vitamin-related metabolic conditions; none tests folic acid in biotin metabolic disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders (cobalamin, folate, biotin, B1, E). Describes inborn errors of vitamin metabolism, each with its own specific vitamin treatment |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | International Journal of Molecular Sciences | Vitamin B12 deficiency and the nervous system; notes B12, folate and biotin act in linked biochemical reactions |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases: malabsorption, metabolic errors and vitamin-dependent syndromes |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; lower thiamine, pyridoxine and biotin levels noted in diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | Vitamins and type 2 diabetes; biotin among the B vitamins found reduced |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | Overview of B vitamins in cellular metabolism and dermatology |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Archives of Biochemistry and Biophysics | Micronutrient deficiencies (including folic acid) and DNA damage; general supplementation argument |
| [38350491](https://pubmed.ncbi.nlm.nih.gov/38350491/) | 2025 | Cohort | Nutrition Reviews | Micronutrient status in children with severe wasting; relevant to nutritional rehabilitation, not biotin disease |
| [16183151](https://pubmed.ncbi.nlm.nih.gov/16183151/) | 2006 | Animal study | International Journal of Cardiology | Folic acid reduced VCAM-1 expression in rats with hyperhomocysteinaemia; not related to biotin |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Biotin deficiency and combined biotin and folic acid deficiency induced in rats; historical |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0901020G0AAAGAG | Folic Acid Tablets 5 mg | Tablet (form not specified in data) | Not specified in the data compiled for this report |

One single-ingredient authorisation is recorded as valid. Refer to the BNF (vitamins and minerals, folic acid) and the SmPC for the licensed indications and dosing.

## Safety Considerations

Data from the knowledge graph (not label text) link folic acid to a number of conditions listed as contraindication associations, including:
- **Haematological:** sickle cell anaemia, haemolytic anaemia, hereditary haemochromatosis, haemosiderosis, iron metabolism disease
- **Renal and metabolic:** kidney disease, nephrolithiasis, primary hyperoxaluria, hypercalcaemia, hyperparathyroidism, diabetes mellitus, diabetic ketoacidosis
- **Gastrointestinal:** peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, diarrhoeal disease, constipation
- **Other:** bipolar disorder, sarcoidosis, Wilson disease

These associations are computational and should be verified against the SmPC. Many may reflect the wider vitamin and mineral drug class and not folic acid specifically.

**Drug Interactions:** The interaction screen returned 100 potential interactions, mostly of unknown severity. The graded ones are:
- Pancrelipase (Moderate)
- Sulfasalazine (Minor)

Others listed with unknown severity include mesalazine, metformin, omeprazole, pantoprazole, lansoprazole, prednisone and simvastatin.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5). There are no registered trials, and the literature gives no direct support. Established biology indicates biotin, not folic acid, is the treatment for biotin metabolic disease.

**To proceed, the following is needed:**
- Clear definition of the target condition (for example, biotinidase or holocarboxylase synthetase deficiency) and a rationale for any role of folic acid beyond biotin
- Mechanism of action data for folic acid
- Mechanistic or preclinical studies showing a benefit of folic acid in biotin-related disease
- Licensed indication text and dosage form details from the SmPC, and verification of label contraindications and warnings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

