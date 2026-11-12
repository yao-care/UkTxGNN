---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Naproxen: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) used for conditions such as arthritis, gout, tendinitis and headache or migraine disorders.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (53 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 53 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Naproxen is an NSAID, and its efficacy in inflammatory and painful musculoskeletal conditions is established, but nothing in the supplied data links that activity to the predicted condition.

Brachydactyly-syndactyly syndrome is a rare congenital skeletal malformation with a developmental genetic basis. The data give no plausible reason for an anti-inflammatory drug to modify such a condition. At most, naproxen might offer symptomatic pain relief for secondary musculoskeletal complaints, which is not a disease-modifying indication.

The high TxGNN score (rank 5,998) reflects a TxGNN model (deep learning) prediction only. It should be treated as a hypothesis-generating signal, not as evidence of benefit.

The model also ranked three other rare syndromes highly (colobomatous microphthalmia-rhizomelic dysplasia syndrome, 0.9922; acromesomelic dysplasia, Hunter-Thompson type, 0.9917; brachyolmia-amelogenesis imperfecta syndrome, 0.9906). All are developmental genetic conditions with no supporting trials or literature, and the same caution applies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1001010P0AAAYAY | Naproxen 100mg/5ml oral suspension | Naproxen |
| 1001010P0AAARAR | Naproxen 125mg/5ml oral suspension | Naproxen |
| 1001010P0AABEBE | Naproxen 125mg/5ml oral suspension sugar free | Naproxen |
| 1001010P0AABCBC | Naproxen 200mg/5ml oral suspension | Naproxen |
| 1001010P0AABDBD | Naproxen 250mg effervescent tablets sugar free | Naproxen |
| 1001010P0AAAHAH | Naproxen 250mg gastro-resistant tablets | Naproxen |
| 1001010P0AAADAD | Naproxen 250mg tablets | Naproxen |
| 1001010P0AABFBF | Naproxen 250mg/5ml oral suspension | Naproxen |
| 1001010P0AABIBI | Naproxen 320mg/5ml oral suspension | Naproxen |
| 1001010P0AAAJAJ | Naproxen 375mg gastro-resistant tablets | Naproxen |
| 1001010P0AAAIAI | Naproxen 500mg gastro-resistant tablets | Naproxen |
| 1001010P0AAAQAQ | Naproxen 500mg modified-release tablets | Naproxen |
| 1001010P0AABGBG | Naproxen 500mg suppositories | Naproxen |
| 1001010P0AAAEAE | Naproxen 500mg tablets | Naproxen |
| 1001010P0AAATAT | Naproxen 500mg/5ml oral suspension | Naproxen |
| 1001010P0AABHBH | Naproxen 60mg/5ml oral suspension | Naproxen |
| 1001010P0AAAWAW | Naproxen 70mg/5ml oral suspension | Naproxen |
| 1001010P0AAAZAZ | Naproxen 75mg/5ml oral suspension | Naproxen |
| 100101070AAAAAA | Naproxen sodium 275mg tablets | Naproxen sodium |
| 1001010P0BDACAD | Arthrosin 250 tablets | Naproxen |

Showing 20 of 53 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Please verify the authorisation details against the MHRA register and the BNF.

<!-- review:begin uk-lic-20261106-naproxen-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One valid single-ingredient authorisation is recorded. Please verify the authorisation details against the MHRA register and the BNF." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 53 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-naproxen-1 -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient authorisation is recorded" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

