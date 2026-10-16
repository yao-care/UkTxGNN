---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis…"
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From Musculoskeletal and Pain Conditions to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) used for conditions such as arthritis, gout, tendinitis and headache or migraine disorders.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis, gout, migraine, osteoarthritis and related conditions (from the knowledge-graph indication list; no approved indication text is available for the UK record) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Naproxen is an NSAID, and its efficacy in inflammatory and painful musculoskeletal conditions is established, but nothing in the supplied data links that activity to the predicted condition.

Brachydactyly-syndactyly syndrome is a rare congenital skeletal malformation with a developmental genetic basis. The data give no plausible reason for an anti-inflammatory drug to modify such a condition. At most, naproxen might offer symptomatic pain relief for secondary musculoskeletal complaints, which is not a disease-modifying indication.

The high TxGNN score (rank 5,998) reflects a knowledge-graph prediction only. It should be treated as a hypothesis-generating signal, not as evidence of benefit.

The model also ranked three other rare syndromes highly (colobomatous microphthalmia-rhizomelic dysplasia syndrome, 99.22%; acromesomelic dysplasia, Hunter-Thompson type, 99.17%; brachyolmia-amelogenesis imperfecta syndrome, 99.06%). All are developmental genetic conditions with no supporting trials or literature, and the same caution applies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010P0AAADAD (as recorded; not in standard PL format) | Naproxen Tab 250mg | Tablet (as named in the product record) | Not available in the compiled data |

One valid single-ingredient authorisation is recorded. Please verify the authorisation details against the MHRA register and the BNF.

## Safety Considerations

- **Contraindications and cautions flagged in the knowledge graph** (these are model-derived drug-disease links, not label text): hypertension, congestive heart failure, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders, liver disease and liver failure, kidney disease, blood coagulation disorders, anaemia, epilepsy, diabetes mellitus and diabetic ketoacidosis, osteoporosis, gallbladder disease, benign prostatic hyperplasia, obesity, and substance abuse/dependence.
- **Drug interactions**: 100 interactions were identified, all of those listed being of moderate severity. Main examples include:
  - Acetylsalicylic acid
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - Metformin and chlorpropamide
  - Acid-suppressing drugs (famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole)
  - Mesalazine and balsalazide
  - Aprepitant
  - Potassium citrate and potassium bicarbonate
  - Bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes)

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials or publications, no supported mechanistic link, and a condition whose developmental genetic basis makes an NSAID effect implausible. The knowledge-graph contraindication profile also adds safety concerns for any new use.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking COX inhibition to the target condition
- Preclinical or case-based evidence of any benefit
- Confirmation of the UK authorisation details (indication text, dosage form, manufacturer) and the label warnings and contraindications from the SmPC and BNF
- A safety assessment for the intended patient population, which for these rare congenital conditions may include children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

