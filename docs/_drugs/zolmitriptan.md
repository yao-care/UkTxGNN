---
layout: default
title: Zolmitriptan
parent: Model Prediction Only (L5)
nav_order: 662
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Zolmitriptan: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Migraine disorder (migraine with or without aura)"
monitor_inn: "Zolmitriptan"
predicted_indications: ["migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Zolmitriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a 5-HT1B/1D receptor agonist (a triptan), originally used for the acute treatment of migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**,
but there are currently **no registered clinical trials** and only **general migraine and triptan literature** (20 publications, mostly reviews) supporting this direction, with no subtype-specific data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (migraine with or without aura) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (no clinical trials; only preclinical, mechanism and general review literature) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Zolmitriptan is a selective serotonin 5-HT1B/1D receptor agonist with both central and peripheral activity. Preclinical work shows it can inhibit trigeminovascular activation, and it is established for the acute treatment of migraine with or without aura. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description draws on the published pharmacology literature.

Migraine with brainstem aura is a migraine subtype that shares the core pathophysiology of other migraines, including trigeminovascular activation and CGRP release. On this basis the mechanism is plausible.

There is, however, an important caveat. Triptans have traditionally been used with caution, or avoided, in brainstem aura (formerly basilar-type migraine) because of theoretical concerns about vasoconstriction. The supplied literature consists of general migraine and triptan reviews and gives no subtype-specific efficacy or safety data. The very high TxGNN score mainly reflects proximity to the already approved migraine indication, not independent evidence for this subtype.

Two other predictions (atrophoderma vermiculata and ulerythema ophryogenesis) have no identifiable mechanistic link, no trials and no literature. They appear to be graph-based artefacts and are not pursued further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below are general migraine or triptan papers. None studies zolmitriptan specifically in migraine with brainstem aura.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of drugs for acute migraine treatment in adults |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | Zolmitriptan 2.5 and 5 mg shows rapid onset (significant relief at 45 minutes) and is more effective than placebo in randomised trials in moderate to severe migraine |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | Placebo-controlled trials show good 2-hour response and pain-free rates; nausea, photophobia and phonophobia also improve |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | Subgroup analysis of RCT | Neurol Sci | Frovatriptan vs zolmitriptan 2.5 mg in 18 patients with migraine with aura (subset of a 107-patient crossover study) |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | J Headache Pain | Frovatriptan compared with rizatriptan, zolmitriptan and almotriptan in migraine with aura; triptans are probably not effective if taken during the aura phase |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical | Cephalalgia | Zolmitriptan is a 5-HT1B/1D partial agonist that inhibits trigeminovascular activation centrally and peripherally |
| [12864759](https://pubmed.ncbi.nlm.nih.gov/12864759/) | 2003 | Clinical study | Headache | Transcranial Doppler study of migraine attacks treated with oral zolmitriptan or sumatriptan |
| [22298171](https://pubmed.ncbi.nlm.nih.gov/22298171/) | 2012 | Case report | Cardiol J | Zolmitriptan-induced acute myocardial infarction in a 45-year-old woman, a relevant cardiovascular safety signal |
| [17177580](https://pubmed.ncbi.nlm.nih.gov/17177580/) | 2007 | Post-marketing surveillance | Clin Drug Investig | Effectiveness and tolerability of zolmitriptan 5 mg nasal spray in real-life practice |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Front Neurol | Treatment options in vestibular migraine, noting that dedicated trials are scarce |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407041Z0AAAAAA | Zolmitriptan tablets 2.5 mg | Tablet (as recorded in the compiled data) | Not recorded in the compiled data |

The compiled data show one valid single-ingredient authorisation. The identifier is in a non-standard format and is not a typical MHRA PL number, so it should be verified against the MHRA register. The dosage form and approved indication fields were blank. Please check the current SmPC, the BNF and any NICE guidance for the licensed indications.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links zolmitriptan with contraindications in the following areas. These should be confirmed against the SmPC.
  - Cardiovascular: hypertension, coronary artery disease, myocardial infarction, myocardial ischaemia, Prinzmetal angina, Wolff-Parkinson-White syndrome, peripheral vascular disease, Raynaud disease, ischaemic bowel disease
  - Cerebrovascular: stroke, transient ischaemic attack, cerebral infarction, brain ischaemia, vertebrobasilar insufficiency, intracranial arteriosclerosis
  - Migraine subtype: familial or sporadic hemiplegic migraine
  - Other: kidney disease, liver disease, gallbladder disease, haemoglobinopathy
  
  The cerebrovascular and hemiplegic migraine entries are particularly relevant to a brainstem aura indication.
- **Drug Interactions:** 82 interactions were recorded. The main ones are:
  - **Major:** lorcaserin, dolasetron, palonosetron, ondansetron, granisetron, dexfenfluramine, fenfluramine, sibutramine (mostly serotonergic or 5-HT3 antagonist combinations)
  - **Moderate:** morphine (including liposomal), cimetidine, obeticholic acid
- **Case report signal:** A published case describes acute myocardial infarction after zolmitriptan use.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but is driven mainly by similarity to the approved migraine indication. There are no clinical trials and no subtype-specific data, and the traditional caution about triptans in brainstem aura, together with vascular contraindications recorded in the knowledge graph, raises a real safety question.

**To proceed, the following is needed:**
- Subtype-specific efficacy and safety evidence for triptans in migraine with brainstem aura (or a well-designed study)
- Review of the current SmPC and BNF warnings and contraindications for zolmitriptan, which were not available in the data compiled for this report
- Verification of the UK marketing authorisation record (number format, dosage form and approved indication)
- A cardiovascular and cerebrovascular risk assessment for the target population
- Detailed mechanism-of-action data from DrugBank to support the mechanistic-link analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

