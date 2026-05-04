---
layout: default
title: Bilastine
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Bilastine
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

# Bilastine: From Allergic Rhinoconjunctivitis to Allergic Urticaria

---

## One-Sentence Summary

Bilastine is a second-generation, non-sedating H1-antihistamine with established use in allergic rhinoconjunctivitis across multiple international markets, though formal original indication data was not retrieved in this evidence pack.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, supported by **6 clinical trials** (including a pivotal Phase 3 RCT, n=522) and **20 publications** — making this one of the most evidence-rich predictions in the current analysis.
Evidence is rated at **L1**, and the drug has received regulatory approval for urticaria by the EMA and UK MHRA (brand name Ilaxten), though authorisation details were not captured in this dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinoconjunctivitis (established from retrieved literature; formal indication text not retrieved in this dataset) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 86.43% |
| Evidence Level | L1 |
| UK Market Status | Not retrieved in this dataset — note: Bilastine is authorised in the UK as **Ilaxten** (MHRA) per published evidence in this pack |
| Number of Marketing Authorisations | 0 (not retrieved) |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN rankings:** The top-ranked TxGNN predictions by score (rank 1–6: duodenal obstruction, duodenal ulcer, duodenogastric reflux, gastric ulcer, leather-bottle stomach, duodenitis) all received a **Hold** recommendation with **L5 evidence** and no supporting clinical trials or literature. Mechanistic analysis indicates these predictions likely represent non-specific noise arising from shared gastrointestinal histamine pathway nodes in the knowledge graph. This report focuses on **Allergic Urticaria** (TxGNN rank 9), which carries the strongest evidence and the most plausible mechanistic basis.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the evidence pack (DrugBank API retrieval flagged as a data gap). However, based on published literature retrieved during evidence collection, Bilastine is a highly selective H1-histamine receptor inverse agonist. It binds competitively to peripheral H1 receptors without meaningful activity at H2, muscarinic, serotonergic, or adrenergic receptors. Critically, Bilastine undergoes minimal hepatic metabolism and does not significantly interact with cytochrome P450 enzymes, conferring a low potential for pharmacokinetic drug–drug interactions — a clinically meaningful advantage over older antihistamines. Its second-generation profile also means it does not readily cross the blood–brain barrier, which explains the confirmed non-sedating behaviour documented in multiple studies.

Allergic urticaria is driven by IgE-mediated mast cell and basophil activation, leading to the release of histamine and other mediators. Histamine binding to H1 receptors in skin produces the defining features: erythematous wheals, pruritus, and — in more severe cases — angioedema. Second-generation H1-antihistamines directly antagonise this mechanism at the target receptor, representing the pharmacological backbone of urticaria management. Bilastine's selectivity, rapid onset (approximately one hour), and prolonged duration (plasma half-life ~14.5 hours; clinical effect up to 26 hours) make it particularly well-suited to once-daily urticaria dosing. This therapeutic rationale aligns directly with EAACI/GA²LEN/EDF/WAO guidelines, which recommend second-generation antihistamines as standard first-line treatment.

The mechanistic case is strongly corroborated by a body of clinical trial and systematic review evidence. A pivotal Phase 3 RCT (NCT00421109, n=522) demonstrated superiority of Bilastine 20 mg over placebo and non-inferiority to levocetirizine 5 mg in Chronic Idiopathic Urticaria — this trial was central to the EMA marketing authorisation. Multiple subsequent systematic reviews and meta-analyses have confirmed consistent and reproducible efficacy signals across chronic urticaria populations, including paediatric cohorts (down to age 2 years). The prediction, whilst framed as a novel repurposing candidate by the TxGNN model, reflects a well-established clinical use case supported by the highest tier of regulatory evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00421109](https://clinicaltrials.gov/study/NCT00421109) | Phase 3 | Completed | 522 | **Pivotal RCT**: double-blind, randomised, placebo-controlled comparison of Bilastine 20 mg QD vs levocetirizine 5 mg QD vs placebo for Chronic Idiopathic Urticaria over 28 days. Established primary efficacy evidence for EMA/MHRA authorisation. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Head-to-head pharmacokinetic and pharmacodynamic comparison of 5 antihistamines (including Bilastine) in urticaria patients. Evaluates suppression of wheal-and-flare response; supports comparative effectiveness data. |
| [NCT01081574](https://clinicaltrials.gov/study/NCT01081574) | Phase 1/2 | Completed | 36 | Multicentre international paediatric PK/PD study (ages 2–<12 years) in allergic rhinoconjunctivitis or chronic urticaria; established optimal paediatric dose regimen per EMA-authorised protocol. |
| [NCT02576041](https://clinicaltrials.gov/study/NCT02576041) | Phase 4 | Completed | 19 | Post-marketing evaluation of effects on attention and driving performance (F1 simulator) in rhinitis/urticaria patients. Confirmed non-sedating profile at licensed dose. |
| [NCT04967092](https://clinicaltrials.gov/study/NCT04967092) | Phase 2 | Unknown | 58 | Double-blind RCT of Modified Xiao-Feng Powder vs Bilastine as active comparator in chronic urticaria; provides indirect comparative effectiveness data, though primary focus is on the herbal intervention. |
| [NCT00419783](https://clinicaltrials.gov/study/NCT00419783) | Phase 1 | Completed | 30 | Randomised, multiple-dose, 5-way crossover QTc/cardiac safety study at therapeutic (20 mg) and supratherapeutic (100 mg) doses. Confirmed no clinically meaningful QT interval prolongation, distinguishing Bilastine from first-generation agents (e.g., terfenadine). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35593100](https://pubmed.ncbi.nlm.nih.gov/35593100/) | 2022 | Systematic Review & Meta-Analysis | *Am J Rhinology & Allergy* | Bilastine significantly reduces symptoms of allergic rhinitis and chronic urticaria versus placebo across multiple RCTs; efficacy consistent with other second-generation antihistamines. |
| [36380619](https://pubmed.ncbi.nlm.nih.gov/36380619/) | 2023 | Systematic Review & Meta-Analysis | *Int Archives of Allergy and Immunology* | Systematic evaluation confirming Bilastine efficacy and safety for chronic urticaria (CU) wheals and erythema; provides evidence-based framework for clinical prescribing. |
| [26844221](https://pubmed.ncbi.nlm.nih.gov/26844221/) | 2016 | Expert Consensus / Clinical Guideline | *Asia Pacific Allergy* | Asia-Pacific Advisory Group consensus: endorses Bilastine as first-line therapy for allergic rhinitis and chronic urticaria, particularly in middle- and low-income countries with increasing allergic disease prevalence. |
| [38742145](https://pubmed.ncbi.nlm.nih.gov/38742145/) | 2024 | International Delphi Study | *Drugs in Context* | Expert consensus across multiple countries supports Bilastine as a preferred second-generation antihistamine for allergic rhinitis and urticaria in adults and children; positions it among leading options for first-line use. |
| [37191185](https://pubmed.ncbi.nlm.nih.gov/37191185/) | 2023 | Delphi Consensus | *Expert Review of Clinical Immunology* | Defines role of Bilastine among second-generation H1-antihistamines in allergic rhinoconjunctivitis and urticaria patients of different ages; highlights non-sedating and QT-safe profile as differentiating features. |
| [27110120](https://pubmed.ncbi.nlm.nih.gov/27110120/) | 2016 | Narrative Review | *Therapeutics and Clinical Risk Management* | Comprehensive overview of Bilastine pharmacology: rapid onset, prolonged action, low DDI potential (no CYP450 interaction), no dose adjustment required in renal/hepatic impairment (mild–moderate); supports use in allergic rhinitis and urticaria. |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Drug Review (Adis Drug Profile) | *Drugs* | Phase 3 trial results summarised: Bilastine 20 mg significantly reduced Total Symptom Score vs placebo in allergic rhinitis; comparable to cetirizine in urticaria symptom control. |
| [39376275](https://pubmed.ncbi.nlm.nih.gov/39376275/) | 2024 | RCT | *Indian J Otolaryngology & Head and Neck Surgery* | Bilastine 20 mg vs fexofenadine 180 mg in perennial allergic rhinitis/chronic urticaria: comparable efficacy and safety, with Autologous Skin Serum Test (ASST) analysis included. |
| [34850647](https://pubmed.ncbi.nlm.nih.gov/34850647/) | 2022 | Paediatric-Focused Review | *Immunotherapy* | Bilastine 10 mg established in children aged 2–<12 via EMA-authorised PK/PD modelling programme; safety and efficacy comparable to adult data, supports paediatric prescribing in urticaria. |
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | *J Investigational Allergology & Clinical Immunology* | Critical review of antihistamine up-dosing (up to 4× licensed dose) in chronic spontaneous urticaria; Bilastine included as one of the agents with supporting evidence for this approach in refractory cases. |

---

## UK Market Information

No UK marketing authorisation records were retrieved in this dataset. However, multiple peer-reviewed publications in the retrieved evidence pack explicitly reference UK MHRA approval of Bilastine as **Ilaxten** (FAES Farma) for symptomatic treatment of allergic rhinoconjunctivitis and urticaria in adults and adolescents, with subsequent paediatric extension (ages 2–<12 years, 10 mg formulation). Healthcare professionals should consult the current **BNF** (Section: Antihistamines) and the Ilaxten **SmPC** on the MHRA product information portal for authorised indications, dosage, and prescribing information.

---

## Additional Prediction of Interest: Cold Urticaria

The TxGNN model also predicted **Cold Urticaria** with evidence level **L2** and a **Proceed with Guardrails** recommendation, supported by 2 clinical trials:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01271075](https://clinicaltrials.gov/study/NCT01271075) | Phase 2/3 | Completed | 20 | **Most direct evidence**: double-blind, triple cross-over, placebo-controlled RCT evaluating Bilastine 20 mg, 40 mg, and 80 mg in Cold Contact Urticaria (CCU). Primary endpoints: Critical Stimulation Time Threshold (CSTT) and Critical Temperature Threshold (CTT). Small-sample cross-over design is standard methodology for this rare physical urticaria subtype. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Comparative antihistamine study in urticaria patients (may include cold urticaria subgroup); high mechanistic relevance. |

Cold urticaria is a physical urticaria subtype in which cold exposure triggers mast cell degranulation and histamine release, directly engaging the H1-mediated pathway targeted by Bilastine. EAACI guidelines recommend second-generation antihistamines — including at up-dosed regimens — as first-line management. This indication represents a plausible and clinically meaningful extension of Bilastine's established profile.

---

## Safety Considerations

No formal safety data (SmPC warnings, contraindications, or drug–drug interactions) were retrieved in this evidence pack. Please refer to the **Ilaxten SmPC** and **BNF** for complete prescribing information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

The following safety information is drawn from published evidence retrieved in this pack:

- **Sedation**: Confirmed non-sedating at standard doses; does not significantly impair driving ability or psychomotor function (Phase 4 study NCT02576041; multiple Phase 3 trials)
- **Cardiac safety**: No QT interval prolongation at therapeutic (20 mg) or supratherapeutic (100 mg) doses; no clinical concern for arrhythmia (Phase 1 study NCT00419783)
- **Drug interactions**: Minimal CYP450 metabolism; low potential for pharmacokinetic drug–drug interactions; no interactions identified in this dataset's DDI query

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bilastine has Level 1 evidence supporting its efficacy in allergic urticaria, including a pivotal Phase 3 RCT (n=522), multiple subsequent systematic reviews and meta-analyses, and regulatory approval by both the EMA and UK MHRA. The H1-receptor mechanism is directly aligned with the pathophysiology of urticaria, and the non-sedating, cardiosafe profile is well characterised. The primary constraint is incomplete regulatory data capture in this dataset, not a deficiency in the underlying evidence base.

**To proceed, the following is needed:**

- **Regulatory data retrieval**: Formally retrieve Ilaxten MHRA authorisation details (PL number, authorised indications, holder) from the MHRA product database to complete the UK Market Information section
- **SmPC review**: Extract approved warnings, contraindications, and special population guidance (pregnancy, lactation, severe renal/hepatic impairment) for the Safety Considerations section
- **MOA confirmation**: Query DrugBank API (DB11591) to formally document mechanism of action, receptor binding profile, and pharmacokinetic parameters
- **NICE guidance check**: Confirm whether NICE has issued technology appraisal or clinical guideline recommendations specifically for Bilastine (or second-generation antihistamines as a class) in urticaria within NHS England
- **Commissioning pathway**: Clarify NHS prescribing status (prescription-only vs. OTC availability) and any formulary restrictions relevant to UK clinical practice

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Data cut-off: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

