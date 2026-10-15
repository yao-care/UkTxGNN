---
layout: default
title: Betaxolol
parent: Model Prediction Only (L5)
nav_order: 102
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

# Betaxolol: From Open-Angle Glaucoma and Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a beta-1 selective adrenergic blocker, originally used for hypertension, open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but at present there are **no registered clinical trials** and **no publications** supporting this specific direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (hypertension is also listed as an original indication) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, betaxolol is a beta-1 selective adrenergic antagonist. In the eye, it lowers intraocular pressure (IOP) by reducing aqueous humour production. Its efficacy in open-angle glaucoma and ocular hypertension is established, and mechanistically it may be applicable to primary hereditary glaucoma.

Hereditary forms of glaucoma, such as primary congenital glaucoma or MYOC/CYP1B1-related glaucoma, share raised IOP as the downstream pathology. An IOP-lowering drug is therefore plausible in this setting. However, no link between betaxolol and the genetic causes of hereditary glaucoma can be established from the available data.

The high TxGNN score (0.997) is a model prediction only. It likely reflects the closeness of hereditary glaucoma to the existing glaucoma indications in the knowledge graph rather than independent evidence.

Age is also a consideration. Hereditary glaucoma often presents in infancy, and topical beta-blockers carry paediatric safety concerns, including bradycardia and bronchospasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000I0AAAAAA | Betaxolol eye drops 0.5% (solution) | Eye drops, solution | Not stated in the data compiled |

The data compiled for this report list one valid single-ingredient authorisation. The authorisation number is not in the standard MHRA "PL" format, and the dosage form, manufacturer and approved indication text are not recorded. Please verify these details against the MHRA register and the BNF.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug–disease links in the TxGNN knowledge graph, not from product label text, and should be checked against the SmPC):

- **Respiratory:** asthma (including intrinsic and allergic asthma), pulmonary emphysema, bronchial disease
- **Cardiac:** atrioventricular block and atrioventricular dissociation
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hypoglycaemia, phaeochromocytoma and related adrenal or paraganglionic tumours
- **Neuromuscular:** myasthenia gravis and other neuromuscular junction disease
- **Organ disease:** kidney disease, liver disease, gallbladder disease
- **Skin:** psoriasis, parapsoriasis
- **Psychiatric:** anxiety disorder, neurotic disorder, dysthymic disorder
- **Other listed conditions:** pyoureter, and cancers of the duodenum, small intestine and heart

**Drug interactions:** the interaction screen returned 100 interacting drugs, of which 20 are shown in the data compiled. Most are rated Moderate, and a few are Minor.

- **Moderate:** epinephrine, morphine, bupropion, atropine, hyoscyamine, acetohexamide, and the corticosteroids hydrocortisone, dexamethasone, betamethasone, triamcinolone and budesonide. Several calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate) are also rated Moderate.
- **Minor:** acetylsalicylic acid, aluminium hydroxide, attapulgite.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no trials or publications for primary hereditary glaucoma. Mechanism data and label-based safety information are also missing, and paediatric safety is a particular concern in this population.

**To proceed, the following is needed:**
- Mechanism of action data for betaxolol and its relevance to hereditary glaucoma
- Label-based warnings and contraindications from the SmPC and BNF, to replace the knowledge-graph-derived list
- Full MHRA authorisation details (PL number, dosage form, approved indication)
- Literature and trial searches for betaxolol in primary congenital and other hereditary glaucomas
- A paediatric safety assessment (bradycardia, bronchospasm) for topical beta-blocker use in infants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

