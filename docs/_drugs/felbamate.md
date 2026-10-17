---
layout: default
title: Felbamate
parent: Model Prediction Only (L5)
nav_order: 277
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Felbamate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy, partial epilepsy, Lennox-Gastaut syndrome"
monitor_inn: "Felbamate"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Felbamate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Felbamate: From Epilepsy to Trigeminal Nerve Neoplasm (with Trigeminal Neuralgia as a Closer Alternative)

## One-Sentence Summary

Felbamate is an antiepileptic drug, originally used for epilepsy, including partial seizures and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** (top-ranked prediction), but there are **no clinical trials and no publications** supporting this indication.
The second-ranked prediction, **trigeminal neuralgia**, has **4 publications** (one case report), which is far more plausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, partial epilepsy, Lennox-Gastaut syndrome (the UK authorisation record contains no indication text) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1); trigeminal neuralgia (rank 2) |
| TxGNN Prediction Score | 99.62% (trigeminal nerve neoplasm); 99.18% (trigeminal neuralgia) |
| Evidence Level | L5 (trigeminal nerve neoplasm); L4 (trigeminal neuralgia) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (trigeminal nerve neoplasm); trigeminal neuralgia remains a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general pharmacological knowledge, felbamate is thought to act through NMDA receptor (glycine site) antagonism and GABAergic potentiation, and may modulate sodium channels.

**Trigeminal nerve neoplasm:** These actions could relieve neuropathic symptoms linked to trigeminal nerve involvement, but they offer no plausible antitumour effect. The high score is probably driven by network proximity to trigeminal neuralgia and other nerve-related nodes in the knowledge graph, not by tumour biology. The prediction should be regarded as a graph-based artefact rather than a credible oncology signal.

**Trigeminal neuralgia:** This condition involves ectopic, hyperexcitable firing of trigeminal afferents, and first-line drugs (carbamazepine, oxcarbazepine) act on voltage-gated sodium channels. Felbamate's mechanisms give it a plausible basis for neuropathic pain, and the link to its original antiepileptic use is much stronger.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either predicted indication.

---

## Literature Evidence

Literature for the top prediction (trigeminal nerve neoplasm): currently no related literature available.

Literature for trigeminal neuralgia (rank 2):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Case report | The Clinical Journal of Pain | Reports that felbamate relieved trigeminal neuralgia; the only direct clinical evidence |
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Review | CNS Drugs | Guide to drug choice in trigeminal neuralgia; carbamazepine is the drug of choice, with baclofen, phenytoin and sodium valproate also effective |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Preclinical (animal) | Indian Journal of Pharmacology | Rat comparison of carbamazepine, gabapentin and lamotrigine in neuropathic pain; felbamate is mentioned only as an antiepileptic reported to be effective |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Case report (safety) | The Annals of Pharmacotherapy | Delayed anaphylaxis associated with felbamate; relevant to safety rather than efficacy |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010AAAAABAB (BNF-style code; no PL number available) | Felbamate tablets 600 mg | Tablet | Not available in the compiled data |

Felbamate sits in the BNF antiepileptic section (chapter 4, central nervous system). It has 1 valid single-ingredient authorisation record.

---

## Safety Considerations

- **Contraindications and risk conditions (from knowledge graph associations, not label text):** long QT syndrome (including familial), torsades de pointes, liver failure and liver disease, gallbladder disease, kidney disease, haematologic disease, aplastic anaemia (including idiopathic), porphyria and other porphyrin metabolism diseases, anxiety disorder, neurotic disorder, dysthymic disorder, and pyoureter.
- **Key warnings:** Felbamate is associated with serious risks of aplastic anaemia and hepatic failure (boxed warnings), and a case report describes delayed anaphylaxis. Please confirm the details in the SmPC.
- **Drug interactions:** 100 interactions were identified in the compiled data. The 20 listed were all of Moderate severity. They include:
  - Opioids: morphine (including liposomal), opium
  - Vitamin D analogues: cholecalciferol, calcifediol, calcitriol, ergocalciferol, dihydrotachysterol
  - Antiemetics and related agents: aprepitant, rolapitant, metoclopramide, dronabinol, nabilone
  - Antidiabetic agents: saxagliptin, linagliptin, repaglinide
  - Others: eliglustat, naloxegol, naltrexone, nitisinone

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** (trigeminal nerve neoplasm). Trigeminal neuralgia is a **research question** only, not yet ready for adoption.

**Rationale:**
- The trigeminal nerve neoplasm prediction has no supporting trials or literature and no plausible antitumour mechanism. The serious risks of aplastic anaemia and hepatic failure make speculative oncology use unjustified.
- For trigeminal neuralgia, the mechanism is plausible, but the direct evidence is a single 1995 case report. Safer alternatives with RCT support exist, so any use would be limited to refractory cases under strict haematological and liver monitoring.

**To proceed, the following is needed:**
- Confirmed mechanism of action data
- Full UK safety information, including the SmPC warnings and contraindications, and the licensed indication text and PL number
- Prospective, controlled evidence for trigeminal neuralgia in refractory patients, with a defined monitoring plan (FBC, liver function)
- A comparison against guideline-recommended therapy (carbamazepine, oxcarbazepine)
- No further work is recommended on the trigeminal nerve neoplasm indication unless independent biological evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

