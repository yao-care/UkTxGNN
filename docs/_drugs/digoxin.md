---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 226
evidence_level: L5
indication_count: 6
---

# Digoxin
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

# Digoxin: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside originally used for atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**,
but there are currently **no registered clinical trials** and only **1 publication** (a general review that does not directly address this question), so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; digitalis poisoning (from the knowledge graph, as the UK authorisation record has no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Digoxin is a cardiac glycoside that is generally understood to inhibit Na+/K+-ATPase, which raises intracellular calcium. This underlies its use in controlling ventricular rate in atrial fibrillation.

The link to Prinzmetal (vasospastic) angina is weak. Raising intracellular calcium could, in theory, promote vasospasm rather than relieve it. Vasospastic angina is conventionally treated with calcium channel blockers and nitrates, which act in the opposite direction. The high TxGNN score appears to reflect graph-based associations between cardiovascular drugs and diseases rather than a credible pharmacological rationale.

Other predictions in the list (duodenal obstruction, duodenal ulcer, duodenogastric reflux, susceptibility to ischaemic stroke, hypoalphalipoproteinaemia) also have no supporting trials or mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | General review of chronopharmacology and circadian rhythms in antihypertensive treatment. It does not provide direct evidence for digoxin in Prinzmetal angina. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0201010F0AAADAD | Digoxin Tab 62.5mcg | Not specified | Not specified |

The record shows one valid single-ingredient product. The authorisation number is as it appears in the compiled data and does not follow the standard PL format, so it should be checked against the MHRA register.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph associations, not label text, and should be verified against the SmPC):
  - Cardiac: myocardial infarction, coronary thrombosis, Wolff-Parkinson-White syndrome, sick sinus syndrome, ventricular fibrillation, hypertrophic cardiomyopathy, atrioventricular block, myocarditis, constrictive pericarditis, restrictive cardiomyopathy, cor pulmonale
  - Metabolic and renal: kidney disease, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, hypothyroidism and myxoedema
  - Other: haemoglobinopathy, pyoureter
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. The first 20 listed are mostly Moderate, with some Minor:
  - Moderate: acarbose, rabeprazole, doxycycline, tetracycline, epinephrine, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, calcium phosphate, metformin, amphotericin B (including the lipid complex), bupropion, acetylsalicylic acid
  - Minor: albiglutide, hyoscyamine, atropine, glycopyrronium

Digoxin has a narrow therapeutic index. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no clinical trials, the single retrieved publication is not relevant to the proposed indication, and the proposed mechanism (increased intracellular calcium) may even be counterproductive in vasospastic angina.

**To proceed, the following is needed:**
- A plausible mechanistic rationale, supported by preclinical or mechanistic studies
- Retrieval of the mechanism of action data
- Review of the UK SmPC and BNF safety information (warnings and contraindications are currently missing)
- Confirmation of the UK authorisation details (dosage form, approved indication, authorisation number format)
- Targeted literature review of digoxin in coronary vasospasm, including any reports of harm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

