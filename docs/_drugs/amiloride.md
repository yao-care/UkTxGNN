---
layout: default
title: Amiloride
parent: Model Prediction Only (L5)
nav_order: 49
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
description: "Amiloride: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Amiloride: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic, originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **no clinical trials** and **no directly relevant publications** supporting this prediction.
Of the other predicted indications reviewed, only pulmonary hypertension due to lung disease or hypoxia and chronic pulmonary heart disease have any supporting literature, and it is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, amiloride blocks the epithelial sodium channel (ENaC) in the distal nephron. This reduces sodium reabsorption and conserves potassium, which lowers blood pressure and fluid retention. Its efficacy in hypertension and heart failure is well established.

Hypertensive renal disease is closely related to the original indication, so a high model score is understandable. However, the prediction most likely reflects amiloride's existing use in hypertension rather than a genuinely new therapeutic signal. Malignant hypertension is a hypertensive emergency and is not managed with potassium-sparing diuretics. Hyperkalaemia risk is also a significant concern when renal function is impaired.

Other predictions were also reviewed:
- **Malignant renovascular hypertension (0.9982):** ENaC inhibition is relevant to mineralocorticoid-driven hypertension. However, the only linked paper is a general 2003 review on investigating mineralocorticoid hypertension, not a study of amiloride.
- **Pulmonary hypertension due to lung disease or hypoxia (0.9981):** Preclinical work suggests hypoxia downregulates alveolar ENaC, and ASIC1a channels (also targeted by amiloride) contribute to hypoxic pulmonary hypertension. No study shows amiloride treats this condition in patients. This is the only alternative with a research-question rationale (L4).
- **Chronic pulmonary heart disease (0.9968):** Heart failure studies exist, but they address congestive heart failure, an existing indication, not cor pulmonale specifically. Evidence is indirect (L4).
- **Pulmonary hypertension with unclear multifactorial mechanism and Braddock syndrome:** No trials, no literature, and no clear mechanistic link. The scores are likely TxGNN model (deep learning) artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports the lead prediction (malignant hypertensive renal disease). The most relevant publications found for related predicted indications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/) | 1987 | RCT (crossover) | Lancet | Captopril alone compared with furosemide plus amiloride in 14 patients with mild heart failure. Ten remained stable on captopril alone; four deteriorated, all with prior pulmonary oedema. |
| [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/) | 1991 | Clinical study (double-blind, placebo-controlled crossover) | Cardiovasc Drugs Ther | Amiloride improved haemodynamics in 11 men with chronic heart failure on digoxin and diuretics. Relevant to heart failure, not cor pulmonale. |
| [25398716](https://pubmed.ncbi.nlm.nih.gov/25398716/) | 2015 | Review | Exp Physiol | Smooth muscle ASIC1 contributes to hypoxic pulmonary hypertension, providing a preclinical rationale. |
| [9376126](https://pubmed.ncbi.nlm.nih.gov/9376126/) | 1997 | Preclinical | Am J Respir Cell Mol Biol | Hypoxia reduced amiloride-sensitive sodium channel activity in rat alveolar epithelial cells. |
| [15219007](https://pubmed.ncbi.nlm.nih.gov/15219007/) | 2004 | Cohort/physiological study | Eur Respir J | High altitude impaired nasal sodium transport in subjects prone to high-altitude pulmonary oedema (indirect human physiology). |
| [16222038](https://pubmed.ncbi.nlm.nih.gov/16222038/) | 2005 | Review | Proc Am Thorac Soc | Reviews effects of hypoxia on alveolar epithelial function. |
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | General discussion of investigating mineralocorticoid hypertension; not an amiloride study. |
| [8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/) | 1996 | Case report | Am J Med Sci | Severe hyperkalaemia (K⁺ 9.3 mEq/L) in a 96-year-old woman with heart failure on trimethoprim-sulfamethoxazole. Highlights a key safety concern. |

Many other retrieved papers (ovarian cancer pH, choroid plexus transport, hepatic ischaemia-reperfusion, neonatal brain injury, patch-clamp assay development) were off-topic and are not listed.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0202030C0AAACAC | Amiloride HCl Tab 5mg | Tablet (5 mg) | Not available in the data compiled for this report |

One valid single-ingredient authorisation is recorded. Please check the current SmPC and BNF (potassium-sparing diuretics) for the licensed indications and dosing.

---

## Safety Considerations

- **Hyperkalaemia:** This is the key concern. A case report describes severe hyperkalaemia in an elderly patient with heart failure given trimethoprim-sulfamethoxazole. Risk is higher in renal impairment, which is directly relevant to the predicted renal indications.
- **Conditions linked to contraindications in the knowledge graph:** These come from the TxGNN knowledge graph, not from label text, so confirm them against the SmPC.
  - Renal and urinary: kidney disease, anuria, diabetic nephropathy, pyoureter
  - Liver and biliary: liver disease, gallbladder disease, hepatic coma, hepatic encephalopathy, neonatal jaundice
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency disease, hyperuricaemia, gout, acidosis, acquired lactic acidosis
  - Other: pancreatitis, systemic lupus erythematosus (including paediatric), hyperparathyroidism, osteitis fibrosa
- **Drug interactions (100 recorded, mostly Moderate or Minor):**
  - Moderate: metformin, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), exenatide, corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), bupropion, dronabinol, and laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose)
  - Minor: doxycycline, amoxicillin, cimetidine

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is model-only (L5) for the lead indication, with no trials and no relevant literature. The signal likely reflects the existing hypertension indication, and malignant hypertension is not appropriately treated with a potassium-sparing diuretic, particularly given the hyperkalaemia risk in renal impairment. Pulmonary hypertension due to lung disease or hypoxia and chronic pulmonary heart disease (both L4) may be worth exploring as research questions only.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Approved indication text and dosage form from the MHRA/SmPC record, plus warnings and contraindications from the SmPC and BNF
- Clinical studies of amiloride in the predicted conditions, particularly hypoxic pulmonary hypertension and cor pulmonale
- A renal and potassium monitoring plan, with review of the knowledge-graph contraindications (kidney disease, diabetes, liver disease) against label text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

