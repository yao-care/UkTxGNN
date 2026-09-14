---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Phenytoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Phenytoin: From Epilepsy to Trigeminal Neuralgia

> **Methodology note:** TxGNN's top-ranked candidate for this drug ("trigeminal nerve neoplasm", score 99.99%) is flagged in the Evidence Pack itself as a likely knowledge-graph artefact — the model appears to have confused "neuralgia" with "neoplasm" for the trigeminal nerve entity, and no oncology-relevant evidence was returned. As it has no clinical rationale, it is not carried forward. This report instead focuses on **Trigeminal Neuralgia** (rank 9), the candidate with the strongest and most clinically coherent supporting evidence among the ten predictions in this pack.

## One-Sentence Summary

Phenytoin is a long-established sodium-channel-blocking antiepileptic medicine; the Evidence Pack does not include structured original-indication text or mechanism-of-action data (flagged as data gaps DG001/DG002). Of the ten TxGNN-predicted indications supplied, **Trigeminal Neuralgia** is the only one with a coherent mechanism and real clinical use, supported by **1 clinical study** and **10+ relevant publications**, including a European clinical guideline and retrospective cohorts of intravenous phenytoin used as rescue therapy for acute pain crises.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in Evidence Pack (data gap DG001); phenytoin is a well-established antiepileptic/anticonvulsant |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| UK Market Status | Not Marketed (per Evidence Pack; see market information note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known pharmacological information, phenytoin is a voltage-gated sodium-channel blocker that stabilises neuronal membranes and suppresses high-frequency repetitive firing — the same principle underlying its long-standing use across multiple epileptic seizure types.

Trigeminal neuralgia (TN) is pathophysiologically a paroxysmal hyperexcitability disorder: ectopic, high-frequency discharges arise in the trigeminal nerve root entry zone, typically due to neurovascular compression and focal demyelination. This is mechanistically analogous to epileptic discharge, which is why carbamazepine — a structurally and mechanistically related sodium-channel blocker — is the established first-line treatment for TN. Phenytoin's TxGNN association is therefore consistent with a recognised drug-class effect rather than a purely computational artefact.

Notably, this is not solely a theoretical prediction: intravenous phenytoin is already used off-label in clinical practice as rescue therapy for acute TN pain exacerbations, particularly when oral first-line agents are ineffective or patients cannot tolerate oral intake. A completed prospective study and multiple retrospective cohorts (144 and smaller case series) describe this practice, lending real-world corroboration to the model's prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Completed | 15 | Prospective systematic study of IV phenytoin for acute exacerbations of trigeminal neuralgia, addressing the problem of oral prophylactic drugs (carbamazepine/oxcarbazepine) being impractical during severe flares |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology guideline on diagnosis and management of TN |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort (retrospective, n=144) | Cephalalgia | IV lacosamide and phenytoin evaluated for effectiveness/safety in acute TN exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Cohort/Case series | Headache | Retrospective analysis of responses to IV phenytoin as acute rescue treatment for TN crisis |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review (comparative) | Journal of Pain Research | Critical comparison of phenytoin and carbamazepine evidence bases in TN |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview of TN pathophysiology and pharmacological treatment options |
| [39993829](https://pubmed.ncbi.nlm.nih.gov/39993829/) | 2024 | Review | Clinical Medicine & Research | In-hospital management approaches for acute TN pain crises |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review (evidence synthesis) | BMJ Clinical Evidence | Summary of TN clinical presentation and treatment evidence |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptic drugs in management of cluster headache and TN |
| [15062534](https://pubmed.ncbi.nlm.nih.gov/15062534/) | 2004 | Review | Neurologic Clinics | Clinical features and treatment of TN and glossopharyngeal neuralgia; antiepileptics noted as most effective agents |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | Clinical overview of TN diagnosis, mechanisms, and management options |

## UK Market Information

The Evidence Pack records this drug as **not marketed**, with **zero** marketing authorisations on file. No licence records were supplied to populate a market information table.

**Caveat for reviewers:** this dataset field originates from a template shared across country projects and may not have been fully localised for the UK. Phenytoin sodium is, in reality, a long-established UK-licensed medicine (e.g., Epanutin, various generic phenytoin sodium capsules/injections) used for epilepsy. Before any decision is finalised, market status should be verified directly against the MHRA product register and current BNF entry rather than relying on this field.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Additional context from the literature search (not structured safety data):* publications retrieved during evidence gathering for this and related predicted indications flagged known phenytoin-associated risks relevant to IV/rescue use, including paradoxical seizures with rapid IV infusion, thrombocytopenia, peripheral neuropathy, and EMPACT syndrome (erythema multiforme associated with phenytoin and cranial radiotherapy). These are illustrative signals from the literature rather than a substitute for the SmPC.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The sodium-channel-blocking mechanism is pharmacologically coherent with TN pathophysiology, and IV phenytoin already has documented off-label real-world use as rescue therapy for acute exacerbations (one completed prospective study, retrospective cohorts, and guideline-level discussion). However, evidence is limited to observational/single-arm data with no RCTs, and phenytoin is not positioned as first-line therapy (carbamazepine/oxcarbazepine remain standard).

**To proceed, the following is needed:**
- TFDA/MHRA product labelling — warnings, contraindications and DDI data (data gap DG001, currently blocking)
- Confirmed mechanism of action documentation from DrugBank or SmPC (data gap DG002)
- Verification of actual UK licensing status directly from the MHRA register/BNF
- A defined guardrail protocol for off-label IV use in acute TN crises (specialist neurology oversight, cardiac/infusion monitoring, patient selection criteria for oral-therapy failure)
- Consideration of prospective comparative data given the absence of RCT evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

