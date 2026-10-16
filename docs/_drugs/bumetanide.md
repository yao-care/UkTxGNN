---
layout: default
title: Bumetanide
parent: Model Prediction Only (L5)
nav_order: 114
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Bumetanide: predicted new indication Acute pulmonary heart disease (evidence level L5). Approved use: Congestive heart failure"
monitor_inn: "Bumetanide"
predicted_indications: ["acute pulmonary heart disease"]
---

# Bumetanide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Bumetanide: From Congestive Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a loop diuretic, originally used to treat congestive heart failure.
The TxGNN model predicts it may be effective for **acute pulmonary heart disease**, but there are currently **no registered clinical trials** and only **5 publications** (mostly general reviews of heart failure and diuretics), so the evidence for this specific new indication is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congestive heart failure (the approved indication text for the UK authorisation is not available in the data compiled for this report) |
| Predicted New Indication | Acute pulmonary heart disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only; no studies specific to the predicted indication) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, bumetanide is a loop diuretic that inhibits the Na-K-2Cl cotransporter (NKCC2) in the thick ascending limb of the loop of Henle. This produces rapid natriuresis and diuresis.

Acute pulmonary heart disease (acute cor pulmonale) involves right ventricular overload, for example from pulmonary embolism or acute lung injury. Reducing right-sided preload and systemic venous congestion could plausibly relieve right ventricular distension and peripheral or hepatic congestion. This is the same principle that underpins bumetanide's use in congestive heart failure and volume overload.

This link is indirect. It rests on the drug's established use in heart failure, not on studies in acute pulmonary heart disease. The high TxGNN score is a computational prediction and probably reflects similarity to the approved heart failure indication. There is also a physiological caution: the failing right ventricle in acute cor pulmonale depends on adequate preload, so excessive diuresis could reduce cardiac output and make the condition worse.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Clinical haemodynamic study | Br J Clin Pharmacol | Intravenous bumetanide in 24 patients with coronary artery disease and acute exercise-induced or chronic heart failure. Cardiac index and pulmonary artery occluded pressure fell, while systemic arterial pressure and vascular resistance rose. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Review of bumetanide pharmacology and use. A potent loop diuretic for oedema in congestive heart failure, hepatic and renal disease and acute pulmonary congestion, with rapid onset (within 30 minutes) and a duration of 3 to 6 hours. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Reviews treatment options and recent trials in acute heart failure, where most patients are managed with diuretics. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Compares the pharmacokinetics, safety, efficacy and cost of loop diuretics, and asks whether furosemide should be first line. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohort | Am J Emerg Med | Epidemiology of heart failure presentations to US emergency departments from 2016 to 2023. This is background data rather than evidence on bumetanide. |

None of these publications studies bumetanide specifically in acute pulmonary heart disease.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0202020D0AAAEAE | Bumetanide tablets 1 mg | Tablet | Not available in the data compiled for this report |

Please check the BNF classification and the current SmPC for the authorised indications. Whether NICE has appraised any indication was not covered by the data compiled for this report.

---

## Safety Considerations

**Contraindication-related conditions (from the TxGNN knowledge graph, not label text):**
The knowledge graph links bumetanide to the following conditions as contraindications or cautions: liver disease, hepatic coma and hepatic encephalopathy, gallbladder disease, thrombocytopenia, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, anuria, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, and hearing disorders or auditory system disease. These should be checked against the SmPC.

**Drug Interactions:**
A total of 100 interactions were recorded. Examples from the first 20 are:
- **Moderate:** acarbose, metformin, alogliptin and albiglutide (antidiabetic agents); corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone); amphotericin B formulations; omeprazole and rabeprazole; bupropion; morphine; bisacodyl; acetohexamide.
- **Minor:** doxycycline, acetylsalicylic acid.

**Specific concern for the proposed use:** reducing preload in acute right ventricular failure may lower cardiac output.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but indirect. There are no clinical trials and no studies in acute pulmonary heart disease, and the physiological risk of preload reduction in acute right ventricular failure is not addressed by the available evidence.

**To proceed, the following is needed:**
- Clinical or mechanistic studies of loop diuretics in acute cor pulmonale, particularly on haemodynamic safety
- Detailed mechanism of action data
- The approved indication text, warnings and contraindications from the SmPC
- Review of current guidelines on managing acute right ventricular failure, to see where diuretics are positioned
- Dosage form and manufacturer details for the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

