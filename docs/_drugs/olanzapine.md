---
layout: default
title: Olanzapine
parent: Moderate Evidence (L3-L4)
nav_order: 426
evidence_level: L3
indication_count: 3
---

# Olanzapine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **3** 
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

# Olanzapine: From Antipsychotic Therapy to Agoraphobia

## One-Sentence Summary

> Olanzapine is a well-established second-generation antipsychotic, though this evidence pack does not capture its UK licensed indications (data gap).
> The TxGNN model's strongest *evidence-supported* signal points to **Agoraphobia** (typically evaluated in the context of treatment-resistant panic disorder),
> with **0 clinical trials** but **7 supporting publications** (mainly reviews, one open-label trial, and case reports) currently underpinning this direction.

> **Note on candidate selection**: This evidence pack contains three TxGNN-ranked predictions. The highest-scoring candidate by raw model score (benign paroxysmal torticollis of infancy) has **no supporting literature, no clinical trials, and no mechanistic rationale** — the evidence pack itself flags this as reflecting graph topology similarity only, with unknown safety in infants. It has therefore not been selected as the headline indication. See "Other TxGNN-Ranked Candidates" below for full transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (data gap). Olanzapine is widely recognised as a second-generation antipsychotic used in schizophrenia and bipolar disorder. |
| Predicted New Indication | Agoraphobia (evidence concentrated in treatment-resistant panic disorder with agoraphobia) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L3 |
| UK Market Status | Not marketed (per this evidence pack — see caveat below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Olanzapine is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the supporting literature within the pack, Olanzapine's known pharmacology — 5-HT2A and dopamine (D2) antagonism, alongside H1 and M1 activity — is proposed to modulate amygdala–prefrontal anxiety circuitry, which is the rationale cited for its use as an augmentation agent.

The clinical link is not to agoraphobia as a standalone diagnosis, but to **treatment-resistant panic disorder with agoraphobia**, where Olanzapine has been trialled as an add-on to SSRIs in patients who failed first-line therapy. This is an important distinction: agoraphobia and panic disorder frequently co-occur and are studied together, but they are not identical diagnostic entities, and the evidence base reflects this overlap rather than agoraphobia in isolation.

Mechanistically this is plausible as a second-line augmentation strategy in a narrow, treatment-resistant population, but it is not supported by any randomised controlled trial data, and the largest study identified is a 12-week open-label trial (n=31). This places the signal well short of a robust efficacy claim.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Review | Psychotherapy and Psychosomatics | Integrative review of pharmacological, psychotherapeutic and neurostimulatory options in treatment-resistant anxiety disorders |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Review | Expert Opinion on Pharmacotherapy | Systematic review of treatment-resistant panic disorder management strategies |
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label Trial | Journal of Clinical Psychopharmacology | 12-week, fixed-dose (5mg/day) olanzapine augmentation in 31 SSRI-resistant panic disorder patients (with/without agoraphobia); efficacy and tolerability assessed via Panic Attack and Anticipatory Anxiety Scale |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort | Journal of Affective Disorders | 24-month outcomes study examining impact of comorbid agoraphobia/panic/OCD/SAD/GAD on bipolar I disorder course |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Case Report | American Journal of Psychiatry | Early case report describing olanzapine's effect on panic attacks |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case Report | Pharmacopsychiatry | Case of remission from treatment-refractory panic disorder with olanzapine + paroxetine combination |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Case Report | Psychiatria Danubina | Case of panic disorder with agoraphobia comorbid with psychosis, managed via CBT |

---

## Other TxGNN-Ranked Candidates (Not Selected as Headline)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|---------|-------------|-----------------|-----------------|-------|
| 1 | Benign paroxysmal torticollis of infancy | 99.54% | L5 | Hold | No clinical trials, no literature, no mechanistic plausibility. The pack's own rationale states there is "no support" — BPTI is linked to CACNA1A/vestibular-migraine mechanisms with no known connection to Olanzapine's D2/5-HT2A/H1/M1 activity. Safety of antipsychotic use in infants is unevaluated. Not clinically actionable. |
| 3 | Dysthymic disorder | 99.28% | L4 | Hold | Only directly relevant study is in patients with borderline personality disorder and comorbid dysthymia (not primary dysthymic disorder). Remaining literature covers second-generation antipsychotics as a class, or other agents (benzamides, amisulpride) rather than Olanzapine specifically. |

---

## UK Market Information

This evidence pack records Olanzapine as **not marketed**, with **0 licensed products** and no licence entries. This does not align with Olanzapine's well-established global market presence (e.g., as a generic antipsychotic and under the brand Zyprexa), and should be treated as a **data completeness gap** in this evidence pack rather than confirmation of actual UK licensing status. MHRA/SmPC records should be independently verified before this report is used for any regulatory or clinical decision.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: This evidence pack flags a **Blocking** data gap (DG001) — UK product label warnings/contraindications and drug–drug interaction data were not available at the time of this report. No safety assessment can be considered complete until this is resolved.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The best-supported candidate (agoraphobia, via treatment-resistant panic disorder) rests on L3 evidence — open-label and case-report data only, with no RCTs — and is further constrained by a **Blocking** safety data gap (no verified UK warnings, contraindications, or DDI data). The top TxGNN-scored candidate (infantile torticollis) is explicitly unsupported by mechanism or literature and should not be pursued.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain verified UK SmPC/BNF warnings and contraindications
- Resolve DG002 (High): confirm Olanzapine's mechanism of action from DrugBank or equivalent source
- Verify actual UK/MHRA licensing status (current "not marketed" status appears inconsistent with known market presence)
- Identify controlled trial data (ideally RCT) for olanzapine augmentation specifically in agoraphobia or panic disorder with agoraphobia
- Clarify diagnostic scope: distinguish agoraphobia as a standalone target versus panic disorder with agoraphobia as studied in the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

