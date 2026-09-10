---
layout: default
title: Epinastine
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Epinastine
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

# Epinastine: From Allergic Disease to Allergic Urticaria

## One-Sentence Summary

Epinastine is a second-generation H1-antihistamine/mast-cell stabiliser, historically marketed abroad (as Alesion) for allergic rhinitis, atopic dermatitis and allergic conjunctivitis. The TxGNN model's top-ranked candidate for this drug (rosacea conjunctivitis, 99.57%) is unsupported by any trial or literature and has therefore not been carried forward; the best-supported repurposing signal is instead **Allergic Urticaria**, backed by **2 post-marketing surveillance studies** (n=3,793 and n=2,001) and **11 publications**, including two randomised comparisons of antihistamine wheal-and-flare suppression.

> **Note on candidate selection:** TxGNN's raw #1-ranked prediction for epinastine was *rosacea conjunctivitis* (score 99.57%), but the evidence pack itself flags this as a purely computational link with no supporting trials, no literature, and a weak mechanistic rationale (Hold). *Allergic urticaria* (rank 2, score 99.28%) is used as the primary indication in this report because it is the only candidate with actual clinical and literature support and a decision stage beyond S0.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for this market (epinastine is unlicensed here; no `taiwan_regulatory.licenses` entries exist). Published literature describes established use abroad, as "Alesion", for allergic rhinitis, atopic dermatitis/eczema, and allergic conjunctivitis. |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data was not returned in this evidence pack (`original_moa: [Data Gap]`, tracked as gap **DG002**). Based on the literature retrieved alongside this candidate, epinastine is a potent H1-receptor antagonist that also stabilises mast cells and suppresses antileukotriene, anti-PAF and antibradykinin pathways, and inhibits mediator release from mast cells and eosinophils (PMID 12845334). This is a well-characterised, class-typical antiallergic profile shared with other second-generation antihistamines.

Allergic urticaria is a histamine/mast-cell-mediated condition — the pathology is essentially the same wheal-and-flare mechanism that H1-antagonists like epinastine are designed to block. Critically, the trial-level rationale in this pack notes that Alesion (epinastine) is **already approved in Japan for urticaria**, meaning this is best understood as a label-extension into a market where the drug is not yet authorised, rather than a novel mechanistic hypothesis. This substantially de-risks the pharmacological plausibility compared with a genuinely new mechanism-of-action claim.

By contrast, the model's highest-scoring candidate (rosacea conjunctivitis) does not share this histamine-driven pathology — rosacea-associated conjunctivitis is primarily vascular and sebaceous in origin — which is consistent with the complete absence of supporting trials or literature for that candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02238236](https://clinicaltrials.gov/study/NCT02238236) | N/A (Post-marketing surveillance) | Completed | 3,793 | Real-world safety/efficacy of Alesion® Dry Syrup in Japanese paediatric patients with allergic rhinitis, eczema/dermatitis, urticaria and pruritus. |
| [NCT02238223](https://clinicaltrials.gov/study/NCT02238223) | N/A (Post-marketing surveillance) | Completed | 2,001 | Real-world safety/efficacy of Alesion® Tablet under updated treatment guidance for allergic rhinitis, asthma, eczema, dermatitis, urticaria, pruritus, prurigo and psoriasis vulgaris with itching. |

*Both studies are large post-marketing surveillance programmes rather than randomised controlled trials — they support real-world usage experience and safety signal detection but cannot establish efficacy causation on their own.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/) | 1999 | RCT | Allergy | Double-blind, single-dose, crossover study; epinastine (with cetirizine, ebastine, fexofenadine, terfenadine, loratadine) suppressed histamine-induced wheal-and-flare for 24h vs placebo. |
| [19558008](https://pubmed.ncbi.nlm.nih.gov/19558008/) | 2009 | RCT | Ann Allergy Asthma Immunol | Compared first- vs second-generation antihistamines in suppressing histamine- and allergen-induced skin reactions, the core mechanism underlying urticaria control. |
| [12845334](https://pubmed.ncbi.nlm.nih.gov/12845334/) | 2000 | Review | Drugs of Today | Overview of epinastine's antihistaminic, antileukotriene, anti-PAF and antibradykinin activity, and mast-cell/eosinophil mediator inhibition. |
| [15510239](https://pubmed.ncbi.nlm.nih.gov/15510239/) | 2004 | Review | Drugs of Today | Epinastine's role across atopic conditions (allergic rhinitis, atopic eczema, allergic conjunctivitis, asthma) and comparative side-effect profile. |
| [11829715](https://pubmed.ncbi.nlm.nih.gov/11829715/) | 2002 | Review | Expert Opin Investig Drugs | Discusses shared histamine-driven mechanisms across allergic rhinitis, asthma, allergic conjunctivitis and chronic idiopathic urticaria (CIU). |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Cohort | Methods Find Exp Clin Pharmacol | Large-scale surveillance (n=1,742) of sedative profiles across H1-antihistamines including epinastine, relevant to tolerability. |
| [34387278](https://pubmed.ncbi.nlm.nih.gov/34387278/) | 2021 | Receptor pharmacology | Curr Opin Allergy Clin Immunol | Reviews receptor-affinity profiles of ophthalmic/systemic antiallergic agents, contextualising epinastine's target engagement. |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Comparative pharmacology study | An Bras Dermatol | Compared wheal-and-flare suppression by first-generation antihistamines marketed in Brazil, including epinastine's class comparators. |
| [10876807](https://pubmed.ncbi.nlm.nih.gov/10876807/) | 2000 | Pharmacology review | Nihon Yakurigaku Zasshi | Cetirizine pharmacology paper benchmarking wheal-response inhibition against terfenadine, loratadine, epinastine and ebastine. |
| [18524543](https://pubmed.ncbi.nlm.nih.gov/18524543/) | 2008 | Immunology study | J Dermatol Sci | Examines antihistamine regulatory effects on dendritic cells/T cells relevant to urticaria and atopic dermatitis pathogenesis. |

---

## UK Market Information

Epinastine currently holds **no marketing authorisation** in this jurisdiction (`market_status: 未上市` / Not marketed; `total_licenses: 0`). No product entries are available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Formal warnings, contraindications and drug-interaction data for epinastine were not available in this evidence pack (data gap **DG001**, flagged Blocking — required before any safety pre-assessment can proceed).*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Allergic urticaria has a mechanistically coherent, class-consistent rationale, supported by two large post-marketing surveillance programmes and RCT-level evidence for the underlying wheal-and-flare mechanism, plus an existing overseas approval (Japan, Alesion) for this exact indication — this is a label-extension case rather than a speculative new mechanism.

**To proceed, the following is needed:**
- Formal MOA/pharmacological classification from DrugBank (gap DG002)
- TFDA-equivalent product warnings, contraindications and DDI profile — currently blocking (gap DG001)
- A locally-run or bridging clinical study, since existing evidence is PMS/overseas RCT data rather than a local pivotal trial
- Formal review of route/formulation compatibility (oral vs ophthalmic) for the urticaria indication, which was not resolved in this evidence pack
- A regulatory pathway assessment for seeking marketing authorisation, given epinastine is currently unlicensed in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

