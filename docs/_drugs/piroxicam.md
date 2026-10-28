---
layout: default
title: Piroxicam
parent: Model Prediction Only (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Piroxicam: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis"
monitor_inn: "Piroxicam"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
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

## Piroxicam: From Rheumatoid Arthritis and Osteoarthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Piroxicam is a non-steroidal anti-inflammatory drug (NSAID), originally used for inflammatory and degenerative joint conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental skeletal and ocular malformation syndrome, but there are **no clinical trials and no publications** supporting this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis (from the knowledge graph, as no indication text is recorded for the UK authorisation) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Piroxicam is generally understood to be a non-selective cyclo-oxygenase (COX) inhibitor. It reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory and degenerative arthritis is established.

This prediction does not appear mechanistically sound. The predicted condition is a rare developmental malformation syndrome, and an NSAID has no plausible way to correct its underlying genetic cause. The high TxGNN score (ranked 130th among all predictions for this drug) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis-generating signal, not as evidence of benefit.

The same applies to most of the other top-ranked predictions for piroxicam, which are mainly congenital skeletal dysplasias and limb malformations. Only the lower-ranked prediction of **juvenile idiopathic arthritis (JIA)** has a clear mechanistic fit and supporting literature (see the conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1003020R0AAAAAA (as recorded; not in standard PL format) | Piroxicam Gel 0.5% | Gel (from product name) | Not stated in the data compiled for this report |

The record shows one valid single-ingredient authorisation and no cancelled authorisations. The authorisation number, dosage form and indication text should be verified against the MHRA register and the current SmPC. The BNF classification should also be checked.

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** The TxGNN knowledge graph links piroxicam to the following conditions as contraindications. These are not taken from the product label and must be confirmed against the SmPC and BNF.
  - Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, cerebral infarction, thrombotic disease, heart disease
  - Gastrointestinal: active peptic ulcer disease
  - Hepatic and renal: kidney disease, liver disease, acute liver failure, hepatitis, drug-induced liver injury, gallbladder disease
  - Haematological: blood coagulation disease, anaemia (including macrocytic), haemoglobinopathy
  - Other: substance abuse or dependence, vision disorder, blindness
- **Drug Interactions:** The interaction screen returned 100 interactions in total, and 20 are listed in the data compiled. The main ones are:
  - **Moderate:**
    - Acetylsalicylic acid
    - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
    - Antidiabetic agents (metformin, glimepiride, chlorpropamide)
    - Aminosalicylates (mesalazine, balsalazide)
    - Aprepitant
    - Potassium citrate and potassium bicarbonate
    - Bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes)
  - **Minor:** H2 antagonists (famotidine, ranitidine, cimetidine) and linaclotide.

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone (L5), with no trials, no literature and no credible mechanistic link to a rare genetic developmental syndrome. Safety screening also cannot be completed, because label-based warnings and contraindications were not available.

**Other predictions:** Among the other predictions for piroxicam, **juvenile idiopathic arthritis** is the only one with supporting evidence (L3, "Research Question"). It has a strong mechanistic fit and includes:
- A 1986 multicentre double-blind crossover study of piroxicam versus naproxen in juvenile chronic arthritis (47 children).
- A 1987 randomised comparison of piroxicam and naproxen in juvenile rheumatoid arthritis (26 patients).
- A 1991 paediatric pharmacokinetic study.
- Two recent NSAID class-level network meta-analyses (2021 and 2024).

The paediatric studies are older and small, and the meta-analyses do not show piroxicam-specific findings. No registered trials were identified. This indication would be the more sensible focus for any further evaluation.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to allow mechanistic-link analysis.
- The current SmPC and BNF warnings and contraindications, to complete the safety screen.
- Confirmation of the authorisation details (number, formulation, approved indication) on the MHRA register. The only recorded product is a topical gel, so route compatibility with any systemic indication needs assessing.
- For JIA, a piroxicam-specific review of the paediatric data and the NICE and BNF position before any further work.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

