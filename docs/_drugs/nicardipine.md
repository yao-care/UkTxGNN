---
layout: default
title: Nicardipine
parent: Model Prediction Only (L5)
nav_order: 442
evidence_level: L5
indication_count: 4
monitor_inn: "Nicardipine"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-28
description: "Nicardipine: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertensive disorder and hypertension"
---

# Nicardipine
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

## Nicardipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia
{: .text-alpha }

## One-Sentence Summary

Nicardipine is a dihydropyridine calcium channel blocker, recorded in the knowledge graph for hypertensive disorder and hypertension.
The TxGNN model predicts it may be useful for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but there are currently **no registered clinical trials** and **no publications that directly study this condition in patients**. The only closely related item is one 1988 animal study of hypoxic pulmonary vasoconstriction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder and hypertension (relation recorded in the knowledge graph; no licence indication text available) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, nicardipine is a dihydropyridine L-type calcium channel blocker that relaxes vascular smooth muscle and lowers systemic blood pressure.

Hypoxic pulmonary vasoconstriction depends partly on calcium influx into pulmonary arterial smooth muscle, so a mechanistic link is plausible. One physiological study in dogs (PMID 3132192, 1988) examined nicardipine's effect on regional hypoxic pulmonary vasoconstriction.

There is also a safety concern. Systemic vasodilation by calcium channel blockers can impair ventilation-perfusion matching and worsen oxygenation in hypoxic lung disease. The high TxGNN score is a computational prediction only and is not clinical evidence.

Other predicted indications in the data (pulmonary hypertension with unclear multifactorial mechanism, malignant hypertensive renal disease, Braddock syndrome) have no retrieved trials or literature. Malignant hypertensive renal disease is most likely an extension of the existing hypertension use rather than a true new indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved publications studies nicardipine in patients with pulmonary hypertension owing to lung disease or hypoxia. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3132192](https://pubmed.ncbi.nlm.nih.gov/3132192/) | 1988 | Physiological/preclinical (dogs) | Br J Anaesth | Effect of nicardipine on regional hypoxic pulmonary vasoconstriction in open-chest dogs; higher doses increased cardiac output |
| [19035721](https://pubmed.ncbi.nlm.nih.gov/19035721/) | 2008 | Clinical study | J Neurosurg | IV nicardipine in hypertensive emergencies in acute brain disease and its effect on cerebral oxygenation (not pulmonary hypertension) |
| [2693295](https://pubmed.ncbi.nlm.nih.gov/2693295/) | 1989 | Review | Fundam Clin Pharmacol | Neuropharmacology of calcium antagonists, including use in cerebral ischaemia, vasospasm and hypoxia |
| [3288055](https://pubmed.ncbi.nlm.nih.gov/3288055/) | 1988 | Review | Ann N Y Acad Sci | Pathophysiology of isolated cardiomyocytes (background only) |
| [1735870](https://pubmed.ncbi.nlm.nih.gov/1735870/) | 1992 | Review | J Post Anesth Nurs | Acute postoperative systemic hypertension (indirect) |
| [14751848](https://pubmed.ncbi.nlm.nih.gov/14751848/) | 2004 | Preclinical | Am J Physiol Lung Cell Mol Physiol | 5-HT-induced calcium influx in rat small intrapulmonary artery (mechanistic background) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206020Q0AAAAAA | Nicardipine HCl Cap 20mg | Not stated | Not stated |

This identifier resembles a BNF-style product code (BNF section 2.6.2, calcium-channel blockers) rather than a standard PL number. Please verify it against the MHRA register.

---

## Safety Considerations

- **Contraindications (relations recorded in the knowledge graph, not label text):** liver disease, gallbladder disease, hypotensive disorder, impaired renal function, intracerebral haemorrhage, cerebral infarction, cerebrovascular disorder, cerebral artery occlusion, brain stem infarction.
- **Drug Interactions:** 100 interactions were recorded. Examples:
  - **Major:** dolasetron.
  - **Moderate:** cimetidine, aprepitant, bupropion, morphine, acetylsalicylic acid, miconazole, magnesium sulfate, several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), and SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin).

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or direct patient studies support nicardipine in pulmonary hypertension owing to lung disease or hypoxia. The only related evidence is one animal study, and systemic vasodilation may worsen oxygenation in hypoxic lung disease. The high TxGNN score alone is insufficient.

**To proceed, the following is needed:**
- Mechanism-of-action data and label warnings and contraindications (from the SmPC and BNF)
- Preclinical or early-phase data on pulmonary haemodynamics and gas exchange in hypoxic lung disease
- Assessment of the ventilation-perfusion mismatch risk
- Confirmation of the UK licence details (dosage form, approved indication, authorisation number)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

