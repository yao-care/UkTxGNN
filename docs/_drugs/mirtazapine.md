---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 419
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Mirtazapine: predicted new indication Ohdo syndrome and variants (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
---

# Mirtazapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Mirtazapine: From Major Depressive Disorder to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is an antidepressant, originally used for depressive disorders and anxiety disorder.
The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (the UK authorisation record has no indication text) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mirtazapine is generally known as a noradrenergic and specific serotonergic antidepressant, acting through alpha-2 adrenergic, 5-HT2/5-HT3 and H1 receptor antagonism. Its efficacy in depression is established, but that does not extend to the predicted condition.

Ohdo syndrome (including the KAT6B-related variants) is a rare genetic disorder of chromatin regulation, with intellectual disability and craniofacial features. No plausible pharmacological pathway links monoaminergic modulation to this underlying epigenetic defect. The high TxGNN score most likely reflects network proximity or shared phenotype nodes in the knowledge graph rather than true biology, so the prediction should be treated with caution.

Two other predictions were also generated:
- **Blepharophimosis - intellectual disability syndrome, Ohdo type** (score 99.11%): a subtype of the same spectrum, likely redundant with the prediction above and driven by the same graph artefact. At most, mirtazapine could offer symptomatic help for comorbid mood or sleep problems, which is not a disease-modifying rationale.
- **Benign paroxysmal torticollis of infancy** (score 99.11%): a weak, speculative link exists, as the condition is related to CACNA1A variants and is considered a migraine equivalent, and serotonergic agents are sometimes used in migraine prophylaxis. There is no direct evidence for mirtazapine, and its use in infants is a concern because it is not approved for paediatric use and carries a warning about suicidality in young patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0403040X0AAAAAA | Mirtazapine Tab 30mg | Not recorded | Not recorded |

This is the only authorisation record in the compiled data. The identifier does not follow the usual MHRA PL number format, so it should be checked against the MHRA register. Please refer to the BNF (antidepressant drugs) and the current SmPC for licensed indications.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindications or cautions** (from knowledge-graph relationships, not from product label text): epilepsy, manic bipolar affective disorder, liver disease, impaired renal function, neutropenia, agranulocytosis, serotonin syndrome, drug-induced akathisia, orthostatic hypotension and other hypotensive disorders, multiple system atrophy, postural orthostatic tachycardia syndrome, myocardial infarction and coronary thrombosis, stroke and other cerebrovascular disorders, cerebral infarction, hypertriglyceridemia, obesity disorders, gallbladder disease and haemoglobinopathy.
- **Drug Interactions**: 100 interactions were recorded; the most clinically important are those classed as **Major**:
  - Bupropion
  - Lorcaserin
  - Dolasetron
  - Palonosetron

  Moderate interactions include famotidine, loperamide, aprepitant, morphine, dexamethasone, cimetidine, clarithromycin, levofloxacin, dronabinol, nabilone, eliglustat and obeticholic acid, among others.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. There are no clinical trials or publications, and no plausible mechanistic link between mirtazapine's receptor pharmacology and the underlying chromatin-regulation defect in Ohdo syndrome.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic analysis
- Label-based warnings and contraindications from the SmPC and BNF
- Confirmed MHRA marketing authorisation details (PL number, dosage form, approved indication)
- Any preclinical or clinical evidence in Ohdo syndrome, or in the related migraine-equivalent condition if that prediction is pursued
- A paediatric safety assessment, given the likely patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

