---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 632
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Trandolapril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Trandolapril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "chronic pulmonary heart disease"]
---

# Trandolapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Trandolapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Trandolapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials** and **no publications** specific to this indication were found in the data compiled for this report. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, trandolapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is strongly driven by activation of the renin-angiotensin system, so blocking this pathway is biologically plausible. The predicted indication is also a severe form of the already-approved hypertension indication.

There are important caveats. The high TxGNN score likely reflects similarity to the approved hypertension indication rather than independent evidence. ACE inhibitors also carry a known risk of acute renal failure in bilateral renal artery stenosis, which is a direct safety concern in this population.

Other predictions in the list include malignant hypertensive renal disease (99.92%), pulmonary hypertension owing to lung disease and/or hypoxia (99.92%), pulmonary hypertension with unclear multifactorial mechanism (99.92%), Braddock syndrome (99.88%) and chronic pulmonary heart disease (99.19%). None has clinical trial support. Only the pulmonary hypertension and chronic pulmonary heart disease predictions have any literature, and that literature is preclinical or indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For context, the literature found for related pulmonary predictions is indirect and mostly preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Preclinical (animal/ex vivo) | General Pharmacology | Trandolapril plus verapamil inhibited hypoxia-induced coronary vasospasm after ischaemia-reperfusion injury in dogs |
| [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) | 1996 | Preclinical (animal) | J Card Fail | Long-term trandolapril treatment assessed for augmented vasoconstriction in rats with chronic heart failure |
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Preclinical (animal) | J Cardiovasc Pharmacol | Trandolapril regressed left ventricular hypertrophy in ageing spontaneously hypertensive rats |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Preclinical (animal) | J Hypertens Suppl | Preclinical results for verapamil plus trandolapril on blood pressure and cardiovascular or metabolic disease |
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Review | Am J Cardiol | Molecular basis of regression of cardiac hypertrophy |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Case report | J Natl Med Assoc | Pain from sickle cell disease resolved on an ACE inhibitor in one patient (indirect relevance) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051U0AAACAC (BNF-style product code; PL number not available) | Trandolapril capsules 2 mg | Capsule | Indication text not available |

One single-ingredient authorisation is currently valid. Please check the SmPC for the licensed indications.

---

## Cytotoxicity

Not applicable. Trandolapril is not an antineoplastic drug.

---

## Safety Considerations

- **Contraindications and disease associations (knowledge-graph derived, not label text):** The knowledge graph links trandolapril to caution or contraindication in several conditions. The most relevant to this report are:
  - Renal artery obstruction and kidney disease
  - Angioedema, including hereditary and ACE inhibitor-related forms
  - Aortic stenosis and hypertrophic cardiomyopathy
  - Hypotensive disorders
  - Liver disease
  - Neutropenia and agranulocytosis
  - Heart failure and some arrhythmias (ventricular tachycardia, atrioventricular block)

  These should be checked against the SmPC.
- **Drug Interactions:** 100 interactions were recorded. Major-level interactions include **potassium citrate** and **potassium bicarbonate**, which raise the risk of hyperkalaemia. Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic drugs (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, glimepiride, chlorpropamide), aspirin, morphine, bupropion, dronabinol, and bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes).
- **Indication-specific concern:** Because the predicted indication involves renal artery disease, the risk of acute renal failure with ACE inhibitors in bilateral renal artery stenosis is particularly important. Renal function and potassium monitoring would be essential.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no trials or publications for trandolapril in malignant renovascular hypertension. There is also a recognised renal safety concern in this setting.

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- Label-based warnings and contraindications from the SmPC and BNF, as the available safety data is knowledge-graph derived only
- Clinical or observational data on trandolapril in renovascular or malignant hypertension
- A renal safety and monitoring plan covering renal function and potassium, especially for renal artery stenosis
- Confirmation of the UK authorisation details (PL number, dosage form, licensed indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

