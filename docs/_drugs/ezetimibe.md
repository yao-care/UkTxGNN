---
layout: default
title: Ezetimibe
parent: High Evidence (L1-L2)
nav_order: 273
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-15
description: "Ezetimibe: predicted new indication Hyperlipoproteinaemia (evidence level L1). Approved use: Hyperlipidaemia (including familial hypercholesterolaemia and sitoste…"
monitor_inn: "Ezetimibe"
predicted_indications: ["hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ezetimibe: From Hyperlipidaemia to Hyperlipoproteinaemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor, originally used to treat hyperlipidaemia, including familial and homozygous familial hypercholesterolaemia and sitosterolaemia.
The TxGNN model predicts it may be effective for **hyperlipoproteinaemia**, with **40 clinical trials** and **19 publications** compiled for this prediction.
This is largely an on-label or near-on-label use rather than true repurposing, so the prediction mainly confirms existing practice.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidaemia (including familial hypercholesterolaemia and sitosterolaemia); the UK authorisation record has no indication text |
| Predicted New Indication | Hyperlipoproteinaemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

Other predictions in the data: familial hypercholesterolaemia (99.38%, L1, Proceed with Guardrails), hypercholesterolaemia due to cholesterol 7alpha-hydroxylase deficiency (99.25%, L5, Hold) and cholesterol-ester transfer protein deficiency (99.09%, L5, Hold).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, ezetimibe inhibits NPC1L1-mediated intestinal cholesterol absorption, which lowers LDL cholesterol. It works both as monotherapy and as an add-on to statins.

Hyperlipoproteinaemia is essentially the same disease space as the original indication (hyperlipidaemia). The prediction is therefore close to on-label use, and the efficacy of ezetimibe alone and with statins is well established.

For the two weaker predictions, the rationale is much thinner:
- **Cholesterol 7alpha-hydroxylase deficiency:** The statin-resistant hypercholesterolaemia and the NPC1L1–bile acid link are plausible, but the only supporting paper is a preclinical mouse study.
- **CETP deficiency:** This condition raises HDL-C and lowers LDL-C, so there is little rationale for an LDL-lowering agent. The retrieved literature does not address ezetimibe in this condition.

---

## Clinical Trial Evidence

The table lists the most relevant trials for the top prediction (hyperlipoproteinaemia), prioritising trials that test ezetimibe directly.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Completed | 40 | Randomised comparison of ezetimibe versus statin, and statin plus ezetimibe versus statin alone, in hypercholesterolaemia |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label treatment-use study of ezetimibe 10 mg/day in homozygous FH or sitosterolaemia |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Ezetimibe/simvastatin plus extended-release niacin in type IIa/IIb hyperlipidaemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate plus ezetimibe in mixed hyperlipidaemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin plus fenofibrate in mixed hyperlipidaemia |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin versus simvastatin alone on carotid atherosclerosis in heterozygous FH |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | Completed | 127 | Ezetimibe/rosuvastatin with candesartan/amlodipine in hypertension and hyperlipidaemia |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completed | 1794 | 52-week post-marketing surveillance of Zetia in Japan (observational) |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Completed | 4105 | Post-marketing surveillance of ezetimibe in Filipino patients |

For the second prediction (familial hypercholesterolaemia), additional directly relevant trials include:
- [NCT03885921](https://clinicaltrials.gov/study/NCT03885921): Phase 3, completed, n=44. Long-term (up to 24 months) open-label safety study of ezetimibe plus a statin in homozygous FH.
- [NCT00867165](https://clinicaltrials.gov/study/NCT00867165): Phase 3, completed, n=138. Randomised, double-blind, placebo-controlled study of ezetimibe monotherapy in children aged 6–10 years with primary hypercholesterolaemia.
- [NCT00129402](https://clinicaltrials.gov/study/NCT00129402): Phase 3, completed, n=248. Ezetimibe with simvastatin in adolescents with heterozygous FH.

Several other trials in the data use ezetimibe only as a comparator or background therapy (for example evolocumab and obicetrapib studies). They support the clinical context but do not test ezetimibe directly.

The two lower-ranked predictions have no registered clinical trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM: fixed-dose obicetrapib plus ezetimibe for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab in heterozygous FH despite intensive statin therapy with or without ezetimibe |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5: inclisiran in homozygous FH |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug and Therapeutics Bulletin | Ezetimibe update: lowers LDL-C alone or with a statin; no cardiovascular outcome evidence at that time |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | American Journal of Cardiovascular Drugs | Ezetimibe inhibits intestinal absorption of cholesterol and plant sterols |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | Current drugs targeting hyperlipidaemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C-lowering therapies on top of statins, ezetimibe and PCSK9 inhibitors |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohort | Lancet | Worldwide retrospective cohort of homozygous FH |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consensus statement | Eur Heart J | European Atherosclerosis Society guidance on FH screening and treatment |

Most of the RCTs above concern other agents, with ezetimibe as background or comparator therapy. Direct ezetimibe evidence comes mainly from the trials listed earlier and the two ezetimibe reviews.

For the lower-ranked predictions:
- **7alpha-hydroxylase deficiency:** [34943976](https://pubmed.ncbi.nlm.nih.gov/34943976/) (Cells, 2021) is a preclinical mouse study showing that NPC1L1 deficiency alters ileal FGF15 expression and the bile acid pool.
- **CETP deficiency:** [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) (Eur Heart J, 2025) is a general review of lipid-lowering targets. [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) is an animal model study of PCSK9 antibody.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0212000L0AAAAAA | Ezetimibe tablet 10 mg | Tablet (10 mg) | Indication text not recorded in the compiled data |

One valid single-ingredient authorisation is recorded. The dosage form and indication details were not captured, so please check the current SmPC and BNF (lipid-regulating drugs) for the licensed indications. Where relevant, check NICE guidance for the appraised use of ezetimibe.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):** pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis and nodular fasciitis. These come from drug–disease relationship data and should be verified against the SmPC.

**Drug Interactions** (100 recorded; main ones listed):
- **Moderate:** chenodeoxycholic acid, eluxadoline, rosuvastatin, simvastatin.
- **Severity not classified:** include calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, acarbose, morphine, metformin, omeprazole, palonosetron, rosiglitazone, lansoprazole, cimetidine, vancomycin and lactulose.

Label warnings and contraindications were not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for hyperlipoproteinaemia and familial hypercholesterolaemia). **Hold** for 7alpha-hydroxylase deficiency and CETP deficiency.

**Rationale:**
- Hyperlipoproteinaemia and familial hypercholesterolaemia are on-label or near-on-label uses, supported by several completed Phase 3 trials (L1). This is confirmation of existing use rather than new repurposing.
- The two rare-condition predictions rest on the model score and general lipid biology, with no clinical evidence (L5), so they should not be pursued now.

**To proceed, the following is needed:**
- Review of the UK SmPC to confirm licensed indications, since the authorisation record has no indication text and the dosage form is missing.
- Detailed mechanism of action data.
- Label-based warnings and contraindications, to replace the knowledge-graph signals.
- A hepatic and muscle safety monitoring plan, particularly when combined with statins.
- For heterozygous FH, confirmation of the licensed population (including paediatric use) against the SmPC.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

