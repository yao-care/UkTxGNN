---
layout: default
title: Acemetacin
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 1
---

# Acemetacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Acemetacin: From Pain and Inflammation to Osteoarthritis Susceptibility

## One-Sentence Summary

Acemetacin is a non-steroidal anti-inflammatory drug (NSAID) and ester prodrug of indomethacin, used in several European countries for the symptomatic management of pain and inflammation in musculoskeletal conditions, though it holds no current UK marketing authorisation.
The TxGNN model predicts it may have relevance for **Osteoarthritis Susceptibility** — a target that extends beyond symptomatic relief into potential disease-modifying territory.
Currently, **no registered clinical trials** and **no published literature** directly support this specific predicted indication, placing the evidence at the lowest tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain and inflammation in musculoskeletal conditions (no UK marketing authorisation) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Acemetacin is an ester prodrug of indomethacin. Following oral administration, it undergoes hydrolysis to release indomethacin, a potent inhibitor of both COX-1 and COX-2 cyclo-oxygenase enzymes. By suppressing prostaglandin synthesis, acemetacin reduces joint inflammation and attenuates pain signalling — precisely the mechanism underpinning the established use of NSAIDs as first-line symptomatic agents in osteoarthritis. The prodrug design was intended to reduce the gastrointestinal tolerability burden associated with indomethacin itself, making it pharmacologically well suited to the chronic dosing that OA management typically requires.

The specific predicted target — **osteoarthritis susceptibility** — warrants careful interpretation. As a knowledge graph phenotype node, "susceptibility" extends beyond symptom control into the realm of disease modification (DMOAD activity), asking whether the drug can alter the underlying course of cartilage degradation rather than merely palliate symptoms. Whilst COX inhibition is clearly effective for the inflammatory component of OA, evidence for genuine disease-modifying effects of NSAIDs in OA remains inconclusive; indeed, some preclinical and observational data suggest that prolonged COX inhibition may adversely affect chondrocyte metabolism and potentially accelerate cartilage loss, which is the opposite of what a DMOAD should achieve.

Mechanistic support therefore sits at a **medium level**: robust for symptomatic pain and inflammation relief, but uncertain — and potentially concerning — for susceptibility modification. The high TxGNN prediction score (99.22%) most likely reflects the strong pharmacological affinity between this drug class and OA-related biological targets in the knowledge graph, rather than confirmed disease-modifying activity in human studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Whilst the TxGNN model assigns a high prediction score and the mechanistic rationale for NSAID activity in OA is pharmacologically coherent, the specific target node (osteoarthritis *susceptibility*) implies disease modification for which there is no supporting clinical trial or published literature evidence (L5); additionally, acemetacin holds no UK marketing authorisation, creating a substantial regulatory barrier before any clinical translation could be considered.

**To proceed, the following is needed:**

- **Target clarification**: Determine whether the intended benefit is symptomatic OA management (where class-level NSAID evidence is extensive) or true disease susceptibility modification (where evidence is lacking and COX inhibition may be detrimental)
- **SmPC retrieval**: Obtain the Summary of Product Characteristics from a jurisdiction where acemetacin is authorised (e.g., Germany, Switzerland) to characterise contraindications, warnings, and drug interactions
- **MOA data**: Retrieve detailed mechanism of action data from DrugBank (DB13783) to support a structured mechanistic analysis
- **Proxy evidence review**: Commission a scoping review of indomethacin and related NSAID prodrug data in OA clinical trials as a surrogate evidence base, given acemetacin's known metabolic equivalence
- **UK regulatory pathway assessment**: Evaluate the requirements for an MHRA marketing authorisation application, including whether existing European data packages could support a UK licence submission
- **DMOAD safety signal review**: Assess the long-term chondrotoxicity literature for COX inhibitors to confirm the risk–benefit profile before progressing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

