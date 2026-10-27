---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ambrisentan: predicted new indication Pulmonary arteriovenous malformation (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "Ambrisentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Ambrisentan
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

## Ambrisentan: From Pulmonary Arterial Hypertension to PAH Associated with Connective Tissue Disease
{: .text-alpha }

## One-Sentence Summary

Ambrisentan is an endothelin receptor antagonist, originally used to treat pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **PAH associated with connective tissue disease (CTD-PAH)**,
with **2 clinical trials** and **19 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (taken from the knowledge-graph indication data, as no approved indication text is recorded in the licence data) |
| Predicted New Indication | Pulmonary arteriovenous malformation (top-ranked by TxGNN); the most clinically supported prediction is PAH associated with connective tissue disease (see below) |
| TxGNN Prediction Score | 99.41% (top-ranked prediction); 99.30% for CTD-PAH |
| Evidence Level | L2 (for CTD-PAH); L4 for the top-ranked prediction |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails (CTD-PAH); Hold (top-ranked pulmonary AVM) |

**Note on prediction selection:** The highest-scoring prediction, pulmonary arteriovenous malformation (score 99.41%), has only one case report and no plausible mechanistic rationale. This report therefore focuses on **PAH associated with connective tissue disease**, the prediction with the strongest supporting evidence. Other predictions are summarised briefly in the conclusion.

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, ambrisentan is a selective endothelin-A (ET-A) receptor antagonist. Blocking this receptor reduces pulmonary vasoconstriction and vascular remodelling, which is the basis of its use in PAH.

CTD-PAH, including PAH associated with systemic sclerosis, is a recognised subgroup of Group 1 PAH. The same endothelin-driven vasoconstriction and remodelling processes are involved, so the mechanism is directly applicable. CTD-PAH patients are already treated within the broader PAH population, so use is effectively on-label. The prediction is therefore best viewed as confirming an existing clinical use rather than a wholly new indication.

The evidence is limited by small trial sizes. One trial tested a combination (ambrisentan plus tadalafil), which cannot isolate the effect of ambrisentan alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | EDITA: proof-of-concept, double-blind, placebo-controlled study of early treatment in borderline PAH associated with systemic sclerosis (single centre) |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | 36-week open-label, single-group study of ambrisentan plus tadalafil in scleroderma-spectrum PAH; outcomes include 6-minute walk distance, NYHA class and haemodynamics |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review/meta-analysis | Intern Emerg Med | Meta-analysis of RCT subgroup data on treatments for CTD-PAH |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Meta-analysis of clinical trials in CTD-PAH, where the optimal treatment is not yet established |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | Subgroup analysis (AMBITION) | Ann Rheum Dis | Initial ambrisentan plus tadalafil combination in CTD-PAH |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Post hoc analysis (AMBITION) | Ann Rheum Dis | Initial combination compared with monotherapy in CTD-PAH and the systemic sclerosis subgroup |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Subgroup analysis (ARIES-E) | Respir Med | 3-year efficacy and safety of ambrisentan in CTD-PAH |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | Clinical study | Am J Respir Crit Care Med | Up-front ambrisentan and tadalafil combination in scleroderma-associated PAH |
| [22777623](https://pubmed.ncbi.nlm.nih.gov/22777623/) | 2012 | Open-label pilot (cohort) | Arthritis Rheum | Ambrisentan in exercise-induced pulmonary hypertension in systemic sclerosis |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Review | Ther Adv Respir Dis | Ambrisentan is approved for idiopathic, heritable and connective tissue disease-associated PAH, with improved exercise capacity and haemodynamics |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Overview of diagnosis and treatment of PAH |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treating PAH associated with connective tissue disease |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205010X0AAAAAA | Ambrisentan Tab 5 mg | Tablet (not recorded in licence data) | Not recorded in the licence data |

The licence data list one valid single-ingredient authorisation. Manufacturer and approved indication text are not recorded, so please consult the MHRA register, the SmPC, the BNF and any NICE guidance for the authorised indications.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** congestive heart failure, anaemia (including macrocytic anaemia) and pulmonary veno-occlusive disease.
- **Drug interactions:** 100 interactions were identified. Those listed as moderate include canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, eliglustat and naltrexone. Minor interactions include clarithromycin, miconazole and omeprazole. For HIV-associated PAH in particular, interactions with antiretrovirals need to be reviewed.
- **Teratogenicity:** Ambrisentan is teratogenic (noted in the data for the Dandy-Walker prediction), so pregnancy precautions apply to any new use.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (CTD-PAH)

**Rationale:**
Two completed trials (a Phase 2 and a Phase 4) and several meta-analyses and subgroup analyses of larger PAH trials support ambrisentan in CTD-PAH. The trials are small, and one tested a combination. The evidence level is therefore L2, not L1.

**Other predictions:**
- PAH associated with congenital heart disease (L3): Proceed with Guardrails. Evidence is a dedicated cohort study and reviews; there is no registered trial.
- PAH associated with HIV infection (L4): Research question. Evidence consists of small series and a registry only.
- PAH associated with schistosomiasis or chronic haemolytic anaemia (L5): Research question. Model prediction only.
- Pulmonary arteriovenous malformation, malformation syndrome with odontal and/or periodontal component, hypotrichosis simplex of the scalp, hypertrichosis and Dandy-Walker malformation syndrome: Hold. There is no plausible mechanism, and some of these may be model artefacts.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Full UK licence details, including approved indication text and dosage form
- Label-based warnings and contraindications from the SmPC and BNF
- Larger controlled studies of ambrisentan monotherapy in CTD-PAH
- Review of drug interactions relevant to the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

