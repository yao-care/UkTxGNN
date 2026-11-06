---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-06
description: "Disopyramide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the UK authorisation data (the drug is a Class Ia antia…"
monitor_inn: "Disopyramide"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
---

# Disopyramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome
{: .text-alpha }

## One-Sentence Summary

Disopyramide is a Class Ia antiarrhythmic drug, and the UK authorisation data compiled for this report does not state its approved indication text.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but **no clinical trials and no publications** currently support this prediction.
This is a model-only signal with no supporting evidence, and it should be treated as a hypothesis rather than a repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation data (the drug is a Class Ia antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (19 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled sources. Based on known pharmacology, disopyramide is a Class Ia antiarrhythmic that blocks sodium channels and has anticholinergic activity.

Tourette syndrome is thought to arise from dysfunction in dopaminergic and cortico-striatal-thalamo-cortical circuits. Sodium channel blockade and anticholinergic effects are not recognised therapeutic mechanisms in this condition, so **no mechanistic link is established**. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of efficacy.

The same applies to the other top-ranked predictions. These include ADHD (and its inattentive subtype), trichotillomania, faciodigitogenital syndrome, specific developmental disorder, chondromyxoid fibroma and trigeminal nerve neoplasm. All were reviewed, none has any supporting trial or publication, and the data provide no plausible pharmacological rationale for any of them.

Two lower-ranked predictions are arrhythmias, which are biologically closer to the drug's known use. These are idiopathic neonatal atrial flutter (rank 7) and multifocal atrial tachycardia (rank 9). Both are still only indirectly supported by class pharmacology. Neonatal use raises major safety concerns, and multifocal atrial tachycardia is usually managed by treating the underlying lung disease, or with calcium channel blockers or beta-blockers, rather than Class Ia agents.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Tourette syndrome.

For context, the only publication retrieved across all top-10 predictions relates to multifocal atrial tachycardia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7418495](https://pubmed.ncbi.nlm.nih.gov/7418495/) | 1980 | Cohort / case report | Chest | Describes lorcainide for resistant ventricular arrhythmias in a patient whose arrhythmias had not responded to quinidine, procainamide, disopyramide, propranolol or digoxin. It does not study disopyramide as a treatment and does not address Tourette syndrome. |

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0203020F0AAABAB | Disopyramide 100mg capsules | Disopyramide |
| 0203020F0AAAVAV | Disopyramide 100mg/5ml oral liquid | Disopyramide |
| 0203020F0AAACAC | Disopyramide 150mg capsules | Disopyramide |
| 0203020G0AAAEAE | Disopyramide 150mg modified-release tablets | Disopyramide phosphate |
| 0203020F0AAASAS | Disopyramide 16mg/5ml oral liquid | Disopyramide |
| 0203020F0AAAWAW | Disopyramide 20mg/5ml oral liquid | Disopyramide |
| 0203020G0AAABAB | Disopyramide 250mg modified-release capsules | Disopyramide phosphate |
| 0203020G0AAACAC | Disopyramide 250mg modified-release tablets | Disopyramide phosphate |
| 0203020F0AAAPAP | Disopyramide 25mg capsules | Disopyramide |
| 0203020F0AAAXAX | Disopyramide 25mg/5ml oral liquid | Disopyramide |
| 0203020F0AAARAR | Disopyramide 50mg/5ml oral liquid | Disopyramide |
| 0203020G0AAAFAF | Disopyramide 50mg/5ml solution for injection ampoules | Disopyramide phosphate |
| 0203020G0BCABAE | Dirythmin SA 150mg tablets | Disopyramide phosphate |
| 0203020G0BBAAAB | Isomide CR 250mg capsules | Disopyramide phosphate |
| 0203020F0BCAAAB | Rythmodan 100mg capsules | Disopyramide |
| 0203020F0BCACAB | Rythmodan 100mg capsules (Imported Canada) | Disopyramide |
| 0203020F0BCABAC | Rythmodan 150mg capsules | Disopyramide |
| 0203020G0BDAAAF | Rythmodan 50mg/5ml solution for injection ampoules | Disopyramide phosphate |
| 0203020G0BDABAC | Rythmodan Retard 250mg tablets | Disopyramide phosphate |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

The BNF classification code (0203020F0) falls within the cardiovascular system, antiarrhythmic drugs chapter. The compiled data do not include a PL number, manufacturer or indication text. The record should be checked against the MHRA product information.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease contraindication links, not label text): long QT syndrome (including familial), atrioventricular block, cardiomyopathy (including hypertrophic), myocarditis, atrial fibrillation and flutter, hypotensive disorder, kidney disease, liver disease, gallbladder disease, potassium deficiency, benign prostatic hyperplasia, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, and hypoglycaemia.
- **Drug Interactions** (100 interactions recorded; examples shown):
  - **Major:** potassium citrate, clarithromycin, picosulfuric acid.
  - **Moderate:** antimuscarinic agents (atropine, hyoscyamine, glycopyrronium, clidinium), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), amphotericin B, loperamide, aprepitant, famotidine and chlorpropamide.
  - **Minor:** cimetidine.
- **Population concern:** the anticholinergic, negative inotropic and proarrhythmic effects are particularly worrying in children and neonates, who make up the typical Tourette syndrome and ADHD populations.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence, with no trials, no literature, no plausible mechanism and a safety profile that is unfavourable for the likely patient population.

**To proceed, the following is needed:**
- Mechanism of action data for disopyramide, to allow a proper mechanistic assessment
- The approved indication text and PL number from the MHRA record
- Full SmPC warnings and contraindications to complete safety screening
- Any preclinical or clinical evidence linking disopyramide to Tourette syndrome
- If an arrhythmia-related direction is explored instead, a focused literature review of disopyramide in atrial flutter and multifocal atrial tachycardia, with a specific neonatal safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

