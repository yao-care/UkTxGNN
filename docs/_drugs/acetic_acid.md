---
layout: default
title: Acetic Acid
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Acetic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acetic Acid: From Topical Antimicrobial Use to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is a widely used topical antimicrobial agent with established clinical applications in wound irrigation, chronic wound management, and as a diagnostic reagent in cervical cancer screening (Visual Inspection with Acetic Acid, VIA), but holds no current MHRA marketing authorisation as a standalone licensed medicine in the United Kingdom. The TxGNN model predicts it may have therapeutic potential for **post-bacterial disorder**, with **1 completed Phase 1 clinical trial** of an acetic acid-based formulation (SoftOx Biofilm Eradicator) providing the most directly relevant safety evidence to date. Of note, the highest-quality evidence across this entire Evidence Pack is found for **tinea corporis** (rank 9, L3, "Proceed with Guardrails"), which may represent a more immediately actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No MHRA marketing authorisation; known clinical uses include topical antimicrobial (wound care, otitis externa) and diagnostic reagent (VIA for cervical screening) |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological properties, acetic acid exerts its antimicrobial effects primarily by lowering local tissue pH to below 4.5, which disrupts bacterial cell membrane integrity, inhibits biofilm formation, and suppresses residual bacterial colonisation. This well-characterised mechanism underpins its established use in wound irrigation — particularly for wounds colonised by organisms such as *Pseudomonas aeruginosa* — and is the basis of the SoftOx Biofilm Eradicator (SBE) formulation that has progressed to Phase 1 clinical evaluation.

The connection to **post-bacterial disorder** — a broad category encompassing sequelae arising in the aftermath of bacterial infection — is mechanistically plausible but remains highly speculative. By reducing residual bacterial burden, acetic acid could theoretically curtail the ongoing inflammatory stimulus that drives post-bacterial tissue damage, microenvironmental disruption, or secondary complications such as chronic wound breakdown. The completion of NCT05710094 (SoftOx, Phase 1, chronic leg wounds) provides indirect safety evidence for topically applied acetic acid-based formulations in a post-bacterial wound context.

However, 'post-bacterial disorder' is a heterogeneous and clinically imprecise category. There are currently no direct studies examining acetic acid's therapeutic role in resolving post-bacterial systemic sequelae — such as post-streptococcal glomerulonephritis, reactive arthritis, or post-infectious functional syndromes — and the high TxGNN score reflects network topology adjacency within the knowledge graph rather than any validated clinical efficacy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT05710094](https://clinicaltrials.gov/study/NCT05710094) | Phase 1 | Completed | 28 | SoftOx Biofilm Eradicator (SBE) — an acetic acid-based biofilm-disrupting antimicrobial — assessed for safety and tolerability via randomised, double-blinded, placebo-controlled single-dose escalation and open-label once/twice/thrice-daily dosing for five days in patients with chronic leg wounds; provides the most direct clinical safety data for acetic acid in an antimicrobial wound care context |
| [NCT04657757](https://clinicaltrials.gov/study/NCT04657757) | N/A | Completed | 16 | Ex vivo investigation of bacterial adhesion and bactericide effects on different implant restoration materials; offers mechanistic data on antimicrobial surface properties relevant to acetic acid's mode of action in post-bacterial tissue environments, though the scale is limited |
| [NCT03212729](https://clinicaltrials.gov/study/NCT03212729) | N/A | Completed | 10 | Antimicrobial photodynamic therapy (aPDT) as an adjunct to conventional endodontic treatment in teeth with primary bacterial endodontic infections (*Enterococcus faecalis*, *Candida* sp.); acetic acid is not the primary intervention but the bacterial eradication setting is contextually relevant |
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Randomised controlled trial comparing apple cider vinegar (acetic acid-containing) plus metformin versus metformin alone in newly diagnosed type 2 diabetes; provides indirect systemic tolerability data for oral acetic acid, though the indication is metabolic rather than post-bacterial |

> **Note:** A total of 18 clinical trials were retrieved for this drug–indication query. The majority have low direct relevance to acetic acid as a therapeutic agent specifically for post-bacterial disorder (reflecting broad retrieval criteria). Only trials with moderate or higher relevance are presented above.

---

## Literature Evidence

Currently no related literature available for post-bacterial disorder.

---

## UK Market Information

Acetic acid does not currently hold any MHRA marketing authorisations as a standalone licensed medicine in the United Kingdom.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| No MHRA-licensed standalone products identified | — | — | — |

Acetic acid is present as an excipient in various licensed pharmaceutical preparations and is employed in clinical practice as an unlicensed topical agent for wound care and otitis externa, and as a diagnostic reagent in VIA cervical screening programmes. Any development as a licensed medicinal product for a new indication would require a full marketing authorisation application to the MHRA.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN model's high prediction score (99.98%) for post-bacterial disorder reflects knowledge graph network topology rather than clinical validation. Whilst acetic acid's antimicrobial mechanism is well established and a completed Phase 1 trial of an acetic acid-based formulation (SoftOx, NCT05710094) confirms tolerability in chronic wound patients, there is currently no direct clinical or preclinical evidence supporting acetic acid as a treatment for post-bacterial disorder as a defined therapeutic indication. The L4 evidence classification and absence of any relevant published literature mean that clinical development for this specific target cannot be justified at this stage.

**Important secondary finding:** Across all ten predicted indications in this Evidence Pack, **tinea corporis** (ringworm, rank 9) carries the highest evidence grade — **L3, "Proceed with Guardrails"** — with mechanistic plausibility (antifungal activity via acidification to pH <4.5, inhibiting dermatophyte growth), historical clinical case series from the 1940s–1950s (PMID 20983383, 20996178, 20256868), a modern non-inferiority RCT evaluating vinegar-based treatment for tinea corporis (PMID 37012894), and additional observational data for tinea pedis and onychomycosis. This indication may represent a more immediately actionable repurposing direction and warrants a dedicated review.

**To advance post-bacterial disorder to the next development stage, the following is needed:**

- A precise clinical definition of the target post-bacterial condition (e.g., chronic wound post-bacterial complications, post-streptococcal sequelae, post-infectious IBS)
- Preclinical (in vitro and/or animal model) proof-of-concept studies in a well-defined post-bacterial disease model
- Mechanistic data specifically confirming acetic acid's role in post-bacterial tissue repair, microbiome restoration, or immune modulation
- Identification of an appropriate formulation, dose, and route of administration for the target indication
- MHRA pre-submission advice regarding the regulatory pathway for a novel medicinal indication in a substance currently unlicensed as a standalone medicine
- NICE engagement for early health technology assessment scoping
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

