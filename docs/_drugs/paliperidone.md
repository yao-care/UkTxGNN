---
layout: default
title: Paliperidone
parent: High Evidence (L1-L2)
nav_order: 441
evidence_level: L2
indication_count: 10
---

# Paliperidone
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

Using the evidence pack's own repurposing rationale to select the reportable candidate: TxGNN's top 9 ranked predictions (retinal dystrophy, X-linked myopia, hydranencephaly, CDG, CMT1G, etc.) are explicitly flagged in the evidence pack as biologically implausible KG-embedding noise with no clinical or literature support and a "Hold" recommendation. The only candidate with mechanistic coherence, real trial data, and a "Proceed with Guardrails" call is rank 10 (treatment-refractory schizophrenia). The report below is built on that candidate.

---

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

> Paliperidone is an established atypical antipsychotic (D2/5-HT2A receptor antagonist, the active metabolite of risperidone) used for schizophrenia-spectrum disorders.
> The TxGNN model's top nine ranked predictions (e.g. retinal dystrophy, X-linked myopia, hydranencephaly) were reviewed and excluded as biologically implausible model noise with no supporting evidence.
> The most credible signal identified is **Treatment-Refractory Schizophrenia**, supported by **4 clinical trials** and **2 publications**, though robust head-to-head evidence specific to the refractory population remains limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per drug-class mechanistic data in evidence pack; structured original-indication field is a data gap) |
| Predicted New Indication | Treatment-Refractory Schizophrenia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for paliperidone is currently a data gap in this evidence pack (DG002, High severity). However, evidence embedded in the trial/literature rationale confirms paliperidone is the active metabolite of risperidone, acting as a D2/5-HT2A receptor antagonist — a core member of the atypical antipsychotic class already used to treat schizophrenia.

Treatment-refractory schizophrenia is not a distinct disease but a clinically defined subgroup of schizophrenia that has failed to respond adequately to standard antipsychotic therapy. Because paliperidone already belongs to the therapeutic class used for schizophrenia broadly, extension of its use into the refractory subgroup is a plausible, low-novelty repurposing hypothesis rather than a cross-mechanism prediction.

That said, current clinical guidelines position clozapine as the only agent with a specific, guideline-endorsed indication for treatment-refractory schizophrenia, including a reduction in suicidal behaviour risk. Paliperidone's specific role in this refractory population is therefore not yet well established and requires stronger head-to-head comparative evidence before it can be considered an equivalent option.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating effectiveness of paliperidone palmitate across three schizophrenia patient subgroups |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Open-label RCT comparing aripiprazole vs paliperidone/risperidone using multi-omics data in first-episode psychosis; paliperidone is one comparator arm |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Compared clozapine vs non-clozapine antipsychotics (may include paliperidone) on inflammatory markers in treatment-resistant schizophrenia; terminated with minimal enrolment |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluates pharmacotherapy combined with recovery-oriented programmes for treatment-resistant schizophrenia and bipolar disorder; drug-specific relevance to paliperidone unconfirmed |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Reviews current psychopharmacological evidence for schizoaffective disorder; notes absence of disorder-specific treatment guidelines, reliance on antipsychotics generally |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Reviews evidence-informed psychopharmacology for early-onset schizophrenia spectrum disorders in adolescents, including dosing and switching considerations |

---

## UK Market Information

Paliperidone currently holds **no UK marketing authorisation** in this evidence pack (market status: Not marketed; 0 licences on record). No product-level licensing table is available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: Key warnings, contraindications and drug-interaction data are recorded as blocking data gaps (DG001) in this evidence pack and could not be evaluated for this report.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paliperidone's class-level mechanism supports plausible use across the schizophrenia spectrum, and one completed Phase 4 study (NCT01860781) shows real-world effectiveness data; however, evidence specific to the *treatment-refractory* subgroup is limited to small, terminated, or status-unknown trials, and clozapine remains the guideline-preferred option for this population.

**To proceed, the following is needed:**
- Resolution of the blocking safety data gap (DG001): TFDA/MHRA labelling, warnings and contraindications
- Detailed mechanism-of-action documentation from DrugBank (DG002)
- Confirmation of UK marketing authorisation pathway, since paliperidone is currently not marketed in this dataset
- Head-to-head RCT evidence comparing paliperidone against clozapine specifically in the treatment-refractory schizophrenia population
- Follow-up on NCT06060886 and NCT07047651 completion to clarify paliperidone-specific outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

