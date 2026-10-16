---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 600
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Telmisartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Hypertension"
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant renovascular hypertension", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker, originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **Prinzmetal angina** with a very high score, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (also stroke, cerebrovascular disorder and cerebral infarction in the knowledge graph; the UK licence record gives no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, telmisartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is established, and mechanistically it may be applicable to Prinzmetal angina.

Prinzmetal (vasospastic) angina is caused by episodic coronary artery spasm. Angiotensin II-mediated vasoconstriction and endothelial dysfunction may contribute to this spasm. Telmisartan has been reported to improve endothelial function, which gives a plausible but unproven link.

The very high graph score most likely reflects network proximity to cardiovascular indications rather than clinical evidence. This should be read as a hypothesis, not as support for use.

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
| 0205052Q0AAACAC | Telmisartan Tab 20mg | Tablet (taken from the product name) | Not specified in the data compiled |

This is the only valid single-ingredient authorisation recorded. The record does not give the manufacturer, a PL number or indication text. Please check the current MHRA record, the SmPC and the BNF for full licensed indications and NICE guidance.

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (not taken from label text, so they must be checked against the SmPC): liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic forms), hepatic encephalopathy and coma, kidney disease, anuria, renal artery obstruction, hypotensive disorder, diabetes mellitus, diabetic ketoacidosis, gout, hyperuricaemia, potassium deficiency, hypercalcaemia, nephrocalcinosis, hyperparathyroidism, osteitis fibrosa, phosphorus metabolism disorders, pancreatitis, gallbladder disease, pyoureter, neonatal jaundice and systemic lupus erythematosus (including paediatric).
- **Drug interactions:** 100 interactions were identified, and the first 20 returned are summarised here.
  - **Major:** potassium citrate and potassium bicarbonate. Both carry a risk of raised potassium when combined with an ARB.
  - **Moderate:** systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulin (human and aspart), exenatide, acetylsalicylic acid, morphine, bupropion, dronabinol and bowel-preparation products (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).
- **Condition-specific concern:** blood-pressure lowering could be problematic in patients with low baseline pressure or significant coronary disease. This has not been assessed for vasospastic angina.

Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it rests only on graph proximity and a plausible endothelial and vasoconstriction hypothesis. No trials or publications were found, so this is an L5 prediction.

**To proceed, the following is needed:**
- A systematic literature search for ARBs (including telmisartan) in vasospastic or coronary spasm disorders, together with preclinical or mechanistic work on coronary vasospasm.
- Detailed mechanism of action data and SmPC warnings and contraindications for the UK product.
- Confirmation of the licence details (PL number, formulation and indication text) from the MHRA record.
- A safety assessment for hypotension and for patients with coronary disease.

**Note on other predictions:** Other predictions for telmisartan in the same data are better supported. The most advanced is **intracerebral hemorrhage** (L1, with the Phase 3 TRIDENT trial of a telmisartan-containing triple low-dose pill). It is confounded by the combination design and is a close extension of the existing hypertension and stroke indications. **Cerebral artery occlusion** (L3) has mainly animal data and overlaps with the stroke indications already approved. If a more evidence-based direction is wanted, a separate evaluation of these indications is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

