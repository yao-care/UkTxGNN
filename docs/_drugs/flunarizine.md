---
layout: default
title: Flunarizine
parent: High Evidence (L1-L2)
nav_order: 274
evidence_level: L1
indication_count: 10
---

# Flunarizine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Flunarizine: From Calcium-Channel Blockade to Migraine Disorder

## One-Sentence Summary

Flunarizine is a selective T-type calcium-channel blocker with additional H1-antihistamine and weak dopamine-receptor blocking activity; the evidence pack's own regulatory record shows no documented original indication and no UK marketing authorisation. The TxGNN model predicts efficacy in **Migraine Disorder** (score **99.12%**), and this is supported by **19 clinical trials**, though — notably — the underlying evidence itself suggests this is confirmation of an already internationally established use rather than a genuinely novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug-level `original_indications` and MOA fields are both data gaps) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original-MOA data is flagged as a gap (DG002) in this evidence pack, but the model's own repurposing rationale supplies working mechanistic detail: flunarizine is described as a selective T-type calcium-channel blocker with additional H1-antihistamine and weak dopamine-receptor blocking activity. This profile is consistent with suppression of cortical spreading depression and abnormal cerebrovascular tone — the mechanistic basis widely cited for migraine prophylaxis.

Importantly, the evidence pack itself flags a caveat that should shape how this prediction is read: it notes that migraine prophylaxis is, in fact, a long-established approved use of flunarizine in most European and Asian markets, and that the empty `original_indications` field most likely reflects a data gap in this specific regulatory source rather than a genuine absence of prior approval. In other words, this candidate is best understood as **evidence confirmation of an existing international use**, not a novel mechanistic hypothesis — a distinction that matters for how "new" the opportunity actually is in a UK context, where the drug currently holds no marketing authorisation at all.

A second, more genuinely hypothesis-generating signal in the same evidence pack is "headache disorder" (rank 4, also Evidence Level L1), which shares the same mechanistic rationale and is supported by 20 literature records, including systematic reviews, meta-analyses and clinical guidelines specifically evaluating flunarizine in migraine/headache prophylaxis (see Literature note below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Head-to-head comparison of flunarizine and propranolol for reducing paediatric migraine frequency (PedMIDAS), ages 8–15. |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Randomised three-arm comparison of greater occipital nerve block, topiramate, and flunarizine for episodic migraine prophylaxis. |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine prophylaxis. |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Open-label pharmacokinetic drug-interaction study of flunarizine and topiramate during mono- and concomitant therapy. |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Flunarizine vs amitriptyline for migraine prophylaxis, comparing attack frequency and VAS pain scores. |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) (PREMI) | Phase 4 | Not yet recruiting | 460 | Pragmatic multicentre trial comparing amitriptyline, flunarizine, topiramate and propranolol as first-line migraine prophylaxis in primary care. |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | Not yet recruiting | 60 | Fu's subcutaneous needling vs flunarizine hydrochloride (active control) for migraine without aura. |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Completed | 60 | Alpha-lipoic acid as add-on to standard prophylaxis (background therapy includes flunarizine) in adolescent migraine. |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Unknown | 96 | Acupuncture vs flunarizine hydrochloride (current standard prophylactic option) for migraine without aura. |
| [NCT02747940](https://clinicaltrials.gov/study/NCT02747940) | Phase 4 | Completed | 200 | fMRI/machine-learning "brain signature" characterisation of chronic migraine and fibromyalgia pain. |

---

## Literature Evidence

Currently no related literature is registered under the "Migraine Disorder" disease label in this evidence pack (PubMed query returned 0 results for this exact term).

*Note: the closely related, mechanistically identical label "headache disorder" in the same evidence pack returns 20 literature records for flunarizine, including systematic reviews/meta-analyses (e.g. the European Headache Federation's flunarizine re-appraisal, PMID 37723437; Stubberud et al.'s meta-analysis, PMID 30699098) and clinical guidelines. This body of literature substantiates the mechanistic rationale above even though it is not indexed against the "Migraine Disorder" term specifically.*

---

## UK Market Information

Flunarizine currently holds no UK marketing authorisation (0 licences on record; market status: **not marketed**). No product, dosage form or approved indication text is therefore available from this data source.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications and drug-interaction data are recorded as a blocking data gap (DG001) in this evidence pack and could not be summarised here.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- TxGNN score is very high (99.12%) and is corroborated by 19 clinical trials directly involving flunarizine in migraine prophylaxis, several head-to-head against established comparators (topiramate, amitriptyline, propranolol). However, this strength largely reflects an already internationally established use rather than a novel mechanistic discovery, and the drug has no current UK marketing authorisation — so any UK pathway would need to start essentially from a licensing/safety baseline of zero.

**To proceed, the following is needed:**
- MHRA/SmPC safety data (key warnings, contraindications, drug interactions) to close the blocking data gap (DG001)
- Confirmed original mechanism-of-action and original-indication regulatory record (DG002), ideally corroborated against a formal international regulatory source rather than inference
- A defined UK licensing pathway assessment, given zero current marketing authorisations
- Literature specifically indexed against "Migraine Disorder" (or explicit confirmation that the "headache disorder" literature set should be treated as equivalent evidence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

