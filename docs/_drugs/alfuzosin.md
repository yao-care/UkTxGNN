---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Alfuzosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "allergic urticaria", "persistent fetal circulation syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Alfuzosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Alfuzosin
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

## Alfuzosin: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic receptor antagonist, originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are **no clinical trials and no publications** supporting this prediction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on established pharmacology, alfuzosin is an alpha-1 adrenergic antagonist. It relaxes smooth muscle in the prostate and bladder neck, which improves urinary flow in BPH.

The predicted indication is not closely related to the original one. Ambras syndrome is a rare genetic disorder linked to regulatory changes on chromosome 8q that affect TRPS1 expression. No plausible pathway connects alpha-1 blockade to this condition. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related rare hair and congenital phenotypes, not biological evidence.

Other top-ranked predictions from the TxGNN model show the same pattern. These include hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly and hypotrichosis simplex of the scalp. None has supporting evidence. Hypertrichosis is a known adverse effect of some vasodilators such as minoxidil, which may explain the association the model learned. The direction of effect (inducing versus treating) is unclear.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704010A0AAAAAA | Alfuzosin HCl Tablets 2.5 mg | Tablet | Not available in the compiled data |

Note: the identifier above (which resembles a BNF-style classification code rather than a standard PL number) and the product details should be verified against the MHRA register and the current BNF entry.

## Safety Considerations

**Contraindications and conditions of concern (from knowledge-graph drug-disease associations, not label text):**
- Orthostatic hypotension, hypotensive disorder, multiple system atrophy and postural orthostatic tachycardia syndrome
- Long QT syndrome (including familial), and torsades de pointes
- Liver disease and liver failure
- Gallbladder disease
- Intraoperative floppy iris syndrome (relevant to planned cataract surgery)

**Drug Interactions** (100 interactions were identified; the main ones are listed):
- **Major:** cisapride, clarithromycin, dolasetron
- **Moderate:** famotidine, aprepitant, bupropion, granisetron, levofloxacin, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), dronabinol, clotrimazole, and several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose)
- **Minor:** cimetidine

**Further considerations for the predicted indications:**
- Urticaria and hypersensitivity are reported adverse reactions to alfuzosin, which is relevant to the allergic urticaria prediction.
- Systemic hypotension is a major concern if used in neonates (persistent fetal circulation syndrome), and neonatal safety and pharmacokinetic data are absent.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials or publications, and no plausible mechanistic link between alpha-1 blockade and Ambras syndrome. None of the other top ten predictions has supporting evidence either.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological hypothesis linking alpha-1 antagonism to TRPS1-related hair phenotypes
- Preclinical evidence (for example, in vitro or animal models of hair follicle biology)
- Clarification of the direction of effect (treatment versus induction of hypertrichosis)
- Full SmPC warnings and contraindications, and the MHRA authorisation details (approved indication, dosage form, licence number)
- A review of whether the very high score from the TxGNN model (deep learning) only reflects similarities the model learned between related diseases, not biological evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

