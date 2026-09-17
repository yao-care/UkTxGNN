---
layout: default
title: Prednisolone
parent: High Evidence (L1-L2)
nav_order: 476
evidence_level: L2
indication_count: 10
---

# Prednisolone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Prednisolone: From Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

> Prednisolone is a systemic corticosteroid; this evidence pack does not record a specific licensed original indication for the drug in the underlying dataset (data gap — see Conclusion section).
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> with **1 highly relevant completed clinical trial** and **10+ supporting publications** (including a placebo-controlled trial) currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (`original_indications` and `taiwan_regulatory.licenses` are both empty — data gap) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug entry (`original_moa: [Data Gap]`, flagged as data gap DG002). Based on known pharmacology, prednisolone is a systemic glucocorticoid that suppresses T-cell-mediated and broader immune/inflammatory activity — this general mechanistic class information comes from the evidence pack's own repurposing rationale, not from an assumed indication.

The evidence pack's rationale states directly: *"Prednisolone is a systemic glucocorticoid that acts by suppressing T-cell-mediated autoimmune attack on the hair follicle, and is already one of the standard treatment options (pulse therapy) for severe/refractory alopecia areata."* Alopecia areata is understood as a T-cell-driven autoimmune attack on the hair follicle, so a broad immunosuppressive/anti-inflammatory agent is mechanistically plausible.

Notably, this is not a purely theoretical repurposing signal: oral pulse corticosteroid therapy (including methylprednisolone, a close pharmacological relative of prednisolone) already has published clinical use in severe, treatment-resistant alopecia areata, which supports the biological plausibility of the TxGNN prediction rather than it being a novel, untested hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone (same corticosteroid class) tested in patients with severe, therapy-resistant alopecia areata; graded **A** relevance in the evidence pack — direct disease-and-drug-class match |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared DERMOJET vs conventional syringe delivery of intralesional steroid for alopecia areata; relevant to steroid-based AA treatment delivery |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (Observational) | Completed | 296 | Real-world safety/effectiveness study of tofacitinib in alopecia, with participants receiving adjuvant prednisolone; relevant as combination-use context |

**Note:** The evidence pack also lists a further ~17 systemic lupus erythematosus (SLE) trials (e.g. baricitinib, sirolimus, PF-06700841, BMS-986165 studies) and unrelated trials (headache nerve block, prostate cancer). These are graded **C** ("background reference only") or unrated in the pack, as they involve different drugs and/or a different autoimmune disease, and have been excluded from the table above as not directly relevant to prednisolone in alopecia areata.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | Journal of the American Academy of Dermatology | Placebo-controlled study of oral pulse prednisolone therapy in alopecia areata — the only placebo-controlled trial identified for this specific drug/indication pairing |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Review | The Cochrane Database of Systematic Reviews | Network meta-analysis of alopecia areata treatments, including immunosuppressants such as corticosteroids |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Review of efficacy and adverse effects of corticosteroid pulse therapy in alopecia areata |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Review | The Australasian Journal of Dermatology | Systematic review of systemic treatments for alopecia areata/totalis/universalis |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Cohort | Saudi Medical Journal | Efficacy and safety of oral mega-pulse methylprednisolone in severe therapy-resistant alopecia areata (publication corresponding to NCT01167946) |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Cohort | Dermato-Endocrinology | Medium-dose prednisolone pulse therapy in alopecia areata |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohort | Dermatologic Therapy | Retrospective analysis of methylprednisolone alone vs with methotrexate in extensive alopecia areata |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohort | Journal der Deutschen Dermatologischen Gesellschaft (JDDG) | Sequential high- and low-dose systemic corticosteroid therapy for severe childhood alopecia areata |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Review of pediatric pulse-dose corticosteroid dosing and administration in alopecia areata |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Review | The Journal of Dermatological Treatment | Durable remission of severe alopecia areata with dexamethasone oral mini-pulse in patients ineligible for JAK inhibitors |

---

## UK Market Information

The evidence pack records **0 marketing authorisations** and a market status of **"Not marketed"** for this drug entry. No licence numbers, product names, or approved indication text are available in `taiwan_regulatory.licenses`.

> **Caveat:** Prednisolone is a long-established, widely-used oral and topical corticosteroid in UK clinical practice under multiple branded and generic products (per BNF classification: corticosteroid, systemic). The "Not marketed / 0 licenses" result above most likely reflects an incompleteness in this evidence pack's regulatory data source rather than actual UK unavailability. This should be verified directly against the MHRA product register before any decision is finalised.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(This evidence pack's `key_warnings`, `contraindications`, and drug interaction fields are all data gaps — flagged as DG001, Blocking severity — meaning no safety pre-screening (S1) can currently be completed from this pack alone.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a completed Phase 4 trial and a placebo-controlled publication directly supporting pulse corticosteroid therapy (methylprednisolone/prednisolone class) in severe, treatment-resistant alopecia areata, alongside multiple supporting reviews and cohort studies — consistent with the L2 evidence level. However, critical safety data (SmPC warnings, contraindications, DDI) and UK licensing status are unresolved data gaps that must be closed before this can move past guarded evaluation.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC warnings and contraindications (DG001, Blocking — required before any S1 safety pre-screening)
- Confirmed mechanism of action documentation from DrugBank (DG002, High)
- Verification of actual UK marketing authorisation status directly against the MHRA register (the "0 licences / not marketed" result in this pack appears inconsistent with prednisolone's known widespread UK use)
- A monitoring plan for long-term/pulse systemic corticosteroid use (bone density, blood glucose, infection risk, adrenal suppression) specific to dermatology prescribing in alopecia areata
- Clarification of prednisolone's positioning relative to newer JAK inhibitor therapies now used in severe alopecia areata
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

