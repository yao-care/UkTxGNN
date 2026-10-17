---
layout: default
title: Alfentanil
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Alfentanil: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the licence data compiled for this report (general use:…"
monitor_inn: "Alfentanil"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Alfentanil
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

# Alfentanil: From Anaesthesia and Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Alfentanil is a short-acting mu-opioid receptor agonist used for anaesthesia and analgesia.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but there are currently **no clinical trials** and **no publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (general use: anaesthesia and analgesia) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, alfentanil is a short-acting mu-opioid receptor agonist. Its efficacy in anaesthesia and analgesia is established, but this does not obviously carry over to NSIAD.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These cause water retention and low blood sodium (hyponatraemia) independent of vasopressin. Opioids can influence vasopressin release in the brain: kappa-opioid agonists tend to suppress it, whereas mu-opioids are often associated with antidiuresis.

The biological plausibility is weak. NSIAD is a receptor-level disorder in the kidney, so central modulation of vasopressin would not be expected to correct constitutive V2 receptor activity. Opioid-induced antidiuresis could even worsen hyponatraemia. The high score is most likely a knowledge-graph artefact and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1501043A0AAADAD | Alfentanil HCl Inj 5mg/ml 1ml Amp | Injection (ampoule) | Not stated in the data available |

## Safety Considerations

- **Disease-related cautions (knowledge graph):** The TxGNN knowledge graph links alfentanil to contraindication relationships with kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, pseudotumor cerebri and intracranial hypertension. These come from graph relationships, not from product label text. Renal involvement is particularly relevant given the proposed kidney-related indication.
- **Drug Interactions:** The interaction screen returned 100 interacting drugs; the main ones listed are below.
  - **Major:** aprepitant, bupropion, clarithromycin, clotrimazole, dexfenfluramine, dolasetron, fenfluramine, granisetron, lorcaserin
  - **Moderate:** atropine, cimetidine, clidinium, dexamethasone, dicyclomine, dronabinol, eluxadoline, glycerol phenylbutyrate, glycopyrronium, hyoscyamine, mazindol

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (L5). There are no trials or publications, and the mechanism argues against benefit: NSIAD is driven by a renal V2 receptor defect, and mu-opioid antidiuresis could worsen hyponatraemia.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic rationale linking mu-opioid agonism to V2 receptor-mediated antidiuresis
- Preclinical evidence (for example, AVPR2 gain-of-function models) showing any benefit
- Label-based warnings and contraindications from the SmPC and BNF, including renal safety review
- Licensed indication text and dosage form for the UK authorisation
- Assessment of route compatibility, since alfentanil is available only as an injection in the data compiled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

