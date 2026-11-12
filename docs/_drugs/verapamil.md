---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 653
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Hypertension, atrial fibrillation, acute coronary syndrome…"
monitor_inn: "Verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
---

# Verapamil
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

## Verapamil: From Hypertension and Arrhythmia to Obsolete Bundle Branch Block
{: .text-alpha }

## One-Sentence Summary

Verapamil is an L-type calcium channel blocker, originally used for hypertension, atrial fibrillation, angina and ventricular tachycardia.
The TxGNN model's (deep learning) top-ranked prediction is **obsolete bundle branch block**, which is almost certainly a model artefact. It is backed by **no clinical trials** and **only indirect preclinical literature**.

This report covers the top-ranked prediction and the best-supported alternative, because the top-ranked prediction has no evidence and a mechanistic concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, acute coronary syndrome, Prinzmetal angina, ventricular tachycardia (the UK licence record has no indication text) |
| Predicted New Indication (rank 1) | Obsolete bundle branch block |
| Best-supported alternative | Pulmonary hypertension owing to lung disease and/or hypoxia (rank 5) |
| TxGNN Prediction Score | 0.9962 (rank 1); 0.9926 (rank 5 alternative) |
| Evidence Level | L5 (rank 1); L4 (rank 5 alternative) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (47 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 47 |
| Recommended Decision | Hold (rank 1); Research question only (rank 5 alternative) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, verapamil blocks L-type calcium channels, relaxing vascular smooth muscle and slowing atrioventricular (AV) nodal conduction. This underpins its use in hypertension, supraventricular arrhythmias and angina.

**Bundle branch block (rank 1).** The mechanistic case is weak. Slowing conduction is not a treatment for bundle branch block, and AV nodal blockade could worsen conduction disease. The term is also flagged as obsolete in the ontology. The high score (0.9962) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Pulmonary hypertension owing to lung disease and/or hypoxia (rank 5).** Hypoxic pulmonary vasoconstriction depends partly on L-type calcium channel activity, so calcium channel blockade is mechanistically plausible. However, blocking hypoxic vasoconstriction may worsen gas exchange through ventilation-perfusion mismatch, and verapamil's negative inotropic effect is a concern in right ventricular dysfunction. In pulmonary arterial hypertension, calcium channel blockers are used only in a small vasoreactive subgroup, mainly with dihydropyridines or diltiazem.

The other predictions (malignant hypertensive renal disease, pulmonary hypertension of unclear multifactorial mechanism, Braddock syndrome, periodic paralysis with transient compartment-like syndrome) have no supporting trials, and their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

**Bundle branch block:** Currently no related literature available.

**Pulmonary hypertension owing to lung disease and/or hypoxia (rank 5):** 20 records were retrieved, but most are off-topic (retinal neuroprotection, natural product chemistry, migraine, multifocal atrial tachycardia). The most relevant are preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24977753](https://pubmed.ncbi.nlm.nih.gov/24977753/) | 2014 | Preclinical (animal) | J Trauma Acute Care Surg | Verapamil preserved cytoskeletal function in an intestinal model after hypoxia-reoxygenation |
| [9768801](https://pubmed.ncbi.nlm.nih.gov/9768801/) | 1998 | Preclinical (ex vivo) | Anesth Analg | Ketamine-induced pulmonary vasodilation in isolated rat lung is partly mediated by L-type calcium channels (verapamil used as a probe) |
| [21962069](https://pubmed.ncbi.nlm.nih.gov/21962069/) | 2011 | Preclinical (animal) | High Alt Med Biol | Long-term hypoxia and serotonin-mediated calcium influx through L-type channels in sheep pulmonary arteries |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathol Biol | Calcium antagonists (including verapamil) for migraine prophylaxis; efficacy not firmly demonstrated (off-topic) |
| [9440591](https://pubmed.ncbi.nlm.nih.gov/9440591/) | 1998 | Review | Chest | Multifocal atrial tachycardia, commonly seen with COPD (indirect context only) |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review | Horm Metab Res | Factors affecting the aldosterone/renin ratio; malignant or renovascular hypertension can cause false negatives |
| [10224210](https://pubmed.ncbi.nlm.nih.gov/10224210/) | 1999 | Case report | Pediatrics | Solitary renal myofibromatosis as a cause of infantile renovascular hypertension |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0206020T0AAA3A3 | Verapamil 10mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AAAIAI | Verapamil 120mg modified-release capsules | Verapamil hydrochloride |
| 0206020T0AAAUAU | Verapamil 120mg modified-release tablets | Verapamil hydrochloride |
| 0206020T0AAAFAF | Verapamil 120mg tablets | Verapamil hydrochloride |
| 0206020T0AABABA | Verapamil 120mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AAAGAG | Verapamil 160mg tablets | Verapamil hydrochloride |
| 0206020T0AAAJAJ | Verapamil 180mg modified-release capsules | Verapamil hydrochloride |
| 0206020T0AAA2A2 | Verapamil 20mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AAAKAK | Verapamil 240mg modified-release capsules | Verapamil hydrochloride |
| 0206020T0AAAHAH | Verapamil 240mg modified-release tablets | Verapamil hydrochloride |
| 0206020T0AABHBH | Verapamil 240mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AABFBF | Verapamil 250mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AABEBE | Verapamil 30mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AAACAC | Verapamil 40mg tablets | Verapamil hydrochloride |
| 0206020T0AAAZAZ | Verapamil 40mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AAAVAV | Verapamil 40mg/5ml oral solution sugar free | Verapamil hydrochloride |
| 0206020T0AABDBD | Verapamil 45mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AABGBG | Verapamil 50mg/5ml oral liquid | Verapamil hydrochloride |
| 0206020T0AAAAAA | Verapamil 5mg/2ml solution for injection ampoules | Verapamil hydrochloride |
| 0206020T0AAADAD | Verapamil 80mg tablets | Verapamil hydrochloride |

Showing 20 of 47 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The record corresponds to BNF section 2.6.2 (calcium-channel blockers).

<!-- review:begin uk-lic-20261106-verapamil-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The record corresponds to BNF section 2.6.2 (calcium-channel blockers). No licence number in PL format, dosage form or indication text was available, so the UK licensed indications should be confirmed against the current SmPC." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 47 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-verapamil-1 -->

---

## Safety Considerations

**Contraindications (from knowledge-graph drug-disease edges, not label text):** The knowledge graph links verapamil with several conditions, including:
- Cardiac: heart failure, atrioventricular block, hypotensive disorder, aortic stenosis, hypertrophic cardiomyopathy, ventricular tachycardia (graph edges, to be verified against the SmPC)
- Hepatic and renal: liver disease, kidney disease, renal artery obstruction
- Neuromuscular: myasthenia gravis and neuromuscular junction disease
- Haematological: neutropenia, agranulocytosis
- Angioedema (including hereditary forms)

These should be treated as signals requiring verification, not as confirmed label contraindications.

**Drug Interactions:** 100 interactions were identified. The sample reviewed included:
- **Major:** loperamide
- **Moderate:** clarithromycin, cimetidine, aprepitant, bupropion, acetylsalicylic acid, metformin, canagliflozin, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone) and calcium salts
- **Minor:** morphine

Several of these (clarithromycin, cimetidine, aprepitant) are plausibly related to CYP3A4 or P-glycoprotein effects, but the mechanisms are not stated in the data.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** (for obsolete bundle branch block and the other prediction-only candidates). Pulmonary hypertension owing to lung disease and/or hypoxia is a **research question** only.

**Rationale:**
- The top-ranked prediction has no trials or literature, an unfavourable mechanistic rationale (possible worsening of conduction disease) and an obsolete ontology term. Its high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- The best-supported alternative has only indirect preclinical evidence, with concerns about V/Q mismatch and negative inotropy.

**To proceed, the following is needed:**
- Mechanism of action data and the current UK SmPC warnings and contraindications (the safety screen cannot be completed without these)
- Confirmation of the UK marketing authorisation number, dosage form and licensed indications
- For pulmonary hypertension: direct preclinical or early clinical data on verapamil in hypoxia-related pulmonary hypertension, including gas exchange and right ventricular safety
- Review of the 30 knowledge-graph contraindication signals against label text

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "No licence number in PL format, dosage form or indication text was available, so the UK licensed indications should be confirmed against the" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

