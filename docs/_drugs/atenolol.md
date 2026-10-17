---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Atenolol: predicted new indication Posterolateral myocardial infarction (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Atenolol: From Hypertension and Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-1 selective blocker, originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but this is an anatomical subtype of an indication it already covers, and **no clinical trials or publications** were found for this specific prediction.
Across the other top-ranked predictions, only small, old or indirect studies were identified, and the evidence is limited overall.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (the UK licence record compiled for this report contains no indication text) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, atenolol is a beta-1 selective adrenoceptor blocker. Blocking these receptors lowers heart rate, contractility and renin release, which reduces myocardial oxygen demand and blood pressure.

Posterolateral myocardial infarction is a subtype of myocardial infarction, which is already an established use of atenolol. The high TxGNN score therefore largely reflects the existing indication rather than a genuinely new repurposing signal. The same applies to the next-ranked predictions: posteroinferior and septal myocardial infarction (both subtypes of MI) and malignant renovascular hypertension (a form of hypertension).

Other predictions are much weaker mechanistically. Pulmonary hypertension and chronic pulmonary heart disease are areas where beta-blockers are generally avoided because of concern about right ventricular function and bronchospasm. Braddock syndrome has no identifiable mechanistic rationale and is likely a graph-based artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction, or for any of the other top-ranked predicted indications.

---

## Literature Evidence

No literature was found for the lead prediction (posterolateral myocardial infarction). The most relevant publications for the related predictions are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Randomised crossover study (single-blind) | La Revue de medecine interne | Atenolol 200 mg vs diltiazem 240 mg compared for anti-ischaemic activity in 23 patients after postero-inferior or anterior MI (posteroinferior MI prediction). Small and old |
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT | Clinical Therapeutics | Telmisartan vs atenolol over 26 weeks in mild to moderate hypertension; not about pulmonary heart disease |
| [30191469](https://pubmed.ncbi.nlm.nih.gov/30191469/) | 2018 | Retrospective cohort | Cardiology and Therapy | Cardiovascular hospitalisation risk with nebivolol vs atenolol and metoprolol in hypertensive patients; indirect |
| [7257500](https://pubmed.ncbi.nlm.nih.gov/7257500/) | 1981 | Clinical imaging study | Zeitschrift fur Kardiologie | Thallium-201 stress scintigraphy in 14 coronary artery disease patients after atenolol 5 mg IV; indirect pharmacodynamic observation (septal MI prediction) |
| [18454714](https://pubmed.ncbi.nlm.nih.gov/18454714/) | 2008 | Case report | Nefrologia | Teenager with neurofibromatosis type 1, aortic coarctation and renal artery stenosis; not evidence of efficacy in malignant renovascular hypertension |
| [8590992](https://pubmed.ncbi.nlm.nih.gov/8590992/) | 1995 | Preclinical (rat) | British Journal of Pharmacology | Propranolol reduced hypoxia-induced right heart hypertrophy in rats |
| [6212672](https://pubmed.ncbi.nlm.nih.gov/6212672/) | 1982 | Preclinical (rabbit) | The Journal of Physiology | Cardioselective and non-selective beta-blockers did not inhibit hypoxic cardiac hypertrophy, conflicting with the rat finding |
| [15881093](https://pubmed.ncbi.nlm.nih.gov/15881093/) | 2005 | Clinical study | Terapevticheskii Arkhiv | Respiratory effects of long-term atenolol in patients with ischaemic heart disease and COPD (safety-focused) |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Preclinical mechanistic | PLoS One | Beta-2 adrenergic receptor effects on hypoxic pulmonary vasoconstriction in rats; not specific to atenolol |

Many other records retrieved for the pulmonary hypertension prediction were unrelated (for example eclampsia, infantile haemangioma and beta-blocker intoxication) and are not listed.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0204000E0AAAAAA | Atenolol oral solution 25 mg/5 ml, sugar-free | Oral solution | Not stated in the data compiled for this report |

This identifier appears to be a BNF-style product code rather than a standard MHRA PL number. Atenolol belongs to BNF chapter 2 (cardiovascular system, beta-adrenoceptor blocking drugs). Please confirm the licensed indications in the SmPC.

---

## Safety Considerations

**Contraindications and cautions (from the knowledge graph, not label text):** the TxGNN knowledge graph links atenolol to contraindications in the following conditions:
- Cardiovascular: atrioventricular block, Raynaud disease
- Respiratory and allergic: asthma (including intrinsic and allergic asthma), anaphylaxis
- Metabolic: type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, gout and hyperuricaemia, hypercalcaemia, nephrocalcinosis, potassium deficiency, phosphorus metabolism disease
- Other: liver failure, pancreatitis, anuria, systemic lupus erythematosus (including paediatric), psoriasis and parapsoriasis, anxiety and related disorders

These are database associations and should be checked against the SmPC and BNF.

**Drug interactions:** 100 interactions were recorded. Those listed include:
- Moderate: epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acetohexamide, atropine, betamethasone, budesonide, and several calcium salts (acetate, carbonate, citrate, gluconate, lactate and others)
- Minor: acetylsalicylic acid, aluminium hydroxide, attapulgite

For any other safety information, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions are subtypes of indications atenolol already has, so they offer little genuine repurposing value, and the truly novel ones (pulmonary hypertension, chronic pulmonary heart disease, Braddock syndrome) have no supportive human evidence and carry plausible safety concerns. The evidence level is L5 for the lead prediction.

**To proceed, the following is needed:**
- Confirmation of the licensed indications from the SmPC, as the UK licence record has no indication text
- Mechanism of action data to support mechanistic analysis
- Safety label data (warnings and contraindications) to enable formal safety screening
- A decision on whether the MI and hypertension subtype predictions add anything beyond existing labelling
- Prospective clinical evidence before any consideration of pulmonary hypertension or cor pulmonale, given the right heart and bronchospasm concerns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

