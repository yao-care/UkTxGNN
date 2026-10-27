---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including generalised tonic-clonic seizures…"
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenytoin
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

## Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenytoin is an established anticonvulsant, originally used to treat epilepsy and related seizure disorders.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **no clinical trials** and only **2 publications** (neither about treating a neoplasm), so this prediction is not supported by evidence. The data compiled for this report indicate that the closely related, clinically plausible prediction is **trigeminal neuralgia** (rank 9).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (including generalised tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome and status epilepticus) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

The approved indication text was not available in the UK licence record, so the original indications above come from the TxGNN knowledge graph.

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Phenytoin is a well-known antiepileptic whose action is generally attributed to blockade of voltage-gated sodium channels. Its efficacy in epilepsy is established.

For **trigeminal nerve neoplasm**, the prediction is **not mechanistically convincing**. The high score likely reflects network proximity to trigeminal neuralgia and seizure-related nodes rather than any antitumour effect. Sodium channel blockade might relieve neuropathic pain symptoms, but there is no plausible mechanism for treating the neoplasm itself. The two retrieved papers concern trigeminal neuralgia and Sturge-Weber syndrome, not neoplasm treatment.

The more credible repurposing signal is for **trigeminal neuralgia** (score 99.97%, rank 9). There, phenytoin reduces ectopic high-frequency firing in the trigeminal nerve, the same mechanism as carbamazepine, the first-line drug. Phenytoin has been mentioned as an alternative or add-on, and intravenous use has been studied for acute exacerbations.

Other predictions (reflex seizures such as audiogenic, reading, startle, eating, micturition-induced and thinking seizures) are theoretically plausible as seizure types, but have little or no direct human evidence. Beta-ketothiolase deficiency has no recognisable mechanistic link and is likely a network artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature for the top-ranked prediction (trigeminal nerve neoplasm):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; does not address neoplasm |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 cases of Sturge-Weber syndrome, covering clinical features and treatment response; not about neoplasm |

Supporting literature for the related prediction, trigeminal neuralgia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on managing trigeminal neuralgia |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | J Pain Res | Compares phenytoin and carbamazepine in trigeminal neuralgia, contrasting marketing-based with evidence-based treatment |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort | Cephalalgia | Retrospective analysis of 144 cases of IV lacosamide and phenytoin for acute exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Cohort | Headache | Retrospective cohort of IV phenytoin as acute rescue treatment in trigeminal neuralgia crisis |
| [22592741](https://pubmed.ncbi.nlm.nih.gov/22592741/) | 2012 | Systematic review | Cochrane Database Syst Rev | Phenytoin for neuropathic pain and fibromyalgia; notes occasional use in intractable trigeminal neuralgia |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Pathophysiology and pharmacological treatments of trigeminal neuralgia |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010Q0AAAAAA | Phenytoin sodium capsules 100 mg | Capsule | Not stated in the licence record |

The identifier shown is the code in the data compiled for this report, and it is not in the usual PL number format. It is a single-ingredient product with a valid status. Please verify the licence details against the MHRA register and the BNF (antiepileptic drugs section).

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** the graph links phenytoin to caution or contraindication in conditions including:
- Cardiac: long QT syndrome, torsades de pointes, hypotensive disorder
- Hepatic and renal: liver disease, liver failure, hepatic coma/encephalopathy, kidney disease, gallbladder disease
- Metabolic: porphyria (including inherited forms), diabetes mellitus, diabetic ketoacidosis, hyperglycaemia
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Other: systemic lupus erythematosus, sleep apnoea syndromes, substance abuse/dependence

These are knowledge-graph associations and should be checked against the SmPC.

**Drug interactions:** 100 interactions were identified; the main examples listed (mostly moderate severity) include:
- Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, albiglutide
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Acid suppressants: omeprazole, famotidine, ranitidine
- Antimicrobials: doxycycline, metronidazole
- Others: bupropion, aprepitant, morphine, cholecalciferol, calcifediol
- Acetylsalicylic acid was classed as minor.

Literature also describes phenytoin-associated thrombocytopenia, hyperglycaemia/diabetic ketoacidosis, and erythema multiforme in patients receiving cranial radiotherapy (EMPACT syndrome). Label-level warnings were not available, so please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, has no plausible antitumour mechanism, no trials and no supporting literature, so the high TxGNN score appears to be a network artefact. The related prediction of trigeminal neuralgia has some observational and review-level support (L3), but carbamazepine and oxcarbazepine remain preferred, so phenytoin would at most be a second-line or acute-setting option.

**To proceed, the following is needed:**
- Do not pursue trigeminal nerve neoplasm further unless new mechanistic or clinical evidence emerges
- If pursuing trigeminal neuralgia, a focused question on IV phenytoin for acute exacerbations, with a prospective or controlled study design
- Mechanism of action data and label-level warnings and contraindications from the SmPC and BNF
- Confirmation of the UK marketing authorisation details (PL number, dosage form, approved indication)
- A safety plan covering narrow therapeutic index, interactions, and the cardiac, hepatic and haematological risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

