---
layout: default
title: Sumatriptan
parent: Model Prediction Only (L5)
nav_order: 588
evidence_level: L5
indication_count: 1
---

# Sumatriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a 5-HT1B/1D receptor agonist (triptan), originally used for the acute treatment of migraine and cluster headache.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**,
but there are currently **no registered clinical trials** and only **general migraine literature** (18 publications, none specific to this subtype) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (the licence record in the data compiled for this report has no indication text; the original indications are taken from the knowledge graph: migraine, cluster headache, paroxysmal hemicrania, hemicrania continua) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only; no studies specific to this subtype) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, sumatriptan is a 5-HT1B/1D agonist. It is thought to relieve migraine through cranial vasoconstriction and inhibition of trigeminal neuropeptide release (such as CGRP), reducing trigeminovascular pain transmission.

Migraine with brainstem aura is a subtype of migraine with aura, so it sits very close to sumatriptan's established migraine indications. This closeness likely explains the high TxGNN score. It reflects the disease's relationship to already-approved migraine indications rather than a novel repurposing signal.

An important caveat: triptans have historically carried cautions or contraindications in hemiplegic and basilar-type migraine, because of a theoretical vasoconstrictive risk to the brainstem and posterior circulation. The same concern applies to this predicted indication, so the apparent mechanistic fit does not mean the use is safe.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publication addresses migraine with brainstem aura directly. The most relevant publications on sumatriptan in migraine and migraine with aura are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytother Res | Double-blind trial in 100 patients with acute migraine without aura comparing ginger powder with sumatriptan |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200 mg in acute migraine with aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Not classified | Neurology | Reports reduced efficacy of sumatriptan in migraine with aura compared with migraine without aura |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of clinical experience with sumatriptan in migraine and cluster headache |
| [12917936](https://pubmed.ncbi.nlm.nih.gov/12917936/) | 2003 | Systematic review | Cochrane Database Syst Rev | Review of oral sumatriptan for acute migraine (a later 2012 version was withdrawn) |
| [26628293](https://pubmed.ncbi.nlm.nih.gov/26628293/) | 2016 | Review | Drugs | Sumatriptan/naproxen combination; phase 3 trials showed more patients pain-free at 2 h than with placebo |
| [27681528](https://pubmed.ncbi.nlm.nih.gov/27681528/) | 2016 | Review | Drugs | Sumatriptan nasal powder for acute migraine with or without aura |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Not classified | Neurology | Subcutaneous sumatriptan and the migraine aura |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Review of status migrainosus as a complication of migraine with or without aura |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407041T0AAACAC | Sumatriptan tablets 100 mg | Tablet (from product name) | Not stated in the data compiled for this report |

The identifier above is a BNF-style product code (BNF chapter 4.7.4.1, drugs for the treatment of acute migraine), not a PL marketing authorisation number. Dosage form and indication details should be confirmed against the MHRA record and the SmPC.

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The knowledge graph links sumatriptan with several conditions, mainly:
  - Cardiovascular: coronary artery disease, myocardial infarction, congestive heart failure, hypertension, peripheral vascular disease
  - Cerebrovascular: stroke, cerebral infarction
  - Other: liver and kidney disease, epilepsy, diabetes, blood coagulation disease
  
  The vascular associations are particularly relevant to the brainstem and posterior circulation concern above.
- **Drug Interactions** (100 interactions recorded; main ones listed):
  - Major: fenfluramine, dexfenfluramine, lorcaserin and sibutramine (serotonergic agents, with a risk of serotonin syndrome), and the 5-HT3 antagonists ondansetron, granisetron, dolasetron and palonosetron
  - Moderate: morphine (including liposomal)

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score mainly reflects the close ontological link to approved migraine indications. There are no clinical trials and no literature specific to migraine with brainstem aura. Triptans have a long-standing theoretical caution in brainstem-type aura, and no label-based safety data were available.

**To proceed, the following is needed:**
- Review of the current SmPC and BNF guidance on triptan use in brainstem aura, hemiplegic and basilar-type migraine
- Targeted literature search for sumatriptan in brainstem aura and basilar-type migraine, including case series and safety data
- Mechanism of action data (currently missing) and label warnings and contraindications
- Confirmation of the MHRA marketing authorisation details (PL number, dosage form, approved indication)
- A cardiovascular and cerebrovascular risk assessment, and a clinical trial or specialist neurology opinion before any use in this subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

