---
layout: default
title: Thioridazine
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
---

# Thioridazine
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

# Thioridazine: From Antipsychotic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

Thioridazine is a phenothiazine antipsychotic; the Evidence Pack does not contain a structured record of its original licensed indication or detailed mechanism of action, though literature context points to historical use in schizophrenia and other psychotic disorders. The TxGNN model predicts a very high likelihood of efficacy for **Manic Bipolar Affective Disorder** (score 99.98%), but **no clinical trials or published literature** in this Evidence Pack directly support that specific prediction, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the structured licensing data provided; literature context suggests historical use as an antipsychotic in schizophrenia/psychotic disorders |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for thioridazine is not available in this Evidence Pack. Based on the information that is available, thioridazine belongs to the phenothiazine class of antipsychotics, acting as a D2 dopamine receptor and 5-HT2A serotonin receptor antagonist. This class of drugs has an established, decades-long history of use in psychotic and mood disorders with psychotic features, which is the pharmacological basis for the TxGNN prediction.

The stated rationale for this specific prediction (manic bipolar affective disorder) is that D2/5-HT2A antagonism theoretically confers anti-manic activity, consistent with the fact that other typical antipsychotics (e.g. haloperidol) are used clinically in acute mania. However, the rationale itself explicitly notes that **this Evidence Pack contains no trials or literature directly supporting this indication** — the high TxGNN score reflects a knowledge-graph inference rather than observed clinical outcomes.

It is worth noting that a closely related node, "bipolar disorder" (ranked 6th among predictions, score 99.69%), does have associated trial and literature evidence in this pack. However, that evidence is predominantly **safety-related** rather than efficacy-related — one trial assessed hyperglycaemic emergencies with atypical antipsychotics, and another specifically evaluated arrhythmia/QT-interval risk with thioridazine. This pattern is consistent with thioridazine's known cardiac liability (QT-interval prolongation), which is widely understood to be the reason it is no longer marketed in many jurisdictions, including the UK.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Manic Bipolar Affective Disorder specifically.

---

## Literature Evidence

Currently no related literature available for Manic Bipolar Affective Disorder specifically.

---

## UK Market Information

Thioridazine is **not currently marketed in the UK** — no marketing authorisations are on file (0 licenses recorded in this Evidence Pack). No dosage form, product name, or approved indication data are therefore available to tabulate.

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, drug-drug interactions) are not populated in this Evidence Pack. Please refer to the SmPC and BNF for authoritative safety information, and report suspected adverse reactions via the Yellow Card Scheme.

**Notable signals identified elsewhere in the Evidence Pack (not from structured SmPC data, but from trial/literature narratives):**
- **Cardiac safety**: A completed trial (NCT00538122) specifically evaluated thioridazine for QT-interval abnormalities and arrhythmia risk via Holter ECG monitoring, consistent with thioridazine's well-known association with QT prolongation.
- **Lithium co-administration**: Case reports describe severe neurotoxicity (delirium, seizures, encephalopathy) when thioridazine was combined with lithium (PMID 106047, PMID 3945208).
- **Antidepressant interaction**: A case report describes elevated nortriptyline plasma levels following co-treatment with paroxetine and thioridazine (PMID 9690702), suggestive of a CYP2D6-mediated interaction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a very high score (99.98%) to manic bipolar affective disorder, this specific prediction is supported by zero clinical trials and zero literature in the Evidence Pack (Evidence Level L5). Combined with the drug's absence from the UK market and safety signals around QT prolongation identified for the closely related "bipolar disorder" node, there is insufficient basis to advance this candidate at present.

**To proceed, the following is needed:**
- TFDA/MHRA product labelling (SmPC) with full warnings and contraindications — currently a blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank or equivalent source (DG002)
- Indication-specific efficacy evidence (RCTs or controlled studies) for manic bipolar affective disorder, rather than relying on cross-indication inference
- A dedicated cardiac safety assessment (QT-interval prolongation risk) before any consideration of clinical use, given the signal in NCT00538122 and thioridazine's regulatory history
- Review of the related "bipolar disorder" prediction (rank 6) evidence base, which is more substantial but is weighted toward safety rather than efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

