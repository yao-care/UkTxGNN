---
layout: default
title: Quetiapine
parent: Moderate Evidence (L3-L4)
nav_order: 492
evidence_level: L4
indication_count: 10
---

# Quetiapine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

Using the pharmaceutical-report-writing instructions in this system prompt directly (no additional skill needed for this task — it's a self-contained formatting job).

**Note on candidate selection:** TxGNN's rank‑1 prediction (`predicted_indications[0]`, retinal dystrophy with/without extraocular anomalies) is explicitly flagged in its own `repurposing_rationale` as a likely **false positive** — none of its 15 associated PubMed records mention quetiapine, and there is no plausible mechanistic link. Eight of the ten ranked candidates (ranks 1–7, 9–10) share this pattern: rare structural/genetic disorders with zero clinical trials, zero literature, and evidence level L5. Presenting the mechanical top-score candidate as "the" prediction would be misleading for a clinical audience. This report therefore centres on **rank 8 (trichotillomania)**, the only candidate with actual supporting literature and a mechanistically coherent rationale.

---

# Quetiapine: From Schizophrenia/Bipolar Disorder (established use) to Trichotillomania

## One-Sentence Summary

> Quetiapine is a well-established atypical antipsychotic; this evidence pack does not itself contain confirmed UK original-indication or MHRA label data. Among ten TxGNN-predicted candidates, the only one with any real supporting evidence is **Trichotillomania (hair-pulling disorder)**, backed by **case reports and narrative reviews** but **no completed clinical trials**. The remaining nine candidates (including the model's highest-scoring prediction) have no literature or trial support and are assessed as likely model artefacts.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (Data Gap); established clinical use is schizophrenia and bipolar disorder |
| Predicted New Indication | Trichotillomania (hair-pulling disorder) |
| TxGNN Prediction Score | 99.38% (rank 8 of ranked candidates) |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on established pharmacological knowledge, quetiapine is a second-generation (atypical) antipsychotic of the dibenzothiazepine class, with antagonist activity at serotonin 5-HT2A, dopamine D2, and histamine H1 receptors. Its efficacy in schizophrenia and bipolar disorder is well established in clinical practice, though the specific UK-approved indication wording was not supplied in this pack.

Trichotillomania (hair-pulling disorder) is classified among obsessive-compulsive and related disorders. Dysregulation of serotonergic and dopaminergic signalling has been implicated in impulse-control symptoms, which provides a plausible mechanistic rationale for exploring quetiapine in this condition. However, this rationale is theoretical: the literature below consists of case reports and reviews rather than controlled trials, and one publication (PMID 11212595) reports quetiapine **exacerbating** obsessive-compulsive symptoms in a patient with co-morbid trichotillomania — an important safety signal that cuts against, not for, the hypothesis.

The other nine TxGNN-ranked candidates (retinal dystrophy, congenital disorder of glycosylation, hydranencephaly, 17p13.3 microdeletion syndrome, polymicrogyria syndromes, several rare myopia subtypes, Charcot-Marie-Tooth disease type 1G) are structural, genetic, or developmental disorders with no plausible link to quetiapine's receptor pharmacology, no supporting literature, and no clinical trials. These are assessed as knowledge-graph co-occurrence artefacts rather than genuine repurposing signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | International Journal of Dermatology | Large-scale review noting the lack of established treatment guidelines for trichotillomania and calling for better clinician education on pharmacological options |
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review | Psychiatry | Overview of trichotillomania pharmacotherapy; describes a 33-year-old woman with a favourable clinical response to quetiapine |
| [17484394](https://pubmed.ncbi.nlm.nih.gov/17484394/) | 2006 | Review | The Journal of Practical Nursing | General treatment overview of trichotillomania |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case Report | Revista Brasileira de Psiquiatria | Case report describing use of quetiapine for treatment of trichotillomania |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case Report | Psychosomatics | Case report and literature review of recurrent Rapunzel syndrome and trichotillomania |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case Report/Review | Journal of Psychiatry & Neuroscience | **Safety signal**: case of quetiapine exacerbating obsessive-compulsive symptoms in a patient with OCD, trichotillomania, delusional disorder and bipolar disorder; reviews antipsychotic-induced OCS |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case Report | Case Reports in Psychiatry | Trichotillomania as a manifestation of dementia; different population (not a quetiapine-treatment report) |

## UK Market Information

This evidence pack records quetiapine as **not marketed** in this jurisdiction (0 marketing authorisations, no license records available). No product/authorisation table could be generated from the supplied data.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags TFDA/product-label warnings and contraindications as a Blocking data gap — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for quetiapine in trichotillomania is limited to case reports and narrative reviews (Evidence Level L4) with no completed clinical trials, and includes at least one report of symptom worsening rather than benefit. Separately, a **Blocking** data gap (missing product-label warnings/contraindications) prevents this candidate from entering Stage 1 safety screening regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve Blocking gap DG001: obtain SmPC/product label warnings and contraindications
- Resolve High-priority gap DG002: confirm mechanism of action and original approved indication(s) via DrugBank/regulatory source
- Identify or commission a prospective controlled study of quetiapine for trichotillomania, given current evidence is case-report level only
- Treat the remaining nine TxGNN candidates as low priority; they show no literature or trial support and are likely knowledge-graph artefacts rather than genuine repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

