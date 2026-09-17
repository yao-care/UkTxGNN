---
layout: default
title: Piroxicam
parent: High Evidence (L1-L2)
nav_order: 467
evidence_level: L2
indication_count: 10
---

# Piroxicam
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

Using no additional skill invocation — this is a direct content-generation task fully specified by the prompt template; proceeding to produce the report.

Note before the report: the raw TxGNN top-8 hits for piroxicam (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, etc.) are ultra-rare genetic/structural syndromes with **zero evidence** and the evidence pack itself scores them "L5/Hold" with explicit "no biological plausibility" rationale — these look like embedding-similarity artefacts, not real signal. The only candidate in this pack with actual clinical evidence is **rank 10, Juvenile Idiopathic Arthritis (L2/Proceed with Guardrails)**, so the report below is built around that candidate rather than the literal `predicted_indications[0]` entry.

---

# Piroxicam: From Adult Inflammatory Arthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is a long-established oxicam-class NSAID conventionally used for adult inflammatory and degenerative joint disease (osteoarthritis, rheumatoid arthritis, ankylosing spondylitis). Among the TxGNN candidates reviewed for this drug, the only one supported by real clinical evidence is **Juvenile Idiopathic Arthritis (JIA)**, backed by **2 historic paediatric RCTs and 2 contemporary systematic reviews/network meta-analyses** — though piroxicam itself is not currently marketed in the UK and carries well-known class-level safety restrictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in the supplied regulatory data; piroxicam is a well-characterised oxicam-class NSAID historically used for osteoarthritis, rheumatoid arthritis and ankylosing spondylitis |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| UK Market Status | Not currently marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacology cited in the evidence pack's own rationale, piroxicam is a non-selective COX-1/COX-2 inhibitor that suppresses prostaglandin synthesis, producing anti-inflammatory and analgesic effects — a mechanism that maps directly onto the synovial inflammation seen in inflammatory arthritides.

JIA and piroxicam's established adult indications (rheumatoid and osteoarthritis) share the same core pathology — synovial inflammation and joint pain — so extending an NSAID from adult to paediatric inflammatory joint disease is mechanistically coherent. This is not really a "novel" repurposing signal so much as a re-affirmation of a use that was already studied in the 1980s: two head-to-head paediatric RCTs against naproxen were conducted at the time, and the drug remains listed alongside other NSAIDs in more recent (2021, 2024) systematic reviews and network meta-analyses of JIA pharmacotherapy.

The other eight TxGNN hits ranked above JIA in this pack (rare skeletal dysplasias, WHIM syndrome, etc.) were reviewed and found to have no biological plausibility and no supporting evidence — the evidence pack itself scores them L5/Hold. They are excluded from further discussion here as likely embedding-similarity artefacts rather than genuine repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | RCT | Eur J Rheumatol Inflamm | 26 children with juvenile rheumatoid arthritis randomised to piroxicam or naproxen; significant reduction in painful and swollen joint counts |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | Br J Rheumatol | 8-week double-blind, double-dummy crossover in 47 children with juvenile chronic arthritis; piroxicam vs naproxen showed no significant efficacy difference |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic Review / Network Meta-analysis | World J Clin Cases | Network meta-analysis of NSAIDs (including piroxicam) for JIA; optimal agent not yet established |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic Review / Meta-analysis | Indian Pediatr | Compared efficacy and safety of 9 NSAIDs, including piroxicam, in JIA |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic Study | Eur J Clin Pharmacol | Steady-state PK in 10 children with rheumatic disease on piroxicam 0.4 mg/kg once daily; mean half-life ~32.6 h |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Review (Safety) | Clin Rheumatol | Long-term toxicity review in a paediatric rheumatology cohort with 155 NSAID exposures |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort | Int Ophthalmol | 56% frequency of chronic iridocyclitis in ANA-positive pauciarticular JCA — relevant to ocular monitoring in this population |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderarztliche Praxis | Discusses piroxicam and sulfasalazine as then-newer agents in juvenile chronic arthritis drug therapy |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review | Drugs | Nabumetone review for OA/RA; provides NSAID-class comparator context |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Review | Drugs | Pirprofen review listing piroxicam among comparator NSAIDs for rheumatic disease |

---

## UK Market Information

Piroxicam is **not currently marketed in the UK** — no marketing authorisations were identified in the data source (0 licenses).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note (independent of this data pack):** Piroxicam is a well-documented special case in EU/UK regulatory history — since 2007 its use has been restricted EU-wide to second-line, short-term treatment due to gastrointestinal, cardiovascular and severe cutaneous adverse reaction (SJS/TEN) risks. This is directly relevant to any paediatric extension and should be factored into risk assessment even though no drug-specific warning data was returned by this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The JIA candidate is supported by genuine paediatric RCT and systematic review evidence (L2), unlike the other TxGNN hits reviewed for this drug. However, the drug-level safety labelling data gap (DG001, Blocking) means this candidate cannot yet clear an initial safety screen, and piroxicam holds no current UK marketing authorisation.

**To proceed, the following is needed:**
- Current UK/EU SmPC or equivalent safety labelling data (DG001)
- Confirmed mechanism of action and paediatric PK/PD data (DG002)
- Clarification of piroxicam's current UK/EU regulatory and restricted-use status before pursuing paediatric development
- A formal risk assessment weighing piroxicam's known GI/CV/skin toxicity profile against benefit in a paediatric population
- No further action needed on the other 8 TxGNN-ranked candidates for this drug — reviewed and excluded as biologically implausible with no supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

