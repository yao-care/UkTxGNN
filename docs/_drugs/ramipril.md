---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 534
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Hypertension to Pulmonary Hypertension (Prediction-Only)

## One-Sentence Summary

Ramipril is an angiotensin-converting enzyme (ACE) inhibitor, originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, but **no clinical trials and no supporting publications** were found for this indication. The closest supporting literature (preclinical, one animal study) relates to the related prediction of pulmonary hypertension owing to lung disease and/or hypoxia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (also stroke and cerebrovascular disorders, cerebral infarction) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*Note: The data compiled for this report contain 9 ranked predictions. The top-ranked prediction has no supporting studies. The best-supported prediction is **cerebral artery occlusion** (L4, preclinical and one small clinical study); it is discussed under "Other Predictions" below.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, ramipril is an ACE inhibitor. It reduces the conversion of angiotensin I to angiotensin II, lowering angiotensin II-mediated vasoconstriction and vascular remodelling.

Its efficacy in systemic hypertension is established. Because the renin-angiotensin system is also implicated in pulmonary vascular tone and remodelling, ACE inhibition is mechanistically plausible in pulmonary hypertension. This is a theoretical link only: no trials or literature were supplied for the top-ranked indication.

For the closely related prediction of pulmonary hypertension owing to lung disease and/or hypoxia, one 1996 rat study (PMID 9200213) reported that ramipril attenuated the effects of chronic hypoxia on pulmonary blood vessels. This is indirect, animal-only evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications were retrieved for the top-ranked indication. The table below shows the most relevant publications for the related hypoxic pulmonary hypertension prediction (rank 2). Most other retrieved papers were off-topic and are omitted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (animal) | Physiological Research | Ramipril (10 mg/kg daily) in rats exposed to chronic hypoxia lowered baseline perfusion pressure in the pulmonary vasculature, attenuating hypoxic pulmonary hypertension |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | Preclinical/Translational | European Heart Journal | ACE2 expression increased after myocardial infarction in rats and humans; only indirectly relevant |
| [18464162](https://pubmed.ncbi.nlm.nih.gov/18464162/) | 2008 | Preclinical (animal, renal) | Microcirculation | Ramipril or valsartan preserved peritubular capillaries; renal, not pulmonary |

## Other Predictions

| Predicted Indication | TxGNN Score | Evidence Level | Summary |
|------|------|------|------|
| Cerebral artery occlusion | 99.74% | L4 | One small clinical study (PMID 8797135, 1996) of ramipril vs enalapril on cerebral blood flow in 15 elderly patients with asymptomatic carotid stenosis. Animal studies are mixed: ACE inhibition reduced infarction in normotensive but not hypertensive rats (PMID 20407464), and candesartan but not ramipril improved outcome (PMID 18300867). |
| Intracerebral haemorrhage | 99.82% | L4 | Indirect animal data only (e.g. PMID 15721222); no direct clinical evidence |
| Malignant hypertensive renal disease | 99.93% | L5 | Prediction only |
| Malignant renovascular hypertension | 99.93% | L5 | Prediction only; safety concern in bilateral renal artery stenosis |
| Braddock syndrome | 99.91% | L5 | Prediction only; no clear mechanistic rationale |
| Brain stem infarction | 99.89% | L5 | Prediction only |
| Prinzmetal angina | 99.83% | L5 | Prediction only; the single retrieved paper is unrelated to ramipril |
| ABri amyloidosis | 99.79% | L5 | Prediction only; no clear mechanistic rationale |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205051R0AAAAAA | Ramipril capsules 1.25 mg | Capsule (per product name) | Not available in the data compiled |

The authorisation number above is in the format supplied in the data and does not follow the usual MHRA "PL" format. It should be verified against the MHRA register. Ramipril is classified in the BNF under ACE inhibitors (cardiovascular system).

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, liver disease, renal artery obstruction, hereditary angioedema, hypotensive disorder, neutropenia and agranulocytosis, systemic lupus erythematosus, scleroderma and systemic sclerosis, connective tissue disease, gallbladder disease, bone and cartilage disease.

**Drug Interactions (100 interactions recorded; examples shown):**
- **Major:** potassium citrate, potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, morphine, and several antidiabetic drugs (metformin, glimepiride, chlorpropamide, alogliptin, and SGLT2 inhibitors such as canagliflozin, dapagliflozin and empagliflozin)

Product-specific warnings and contraindications from the SmPC were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on model output alone (L5), with no trials or literature. The only supporting evidence for related pulmonary hypertension is a single 1996 animal study. Ramipril is already marketed and well characterised, but there is no basis yet to pursue pulmonary hypertension as a new indication.

**To proceed, the following is needed:**
- Targeted literature review of ACE inhibitors in pulmonary hypertension, ideally with human data
- Detailed mechanism of action data to support the pulmonary vascular link
- Approved indication text and dosage form details for the UK marketing authorisation
- SmPC-based safety data (warnings and contraindications), and a review of the safety implications of the knowledge-graph contraindications, particularly renal disease
- If a repurposing direction is pursued, consider prioritising cerebral artery occlusion, which has the strongest (though still L4) evidence among the predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

