---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dipyridamole: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
---

# Dipyridamole
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

# Dipyridamole: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilator drug, listed in the knowledge graph under atrial fibrillation as its original indication.
The TxGNN model's top-ranked prediction is **Prinzmetal angina**, but this is supported by **no clinical trials** and only **10 low-tier publications**, so it is not recommended for progression.
Among the other predictions, **stroke disorder** and **transient ischaemic attack** have far stronger evidence (including the large ESPRIT trial), though these are already established uses rather than novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (knowledge graph indication; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (for Prinzmetal angina) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

For comparison, the other predictions with meaningful evidence are:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Stroke disorder | 99.95% | L1 | Proceed with Guardrails |
| Transient ischaemic attack | 99.87% | L1 | Proceed with Guardrails |
| Thrombotic disease | 99.94% | L3 | Hold (research question) |

Predictions ranked 4 and 6-10 (sick sinus syndrome 2, sarcoglycanopathy, Wildervanck syndrome, macrocephaly with dysmorphic facies and psychomotor retardation, cavernous sinus thrombosis, lateral sinus thrombosis) have model prediction only (L5) and no trials or literature. They are not discussed further.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the literature, dipyridamole inhibits adenosine reuptake and phosphodiesterase, raising extracellular adenosine and intracellular cAMP/cGMP. This inhibits platelet aggregation and causes vasodilation.

For **Prinzmetal angina**, a vasodilator mechanism is plausible in principle. However, the literature mostly describes dipyridamole as a **stress-testing agent**, not a treatment. One report (PMID 3421166) suggests that stopping dipyridamole stress with aminophylline can trigger coronary vasospasm in variant angina. This points to a potential safety concern rather than therapeutic benefit. No treatment trials exist.

For **stroke and TIA**, the antiplatelet mechanism directly supports secondary prevention, usually combined with aspirin. This is an established, guideline-supported use. The link to the original atrial fibrillation indication is not clear from the data, as the data do not describe the relationship, and guidance notes that these combinations are used in the absence of atrial fibrillation.

---

## Clinical Trial Evidence

Because the top-ranked prediction (Prinzmetal angina) has no registered trials, the table below shows the most relevant trials for the best-supported predictions (stroke disorder and TIA).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | Completed | 4500 | ESPRIT: aspirin plus dipyridamole or mild anticoagulation versus aspirin alone after cerebral ischaemia of arterial origin |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | Completed | 551 | EARLY: Aggrenox started within 24 hours of stroke versus after 7 days of aspirin |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | Completed | 240 | Antioxidant effect of aspirin plus dipyridamole in carotid revascularisation |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | Completed | 250 | Feasibility of antiplatelet versus anticoagulant trial in cervical artery dissection (indirect relevance) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure versus anticoagulants or antiplatelets for stroke recurrence (dipyridamole not the tested drug) |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | Completed | 664 | Gore REDUCE: PFO closure plus antiplatelets versus antiplatelets alone (dipyridamole part of comparator only) |
| [NCT06053021](https://clinicaltrials.gov/study/NCT06053021) | N/A | Unknown | 1200 | Antiplatelet therapy in acute ischaemic stroke with thrombocytopenia (indirect relevance) |
| [NCT06983795](https://clinicaltrials.gov/study/NCT06983795) | N/A | Not yet recruiting | 1000 | Asia-Pacific PFO and ischaemic stroke registry (indirect relevance) |

Only ESPRIT is directly relevant, and it is a Phase 4 trial. No registered trials were found for Prinzmetal angina or thrombotic disease.

---

## Literature Evidence

**Prinzmetal angina (top-ranked prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Clinical observation | Jpn Circ J | 26 patients with rest angina given several drugs including dipyridamole 50 mg; small non-randomised observation |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Small clinical study | Am J Cardiol | Aminophylline termination of dipyridamole stress can trigger coronary vasospasm in variant angina (safety signal) |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Cohort | Br Heart J | Exercise test reproducibility in patients with ST elevation and differing dipyridamole test responses (diagnostic) |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Cohort (diagnostic) | Jpn Circ J | Dipyridamole-loading thallium imaging for coronary artery disease detection (diagnostic only) |

**Stroke and TIA (best-supported predictions)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis (individual patient data) | Stroke | Dipyridamole with or without aspirin for secondary prevention after ischaemic stroke or TIA |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane review | Cochrane Database Syst Rev | Adding dipyridamole to aspirin associated with 22% risk reduction versus aspirin alone in one trial; wider reviews show less difference against other antiplatelets |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analysis | J Neurol Sci | Efficacy and safety of aspirin plus dipyridamole versus aspirin after TIA or stroke |
| [31177983](https://pubmed.ncbi.nlm.nih.gov/31177983/) | 2019 | Network meta-analysis | Stroke | Efficacy and safety of antiplatelet agents after noncardioembolic stroke or TIA |
| [34399713](https://pubmed.ncbi.nlm.nih.gov/34399713/) | 2021 | Systematic review/network meta-analysis | BMC Neurol | Antiplatelet drugs for secondary prevention after ischaemic stroke or TIA |
| [26304937](https://pubmed.ncbi.nlm.nih.gov/26304937/) | 2015 | Network meta-analysis | J Am Heart Assoc | Long-term antiplatelet mono- and dual therapies after ischaemic stroke or TIA |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | Antiplatelet therapy for prevention of death, MI and stroke in high-risk patients |
| [34211246](https://pubmed.ncbi.nlm.nih.gov/34211246/) | 2021 | Review | Aust Prescr | Aspirin, clopidogrel, or aspirin plus dipyridamole are first-line options for secondary stroke prevention in the absence of atrial fibrillation |

For thrombotic disease, the literature is mainly general antiplatelet reviews plus some unrelated results, so it is not tabulated.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0209000L0AAACAC | Dipyridamole tablets 100 mg | Not stated | Not stated |

One valid single-ingredient authorisation is recorded. Dosage form, manufacturer and approved indication text are not available in the data compiled for this report. The authorisation number shown does not follow the usual MHRA PL format, so it should be verified against the MHRA register. Please check the current BNF and SmPC for licensed indications.

---

## Safety Considerations

**Contraindications (from the knowledge graph, not label text):** the TxGNN knowledge graph links dipyridamole with a long list of disease contraindications. The main ones relevant to practice include:
- Bleeding and haematological: thrombocytopenia, haemophilia, congenital prothrombin deficiency, vitamin K deficiency haemorrhagic disease, anaemia
- Gastrointestinal: peptic ulcer disease (including active), gastritis
- Cardiovascular: acute coronary syndrome, myocardial infarction, coronary thrombosis, hypotensive disorder
- Other: kidney disease, liver disease, gallbladder disease, gout, Reye syndrome, Alzheimer disease

These are database associations and need to be checked against the SmPC.

**Drug Interactions:** 100 interactions were identified. Those graded Moderate are dexfenfluramine, sibutramine and fenfluramine. The rest listed (for example aspirin, cimetidine, omeprazole, pantoprazole, lansoprazole, metformin, morphine, simvastatin, prednisone, vancomycin) have no severity grade available.

**Other considerations from the evidence:**
- Potential coronary vasospasm trigger when dipyridamole stress is reversed with aminophylline in variant angina
- Adenosine potentiation could theoretically worsen bradycardia (relevant to the sick sinus syndrome prediction)
- For stroke and TIA use: headache tolerability, bleeding risk, and caution in unstable coronary disease

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, Prinzmetal angina)

**Rationale:**
- Prinzmetal angina is supported only by small, older, mostly diagnostic or observational reports, with no treatment trials and a possible vasospasm safety signal. Evidence level is L4.
- By contrast, stroke disorder and TIA (L1, Proceed with Guardrails) rest on ESPRIT, meta-analyses and Cochrane reviews, but these are established uses of aspirin plus dipyridamole, not new repurposing. Thrombotic disease (L3) remains a research question needing thrombosis-specific trials.

**To proceed, the following is needed:**
- Confirmation of the original indication, since the knowledge graph lists atrial fibrillation but no approved indication text is available for the UK authorisation
- SmPC-derived warnings, contraindications and approved indication text for the UK product (the key warnings and contraindications data are missing)
- Detailed mechanism of action data
- For Prinzmetal angina: a prospective controlled study with defined endpoints and a vasospasm safety assessment
- For stroke and TIA: confirmation of current UK licensing and guideline positioning (including NICE guidance) and a patient-selection and monitoring plan covering headache and bleeding risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

