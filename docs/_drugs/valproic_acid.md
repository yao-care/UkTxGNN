---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 650
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Valproic Acid: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
monitor_inn: "Valproic acid"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Valproic Acid
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

## Valproic Acid: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Valproic acid is an established antiseizure medicine, originally used for epilepsy and manic episodes of bipolar disorder.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **no registered clinical trials** and only **1 publication** (a 1997 case series on Sturge-Weber syndrome), which does not support this prediction.
The more plausible predicted uses are epilepsy-related (for example trigeminal neuralgia and startle epilepsy), and these are discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy; manic bipolar affective disorder; absence epilepsy (from the TxGNN knowledge graph, as no approved indication text is available in the UK data) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

For context, the other leading predictions are:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Visual epilepsy | 99.88% | L4 | Research question |
| 3 | Trigeminal neuralgia | 99.83% | L4 | Research question |
| 4 | Orgasm-induced seizures | 99.81% | L5 | Hold |
| 5 | Eating seizures | 99.81% | L4 | Hold |
| 6 | Thinking seizures | 99.81% | L5 | Hold |
| 7 | Audiogenic seizures | 99.81% | L4 | Hold |
| 8 | Startle epilepsy | 99.81% | L4 | Research question |
| 9 | Micturition-induced seizures | 99.81% | L5 | Hold |
| 10 | Reading seizures | 99.79% | L4 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data compiled for this report is not available. Based on the literature reviewed, valproic acid is a broad-spectrum antiseizure drug. Its reported actions include enhancing GABAergic inhibition, blocking sodium channels and T-type calcium channels, and inhibiting histone deacetylase (HDAC).

For the top-ranked prediction, **trigeminal nerve neoplasm**, there is no credible mechanistic link. The only retrieved paper is a case series on Sturge-Weber syndrome, where valproic acid is probably used just for seizure control. The high model score is not backed by clinical or mechanistic evidence, and it should be treated as a likely artefact.

The epilepsy-related predictions are more reasonable, but most are extensions of the existing epilepsy indication rather than true repurposing:

- **Visual, reading and other reflex epilepsies:** valproate is a standard treatment in idiopathic generalised epilepsies, which include photosensitive and reflex forms. No study directly tests it in these specific seizure types.
- **Trigeminal neuralgia:** sodium channel blockade and GABAergic inhibition could reduce paroxysmal neuropathic pain. Reviews mention valproate as a second-line option, with carbamazepine as first-line. Much of the retrieved literature concerns carbamazepine instead.
- **Startle epilepsy:** one small clinical study examined valproate and the auditory startle reflex, and a case report describes a response in hyperekplexia (a distinct glycinergic disorder), so the link is indirect.
- **Audiogenic seizures:** evidence is entirely from animal models.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

---

## Literature Evidence

Evidence for the top-ranked prediction (trigeminal nerve neoplasm):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases; not relevant to tumour treatment |

Selected evidence for the more plausible predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20200383](https://pubmed.ncbi.nlm.nih.gov/20200383/) | 2010 | RCT | N Engl J Med | Ethosuximide, valproic acid and lamotrigine compared in childhood absence epilepsy (indirect, supports existing epilepsy use) |
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Curr Neuropharmacol | Molecular mechanisms and clinical evidence for valproic acid in epilepsy |
| [1774173](https://pubmed.ncbi.nlm.nih.gov/1774173/) | 1991 | Review | Headache | Medical management of trigeminal neuralgia; valproic acid listed among anticonvulsants reported to be efficacious |
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs for non-epileptic indications; evidence mostly from case series and small trials |
| [11129121](https://pubmed.ncbi.nlm.nih.gov/11129121/) | 2000 | Review | Drugs | Anticonvulsants for neuropathic pain: mechanisms and place in therapy |
| [29262725](https://pubmed.ncbi.nlm.nih.gov/29262725/) | 2018 | Clinical study | Clin EEG Neurosci | Examined whether valproate suppresses the auditory startle reflex in epilepsy |
| [2496695](https://pubmed.ncbi.nlm.nih.gov/2496695/) | 1989 | Case report | Pediatr Neurol | Hyperekplexia with complete resolution on valproic acid (indirect) |
| [33551767](https://pubmed.ncbi.nlm.nih.gov/33551767/) | 2020 | Preclinical | Front Behav Neurosci | Cannabidiol and valproate in an audiogenic seizure hamster model |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Cohort/Review | Future Oncol | Levetiracetam and valproic acid in glioma: antiseizure and possible antineoplastic effects (indirect) |
| [16302877](https://pubmed.ncbi.nlm.nih.gov/16302877/) | 2005 | Review | Epilepsia | Photosensitivity in idiopathic generalised epilepsies (indirect) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402030Q0AAABAB | Valproic Acid Tab G/R 500mg | Not specified | Not specified in the data compiled |

The data compiled for this report lists one valid single-ingredient authorisation (a modified-release 500 mg tablet). The identifier appears to be a BNF-style code (chapter 4, central nervous system) rather than a standard MHRA PL number, and no approved indication text is available. Please check the current SmPC and BNF for licensed indications and NICE guidance.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, carbamoyl phosphate synthetase I deficiency, inherited porphyria and other porphyrias, kidney disease, pyoureter, hyperargininemia, haematological disease, pancreatitis, citrullinemia, cognitive disorder, liver disease, gallbladder disease and thrombocytopenia.

**Drug interactions:** 100 interactions were identified; the first 20 returned include:

- **Major:** glycerol phenylbutyrate
- **Moderate:** bupropion, morphine (including liposomal), acetylsalicylic acid, clarithromycin, difenoxin, diphenoxylate, activated charcoal, dronabinol, metoclopramide, nabilone
- **Minor:** cimetidine, magnesium oxide, aluminium hydroxide, calcium carbonate, esomeprazole, magaldrate, magnesium carbonate, magnesium hydroxide

The retrieved literature also notes interactions with carbapenem antibiotics, which can lower valproate levels. Valproate in females of reproductive age carries well-recognised teratogenic risk, so current MHRA pregnancy prevention requirements apply.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, trigeminal nerve neoplasm, has no supporting trials, no mechanistic link and only one irrelevant case series (L5). The epilepsy-related predictions are plausible but largely extend the existing indication, with only indirect, preclinical or case-level evidence (L4). Of these, trigeminal neuralgia, visual epilepsy and startle epilepsy are the most reasonable research questions.

**To proceed, the following is needed:**
- Review the model's top-ranked prediction (trigeminal nerve neoplasm) and confirm it is a spurious result
- Detailed mechanism of action data
- Approved indication text and dosage forms for the UK authorisation, confirmed against the MHRA record and SmPC
- Label-based warnings and contraindications from the SmPC and BNF (the current safety data are knowledge-graph derived)
- For trigeminal neuralgia: a valproate-specific controlled comparison against carbamazepine
- A risk-benefit assessment covering teratogenicity and hepatotoxicity before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

