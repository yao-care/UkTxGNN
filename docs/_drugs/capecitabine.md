---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Cardia Adenocarcinoma and Related Gastric Subtypes

## One-Sentence Summary

Capecitabine (Xeloda) is an orally administered fluoropyrimidine prodrug widely used in the treatment of colorectal and breast cancer, which is converted in tumour tissue to active 5-fluorouracil (5-FU) to inhibit thymidylate synthase (TYMS) and block DNA synthesis.
The TxGNN model has predicted **10 histologically distinct gastric cancer subtypes** as potential new indications; the highest-scoring prediction is **Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)**, but the most clinically actionable candidates are **Gastric Cardia Adenocarcinoma (Rank 5)** and **Gastric Body Carcinoma (Rank 8)**, together supported by over 20 clinical trials (including completed Phase 3 studies) and more than 25 publications.
Evidence strength ranges from L2 (*Proceed with Guardrails*) for gastric cardia and body carcinoma down to L5 (model prediction only, no supporting studies) for rare subtypes such as GAPPS and malignant gastric granular cell tumour.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer; breast cancer (established clinical use; original_indications field not populated in this Evidence Pack) |
| Top TxGNN-Predicted Indication | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) |
| Best-Evidenced Predicted Indication | Gastric Cardia Adenocarcinoma (Rank 5) / Gastric Body Carcinoma (Rank 8) |
| TxGNN Prediction Score (Rank 1 / Best Candidate) | 99.94% / 99.91% |
| Evidence Level (Best Candidate) | L2 |
| UK Market Status | Not marketed (data gap — see note below) |
| Number of UK Marketing Authorisations | 0 (data gap — see note below) |
| Recommended Decision | **Proceed with Guardrails** (Gastric Cardia Adenocarcinoma; Gastric Body Carcinoma) |

> **Important note on UK market status**: The Evidence Pack records zero UK marketing authorisations for Capecitabine. This is a known data gap (DG001, DG002) and does not reflect the actual regulatory position. Capecitabine (Xeloda®, Roche Products Ltd) is a well-established antineoplastic agent in UK clinical practice. Healthcare professionals should verify the current MHRA approval status via the electronic Medicines Compendium (eMC) and the British National Formulary (BNF).

---

## Prediction Summary: All 10 Predicted Gastric Cancer Subtypes

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Recommendation |
|------|------------------|-------------|----------------|----------------|
| 1 | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) | 99.94% | L5 | Hold |
| 2 | Gastric Tubular Adenocarcinoma | 99.94% | L4 | Hold |
| 3 | Microinvasive Gastric Cancer | 99.94% | L5 | Hold |
| 4 | Signet Ring Cell Gastric Adenocarcinoma | 99.94% | L3 | Research Question |
| 5 | Gastric Cardia Adenocarcinoma | 99.91% | L2 | **Proceed with Guardrails** |
| 6 | Gastric Pylorus Carcinoma | 99.91% | L4 | Hold |
| 7 | Carcinoma of Stomach, Salivary Gland Type | 99.91% | L4 | Hold |
| 8 | Gastric Body Carcinoma | 99.90% | L2 | **Proceed with Guardrails** |
| 9 | Epstein-Barr Virus-Associated Gastric Carcinoma | 99.90% | L4 | Research Question |
| 10 | Malignant Gastric Granular Cell Tumour | 99.89% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Capecitabine is a fluoropyrimidine carbamate prodrug that undergoes a three-step enzymatic conversion after oral administration. The critical final step is catalysed by thymidine phosphorylase (TP), an enzyme preferentially expressed in tumour tissue. This produces 5-fluorouracil (5-FU) at the tumour site, which then inhibits thymidylate synthase (TYMS) — a rate-limiting enzyme in de novo pyrimidine synthesis — thereby starving tumour cells of the thymidine triphosphate required for DNA replication and repair. This tumour-preferential activation mechanism confers a more favourable therapeutic index compared with intravenous 5-FU infusion.

Gastric adenocarcinomas of all major histological subtypes characteristically overexpress both TP and TYMS, making them mechanistically susceptible to fluoropyrimidine-based therapy. This is not a theoretical association: Capecitabine-containing regimens — CAPOX (Capecitabine + Oxaliplatin), ECX (Epirubicin + Cisplatin + Capecitabine), and XP (Capecitabine + Cisplatin) — are embedded in global first-line treatment guidelines (ESMO, NCCN) for advanced gastric and gastro-oesophageal junction (GEJ) cancer. The landmark GLOW Phase 3 trial (n=507) used CAPOX as its standard backbone, and KEYNOTE-811 (n=763) validated Capecitabine-containing regimens as an accepted standard of care in this disease.

The TxGNN model's uniformly high prediction scores (all > 99.89%) across all 10 gastric subtypes therefore reflect genuine biological and knowledge-graph connectivity — specifically the well-documented relationship between fluoropyrimidines and gastric adenocarcinoma — rather than speculative inference. The critical clinical question is not whether Capecitabine works in gastric cancer broadly, but whether subtype-specific evidence is sufficient to guide its use in histologically distinct entities. The evidence base varies markedly: robust Phase 3 data for broadly defined gastric cardia and body carcinoma; emerging Phase 2 data for signet ring cell carcinoma; and no clinical evidence at all for ultra-rare entities such as GAPPS or malignant gastric granular cell tumour. Notably, for GAPPS (rank 1), the extremely small global patient population (<50 reported families) renders clinical trial evidence structurally impossible to generate, and for microinvasive gastric cancer (rank 3), the standard of care is curative endoscopic resection rather than systemic chemotherapy.

---

## Clinical Trial Evidence

*The top-ranked prediction (GAPPS, rank 1) has no registered clinical trials. Evidence is therefore drawn from the best-evidenced actionable indications: Gastric Cardia Adenocarcinoma (rank 5), Gastric Body Carcinoma (rank 8), and Signet Ring Cell Gastric Adenocarcinoma (rank 4). Trials with direct Capecitabine relevance are prioritised.*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | Completed | 48 | **Most direct evidence**: CAPOX (Oxaliplatin + Capecitabine) as first-line treatment for metastatic adenocarcinoma of the oesophagus, GEJ, and **gastric cardia**. Corresponds to PMID 16303863 (ORR 45%). This is the single most directly relevant trial for gastric cardia adenocarcinoma. |
| [NCT00374036](https://clinicaltrials.gov/study/NCT00374036) | Phase 3 | Completed | 416 | Large multicentre Phase 3 trial comparing polychemotherapy sequences for locally advanced or metastatic gastric/cardia adenocarcinoma. Capecitabine-containing arms included; provides near-L1 evidence for this indication. |
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | Completed | 763 | KEYNOTE-811: Pembrolizumab ± standard chemotherapy (CAPOX or FP) vs placebo + chemotherapy as first-line treatment for advanced gastric/GEJ adenocarcinoma. Validates Capecitabine-containing regimens as Phase 3-level standard of care in gastric cancer. |
| [NCT03653507](https://clinicaltrials.gov/study/NCT03653507) | Phase 3 | Active, not recruiting | 507 | GLOW trial: Zolbetuximab + **CAPOX** vs placebo + CAPOX for CLDN18.2-positive, HER2-negative advanced gastric/GEJ adenocarcinoma. Capecitabine formally embedded as Phase 3-validated standard backbone. |
| [NCT06901531](https://clinicaltrials.gov/study/NCT06901531) | Phase 3 | Recruiting | 500 | Zolbetuximab + pembrolizumab + CAPOX (or mFOLFOX6) for CLDN18.2+/PD-L1+/HER2− gastric/GEJ adenocarcinoma. Ongoing Phase 3 further cementing CAPOX as standard first-line regimen. |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | Completed | 73 | Randomised Phase 2 of extended neoadjuvant therapy for locally advanced adenocarcinoma of the oesophagus, GEJ, and **gastric cardia**; Capecitabine-containing arm (docetaxel + oxaliplatin + capecitabine) assessed. |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | N/A | Completed | 27 | Dose-finding study of TEX (Taxotere + Eloxatin + **Xeloda/Capecitabine**) + Herceptin in HER2-positive advanced oesophageal, cardia, and gastric cancer. Establishes Capecitabine dosing in HER2+ subtype. |
| [NCT06238752](https://clinicaltrials.gov/study/NCT06238752) | Phase 2 | Completed | 33 | Apatinib + tislelizumab + **CAPOX** as first-line treatment for HER2-negative advanced gastric/GEJ cancer with **signet ring cell carcinoma** or peritoneal metastasis. Direct Capecitabine evidence in SRCC subtype. |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | Not yet recruiting | 66 | AK112 (PD-1/VEGF bispecific antibody) + chemotherapy as neoadjuvant treatment for locally advanced resectable gastric/GEJ adenocarcinoma containing **signet ring cells**. Planned 2025–2029; chemotherapy backbone may include Capecitabine. |
| [NCT04379596](https://clinicaltrials.gov/study/NCT04379596) | Phase 1b/2 | Recruiting | 450 | DESTINY-Gastric03: T-DXd (trastuzumab deruxtecan) monotherapy and in combination with chemotherapy (including Capecitabine-containing regimens) and/or immunotherapy in HER2-expressing advanced gastric/GEJ/oesophageal adenocarcinoma. |

---

## Literature Evidence

*Prioritising publications with direct Capecitabine evidence in gastric cancer subtypes (tiers 1–2). The rank 1 indication (GAPPS) has no supporting literature.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/) | 2006 | Phase 2 Trial | Ann Oncol | **Most direct evidence for gastric cardia**: CAPOX (Oxaliplatin + Capecitabine) first-line in metastatic adenocarcinoma of the oesophagus, GEJ, and gastric cardia (n=48); ORR 45%, median OS 8.5 months. Directly validates Capecitabine in gastric cardia subtype as a first-line agent. |
| [18997184](https://pubmed.ncbi.nlm.nih.gov/18997184/) | 2009 | Prospective Cohort / Phase 2 | Jpn J Clin Oncol | Oral fluoropyrimidines (Capecitabine or S-1) + Cisplatin in elderly patients with advanced gastric cancer; evaluates tolerability and efficacy of Capecitabine specifically in this population. |
| [24175788](https://pubmed.ncbi.nlm.nih.gov/24175788/) | 2013 | Retrospective Comparative Study | Asian Pac J Cancer Prev | Capecitabine vs bolus 5-FU concurrent with postoperative radiotherapy for gastric adenocarcinoma: comparable local control, distant control, and survival; establishes Capecitabine as an effective oral substitute for 5-FU in gastric chemoradiation. |
| [35085931](https://pubmed.ncbi.nlm.nih.gov/35085931/) | 2022 | Retrospective Cohort | Eur J Cancer | FLOT vs MAGIC-type perioperative regimens (ECF/ECX — ECX contains Capecitabine) in locally advanced oesophago-gastric adenocarcinoma: FLOT demonstrated improved pathological response. Provides comparative effectiveness context for the Capecitabine-containing ECX regimen. |
| [19690058](https://pubmed.ncbi.nlm.nih.gov/19690058/) | 2010 | Phase 1/2 | Ann Oncol | Postoperative chemoradiotherapy in gastric cancer using weekly cisplatin + daily oral Capecitabine; feasibility and toxicity established, providing an alternative to the SWOG 0116 INT regimen. |
| [17848909](https://pubmed.ncbi.nlm.nih.gov/17848909/) | 2007 | Phase 1/2 | Br J Cancer | Dose-finding study for postoperative radiotherapy with concurrent daily cisplatin + Capecitabine in gastric cancer; maximum tolerated dose established; Capecitabine safety profile characterised in the CRT setting. |
| [35922756](https://pubmed.ncbi.nlm.nih.gov/35922756/) | 2022 | Translational / Mechanistic Study | Mol Med | MALAT1-miRNA network regulates TYMS expression and affects 5-FU-based chemotherapy response; elucidates mechanisms of Capecitabine resistance and potential predictive biomarkers relevant to gastric cancer. |
| [26848413](https://pubmed.ncbi.nlm.nih.gov/26848413/) | 2015 | Case Report | Cureus | Unusual recurrence of **signet ring cell gastric adenocarcinoma** treated with ECX (Epirubicin + Cisplatin + Capecitabine) combined with multivisceral resection; illustrates Capecitabine use in this specific histological subtype. |
| [41555855](https://pubmed.ncbi.nlm.nih.gov/41555855/) | 2026 | Case Series | Surg Case Rep | Conversion surgery for advanced gastric cancer following **CAPOX + pembrolizumab**; demonstrates contemporary real-world use of Capecitabine-based immunochemotherapy and its potential to render previously unresectable disease operable. |
| [29372626](https://pubmed.ncbi.nlm.nih.gov/29372626/) | 2018 | Phase 3 Re-analysis | Asia-Pac J Clin Oncol | Re-analysis of ML17032 Phase 3 trial: Capecitabine/Cisplatin (XP) vs 5-FU/Cisplatin (FP) in Chinese patients with advanced gastric cancer; XP confirmed non-inferior to FP, supporting oral Capecitabine as a practical alternative to IV fluorouracil. |

---

## Cytotoxicity

Capecitabine qualifies for inclusion of this section: it is a conventional antineoplastic agent of the fluoropyrimidine class, with original indications including colorectal cancer and breast cancer, and is in clinical use for advanced gastric cancer.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — fluoropyrimidine class (oral prodrug of 5-fluorouracil) |
| Myelosuppression Risk | Low to moderate; neutropenia, anaemia, and thrombocytopenia are reported but typically less severe than intravenous 5-FU/leucovorin regimens. When combined with oxaliplatin (CAPOX) or cisplatin (XP), myelosuppression risk increases. |
| Emetogenicity Classification | Low (oral administration; nausea and vomiting reported but generally mild to moderate; co-administered platinum agents substantially increase emetogenicity) |
| Monitoring Items | FBC with differential before each treatment cycle; renal function (creatinine clearance — dose adjustment required if CrCl 30–50 mL/min; contraindicated if CrCl < 30 mL/min); liver function tests; INR if co-prescribed with warfarin or other coumarins; hand-foot syndrome grading at each clinic visit; DPD enzyme activity or DPYD genotyping before initiation (MHRA requirement since 2020) |
| Handling Protection | Standard cytotoxic medicinal product handling precautions apply; oral route reduces risk of environmental exposure during preparation compared with IV chemotherapy, but tablets must not be crushed or split; patients and carers should wash hands after handling; healthcare professionals should follow local cytotoxic drug handling policies |

---

## Safety Considerations

The Evidence Pack does not contain populated safety data for Capecitabine (all key warnings and contraindications are listed as data gaps; no drug–drug interactions retrieved). Please refer to the **Xeloda SmPC** (available via eMC: www.medicines.org.uk) and the **BNF** for full prescribing information. Report suspected adverse reactions via the **Yellow Card Scheme** (yellowcard.mhra.gov.uk).

**Key safety considerations for UK practice (from established clinical knowledge):**

- **DPD deficiency (DPYD)**: Patients with complete dihydropyrimidine dehydrogenase (DPD) deficiency must not receive Capecitabine; those with partial DPD deficiency require dose reduction. MHRA issued a Drug Safety Update in 2020 mandating DPD testing before initiation of all fluoropyrimidine chemotherapy in the UK. Pharmacogenomic testing for *DPYD* variants (*2A, *13, c.2846A>T, HapB3) is now standard NHS practice.
- **Coumarin anticoagulant interaction**: Capecitabine significantly potentiates the anticoagulant effect of warfarin and other coumarin derivatives; INR must be monitored closely and dose adjustments made. This interaction can be fatal if unmanaged.
- **Hand-foot syndrome (palmar-plantar erythrodysaesthesia)**: The most common dose-limiting toxicity; dose modification or interruption is required for Grade 2 or above.
- **Renal impairment**: Dose reduction to 75% of standard dose recommended for CrCl 30–50 mL/min; Capecitabine is contraindicated in severe renal impairment (CrCl < 30 mL/min).
- **Phenytoin interaction**: Capecitabine can increase phenytoin plasma levels; dose monitoring is required.

---

## Conclusion and Next Steps

### Decision Summary by Predicted Indication

| Predicted Indication | Evidence Level | Recommended Decision |
|---------------------|----------------|---------------------|
| Gastric Cardia Adenocarcinoma (Rank 5) | L2 | **Proceed with Guardrails** |
| Gastric Body Carcinoma (Rank 8) | L2 | **Proceed with Guardrails** |
| Signet Ring Cell Gastric Adenocarcinoma (Rank 4) | L3 | Research Question |
| Epstein-Barr Virus-Associated Gastric Carcinoma (Rank 9) | L4 | Research Question |
| Gastric Tubular Adenocarcinoma (Rank 2) | L4 | Hold |
| Gastric Pylorus Carcinoma (Rank 6) | L4 | Hold |
| Carcinoma of Stomach, Salivary Gland Type (Rank 7) | L4 | Hold |
| GAPPS (Rank 1) | L5 | Hold |
| Microinvasive Gastric Cancer (Rank 3) | L5 | Hold |
| Malignant Gastric Granular Cell Tumour (Rank 10) | L5 | Hold |

---

**Decision: Proceed with Guardrails** (Gastric Cardia Adenocarcinoma; Gastric Body Carcinoma)

**Rationale:**
Multiple completed Phase 2 and Phase 3 trials — including a dedicated Phase 2 study directly evaluating CAPOX in gastric cardia adenocarcinoma (NCT00040859, ORR 45%), and the Phase 3 GLOW (n=507) and KEYNOTE-811 (n=763) trials using CAPOX as the standard chemotherapy backbone — provide robust evidence that Capecitabine-containing regimens are effective and safe in advanced gastric and GEJ adenocarcinoma. The mechanistic rationale (TYMS overexpression, TP-mediated tumour-preferential activation) is well established for adenocarcinoma histology.

**Hold** is recommended for rare and biologically distinct subtypes where either: (a) the cancer biology does not support fluoropyrimidine activity (malignant gastric granular cell tumour — Schwann cell origin, not adenocarcinoma); (b) the clinical stage makes systemic chemotherapy inappropriate (microinvasive gastric cancer — standard of care is curative endoscopic resection); or (c) the patient population is too small globally to generate evidence and extrapolation is unjustified (GAPPS — < 50 families reported worldwide).

**To proceed, the following is needed:**

- **DPD / DPYD testing**: MHRA mandates DPD deficiency screening before Capecitabine initiation in all patients; this is a prerequisite for safe prescribing in the UK
- **UK regulatory and formulary confirmation**: Verify current MHRA-approved indications via eMC; if specific gastric subtypes fall outside the current licensed indication, local off-label prescribing governance must be followed
- **Histological subtype documentation**: Confirm adenocarcinoma histology (not salivary gland-type carcinoma, GCT, or other non-adenocarcinoma subtypes) before applying fluoropyrimidine-based therapy
- **Upper GI MDT review**: All patients with gastric cancer should be discussed at a specialist upper GI multidisciplinary team meeting before initiating systemic therapy, in line with NICE guidance
- **Biomarker assessment**: HER2, PD-L1 (CPS), CLDN18.2, and MSI/dMMR status should be assessed at diagnosis as they influence the choice of additional agents to combine with Capecitabine
- **Renal function assessment**: CrCl must be documented before dosing; dose adjust for CrCl 30–50 mL/min
- **Evidence generation for SRCC and EBV subtypes**: Prospective data from ongoing trials (including NCT07091227) should be awaited before adopting Capecitabine specifically for signet ring cell or EBV-associated gastric carcinoma outside of established clinical practice
- **Full SmPC review**: Consult the current Xeloda SmPC via eMC for complete prescribing information, including contraindications, dose modifications, and monitoring requirements

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All treatment decisions should be made by qualified healthcare professionals in line with current NICE guidance, local formulary policies, and individual patient circumstances. Suspected adverse reactions should be reported via the MHRA Yellow Card Scheme (yellowcard.mhra.gov.uk).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

