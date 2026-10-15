---
layout: default
title: Indomethacin
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indomethacin: From Inflammatory Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Indomethacin is an NSAID used for inflammatory and degenerative joint conditions such as rheumatoid arthritis, ankylosing spondylitis and gout, and for patent ductus arteriosus.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
**No clinical trials and no publications** currently support this prediction, so it rests on the model's graph-based score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, gout, osteoarthritis, bursitis, tendinitis, frozen shoulder, patent ductus arteriosus (among others; taken from the knowledge-graph indication list, as no licensed indication text was available) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.97% (model rank 350) |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, indomethacin is a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation, and this effect is well established in inflammatory arthritis and gout.

Brachydactyly-syndactyly syndrome is a rare congenital limb malformation caused by abnormal skeletal development. It is not an inflammatory condition. No mechanistic link between COX inhibition and skeletal developmental patterning has been identified.

The high TxGNN score most likely reflects associations in the knowledge graph, such as shared musculoskeletal or limb-phenotype connections. It is not supported by biological or clinical evidence. This prediction should be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Six single-ingredient indomethacin products are recorded as valid. The licence numbers below are shown exactly as held in the data compiled for this report. They are not in the MHRA "PL" format, so verify them against the MHRA register. Approved indication text was not available for any product.

| Marketing Authorisation Number | Product Name | Dosage Form |
|---------|------|------|
| 1001010K0BDAAAA | Indocid Cap 25mg | Capsule |
| 1001010K0AAAAAA | Indometacin Cap 25mg | Capsule |
| 1001010K0BQABAD | Indomax-75 SR Cap 75mg | Modified-release capsule |
| 1001010K0BVAAAD | Pardelprin MR Cap 75mg | Modified-release capsule |
| 1001010K0BXAAAD | Berlind 75 Ret Cap 75mg | Prolonged-release capsule |

A sixth authorisation, Indolar SR Cap 75mg (1001010K0BGADAD), is also recorded as valid.

## Safety Considerations

**Contraindication signals (from the knowledge graph, not label text):**
The TxGNN knowledge graph links indomethacin to contraindications in the following groups. Confirm these against the SmPC and BNF.
- **Cardiovascular:** hypertension, myocardial infarction, coronary thrombosis, heart disease, cardiovascular disease
- **Gastrointestinal:** gastric, duodenal and active peptic ulcer disease; ulcerative colitis; inflammatory bowel disease; necrotizing enterocolitis; oesophageal dyskinesia
- **Renal and hepatic:** kidney disease, liver disease, gallbladder disease
- **Haematological and bleeding:** thrombocytopenia, blood coagulation disease, intracerebral haemorrhage, haemoglobinopathy
- **Respiratory:** asthma (including intrinsic and allergic)
- **Neurological and psychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- **Other:** infectious disease

**Drug interactions:**
A total of 252 interactions were recorded. Examples include:
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, metformin, glimepiride, chlorpropamide, aprepitant, mesalazine, balsalazide, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes
- **Minor:** famotidine, ranitidine, cimetidine, linaclotide

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a model score. There are no trials or publications, no plausible mechanistic link between COX inhibition and a congenital skeletal malformation, and an extensive list of potential contraindications and interactions. The evidence level is L5.

**To proceed, the following is needed:**
- A credible biological rationale linking prostaglandin or COX pathways to the pathology of this syndrome
- Any preclinical or case-level evidence of benefit
- Verified MOA data and MHRA-registered licence and indication details
- A risk-benefit assessment for the likely paediatric or young patient population

For comparison, the same data includes a more evidence-supported prediction, **juvenile idiopathic arthritis** (L3, with literature that is mostly historical reviews). That prediction may warrant a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

