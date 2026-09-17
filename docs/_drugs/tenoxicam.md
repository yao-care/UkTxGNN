---
layout: default
title: Tenoxicam
parent: High Evidence (L1-L2)
nav_order: 563
evidence_level: L2
indication_count: 10
---

# Tenoxicam
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

# Tenoxicam: From Established NSAID Use to Rheumatoid Arthritis

## One-Sentence Summary

Tenoxicam is an oxicam-class non-steroidal anti-inflammatory drug (NSAID); no original indication or UK marketing history is recorded in this Evidence Pack, and the drug is not currently marketed in the UK. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, a prediction supported by **1 clinical trial** and **20 publications**, though the underlying literature shows this is a long-established use of tenoxicam rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in this Evidence Pack (no UK marketing authorisation on file); the literature confirms tenoxicam is an oxicam-class NSAID historically used for rheumatic and musculoskeletal pain conditions |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the DrugBank field (`original_moa` = Data Gap). However, the supporting literature and rationale data indicate that tenoxicam belongs to the oxicam class of NSAIDs (the same class as piroxicam) and acts as a non-selective COX-1/COX-2 inhibitor, reducing prostaglandin synthesis and thereby producing anti-inflammatory and analgesic effects — the standard pharmacological basis for NSAID use in inflammatory joint disease.

Rheumatoid arthritis is, in fact, one of the oxicam class's core historical indications rather than a newly hypothesised use. Multiple randomised controlled trials from the 1980s–1990s (e.g. head-to-head comparisons with piroxicam, aceclofenac and naproxen) demonstrate consistent efficacy of tenoxicam in RA symptom control, comparable to other established NSAIDs. This means the TxGNN prediction in this case largely **confirms a well-documented existing use** rather than identifying a genuinely novel therapeutic hypothesis — a distinction that should be considered when interpreting the "repurposing" framing of this candidate.

Mechanistically, the applicability is straightforward: RA is characterised by synovial inflammation driven by prostaglandin-mediated pathways, which is directly addressed by COX inhibition. This is corroborated by pharmacokinetic data showing tenoxicam distributes into synovial fluid in RA patients, supporting local anti-inflammatory activity at the site of disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | N/A | Completed | 80 | Compared tenoxicam alone, paracetamol alone, and a tenoxicam-paracetamol combination for postoperative pain control after double-jaw orthognathic surgery (not RA-specific, but confirms tenoxicam's analgesic/anti-inflammatory profile). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | RCT | The Journal of Rheumatology | RCT (n=102) comparing tenoxicam 20 mg OD vs piroxicam 20 mg OD in RA; no significant difference in efficacy or adverse events. |
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clinical Rheumatology | Multicentre double-blind RCT (n=292) comparing aceclofenac vs tenoxicam in RA; both showed comparable, sustained clinical improvement over 3 months. |
| [3915889](https://pubmed.ncbi.nlm.nih.gov/3915889/) | 1985 | Cohort/Trial | European Journal of Rheumatology and Inflammation | Open multicentre study of rectal tenoxicam suppositories (20 mg/day) in 79 patients with RA or arthrosis over 6 weeks; efficacy demonstrated. |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | Cohort/Trial | European Journal of Rheumatology and Inflammation | Double-blind parallel trials comparing tenoxicam with piroxicam in osteoarthrosis, RA and ankylosing spondylitis; tenoxicam at least as effective. |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | Cohort/Trial | Journal of International Medical Research | Large general-practice study (n=2,963) of oral tenoxicam 20 mg/day for 12 weeks in osteoarthritis and RA; symptom reduction, many continued treatment beyond 52 weeks. |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Review confirming tenoxicam is an effective analgesic/anti-inflammatory for RA, osteoarthritis and ankylosing spondylitis, with efficacy at least equivalent to other NSAIDs. |
| [8137596](https://pubmed.ncbi.nlm.nih.gov/8137596/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetic review: tenoxicam is completely absorbed orally, ~99% protein bound, with no evidence of enterohepatic recycling. |
| [3262939](https://pubmed.ncbi.nlm.nih.gov/3262939/) | 1988 | PK Study | Therapeutic Drug Monitoring | Studied plasma/synovial fluid distribution of a single 40 mg tenoxicam dose in RA/OA patients; characterised factors determining synovial fluid/plasma ratio. |
| [8187453](https://pubmed.ncbi.nlm.nih.gov/8187453/) | 1994 | Mechanistic/Basic | Clinical Rheumatology | Investigated tenoxicam's effect on neutrophil chemotaxis in RA patients vs healthy controls; no significant difference found. |
| [41419140](https://pubmed.ncbi.nlm.nih.gov/41419140/) | 2026 | Formulation Study | European Journal of Pharmaceutical Sciences | Developed a topical nanosponge gel co-delivering baricitinib and tenoxicam for RA; high drug-loading efficiency (67.0% BAR, 82.1% TNX) with amorphised drug state. |

---

## UK Market Information

Tenoxicam does not currently hold a UK marketing authorisation. `taiwan_regulatory` (used here as the regulatory data field) records **0 licences** and a market status of **Not Marketed**, so no product-level authorisation table can be provided. Any UK deployment of tenoxicam for RA would require a new marketing authorisation pathway (e.g. via MHRA), as no existing licensed product is available to reference against BNF classification.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is currently available in the Evidence Pack — please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Supplementary pharmacovigilance note:** A case report identified elsewhere in this Evidence Pack ([PMID 9303679](https://pubmed.ncbi.nlm.nih.gov/9303679/), *Atención Primaria*, 1997) describes alopecia as a possible adverse effect of tenoxicam. This is unrelated to the RA indication under evaluation but should be noted for future pharmacovigilance monitoring.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Tenoxicam has decades of RCT-level clinical evidence supporting efficacy in RA, but this largely confirms an already-established NSAID indication rather than representing a novel repurposing hypothesis, and two data gaps are flagged as blocking/high-severity in the Evidence Pack: mechanism of action detail (DG002) and, critically, TFDA/product label warnings and contraindications (DG001, marked **Blocking**), which currently prevents a formal S1 safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain full SmPC/product label warnings and contraindications before any safety assessment can proceed
- Resolve DG002: confirm mechanism of action via DrugBank or equivalent pharmacological reference
- Clarify UK regulatory pathway, given 0 current marketing authorisations
- Reassess whether this candidate should be reclassified as "confirmatory of existing use" rather than a novel repurposing opportunity, given the strength of pre-existing RA evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

