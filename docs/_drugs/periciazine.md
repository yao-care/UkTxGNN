---
layout: default
title: Periciazine
parent: Model Prediction Only (L5)
nav_order: 485
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Periciazine: predicted new indication Migraine disorder (evidence level L5). Approved use: Schizophrenia and other psychoses"
monitor_inn: "periciazine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "dysthymic disorder", "migraine with or without aura, susceptibility to", "ulerythema ophryogenesis"]
---

# Periciazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Periciazine: From Psychotic Disorders to Migraine Disorder

## One-Sentence Summary

Periciazine is a phenothiazine antipsychotic, used in the UK for schizophrenia and other psychoses, and for short-term adjunctive management of severe anxiety, psychomotor agitation and violent or dangerously impulsive behaviour.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no clinical trials** and **no publications** for periciazine in this indication, so the prediction rests on model output and class-level reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and other psychoses; short-term adjunctive management of severe anxiety, psychomotor agitation and violent or dangerously impulsive behaviour (the licence records compiled for this report contain no indication text, so this is taken from pharmacology data) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for periciazine. Based on known pharmacology, it is a phenothiazine antipsychotic with dopamine D2 antagonism, plus antihistaminic, anticholinergic and alpha-adrenergic blocking activity. The data compiled for this report also list the dopamine D1 receptor (DRD1) as a target, although a primary molecular target has not been confirmed in peer-reviewed data.

Other phenothiazines, such as chlorpromazine and prochlorperazine, are used for acute migraine and migraine-associated nausea. This gives a class-level rationale for dopamine antagonism being relevant to migraine. However, no periciazine-specific evidence supports this, and the TxGNN score is a computational prediction only.

**Other predicted indications** (all L5, all Hold):
- **Migraine with brainstem aura** and **migraine with or without aura, susceptibility to**: These share the migraine rationale. The first likely reflects the wider migraine cluster rather than subtype-specific biology, and brainstem aura adds sedation and neurological-monitoring concerns. The second describes a genetic susceptibility phenotype rather than a treatable condition.
- **Dysthymic disorder**: There is only a weak, indirect rationale. Periciazine's sedative and extrapyramidal profile argues against use in chronic low-grade depression.
- **Atrophoderma vermiculata** and **ulerythema ophryogenesis**: No plausible mechanistic link was identified. These are probably graph-based artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010P0AAADAD | Pericyazine Tablets 2.5 mg | Tablet | Not stated in the compiled records |
| 0402010P0BBABAE | Neulactil Tablets 10 mg | Tablet | Not stated in the compiled records |

Both products are valid single-ingredient authorisations. The identifiers shown are BNF-style codes (BNF chapter 4.2.1, antipsychotic drugs), not MHRA "PL" numbers. Dosage form is inferred from the product names, as it is not recorded in the compiled data. No NICE-appraised indication for migraine was identified.

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned only one pharmacological entry (the dopamine D1 receptor target), with no drug-drug interactions listed. This is not evidence that none exist. Phenothiazines have well-known interactions, including additive CNS depression and anticholinergic effects, so please check the BNF.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and a class-level argument from other phenothiazines. There are no trials or publications for periciazine in migraine, and the mechanism of action and safety data are incomplete. The other predicted indications have weaker or no plausible rationale.

**To proceed, the following is needed:**
- Complete safety data (warnings and contraindications) from the SmPC and BNF, which currently blocks safety screening
- Confirmed mechanism of action and receptor binding data
- A literature review for periciazine or close phenothiazine analogues in migraine, compared with established agents such as prochlorperazine and chlorpromazine
- Assessment of route compatibility, since migraine treatment often needs non-oral or rapid-onset routes and only oral tablets are recorded
- Review of the sedation and extrapyramidal burden relative to existing migraine options
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

