---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Asthma"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
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

## Salbutamol: From Asthma to Papillary Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a short-acting beta-2 agonist bronchodilator, originally used to treat asthma and other bronchial disease.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma; bronchial disease |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, salbutamol is a beta-2 adrenergic agonist whose efficacy in asthma and bronchial disease is well established, and mechanistically it may be applicable to papillary conjunctivitis.

A possible link is that beta-2 agonism could reduce mast cell mediator release or ocular vascular congestion. This is speculative and has not been tested for this condition. No similarity analysis between asthma and papillary conjunctivitis has been completed, and the ocular route of administration has not been assessed. Salbutamol is currently marketed in the UK as an inhaled product, not an ocular one.

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
| 0301011R0AAAFAF (as listed; appears to be a BNF-style code rather than a PL number) | Salbutamol powder for inhalation 95 mcg (200 doses) | Inhalation powder | — |

The listing shows one valid single-ingredient product and no cancelled authorisations. Approved indication text was not available for this entry. The code prefix (0301011R) corresponds to the BNF bronchodilator (selective beta-2 agonist) section, and this should be confirmed against the current BNF and the MHRA register.

---

## Safety Considerations

- **Contraindications and cautions from the drug-disease knowledge graph** (not taken from product label text; verify against the SmPC): hypertension, long QT syndrome (including familial), epilepsy, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, metabolic acidosis, benign prostatic hyperplasia and bladder neck obstruction, ocular hypertension, angle-closure glaucoma, hyperthyroidism and thyrotoxicosis (including Graves disease), sudden cardiac arrest, heart conduction disease, myocardial ischaemia and coronary artery disease.
  - The glaucoma and ocular hypertension signals are particularly relevant to any ocular use.
- **Drug Interactions**: 100 interactions are recorded, and the 20 reviewed include:
  - **Moderate**: acarbose, isometheptene, famotidine, epinephrine, albiglutide, acetohexamide, alogliptin, bisacodyl, canagliflozin, castor oil, chlorpropamide, cisapride, clarithromycin, dapagliflozin, diethylpropion. Several are antidiabetic agents, which fits the known effect of salbutamol on blood glucose.
  - **Minor**: hydrocortisone, beclomethasone dipropionate, betamethasone, budesonide, dexamethasone.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for papillary conjunctivitis and the mechanistic link is untested. The knowledge graph also flags glaucoma and ocular hypertension as contraindications, which is a concern for any ocular use.

**To proceed, the following is needed:**
- Preclinical or early clinical evidence of salbutamol in papillary conjunctivitis. Preclinical work on beta-2 agonists in allergic conjunctivitis exists and could be a starting point.
- Mechanism of action data to support the proposed mast cell or vascular pathway.
- An assessment of route and formulation, since only an inhaled product is currently listed.
- Verified warnings and contraindications from the SmPC.
- Prioritisation of other predicted indications for salbutamol (for example bronchitis and anaphylaxis), which have more trial and literature evidence than this one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

