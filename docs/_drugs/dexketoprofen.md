---
layout: default
title: Dexketoprofen
parent: Model Prediction Only (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexketoprofen: predicted new indication Tendinitis (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Dexketoprofen
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

# Dexketoprofen: From Pain Management (Indication Not Recorded) to Tendinitis

## One-Sentence Summary

Dexketoprofen is a non-steroidal anti-inflammatory drug (NSAID) marketed in the UK as a 25 mg tablet.
The TxGNN model's top-ranked prediction is **tendinitis**, but this is supported by **no registered clinical trials** and only **1 indirect publication** (an emergency department study in non-specific musculoskeletal pain).
Among the other predictions, **migraine disorder** has by far the strongest evidence (**5 clinical trials** and **20 publications**), and is discussed below as the more actionable direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Tendinitis (rank 1); migraine disorder (rank 6) has the strongest evidence |
| TxGNN Prediction Score | 99.90% (tendinitis); 99.87% (migraine disorder) |
| Evidence Level | L4 (tendinitis); L1 (migraine disorder) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (tendinitis); Proceed with Guardrails (migraine disorder) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dexketoprofen is the active (S)-enantiomer of ketoprofen and belongs to the NSAID class, which inhibits cyclo-oxygenase (COX-1 and COX-2) enzymes and so reduces prostaglandin production. Its efficacy in acute pain has been established, and mechanistically it may be applicable to inflammatory and pain conditions.

**Tendinitis.** Prostaglandin-mediated inflammation and pain are plausible drivers of tendon disorders, so an NSAID is a reasonable candidate. However, the only supporting evidence is a single emergency department trial in non-traumatic musculoskeletal pain, which mentions tendinitis only as one possible cause. It is indirect and not specific to tendinitis.

**Migraine disorder.** COX inhibition reduces prostaglandin-driven neurogenic inflammation and trigeminovascular pain signalling during acute attacks. This is supported by placebo-controlled and active-comparator randomised trials and a meta-analysis. The evidence relates to acute treatment only.

**Other predictions.** Rheumatoid arthritis (symptomatic relief only), headache disorder (evidence derived from the migraine studies), and migraine with brainstem aura (extrapolated from general migraine) have partial or indirect rationale. Fibromyalgia, idiopathic granulomatous myositis, myositis fibrosa, exostosis and congenital hypotrichosis milia are model predictions only, with weak or no mechanistic support and no clinical evidence.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, tendinitis. Currently no related clinical trials registered.

For reference, the following trials relate to the best-supported prediction, **migraine disorder**:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | Completed | 224 | IV dexketoprofen versus placebo in acute migraine attack in the emergency department |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | Not applicable | Completed | 150 | IV metoclopramide versus dexketoprofen trometamol versus the combination in acute migraine |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | Completed | 200 | IV dexketoprofen versus paracetamol for headache from acute migraine attack |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | Completed | 160 | IV ibuprofen versus IV dexketoprofen for migraine-related headache |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | Unknown | 210 | IV paracetamol, dexketoprofen and ibuprofen compared on pain scores in acute migraine |

---

## Literature Evidence

For tendinitis, one publication is available:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT | Am J Emerg Med | IV dexketoprofen versus paracetamol in non-traumatic musculoskeletal pain in the emergency department (indirect; not tendinitis-specific) |

For reference, key publications for **migraine disorder**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | RCT | Cephalalgia | IV dexketoprofen versus placebo for migraine attack in the emergency department |
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | Meta-analysis | Medicine | Efficacy of dexketoprofen versus placebo for pain control in migraine attack across randomised studies |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | RCT | Am J Emerg Med | IV metoclopramide versus dexketoprofen trometamol versus the combination in acute migraine |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | RCT (Phase II) | J Pain | Dose-optimisation, placebo-controlled crossover study of 25 mg and 50 mg dexketoprofen trometamol in migraine |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | RCT | Emerg Med J | IV paracetamol versus dexketoprofen in acute migraine in the emergency department |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | RCT | Cephalalgia | Frovatriptan plus dexketoprofen versus frovatriptan alone in migraine with or without aura |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society update on parenteral treatments for migraine in the emergency department |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010AEAAAAAA | Dexketoprofen Tab 25mg | Tablet | Not available in the data compiled for this report |

The BNF classifies dexketoprofen among the non-steroidal anti-inflammatory drugs. Please check the current SmPC and BNF for the licensed indications. Dexketoprofen is not listed here under a NICE-appraised indication in the data compiled for this report.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Class-level cautions relevant to any repurposing work include gastrointestinal, renal and cardiovascular risks of NSAIDs, and the risk of medication-overuse headache with frequent analgesic use in headache disorders.

---

## Conclusion and Next Steps

**Decision: Hold (tendinitis, the top-ranked prediction). Proceed with Guardrails for migraine disorder as a separate, better-evidenced direction.**

**Rationale:**
- Tendinitis has a high model score but only one indirect trial, and no registered trials, so it remains at L4 and should not progress on current evidence.
- Migraine disorder is supported by multiple randomised trials, including a placebo-controlled study, and a meta-analysis (L1). Guardrails should limit use to acute treatment in adults, with attention to NSAID gastrointestinal, renal and cardiovascular risks. No prophylaxis evidence was provided.

**To proceed, the following is needed:**
- Original licensed indication text from the MHRA/SmPC, as the authorisation record is incomplete
- Warnings, contraindications and interaction data from the SmPC and BNF (the safety screen cannot be completed without these)
- Mechanism of action data from DrugBank
- For tendinitis: tendon-specific randomised trials, ideally against another NSAID or placebo
- For migraine disorder: assessment of evidence in UK primary-care settings and oral formulations, since most trials used IV dexketoprofen in Turkish emergency departments, and confirmation of the formulation and route available in the UK
- For headache disorder and migraine with brainstem aura: subtype-specific studies before any extension beyond migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

