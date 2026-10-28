---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 192
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Cyanocobalamin: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin B12 deficiency…"
monitor_inn: "Cyanocobalamin"
predicted_indications: ["biotin metabolic disease"]
---

# Cyanocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease
{: .text-alpha }

## One-Sentence Summary

Cyanocobalamin (vitamin B12) is originally used to treat vitamin B12 deficiency and related anaemias, including pernicious anaemia.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**, but this is a model prediction only: **no clinical trials** and only **1 publication** (a general review of vitamin production, not a clinical study) were found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, pernicious anaemia and other deficiency anaemias (the UK authorisation record contains no indication text) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, cyanocobalamin is a cofactor for methionine synthase and methylmalonyl-CoA mutase. Biotin is a cofactor for carboxylases such as propionyl-CoA carboxylase. Both pathways feed into propionate and methylmalonate metabolism, so a plausible but unverified link may exist through shared organic acid metabolism.

However, the link is weak. Biotin-responsive disorders, such as biotinidase deficiency and holocarboxylase synthetase deficiency, are treated with biotin, not vitamin B12. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No direct mechanistic link between cyanocobalamin and biotin metabolism is established in the data supplied.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | Overview of biotechnological production of vitamins, coenzymes and related biochemicals. It does not address treating biotin metabolic disease with cyanocobalamin. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0901020D0AAAEAE (BNF code) | Cyanocobalamin Tablets 50 microgram | Tablet | Not stated in the data compiled |

Only one single-ingredient product is recorded, and it is currently valid. The identifier shown is a BNF-style code rather than an MHRA PL number, so the MHRA record should be checked directly.

---

## Safety Considerations

**Drug interactions:** The data compiled for this report lists 100 potential interactions. The 20 shown are mostly of minor severity or unclassified.

- **Minor:** acid-suppressing drugs (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole) and potassium chloride. These are generally linked to reduced B12 absorption.
- **Severity not classified:** metformin, glimepiride, acarbose, rosiglitazone, mesalazine, doxycycline, sucralfate and morphine.

Please refer to the SmPC and BNF for warnings and contraindications, as label-based data were not available. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no registered trials, no relevant clinical literature and no established mechanistic link. Established treatment for biotin-related disorders is biotin itself.

**To proceed, the following is needed:**
- Mechanism of action data for cyanocobalamin, to test any link to biotin-dependent pathways
- Targeted literature review on vitamin B12 in biotinidase and holocarboxylase synthetase deficiency, and in organic acid disorders
- Label warnings and contraindications from the SmPC and BNF
- Confirmation of the MHRA authorisation number and approved indication for the listed product
- Preclinical or biochemical evidence before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

