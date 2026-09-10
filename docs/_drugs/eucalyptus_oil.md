---
layout: default
title: Eucalyptus Oil
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Eucalyptus Oil
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

# Eucalyptus Oil: From Traditional Topical Remedy to Osteoarthritis

## One-Sentence Summary

Eucalyptus oil has a long history of traditional topical and inhalation use for minor musculoskeletal and respiratory complaints, but it holds no UK marketing authorisation and no formal original indication is on file. The TxGNN model predicts potential effectiveness for **Osteoarthritis**, supported by **1 clinical trial** and **3 publications** — though the trial tested a multi-ingredient herbal blend rather than eucalyptus oil alone, making the evidence indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no UK marketing authorisation or formally recorded indication (traditional topical/aromatherapy use only) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, eucalyptus oil is a volatile essential oil traditionally applied topically or by inhalation for its counter-irritant and mild anti-inflammatory properties; it does not currently hold a UK marketing authorisation as a licensed medicine.

Mechanistically, the plausibility rests largely on 1,8-cineole (eucalyptol), the principal constituent of eucalyptus oil. Preclinical and *in silico* work identified in the related rheumatoid arthritis prediction (PMID 38649658) shows eucalyptol reduces pro-inflammatory mediators (IL-17, NF-κB, COX-2, 5-LOX) in an adjuvant-induced arthritis model, offering a biological rationale that could extend to osteoarthritic joint inflammation.

However, the key caveat is that the pivotal osteoarthritis trial (NCT01684371) tested "Elmore Oil" — a combination product of eucalyptus oil, tea tree oil, olive oil and vanilla — not eucalyptus oil as a single agent. The evidence pack itself grades this trial's relevance as "C" (indirect), and the remaining literature consists mainly of unrelated drug-delivery/formulation studies that merely use eucalyptus oil as an excipient rather than as the active therapeutic agent being tested.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01684371](https://clinicaltrials.gov/study/NCT01684371) | N/A | Completed | 60 | Double-blind, placebo-controlled crossover trial of Elmore Oil (a herbal blend containing eucalyptus oil, tea tree oil, olive oil and vanilla) applied topically for osteoarthritis pain and stiffness. Note: tests a multi-component product, not eucalyptus oil alone. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15778570](https://pubmed.ncbi.nlm.nih.gov/15778570/) | 2005 | Observational/Interventional | Taehan Kanho Hakhoe chi | Aromatherapy (including eucalyptus) evaluated for effects on pain, depression and life satisfaction in arthritis patients. |
| [37111672](https://pubmed.ncbi.nlm.nih.gov/37111672/) | 2023 | Review | Pharmaceutics | Overview of nanoemulgel drug-delivery systems for topical anti-inflammatory therapy; eucalyptus oil discussed as a formulation excipient rather than active agent. |
| [38409718](https://pubmed.ncbi.nlm.nih.gov/38409718/) | 2024 | Formulation study | Anti-inflammatory & Anti-allergy Agents in Medicinal Chemistry | Development of a celecoxib emulgel using natural oil as an excipient for osteoarthritis and rheumatoid arthritis pain relief; celecoxib, not eucalyptus oil, is the active drug studied. |

---

## UK Market Information

Eucalyptus oil is not currently marketed in the UK under a formal MHRA marketing authorisation — no licences are on file (0 of 0). It is only encountered as an ingredient in traditional topical rubs, inhalant preparations or aromatherapy products, which fall outside licensed medicine status.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Additional signal from the evidence pack:** a lower-ranked TxGNN prediction (hepatic porphyria, rank 4) is explicitly flagged by the evidence analysis as a *safety concern rather than a treatment opportunity* — terpene-containing essential oils such as eucalyptus oil are traditionally considered a possible porphyria trigger. This should be treated as a caution point for any future evaluation, not pursued as an indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists — no MHRA/SmPC warnings, contraindications or DDI data are available, so a basic safety review cannot be completed. The single supporting clinical trial tested a multi-ingredient herbal product rather than eucalyptus oil alone (graded "C"/indirect relevance by the evidence pack), and no dedicated RCT of eucalyptus oil monotherapy in osteoarthritis exists. Combined with L3 evidence and the drug's unlicensed status in the UK, this does not yet support progression.

**To proceed, the following is needed:**
- MHRA/SmPC-equivalent safety data (warnings, contraindications, drug interactions) for eucalyptus oil
- Documented mechanism of action specific to eucalyptus oil (not just its constituent eucalyptol)
- A dedicated randomised controlled trial of eucalyptus oil monotherapy (topical) in osteoarthritis, distinct from combination herbal products
- Clarification of the porphyria safety signal before any further repurposing work proceeds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

