---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 305
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Formoterol: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Formoterol is a long-acting beta2-adrenergic agonist (LABA) used in inhaled combination products for obstructive airway disease, with original indications of pulmonary emphysema and asthma.
The TxGNN model predicts it may be effective for **respiratory malformation**, but there are **no clinical trials** and **no publications directly addressing this condition**, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Formoterol is a long-acting beta2-agonist, and this class relaxes airway smooth muscle to produce bronchodilation. Its efficacy in asthma and COPD-related disease is well established.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a specific link between formoterol and respiratory disease. Respiratory malformation is a structural, congenital problem. Bronchodilation would not be expected to correct it or modify the disease, so no plausible disease-modifying mechanism is evident.

At best, formoterol might relieve secondary airflow obstruction or wheeze in affected patients. Nothing in the compiled data tests or supports even that.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Nine publications were retrieved. None addresses respiratory malformation. They concern asthma, COPD and unrelated topics, so they offer only background on formoterol.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Systematic review / meta-analysis | J Am Pharm Assoc | Safety and efficacy of budesonide/glycopyrrolate/formoterol versus glycopyrrolate/formoterol in COPD |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT | Eur Respir J | Repeated-dose budesonide/formoterol compared with salbutamol in adult asthma (crossover trial) |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Long-term safety and asthma control with budesonide/formoterol in African American patients |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | RCT | Eur Respir J | Formoterol protected against platelet-activating factor-induced effects in asthma |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | Budesonide/formoterol pMDI for persistent asthma: efficacy and safety overview |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Review | Prog Neuropsychopharmacol Biol Psychiatry | Neurotransmitter-based strategies for cognitive dysfunction in Down syndrome (not relevant to formoterol in respiratory malformation) |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Physiological study | Eur J Appl Physiol | Compensatory responses to increased mechanical load in COPD during sleep |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | Small airway disease in a patient with long COVID |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Case report | Medicine | Allergic bronchopulmonary mycosis in a postoperative lung cancer patient |

---

## UK Market Information

Two valid single-ingredient formoterol-containing authorisations are recorded. Dosage form and approved indication text were not available for either.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0302000N0AABLBL | Fluticasone/Formoterol inhaler 50/5 mcg, 120 doses | Inhaler (not specified) | Not stated |
| 0302000C0AABXBX | Beclometasone dipropionate/Formoterol inhaler 100/6 mcg, 120 doses | Inhaler (not specified) | Not stated |

Both products fall within the BNF respiratory system chapter (inhaled corticosteroid with long-acting beta2 agonist combinations). Neither has an authorised indication for respiratory malformation.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from the TxGNN knowledge graph, not from product label text, so they should be checked against the SmPC): the main clinically relevant conditions flagged are hypertensive disorder/hypertension, long QT syndrome (including familial), epilepsy, liver disease and gallbladder disease. Measles, herpes simplex keratitis and a large group of pituitary and growth hormone deficiency-related disorders (for example hypopituitarism, Kallmann syndrome, Sheehan syndrome) are also flagged.
- **Drug Interactions**: 463 interactions were identified. Examples rated Moderate include:
  - Antidiabetic agents (acarbose, alogliptin, albiglutide, dulaglutide, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide).
  - Agents with QT-prolongation relevance (cisapride, clarithromycin, dolasetron).
  - Sympathomimetics (ephedrine, isometheptene, diethylpropion).
  - Famotidine.

  Corticosteroids (beclometasone, betamethasone, budesonide, dexamethasone) are rated Minor.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score for respiratory malformation is a computational prediction with no registered trials, no directly relevant literature and no plausible mechanism, since a structural malformation is not expected to respond to bronchodilation.

Other predictions in the same analysis have far more evidence, but they are largely existing uses of formoterol. Obstructive lung disease and asthma reach L1 and "Proceed with Guardrails", but they are confirmations of established indications rather than new repurposing. Bronchitis reaches L2 only through indirect COPD evidence.

**To proceed, the following is needed:**
- A defined clinical rationale for a specific respiratory malformation phenotype, such as secondary airway obstruction or wheeze that could benefit from bronchodilation.
- Any clinical or preclinical evidence in this population. None is currently available.
- Detailed mechanism of action data for formoterol.
- Authorised indication text and dosage forms for the UK authorisations.
- Review of the SmPC for contraindications and warnings, particularly cardiovascular and QT-related risks.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

