---
layout: default
title: Lacosamide
parent: Model Prediction Only (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Lacosamide"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "insomnia (disease)", "migraine with brainstem aura", "myofascial pain syndrome", "obsessive-compulsive disorder", "papillary conjunctivitis"]
description: "Lacosamide: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Lacosamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Lacosamide: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Lacosamide is an antiseizure medicine that acts on voltage-gated sodium channels.
The TxGNN model predicts it may be effective for **migraine disorder**, the highest-evidence candidate among the model's top ten predictions,
with **4 clinical trials** (including 3 Phase 3 trials) and **18 publications** currently linked to this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 (as assigned in the compiled data; see the caveats below) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. From the published literature, lacosamide enhances slow inactivation of voltage-gated sodium channels and may also interact with collapsin response mediator protein 2 (CRMP2). Preclinical work suggests this could inhibit release of calcitonin gene-related peptide (CGRP) in the trigeminal system, a key pathway in migraine.

Migraine and epilepsy share features of neuronal hyperexcitability. Lacosamide reduced cortical spreading depolarisation in mice (PMID 40670944), a model relevant to migraine aura. Other antiseizure drugs, such as topiramate and valproate, are established migraine preventives, which supports class-level plausibility.

Two caveats apply. First, the mechanistic link is plausible but not proven in humans. Second, the evidence level of L1 reflects the number of Phase 3 trials listed. Of these, one is a small pilot-style study with a biomarker focus, and another has unknown status. The published result details were not available here and must be verified before the level is relied upon.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Phase 3 | Completed | 600 | Lacosamide versus propranolol in migraine; outcomes are reduction in monthly migraine days and ≥50% responder rate. Corresponds to the published RCT (PMID 41863672). |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Phase 3 | Unknown | 600 | Lacosamide versus topiramate in migraine; same outcomes. Completion and results are unverified. |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Phase 3 (labelled) | Completed | 200 | Randomised pilot of lacosamide 50 mg twice daily plus ibuprofen versus ibuprofen alone, assessing serum CGRP in episodic migraine. Biomarker focus, and the Phase 3 label appears inconsistent with a pilot design. |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Phase 2 | Completed | 218 | Double-blind, placebo-controlled trial of lacosamide 100 mg/day and 300 mg/day for up to 18 weeks to prevent migraine. The indication could not be confirmed from the available data, and no results were provided. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | RCT (double-blind) | Molecular Neurobiology | Lacosamide versus propranolol for preventing episodic migraine, including patients who cannot tolerate propranolol. Result details were not available here. |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | RCT | Acta Neurologica Belgica | Effect of lacosamide on serum CGRP in episodic migraine. Lacosamide is proposed to inhibit CGRP release via CRMP2. |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | Systematic review and meta-analysis | Epilepsia | Adverse event profile of lacosamide across randomised controlled trials. |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | Preclinical | J Headache Pain | Lacosamide effect on cortical spreading depolarisation in mice. |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | Preclinical | Pain Reports | (S)-Lacosamide in preclinical models of cephalic pain, exploring CRMP2 as a target for inhibiting CGRP release. |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Review | Expert Opin Emerg Drugs | Emerging treatments for chronic and refractory chronic migraine. |
| [35696452](https://pubmed.ncbi.nlm.nih.gov/35696452/) | 2022 | Review | Brain | SCN1A gain-of-function disorders, including links to familial hemiplegic migraine type 3 (indirect mechanistic support). |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010AHAAAAAA (BNF-style code; not a PL number) | Lacosamide tablets 50 mg | Tablet (form not specified in the data) | Not stated in the data compiled |

One single-ingredient authorisation is recorded as valid. No approved indication text was available, so UK-specific indications should be confirmed in the SmPC and BNF.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease links in the TxGNN knowledge graph, not from label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, atrial fibrillation, atrial flutter, coronary artery disease, myocardial ischaemia, atrioventricular block, sick sinus syndrome and familial sick sinus syndrome. The cardiac conduction items are particularly relevant to patient selection.
- **Drug interactions** (25 recorded; main ones listed):
  - Major: dolasetron, ceritinib, siponimod.
  - Moderate: clarithromycin, ethanol, cobicistat, chloroquine, hydroxychloroquine, mefloquine, lidocaine, ketoconazole, pasireotide, alectinib, brigatinib, crizotinib, fingolimod, idelalisib, imatinib, ozanimod, sunitinib.
- **Literature safety signal**: a case report describes lacosamide-precipitated neutropenia in a patient with bipolar disorder and epilepsy (PMID 30251375 is a separate study; the case is PMID 30275630). A systematic review (PMID 22779776) characterises the drug's adverse event profile.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine is the best-supported of the model's predictions, with two completed Phase 3 trials against active comparators, a published double-blind RCT versus propranolol, and supportive preclinical data on spreading depolarisation and CGRP. However, no placebo-controlled Phase 3 evidence is available, and the detailed results have not been verified.

**To proceed, the following is needed:**
- Verify the results of NCT05851781 and PMID 41863672, including effect sizes and tolerability.
- Confirm the status and results of NCT06243692, and clarify the indication and outcomes of NCT00440518.
- Confirm that the Phase 3 label on NCT05632133 is accurate, given its pilot design.
- Obtain UK SmPC warnings, contraindications and approved indications, which were not available in the compiled data.
- Review the cardiac conduction and haematological (neutropenia) safety signals, and the interaction burden, for a migraine-prevention population.
- Obtain detailed mechanism-of-action data.
- Consider placebo-controlled evidence, since comparator-only designs do not establish superiority to placebo.

**Other predictions (for context):** The remaining top-ten predictions have weaker support. Bipolar disorder (manic) has limited observational evidence and a neutropenia safety flag (Research Question). Myofascial pain syndrome has one completed Phase 2 placebo-controlled trial in fibromyalgia without available results (Research Question). Migraine with brainstem aura has only indirect support (Research Question). Tourette syndrome, trichotillomania, nephrogenic syndrome of inappropriate antidiuresis, insomnia, obsessive-compulsive disorder and papillary conjunctivitis are model predictions without supporting clinical evidence (Hold). For Tourette syndrome, the literature raises a possible adverse signal of antiepileptic-induced tics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

