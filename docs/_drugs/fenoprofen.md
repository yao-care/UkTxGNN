---
layout: default
title: Fenoprofen
parent: High Evidence (L1-L2)
nav_order: 266
evidence_level: L2
indication_count: 10
---

# Fenoprofen
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Fenoprofen: From Rheumatic Pain and Inflammation to Ankylosing Spondylitis

## One-Sentence Summary

Fenoprofen is a propionic-acid-derivative NSAID historically used to relieve pain and inflammation in rheumatic conditions such as rheumatoid arthritis and osteoarthritis. Of the ten indications TxGNN predicted, nine (including the top-ranked hit) were assessed by the evidence pipeline as mechanistically implausible model noise — rare monogenic skeletal dysplasias and immune disorders with no plausible link to NSAID pharmacology. The one candidate with genuine supporting evidence is **Ankylosing Spondylitis**, backed by **2 randomised controlled trials** and **9 publications**, all predating 1990.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the regulatory dataset provided; fenoprofen is a propionic acid NSAID historically used for rheumatoid arthritis, osteoarthritis and general rheumatic pain |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** TxGNN's nine highest-scoring predictions for fenoprofen (e.g. acromesomelic dysplasia, brachyolmia, WHIM syndrome) have no clinical trials or literature support and were flagged by the evidence pipeline as prediction noise — likely knowledge-graph co-occurrence artefacts rather than genuine pharmacological signals. Ankylosing spondylitis, ranked 10th by raw score, is the only candidate with direct clinical evidence and is therefore the focus of this report.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this specific fenoprofen product record is not available. Based on known pharmacology, fenoprofen belongs to the propionic acid class of NSAIDs (alongside ibuprofen and naproxen) and works by non-selectively inhibiting cyclo-oxygenase (COX-1 and COX-2), reducing prostaglandin synthesis and thereby producing anti-inflammatory and analgesic effects.

Ankylosing spondylitis is an inflammatory spondyloarthropathy in which NSAIDs are a well-established first-line symptomatic treatment across the class — used to reduce axial pain, stiffness and inflammation. Fenoprofen's original use in rheumatic and joint disease (rheumatoid arthritis, osteoarthritis, gout) sits on the same inflammatory-pain spectrum as ankylosing spondylitis, making the mechanistic extension straightforward and consistent with how other propionic acid NSAIDs (naproxen, indomethacin) are already used in this condition.

This is therefore less a novel repurposing discovery than a re-confirmation of an indication fenoprofen was directly studied for during the 1970s–80s, before largely falling out of routine use in favour of newer agents.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7010512](https://pubmed.ncbi.nlm.nih.gov/7010512/) | 1980 | RCT | Rheumatology and Rehabilitation | Double-blind cross-over of fenoprofen 600mg TID vs phenylbutazone 100mg TID in 30 ankylosing spondylitis patients; phenylbutazone improved most measures, but chest expansion improved significantly only with fenoprofen |
| [6996071](https://pubmed.ncbi.nlm.nih.gov/6996071/) | 1980 | RCT | Rheumatology and Rehabilitation | Double-blind cross-over trial of indomethacin, fenoprofen and placebo in ankylosing spondylitis, with discussion of patient assessment methodology |
| [7026817](https://pubmed.ncbi.nlm.nih.gov/7026817/) | 1981 | Review | JAMA | Six-way crossover comparison of NSAIDs in 32 ankylosing spondylitis and 33 rheumatoid arthritis patients; naproxen, indomethacin and fenoprofen calcium were among the most effective agents in AS |
| [324748](https://pubmed.ncbi.nlm.nih.gov/324748/) | 1977 | Review | Drugs | Comprehensive review of fenoprofen pharmacology and efficacy in rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and gout; comparable to aspirin with fewer/milder side effects |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review | Drugs | Review of naproxen (same propionic acid class) in rheumatic disease, supporting class-wide efficacy in inflammatory arthritides |
| [300118](https://pubmed.ncbi.nlm.nih.gov/300118/) | 1977 | Review | JAMA | Review of fenoprofen calcium, naproxen and tolmetin sodium; notes potential use in ankylosing spondylitis alongside rheumatoid arthritis |
| [391117](https://pubmed.ncbi.nlm.nih.gov/391117/) | 1979 | Review | Annals of Internal Medicine | Ibuprofen review noting chemical relation to fenoprofen and naproxen within the propionic-acid NSAID class |
| [4615887](https://pubmed.ncbi.nlm.nih.gov/4615887/) | 1974 | Cohort | Current Medical Research and Opinion | Clinical experience report on fenoprofen as a new antirheumatic agent |
| [36583943](https://pubmed.ncbi.nlm.nih.gov/36583943/) | 2023 | Other | ChemMedChem | Describes fenoprofen's established use in rheumatoid arthritis, degenerative joint disease, ankylosing spondylitis and gout via COX-1/COX-2 inhibition, in the context of developing carborane analogues with improved antitumour activity |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two double-blind RCTs and several supporting reviews from the 1970s–80s directly demonstrate fenoprofen's efficacy in ankylosing spondylitis, consistent with the established class effect of propionic acid NSAIDs in spondyloarthropathy. However, all evidence predates 1990, no UK marketing authorisation currently exists for this product, and mechanism-of-action and safety data are absent from the current dataset — so this is a re-confirmation of dated evidence rather than a validated modern therapeutic pathway.

**To proceed, the following is needed:**
- Confirm original UK-licensed indication(s) and formal MOA record via DrugBank/SmPC
- Obtain current SmPC/BNF safety, contraindication and interaction data (none available in this dataset)
- Assess whether a UK marketing authorisation pathway exists, given current "not marketed" status and zero licenses on record
- Seek contemporary (post-2000) evidence comparing fenoprofen against modern axial spondyloarthritis standard-of-care (other NSAIDs, biologics), since existing trials are over 40 years old and pre-date current diagnostic/treatment guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

