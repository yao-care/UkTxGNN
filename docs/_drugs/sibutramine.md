---
layout: default
title: Sibutramine
parent: Model Prediction Only (L5)
nav_order: 568
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Sibutramine: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
---

# Sibutramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Sibutramine: From Obesity to Hypervitaminosis

## One-Sentence Summary

Sibutramine was originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are **no clinical trials and no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the UK authorisation record has no approved indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Marketed (per the data compiled for this report) |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sibutramine is a serotonin-noradrenaline reuptake inhibitor (SNRI) that was used for appetite suppression, and its use in obesity is its established role.

No plausible mechanistic link to hypervitaminosis has been identified. Hypervitaminosis results from excess vitamin intake and is managed by stopping the offending supplement and providing supportive care. An appetite suppressant has no obvious role in this process. The high score (99.98%) is a graph-based prediction with no clinical or literature support, and it probably reflects associations within the knowledge graph rather than a real pharmacological rationale.

Other predictions for this drug are equally weak. The proximal 16p11.2 microdeletion syndrome prediction (99.98%) most likely reflects the shared obesity phenotype, while the predictions for obsolete hypertelorism (99.97%) and frontorhiny (99.95%) have no plausible pharmacological basis. All four have no trials or publications and are rated L5 with a recommendation to hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0405020S0AAAAAA | Sibutramine Cap 10mg | Capsule (inferred from product name) | Not stated |

This identifier looks like a BNF-style classification code rather than a standard MHRA PL number, and the dosage form, manufacturer and approved indication are blank in the compiled record. The marketed status and the single authorisation should be checked against the MHRA register before any decision relies on them. Sibutramine has been withdrawn in many jurisdictions because of cardiovascular risk.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph-derived associations, not label text). The list includes:
  - Cardiovascular and cerebrovascular: hypertension, coronary artery disease, myocardial infarction, stroke, cerebral infarction, heart conduction disease, sudden cardiac arrest, and cardiovascular and heart disease in general.
  - Renal and hepatic: liver failure, kidney disease, chronic kidney disease.
  - Neurological and psychiatric: epilepsy, anorexia nervosa, bulimia nervosa.
  - Other: diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, angle-closure glaucoma, neuroleptic malignant syndrome, serotonin syndrome.
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Examples of **Major** interactions include:
  - Fentanyl
  - Dextromethorphan
  - Tramadol

  Examples of **Moderate** interactions include:
  - Sympathomimetics: phenylephrine, pseudoephedrine, epinephrine
  - Beta-agonists: salbutamol, formoterol
  - NSAIDs: ibuprofen, ketorolac
  - Antiplatelet agent: abciximab
  - Others: codeine, dihydrocodeine, acetazolamide, acarbose

Label-based warnings and contraindications are not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no publications and no plausible mechanism. The drug carries substantial cardiovascular risk and many interactions, so exploratory use is not justified.

**To proceed, the following is needed:**
- Mechanism of action data and a credible pharmacological rationale linking sibutramine to hypervitaminosis
- A systematic literature search for any supporting evidence
- Label warnings and contraindications (SmPC/BNF), and verification of the UK authorisation and its current regulatory status
- A cardiovascular and interaction risk assessment before any further consideration
- If an obesity-related syndrome such as 16p11.2 microdeletion is of interest, a separate review focused on its obesity component rather than the hypervitaminosis prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

