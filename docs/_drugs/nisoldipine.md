---
layout: default
title: Nisoldipine
parent: Model Prediction Only (L5)
nav_order: 447
evidence_level: L5
indication_count: 4
monitor_inn: "Nisoldipine"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-30
description: "Nisoldipine: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension"
---

# Nisoldipine
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

## Nisoldipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism
{: .text-alpha }

## One-Sentence Summary

Nisoldipine is a dihydropyridine calcium channel blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, but this is a computational prediction only, with **no clinical trials** and **no publications** that directly study this disease. A related prediction, pulmonary hypertension owing to lung disease and/or hypoxia, has 18 retrieved publications, all preclinical or mechanistic.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (relation recorded in the knowledge graph; no licence indication text is available for the UK product) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nisoldipine is a dihydropyridine L-type calcium channel blocker. It causes vasodilation and lowers blood pressure in hypertension. Mechanistically, relaxation of pulmonary vascular smooth muscle could be relevant to pulmonary hypertension.

This link is theoretical. No trials or publications addressing this exact predicted disease were found, and the high TxGNN score is a model output rather than validated evidence.

Other predictions in the list:
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 0.9977): hypoxic pulmonary vasoconstriction depends partly on calcium channel activity and intracellular calcium release. The evidence is preclinical only (see below). Calcium channel blockers have shown limited and inconsistent benefit in hypoxic pulmonary hypertension, and may worsen gas exchange by blunting protective hypoxic vasoconstriction in well-ventilated lung regions.
- **Malignant hypertensive renal disease** (score 0.9975): largely an extension of the existing hypertension use. Malignant hypertension is an emergency usually managed with titratable intravenous agents, and no supporting studies were found.
- **Braddock syndrome** (score 0.9968): no mechanistic rationale can be established from the data. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications were found for the top-ranked indication. The table below shows the most relevant publications retrieved for the related prediction, pulmonary hypertension owing to lung disease and/or hypoxia. All are animal, in vitro or mechanistic studies, and none studies humans with the predicted disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3872360](https://pubmed.ncbi.nlm.nih.gov/3872360/) | 1985 | Animal study | J Pharmacol Exp Ther | Compared nisoldipine, nifedipine and bepridil on experimental pulmonary hypertension in anaesthetised dogs |
| [2476607](https://pubmed.ncbi.nlm.nih.gov/2476607/) | 1989 | Animal study | J Cardiovasc Pharmacol | Calcium antagonists (including nisoldipine) and other drugs tested on the hypoxia-induced rise in rat right ventricular pressure |
| [9298524](https://pubmed.ncbi.nlm.nih.gov/9298524/) | 1997 | Preclinical mechanistic | Br J Pharmacol | Intracellular calcium release plays a prominent role in hypoxic vasoconstriction of canine pulmonary artery |
| [1566816](https://pubmed.ncbi.nlm.nih.gov/1566816/) | 1992 | Preclinical mechanistic | Am J Physiol | Potassium channel inhibition contributes directly to hypoxic pulmonary vasoconstriction |
| [15613369](https://pubmed.ncbi.nlm.nih.gov/15613369/) | 2005 | Preclinical mechanistic | J Physiol | Hypoxia mobilises sarcoplasmic reticulum stores, activating capacitative calcium entry in canine pulmonary arterial smooth muscle cells |
| [15528240](https://pubmed.ncbi.nlm.nih.gov/15528240/) | 2005 | Preclinical mechanistic | J Physiol | Voltage-dependent calcium channels, including nisoldipine-sensitive L-type channels, in rabbit carotid body chemoreceptor cells |
| [10980033](https://pubmed.ncbi.nlm.nih.gov/10980033/) | 2000 | Preclinical mechanistic | J Neurophysiol | Hypoxia augments L-type calcium current in rabbit carotid body glomus cells |
| [10630745](https://pubmed.ncbi.nlm.nih.gov/10630745/) | 2000 | Animal study | J Cardiovasc Pharmacol | Nifedipine and nisoldipine compared on coronary vasoconstriction in rat hearts (coronary, not pulmonary) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0206020W0AAABAB | Nisoldipine tablets 20 mg modified-release | Modified-release tablet | Not stated in the data compiled for this report |

This record lists one single-ingredient product. The BNF classification code embedded in the identifier suggests the cardiovascular calcium channel blocker section, but no approved indication text is available here.

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver failure, hypotensive disorder, coronary artery disease, coronary atherosclerosis, arteriosclerosis disorder, atherosclerosis. These should be checked against the SmPC.
- **Drug Interactions:** 100 interactions were recorded. Examples:
  - **Major:** dolasetron.
  - **Moderate:** cimetidine, aprepitant, bupropion, morphine, acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), magnesium sulfate, dronabinol and nabilone.
  - **Minor:** omeprazole.
- **Additional concern for the hypoxic pulmonary hypertension prediction:** calcium channel blockers may worsen gas exchange by inhibiting hypoxic vasoconstriction in well-ventilated regions.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. No clinical trial or publication directly studies pulmonary hypertension with unclear multifactorial mechanism, so the evidence level is L5. The related hypoxic pulmonary hypertension literature is entirely preclinical, and there is a safety concern with calcium channel blockers in that setting.

**To proceed, the following is needed:**
- Mechanism of action data for nisoldipine
- Licence indication text and SmPC warnings and contraindications for the UK product
- Human clinical studies in the predicted pulmonary hypertension indication
- Clinical review of the benefit-risk balance, including gas exchange effects and the existing contraindications
- Review of the predictions with weak rationale (Braddock syndrome) and of malignant hypertensive renal disease, which is largely an extension of the current hypertension use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

