---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
---

# Colchicine
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

Using the report template supplied in this prompt (no additional skill needed — this is a direct content-generation task against a well-specified format). One structural note before the report: this evidence pack is a **multi-indication** pack (`TW-DB01394-multi`) with three independently scored predicted indications of very different evidence strength, so I've kept the JSON's rank order but organised trial/literature evidence per indication rather than only using index `[0]`, since collapsing to just "Malaria" (rank 1, weakest evidence) would hide the clinically important Familial Mediterranean Fever finding (rank 2, by far the strongest evidence). Original indication and MOA are both explicit Blocking/High-severity data gaps in the pack itself (DG001, DG002) — no real-world knowledge has been substituted for these.

---

# Colchicine: Predicted Applications in Familial Mediterranean Fever, Malaria and Dermatofibrosarcoma Protuberans

## One-Sentence Summary

The evidence pack does not record an original licensed indication for Colchicine in the UK (no marketing authorisations on file). TxGNN predicts three candidate indications — **Familial Mediterranean Fever** (score 99.38%), **Plasmodium falciparum malaria** (score 99.60%) and **Dermatofibrosarcoma protuberans** (score 99.37%) — but the strength of supporting evidence varies enormously, from an established clinical consensus (FMF) to a single unsupported model prediction (DFSP).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation or original indication data on file (Blocking data gap, see below) |
| Predicted New Indications | 1. Familial Mediterranean Fever — 99.38% (L1, Proceed with Guardrails); 2. *P. falciparum* malaria — 99.60% (L4, Hold); 3. Dermatofibrosarcoma protuberans — 99.37% (L5, Hold) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** overall (safety data gap is blocking), with **Proceed with Guardrails** achievable for Familial Mediterranean Fever once safety data is supplied |

## Why is These Predictions Reasonable?

Detailed mechanism-of-action data for Colchicine is not available in this evidence pack — this is flagged internally as a High-severity gap (DG002) requiring a DrugBank API lookup. No original indication or UK licence data is available either (DG001, Blocking), so a mechanistic bridge from an established use to the new predictions cannot be built from the source data. What follows is drawn instead from the per-indication rationale already generated against Colchicine's known pharmacology (tubulin binding / microtubule inhibition):

**Familial Mediterranean Fever** has the clearest mechanistic fit. Colchicine inhibits microtubule polymerisation, blocking neutrophil cytoskeletal reorganisation and chemotaxis, and suppresses NLRP3 inflammasome activation — directly addressing FMF pathology, where MEFV gene mutations drive pyrin/inflammasome overactivation. In practice this is not a novel repurposing hypothesis but a long-established first-line use; the literature returned here is mostly recent reviews rather than original RCTs, but decades of clinical consensus support a high evidence level.

**Malaria**: the same tubulin-binding mechanism could theoretically disrupt the cytoskeletal processes malaria parasites rely on for invasion and division. However, the supporting literature (1984–1994) is old, indirect, and mostly tests related compounds (tubulozole) or unrelated resistance genes (pfmdr1) rather than colchicine itself — a mechanistically plausible but evidentially weak link.

**Dermatofibrosarcoma protuberans**: colchicine's anti-mitotic action could plausibly inhibit proliferation in this sarcoma, but this is a pure TxGNN knowledge-graph inference with no corroborating preclinical, in vitro or clinical evidence whatsoever.

## Clinical Trial Evidence

**Familial Mediterranean Fever**

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | Recruiting | 25 | Non-interventional safety/effectiveness study of canakinumab (Ilaris) in colchicine-resistant FMF and related periodic fever syndromes — trial drug is canakinumab, not colchicine; included only because colchicine-resistant FMF is the target population (relevance grade C) |

**Plasmodium falciparum malaria**: Currently no related clinical trials registered.

**Dermatofibrosarcoma protuberans**: Currently no related clinical trials registered.

## Literature Evidence

**Familial Mediterranean Fever** (10 of 20 most relevant shown, prioritising resistance/safety/guideline content)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37298536](https://pubmed.ncbi.nlm.nih.gov/37298536/) | 2023 | Review | Int J Mol Sci | Update on FMF pathogenesis, treatment resistance and compliance |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Review | Presse Med | FMF overview: MEFV/pyrin pathology and disease course |
| [28413100](https://pubmed.ncbi.nlm.nih.gov/28413100/) | 2017 | Review | Semin Arthritis Rheum | Colchicine resistance/intolerance in FMF: definitions, causes, alternatives |
| [35789271](https://pubmed.ncbi.nlm.nih.gov/35789271/) | 2023 | Cohort | Mod Rheumatol | Early predictors of colchicine resistance in FMF |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohort | Int J Rheum Dis | Canakinumab in FMF, with vs without concurrent colchicine |
| [20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/) | 2010 | Review/Toxicology | Clin Toxicol | Colchicine poisoning — narrow therapeutic index, safety profile |
| [38354004](https://pubmed.ncbi.nlm.nih.gov/38354004/) | 2023 | Review | Rev Prat | Long-term colchicine prevents FMF attacks; MEFV exon 10 diagnosis |
| [37903671](https://pubmed.ncbi.nlm.nih.gov/37903671/) | 2023 | Guideline | Rev Med Interne | French national protocol for FMF diagnosis and management |
| [29773275](https://pubmed.ncbi.nlm.nih.gov/29773275/) | 2017 | Review | Best Pract Res Clin Rheumatol | Periodic fever syndromes overview including FMF |
| [25649364](https://pubmed.ncbi.nlm.nih.gov/25649364/) | 2014 | Review | Acta Med (Hradec Kralove) | Colchicine is the only agent shown to reduce FMF amyloidosis risk |

**Plasmodium falciparum malaria**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro/Mechanistic | PLoS One | Curcumin disrupts *P. falciparum* microtubules (colchicine not directly tested) |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro/Molecular | Mol Cell Biol | pfmdr1 gene expression linked to chloroquine susceptibility |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro/Mechanistic | Antimicrob Agents Chemother | Tubulozole mode of action against *P. falciparum*; colcemid comparison noted |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro/Mechanistic | Cell Biol Int Rep | Tubulin-binding compounds active against *P. falciparum* in vitro |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro/Mechanistic | Cell Biol Int Rep | Duplicate/companion report of tubulin-binding compound activity |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observational/Serology | Clin Exp Immunol | Anti-intermediate filament antibodies in acute malaria sera |

**Dermatofibrosarcoma protuberans**: Currently no related literature available.

## UK Market Information

No UK marketing authorisations are currently on record for Colchicine in this evidence pack (market status: Not marketed, 0 licences). This should be verified directly against the MHRA products database and current BNF entry, since the evidence pack flags the absence of this data as a Blocking gap (DG001) rather than a confirmed negative finding.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: warnings, contraindications and drug interaction data are recorded in this evidence pack as a Blocking gap (DG001) — no marketing authorisation/SmPC has yet been located for Colchicine, so safety assessment cannot proceed to stage S1 until this is resolved.*

## Conclusion and Next Steps

**Decision: Hold (overall) — Proceed with Guardrails achievable for Familial Mediterranean Fever specifically**

**Rationale:**
- The Blocking safety data gap (DG001 — no MHRA/SmPC warnings or contraindications on file) prevents any of the three indications from clearing initial safety screening (S1), regardless of efficacy evidence strength.
- Evidence quality is highly uneven across candidates: FMF is supported by L1-grade, decades-deep clinical consensus (decision stage S3); malaria evidence is L4 and dated/indirect; DFSP is L5, a model prediction with no corroborating data.

**To proceed, the following is needed:**
- MHRA SmPC / current BNF entry for Colchicine — warnings, contraindications, drug interactions (resolves DG001)
- Mechanism-of-action data via DrugBank API (resolves DG002)
- For FMF: confirm current UK licensing/off-label status specifically for this indication
- For malaria: contemporary preclinical work directly testing colchicine (not analogue compounds) before further consideration
- For DFSP: treat as hypothesis-generating only; requires in vitro/in vivo validation before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

