---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 342
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Irbesartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Irbesartan: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), originally used to treat hypertension and diabetic nephropathy.
but there are currently **no clinical trials** and **no publications** directly supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

Other predicted indications in the data compiled for this report:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 0.9931 | L5 | Hold |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 0.9925 | L5 | Hold |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9925 | L5 | Research Question |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Irbesartan is known to be an AT1 receptor blocker. It is already used for hypertension and diabetic nephropathy, and its efficacy there is established.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, so blocking AT1 receptors offers a plausible antihypertensive effect. The second prediction, malignant hypertensive renal disease, is a natural extension of the existing hypertension and diabetic nephropathy indications, because RAS blockade is renoprotective.

An important caution: ARBs carry a known risk of acute renal function decline in bilateral renal artery stenosis or stenosis in a solitary kidney. This is directly relevant to renovascular disease and needs careful safety review before any repurposing.

The pulmonary hypertension predictions are more speculative. Angiotensin II signalling through AT1 receptors may contribute to pulmonary vascular remodelling and vasoconstriction, but the underlying causes are heterogeneous and the mechanistic link is unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction (malignant renovascular hypertension). The table below covers the fourth prediction, pulmonary hypertension owing to lung disease and/or hypoxia. All of the studies are preclinical, indirect or review-level, and none assesses pulmonary hypertension in patients. Studies on other agents or unrelated topics have been left out.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Reviews the pleiotropic effects of AT1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Animal study | Biomed Pharmacother | Irbesartan ameliorated pulmonary artery lesions in a rat model of chronic mountain sickness, via cholesterol metabolism |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Animal study | Eur Rev Med Pharmacol Sci | Irbesartan improved oxidative stress in rats with high-altitude pulmonary hypertension, with involvement of intestinal flora |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | In vitro/preclinical | PLoS One | Irbesartan protected cardiomyocytes under hypoxic stress |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Animal study | Sleep Breath | Irbesartan attenuated sleep apnoea-induced cardiac apoptosis and upregulated Sirtuin 1 |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Animal study | Am J Physiol Heart Circ Physiol | Irbesartan inhibited coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205052I0AAAAAA | Irbesartan Tab 75mg | Not specified | Not specified |

Only one valid single-ingredient authorisation is recorded, and no dosage form or indication text was supplied. Please check the current MHRA record and BNF (cardiovascular system, angiotensin-II receptor antagonists) for full details.

## Safety Considerations

**Contraindications and conditions flagged in the knowledge graph** (these come from drug-disease relationships in the TxGNN knowledge graph, not from product label text):

- Angioedema (including hereditary, acquired and RAS-blocker-induced forms)
- Renal and urinary: anuria, renal artery obstruction, nephrocalcinosis
- Metabolic and electrolyte: potassium deficiency disease, hypercalcaemia, phosphorus metabolism disease, hyperparathyroidism, gout, hyperuricaemia, diabetes mellitus, diabetic ketoacidosis
- Hepatic: hepatic coma and encephalopathy
- Other: hypotensive disorder, pancreatitis, systemic lupus erythematosus, myopathy and rhabdomyolysis, familial periodic paralysis, neonatal jaundice

Several of these entries (for example gout and nephrocalcinosis) look more like thiazide-type warnings than ARB-specific ones, so they should be verified against the SmPC.

**Drug interactions:** 100 interactions were recorded. Those listed in the data are mostly of moderate severity. The major-severity interactions are:

- Potassium citrate (Major)
- Potassium bicarbonate (Major)

Both carry a risk of hyperkalaemia with ARBs.

Moderate interactions include:

- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
- SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
- Insulins (aspart, degludec)
- Aspirin
- Morphine
- Bupropion
- Aprepitant
- Dronabinol
- Bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate)

Report suspected adverse reactions via the Yellow Card Scheme. Please also refer to the SmPC and BNF for authoritative warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (0.9931) is a computational prediction only. No clinical trials or literature support irbesartan in malignant renovascular hypertension, and the known renal risk of ARBs in renal artery stenosis raises a specific safety concern. The pulmonary hypertension signal (L4) is preclinical and indirect, so it is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- A systematic literature search for ARB use in renovascular and malignant hypertension
- A safety review of renal function risk in bilateral renal artery stenosis or solitary kidney
- Detailed mechanism of action data
- SmPC warnings and contraindications, which were not available in the data compiled for this report
- Confirmation of the approved indication and dosage form from the MHRA record
- For pulmonary hypertension, direct preclinical models of pulmonary hypertension, followed by early-phase clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

