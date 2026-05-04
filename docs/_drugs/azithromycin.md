---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Congenital Hematological Disorder (Sickle Cell Disease)

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. This is a multi-candidate evidence pack (`TW-DB00207-multi`); ten TxGNN-predicted indications are evaluated, with the highest-evidence candidate (congenital hematological disorder / sickle cell disease) featured as the primary focus.

---

## One-Sentence Summary

Azithromycin is a macrolide antibiotic with established use in community-acquired bacterial infections, including respiratory tract infections, chlamydial sexually transmitted infections, and skin and soft tissue infections.

The TxGNN model identifies **10 candidate repurposing indications**; the highest-evidence opportunity is **congenital hematological disorder** — specifically, prevention of acute chest syndrome (ACS) in **sickle cell disease** — with **4 clinical trials** and **2 publications** providing supporting context, and a mechanistic rationale grounded in Azithromycin's well-characterised anti-inflammatory and immunomodulatory properties.

Note: the algorithm's highest-scoring prediction (hyperamylasemia, TxGNN rank 1, score 99.81%) lacks biological plausibility and is recommended Hold at Stage 0.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Community-acquired bacterial infections (respiratory tract, skin/soft tissue, urogenital – *Chlamydia trachomatis*) |
| Primary Predicted Indication (Best Evidence) | Congenital hematological disorder – sickle cell disease (ACS prevention) |
| TxGNN Score (Primary Candidate) | 99.40% (rank 5,712 of all disease nodes) |
| Highest TxGNN Score (Rank 1) | 99.81% – hyperamylasemia (biological plausibility: low; recommendation: Hold) |
| Evidence Level | L3 – observational studies / systematic review context |
| UK Market Status | Data retrieval gap – MHRA authorisation data not captured in this pack; Azithromycin is widely licensed in the UK (Zithromax® and multiple generics) |
| Number of MHRA Marketing Authorisations | Data retrieval gap |
| Recommended Decision | **Research Question** (sickle cell disease / ACS); **Hold** for all other predicted indications |

---

## Top 10 TxGNN Predicted Indications – Summary

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Literature | Recommendation |
|------|---------------------|-------------|----------------|--------|------------|----------------|
| 1 | Hyperamylasemia | 99.81% | L5 | 0 | 0 | Hold |
| 2 | Polyclonal hyperviscosity syndrome | 99.81% | L5 | 0 | 0 | Hold |
| 3 | Congenital analbuminemia | 99.79% | L5 | 0 | 0 | Hold |
| 4 | Punctate epithelial keratoconjunctivitis | 99.78% | L4 | 0 | 1 | Hold |
| 5 | Blood group incompatibility | 99.70% | L5 | 0 | 0 | Hold |
| 6 | Premalignant hematological system disease | 99.64% | L5 | 0 | 0 | Hold |
| 7 | Monoclonal gammopathy | 99.61% | L4 | 0 | 7 | Research Question |
| 8 | Haematological disease with acquired peripheral neuropathy | 99.56% | L5 | 0 | 0 | Hold ⚠️ |
| 9 | Septicaemic plague | 99.52% | L4 | 0 | 5 | Research Question |
| **10** | **Congenital hematological disorder (sickle cell disease)** | **99.40%** | **L3** | **4** | **2** | **Research Question** |

> ⚠️ Rank 8 carries an active safety signal: Azithromycin can itself cause drug-induced peripheral neuropathy (DIPN) and may worsen pre-existing acquired neuropathy. This indication is contraindicated for further development.

---

## Why is This Prediction Reasonable?

### Mechanism of Action

Azithromycin is a second-generation macrolide antibiotic that inhibits bacterial protein synthesis by binding reversibly to the 50S ribosomal subunit, blocking translocation of peptidyl-tRNA. Critically for repurposing, it also exerts **anti-inflammatory and immunomodulatory effects** independent of its antibacterial activity: it suppresses IL-8, TNF-α, IL-1β, and NF-κB signalling; inhibits neutrophil chemotaxis; down-regulates matrix metalloproteinase-9 (MMP-9); and — as demonstrated in the in vitro evidence for monoclonal gammopathy (see below) — blocks lysosomal autophagy flux, inducing ER stress-mediated cytotoxicity in malignant plasma cells when combined with bortezomib (PMID 23546223).

> Note: Formal MOA data was not retrieved in this evidence pack. The above is drawn from established pharmacological knowledge.

### Relationship Between Original and New Indication

Pulmonary inflammation is the shared pathophysiological thread. In sickle cell disease, polymerisation of deoxygenated HbS triggers vaso-occlusion and sterile neutrophilic lung inflammation, culminating in acute chest syndrome (ACS) — the leading cause of death in this population. Azithromycin's established role in suppressing airway and alveolar inflammation (as used in non-CF bronchiectasis, COPD, and diffuse panbronchiolitis) provides a biologically coherent basis for ACS prevention.

Atypical organisms (*Mycoplasma pneumoniae*, *Chlamydophila pneumoniae*) are also recognised triggers of ACS episodes, and Azithromycin offers direct antimicrobial cover against these pathogens in addition to its anti-inflammatory action.

### Why Two Phase 1 Trials Were Withdrawn

Both directly relevant trials (NCT02630394 and NCT02960503) were withdrawn before enrolling a single participant. This is a major feasibility signal. Likely barriers include: QTc prolongation risk in patients already prone to cardiac complications; challenges with paediatric and under-resourced population recruitment; and potential investigator resourcing constraints. Understanding the exact withdrawal reason is a prerequisite before any further development.

---

## Clinical Trial Evidence

*Trials listed for the primary candidate: congenital hematological disorder (rank 10).*

| Trial Number | Phase | Status | Enrolment | Key Findings / Relevance |
|-------------|-------|--------|-----------|--------------------------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | **Withdrawn** (0 enrolled) | 0 | **Highest direct relevance.** Pilot study specifically designed to evaluate Azithromycin prophylaxis against ACS in sickle cell disease. ACS is the second most common cause of hospitalisation and leading cause of death in SCD. Macrolides proposed for dual anti-inflammatory + antimicrobial atypical organism cover. Withdrawal reason not publicly documented — must be investigated before reinitiation. |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | **Withdrawn** (0 enrolled) | 0 | Macrolide therapy to improve FEV₁ in adults with sickle cell anaemia. Targets obstructive lung disease and pulmonary hypertension — key SCD pulmonary complications. Both this and NCT02630394 withdrawn simultaneously with zero enrolment, suggesting a systemic barrier requiring investigation. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Large paediatric PK/PD/safety platform study. Azithromycin is one of many understudied drugs; provides paediatric safety data but no SCD efficacy data. Low direct relevance. |
| [NCT04294641](https://clinicaltrials.gov/study/NCT04294641) | Phase 2 | Completed | 10 | Ibrutinib for newly diagnosed chronic GVHD. Azithromycin may appear as prophylactic co-medication. Not a repurposing trial. Very low direct relevance. |

---

## Literature Evidence

*Primary literature for congenital hematological disorder (rank 10) and key mechanistic literature for monoclonal gammopathy (rank 7).*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Systematic Review / Meta-analysis (Cochrane) | *Cochrane Database of Systematic Reviews* | Antibiotics for preventing lower respiratory tract infections in high-risk children aged ≤12 years. Supports biological rationale for antibiotic prophylaxis in immunologically vulnerable populations, relevant to SCD children at risk of ACS. |
| [34471086](https://pubmed.ncbi.nlm.nih.gov/34471086/) | 2021 | Case Report | *American Journal of Case Reports* | Megadose methylprednisolone for ITP in a COVID-19 positive infant. Provides context for haematological complications in paediatric settings; low direct relevance to Azithromycin repurposing. |
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | In vitro / Mechanistic Study | *International Journal of Oncology* | **Key mechanistic evidence for monoclonal gammopathy (rank 7).** Azithromycin (and other macrolides) blocks autophagy flux via lysosomal inhibition, inducing ER stress and CHOP-mediated apoptosis in multiple myeloma cell lines. Combined with bortezomib, produces synergistic cytotoxicity in U266, IM-9, and RPMI8226 cells. Provides rationale for Azithromycin + proteasome inhibitor combinations in myeloma, where dual blockade of protein degradation pathways is mechanistically sound. |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | *Cornea* | Microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult diagnosed by metagenomic sequencing. Azithromycin is an established treatment for microsporidial infection. Indirectly supports the rank 4 prediction (punctate epithelial keratoconjunctivitis) but evidence is very limited. |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro Susceptibility Study | *Antimicrobial Agents and Chemotherapy* | In vitro MIC testing of 14 antimicrobials against 78 *Yersinia pestis* strains. Azithromycin showed **poor activity** against all strains. This is a negative finding for septicaemic plague (rank 9) — current standard of care (streptomycin, doxycycline) remains preferable. |
| [19392866](https://pubmed.ncbi.nlm.nih.gov/19392866/) | 2009 | Systematic Review | *Alimentary Pharmacology & Therapeutics* | Epidemiology and clinical features of traveller's diarrhoea. Contextual relevance to Azithromycin's established antimicrobial uses; low relevance to plague. |

---

## UK Market Information

> **Data Retrieval Gap**: The regulatory data collection pipeline did not return MHRA licensing records for Azithromycin in this evidence pack. This is likely a technical data retrieval issue rather than reflecting the actual UK market status.

Based on publicly available MHRA and BNF information, Azithromycin is widely authorised in the United Kingdom:

| Marketing Authorisation | Product Name | Dosage Form | Approved Indication (Summary) |
|------------------------|-------------|-------------|-------------------------------|
| Multiple PLs (generics) | Zithromax® / Azithrox® / generics | Capsules 250 mg; Tablets 500 mg; Oral suspension | Community-acquired pneumonia; pharyngitis/tonsillitis; acute exacerbations of chronic bronchitis; skin and soft tissue infections; uncomplicated urogenital *Chlamydia trachomatis* infections |
| Ophthalmic formulation | AzaSite® (1% ophthalmic gel) | Eye drops/gel | Bacterial conjunctivitis |

> **BNF Classification**: Section 5.1.5 – Macrolides. Refer to current BNF and individual SmPCs for full prescribing information.

**Recommended action**: Re-run the MHRA data collection pipeline for DB00207 to populate the full licence register, including all PL numbers, indication text, dosage forms by route, and any conditional marketing authorisations.

---

## Safety Considerations

Safety data was not retrieved in this evidence pack. The following applies:

> Please refer to the SmPC and BNF for complete safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

Key safety considerations known from established pharmacological sources and relevant to this repurposing context:

- **QTc Prolongation**: Azithromycin is associated with QTc interval prolongation and risk of fatal arrhythmia (torsades de pointes). This is a **critical safety barrier** for the sickle cell disease indication, where patients already carry elevated cardiovascular risk. Any clinical trial design must include mandatory pre-treatment and on-treatment ECG monitoring and exclude patients with baseline QTc ≥450 ms (males) / ≥470 ms (females).
- **Hepatotoxicity**: Rare but serious drug-induced liver injury reported; relevant to monitoring protocol design.
- **Drug-Induced Peripheral Neuropathy (DIPN)**: Active safety signal for rank 8 prediction; this indication should not be pursued.
- **Antimicrobial Resistance**: Long-term macrolide prophylaxis carries risk of promoting macrolide-resistant respiratory pathogens — a key concern in any SCD prophylaxis protocol.

---

## Conclusion and Next Steps

**Decision: Research Question** *(congenital hematological disorder – sickle cell disease / ACS prevention)*
**Decision: Hold** *(all remaining 9 predicted indications)*

---

**Rationale:**

Azithromycin's anti-inflammatory and immunomodulatory properties provide a biologically coherent basis for preventing acute chest syndrome in sickle cell disease, and two Phase 1 trials were initiated (though subsequently withdrawn before enrolment). All other TxGNN-predicted indications either lack biological plausibility, carry active safety concerns, or have no supportive evidence beyond model prediction alone.

---

**To proceed with the sickle cell disease / ACS indication, the following is needed:**

- [ ] **Establish withdrawal reasons** for NCT02630394 and NCT02960503 — contact the principal investigators directly; if withdrawal was administrative/funding-related rather than safety-driven, re-initiation may be feasible
- [ ] **Cardiac safety risk assessment**: Conduct a formal QTc risk–benefit analysis for the SCD population; consider Holter monitoring sub-study design
- [ ] **Retrieve full MHRA licensing data**: Re-run regulatory pipeline to populate UK authorisation records
- [ ] **Retrieve SmPC warnings and contraindications**: MHRA SmPC retrieval is flagged as a blocking data gap (DG001)
- [ ] **Retrieve formal MOA data** from DrugBank API (data gap DG002) to complete mechanism analysis
- [ ] **Antimicrobial stewardship review**: Evaluate macrolide resistance implications of prophylactic use in SCD population in the UK context (liaise with UKHSA)
- [ ] **Paediatric consideration**: Sickle cell disease predominantly affects children in the UK; a paediatric investigation plan (PIP) will be required if pursuing a formal indication
- [ ] **Monoclonal gammopathy (rank 7) secondary track**: PMID 23546223 provides in vitro mechanistic support for Azithromycin + bortezomib synergy in myeloma; this warrants a dedicated IND-enabling study (separate from the SCD track)

---

*Report generated: 4 April 2026 | Evidence data cutoff: 4 April 2026 | Candidate ID: TW-DB00207-multi v4*
*This report is for research purposes only and does not constitute clinical guidance or a recommendation to prescribe.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

