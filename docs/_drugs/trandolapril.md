---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 590
evidence_level: L5
indication_count: 6
---

# Trandolapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Trandolapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Trandolapril is an ACE inhibitor originally used for the treatment of hypertension (and, as a drug class, for post-myocardial infarction heart failure).
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
but currently **no clinical trials** and **no supporting literature** are available for this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor class) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Trandolapril is not available in this Evidence Pack. Based on known pharmacological information, Trandolapril belongs to the **ACE inhibitor (ACEi) class**, which works by inhibiting the renin-angiotensin system to lower blood pressure. Its efficacy in general hypertension is well established, and mechanistically this class of drugs is already used for renovascular hypertension.

However, the "malignant" subtype of renovascular hypertension warrants particular caution. Patients with malignant renovascular hypertension frequently have underlying **bilateral renal artery stenosis**, a condition in which ACE inhibitors are known to carry a class-level risk of precipitating **acute renal failure**, because glomerular filtration in stenotic kidneys becomes critically dependent on angiotensin II-mediated efferent arteriolar constriction. This is a recognised safety concern for the entire ACEi class, not specific to Trandolapril.

For context, another TxGNN-predicted indication in this Evidence Pack, chronic pulmonary heart disease (rank 6), is supported by a direct Trandolapril-specific animal study (PMID 8989645) showing improved vascular contractile function in a rat model of chronic heart failure. By contrast, the top-ranked prediction discussed here (malignant renovascular hypertension) has a plausible class-level mechanistic rationale but no drug-specific or disease-specific supporting evidence at all.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

No marketing authorisations for Trandolapril are recorded in this Evidence Pack; the drug is currently listed as not marketed in the dataset reviewed. This should be verified directly against the MHRA products database and the current BNF, as Trandolapril-containing products may exist under a different data source.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature specifically support the use of Trandolapril in malignant renovascular hypertension; the only basis is a class-level mechanistic argument. This is further tempered by a known ACE inhibitor class risk of inducing acute renal failure in patients with bilateral renal artery stenosis, a common feature of this condition — meaning the mechanistic rationale cuts both ways.

**To proceed, the following is needed:**
- SmPC warnings and contraindications for Trandolapril (currently a blocking data gap; required before any S1 safety screening)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Dedicated preclinical or clinical evidence in renovascular hypertension, particularly regarding renal function outcomes in patients with suspected bilateral renal artery stenosis
- Drug-drug interaction (DDI) data, currently unavailable ("not_found")
- Consideration of the stronger, drug-specific evidence trail for chronic pulmonary heart disease (rank 6) as an alternative research priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

