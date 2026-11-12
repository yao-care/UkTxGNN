---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Nabumetone"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis"]
description: "Nabumetone: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Nabumetone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Nabumetone: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Nabumetone is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and related joint disease.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type** (a rare genetic skeletal disorder), but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Nabumetone is understood to be a COX-2-preferential NSAID that reduces prostaglandin-mediated inflammation and pain. Its use in rheumatoid arthritis and osteoarthritis is established.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia caused by loss-of-function mutations in *CDMP1/GDF5*. Nabumetone has no known interaction with the GDF5/BMP signalling pathway. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, an NSAID might give symptomatic pain relief, not modify the disease.

Of the ten predictions reviewed, the most biologically coherent are indirect and symptomatic:
- **Rheumatoid nodulosis** (score 0.9993, L4): a variant of rheumatoid disease, so symptom control is plausible, but NSAIDs do not alter nodule formation.
- **Pseudoachondroplasia** (score 0.9998, L5): early-onset osteoarthritis could be eased symptomatically, with no evidence of disease modification.

The remaining predictions (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachyolmia, brachydactyly-syndactyly syndrome, WHIM syndrome) have no plausible mechanistic link to COX inhibition.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1001010X0AAACAC | Nabumetone 500mg dispersible tablets sugar free | Nabumetone |
| 1001010X0AAAAAA | Nabumetone 500mg tablets | Nabumetone |
| 1001010X0AAADAD | Nabumetone 500mg/5ml oral suspension | Nabumetone |
| 1001010X0BBACAC | Relifex 500mg dispersible tablets | Nabumetone |
| 1001010X0BBAAAA | Relifex 500mg tablets | Nabumetone |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier does not follow the usual MHRA "PL XXXXX/XXXX" format, so the entry should be checked against the MHRA product database before being relied on.

<!-- review:begin uk-lic-20261106-nabumetone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Only one valid single-ingredient authorisation is recorded. The identifier does not follow the usual MHRA "PL XXXXX/XXXX" format, so the entry should be checked against the MHRA product database before being relied on." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-nabumetone-1 -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease links, not label text): hypertension, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active), substance abuse/dependence, blood coagulation disease, myocardial infarction, coronary thrombosis, haemoglobinopathy, cardiovascular disease and heart disease. These are consistent with known NSAID class concerns (gastrointestinal, cardiovascular, renal and bleeding risks) and must be confirmed against the SmPC.
- **Drug interactions** (100 recorded; most relevant shown):
  - Moderate: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, potassium citrate, potassium bicarbonate, vancomycin, and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate).
  - Minor: ranitidine, cimetidine, linaclotide.
- **Pregnancy and development:** NSAIDs are generally avoided in pregnancy, which complicates any rationale for developmental syndromes.
- **Additional risk:** in WHIM syndrome, NSAID-related platelet and gastrointestinal effects would add risk without a mechanistic benefit.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanistic link to nabumetone. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and the drug carries recognised NSAID safety risks.

**To proceed, the following is needed:**
- Mechanism of action data for nabumetone
- Label warnings and contraindications from the SmPC and BNF, and the approved indication text and dosage form for the UK authorisation
- For the two L4 candidates (spondyloarthropathy, rheumatoid nodulosis), a search for nabumetone-specific trials and literature, which may justify treating them as research questions
- For pseudoachondroplasia, consideration of a research question on symptomatic NSAID use for secondary arthropathy pain

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Only one valid single-ingredient authorisation is recorded" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

