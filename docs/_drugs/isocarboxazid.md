---
layout: default
title: Isocarboxazid
parent: Model Prediction Only (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Isocarboxazid
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

# Isocarboxazid: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Isocarboxazid is a classic irreversible, non-selective monoamine oxidase inhibitor (MAOI) antidepressant, historically used in the treatment of depression (particularly atypical and treatment-resistant forms). The TxGNN model's highest-scoring prediction is **Benign Paroxysmal Torticollis of Infancy**, but this direction is currently supported by **no clinical trials** and **no published literature**, and the drug's own repurposing rationale flags the mechanistic link as absent and the safety profile as inappropriate for this paediatric population.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (MAOI antidepressant class) — no formal UK licence text is available for this product |
| Predicted New Indication | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for isocarboxazid is not available in this evidence pack (marked as a data gap). Based on established pharmacological knowledge cited elsewhere in the evidence (e.g. PMID 35837681, "classic MAO inhibitor antidepressants... for treatment-resistant depression"), isocarboxazid is known to act by irreversibly inhibiting MAO-A and MAO-B, raising synaptic concentrations of serotonin, noradrenaline and dopamine — the pharmacological basis for its use in depression.

Benign paroxysmal torticollis of infancy is a self-limiting paediatric condition with an unclear aetiology, thought to be related to vestibular dysfunction or a migraine-spectrum phenomenon in infants. The evidence pack's own repurposing rationale for this prediction is explicit that **no known pathway connects MAO inhibition to this condition's pathophysiology**, and that MAOI use in infants carries substantial safety risk (hypertensive crisis, dietary/drug interactions) with no supporting clinical evidence.

In short, this is a case where the TxGNN model's statistical prediction score is high, but the accompanying mechanistic and clinical evidence does not support it — and in fact argues against pursuing it. By contrast, several lower-ranked predictions in this evidence pack (e.g. melancholia, neurotic depression — both L2, "Proceed with Guardrails") are far better supported, since they sit within isocarboxazid's known antidepressant pharmacology and are backed by placebo-controlled trials. These may be more appropriate candidates for further evaluation than the top-ranked prediction discussed here.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this evidence pack could not retrieve isocarboxazid's warnings, contraindications, or drug interaction data (flagged as a **Blocking** data gap, DG001). Given that MAOIs carry well-known risks (hypertensive crisis with tyramine-containing foods, serious interactions with serotonergic and sympathomimetic drugs), formal SmPC/BNF review is essential before any further evaluation of this or any other predicted indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (benign paroxysmal torticollis of infancy) has no clinical trial or literature support, no plausible mechanistic pathway, and known safety concerns for MAOI use in infants. Combined with missing UK labelling/safety data (Blocking gap DG001) and missing MOA confirmation (DG002), this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- UK SmPC warnings, contraindications and interaction data for isocarboxazid (DG001 — blocking)
- Confirmed mechanism of action data from DrugBank or equivalent source (DG002)
- If pursuing repurposing further, redirect evaluation toward higher-evidence predictions in this dataset (e.g. melancholia or neurotic depression, both L2/"Proceed with Guardrails"), which align with isocarboxazid's established antidepressant pharmacology
- Any future paediatric indication would require a specific, disease-relevant mechanistic rationale and dedicated safety data before consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

