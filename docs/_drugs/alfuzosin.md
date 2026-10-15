---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic receptor antagonist, originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are **no clinical trials and no publications** supporting this prediction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (the MHRA authorisation text is not available in the data compiled for this report; the indication comes from the TxGNN knowledge graph) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on established pharmacology, alfuzosin is an alpha-1 adrenergic antagonist. It relaxes smooth muscle in the prostate and bladder neck, which improves urinary flow in BPH.

The predicted indication is not closely related to the original one. Ambras syndrome is a rare genetic disorder linked to regulatory changes on chromosome 8q that affect TRPS1 expression. No plausible pathway connects alpha-1 blockade to this condition. The very high TxGNN score probably reflects graph-neighbourhood similarity among rare hair and congenital phenotypes rather than a true pharmacological link.

Other top-ranked predictions show the same pattern. These include hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly and hypotrichosis simplex of the scalp. None has supporting evidence. Hypertrichosis is a known adverse effect of some vasodilators such as minoxidil, which may explain the association in the knowledge graph. The direction of effect (inducing versus treating) is unclear.

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
- A review of whether the very high score is a graph artefact, for example by checking the knowledge-graph paths behind the prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

