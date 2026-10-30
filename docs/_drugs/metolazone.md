---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 408
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Metolazone"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Metolazone: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Metolazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Metolazone: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Metolazone is a thiazide-like diuretic, originally used to treat hypertension.
but there are currently **no registered clinical trials** and **no relevant publications** supporting this direction. The evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, metolazone is a thiazide-like diuretic that inhibits the Na+/Cl- cotransporter in the distal convoluted tubule. Its efficacy in hypertension is established, and mechanistically a diuretic could reduce volume load in other hypertensive conditions.

Malignant renovascular hypertension is a severe, renin-driven form of hypertension. A diuretic could plausibly lower volume load, but thiazide-type agents are not first-line here. Management centres on blood pressure control and revascularisation, and RAAS blockade is hazardous in bilateral renal artery stenosis. The high TxGNN score most likely reflects the similarity of this condition to the original hypertension indication rather than any specific supporting evidence.

Other predicted indications are also weakly supported:
- **Malignant hypertensive renal disease** (score 0.9984): metolazone retains efficacy at reduced GFR and is used with loop diuretics for diuretic resistance, but this is a hypertensive emergency where parenteral agents and rapid controlled blood pressure reduction are standard. Oral metolazone has no established role, and there is a risk of excessive volume or electrolyte depletion.
- **Pulmonary hypertension (unclear multifactorial mechanism, and owing to lung disease/hypoxia)** (score 0.9983): diuretics offer indirect symptomatic relief of right-heart volume overload, but metolazone does not act on the pulmonary vascular mechanisms driving the disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), one paper was retrieved. It is preclinical and does not support the indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2916665](https://pubmed.ncbi.nlm.nih.gov/2916665/) | 1989 | Preclinical/Basic research | The American Journal of Physiology | In rats, binding of [3H]metolazone to thiazide receptors in the renal cortex fell by about 90% after 10 minutes of acute renal ischaemia, and this was reversible. It concerns renal receptor biology, not pulmonary hypertension. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0202010V0AAAAAA | Metolazone Tab 5mg | Not specified | Not specified |

Note: the licence data compiled for this report contain one valid single-ingredient authorisation. Dosage form and approved indication text are not available, so please check the current SmPC and BNF entry.

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease relationships in the TxGNN knowledge graph, not label text):
- Fluid and electrolyte or metabolic: potassium deficiency, hypercalcaemia, phosphorus metabolism disease, nephrocalcinosis, gout, anuria
- Hepatic: liver failure, hepatic coma, hepatic encephalopathy
- Diabetes-related: diabetes mellitus, diabetic ketoacidosis
- Cardiovascular and autonomic: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- Other: pancreatitis, systemic lupus erythematosus (including paediatric), HELLP syndrome

**Drug Interactions:** 100 interactions were identified in the interaction database; examples are below.
- Moderate: acarbose, alogliptin, albiglutide (antidiabetic agents, possible loss of glycaemic control); hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone (corticosteroids); amphotericin B (including lipid complex); omeprazole, rabeprazole; bupropion; morphine; bisacodyl; cholecalciferol; calcium phosphate
- Minor: doxycycline, hyoscyamine, atropine

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. There are no clinical trials and no relevant clinical literature. The clinical rationale is weak, because first-line management of malignant renovascular hypertension relies on RAAS blockade and revascularisation, and parenteral agents are standard in hypertensive emergencies. Metolazone also carries a risk of volume and electrolyte depletion in these settings.

**To proceed, the following is needed:**
- Mechanism of action data, to allow mechanistic-link analysis
- SmPC and BNF warnings and contraindications for formal safety screening
- Approved indication text, dosage form and manufacturer details for the UK authorisation
- Clinical or observational evidence in the predicted indication, followed by a specialist (nephrology/cardiology) review of whether any role exists beyond adjunctive diuretic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

