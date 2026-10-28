---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 125
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Camphor: predicted new indication Migraine disorder (evidence level L4). Approved use: Not available in the data compiled for this report"
monitor_inn: "Camphor"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
---

# Camphor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Camphor: From an Unspecified Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Camphor is a long-established topical counterirritant, but the data compiled for this report do not record a specific approved indication for it in the UK.
The TxGNN model predicts it may be useful for **migraine disorder**, but there are **no registered clinical trials** and only **3 publications** (case reports and a case series, with no efficacy data) behind this prediction.
The evidence is currently at the model-prediction and preclinical level, so this should be treated as a research question rather than a basis for clinical use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the single authorisation record has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, camphor modulates transient receptor potential (TRP) channels (TRPV1, TRPA1 and TRPM8) and acts as a topical counterirritant. These channels are involved in sensory and pain signalling, which makes a link with trigeminovascular pain pathways in migraine plausible in principle.

A 2026 preclinical animal study (PMID 42849823) reported that natural (+)-camphor reduced reserpine-induced migraine with local cerebral vasospasm, apparently via the p38β MAPK/ATF2 pathway. This is the strongest piece of supporting evidence, but it is animal data only.

The remaining literature is indirect. Two reports describe cluster headache linked to essential-oil toothpastes containing camphor and eucalyptus, which, if anything, suggest camphor-containing products may provoke headache. Other hits concern camphor content in feverfew oil or are unrelated to camphor. No human trial shows benefit in migraine.

Other predicted indications (migraine subtypes, erectile dysfunction, pulmonary hypertension, Raynaud disease, Tourette syndrome and several rare conditions) have no credible supporting evidence. The pulmonary hypertension literature hits are a name collision with the CAMPHOR questionnaire (Cambridge Pulmonary Hypertension Outcome Review) and have nothing to do with the drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42849823](https://pubmed.ncbi.nlm.nih.gov/42849823/) | 2026 | Preclinical animal study | J Ethnopharmacol | Natural (+)-camphor alleviated reserpine-induced migraine with cerebral vasospasm in an animal model, via the p38β MAPK/ATF2 pathway |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cases of cluster headache linked to toothpastes containing pro-convulsant essential oils |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Rep | Two cases of cluster headache temporally related to toothpastes containing camphor and eucalyptus oils |
| [27324458](https://pubmed.ncbi.nlm.nih.gov/27324458/) | 2016 | Analytical chemistry | Biomed Chromatogr | Method for measuring camphor in feverfew essential oil (indirect relevance only) |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical review of paediatric neuropsychopharmacology in the 1940s–50s (not direct evidence for migraine) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190400000AAIKIK | Camphor (S) BP 1988 | Not specified | Not specified |

The single authorisation is recorded as a valid single-ingredient product. Dosage form and indication details were not available in the data compiled for this report, so please check the current MHRA record, the BNF and any relevant NICE guidance.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Points from the compiled data that warrant caution:
- Case reports link camphor-containing essential-oil products with cluster headache, and essential oils with pro-convulsant properties are known to cause seizures and may worsen migraine.
- Camphor has recognised neurotoxicity (seizure risk in overdose), which argues for caution in any neurological indication.
- An oral acute toxicity study in rats (PMID 27955803) raised tissue oxidative stress and toxicity concerns.
- No drug interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9985), but the evidence is limited to a single animal study and indirect case reports, some of which suggest camphor may provoke headache rather than treat it. There are no human trials, and neurotoxicity is a recognised concern.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) to support the TRP-channel hypothesis
- Authorisation details (dosage form, approved indication) and SmPC warnings and contraindications for the UK product, as these are currently missing
- Further preclinical replication of the migraine findings, including a dose-safety assessment
- A clear route and formulation rationale before any early-phase human study is considered
- A formal safety review covering seizure risk and potential headache provocation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

