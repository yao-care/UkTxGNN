---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 639
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Triamterene: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension and congestive heart failure"
monitor_inn: "Triamterene"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Triamterene
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

# Triamterene: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic, originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **no clinical trials** and **no relevant publications** supporting this prediction. It rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the UK licence record contains no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron. This promotes sodium loss and reduces fluid volume, which lowers blood pressure. It is already used for hypertension and congestive heart failure.

The link to malignant renovascular hypertension is weak. This condition is driven mainly by activation of the renin-angiotensin system and renal artery stenosis. A diuretic alone is unlikely to be adequate, and volume depletion could worsen renal perfusion. The high TxGNN score probably reflects similarity to the approved hypertension indication rather than independent evidence.

Other predictions for this drug follow the same pattern:
- **Malignant hypertensive renal disease** (99.89%): the score appears inherited from the parent hypertension indication. Hyperkalaemia risk in renal impairment makes triamterene a poor fit.
- **Pulmonary hypertension** (two forms, 99.88%): diuretics can relieve right-heart congestion, but there is no known action on pulmonary vascular remodelling.
- **Braddock syndrome** (99.84%): no mechanistic rationale is identifiable.
- **Chronic pulmonary heart disease** (99.75%): the most plausible of the group, as diuretics are used for volume overload in right-sided heart failure and triamterene is already used in congestive heart failure. The evidence remains indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications were found for the lead prediction (malignant renovascular hypertension). The table below lists publications retrieved for the related predictions, and none of them directly supports the lead indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Randomised crossover study (16 patients; classified as review) | Dtsch Med Wochenschr | Hydrochlorothiazide plus triamterene compared with a digitalis glycoside in chronic heart failure. Relevant to heart failure in general, not pulmonary heart disease specifically. |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Clinical study | Fortschr Med | Fixed verapamil/triamterene/hydrochlorothiazide combination in 12 patients with chronic heart failure lowered blood pressure and heart rate over four weeks. Combination therapy, so triamterene's own effect cannot be isolated. |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Case report | Chest | Low-pressure pulmonary oedema after a triamterene-hydrochlorothiazide tablet, thought to be due to the hydrochlorothiazide component. This is a safety signal, not efficacy evidence. |
| [5639361](https://pubmed.ncbi.nlm.nih.gov/5639361/) | 1968 | Preclinical (animal physiology) | J Physiol | Study of electrical potential across rat colon mucosa. Unrelated to the predicted indication. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0202030W0AAAAAA | Triamterene capsule 50 mg | Capsule | Not stated in the data compiled for this report |

Please check the product's SmPC and the BNF classification for the licensed indications.

---

## Safety Considerations

**Contraindications (from knowledge-graph associations, not label text):** the TxGNN knowledge graph links triamterene to contraindications in the following groups. These should be verified against the SmPC.
- **Renal:** kidney disease, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- **Hepatic:** liver failure, liver disease, hepatic coma, hepatic encephalopathy
- **Metabolic and endocrine:** diabetes mellitus (type 1 and type 2), diabetic ketoacidosis, gout, hyperuricaemia, hyperparathyroidism, hypercalcaemia, acidosis, lactic acidosis
- **Other:** pancreatitis, gallbladder disease, systemic lupus erythematosus, folic acid deficiency anaemia, neonatal jaundice

**Drug Interactions:** 100 interactions were recorded. Those retrieved include:
- **Major:** potassium citrate (risk of hyperkalaemia)
- **Moderate:** metformin, canagliflozin, dapagliflozin, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, bupropion, morphine, dronabinol, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes
- **Minor:** famotidine, ranitidine, cimetidine, doxycycline, minocycline

Hyperkalaemia and renal function monitoring would be essential in any further assessment. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials or supporting literature (Evidence Level L5). A diuretic is unlikely to be adequate for a renin-driven condition, and hyperkalaemia and renal risks make triamterene a poor fit for malignant renovascular hypertension. Chronic pulmonary heart disease (L4) is the only related prediction with a plausible indirect link, and it is better framed as a research question.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer pharmacological rationale for the predicted condition
- Retrieval of SmPC warnings and contraindications to complete the safety review
- Controlled clinical evidence in the target population
- A hyperkalaemia and renal function monitoring plan for any further assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

