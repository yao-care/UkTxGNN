---
layout: default
title: Daptomycin
parent: Model Prediction Only (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic used against Gram-positive bacterial infections. The TxGNN model assigns a very high score (99.86%) to **Osteoarthritis** as a repurposing candidate, but this is currently supported by **0 clinical trials** and **10 publications** — and closer reading shows the literature is almost entirely about treating *infections in* joints, not osteoarthritis itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (e.g. complicated skin/soft-tissue infections, bacteraemia) — no UK licence text available in this evidence pack |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only — see rationale below) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Daptomycin is a calcium-dependent cyclic lipopeptide antibiotic. It inserts into the cell membrane of Gram-positive bacteria, causing depolarisation and disrupting protein, DNA and RNA synthesis, leading to bacterial cell death. This mechanism has no established biological link to osteoarthritis, which is a degenerative joint disease driven by cartilage breakdown, low-grade inflammation and mechanical/metabolic stress — not bacterial infection.

All 10 supporting publications describe daptomycin used to treat **osteoarticular or prosthetic joint infections** (septic arthritis, periprosthetic joint infection, bone/joint infection with Staphylococcus or Corynebacterium species) — that is, antimicrobial therapy given when a joint is infected, often during or after orthopaedic surgery. This is a fundamentally different clinical scenario from treating osteoarthritis itself.

The most plausible explanation is that TxGNN's knowledge graph conflates "osteoarthritis" with adjacent disease vocabulary such as "septic arthritis" or "prosthetic joint infection," producing a high similarity score that does not reflect a genuine pharmacological repurposing opportunity. One retrieved case report (PMID 32206362) even describes a patient initially diagnosed with osteoarthritis whose atypical imaging led to detection of an unrelated Corynebacterium joint infection — illustrating exactly this kind of terminology overlap rather than therapeutic evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | International orthopaedics | High-dose daptomycin + rifampicin evaluated for Gram-positive osteoarticular *infections*, not osteoarthritis |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Daptomycin efficacy/safety in hip and knee periprosthetic joint *infections* |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone/joint and implant-associated *infections* |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro susceptibility | J Antibiotics | In vitro susceptibility of S. aureus/S. epidermidis isolated from prosthetic joint *infections* |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs standard therapy outcomes in osteoarticular *infections* with S. aureus bacteraemia |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | Case Reports in Orthopedics | Chronic Corynebacterium striatum septic arthritis in a patient referred for knee replacement — initially mistaken for osteoarthritis on imaging |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Registry/Survey | Int J Antimicrob Agents | Survey of current antibiotic practice for prosthetic joint *infections* among infectious disease physicians |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry (EU-CORE) | Medicina clinica | Spanish EU-CORE registry data on real-world daptomycin use across Gram-positive *infections* |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort/Microbiology | Surgical infections | 10-year microbiological profile of Staphylococci causing osteoarticular *infections* |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | ASM case reports | First reported isolation of Corynebacterium propinquum from synovial fluid causing septic arthritis in a native joint |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags detailed MHRA warnings/contraindications as a Blocking data gap — see Next Steps.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not corroborated by genuine indication-relevant evidence — all 10 publications concern treating infections *in* joints, not degenerative osteoarthritis, and there is no mechanistic pathway from an antibacterial membrane-disrupting agent to cartilage/inflammatory disease modification. Combined with the absence of clinical trials, no UK marketing authorisation, and missing MOA/safety data, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- MHRA/SmPC warnings and contraindications (currently a Blocking data gap)
- Authoritative mechanism-of-action confirmation from DrugBank (currently a High-severity data gap)
- Clarification from the TxGNN disease vocabulary on whether "osteoarthritis" is being conflated with septic arthritis/prosthetic joint infection terms, before this candidate is pursued further
- If disambiguation confirms conflation, this candidate should be reclassified as a negative/noise prediction rather than re-evaluated

**Note on other candidates in this evidence pack:** The remaining nine predicted indications for daptomycin (rheumatoid arthritis, osteoarthritis susceptibility, gout, and several rare skeletal dysplasias) all carry the same L5/Hold status, with either zero supporting literature or, in the case of gout, a single adverse-event case report (daptomycin-induced rhabdomyolysis complicated by gout) rather than therapeutic evidence. None currently warrant further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

