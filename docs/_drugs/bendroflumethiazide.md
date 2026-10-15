---
layout: default
title: Bendroflumethiazide
parent: Model Prediction Only (L5)
nav_order: 94
evidence_level: L5
indication_count: 5
---

# Bendroflumethiazide
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

# Bendroflumethiazide: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bendroflumethiazide is a thiazide diuretic, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, bendroflumethiazide is a thiazide diuretic that inhibits the sodium-chloride cotransporter in the distal convoluted tubule. Its efficacy in hypertension is established, and lowering blood pressure gives a plausible link to hypertensive renal disease.

The link is weak, however. Malignant hypertension is a hypertensive emergency, usually managed with rapid-acting parenteral agents, and thiazides are not a standard treatment. Thiazide efficacy is also reduced in advanced renal impairment. The very high TxGNN score most likely reflects how close this indication sits to the approved hypertension indication in the knowledge graph, rather than independent evidence.

Other predictions share this weakness:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Malignant renovascular hypertension | 99.88% | Driven mainly by renin-angiotensin-aldosterone system activation; thiazide diuresis may further stimulate renin release |
| 3 | Pulmonary hypertension (unclear multifactorial mechanism) | 99.87% | Different pathophysiology from systemic hypertension; at most symptomatic volume control |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.87% | Thiazides do not address hypoxic vasoconstriction; metabolic alkalosis may depress respiratory drive |
| 5 | Braddock syndrome | 99.83% | Very rare disorder with no mechanistic rationale in the available data |

All five predictions are at evidence level L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0202010B0AAABAB (BNF code) | Bendroflumethiazide Tablets 2.5 mg | Tablet | Not stated in the compiled data |

Bendroflumethiazide appears in BNF chapter 2 (cardiovascular system) as a thiazide diuretic. One valid single-ingredient product was identified.

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for these.

- **Contraindications suggested by the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text, so they should be verified against the SmPC):
  - Renal and hepatic: kidney disease, anuria, liver disease, hepatic coma and hepatic encephalopathy, pancreatitis, gallbladder disease
  - Metabolic and electrolyte: potassium deficiency, hypercalcaemia, hyperparathyroidism, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, gout, nephrocalcinosis, phosphorus metabolism disorders
  - Neuromuscular and cardiorespiratory: myasthenia gravis and other neuromuscular junction diseases, atrioventricular block, pulmonary emphysema, bronchial disease
  - Other: systemic lupus erythematosus (including paediatric), neonatal jaundice, anxiety, neurotic and dysthymic disorders
- **Drug interactions:** 100 interactions were identified. Most of those listed are of moderate severity:
  - Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide): thiazides may impair glucose control
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone): additive hypokalaemia risk
  - Amphotericin B (including the lipid complex): additive hypokalaemia risk
  - Proton pump inhibitors (omeprazole, rabeprazole), bupropion, morphine and cholecalciferol
  - Minor: doxycycline, hyoscyamine and atropine

Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials or publications. Thiazides are not a recognised treatment for malignant hypertension, which needs urgent, targeted management, and they are less effective in advanced renal impairment. The safety data are also incomplete.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer mechanistic rationale for malignant hypertensive renal disease
- Systematic literature review and trial registry searches for thiazides in hypertensive nephropathy
- SmPC and BNF warnings and contraindications, including renal-function thresholds for thiazide efficacy
- The approved indication text and dosage form for the UK authorisation
- A safety review addressing the renal, electrolyte and metabolic contraindications flagged above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

