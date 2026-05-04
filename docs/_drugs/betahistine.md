---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Betahistine
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

# Betahistine: From Ménière's Disease to Peripheral Vertigo

> **DISCLAIMER:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.

---

## One-Sentence Summary

Betahistine is a histamine analogue widely established in clinical practice as a first-line treatment for Ménière's disease and vestibular vertigo, acting as a weak H1 receptor agonist and potent H3 receptor antagonist to improve inner ear blood flow and accelerate vestibular compensation.
The TxGNN model predicts it may be effective for **Peripheral Vertigo** — the highest-evidence predicted indication in this evidence pack — supported by **4 clinical trials** and **20 publications**.
Of note, the top TxGNN-ranked novel prediction is **Restless Legs Syndrome** (score: 98.51%), but this currently carries no clinical evidence (L5, Hold); the peripheral vertigo indication is recommended to **Proceed with Guardrails** at evidence level L1.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ménière's disease / vestibular vertigo (inferred from clinical literature — UK MHRA licence data not captured in this evidence pack; see note below) |
| Top TxGNN-Predicted Novel Indication | Restless Legs Syndrome |
| Highest-Evidence Predicted Indication | Peripheral Vertigo |
| TxGNN Prediction Score | 98.51% (Restless Legs Syndrome) / 98.07% (Peripheral Vertigo) |
| Evidence Level | L1 (Peripheral Vertigo); L5 (Restless Legs Syndrome) |
| UK Market Status | Not captured — **likely a data gap** (Serc® is listed in the BNF; see note below) |
| Number of UK Marketing Authorisations | 0 recorded (data gap — MHRA data not retrieved) |
| Recommended Decision | **Proceed with Guardrails** (Peripheral Vertigo); **Hold** (Restless Legs Syndrome) |

> ⚠️ **UK Market Data Note:** This evidence pack records zero MHRA licences for betahistine. This is almost certainly a data capture gap. Betahistine dihydrochloride (Serc®) is listed in the **British National Formulary (BNF) section 4.6** (*Drugs used in nausea and labyrinthine disorders*) and is understood to hold an MHRA marketing authorisation for Ménière's disease. Clinicians should verify the current status via the [MHRA Product Database](https://products.mhra.gov.uk/) before any prescribing decision.

---

## Why is This Prediction Reasonable?

Betahistine is a structural analogue of histamine with dual receptor activity. Detailed mechanism of action data is not available in the current evidence pack (a DrugBank data gap has been flagged), but the extensive clinical literature contained within this evidence pack allows a well-founded mechanistic account. Betahistine acts as a **weak agonist at H1 receptors**, promoting vasodilation of cochlear and labyrinthine microvasculature and improving inner ear blood flow. Simultaneously, it acts as a **potent inverse agonist at presynaptic H3 receptors** in the vestibular nuclei, increasing local histamine and dopamine neurotransmitter release, thereby accelerating central vestibular compensation and reducing both the frequency and severity of vertigo attacks.

Peripheral vertigo is an umbrella clinical category encompassing Ménière's disease, benign paroxysmal positional vertigo (BPPV), vestibular neuritis, and labyrinthitis — all characterised by disrupted inner ear fluid homeostasis or impaired vestibular afferent signalling. Since betahistine is already established for Ménière's disease (the most common form of peripheral vertigo), TxGNN's prediction that betahistine is effective for the broader peripheral vertigo spectrum represents a logical and mechanistically coherent extension. The H1-mediated improvement in endolymphatic circulation and H3-mediated acceleration of central vestibular compensation are applicable across all major peripheral vestibular aetiologies.

The European Academy of Otology and Neurotology (EAONO) 2018 Position Statement, two separate Cochrane systematic reviews (2016, 2023), a meta-analysis of 12 double-blind RCTs, and the large multicentre BEMED Phase 3 trial collectively provide high-quality L1 evidence that betahistine is clinically effective across the peripheral vertigo spectrum. The TxGNN model prediction is fully supported by this body of evidence.

---

## Predicted Indication Summary Table

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|------------|---------------|---------|
| 1 | Restless Legs Syndrome | 98.51% | L5 | Hold |
| 2 | Active Cochlear Ménière's Disease | 98.34% | L4 | Research Question |
| 3 | Active Cochleovestibular Ménière's Disease | 98.34% | L5 | Hold |
| **4** | **Active Vestibular Ménière's Disease** | **98.34%** | **L2** | **Proceed with Guardrails** |
| 5 | Otosclerosis | 98.19% | L4 | Research Question |
| **6** | **Peripheral Vertigo** | **98.07%** | **L1** | **Proceed with Guardrails** |
| 7 | Age-Related Hearing Impairment | 97.93% | L5 | Hold |
| 8 | Vertigo, Benign Recurrent, Type 2 | 97.78% | Pending | Pending |
| 9 | Autosomal Recessive Hyperinsulinism (Kir6.2) | 97.77% | L5 | Hold ⚠️ |
| 10 | Hyperinsulinemic Hypoglycaemia, Familial | 97.32% | L5 | Hold ⚠️ |

> ⚠️ **Safety concern for Ranks 9 & 10:** The mechanistic rationale for the hyperinsulinism indications is contradictory — betahistine's H3 antagonism may *promote* rather than inhibit insulin secretion, which is counter-therapeutic and potentially harmful in congenital hyperinsulinism. These indications should not be pursued without extensive preclinical safety evaluation.

---

## Clinical Trial Evidence

*Primary focus: Peripheral Vertigo (Rank 6, L1 evidence). Trials for Restless Legs Syndrome: none registered.*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01759251](https://clinicaltrials.gov/study/NCT01759251) | Observational (Post-marketing) | Completed | 309 | International post-marketing observational programme of Betaserc® (betahistine dihydrochloride) in outpatients with vestibular vertigo in Russia and Ukraine; evaluates real-world effectiveness and course of symptoms after treatment discontinuation |
| [NCT03908567](https://clinicaltrials.gov/study/NCT03908567) | Phase 2 | Completed | 124 | TRAVERS trial: AM-125 (novel intranasal betahistine formulation) versus placebo for acute peripheral vertigo following vestibular schwannoma neurosurgery; proof-of-concept RCT demonstrating betahistine efficacy via an alternative route of administration |
| [NCT07203248](https://clinicaltrials.gov/study/NCT07203248) | Observational | Not yet recruiting | 2,000 | Real-world study of CGRP-targeted medications for vestibular migraine in Chinese patients; betahistine may appear as comparator or background therapy — **low direct relevance** |
| [NCT06001047](https://clinicaltrials.gov/study/NCT06001047) | N/A | Recruiting | 120 | Head acupuncture versus sham acupuncture for residual dizziness following canalith repositioning in BPPV; betahistine role as background therapy only — **low direct relevance** |

---

## Literature Evidence

*Primary focus: Peripheral Vertigo (Rank 6). Top 10 most relevant publications selected from 20 retrieved.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | Phase 3 RCT (BEMED) | *BMJ* | Landmark multicentre, double-blind, placebo-controlled, dose-defining trial of betahistine (24 mg bd vs 48 mg bd vs placebo) in Ménière's disease; primary endpoint — vertigo attack frequency over 9 months |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Cochrane Systematic Review | *Cochrane Database Syst Rev* | Comprehensive Cochrane review of systemic pharmacological interventions for Ménière's disease, including betahistine, diuretics, antivirals, and corticosteroids; current best evidence synthesis |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Cochrane Systematic Review | *Cochrane Database Syst Rev* | Betahistine for symptoms of vertigo from multiple causes; concludes betahistine may work by improving blood flow to the inner ear; reviews all available RCT evidence |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | Meta-analysis | *Eur Arch Otorhinolaryngol* | Meta-analysis of 12 double-blind, randomised, placebo-controlled trials of betahistine in vestibular vertigo and Ménière's disease; introduces the odds of favourable treatment outcome as an effect parameter |
| [30256205](https://pubmed.ncbi.nlm.nih.gov/30256205/) | 2018 | Clinical Practice Guideline | *J Int Adv Otology* | EAONO European Position Statement on diagnosis and treatment of Ménière's disease; betahistine recognised as a standard first-line medical treatment |
| [40070497](https://pubmed.ncbi.nlm.nih.gov/40070497/) | 2025 | Systematic Review & Meta-analysis | *World J Otorhinolaryngol Head Neck Surg* | Betahistine as add-on therapy to Epley manoeuvre for BPPV; meta-analysis assessing effectiveness in reducing residual dizziness |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Review | *Acta Oto-Laryngologica* | Narrative review demonstrating betahistine's efficacy and safety across multiple peripheral vertigo subtypes: Ménière's disease, BPPV, vestibular neuronitis, and other causes |
| [24177346](https://pubmed.ncbi.nlm.nih.gov/24177346/) | 2013 | Review / Mechanistic Discussion | *J Vestibular Res* | Mechanistic review of betahistine's role in vestibular compensation; clarifies H1/H3 receptor pathways and their relevance to symptom relief and vestibular recovery |
| [32530417](https://pubmed.ncbi.nlm.nih.gov/32530417/) | 2020 | Review | *Dtsch Arztebl Int* | Comprehensive current review of peripheral, central, and functional vestibular vertigo syndromes including pathophysiology, genetics, and pharmacotherapy |
| [31111729](https://pubmed.ncbi.nlm.nih.gov/31111729/) | 2020 | Observational Cohort | *Ear Nose Throat J* | Real-life primary care study of betahistine 48 mg/day for peripheral vestibular vertigo (n=150); establishes clinical effect and safety in routine practice settings |

---

### Supporting Literature: Active Vestibular Ménière's Disease (Rank 4, L2 evidence)

*Top 5 publications from 19 retrieved for this subtype:*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19300572](https://pubmed.ncbi.nlm.nih.gov/19300572/) | 2007 | Review / Clinical Analysis | *Neuropsychiatr Dis Treat* | Betahistine (Serc®/BetaSerc®) as the mainstay of drug treatment for Ménière's disease and vestibular system disorders; discusses clinical evidence and role in vestibular compensation |
| [22365373](https://pubmed.ncbi.nlm.nih.gov/22365373/) | 2012 | RCT (Comparative) | *J Laryngol Otol* | RCT of transtympanic low-pressure therapy in patients with unilateral Ménière's disease unresponsive to betahistine; provides evidence for betahistine as the established standard treatment comparator |
| [37528598](https://pubmed.ncbi.nlm.nih.gov/37528598/) | 2023 | Observational Cohort | *J Int Adv Otology* | Associations between medical therapy (including betahistine), self-administered exercise, and Ménière's disease characteristics; real-world effectiveness data |
| [7113814](https://pubmed.ncbi.nlm.nih.gov/7113814/) | 1982 | Clinical Study (Long-term follow-up) | *Adv Otorhinolaryngol* | Long-term evaluation of betahistine HCl over 12–14 years; success rate >80% with no habituation; supports sustained long-term efficacy |
| [29942281](https://pubmed.ncbi.nlm.nih.gov/29942281/) | 2018 | Animal Model (PK/PD) | *Front Neurol* | Pharmacokinetic and pharmacodynamic analysis of betahistine in unilateral vestibular neurectomised cats; betahistine doses comparable to human therapeutic levels demonstrate vestibular recovery effects |

---

### Supporting Literature: Active Cochlear Ménière's Disease (Rank 2, L4 evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26139562](https://pubmed.ncbi.nlm.nih.gov/26139562/) | 2015 | Mechanistic Study (Animal/Ex vivo) | *Audiol Neurootol* | H3 heteroreceptors as mediators of betahistine-induced increase in cochlear blood flow; adrenergic α2-receptor involvement also investigated; provides mechanistic basis for cochlear Ménière's subtype |
| [28818391](https://pubmed.ncbi.nlm.nih.gov/28818391/) | 2017 | Mechanistic Study (Animal/Tissue) | *Life Sci* | Role of capillary pericytes and precapillary arterioles in betahistine's vascular mechanism in a guinea pig inner ear model; betahistine increases local blood flow in stria vascularis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| *Not retrieved — data gap* | Serc® (betahistine dihydrochloride) — *expected* | Tablet (8 mg, 16 mg, 24 mg) — *expected* | Ménière's disease (vertigo, tinnitus, hearing loss) — *expected* |

Betahistine dihydrochloride is listed in **BNF section 4.6** (*Drugs used in nausea and labyrinthine disorders*) as a recognised treatment for Ménière's disease in the UK. NICE Clinical Knowledge Summaries (CKS) for Ménière's disease reference betahistine as a first-line medical management option. To retrieve the precise marketing authorisation details (PL number, approved indications text, SmPC), clinicians should consult the [MHRA products database](https://products.mhra.gov.uk/) directly.

---

## Safety Considerations

Please refer to the Summary of Product Characteristics (SmPC) and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** ([yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/)).

The current evidence pack contains no captured safety data for betahistine (all warnings, contraindications, and drug interactions are recorded as data gaps). Based on the drug's known histaminergic mechanism, clinicians should be aware of the following widely-recognised safety considerations pending retrieval of the SmPC:

- **Contraindication:** Phaeochromocytoma (risk of hypertensive crisis from histamine analogue activity)
- **Caution:** Peptic ulcer disease or history thereof (H1 agonism may increase gastric acid secretion)
- **Caution:** Asthma and other bronchospastic conditions (potential bronchoconstriction)
- **Caution:** Use in children — limited evidence; not routinely recommended in paediatric patients
- **Drug interactions:** Betahistine may antagonise the effects of H1-antihistamines; theoretical interaction with MAO inhibitors (betahistine is metabolised via MAO)

These precautions are widely referenced in published clinical literature and standard formularies but should be confirmed from the full SmPC before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Betahistine has Level 1 evidence — including two Cochrane systematic reviews, a Phase 3 RCT (BEMED), and a meta-analysis of 12 RCTs — supporting its clinical effectiveness across the peripheral vertigo spectrum. The TxGNN prediction is pharmacologically coherent and clinically consistent with established use. However, the UK regulatory data in this evidence pack is incomplete and must be independently verified before any clinical action is taken.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm current MHRA marketing authorisation status, authorised indications, and approved dosing via the MHRA products database and current BNF/SmPC
- **Safety data completion:** Retrieve full SmPC to complete the safety assessment (contraindications, drug interactions, special population warnings) — this is currently flagged as a **Blocking data gap**
- **MOA documentation:** Obtain formal mechanism of action data from DrugBank API (currently a **High severity data gap**) to strengthen repurposing rationale
- **Novel indications (e.g., Restless Legs Syndrome):** Require preclinical mechanistic studies and Phase 1/2 clinical trials before any translation; H3 antagonism–dopamine interaction hypothesis needs validation in RLS animal models
- **High-risk novel indications (Ranks 9–10, hyperinsulinism):** Mechanistic direction is contradictory to therapeutic goals; recommend against further evaluation without resolution of the safety concern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

