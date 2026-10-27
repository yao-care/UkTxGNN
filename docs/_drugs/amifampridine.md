---
layout: default
title: Amifampridine
parent: Model Prediction Only (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amifampridine: predicted new indication Glaucoma (evidence level L5). Approved use: Lambert-Eaton myasthenic syndrome"
monitor_inn: "Amifampridine"
predicted_indications: ["glaucoma", "acute intermittent porphyria", "esophageal varices without bleeding", "esophageal varices with bleeding", "porphyria", "primary immunodeficiency syndrome due to p14 deficiency", "paraneoplastic limbic encephalitis", "paraneoplastic polyneuropathy", "varicose disease", "paraneoplastic cerebellar degeneration"]
---

# Amifampridine
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

## Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma
{: .text-alpha }

## One-Sentence Summary

Amifampridine was originally used to treat Lambert-Eaton myasthenic syndrome (LEMS).
The TxGNN model predicts it may be effective for **glaucoma**, but there are currently **no registered clinical trials and no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lambert-Eaton myasthenic syndrome |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Amifampridine (3,4-diaminopyridine) is a voltage-gated potassium channel blocker. By prolonging presynaptic depolarisation, it enhances acetylcholine release at the neuromuscular junction, which is why it helps people with LEMS. The data compiled for this report do not include a formal mechanism-of-action entry, so this description draws on general pharmacological knowledge.

Currently, there is no established link between this mechanism and the regulation of intraocular pressure or neuroprotection of retinal ganglion cells. The high TxGNN score is a graph-based prediction only. It should be read as a hypothesis-generating signal, not as evidence of benefit. Of the top ten predictions, the more mechanistically coherent ones are actually paraneoplastic polyneuropathy and paraneoplastic cerebellar degeneration, which sit close to LEMS in the paraneoplastic spectrum. These are flagged as research questions, but they also have no retrieved clinical evidence.

## Other Predicted Indications (Top 10)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Glaucoma | 99.71% | L5 | Hold; no mechanistic link |
| 2 | Acute intermittent porphyria | 99.32% | L5 | Hold; seizure-risk concern |
| 3 | Oesophageal varices without bleeding | 98.77% | L5 | Hold; likely graph artefact |
| 4 | Oesophageal varices with bleeding | 98.77% | L5 | Hold; no supporting data |
| 5 | Porphyria | 98.51% | L5 | Hold; seizure-risk concern |
| 6 | Primary immunodeficiency due to p14 deficiency | 98.39% | L5 | Hold; no recognised pathway link |
| 7 | Paraneoplastic limbic encephalitis | 98.31% | L5 | Hold; seizure-threshold concern |
| 8 | Paraneoplastic polyneuropathy | 98.26% | L5 | Research question |
| 9 | Varicose disease | 98.08% | L5 | Hold; likely graph artefact |
| 10 | Paraneoplastic cerebellar degeneration | 97.99% | L5 | Research question |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 100201000AAADAD | Amifampridine Tab 10mg | Not specified | Not specified |

The compiled data list one valid single-ingredient authorisation. The dosage form, manufacturer and approved indication text were not available, and the authorisation number is not in the usual MHRA PL format. Please verify details against the MHRA register and the BNF.

## Safety Considerations

- **Drug Interactions**: The interaction screen identified 68 interacting drugs. The 20 entries shown include one rated Major and the rest Moderate.
  - **Major**: bupropion.
  - **Moderate (examples)**: corticosteroids (hydrocortisone, betamethasone, dexamethasone, prednisolone, prednisone); sympathomimetics and appetite suppressants (ephedrine, phentermine, fenfluramine, dexfenfluramine, diethylpropion, mazindol, sibutramine); levofloxacin; metoclopramide; opioids (morphine, opium); dronabinol; and polyethylene glycol with electrolytes.
- **Seizure threshold**: Amifampridine lowers the seizure threshold. This is a particular concern for the porphyria and paraneoplastic limbic encephalitis predictions, where seizures can occur. Several of the interacting drugs above (such as bupropion and levofloxacin) also lower the seizure threshold.

Label-based warnings and contraindications were not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction is supported only by a model score, with no trials, no publications and no plausible mechanistic link to intraocular pressure or retinal neuroprotection. Seizure-threshold lowering adds a safety concern in several of the other predicted conditions.

**To proceed, the following is needed:**
- Targeted literature review for the predicted indication, and for paraneoplastic polyneuropathy and paraneoplastic cerebellar degeneration, which are the more plausible research questions
- Mechanism-of-action data and a defined mechanistic hypothesis linking potassium channel blockade to glaucoma
- Label warnings and contraindications from the SmPC and BNF, to allow a proper safety screen
- Preclinical evidence (for example, ocular models) before any clinical development
- Confirmation of the UK authorisation details (dosage form, indication, PL number) from the MHRA register
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

