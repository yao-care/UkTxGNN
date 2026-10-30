---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 385
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
description: "Mebendazole: predicted new indication Acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Mebendazole
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

## Mebendazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Mebendazole is an anthelmintic (worm-killing) medicine, originally used for threadworm (enterobiasis), roundworm (ascaridiasis) and whipworm (trichuriasis) infections.
The TxGNN model predicts it may be effective for **acne**, but **no clinical trials** and only **1 publication** were found, and that publication is unrelated to acne. The prediction is computational only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mebendazole is a benzimidazole anthelmintic. It is generally understood to bind parasite beta-tubulin, which blocks microtubule formation and glucose uptake in the worm.

This mechanism explains its activity against intestinal worms, but it does not obviously apply to acne. Acne involves excess sebum production, *Cutibacterium acnes* colonisation and inflammation of the hair follicle. No credible mechanistic link between tubulin inhibition and these processes has been established.

The high TxGNN score (0.9920) should therefore be read as a computational signal, not clinical support. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | Am J Trop Med Hyg | Describes a patient in Venezuela with proliferative sparganosis (a tapeworm larval infection) who had acne-like skin lesions. It does not study acne or mebendazole as an acne treatment, so it is **off-topic** |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0505010D0AAAAAA | Mebendazole Oral Suspension 100mg/5ml | Oral suspension (from product name) | Not specified in the data compiled |

The identifier above resembles a BNF-style classification code (BNF chapter 5, infections) rather than a standard PL number. Please check the MHRA register for the official authorisation details and approved indications.

---

## Safety Considerations

- **Contraindications (knowledge-graph links, not label text):** liver disease and gallbladder disease.
- **Drug Interactions (10 recorded, from DDInter):**
  - **Moderate:** metronidazole, phenobarbital, carbamazepine, phenytoin, fosphenytoin, primidone, ritonavir, iodide I-131, iodide I-123.
  - **Minor:** cimetidine.
  - Several of these are anticonvulsants, which may lower mebendazole exposure through enzyme induction.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction rests only on a model score. There are no registered trials, the single retrieved publication is off-topic, and no plausible mechanism links mebendazole to acne pathology.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis, supported by laboratory or preclinical data
- Any clinical or observational data on mebendazole in acne
- Formal mechanism of action data and full SmPC safety information

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

