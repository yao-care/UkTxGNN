---
layout: default
title: Dabigatran Etexilate
parent: Model Prediction Only (L5)
nav_order: 201
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Dabigatran Etexilate: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not recorded in the UK licence data compiled for this report (the pro…"
monitor_inn: "Dabigatran etexilate"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dabigatran etexilate: From Anticoagulation to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor (anticoagulant) with a marketed UK product.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**,
but the data compiled for this report contain **no relevant clinical trials** and **only 1 publication, which does not address efficacy**. The signal is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the UK licence data compiled for this report (the product is a direct thrombin inhibitor anticoagulant) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Dabigatran is, however, a well-known direct thrombin inhibitor, and its established use is in anticoagulation.

A theoretical link to sclerosing cholangitis exists through thrombin signalling (PAR-1) in the activation of hepatic stellate cells and in liver fibrosis, which could be relevant to cholestatic fibrosis. This remains a hypothesis. No clinical or preclinical evidence in the data supports it.

The one publication retrieved (PMID 36906733) is about the drug-drug interaction profile of cilofexor, a different compound, and does not assess dabigatran. The high TxGNN score should therefore be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | In vitro/DDI pharmacology study | Clinical Pharmacokinetics | Evaluates cytochrome P450 and transporter-mediated drug interaction potential of cilofexor, an FXR agonist in development for NASH and primary sclerosing cholangitis. It does not study dabigatran or its efficacy. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0208020X0AAAAAA | Dabigatran Etexilate Cap 75mg | Not recorded | Not recorded |

The licence record is a single, valid, single-ingredient product. The identifier appears to be a BNF-style product code (BNF chapter 2, section 8: oral anticoagulants) rather than a standard PL number. Approved indication text and dosage form were not available.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (drug-disease contraindication links, not label text): blood coagulation disease, anaemia, macrocytic anaemia, intracerebral haemorrhage. These should be verified against the SmPC.
- **Bleeding risk**: As an anticoagulant, dabigatran would be expected to increase bleeding risk. This is a particular concern in conditions with a bleeding tendency.

Please refer to the SmPC and BNF for full warnings, contraindications and interactions. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no relevant trials, and the only publication is unrelated to dabigatran efficacy. The mechanistic rationale is theoretical.

**To proceed, the following is needed:**
- Preclinical evidence (for example, thrombin/PAR-1 inhibition in cholestatic liver fibrosis models)
- Retrieval of the SmPC and BNF safety information, including contraindications and interactions
- Confirmation of the licensed indications and dosage form for the UK product
- A review of safety in hepatobiliary disease, given bleeding risk and the knowledge-graph contraindication signals
- A detailed mechanism of action summary to support the mechanistic-link analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

