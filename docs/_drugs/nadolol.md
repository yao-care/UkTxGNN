---
layout: default
title: Nadolol
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Nadolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Nadolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Nadolol
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

## Nadolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Nadolol is a non-selective beta-blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **no clinical trials** and **no publications** specific to this condition, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, nadolol is a non-selective beta-blocker. Its efficacy in hypertension is established, and beta-blockade reduces renin release and blood pressure, which may be relevant to hypertensive renal disease.

The predicted indication is closely related to the original one. The high score (0.9959) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than an independent repurposing signal. In practice, malignant hypertension is a hypertensive emergency usually managed with intravenous agents, so oral nadolol is unlikely to be first-line.

Other predictions in the same list were assessed in the same way:

- **Pulmonary hypertension with unclear multifactorial mechanism** (score 0.9953, L5): no trials or literature. Beta-blockers have historically been avoided in pulmonary arterial hypertension because of concerns about cardiac output and right ventricular function.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 0.9953, L4): 12 publications were returned, but all are preclinical or indirect (see Literature Evidence). Beta-blockade may worsen outcomes in patients with COPD.
- **Braddock syndrome** (score 0.9943, L5): no plausible mechanistic rationale is evident, and the signal is probably a network-connectivity artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top-ranked prediction (malignant hypertensive renal disease). For the fourth-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia, the following publications were returned. None is a nadolol-specific clinical study in patients.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6488695](https://pubmed.ncbi.nlm.nih.gov/6488695/) | 1984 | Animal study | Clin Physiol Biochem | Chronic propranolol lowered pulmonary artery pressure in conscious dogs; nadolol, a structurally dissimilar beta-blocker, produced a similar decrease in total pulmonary resistance |
| [2566504](https://pubmed.ncbi.nlm.nih.gov/2566504/) | 1989 | Preclinical/Review | Eur J Pharmacol | Beta-blockers of various profiles showed cardioprotective effects in a guinea pig heart model of anoxia |
| [8729060](https://pubmed.ncbi.nlm.nih.gov/8729060/) | 1996 | Preclinical | J Mol Cell Cardiol | Catecholamine-mediated chloride currents and early action potential shortening in hypoxic rabbit hearts; nadolol used as a tool |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Animal study | PLoS One | β2-adrenergic receptor-dependent attenuation of hypoxic pulmonary vasoconstriction in intermittent hypoxic rats |
| [24795691](https://pubmed.ncbi.nlm.nih.gov/24795691/) | 2014 | Preclinical | Front Neurol | β1-blockers lowered norepinephrine release in normotensive and hypertensive rats |
| [39252618](https://pubmed.ncbi.nlm.nih.gov/39252618/) | 2025 | Preclinical | CNS Neurol Disord Drug Targets | Nadolol attenuated brain cell ferroptosis in ischaemic stroke rats via the HOIL-1/IRP2 pathway |

The remaining records (PMIDs 8935706, 1913717, 31527180, 1670627, 11076740, 10684471) are animal or isolated-tissue studies of hypoxia, ischaemia and catecholamines in the heart, with little relevance to this indication.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0204000M0AAABAB | Nadolol Tab 80mg | Tablet (not specified in the data) | Not specified in the data |

The data compiled for this report list one valid single-ingredient authorisation. The identifier shown is not in the usual MHRA PL format, so the authorisation details should be verified against the MHRA register and the BNF (beta-blocker section).

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (not label text; to be confirmed against the SmPC):
- Cardiorespiratory: atrioventricular block, pulmonary emphysema, bronchial disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, hyperparathyroidism, gout, hyperuricaemia, phosphorus metabolism disease
- Renal and hepatic: kidney disease, anuria, liver disease, hepatic coma and encephalopathy, pancreatitis, gallbladder disease, nephrocalcinosis
- Neuromuscular: myasthenia gravis, neuromuscular junction disease
- Other: systemic lupus erythematosus, anxiety and neurotic disorders, dysthymic disorder, neonatal jaundice

**Drug Interactions** (100 interactions recorded; selected examples):
- **Major:** epinephrine
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, cimetidine, SGLT2 inhibitors (canagliflozin, dapagliflozin), chlorpropamide, calcium salts
- **Minor:** acetylsalicylic acid, clarithromycin, magnesium oxide

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF, and report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is an extension of nadolol's existing hypertension indication, with a high model score but no clinical trials or publications for malignant hypertensive renal disease. Oral nadolol is unlikely to be suitable for a hypertensive emergency, and the other predicted indications show no supportive evidence or raise safety concerns.

**To proceed, the following is needed:**
- Mechanism of action data and SmPC-based warnings and contraindications
- Clinical evidence specific to hypertensive renal disease or renovascular hypertension
- Clarification of the UK authorisation details (PL number, dosage form, approved indication)
- Review of the safety signals (renal disease, bronchial disease, atrioventricular block, diabetes) for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

