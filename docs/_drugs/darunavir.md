---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 208
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Darunavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Darunavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Darunavir
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

## Darunavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **no clinical trials** and **no publications** supporting this prediction.
The evidence is model-based only, and the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the marketing authorisation record contains no approved indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, darunavir belongs to the HIV-1 protease inhibitor class. Its efficacy in HIV infection is established, and the feline disease is caused by a related lentivirus (feline immunodeficiency virus, FIV).

That relationship gives the prediction some plausibility, but the link is weak. FIV protease differs structurally from HIV-1 protease in substrate specificity and inhibitor sensitivity, and HIV-1 protease inhibitors are known to have reduced activity against it. The very high TxGNN score most likely reflects the similarity between the disease classes (HIV/AIDS and feline AIDS) rather than demonstrated target engagement.

This is also a veterinary condition rather than a human one, so it is of limited direct relevance to UK human-medicine repurposing.

Other predictions in the data compiled for this report do not look stronger:
- **Simian immunodeficiency virus infection** (L4): four preclinical macaque studies were found (2011–2016). They appear to examine combination antiretroviral regimens, and it is unclear whether darunavir was a component. They are best viewed as HIV animal-model work, not as a new human indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (L5): no plausible mechanistic link; likely a TxGNN model (deep learning) artefact.
- **Obsolete familial combined hyperlipidaemia** (L5): protease inhibitors are associated with adverse lipid effects, so the association may reflect a side-effect relationship rather than a therapeutic one. The disease term is also obsolete.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For the second-ranked prediction (simian immunodeficiency virus infection), the following preclinical studies were identified. None is a human study, and none was confirmed to test darunavir specifically.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (non-human primate) | PLoS One | Suppressive combination antiretroviral therapy plus the histone deacetylase inhibitor SAHA in SIV-infected Chinese rhesus macaques, studying the viral reservoir |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical (non-human primate) | AIDS Res Hum Retroviruses | Comparison of two coformulated injectable antiretroviral regimens in SIV-infected rhesus macaques |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (non-human primate) | PLoS Pathog | Highly intensified multidrug ART induced long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical (non-human primate) | AIDS | Auranofin restricted the viral reservoir in the monkey AIDS model and contained viral load after ART suspension |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010ACAAABAB (BNF-style code; no PL number provided) | Darunavir tablets 400 mg | Tablet | Not stated in the data compiled |

Darunavir is classified in BNF chapter 5 (infections), under HIV protease inhibitors (section 5.3.1).

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver failure, liver disease, cirrhosis, chronic hepatitis B and C infection, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridaemia, and haemophilia.
- **Drug interactions:** 100 interactions were identified. Examples include:
  - **Major:** cisapride.
  - **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide, albiglutide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant and clarithromycin.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no clinical trials or publications. FIV protease is known to respond poorly to HIV-1 protease inhibitors, and the condition is veterinary rather than human. The simian model evidence is indirect and does not isolate darunavir.

**To proceed, the following is needed:**
- Mechanism of action data for darunavir
- In vitro data on darunavir activity against FIV protease and FIV replication
- Confirmation of whether darunavir was used in any of the identified macaque studies
- Approved indication text and PL number for the UK authorisation
- Warnings and contraindications from the SmPC
- A decision on whether a veterinary indication falls within the scope of this repurposing programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

