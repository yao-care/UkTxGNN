---
layout: default
title: Oxygen
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Oxygen
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

Using the drug-repurposing evaluation report template (already fully specified in your instructions) to produce the report below — no additional skill invocation needed for this pure content-generation task.

# Oxygen: From Undocumented Original Indication to Dry Eye Syndrome

## One-Sentence Summary

> The evidence pack contains no recorded original indication or marketing authorisation for Oxygen (DrugBank DB09140) in this dataset.
> The TxGNN model's top prediction suggests possible relevance to **Dry Eye Syndrome**, with **21 clinical trials** and **20 publications** nominally linked to this pairing — however, on closer reading almost none of this evidence concerns oxygen *therapy* itself; it overwhelmingly concerns **reactive oxygen species (oxidative stress)**, a mechanistically distinct concept that the model appears to have conflated with the drug name "Oxygen".

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no `original_indications` entries and no licence records available) |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 93.22% |
| Evidence Level | L4 (no completed RCT directly evaluates oxygen therapy for dry eye; evidence base is largely mechanistic/preclinical and off-target) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Oxygen is not available in this evidence pack, and no original indication is recorded, which limits any comparison between an established use and the predicted new one.

More importantly, the evidence pack's own repurposing rationale flags a specific concern: the great majority of the clinical trial and literature evidence retrieved for "dry eye syndrome" is about **reactive oxygen species (ROS) and oxidative stress** in dry eye pathophysiology — not about administering oxygen gas as a therapy. This is a plausible failure mode of embedding-based models such as TxGNN, which can conflate a drug entity ("Oxygen") with a closely related biochemical concept ("oxidative stress"/"reactive oxygen species") that shares vocabulary but not pharmacology. Only one trial in the evidence set genuinely tests an oxygen-based intervention (hyperbaric oxygen therapy), and it is a general "emerging indications" registry study that is not yet recruiting and not specific to dry eye disease.

By contrast, the second-ranked prediction in this evidence pack — **dermatitis** — has two *completed* trials that directly test oxygen or hyperbaric oxygen as the intervention (oxygen for infant diaper dermatitis; hyperbaric oxygen for radiation-induced dermatitis), giving it a more defensible mechanistic story (oxygen promoting wound healing and countering local hypoxia-driven inflammation) than the top-ranked dry eye prediction. This is noted here for completeness but is outside the scope of the primary indication being evaluated below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01369589](https://clinicaltrials.gov/study/NCT01369589) | Phase 1/2 | Completed | 24 | Oral rinse (P-552) for xerostomia in Sjögren's syndrome; oral, not ocular, and does not involve oxygen as an intervention |
| [NCT02975102](https://clinicaltrials.gov/study/NCT02975102) | NA | Completed | 87 | CBL-101 vs Vismed® eye drops in moderate-to-severe dry eye; graded **not relevant** — unrelated to oxygen |
| [NCT03464357](https://clinicaltrials.gov/study/NCT03464357) | NA | Unknown | 16 | fMRI study of cortical response to light in photophobia related to dry eye; no oxygen intervention |
| [NCT04584216](https://clinicaltrials.gov/study/NCT04584216) | NA | Completed | 60 | Steam eye mask with acupoint stimulation for eye fatigue/dry eye symptoms; no oxygen intervention |
| [NCT02370225](https://clinicaltrials.gov/study/NCT02370225) | NA | Completed | 45 | Aerobic exercise for fatigue in Sjögren's syndrome; no oxygen intervention |
| [NCT07240649](https://clinicaltrials.gov/study/NCT07240649) | Phase 4 | Not yet recruiting | 100 | The only trial in this set that actually tests oxygen (hyperbaric oxygen therapy) — but as a general "emerging indications" registry study, not specific to dry eye, and not yet recruiting |
| [NCT02680158](https://clinicaltrials.gov/study/NCT02680158) | NA | Completed | 48 | Intranasal lacrimal neurostimulator device for tear production; graded **not relevant** — no oxygen intervention |
| [NCT03805425](https://clinicaltrials.gov/study/NCT03805425) | NA | Unknown | 25 | Corneal crosslinking (PiXL) for hyperopia; no oxygen intervention |
| [NCT06004895](https://clinicaltrials.gov/study/NCT06004895) | NA | Completed | 26 | Mechanisms of light-based therapies for dry eye/Meibomian gland dysfunction; no oxygen intervention |
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | NA | Completed | 60 | N-acetylcysteine for Sjögren's-related dryness, targeting reactive oxygen species; mechanistically adjacent but does not use oxygen therapy |

**Note:** Of the 21 registered trials linked to this prediction, only one involves an oxygen-based intervention, and it is not disease-specific and has not yet started recruiting. No completed or ongoing trial tests oxygen therapy specifically for dry eye syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33938134](https://pubmed.ncbi.nlm.nih.gov/33938134/) | 2022 | Systematic Review/Meta-analysis | Acta Ophthalmologica | Oxidative and antioxidative stress markers are elevated in dry eye disease compared with healthy controls |
| [28834388](https://pubmed.ncbi.nlm.nih.gov/28834388/) | 2018 | Review | Acta Ophthalmologica | Reviews the role of oxidative stress and environmental factors in dry eye pathogenesis |
| [35435328](https://pubmed.ncbi.nlm.nih.gov/35435328/) | 2022 | Review | Advanced Science | Discusses anti-oxidative/anti-inflammatory micelle eye drops targeting the ROS-driven dry eye "vicious cycle" |
| [38725011](https://pubmed.ncbi.nlm.nih.gov/38725011/) | 2024 | Review | J Nanobiotechnology | Comprehensive review of dry eye therapies targeting inflammation, oxidative stress and mitochondrial dysfunction |
| [36066316](https://pubmed.ncbi.nlm.nih.gov/36066316/) | 2022 | Cohort/Mechanistic | Invest Ophthalmol Vis Sci | AKR1C1 protects corneal epithelial cells against oxidative-stress-mediated ferroptosis in dry eye |
| [40045550](https://pubmed.ncbi.nlm.nih.gov/40045550/) | 2025 | Preclinical | Animal Models Exp Med | Astaxanthin reduces inflammation/oxidative stress in a benzalkonium-chloride dry eye model |
| [39699913](https://pubmed.ncbi.nlm.nih.gov/39699913/) | 2024 | Mechanistic | Invest Ophthalmol Vis Sci | ER stress drives ROS production and NLRP3 inflammasome activation in dry eye disease |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Advanced Materials | Nano-formulated catalase eye drops for ROS scavenging in dry eye disease |
| [38632691](https://pubmed.ncbi.nlm.nih.gov/38632691/) | 2024 | Preclinical | ACS Nano | Nanoceria-based cyclosporin A delivery targeting oxidative stress-inflammation crosstalk in dry eye |
| [39792610](https://pubmed.ncbi.nlm.nih.gov/39792610/) | 2025 | Preclinical | Advanced Science | ROS-responsive microneedle patch for Sjögren's-related dry eye |

**Note:** All ten publications above concern reactive oxygen species (ROS)/oxidative stress biology in dry eye disease. None evaluates supplemental oxygen or oxygen therapy as a treatment. This literature signal most plausibly reflects lexical overlap between "Oxygen" and "oxidative stress/ROS" rather than a genuine pharmacological hypothesis.

---

## UK Market Information

Oxygen is currently **not marketed** in the UK according to this evidence pack, and no marketing authorisation records are available (`total_licenses: 0`). No UK product/licence table can be generated from the data provided.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications and drug–drug interaction data are not yet available in this evidence pack; obtaining the product label warnings is flagged as a blocking data gap for any further safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (dry eye syndrome) is not supported by any trial or publication that actually tests oxygen therapy for this condition — the evidence base almost entirely reflects reactive oxygen species/oxidative stress biology, a likely semantic conflation in the embedding model rather than a genuine repurposing signal. Combined with the absence of original indication, MOA, and product label data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Manual relevance triage of the "pending"-graded trials and publications to rule out any genuine oxygen-therapy signal within the dry eye evidence set
- Product label warnings and contraindications (currently a blocking data gap)
- Mechanism-of-action documentation for Oxygen (currently a high-severity data gap)
- Confirmation of Oxygen's original/established indication and any UK regulatory status, to enable a proper original-vs-new indication comparison
- If pursuing oxygen repurposing further, consider re-scoping evaluation toward the **dermatitis** signal (rank 2), which has two completed trials directly testing oxygen/hyperbaric oxygen as the intervention and a more coherent mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

