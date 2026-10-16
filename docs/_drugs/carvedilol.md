---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 137
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Carvedilol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension"
---

# Carvedilol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Carvedilol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a beta-blocker with alpha-1 blocking activity, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the approved indication text for the UK licence is not available) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carvedilol is a non-selective beta-blocker with additional alpha-1 blocking activity, and its efficacy in hypertension is established.

Malignant renovascular hypertension is a severe form of hypertension driven largely by activation of the renin-angiotensin system. Beta-blockade reduces renin release, which offers a plausible mechanism. Alpha-1 blockade adds vasodilation.

However, this is an extension of the existing hypertension indication rather than a truly novel repurposing. The high score is a computational prediction only. Malignant hypertension is usually managed acutely with intravenous agents, and oral carvedilol is not a standard choice in that setting.

Other predictions in the data (for example malignant hypertensive renal disease, scoring 99.55%) follow the same pattern: high scores with no supporting clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For context, the nearby prediction of pulmonary hypertension owing to lung disease and/or hypoxia (score 99.54%) has only indirect, mostly preclinical literature, such as [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) (2015, rat study of carvedilol reversing hypertension induced by chronic intermittent hypoxia). It does not support the lead prediction.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 020400080AAABAB | Carvedilol Tablet 12.5 mg | Not stated | Not stated |

The licence number is not in the standard MHRA PL format, and no dosage form or indication text was available. Please verify the authorisation against MHRA records and the BNF before relying on it.

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text):** liver failure; asthma (including intrinsic and allergic asthma); bronchitis; pulmonary emphysema and other bronchial disease; diabetes mellitus and diabetic ketoacidosis; hypotensive disorder; peripheral vascular disease (including intermittent claudication and peripheral arterial disease); atrioventricular block; sick sinus syndrome (including the familial form); Prinzmetal angina; anaphylaxis; intraoperative floppy iris syndrome.
- **Drug Interactions:** 100 interactions were identified. Those shown include:
  - **Major:** epinephrine.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine), bupropion, morphine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate).
  - **Minor:** acetylsalicylic acid, aluminium hydroxide, attapulgite.
- **Other considerations:** non-selective beta-blockade raises respiratory concerns in lung disease. Beta-blockers have also raised concerns in pulmonary hypertension because of possible right ventricular depression.

Label-based warnings were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials or publications for malignant renovascular hypertension, and it largely restates the existing hypertension indication. Oral carvedilol is not a standard option for this acute, severe condition.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- SmPC and BNF warnings and contraindications, as safety screening cannot proceed without them
- Confirmation of the UK marketing authorisation details (number, dosage form, approved indication)
- A targeted literature search for beta-blockers in malignant or renovascular hypertension, and any relevant trial registrations (including ISRCTN and EU CTR)
- Clarification of how this differs from the existing hypertension indication, and the clinical role of an oral agent in a setting usually managed with intravenous therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

