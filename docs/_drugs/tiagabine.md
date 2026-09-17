---
layout: default
title: Tiagabine
parent: Moderate Evidence (L3-L4)
nav_order: 572
evidence_level: L3
indication_count: 1
---

# Tiagabine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

# Tiagabine: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

Tiagabine is a GABA reuptake inhibitor used as adjunctive therapy for partial (focal) epilepsy. The TxGNN model predicts a possible link to **Visual Epilepsy**, but the supporting evidence largely concerns visual-field *side effects* of tiagabine rather than treatment efficacy for this seizure subtype, and only **1 indirect clinical trial** and **19 publications** are currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial (focal) epilepsy — adjunctive/add-on therapy (as described in evidence rationale; no UK licence text available) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The structured `original_moa` field is not populated, but the evidence pack's own rationale text provides mechanistic detail: Tiagabine is a selective GABA reuptake inhibitor (GAT‑1 inhibitor) that increases extracellular GABA concentration at the synapse, enhancing inhibitory neurotransmission and suppressing neuronal hyperexcitability. It is an established adjunctive treatment for partial (focal) epilepsy.

Visual (photosensitive/reflex) epilepsy is a subtype within the broader epilepsy spectrum, triggered by visual stimuli rather than a distinct disease mechanism. Since tiagabine's GABAergic action is not seizure-type-specific, there is a theoretical biological plausibility that its mechanism could extend to other epilepsy subtypes, including visual epilepsy.

However, a significant caveat applies. The literature underlying this specific prediction is dominated by studies of **visual field defects as an adverse effect** of GABAergic antiepileptics (vigabatrin and tiagabine) — for example PMID 12588906 and PMID 17560495 — rather than evidence of therapeutic efficacy in visual/photosensitive epilepsy. This raises a real possibility that the TxGNN knowledge-graph link conflates "epilepsy treatment" literature with "AED-induced visual side-effect" literature, rather than representing a genuine, independent repurposing hypothesis. This prediction should therefore be treated with caution rather than as positive supporting evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational "Liceo" study assessing new AEDs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, tiagabine, topiramate) as first-choice bitherapy in focal epilepsy; not designed to evaluate tiagabine specifically or the visual epilepsy subtype (relevance graded C — indirect). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22592677](https://pubmed.ncbi.nlm.nih.gov/22592677/) | 2012 | Cochrane review | Cochrane Database Syst Rev | Systematic review of tiagabine as add-on therapy for drug-resistant partial epilepsy; supports general efficacy but not visual epilepsy specifically. |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice guideline | Neurology | AAN/AES guideline update on efficacy and tolerability of newer AEDs (including tiagabine) for new-onset focal/generalised epilepsy. |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Case series/safety | J Neurol Neurosurg Psychiatry | Reports visual field defects associated with vigabatrin and tiagabine — an adverse-effect study, not evidence of efficacy for visual epilepsy. |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Review | Pediatric Neurology | Reviews visual adverse effects (visual field and colour vision deficits) of antiepileptic drugs, including tiagabine. |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Overview of mechanisms of action of currently used antiseizure drugs, including GABAergic agents such as tiagabine. |
| [11520315](https://pubmed.ncbi.nlm.nih.gov/11520315/) | 2001 | Review | Epilepsia | Reviews GABAergic mechanisms underlying epilepsy and seizure control. |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Drug review | Seminars in Pediatric Neurology | Reviews tiagabine pharmacokinetics, efficacy against partial seizures, and safety data. |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Drug review | Epilepsia | Reviews tiagabine's unique GABA-reuptake mechanism, pharmacokinetics, and add-on efficacy for partial seizures. |
| [15094857](https://pubmed.ncbi.nlm.nih.gov/15094857/) | 1998 | Drug review | Drugs of Today | Summarises tiagabine's mechanism, efficacy in seizure models, and lack of significant hepatic drug interactions. |
| [10030435](https://pubmed.ncbi.nlm.nih.gov/10030435/) | 1998 | Drug review | J Intellect Disabil Res | Discusses tiagabine as a therapeutic option for partial epilepsy in patients with intellectual disability. |

## UK Market Information

Tiagabine is **not currently marketed in the United Kingdom**. No MHRA marketing authorisations are on record (total licences: 0), so no product-level dosage form or indication data is available.

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interactions) is currently available for this candidate — all relevant fields are data gaps, including a **blocking** gap on TFDA/UK label warnings and contraindications (DG001) that prevents a formal S1 safety review.

Please refer to the SmPC and BNF for safety information once available. As tiagabine is not currently licensed in the UK, no UK SmPC currently exists; safety data should be sourced from other jurisdictions' product labelling in the interim. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is only supported to Evidence Level L3, and the evidence pack's own mechanistic rationale flags a strong likelihood that the "visual epilepsy" link is a knowledge-graph artefact — conflating AED efficacy literature with visual-field *side-effect* literature — rather than an independent repurposing hypothesis. Combined with a blocking data gap on safety/label information (DG001) and the drug's unlicensed status in the UK, there is insufficient basis to advance beyond the research-question stage.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent label data (warnings, contraindications) to resolve DG001 (blocking)
- Structured original MOA and original indication data for the drug record (DG002)
- Targeted evidence (case series or trials) specifically evaluating tiagabine efficacy in photosensitive/visual epilepsy, distinct from adverse-effect literature
- Confirmation from the KG/mapping team on whether the "visual epilepsy" node is genuinely distinct from general "epilepsy," to rule out the suspected literature-confound artefact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

