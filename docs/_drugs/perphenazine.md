---
layout: default
title: Perphenazine
parent: Model Prediction Only (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Perphenazine
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

# Perphenazine: From Antipsychotic Therapy to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Perphenazine is a typical (first-generation) antipsychotic (phenothiazine class, D2/5-HT2A antagonist); this evidence pack does not document its originally approved indication (original_indications field empty, MOA marked as a data gap pending DrugBank confirmation). The TxGNN model's top-ranked prediction is **Retinal Dystrophy with or without Extraocular Anomalies**, but on review this is supported by **0 clinical trials** and **15 publications, none of which mention perphenazine** — the evidence pack's own analysis flags this as likely knowledge-graph noise rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in this evidence pack (original_indications empty; TFDA label extraction pending — DG001) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.96% (raw rank 825) |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for perphenazine is not available in this pack (DG002, MOA marked as data gap). Based on information embedded elsewhere in this evidence pack (see the anxiety-disorder candidate's rationale), perphenazine is understood to act as a D2/5-HT2A receptor antagonist with additional H1/α1-adrenergic antagonism — consistent with its known use as a typical antipsychotic/phenothiazine. No original indication text was supplied, so the drug's approved therapeutic history cannot be independently verified here.

There is no biologically plausible relationship between this mechanism and retinal dystrophy with or without extraocular anomalies, which is predominantly a group of inherited disorders caused by photoreceptor or retinal-pigment-epithelium gene defects. The evidence pack's own mechanistic assessment reaches the same conclusion: it explicitly states there is "no known mechanistic link" between the two.

Having reviewed all 15 associated publications, none reference perphenazine, its pharmacological class, or any drug treatment for the ophthalmological conditions discussed — they cover orbital infections, diplopia, congenital ptosis, lens anomalies, cryptophthalmia, and related structural eye disorders. This pattern is best interpreted as keyword co-occurrence noise in the underlying knowledge graph rather than substantive biological evidence, despite the high TxGNN confidence score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*Note: none of the citations below mention perphenazine or its pharmacological class directly. They are general ophthalmology literature that co-occurs with the predicted disease term in the knowledge graph and are presented here for transparency, not as supporting evidence — consistent with the "Hold" recommendation above.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections secondary to sinusitis; no drug treatment discussion relevant to perphenazine |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Diagnostic approach to diplopia; not disease- or drug-specific |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis pathophysiology and evaluation |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape and associated syndromes |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler vitreoretinal degeneration syndrome complex |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging features of pediatric ocular pathologies (congenital/developmental) |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | Clinical features and management of orbital arteriovenous malformations |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Unilateral cryptophthalmia case series |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | Congenital trochlear-oculomotor synkinesis case |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optom Vis Sci | Congenital extraocular muscle fibrosis with variable synergistic divergence |

---

## UK Market Information

Perphenazine currently holds **no UK marketing authorisations** in this evidence pack (`market_status`: Not Marketed, `total_licenses`: 0). No product-level licence data is available to summarise in this report.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications, and drug-interaction data in this evidence pack are all marked as data gaps or "not found" — DG001 remains a blocking gap for any formal safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for perphenazine (retinal dystrophy with or without extraocular anomalies) has no supporting clinical trials, no mechanistically relevant literature, and the evidence pack's own analysis identifies it as likely computational noise rather than a genuine signal (Evidence Level L5).

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/MHRA label warnings and contraindications) — currently blocking any S1 safety screening
- Resolve DG002 (confirm mechanism of action via DrugBank API)
- Obtain documented original indication data for perphenazine to enable a proper original-vs-predicted indication comparison
- **Separately note:** this evidence pack also contains a materially stronger candidate — *anxiety disorder* (rank 10, Evidence Level L2, two clinical trials, 20 publications including several historical RCTs of perphenazine combinations) — which is rated "Proceed with Guardrails" and warrants its own dedicated evaluation report rather than being assessed alongside this Hold-rated candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

