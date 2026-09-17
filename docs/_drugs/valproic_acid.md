---
layout: default
title: Valproic Acid
parent: High Evidence (L1-L2)
nav_order: 608
evidence_level: L2
indication_count: 10
---

# Valproic Acid
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

# Valproic Acid: From Epilepsy to Visual (Photosensitive) Epilepsy

## One-Sentence Summary

Valproic acid is a long-established broad-spectrum antiepileptic, historically used for generalised and focal epilepsy (and also for bipolar disorder and migraine prophylaxis). Among the candidates identified by TxGNN in this Evidence Pack, **Visual Epilepsy** (photosensitive/light-induced reflex epilepsy) is the best-supported new indication, with **4 clinical trials** and **20 publications** currently informing this direction, although none of the trials targets visual epilepsy as its primary endpoint.

> **Note on selection**: TxGNN's raw top-ranked candidate for this drug, *trigeminal nerve neoplasm*, was reviewed and excluded — the evidence pack itself flags it as a likely model artefact (no clinical trials, a single unrelated case-series on Sturge-Weber syndrome, and no plausible mechanistic link to tumour biology). Visual epilepsy was the strongest of the remaining candidates and is used here as the primary focus of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalised and focal seizures); also used for bipolar disorder (mania) and migraine prophylaxis. Formal UK indication wording is not available in this dataset (data gap). |
| Predicted New Indication | Visual Epilepsy (photosensitive/light-induced reflex epilepsy) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (per current dataset — see note below)* |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

\*Valproic acid is a decades-old, widely used antiepileptic internationally (e.g. UK brand Epilim). A "not marketed / 0 licences" result in this dataset most likely reflects incomplete regulatory data capture rather than genuine absence from the UK market, and should be verified directly against the MHRA product database and BNF before any commercial decision is made.

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation was not available in this Evidence Pack (data gap). Based on the mechanistic rationale accompanying the prediction, valproic acid acts through a broad combination of pathways: voltage-gated sodium channel blockade, T-type calcium channel inhibition, and enhancement of GABAergic (inhibitory) neurotransmission relative to glutamatergic (excitatory) signalling. This multi-target profile is what underlies its long-standing role as a first-line agent for idiopathic generalised epilepsies, including juvenile myoclonic epilepsy (JME) — a syndrome in which photosensitivity/visual triggers are common.

Visual (photosensitive) epilepsy sits within this same idiopathic generalised epilepsy spectrum rather than being a mechanistically distinct disease. Reflex seizures provoked by flickering light or visual patterns share the same underlying cortical hyperexcitability and thalamocortical circuit abnormalities that valproic acid is already known to suppress in generalised epilepsy. This makes the TxGNN prediction biologically coherent, even though no trial in this pack has enrolled patients specifically selected for visual/photosensitive triggers — the supporting evidence is largely extrapolated from valproic acid's established efficacy across the broader reflex/generalised epilepsy spectrum (e.g. neuroprotection and seizure prevention after brain injury, and management of progressive myoclonic epilepsies that frequently exhibit photosensitivity).

By contrast, the raw top-ranked TxGNN candidate — trigeminal nerve neoplasm — has no such mechanistic bridge: valproic acid's established actions (GABAergic/sodium-channel/HDAC-related effects) relate to neuronal excitability and epigenetic regulation, not tumour growth control in this specific context, and the single associated publication does not concern oncology at all. This candidate was therefore treated as noise rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07226141](https://clinicaltrials.gov/study/NCT07226141) | Phase 1/2 | Not yet recruiting | 28 | Evaluates valproate as adjunct therapy for residual amblyopia (visual pathway plasticity) in children aged 8–17; not a seizure trial but tests VPA's effect on visual system plasticity. |
| [NCT02027987](https://clinicaltrials.gov/study/NCT02027987) | Phase 1 | Unknown | 160 | Neuroprotection and epilepsy-prevention study of VPA after severe traumatic brain injury; supports VPA's broad-spectrum antiseizure and neuroprotective role. |
| [NCT00639119](https://clinicaltrials.gov/study/NCT00639119) | Phase 2 | Unknown | 16 | Trial of ropinirole (not VPA) in Unverricht-Lundborg progressive myoclonic epilepsy, a condition strongly associated with light-sensitive seizures; VPA is noted as a mainstay comparator treatment. |
| [NCT00021866](https://clinicaltrials.gov/study/NCT00021866) | N/A | Completed | 331 | NEAD study: examines neurodevelopmental effects of antiepileptic drugs (including VPA) taken during pregnancy; not a treatment-efficacy trial for visual epilepsy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Current Neuropharmacology | Comprehensive review of VPA's molecular mechanisms (GABAergic/glutamatergic modulation, ion channel effects) underpinning its antiepileptic and anti-reflex-seizure activity. |
| [30734897](https://pubmed.ncbi.nlm.nih.gov/30734897/) | 2019 | Guideline/Review | Paediatric Drugs | Practical guide to childhood absence epilepsy; confirms VPA as an effective option within the idiopathic generalised epilepsy spectrum that includes photosensitive phenotypes. |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | New England Journal of Medicine | Overview of initial seizure management in adults, situating VPA among first-line broad-spectrum agents. |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Review | Future Oncology | Discusses antiseizure (and possible antineoplastic) effects of VPA in glioma-related epilepsy, illustrating its broad-spectrum seizure control across aetiologies. |
| [34663708](https://pubmed.ncbi.nlm.nih.gov/34663708/) | 2021 | Cohort study | Neurosciences (Riyadh) | Evaluates efficacy and safety of VPA in children under 2 years with epilepsy, supporting its broad applicability across seizure types. |
| [37037506](https://pubmed.ncbi.nlm.nih.gov/37037506/) | 2023 | Review | Brain and Nerve | Review of current clinical practice guidelines for epilepsy treatment, including VPA's role as a standard antiseizure medication (ASM). |
| [24798217](https://pubmed.ncbi.nlm.nih.gov/24798217/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Reviews pharmacotherapy for generalised tonic-clonic seizures, a seizure type commonly triggered by photosensitivity, with VPA as a mainstay treatment. |
| [26715390](https://pubmed.ncbi.nlm.nih.gov/26715390/) | 2016 | Pharmacokinetic study | CNS Drugs | Evaluates pharmacokinetics and clinical utility of continuous-infusion VPA in acute seizure management. |
| [27855134](https://pubmed.ncbi.nlm.nih.gov/27855134/) | 2016 | Pharmacogenetic study | Therapeutic Drug Monitoring | Examines genetic factors affecting VPA plasma levels and treatment response in children with epilepsy. |
| [16302877](https://pubmed.ncbi.nlm.nih.gov/16302877/) | 2005 | Review | Epilepsia | Reviews photosensitivity in idiopathic generalised epilepsies — the disease category most directly relevant to visual/photosensitive epilepsy — describing seizure types and treatment context. |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: This Evidence Pack flags safety data as a Blocking data gap — key warnings, contraindications, and drug–drug interaction data specific to this dataset could not be retrieved. Given valproic acid carries well-documented, clinically significant risks — including teratogenicity/pregnancy prevention programme requirements, hepatotoxicity, and hyperammonaemia — full SmPC review is essential before any clinical use is considered.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Visual (photosensitive) epilepsy sits within the same idiopathic generalised epilepsy spectrum in which valproic acid is already a first-line, decades-proven treatment; the mechanistic rationale is strong even though no trial has directly enrolled patients selected specifically for visual/photosensitive seizure triggers. The evidence base is indirect (extrapolated from broader epilepsy and reflex-epilepsy literature) rather than disease-specific, which supports cautious progression rather than unconditional endorsement. The originally top-ranked TxGNN candidate (trigeminal nerve neoplasm) was excluded as low-confidence noise, and is not the basis for this recommendation.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent product labelling data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Verification of current UK marketing authorisation status directly via MHRA/BNF, as the "not marketed / 0 licences" result in this dataset appears inconsistent with valproic acid's known long-standing UK availability
- Results from NCT07226141 (Phase 1/2, not yet recruiting) once available, as it is the only trial directly probing VPA's effect on a visual-system endpoint
- A dedicated pilot study or case series specifically enrolling patients with visual/photosensitive-triggered seizures, to close the gap between the broad generalised-epilepsy evidence base and this specific reflex phenotype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

