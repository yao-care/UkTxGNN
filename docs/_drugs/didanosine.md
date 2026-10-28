---
layout: default
title: Didanosine
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 3
monitor_inn: "Didanosine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Didanosine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infection and AIDS"
---

# Didanosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Didanosine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Didanosine was originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **no registered clinical trials** and only **2 publications**, neither of which tests efficacy in infected cats. The evidence for this prediction is therefore very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (relation recorded in the knowledge graph; the UK record contains no approved indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9933 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Didanosine is, however, a nucleoside reverse transcriptase inhibitor (NRTI) acting on the reverse transcriptase of retroviruses. Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, so antiviral activity is mechanistically plausible.

The two publications retrieved do not support efficacy. One examines didanosine-induced sensory neuropathy in an FIV animal model (a toxicity finding), and the other examines neuronal autophagy and the neuroprotective effects of antiretroviral therapy in lentivirus infection. The high score most likely reflects the drug's known anti-HIV activity rather than feline-specific data. Neither study directly tests whether didanosine treats the disease in cats, so the evidence level is capped at L5.

Two other predictions were also generated: simian immunodeficiency virus (SIV) infection and a rare neurodevelopmental disorder. The SIV prediction has preclinical support (see below) but is not a human indication. The neurodevelopmental prediction has no supporting evidence and is mechanistically implausible, since didanosine is associated with mitochondrial toxicity and neuropathy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17616550](https://pubmed.ncbi.nlm.nih.gov/17616550/) | 2007 | Animal study | Brain | In an FIV-infected animal model, didanosine caused sensory neuropathy with impaired mitochondrial and neurotrophic factor gene expression (a toxicity finding, not efficacy) |
| [19380511](https://pubmed.ncbi.nlm.nih.gov/19380511/) | 2009 | Animal/in vitro study | FASEB J | Lentivirus infection activated CXCR3 and suppressed neuronal autophagy; antiretroviral therapy showed neuroprotective effects |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010N0AAAIAI | Didanosine Cap E/C 400mg | Capsule (enteric-coated, from product name) | Not stated in the data compiled for this report |

This is a single-ingredient product record. The approved indication text is not available, so the original indications above are not confirmed by licence text.

## Cytotoxicity

Didanosine is an antiviral, not an antineoplastic, so this section does not apply.

## Safety Considerations

**Contraindication relations recorded in the knowledge graph** (these are not label text and should be verified against the SmPC):
kidney disease and impaired renal function, liver disease, gallbladder disease, peripheral neuropathy and peripheral nervous system disease, diabetes mellitus, diabetic ketoacidosis, hypertension, coronary artery disease, hypertriglyceridemia, obesity, nephrolithiasis, acute urate nephropathy, hyperparathyroidism, hypercalcemia, adrenocortical insufficiency (Addison disease), sarcoidosis, diarrhoeal disease, and substance abuse/dependence, among others.

**Drug Interactions** (100 recorded; main examples from the first 20 listed):
- **Moderate:** acetylsalicylic acid, metronidazole, levofloxacin, naltrexone, nitisinone, orlistat, rosuvastatin, simvastatin, tinidazole
- **Minor:** ranitidine, doxycycline, minocycline, tetracycline
- **Unknown severity:** levocarnitine, amphotericin B, pantoprazole, glimepiride, morphine, metformin

The preclinical literature also links didanosine to sensory neuropathy and mitochondrial toxicity.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and no cited study directly shows efficacy against feline immunodeficiency. The only retrieved studies concern toxicity and neuroprotection. The prediction is plausible mainly because didanosine is already known as an anti-HIV drug.

**To proceed, the following is needed:**
- Mechanism of action data
- Efficacy studies of didanosine in FIV-infected cats (veterinary context, outside the human UK licence)
- Licence indication text and SmPC safety data for the UK product
- Consideration of the existing neuropathy and mitochondrial toxicity signals before any new use
- Note: the SIV prediction has macaque data (PMID 9282812, didanosine rescued animals from a lethal SIV challenge), but it is a preclinical model and not a new human indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

