---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Perampanel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Perampanel: From Epilepsy (Focal and Generalised Seizures) to Visual Epilepsy

## One-Sentence Summary

Perampanel is a selective AMPA-receptor antagonist used in the treatment of refractory partial-onset (focal) and generalised seizures. The TxGNN model predicts it may also be effective for **visual epilepsy** (a rare reflex epilepsy triggered by visual stimuli), with a very high prediction score but currently only **3 clinical trials** and **0 dedicated publications** — none of which specifically study visual/photosensitive epilepsy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — refractory partial-onset and generalised seizures (drawn from clinical trial background text; not separately confirmed in the regulatory dossier, which lists no original indications) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 (1 completed Phase 2 randomised, double-blind, placebo-controlled trial; note all 3 trials are general-epilepsy studies, none disease-specific to visual/reflex epilepsy) |
| UK Market Status | Not marketed (0 marketing authorisations recorded — see caveat below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the regulatory dossier for perampanel. However, the supporting literature within this evidence pack consistently describes perampanel as a first-in-class, selective, non-competitive antagonist of AMPA-type glutamate receptors (PMID [21635236](https://pubmed.ncbi.nlm.nih.gov/21635236/), [29042752](https://pubmed.ncbi.nlm.nih.gov/29042752/)). By dampening excitatory glutamatergic transmission broadly across seizure-generating circuits, this mechanism underlies perampanel's established use in refractory partial-onset and primary generalised tonic-clonic seizures.

Visual epilepsy is a reflex epilepsy in which seizures are triggered by visual stimuli (e.g. flicker, pattern). Reflex epilepsies share cortical hyperexcitability as a common pathway, and AMPA receptors play a well-documented role in propagating cortically-triggered seizure activity. This gives some mechanistic plausibility to the TxGNN prediction, and is indirectly reinforced by preclinical evidence of perampanel's efficacy in other reflex/stimulus-triggered seizure models, such as audiogenic seizures in genetically epilepsy-prone rats (PMID [30092489](https://pubmed.ncbi.nlm.nih.gov/30092489/)).

That said, none of the three retrieved trials specifically enrolled or studied patients with visual/photosensitive epilepsy — they are general focal/generalised epilepsy studies, one of which incidentally used visual evoked potential (VEP) testing as a neurophysiological outcome measure rather than a treatment-efficacy endpoint. The mechanistic rationale is therefore currently stronger than the direct clinical evidence for this specific reflex-epilepsy subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Assessed tolerability, safety and pharmacokinetics of perampanel (E2007) in patients with refractory partial or generalised seizures on concomitant AEDs |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Evaluated perampanel's effects on cognition and EEG in epilepsy patients, focusing on adverse-effect assessment during AED introduction |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | First study to examine whether perampanel affects neurophysiology tests (EEG, SEP, BAEP, VEP) |

---

## Literature Evidence

Currently no related literature available for this specific indication (visual epilepsy).

---

## UK Market Information

No marketing authorisation is recorded for perampanel in this evidence pack (0 licences; market status: not marketed).

**Note:** this should be verified before the evaluation is finalised — perampanel (originator brand Fycompa) is a recognised antiepileptic medicine with regulatory history internationally, so the absence of a UK licence record here is unexpected and should be confirmed directly against the current MHRA product register.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Important gap:** the evidence pack flags perampanel's key warnings, contraindications and drug interaction data as an unresolved **Blocking** data gap (DG001) — this prevents completion of an initial safety assessment and must be resolved before this candidate can progress, regardless of the efficacy signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Safety data (warnings, contraindications, DDIs) is marked as a Blocking gap in the evidence pack, which alone prevents progression past initial safety screening. This is compounded by an unconfirmed mechanism of action, an apparent absence of UK marketing authorisation, and the fact that the top-ranked indication (visual epilepsy) has no disease-specific clinical evidence — all three retrieved trials are general epilepsy studies rather than reflex/photosensitive epilepsy trials.

**To proceed, the following is needed:**
- MHRA-approved SmPC/PIL to resolve the Blocking safety data gap (DG001): key warnings, contraindications, drug interactions
- Confirmed mechanism-of-action data against official regulatory labelling (DG002)
- Verification of UK marketing authorisation status directly against the MHRA products register
- Disease-specific evidence (reflex/photosensitive epilepsy cohorts) before advancing "visual epilepsy" beyond mechanistic rationale
- Consider that within this same evidence pack, **status epilepticus** (rank 10) carries markedly stronger direct evidence — five dedicated trials including disease-specific Phase 2–4 studies, evidence level L2, and a "Proceed with Guardrails" scoring — and may represent a more tractable repurposing target once the safety data gap is resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

