---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 419
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Mirtazapine: From Major Depressive Disorder to Ohdo Syndrome and Variants
{: .text-alpha }

## One-Sentence Summary

Mirtazapine is an antidepressant, originally used for depressive disorders and anxiety disorder.
The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (the UK authorisation record has no indication text) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (19 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mirtazapine is generally known as a noradrenergic and specific serotonergic antidepressant, acting through alpha-2 adrenergic, 5-HT2/5-HT3 and H1 receptor antagonism. Its efficacy in depression is established, but that does not extend to the predicted condition.

Ohdo syndrome (including the KAT6B-related variants) is a rare genetic disorder of chromatin regulation, with intellectual disability and craniofacial features. No plausible pharmacological pathway links monoaminergic modulation to this underlying epigenetic defect. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction should be treated with caution.

Two other predictions were also generated:
- **Blepharophimosis - intellectual disability syndrome, Ohdo type** (score 0.9911): a subtype of the same spectrum, likely redundant with the prediction above; the score comes from the TxGNN model (deep learning) and may reflect the same similarities the model learned between related diseases, not biological evidence. At most, mirtazapine could offer symptomatic help for comorbid mood or sleep problems, which is not a disease-modifying rationale.
- **Benign paroxysmal torticollis of infancy** (score 0.9911): a weak, speculative link exists, as the condition is related to CACNA1A variants and is considered a migraine equivalent, and serotonergic agents are sometimes used in migraine prophylaxis. There is no direct evidence for mirtazapine, and its use in infants is a concern because it is not approved for paediatric use and carries a warning about suicidality in young patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0403040X0AAALAL | Mirtazapine 15mg orodispersible tablets | Mirtazapine |
| 0403040X0AAAQAQ | Mirtazapine 15mg orodispersible tablets sugar free | Mirtazapine |
| 0403040X0AAANAN | Mirtazapine 15mg tablets | Mirtazapine |
| 0403040X0AAASAS | Mirtazapine 15mg/5ml oral solution | Mirtazapine |
| 0403040X0AAAGAG | Mirtazapine 15mg/ml oral solution sugar free | Mirtazapine |
| 0403040X0AAAIAI | Mirtazapine 2mg capsules | Mirtazapine |
| 0403040X0AAAJAJ | Mirtazapine 30mg orodispersible tablets | Mirtazapine |
| 0403040X0AAAAAA | Mirtazapine 30mg tablets | Mirtazapine |
| 0403040X0AAABAB | Mirtazapine 30mg/5ml oral liquid | Mirtazapine |
| 0403040X0AAAMAM | Mirtazapine 45mg orodispersible tablets | Mirtazapine |
| 0403040X0AAARAR | Mirtazapine 45mg orodispersible tablets sugar free | Mirtazapine |
| 0403040X0AAAPAP | Mirtazapine 45mg tablets | Mirtazapine |
| 0403040X0AAAHAH | Mirtazapine 4mg capsules | Mirtazapine |
| 0403040X0AAAKAK | Mirtazapine 750micrograms/5ml oral liquid | Mirtazapine |
| 0403040X0AAAFAF | Mirtazapine 75mg/5ml oral suspension | Mirtazapine |
| 0403040X0BBAAAA | Zispin 30mg tablets | Mirtazapine |
| 0403040X0BBACAL | Zispin SolTab 15mg orodispersible tablets | Mirtazapine |
| 0403040X0BBABAJ | Zispin SolTab 30mg orodispersible tablets | Mirtazapine |
| 0403040X0BBADAM | Zispin SolTab 45mg orodispersible tablets | Mirtazapine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier does not follow the usual MHRA PL number format, so it should be checked against the MHRA register. Please refer to the BNF (antidepressant drugs) and the current SmPC for licensed indications.

<!-- review:begin uk-lic-20261106-mirtazapine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "This is the only authorisation record in the compiled data. The identifier does not follow the usual MHRA PL number format, so it should be checked against the MHRA register." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 19 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-mirtazapine-1 -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "This is the only authorisation record in the compiled data" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

