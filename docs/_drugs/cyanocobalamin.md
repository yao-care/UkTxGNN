---
layout: default
title: Cyanocobalamin
parent: Moderate Evidence (L3-L4)
nav_order: 181
evidence_level: L4
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

Using the evidence pack as provided (Taiwan-labelled fields carry the UK dataset for this build). No skill fits a one-shot report-writing task like this, so proceeding directly.

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin (vitamin B12) has no UK marketing authorisation on file in this evidence pack and is currently not marketed. The TxGNN model predicts a possible link to **Biotin Metabolic Disease**, but this is a single, low-confidence signal: of the **15 clinical trials** and **20 publications** reviewed, none directly test cyanocobalamin in this indication, and the biochemical pathways of cobalamin and biotin are distinct.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (no UK marketing authorisation on file); cyanocobalamin is generally used as vitamin B12 replacement therapy |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cyanocobalamin is not available in this evidence pack. Based on general pharmacological knowledge, cyanocobalamin is a synthetic form of vitamin B12 (cobalamin), acting as a cofactor for methionine synthase and methylmalonyl-CoA mutase. Its established clinical role is treating vitamin B12 deficiency states.

Biotin metabolic diseases (e.g. biotinidase deficiency, holocarboxylase synthetase deficiency) arise from impaired biotin utilisation in the carboxylase enzyme family (propionyl-CoA carboxylase, pyruvate carboxylase, etc.) — a biochemically distinct pathway from cobalamin metabolism. The two vitamins are not interchangeable at the enzyme level.

The model's rationale itself flags this: the high TxGNN score most likely reflects proximity within a knowledge-graph cluster of "vitamin-dependent metabolic diseases" (guilt-by-association) rather than a demonstrated causal or enzymatic link. With original indication and MOA data both absent from the pack, this mechanistic hypothesis cannot be cross-checked against confirmed pharmacology, so it should be treated as exploratory only.

## Clinical Trial Evidence

None of the identified trials directly test cyanocobalamin for biotin metabolic disease; all are indirect (broader micronutrient/vitamin studies or newborn screening programmes that may incidentally cover biotin metabolic disease detection). Listed below for transparency:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Newborn genomic screening programme (Baby Detect) covering a panel of 126 treatable conditions, potentially including biotin metabolic disease detection — does not test cyanocobalamin treatment |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient palliative intervention in congestive heart failure; not biotin-disease specific |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Q10 ubiquinol plus vitamin B/E complex in autism/Phelan-McDermid syndrome; uses active folate, not cyanocobalamin |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Pilot comparison of natural vs synthetic vitamin B-complex bioavailability |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin/mineral supplementation in type 2 diabetic neuropathy/nephropathy; unrelated disease entity |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and childhood neurodevelopment; unrelated to biotin metabolism |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption in post-bariatric surgery patients |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Carglumic acid (Carbaglu) in propionic/methylmalonic acidaemia — related organic acidaemia class, but a different drug and mechanism |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional intervention for methylation/oxidative stress in autism |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completed | 202 | Multivitamin/mineral ± fatty acid supplementation on impulsivity and aggression |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders spanning cobalamin, folate, biotin, B1 and E — the most directly relevant source linking B12 and biotin pathways conceptually |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics of North America | B-complex vitamins as coenzyme cofactors in megavitamin-responsive aminoacidopathies |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins implicated in inborn metabolic errors via malabsorption, metabolic errors, or dependency syndromes |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Overview of vitamin dependency syndromes |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Vitamin B12 as cofactor for methylmalonyl-CoA mutase and methionine synthase; mechanisms of B12 deficiency in nervous system disease |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Relationship between B-group vitamins including biotin and type 2 diabetes |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterology Clinics of North America | Vitamin/mineral deficiencies, monitoring and repletion in inflammatory bowel disease |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Ann NY Acad Sci | Interactions among B-complex vitamins including thiamin and riboflavin |
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | J Chem Technol Biotechnol | Biotechnological production of vitamins and related coenzymes |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Cohort/Mechanistic | J Endocrinol | B12-deficient diet in rats induces glucose intolerance and a prediabetic phenotype |

## UK Market Information

No UK marketing authorisations are recorded for cyanocobalamin in this evidence pack (0 licenses on file; market status: **Not marketed**). Product-specific information (brand names, formulations, licensed indication wording) would need to be sourced directly from the MHRA product database or SmPC/BNF once identified.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between cobalamin and biotin metabolism is biochemically weak — the two vitamins act on distinct enzyme pathways — and the high TxGNN score likely reflects knowledge-graph clustering rather than a causal relationship. No clinical trial or publication in this pack directly tests cyanocobalamin for biotin metabolic disease, and the drug currently has no UK marketing authorisation.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for cyanocobalamin (currently a data gap, high impact)
- UK product literature/SmPC warnings and contraindications (currently a data gap, blocking for any safety assessment)
- A targeted literature or preclinical search specifically on cobalamin's role, if any, in carboxylase-dependent (biotin) metabolic pathways
- Confirmation of whether any UK marketing authorisation exists or is planned, given the drug is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

