---
layout: default
title: Digitoxin
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Digitoxin
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

# Digitoxin: From Cardiac Indications to Prinzmetal Angina

## One-Sentence Summary

Digitoxin is a cardiac glycoside marketed in the UK as a 100 microgram tablet. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 97.86% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, digitoxin is a cardiac glycoside that inhibits Na+/K+-ATPase, raising intracellular calcium.

This mechanism does not obviously support use in Prinzmetal (vasospastic) angina. Higher intracellular calcium would be expected to increase vascular smooth muscle tone, which could be counterproductive in a condition driven by coronary vasospasm. The high TxGNN score is a graph-based prediction, and the mechanistic rationale is unclear and possibly contradictory. This prediction should be treated with considerable caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For context, the other nine predictions were also reviewed. Only rheumatoid arthritis, thrombotic disease and hyperthyroidism had any retrieved literature, and none of it showed therapeutic benefit. It consisted of pharmacokinetic and interaction studies, case reports of toxicity, preclinical work and very old uncontrolled reports of topical digitoxin for venous disease. All ten predictions are currently rated Hold.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0201010D0AAAAAA | Digitoxin Tab 100mcg | Not stated | Not stated |

This identifier appears to be a BNF-style product code (BNF chapter 2.1.1, cardiac glycosides) rather than a standard PL number. Licence-level details such as indication and dosage form are not available.

## Safety Considerations

**Drug Interactions**: The interaction screen returned 87 interacting drugs. Examples include:
- **Major**: dolasetron
- **Moderate**: acarbose, doxycycline, tetracycline, clarithromycin, epinephrine, aprepitant, amphotericin B, calcium salts and vitamin D analogues (cholecalciferol, calcifediol, calcitriol), and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)
- **Minor**: cimetidine, picosulfuric acid

Digitoxin has a narrow therapeutic index. The retrieved literature also shows that thyroid status, hypokalaemia, hypomagnesaemia and hepatic or renal dysfunction can alter glycoside handling and toxicity.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the known mechanism may work against benefit in vasospastic angina. The narrow therapeutic index adds further concern.

**To proceed, the following is needed:**
- Mechanism of action data, and a clear mechanistic case for vasospastic angina
- Licensed indication, dosage form and product information for the UK authorisation
- Warnings and contraindications from the SmPC and BNF
- Preclinical or early clinical evidence of benefit, with a safety and monitoring plan that accounts for the narrow therapeutic index
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

