---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Anastrozole
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

# Anastrozole: From Aromatase Inhibitor to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a third-generation non-steroidal aromatase inhibitor that suppresses oestrogen synthesis by selectively inhibiting CYP19A1, and is established globally as adjuvant endocrine therapy for hormone receptor-positive breast cancer in postmenopausal women.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **50 registered clinical trials** and **20 publications** currently identified to support this direction.
This prediction constitutes a high-confidence model validation, as anastrozole's therapeutic role in ER+ breast cancer represents one of the most comprehensively evidenced drug–disease relationships in contemporary oncology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not listed in this evidence pack (established globally for adjuvant treatment of hormone receptor-positive breast cancer) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| UK Market Status | Not listed in this data pack |
| Number of Marketing Authorisations | 0 (in this data pack) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Anastrozole is a potent and selective inhibitor of CYP19A1 (aromatase), the enzyme responsible for the final step of oestrogen biosynthesis — the conversion of androgens (androstenedione, testosterone) to oestradiol in peripheral tissues, including adipose tissue, muscle, and the tumour microenvironment. In postmenopausal women, this peripheral aromatisation pathway is the dominant source of circulating oestrogen; by blocking it, anastrozole reduces plasma oestradiol concentrations by more than 80%, effectively depriving hormone receptor-positive tumour cells of their primary growth stimulus.

At the cellular level, oestrogen signalling through ERα promotes G1 cell cycle progression via upregulation of cyclin D1 and suppression of p21 and p27. Eliminating this oestrogenic drive inhibits cell cycle entry and promotes apoptosis in ER+ breast cancer cells. The mechanism is direct, the biological rationale is well-established, and the causal chain from enzyme target to clinical outcome is among the most thoroughly validated in oncology — confirmed by decades of preclinical and clinical research.

The TxGNN prediction for female breast carcinoma is therefore best understood as a model validation result of the highest quality. The knowledge graph has correctly identified one of the most well-characterised drug–disease relationships in modern medicine. The landmark ATAC trial (9,358 patients) demonstrated that anastrozole significantly outperformed tamoxifen as 5-year adjuvant therapy in ER+ postmenopausal breast cancer, and IBIS-II further confirmed its role in chemoprevention in high-risk women. The model's 99.68% prediction score reflects the completeness and biological coherence of this relationship within the TxGNN knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Completed | 9,358 | ATAC trial: anastrozole vs tamoxifen vs combination as 5-year adjuvant therapy in postmenopausal breast cancer; anastrozole demonstrated superior disease-free survival and fewer serious side effects than tamoxifen |
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | Completed | 7,576 | Largest head-to-head AI trial (exemestane vs anastrozole) in ER+ primary breast cancer; serves as the benchmark reference for anastrozole efficacy in ER+ disease and is widely cited in clinical guidelines |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | Completed | 4,172 | Letrozole vs anastrozole as 5-year adjuvant therapy in HR+/node-positive postmenopausal breast cancer; direct comparison of the two most widely used non-steroidal AIs |
| [NCT00556374](https://clinicaltrials.gov/study/NCT00556374) | Phase 3 | Completed | 3,420 | Denosumab vs placebo in non-metastatic breast cancer patients receiving aromatase inhibitor therapy; addresses the key safety concern of AI-associated bone mineral density loss |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | Completed | 2,980 | IBIS-II DCIS: adjuvant anastrozole vs tamoxifen in postmenopausal women following surgery for hormone receptor-positive ductal carcinoma in situ |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Completed | 1,914 | Treatment duration optimisation: 3 vs 6 years of anastrozole following 2–3 years of tamoxifen in postmenopausal ER+ breast cancer; directly informs adjuvant sequencing decisions |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Completed | 298 | Exemestane vs anastrozole as initial hormonal therapy in postmenopausal advanced/recurrent breast cancer; time to tumour progression as primary endpoint — non-inferiority design |
| [NCT00256698](https://clinicaltrials.gov/study/NCT00256698) | Phase 3 | Completed | 514 | FACT trial: anastrozole monotherapy vs anastrozole + fulvestrant (maximal oestrogen blockade) in HR+ first-relapse breast cancer; evaluates combination endocrine strategy |
| [NCT06311383](https://clinicaltrials.gov/study/NCT06311383) | Observational | Completed | 2,610 | Real-world effectiveness of ribociclib + aromatase inhibitor (including anastrozole) vs endocrine monotherapy vs chemotherapy as first-line treatment in HR+/HER2− metastatic breast cancer (Germany); strengthens external validity of RCT data |
| [NCT01151215](https://clinicaltrials.gov/study/NCT01151215) | Phase 2 | Terminated | 482 | AZD8931 + anastrozole vs anastrozole alone in HR+ endocrine-naïve locally advanced or metastatic breast cancer (MINT study); despite early termination, the 482 patients enrolled provide safety reference data for anastrozole in this setting |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT (ATAC landmark trial) | *Lancet* | After 5-year adjuvant therapy, anastrozole significantly prolonged disease-free survival vs tamoxifen (HR 0.87; p=0.01) with fewer distant recurrences and thromboembolic events in ER+ postmenopausal breast cancer — the defining trial establishing anastrozole as standard of care |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | Phase 3 RCT (chemoprevention) | *Lancet* | IBIS-II long-term follow-up: anastrozole reduced breast cancer incidence by 49% vs placebo over 10 years in high-risk postmenopausal women; the prevention effect persisted well beyond the 5-year treatment period |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | Phase 3 RCT | *Lancet* | IBIS-II DCIS: anastrozole superior to tamoxifen for preventing locoregional and contralateral breast cancer in postmenopausal women with HR+ DCIS (HR 0.49; 95% CI 0.35–0.69) |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-analysis of RCTs | *Oncotarget* | Systematic meta-analysis confirming anastrozole is superior to tamoxifen in disease-free and distant metastasis-free survival, with lower rates of thromboembolic events and endometrial cancer across multiple trials |
| [30499075](https://pubmed.ncbi.nlm.nih.gov/30499075/) | 2020 | Meta-analysis | *Pathology Oncology Research* | Meta-analysis of 7 RCTs: endocrine therapy including anastrozole significantly reduces ipsilateral and contralateral breast cancer recurrence after breast-conserving surgery and radiotherapy for DCIS |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | Pharmacogenomics (Phase 3 sub-study) | *Clinical Pharmacology and Therapeutics* | SNP–treatment interaction analysis from MA.27 trial (n=4,465): identifies CSMD1 locus as a genetic factor differentiating anastrozole from exemestane efficacy; supports personalised AI selection |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | Pharmacogenomics / GWAS | *JCI Insight* | Genome-wide association study in MA.27 trial identifies CSMD1 SNP associated with breast cancer-free interval; reveals an additional mechanism of anastrozole action beyond aromatase inhibition, relevant to resistance research |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Review | *Expert Opinion on Drug Safety* | Comprehensive safety and efficacy review of anastrozole; summarises multiple adjuvant RCTs demonstrating superiority over tamoxifen with favourable tolerability profile |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | *Expert Opinion on Pharmacotherapy* | Comparative review of all three third-generation AIs (anastrozole, letrozole, exemestane) in early breast cancer; consistent superiority over tamoxifen demonstrated across all four major adjuvant trial design strategies |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | *Oncology* | Review of anastrozole across the full breast cancer continuum (advanced, early, prevention); documents survival benefit and tolerability advantages from multiple large randomised studies |

---

## UK Market Information

No marketing authorisation data for Anastrozole was available in this evidence pack (0 licences recorded; market status listed as "not marketed" in the regulatory data field).

Anastrozole (brand name Arimidex, AstraZeneca) is in practice an established medicine in the United Kingdom, holding MHRA marketing authorisations for the adjuvant treatment of hormone receptor-positive early invasive breast cancer and first-line treatment of advanced breast cancer in postmenopausal women. It is listed in the British National Formulary (BNF) as an aromatase inhibitor and has been evaluated by NICE (Technology Appraisal TA112). The absence of licensing records in this evidence pack represents a data population gap and should not be read as indicating a lack of UK regulatory approval. Reviewers should consult the current MHRA-approved SmPC and BNF directly to confirm licensed indications and prescribing conditions before any clinical decision is made.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted endocrine therapy — non-steroidal aromatase inhibitor; **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low (aromatase inhibitors do not cause bone marrow suppression; routine haematological monitoring is not required for this reason) |
| Emetogenicity Classification | Minimal (oral tablet formulation; very low emetogenic risk) |
| Monitoring Items | Bone mineral density (DEXA scan at baseline and at regular intervals during treatment); liver function tests; serum lipids; musculoskeletal symptoms (arthralgia, myalgia — common class effect requiring clinical review) |
| Handling Protection | Standard pharmaceutical precautions apply; specialist cytotoxic handling and preparation protocols are not required for this drug class |

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Known class effects of aromatase inhibitors — including musculoskeletal symptoms (arthralgia, myalgia), accelerated bone mineral density loss (increased long-term fracture risk), and lipid profile changes — should be reviewed in the current MHRA-approved SmPC before any prescribing decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for female breast carcinoma is supported by Level 1 evidence of exceptional strength: multiple completed Phase 3 RCTs including the landmark ATAC trial (9,358 patients), long-term chemoprevention data from IBIS-II (10-year follow-up), and a body of meta-analyses — collectively establishing anastrozole as a standard-of-care aromatase inhibitor in hormone receptor-positive breast cancer. The drug's mechanism of CYP19A1 inhibition directly addresses the oestrogen-driven growth of ER+ tumour cells, and the evidence chain from molecular target to clinical outcome is one of the most complete in oncology.

**To proceed, the following is needed:**

- Population of UK MHRA marketing authorisation records within this evidence pack (anastrozole is expected to hold current MHRA licences for breast cancer indications; their absence here reflects a data gap rather than a true regulatory void)
- Full SmPC safety data including current warnings, contraindications, and drug–drug interactions (particularly interactions with CYP enzyme inducers/inhibitors and oestrogen-containing products)
- Completion of mechanism of action (MOA) data integration from DrugBank
- Bone health monitoring protocol established at prescribing initiation: DEXA scan at baseline and annually during treatment given well-documented AI-associated bone mineral density loss
- Review of current NICE guidance (TA112 and any subsequent appraisals) and applicable MHRA communications to confirm up-to-date licensed indications and any relevant safety communications before clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

