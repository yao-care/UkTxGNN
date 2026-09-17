---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 536
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

Using no external skill here — this is a direct content-generation task fully specified by the provided report template; I'll produce the report against the given Evidence Pack.

# Sotalol: From Antiarrhythmic Therapy to Sick Sinus Syndrome 2, Autosomal Dominant (Signal Flagged as Likely False Positive)

## One-Sentence Summary

Sotalol is an antiarrhythmic (beta-blocking, potassium-channel-blocking) agent used internationally for atrial fibrillation and ventricular arrhythmias; no UK marketing authorisation is on file for this drug in this dataset. The TxGNN model's top-ranked prediction — **Sick Sinus Syndrome 2, Autosomal Dominant** — is **not supported by any clinical trial or literature evidence** and is mechanistically implausible as a treatment target: Sotalol's sinus-node-suppressing action would be expected to *worsen*, not treat, this condition. Across all seven candidates in this multi-indication screen, none currently meet the bar for a "Go" decision.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally licensed in the UK (no marketing authorisation on file); evidence in this pack indicates international use as an antiarrhythmic for atrial fibrillation and ventricular arrhythmias |
| Predicted New Indication (top-ranked) | Sick Sinus Syndrome 2, Autosomal Dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this record (`original_moa: [Data Gap]`). However, evidence embedded in this pack's literature abstracts indicates Sotalol is a non-selective beta-adrenergic blocker with Class III antiarrhythmic activity (IKr/potassium-channel blockade), consistent with its established international use for rhythm control in atrial fibrillation and management of ventricular arrhythmias, including in adults with congenital heart disease.

For the top-ranked prediction, the relationship between Sotalol's known pharmacology and Sick Sinus Syndrome runs in the **wrong direction**. Beta-blockade and IKr-mediated repolarisation prolongation both suppress sinoatrial node automaticity and conduction; in a patient with sick sinus syndrome, this would be expected to aggravate bradycardia or precipitate sinus arrest rather than treat the condition. Sick sinus syndrome is typically listed as a caution or contraindication for beta-blockers and Class III antiarrhythmics in product literature, not an indication.

This suggests the very high TxGNN score reflects a **structural artefact of the knowledge graph** — Sotalol shares graph neighbours (sinus node, cardiac conduction pathway) with sick sinus syndrome because of a *safety* relationship, which the model appears to have encoded as a *therapeutic* one. No clinical trials or publications support treating sick sinus syndrome with Sotalol, and none should be sought on this basis; this is a signal for safety review, not repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Screened

This evidence pack scored seven candidate indications for Sotalol. For completeness and to avoid over-weighting the (likely erroneous) top score, all are summarised below.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------------|-----------------|-----------------|------|
| 1 | Sick sinus syndrome 2, autosomal dominant | 99.76% | L5 | Hold | Mechanistically a contraindication signal, not a treatment signal — see above |
| 2 | Wildervanck syndrome | 99.65% | L5 | Hold | Congenital skeletal/otic syndrome; no mechanistic link to cardiac electrophysiology; likely graph noise |
| 3 | Sarcoglycanopathy (limb-girdle muscular dystrophy) | 99.64% | L5 | Research Question | Plausible only indirectly, via management of associated cardiomyopathy/arrhythmia (as with Duchenne/Becker MD); no trials or literature yet identified |
| 4 | Stroke disorder | 99.44% | L3 | Research Question | Best-evidenced candidate, but represents an extension of the *existing* AF-rhythm-control indication rather than a novel mechanism; identified trials mostly test ablation or other antiarrhythmics, not Sotalol specifically against stroke outcomes ([NCT00007605](https://clinicaltrials.gov/study/NCT00007605), [NCT00911508](https://clinicaltrials.gov/study/NCT00911508)) |
| 5 | Manic bipolar affective disorder | 99.43% | L4 | Hold | Literature concerns a QT-prolongation drug–drug interaction risk with antipsychotics (e.g., risperidone) and a bradycardia case report during lithium co-therapy — these are safety signals, not efficacy evidence for mania |
| 6 | Macrocephaly, dysmorphic facies, and psychomotor retardation | 99.42% | L5 | Hold | Congenital neurodevelopmental syndrome; no mechanistic plausibility; no evidence |
| 7 | Obsolete susceptibility to ischaemic stroke | 99.23% | L5 | Hold | Duplicate/obsolete ontology term overlapping with #4; should be merged rather than pursued independently |

## UK Market Information

Sotalol currently holds **no marketing authorisation on file** in this dataset (`total_licenses: 0`, market status: Not marketed). No product entries, dosage forms, or licensed indications are available to summarise.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> Note: This dataset flags UK-specific SmPC warnings/contraindications as a **blocking data gap** (DG001) — this must be resolved before any safety assessment (S1) can proceed for this drug, regardless of which candidate indication is pursued.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (sick sinus syndrome) is not a genuine repurposing opportunity — it is best read as a mechanistic contraindication signal misclassified by the knowledge graph, with zero supporting trials or literature. Across the full set of seven predictions, none currently meet the evidence bar for "Go"; the most credible candidate (stroke-risk reduction) is an incremental extension of Sotalol's existing antiarrhythmic use rather than a novel indication, and is only supported at L3 (indirect trial/literature evidence, no Sotalol-specific stroke-outcome trial).

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain UK/EU SmPC warnings and contraindications for Sotalol before any safety screening can begin
- Resolve DG002: confirm original mechanism of action and licensed indication(s) via DrugBank or an equivalent authoritative source
- Confirm current UK marketing/licensing status, since this record shows zero authorisations
- If pursuing the stroke-risk-reduction angle (rank 4): identify or commission a trial with Sotalol as the specific intervention and stroke/thromboembolism as a primary or secondary endpoint
- If pursuing the sarcoglycanopathy angle (rank 3): seek preclinical or observational data on antiarrhythmic management of cardiomyopathy in this specific muscular dystrophy population
- No further action recommended on ranks 1, 2, 5, 6, or 7 without new evidence, given absent or contraindicated mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

