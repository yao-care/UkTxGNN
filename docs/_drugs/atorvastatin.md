---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atorvastatin: From Hypercholesterolaemia to Familial Hypercholesterolaemia

---

## One-Sentence Summary

Atorvastatin is a widely used HMG-CoA reductase inhibitor (statin), primarily indicated for the management of hypercholesterolaemia and prevention of cardiovascular events.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolaemia (FH)**, with **35 clinical trials** and **19 publications** currently supporting this direction.
This prediction carries a high-confidence score of **99.42%** and aligns with established clinical practice globally, effectively validating the model's predictive performance for this drug–disease pairing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolaemia and cardiovascular risk reduction *(UK MHRA licensing data not retrieved in this evidence pack — see note in UK Market Information section)* |
| Predicted New Indication | Familial Hypercholesterolaemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| UK Market Status | Not retrieved *(data gap; Atorvastatin is known to be commercially available in the UK)* |
| Number of Marketing Authorisations | 0 *(data collection gap — does not reflect actual MHRA authorisation status)* |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned in this evidence pack. However, based on well-established pharmacological knowledge, Atorvastatin competitively inhibits **HMG-CoA reductase** — the rate-limiting enzyme in hepatic cholesterol biosynthesis. By reducing intracellular cholesterol in hepatocytes, the drug triggers compensatory upregulation of **LDL receptors (LDLR)** on the hepatocyte surface, substantially increasing the clearance of circulating LDL-C. Atorvastatin also reduces the hepatic production of apolipoprotein B-containing lipoproteins and has a prolonged plasma half-life (~20–30 hours) relative to earlier statins, enabling sustained 24-hour HMG-CoA reductase inhibition.

Familial Hypercholesterolaemia is a hereditary condition characterised by loss-of-function mutations in the **LDLR**, **APOB**, or **PCSK9** genes, resulting in severely impaired LDL-C clearance and markedly elevated LDL-C levels from birth. The compensatory upregulation of LDL receptors induced by atorvastatin directly addresses — albeit partially — the core pathophysiological deficit. In **heterozygous FH (heFH)**, where at least one functional LDLR allele is preserved, atorvastatin typically achieves 40–50% LDL-C reductions. In **homozygous FH (HoFH)**, residual receptor activity is near-absent and combination therapy (ezetimibe, PCSK9 inhibitors, or LDL apheresis) is generally required alongside a statin.

The biological plausibility is strongly reinforced by the clinical evidence base: multiple completed Phase 3 trials, long-term paediatric studies, and major clinical guidelines — including **NICE CG71 (Familial Hypercholesterolaemia)** and the **AACE/ACE Dyslipidaemia Guidelines** — consistently position high-intensity statins, including atorvastatin, as the cornerstone of FH management. The TxGNN prediction score of 99.42% reflects this near-universal mechanistic and clinical concordance.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | Three-year open-label study of atorvastatin in children and adolescents (from age 6) with heFH; characterised sustained LDL-C reduction, growth, BMI, and Tanner Stage development |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Completed | 800 | Large double-blind RCT comparing torcetrapib/atorvastatin vs maximally tolerated atorvastatin alone in heFH; carotid intima-media thickness assessed over 24 months; torcetrapib arm terminated due to safety findings |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Phase 3 | Completed | 400 | Six-month double-blind RCT of torcetrapib/atorvastatin vs atorvastatin monotherapy in heFH; provides direct comparator data for atorvastatin LDL-C lowering efficacy in FH |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Phase 3 | Completed | 30 | Forced-titration open-label study of torcetrapib/atorvastatin in HoFH; evaluated efficacy and safety in the most severe FH phenotype |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term (24-month) open-label extension assessing safety and tolerability of ezetimibe co-administered with atorvastatin or simvastatin in HoFH |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Double-blind efficacy and safety study of ezetimibe 10 mg added to atorvastatin 10 mg in heFH or CHD/multiple cardiovascular risk factors with inadequately controlled primary hypercholesterolaemia |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | Completed | 432 | Twelve-month open-label long-term safety of ezetimibe co-administered with atorvastatin 10–80 mg daily in heFH or CHD/multiple cardiovascular risk factors |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Completed | 39 | Eight-week study evaluating the pharmacokinetics, pharmacodynamics, safety and tolerability of atorvastatin specifically in children and adolescents with heFH |
| [NCT02460159](https://clinicaltrials.gov/study/NCT02460159) | Phase 3 | Completed | 135 | Long-term safety of ezetimibe/atorvastatin fixed-dose combination (10/10 mg and 10/20 mg) in Japanese patients with hypercholesterolaemia not controlled on statin monotherapy |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Double-blind study comparing alirocumab vs ezetimibe added to atorvastatin, vs atorvastatin dose increase, vs switch to rosuvastatin, in high cardiovascular-risk patients including heFH not controlled on atorvastatin |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Practice Guideline | *Endocrine Practice* | AACE/ACE dyslipidaemia guidelines; positions high-intensity statins, including atorvastatin, as first-line therapy in FH with defined LDL-C targets |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort/Outcomes Study | *JACC* | Statin therapy in heFH substantially reduces coronary artery disease event rates and all-cause mortality; quantifies absolute risk reduction in a defined FH population |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Narrative Review | *Curr Atheroscler Rep* | Review of emerging pharmacological therapies for HoFH; contextualises the role of statins (including atorvastatin) as a foundation alongside PCSK9 inhibitors and novel agents |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical Study | *J Clin Lipidol* | Three-year real-world study of atorvastatin in children/adolescents aged 6–17 years with heFH; demonstrates sustained LDL-C lowering and no adverse effects on growth or development |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Trial | *Nutr Metab Cardiovasc Dis* | Head-to-head comparison of atorvastatin vs simvastatin in heFH; atorvastatin achieved NCEP LDL-C goals in a higher proportion of patients with additional favourable effects on fibrinogen |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Interventional Study | *Echocardiography* | Atorvastatin therapy improves myocardial and peripheral blood flow reserve in FH subjects without overt coronary atherosclerosis, demonstrating early vascular pleiotropic benefits |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Clinical Review | *Ann Pharmacother* | Comprehensive review of atorvastatin pharmacology, efficacy, and safety in primary hypercholesterolaemia and mixed dyslipidaemias; foundational reference for dosing principles |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | *JACC* | Review of monitoring and care strategies for FH patients; emphasises intensive statin therapy as an essential component of long-term cardiovascular risk management |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic Epidemiology Study | *Pharmacogenomics J* | Next-generation sequencing strategy combining FH gene panels with pharmacogenomic regions relevant to statin prescription; supports genotype-guided atorvastatin selection and dose optimisation |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | Drug Review | *Rev Med Bruxelles* | Overview of atorvastatin mechanism (HMG-CoA reductase inhibition), prolonged half-life of active metabolites, and biological efficacy in cholesterol reduction, including LDL-C, TG, and Apo B reductions |

---

## UK Market Information

> ⚠️ **Data Collection Gap:** This evidence pack recorded **0 marketing authorisations** and a market status of "not marketed" for Atorvastatin in the UK. This is inconsistent with the well-established commercial presence of Atorvastatin in the UK under the brand name **Lipitor** (Pfizer) and numerous MHRA-approved generic formulations. This appears to be a failure in the data collection pipeline for this run and should be remediated by querying the MHRA Product Licence database directly.

For current, authoritative UK prescribing information, refer to:
- **BNF Chapter 2.12** — Lipid-regulating drugs (Atorvastatin monograph)
- **MHRA Product Licence search** for Atorvastatin calcium tablets
- **NICE CG71** — Identification and management of Familial Hypercholesterolaemia
- **NICE TA385** — Alirocumab for treating primary hypercholesterolaemia and mixed dyslipidaemia (contextualises statin background therapy)
- **SmPC** for Lipitor and relevant generic products

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for atorvastatin in familial hypercholesterolaemia is exceptionally robust (Evidence Level L1), comprising multiple completed Phase 3 randomised trials in both heterozygous and homozygous FH — including paediatric populations — as well as endorsement in major international clinical guidelines including NICE CG71. The TxGNN prediction (99.42%) effectively validates the model's performance by confirming an established clinical indication rather than proposing a novel one. The principal guardrails relate to ensuring appropriate patient stratification (heFH vs HoFH), managing combination therapy decisions, and resolving the UK licensing data gap.

**To proceed, the following is needed:**

- **Resolve the UK licensing data gap:** Re-run the MHRA product licence data collection pipeline to accurately capture all current marketing authorisations for atorvastatin in the UK
- **Retrieve formal MOA data:** Query the DrugBank API for DB01076 to populate the mechanism of action field (flagged as High severity data gap in this evidence pack)
- **Obtain full UK safety profile:** Retrieve MHRA SmPC warnings, contraindications, and drug interactions — particularly for CYP3A4 interactions (e.g., ciclosporin, clarithromycin, strong CYP3A4 inhibitors) relevant to FH patients on complex regimens
- **HoFH-specific pathway:** For homozygous FH patients, document eligibility criteria for LDL apheresis (NICE CG71) and PCSK9 inhibitor access (NICE TA393/TA394) as atorvastatin monotherapy is insufficient in this subgroup
- **Paediatric dosing review:** Confirm MHRA-approved age indications and dose ranges for children with FH, with reference to the atorvastatin SmPC and NICE CG71 paediatric recommendations
- **Pharmacogenomic consideration:** Review CYP3A4 and SLCO1B1 genotyping opportunities for FH patients at high risk of statin-associated myopathy, as highlighted in the pharmacogenomics literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

