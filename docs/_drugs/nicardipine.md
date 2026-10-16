---
layout: default
title: Nicardipine
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Nicardipine: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
---

# Nicardipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Nicardipine: From Hypertension to Pulmonary Hypertension (Multifactorial Mechanism)

## One-Sentence Summary

Nicardipine is a dihydropyridine calcium channel blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but there are currently **no registered clinical trials** and **no directly supporting publications** for this specific indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on drug class, nicardipine is a dihydropyridine calcium channel blocker. It relaxes vascular smooth muscle and causes vasodilation, and its efficacy in systemic hypertension is established.

Pulmonary hypertension involves raised pressure in the pulmonary arteries, and pulmonary vascular tone is partly calcium-dependent. This gives a plausible but unverified link between systemic vasodilation and pulmonary vasodilation.

There is an important caution. Calcium channel blockers can inhibit hypoxic pulmonary vasoconstriction, which may worsen ventilation-perfusion matching and gas exchange. This needs careful evaluation before any clinical use in this setting. The one directly relevant publication identified concerns nicardipine and regional hypoxic pulmonary vasoconstriction in dogs (see below), which is not evidence of benefit in patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was identified for the top-ranked predicted indication. The table below lists the most relevant publications retrieved for the related predicted indication, pulmonary hypertension owing to lung disease and/or hypoxia (rank 2). Only the first is directly about nicardipine and the pulmonary circulation; the others are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3132192](https://pubmed.ncbi.nlm.nih.gov/3132192/) | 1988 | Preclinical/physiological study | Br J Anaesth | Effect of nicardipine on regional hypoxic pulmonary vasoconstriction in 14 open-chest dogs, including a group with controlled cardiac output |
| [19035721](https://pubmed.ncbi.nlm.nih.gov/19035721/) | 2008 | Clinical study | J Neurosurg | IV nicardipine in hypertensive emergencies in acute brain disease and its effect on brain tissue oxygen; systemic, not pulmonary, hypertension |
| [2693295](https://pubmed.ncbi.nlm.nih.gov/2693295/) | 1989 | Review | Fundam Clin Pharmacol | Neuropharmacology of calcium antagonists in cerebral ischaemia, vasospasm and hypoxia |
| [1735870](https://pubmed.ncbi.nlm.nih.gov/1735870/) | 1992 | Review | J Post Anesth Nurs | Acute postoperative hypertension in hypertensive patients; systemic, not pulmonary |
| [14751848](https://pubmed.ncbi.nlm.nih.gov/14751848/) | 2004 | Preclinical | Am J Physiol Lung Cell Mol Physiol | 5-HT-induced calcium influx in rat small intrapulmonary artery; background on pulmonary vasoconstriction mechanisms |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206020Q0AAAAAA | Nicardipine HCl capsule 20 mg | Capsule | Not stated in the data compiled for this report |

The reference code above appears to be a BNF-style product code rather than a standard PL number. Dosage form and approved indication details were not available. Please check the current MHRA listing, SmPC and BNF.

## Safety Considerations

- **Contraindications and disease associations (from knowledge-graph data, not label text):** liver disease, gallbladder disease, hypotensive disorder, impaired renal function, intracerebral haemorrhage, cerebral infarction, ischaemic stroke susceptibility, cerebrovascular disorder, cerebral artery occlusion and brain stem infarction. Verify against the SmPC.
- **Drug Interactions:** 100 interactions were identified in total. The only one listed as **Major** among those reviewed was **dolasetron**. Examples of **Moderate** interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Other drugs: bupropion, aprepitant, morphine, acetylsalicylic acid, cimetidine, miconazole, magnesium sulfate
  - Calcium salts: calcium phosphate, calcium acetate
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
  - Cannabinoids: dronabinol, nabilone
- **Specific concern for this indication:** possible worsening of gas exchange through inhibition of hypoxic pulmonary vasoconstriction.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials and no directly supportive human evidence for this indication (evidence level L5). The only pulmonary-specific paper is an animal study, and there is a recognised risk of impaired gas exchange.

**To proceed, the following is needed:**
- Mechanism of action data for nicardipine
- UK label information (SmPC warnings, contraindications, approved indication, dosage form) to complete safety screening
- Systematic literature review of calcium channel blockers in pulmonary hypertension, with attention to disease subgroup and vasoreactivity
- Preclinical and early clinical data on pulmonary haemodynamics and oxygenation
- Clarification of the disease definition used in the prediction
- Note: other predicted indications (malignant renovascular hypertension, malignant hypertensive renal disease) largely overlap with the existing hypertension indication and offer limited repurposing novelty. Braddock syndrome has no identifiable mechanistic rationale and needs manual curation of its disease definition.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

