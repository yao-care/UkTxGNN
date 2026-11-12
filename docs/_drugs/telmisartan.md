---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 600
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
description: "Telmisartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Telmisartan
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

## Telmisartan: Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker, originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **Prinzmetal angina** with a very high score, but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (22 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 22 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, telmisartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is established, and mechanistically it may be applicable to Prinzmetal angina.

Prinzmetal (vasospastic) angina is caused by episodic coronary artery spasm. Angiotensin II-mediated vasoconstriction and endothelial dysfunction may contribute to this spasm. Telmisartan has been reported to improve endothelial function, which gives a plausible but unproven link.

The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This should be read as a hypothesis, not as support for use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0205052Q0AAACAC | Telmisartan 20mg tablets | Telmisartan |
| 0205052Q0AAAAAA | Telmisartan 40mg tablets | Telmisartan |
| 0205052Q0AAADAD | Telmisartan 40mg/5ml oral suspension | Telmisartan |
| 0205052Q0AAABAB | Telmisartan 80mg tablets | Telmisartan |
| 0205052R0BCAAAA | Actelsar HCT 40mg/12.5mg tablets | Telmisartan with diuretic |
| 0205052R0BCABAB | Actelsar HCT 80mg/12.5mg tablets | Telmisartan with diuretic |
| 0205052R0BCACAC | Actelsar HCT 80mg/25mg tablets | Telmisartan with diuretic |
| 0205052Q0BBACAC | Micardis 20mg tablets | Telmisartan |
| 0205052Q0BBAAAA | Micardis 40mg tablets | Telmisartan |
| 0205052Q0BBABAB | Micardis 80mg tablets | Telmisartan |
| 0205052R0BBAAAA | MicardisPlus 40mg/12.5mg tablets | Telmisartan with diuretic |
| 0205052R0BBABAB | MicardisPlus 80mg/12.5mg tablets | Telmisartan with diuretic |
| 0205052R0BBACAC | MicardisPlus 80mg/25mg tablets | Telmisartan with diuretic |
| 0205052R0AAAAAA | Telmisartan 40mg / Hydrochlorothiazide 12.5mg tablets | Telmisartan with diuretic |
| 0205052R0AAABAB | Telmisartan 80mg / Hydrochlorothiazide 12.5mg tablets | Telmisartan with diuretic |
| 0205052R0AAACAC | Telmisartan 80mg / Hydrochlorothiazide 25mg tablets | Telmisartan with diuretic |
| 0205052R0BDAAAA | Tolucombi 40mg/12.5mg tablets | Telmisartan with diuretic |
| 0205052R0BDABAB | Tolucombi 80mg/12.5mg tablets | Telmisartan with diuretic |
| 0205052R0BDACAC | Tolucombi 80mg/25mg tablets | Telmisartan with diuretic |
| 0205052Q0BCACAC | Tolura 20mg tablets | Telmisartan |

Showing 20 of 22 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Please check the current MHRA record, the SmPC and the BNF for full licensed indications and NICE guidance.

<!-- review:begin uk-lic-20261106-telmisartan-1 -->

> **Review correction (2026-11-06)**: Originally stated: "This is the only valid single-ingredient authorisation recorded. The record does not give the manufacturer, a PL number or indication text. Please check the current MHRA record, the SmPC and the BNF for full licensed indications and NICE guidance." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 22 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-telmisartan-1 -->

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
The prediction score from the TxGNN model (deep learning) is very high, but it may reflect similarities the model learned between related diseases, not biological evidence, together with a plausible endothelial and vasoconstriction hypothesis. No trials or publications were found, so this is an L5 prediction.

**To proceed, the following is needed:**
- A systematic literature search for ARBs (including telmisartan) in vasospastic or coronary spasm disorders, together with preclinical or mechanistic work on coronary vasospasm.
- Detailed mechanism of action data and SmPC warnings and contraindications for the UK product.
- Confirmation of the licence details (PL number, formulation and indication text) from the MHRA record.
- A safety assessment for hypotension and for patients with coronary disease.

**Note on other predictions:** Other predictions for telmisartan in the same data are better supported. The most advanced is **intracerebral hemorrhage** (L1, with the Phase 3 TRIDENT trial of a telmisartan-containing triple low-dose pill). It is confounded by the combination design and is a close extension of the existing hypertension and stroke indications. **Cerebral artery occlusion** (L3) has mainly animal data and overlaps with the stroke indications already approved. If a more evidence-based direction is wanted, a separate evaluation of these indications is recommended.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "This is the only valid single-ingredient authorisation recorded. The record does not give the manufacturer, a PL number or indication text" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

