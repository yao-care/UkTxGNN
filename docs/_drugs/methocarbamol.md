---
layout: default
title: Methocarbamol
parent: Model Prediction Only (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Methocarbamol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the data compiled for this report (general class use:…"
monitor_inn: "Methocarbamol"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "panuveitis (disease)", "anaphylaxis", "iris disease", "uveitis", "ventricular tachycardia", "food-dependent exercise-induced anaphylaxis", "conjunctivitis", "obsolete bundle branch block"]
---

# Methocarbamol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Methocarbamol: From Muscle Spasm (Original Indication Not Recorded) to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Methocarbamol is a centrally acting skeletal muscle relaxant, and the data compiled for this report do not record its original licensed indication.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model prediction only and should be treated as a hypothesis, not as evidence of benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report (general class use: relief of muscle spasm) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methocarbamol is a centrally acting skeletal muscle relaxant. A plausible link would therefore be symptomatic relief of muscle spasm or pain associated with the condition.

The prediction is only partly plausible. Cauda equina syndrome is a surgical emergency caused by compression of the nerve roots, and its management is urgent decompression. A muscle relaxant would not address the underlying pathology. The very high score (0.9998) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the mechanism cannot be verified from the available data.

Other predictions in the same list (for example uveitis, panuveitis, iris disease, conjunctivitis, ventricular tachycardia and anaphylaxis) also have no supporting trials and no identifiable mechanistic rationale. This pattern suggests the scores from the TxGNN model (deep learning) may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1002020S0AAADAD | Methocarbamol 1500mg tablets | Methocarbamol |
| 1002020S0AAACAC | Methocarbamol 375mg/5ml oral suspension | Methocarbamol |
| 1002020S0AAABAB | Methocarbamol 750mg tablets | Methocarbamol |
| 1002020S0AAAEAE | Methocarbamol 750mg/5ml oral suspension sugar free | Methocarbamol |
| 1002020S0BBAAAB | Robaxin 750 tablets | Methocarbamol |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Indication text and dosage form details are not available in the data compiled for this report. Please check the current MHRA product information and the BNF (skeletal muscle relaxants) for licensed indications.

<!-- review:begin uk-lic-20261106-methocarbamol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The registry lists one valid single-ingredient authorisation. Indication text and dosage form details are not available in the data compiled for this report." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-methocarbamol-1 -->

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease links in the model's knowledge graph, not from product label text, so they should be verified against the SmPC): epilepsy, kidney disease, liver disease, gallbladder disease, thrombocytopenia, thrombocytopenic purpura, anaemia (including macrocytic anaemia), peptic ulcer disease (including active disease), gastritis, gout, substance abuse/dependence, haemophilia, von Willebrand disease, congenital prothrombin deficiency, vitamin K deficiency haemorrhagic disease, nasal cavity polyp, Reye syndrome, Alzheimer disease, Pick disease and cerebellar degeneration.
- **Drug Interactions**: 100 interactions were identified in total. The main ones listed are:
  - **Major**: morphine (including liposomal morphine), likely additive central nervous system and respiratory depression.
  - **Moderate**: dronabinol, nabilone, metoclopramide, opium, sibutramine.
  - Several other interactions are of unknown severity (for example metformin, omeprazole, pantoprazole, prednisone, doxycycline and glimepiride).
- **Hypersensitivity**: A 2026 review of side-effect profiles of centrally acting muscle relaxants notes that hypersensitivity reactions are a recognised concern in this drug class.

Warning and contraindication text from the product information was not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or supportive publications. Cauda equina syndrome requires urgent surgical management, and a muscle relaxant has no plausible disease-modifying role.

**To proceed, the following is needed:**
- Mechanism of action data for methocarbamol
- The licensed indication and product information (SmPC) for the UK authorisation
- Any clinical or observational evidence in cauda equina syndrome, or a clearly defined symptomatic role (such as adjunctive spasm or pain relief)
- A review of safety data, including the CNS depressant interactions and the knowledge-graph contraindications
- Consideration of other predicted indications, none of which currently has supporting evidence either

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The registry lists one valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

