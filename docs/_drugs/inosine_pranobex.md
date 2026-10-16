---
layout: default
title: Inosine Pranobex
parent: Model Prediction Only (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Inosine Pranobex: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Inosine pranobex"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "hepatic porphyria", "pseudoachondroplasia", "gout", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome"]
---

# Inosine Pranobex
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

# Inosine Pranobex: From an Immunomodulatory Agent to Osteoarthritis (Prediction Only)

## One-Sentence Summary

Inosine pranobex is an immunomodulatory medicine marketed in the UK, but the data compiled for this report do not include an approved indication text for it.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.
The strongest signal among the top-ranked predictions is for **rheumatoid arthritis**, supported by **one 1990 randomised placebo-controlled trial** and one general review, which is discussed below as a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available. Inosine pranobex is generally described as an immunomodulator (enhancing T-lymphocyte function and modulating cytokines). Any link to osteoarthritis is speculative, for example through modulation of low-grade inflammation. No mechanistic data were supplied to test this idea.

The original indication could not be determined from the data, so the relationship between the original and predicted indications cannot be assessed. The osteoarthritis prediction has a high graph score (0.981) but no trials or publications behind it.

**Other predictions in the top ten**

- **Rheumatoid arthritis (score 97.74%, evidence level L4):** This is the most plausible candidate. An immunomodulator is mechanistically relevant to an immune-mediated disease. One randomised, double-blind, placebo-controlled trial exists (see below), but its outcome was not available in the data. It is treated as a research question.
- **Osteoarthritis susceptibility (97.79%):** This is a genetic susceptibility phenotype, not a treatable condition, and likely overlaps with the osteoarthritis prediction.
- **Gout (97.12%):** Inosine is a purine metabolite and may be metabolised to uric acid. The likely direction of effect is harmful (hyperuricaemia), not therapeutic. This should be viewed as a safety concern rather than an opportunity.
- **Hepatic porphyria, pseudoachondroplasia, and the hepatic-vascular entities (early-onset familial noncirrhotic portal hypertension, hepatoportal sclerosis, idiopathic copper-associated cirrhosis, hepatopulmonary syndrome):** There is no mechanistic or clinical support. Several share an identical score (0.970), suggesting a clustered graph artefact rather than independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis.

---

## Literature Evidence

No publications are available for osteoarthritis. The publications below relate to the rheumatoid arthritis prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1693065](https://pubmed.ncbi.nlm.nih.gov/1693065/) | 1990 | RCT | Annals of the Rheumatic Diseases | Randomised, double-blind, placebo-controlled trial of inosine pranobex (3 g/day) as a possible second-line drug in rheumatoid arthritis: 24 patients on the drug and 26 on placebo for up to 24 weeks. Outcomes assessed included morning stiffness, articular index, grip strength, pain, ESR, CRP, IgG, IgM and serum urate. The results were not available in the data. |
| [1715732](https://pubmed.ncbi.nlm.nih.gov/1715732/) | 1991 | Review | Current Opinion in Rheumatology | General review of novel immunotherapies potentially applicable to rheumatoid arthritis. It is not specific to inosine pranobex. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503021D0AAAAAA (BNF-style product code, not a PL number) | Inosine Pranobex Tab 500mg | Tablet (strength 500 mg) | Not available |

One valid single-ingredient authorisation is recorded. Manufacturer, dosage form detail and indication text were not available in the data compiled for this report.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

One point deserves attention: inosine is a purine metabolite and may be metabolised to uric acid. Serum urate and gout history would be relevant considerations in any new use, but this is an inference from the biochemistry and not from label data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction rests on a model score alone (L5), with no trials, no publications and no supporting mechanism. The rheumatoid arthritis signal is more interesting (L4), but the single 1990 trial cannot be graded without its full text and results.

**To proceed, the following is needed:**
- Full text of the 1990 rheumatoid arthritis RCT (PMID 1693065) to establish its power, outcomes and direction of effect. A well-powered positive result could support upgrading that indication to L2/L1.
- Mechanism of action data (for example from DrugBank) and a plausible rationale for osteoarthritis.
- The approved indication, dosage form and manufacturer from the SmPC and BNF, to establish the original indication.
- Warnings, contraindications and interaction data from the SmPC and BNF. Safety data are currently missing, so safety screening cannot proceed.
- An assessment of the hyperuricaemia and gout risk linked to inosine metabolism.
- A check of route and formulation compatibility with any proposed new indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

