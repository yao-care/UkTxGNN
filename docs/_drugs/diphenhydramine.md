---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic Symptom Relief to Allergic Rhinitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1-antihistamine long used over-the-counter for allergic symptoms; this evidence pack evaluated 10 TxGNN-predicted indications rather than a single new one. The two candidates with real supporting evidence — **Allergic Rhinitis** (98.35% TxGNN score, L1 evidence, 7 trials/18 papers) and **Allergic Urticaria** (98.24%, L2 evidence, 3 trials/19 papers) — both received "Proceed with Guardrails," but the evidence itself notes these are **established, not novel**, uses of the drug. The remaining 8 candidates (including the model's own top-ranked "rosacea conjunctivitis") have little or no supporting evidence and are recommended as Hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from UK regulatory data (data gap); diphenhydramine is a classic first-generation H1-antihistamine used for allergic reactions and insomnia |
| Predicted New Indication | Allergic Rhinitis (lead candidate; Allergic Urticaria closely follows — see below) |
| TxGNN Prediction Score | 98.35% (Rhinitis) / 98.24% (Allergic Urticaria) |
| Evidence Level | L1 (Rhinitis) / L2 (Allergic Urticaria) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

Note: the model's single highest-scoring prediction, **rosacea conjunctivitis** (99.20%), has zero supporting trials or literature and is scored L5/Hold — it is treated in the supplementary table below rather than as the headline indication.

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not supplied in this evidence pack (data gap). However, the evidence pack's own rationale fields consistently describe diphenhydramine as a first-generation H1-histamine receptor antagonist that directly blocks histamine-mediated nasal mucosal vasodilation, glandular secretion and itch reflexes — the classic pharmacology underlying allergic rhinitis — and equally blocks the histamine-driven mast cell mediator effects (wheal/flare, pruritus) that underlie urticaria.

Both allergic rhinitis and allergic urticaria are IgE/histamine-mediated conditions, so the mechanistic link to diphenhydramine is direct and well established rather than a genuinely novel repurposing signal. Indeed, the rationale text for rhinitis explicitly notes this is "非新穎關聯" (not a novel association) and for urticaria that the mechanism is "機轉明確且已廣泛臨床使用" (well-established and already in wide clinical use). In practice, TxGNN has re-identified the drug's own known therapeutic class rather than uncovered an unexpected new use — which is consistent with diphenhydramine's decades-long OTC use (e.g., Benadryl) for exactly these indications in other markets. The clinical opportunity for the UK is therefore less about "new indication discovery" and more about confirming feasibility of bringing a currently unlicensed product to the UK market for these already-supported uses.

---

## Clinical Trial Evidence

### Allergic Rhinitis

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | Completed | 1021 | Diphenhydramine 25 mg/50 mg vs placebo and pseudoephedrine for nasal congestion relief in seasonal allergic rhinitis — largest and most directly relevant trial (Grade A) |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | Completed | 36 | Pharmacokinetics of diphenhydramine in children and adolescents; supports paediatric dosing safety, not efficacy |
| [NCT00599872](https://clinicaltrials.gov/study/NCT00599872) | Phase 3 | Completed | 430 | Sublingual immunotherapy trial for ragweed-induced allergic rhinoconjunctivitis; diphenhydramine likely used only as rescue medication, not the primary intervention |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | Completed | 20 | Examines thermoregulatory effect of diphenhydramine during exercise; not an efficacy trial |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | Unknown | 16 | Thermoregulatory response during heat stress; small, status unknown |
| [NCT01177852](https://clinicaltrials.gov/study/NCT01177852) | Phase 3 | Withdrawn | 0 | Fixed-dose combination for paediatric cough/rhinitis; withdrawn, no data |
| [NCT01199497](https://clinicaltrials.gov/study/NCT01199497) | Phase 3 | Withdrawn | 0 | Fixed-dose combination for cough/rhinitis; withdrawn, no data |

### Allergic Urticaria

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicentre pilot comparing IV cetirizine 10 mg to IV diphenhydramine 50 mg for acute urticaria in emergency settings — direct head-to-head efficacy data (Grade A) |
| [NCT04660799](https://clinicaltrials.gov/study/NCT04660799) | Phase 2 | Completed | 50 | Rituximab PK/efficacy study in DLBCL; diphenhydramine relevance is incidental (premedication context) |
| [NCT05354466](https://clinicaltrials.gov/study/NCT05354466) | Phase 4 | Completed | 174 | Sugammadex vs neostigmine respiratory events in paediatric tonsillectomy; diphenhydramine likely only an incidental allergy-management drug |

---

## Literature Evidence

### Allergic Rhinitis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16680933](https://pubmed.ncbi.nlm.nih.gov/16680933/) | 2006 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine vs desloratadine vs placebo in moderate-to-severe seasonal allergic rhinitis |
| [8634878](https://pubmed.ncbi.nlm.nih.gov/8634878/) | 1996 | RCT | Ann Allergy Asthma Immunol | Learning impairment in seasonal allergic rhinitis patients treated with sedating vs non-sedating antihistamines |
| [14582817](https://pubmed.ncbi.nlm.nih.gov/14582817/) | 2003 | Cohort | Ann Allergy Asthma Immunol | Diphenhydramine vs desloratadine effects on vigilance and cognitive function during ragweed-induced allergic rhinitis treatment |
| [36420548](https://pubmed.ncbi.nlm.nih.gov/36420548/) | 2022 | Pilot Cohort | Tokai J Exp Clin Med | Transdermal diphenhydramine applied to the nasal ala in allergic rhinitis and asthma patients |
| [40152721](https://pubmed.ncbi.nlm.nih.gov/40152721/) | 2025 | Review | Med Lett Drugs Ther | Treatment of allergic rhinitis and allergic conjunctivitis |
| [33848281](https://pubmed.ncbi.nlm.nih.gov/33848281/) | 2021 | Review | Med Lett Drugs Ther | Drugs for allergic rhinitis and allergic conjunctivitis |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Oral antihistamines for allergic rhinitis and chronic idiopathic urticaria |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Review | Allergy Asthma Clin Immunol | CSACI position statement: newer-generation antihistamines preferred as first-line over first-generation agents |
| [36759413](https://pubmed.ncbi.nlm.nih.gov/36759413/) | 2023 | Preclinical | AAPS PharmSciTech | Diphenhydramine nasal nano-gel/nano-emulgel in an animal allergic rhinitis model |
| [29569155](https://pubmed.ncbi.nlm.nih.gov/29569155/) | 2018 | Preclinical | AAPS PharmSciTech | Formulation development of diphenhydramine nasal nano-emulgel |

### Allergic Urticaria

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Pathogenesis and treatment of chronic spontaneous urticaria, including antihistamine role |
| [34862952](https://pubmed.ncbi.nlm.nih.gov/34862952/) | 2022 | Review | Adv Ther | Narrative review of IV antihistamines for acute urticaria, contrasting IV diphenhydramine with newer IV cetirizine |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Review | Allergy Asthma Clin Immunol | CSACI position statement on first- vs second-generation antihistamines for urticaria |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Oral antihistamines for chronic idiopathic urticaria |
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Review | J Pediatr Pharmacol Ther | Review of diphenhydramine's clinical applications, including urticaria, and adverse effect profile |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1-antihistamines in children, including allergic and urticarial conditions |
| [15701213](https://pubmed.ncbi.nlm.nih.gov/15701213/) | 2004 | pending | Curr Med Res Opin | Notes first-generation antihistamines (diphenhydramine, hydroxyzine) as first-line treatment historically used for chronic idiopathic urticaria |

---

## Other TxGNN-Predicted Indications (Not Prioritised)

This evidence pack scored 10 candidate indications in total. Only rhinitis and allergic urticaria (above) had meaningful supporting evidence. The remaining candidates are summarised for completeness:

| Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---------|------------|-----------------|-----------------|------|
| Rosacea conjunctivitis | 99.20% | L5 | Hold | Model's top-ranked prediction, but no trials or literature; mechanistic rationale weak |
| Cold urticaria | 95.92% | L4 | Research Question | Plausible H1-mechanism, supported only by historical case reports/reviews (earliest from 1949), no controlled trials |
| Cauda equina syndrome | 95.57% | L5 | Hold | No mechanistic or evidentiary link to H1-antagonism; classified as prediction noise |
| Nasopharyngitis | 94.96% | L3 | Research Question | Antihistamines relieve allergy-like symptoms but have no antiviral effect; only 1 supporting RCT |
| Viral conjunctivitis | 93.97% | L5 | Hold | No trials or literature; no antiviral mechanism |
| Neuralgia | 92.30% | L5 | Hold | 5 retrieved trials all test unrelated drugs (telmisartan, lidocaine, topiramate); prediction mismatch |
| Trigeminal autonomic cephalalgia | 92.25% | L4 | Research Question | Historical case reports (1947–1952) on antihistamine use in histamine headache; one terminated combination trial |
| Glossodynia | 92.08% | L5 | Hold | No mechanistic rationale, trials or literature |

---

## UK Market Information

Diphenhydramine currently holds **no UK marketing authorisation** (market status: not marketed; 0 licences on record). No product name, dosage form or licensed indication text is available to summarise. Any UK development for allergic rhinitis or allergic urticaria would require a new marketing authorisation application (or reliance on an existing EU/US reference product), since no MHRA-authorised UK product exists to build on.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

(No structured key warnings, contraindications or drug-interaction data were available in this evidence pack — all fields were data gaps.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Allergic Rhinitis and Allergic Urticaria only)

**Rationale:**
- Allergic rhinitis (L1 evidence, one large Phase 4 RCT with n=1021, multiple supportive RCTs/reviews) and allergic urticaria (L2 evidence, a direct IV comparator Phase 3 pilot trial) both have credible, if not novel, evidence for diphenhydramine's efficacy via its well-established H1-antihistamine mechanism.
- These are not new mechanistic discoveries — they reconfirm diphenhydramine's known drug class use — but the drug has **no current UK marketing authorisation**, so guardrails are needed around regulatory pathway rather than pharmacology.
- All other predicted indications (rosacea conjunctivitis, cauda equina syndrome, viral conjunctivitis, neuralgia, glossodynia) lack credible evidence and should remain on Hold; cold urticaria, nasopharyngitis and trigeminal autonomic cephalalgia warrant only exploratory research questions.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent safety data: SmPC warnings, contraindications and drug–drug interaction profile (all currently data gaps, flagged Blocking in this evidence pack)
- Confirmation of a formal mechanism-of-action source (DrugBank query) rather than inferred rationale text
- A regulatory strategy for obtaining UK marketing authorisation, since diphenhydramine currently has zero UK licences
- Independent replication of the rhinitis/urticaria efficacy data specifically in a UK-relevant population, given existing trials are largely US/international
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

