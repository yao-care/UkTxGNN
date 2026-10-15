---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
---

# Haloperidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Haloperidol: From Psychotic Disorder to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is a long-established antipsychotic, used for psychotic disorders, schizophrenia and Tourette syndrome.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psychotic disorder (also schizophrenia, schizoaffective disorder, schizophreniform disorder, Tourette syndrome) |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Haloperidol is generally understood to be a dopamine D2 receptor antagonist, and this underlies its use in psychosis and Tourette syndrome.

No mechanistic link has been identified between D2 antagonism and the fucosylation pathways that are defective in this rare inherited metabolic condition. The very high TxGNN score (99.91%) reflects patterns in the knowledge graph rather than biological or clinical evidence. On current information the prediction is not plausible enough to act on without further mechanistic work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010J0AAAAAA (listed identifier, not in PL format) | Haloperidol capsules 500 microgram | Not stated | Not stated |

The record contains one valid single-ingredient authorisation. It gives no dosage form or approved indication text, so refer to the current SmPC and BNF for licensed uses. No NICE-appraised indication for the predicted condition is identified.

---

## Safety Considerations

- **Contraindications and cautions (knowledge-graph associations, not label text):** The drug-disease associations recorded for haloperidol include:
  - cardiac: long QT syndrome (including familial), torsades de pointes
  - neurological: epilepsy, basal ganglia disease, neuroleptic malignant syndrome
  - blood disorders: neutropenia, leukopenia, agranulocytosis and congenital neutropenia syndromes
  - endocrine: hypothyroidism, potassium deficiency
  - other: liver disease, gallbladder disease, hypotensive disorder, female breast carcinoma

  Check the SmPC for the formally licensed contraindications.
- **Drug Interactions:** 100 interactions are recorded.
  - **Major:** bupropion, morphine, clarithromycin and dolasetron.
  - **Moderate (examples):** famotidine, epinephrine, hydrocortisone, amphotericin B, hyoscyamine, loperamide, aprepitant, atropine, glycopyrronium and dicyclomine.

Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanistic link between dopamine antagonism and defective fucosylation. Haloperidol also carries significant safety considerations, such as QT prolongation and extrapyramidal effects, so exposing patients to it without a rationale is hard to justify.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis, supported by preclinical data in glycosylation-disorder models
- Detailed mechanism of action data for haloperidol
- Review of the SmPC and BNF safety information against this rare-disease population

**Note on other predictions for this drug:** Among the other predicted indications, only **manic bipolar affective disorder** (TxGNN score 99.83%) has substantial support. It has completed Phase 3 trials, including a placebo- and haloperidol-controlled olanzapine trial (NCT00129220, n=224), and network meta-analyses (PMIDs 34642461, 39191865). That use is close to haloperidol's existing psychiatric indications rather than true repurposing, and it is rated "Proceed with Guardrails". Guardrails would include monitoring for extrapyramidal symptoms, QTc prolongation and tardive dyskinesia, and reviewing interactions before co-prescribing. The remaining predictions (retinal dystrophy, myopia variants and various congenital malformation syndromes) are rated Hold, mostly with no clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

