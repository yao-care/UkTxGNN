---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-06
monitor_inn: "Propranolol"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
description: "Propranolol: predicted new indication Distal myopathy, Tateyama type (evidence level L5). Approved use: Not recorded in the local data"
---

# Propranolol
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

## Propranolol: Distal myopathy, Tateyama type
{: .text-alpha }

## One-Sentence Summary

Propranolol is a non-selective beta-blocker, originally used for hypertension, arrhythmias, hypertrophic cardiomyopathy and infantile haemangioma-type vascular conditions.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, a rare muscle disease.
This prediction is currently supported by **0 clinical trials** and **0 publications**, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 0.9940 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (67 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 67 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Propranolol is a non-selective beta-adrenergic blocker. Its efficacy in cardiovascular conditions such as hypertension, arrhythmia and hypertrophic cardiomyopathy is well established. Mechanistically, it reduces heart rate, myocardial contractility and oxygen demand.

No plausible link between beta-adrenergic blockade and this rare distal myopathy can be established from the available data. The high score (0.9940) comes from the TxGNN model (deep learning). It may reflect similarities the model learned between related diseases, not biological evidence. It is not evidence of a pharmacological rationale. This prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0204000R0AACMCM | Propranolol 1.67mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AADKDK | Propranolol 10mg orodispersible tablets sugar free | Propranolol hydrochloride |
| 0204000R0AAAHAH | Propranolol 10mg tablets | Propranolol hydrochloride |
| 0204000R0AACJCJ | Propranolol 10mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACXCX | Propranolol 10mg/5ml oral solution sugar free | Propranolol hydrochloride |
| 0204000R0AACRCR | Propranolol 15mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AAABAB | Propranolol 160mg modified-release capsules | Propranolol hydrochloride |
| 0204000R0AAALAL | Propranolol 160mg tablets | Propranolol hydrochloride |
| 0204000R0AADEDE | Propranolol 16mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AAACAC | Propranolol 1mg/1ml solution for injection ampoules | Propranolol hydrochloride |
| 0204000R0AACSCS | Propranolol 2.5mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACQCQ | Propranolol 2.75mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACPCP | Propranolol 20mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AADGDG | Propranolol 22.5mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACKCK | Propranolol 25mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACUCU | Propranolol 2mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACZCZ | Propranolol 3.5mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AADADA | Propranolol 32mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AACTCT | Propranolol 3mg/5ml oral liquid | Propranolol hydrochloride |
| 0204000R0AADLDL | Propranolol 40mg orodispersible tablets sugar free | Propranolol hydrochloride |

Showing 20 of 67 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

The identifier above is not in the standard MHRA "PL XXXXX/XXXX" format. It should be verified against the MHRA register and the BNF before any reliance is placed on it.

---

## Safety Considerations

Label-derived warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for these. Report suspected adverse reactions via the Yellow Card Scheme.

- **Disease contraindications flagged in the knowledge graph** (derived from graph relationships, not from label text; they require confirmation against the SmPC): bronchitis, kidney disease, liver disease, pancreatitis, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, gout, myasthenia gravis, systemic lupus erythematosus, anxiety and neurotic disorders, and several muscle disorders (myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis). Also flagged were hepatic coma and encephalopathy, anuria, hyperparathyroidism, hypercalcaemia, nephrocalcinosis, potassium deficiency and neonatal jaundice.
  - The muscle-related flags are relevant here. The knowledge graph links propranolol to myopathy as a contraindication, which sits uneasily with a prediction of benefit in a myopathy.
- **Drug interactions** (DDInter, 100 interactions recorded; examples below):
  - **Major:** epinephrine.
  - **Moderate:** hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, atropine, hyoscyamine, methscopolamine, bupropion, morphine, lorcaserin, canagliflozin, chlorpropamide, cimetidine, calcium acetate, calcium phosphate.
  - **Minor:** ascorbic acid, acetylsalicylic acid, magnesium oxide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications and no identifiable mechanistic link. The knowledge graph also lists myopathy as a contraindication-type association for propranolol. The evidence level is L5.

**To proceed, the following is needed:**
- Evidence of a biological mechanism connecting beta-adrenergic signalling to the pathology of distal myopathy, Tateyama type.
- Systematic literature and registry searches (including ISRCTN and the EU Clinical Trials Register) for any relevant preclinical or clinical data.
- Clarification of the knowledge-graph myopathy contraindication against SmPC and BNF content.
- Verification of the UK licence record, including the product's authorisation number and approved indication.
- Complete mechanism of action and label safety data.

**Other predicted indications:** Cirrhotic cardiomyopathy and the broader category of cardiomyopathy have some supporting literature (Evidence Levels L4 and L3). For cardiomyopathy, much of the evidence overlaps with the existing hypertrophic cardiomyopathy use. For cirrhotic cardiomyopathy, some publications raise safety concerns about beta-blockers in advanced cirrhosis. If the programme is to continue, these are more evidence-supported candidates for further review than the one assessed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

