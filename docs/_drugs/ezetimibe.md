---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the evidence pack fields directly (predicted_indications[0] = **hyperlipoproteinemia**, score 0.9963, evidence_level L1) as the basis for the report, following the fixed section order.

# Ezetimibe: From Hypercholesterolaemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor established for hypercholesterolaemia and mixed dyslipidaemia. The TxGNN model predicts it may also be effective for **Hyperlipoproteinemia**, a closely related lipid disorder, with **50 clinical trials** and **19 publications** currently available as supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not itemised in this evidence pack (no licence records supplied); ezetimibe is established as a cholesterol absorption inhibitor for hypercholesterolaemia/mixed dyslipidaemia |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack (DG002, High severity). However, the repurposing rationale attached to this candidate provides pharmacological detail: ezetimibe selectively inhibits the Niemann-Pick C1-Like 1 (NPC1L1) cholesterol transporter at the intestinal brush border, blocking absorption of both dietary and biliary cholesterol. This reduces hepatic cholesterol stores and upregulates LDL receptor expression, lowering circulating LDL-C.

Hyperlipoproteinemia is a broad classification of lipid disorders characterised by elevated LDL-C and/or triglycerides — the same physiological axis that ezetimibe's NPC1L1-mediated mechanism directly targets. This is not a distant cross-indication extrapolation; it sits within the drug's core pharmacological action, which is why the evidence base is unusually dense (50 registered trials, 19 publications) for a "predicted" indication.

This is reflected in the trial record itself: numerous completed Phase 3 studies test ezetimibe (alone or in fixed-dose combinations with simvastatin, fenofibrate, niacin, or newer agents such as obicetrapib) specifically in mixed hyperlipidaemia and related lipid disorders, alongside large-scale post-marketing surveillance programmes in Japan and the Philippines confirming real-world safety and efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin plus fenofibrate coadministration for cholesterol lowering in mixed hyperlipidaemia — key drug-specific efficacy trial |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1,220 | Ezetimibe/simvastatin + extended-release niacin vs monotherapy in Type IIa/IIb hyperlipidaemia |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib 10 mg + ezetimibe 10 mg fixed-dose combination on top of maximally tolerated lipid therapy in HeFH/ASCVD |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration: efficacy and safety in mixed hyperlipidaemia |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A (post-marketing) | Completed | 11,332 | Large Japanese post-marketing surveillance of Zetia (ezetimibe) mono/combination therapy — real-world safety and efficacy |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A (post-marketing) | Completed | 4,105 | Filipino post-marketing surveillance of ezetimibe safety, tolerability and efficacy |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A (post-marketing) | Completed | 1,794 | 52-week long-term Japanese post-marketing surveillance of Zetia mono/combination therapy |
| [NCT00655265](https://clinicaltrials.gov/study/NCT00655265) | Phase 4 | Completed | 86 | Colesevelam as add-on to statin + ezetimibe in difficult-to-treat familial hypercholesterolaemia |
| [NCT00189085](https://clinicaltrials.gov/study/NCT00189085) | Phase 4 | Completed | 20 | Effect of ezetimibe on postprandial hyperlipidaemia and endothelial dysfunction in metabolic syndrome |

*Note: 50 trials in total are recorded against this indication in the evidence pack; the 10 above were prioritised by relevance grade, phase and enrolment size.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM Phase 3 trial: obicetrapib + ezetimibe fixed-dose combination significantly lowers LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | RCT of oral PCSK9 inhibitor enlicitide in HeFH patients not at LDL-C goal despite existing lipid-lowering therapy (including ezetimibe) |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Overview of familial hypercholesterolaemia management, with ezetimibe as an LDL-C-lowering adjunct to statins |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH epidemiology, underdiagnosis/undertreatment and drug therapy overview |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | Global burden and management approaches to familial hypercholesterolaemia |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | Comprehensive FH primer covering LDLR/APOB/PCSK9 pathways and treatment options |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Molecular Sciences | Pathophysiology, diagnosis and treatment of postprandial hyperlipidaemia |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | Review of current drugs targeting hyperlipidaemia |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors, contextualising statin/ezetimibe intolerance |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Review | European Heart Journal | EAS consensus statement on underdiagnosis/undertreatment of FH, with screening and treatment guidance |

*Note: 19 publications in total are recorded against this indication; the 10 above were prioritised by study type (RCT first) and recency.*

## UK Market Information

No marketing authorisation entries are recorded against ezetimibe in this evidence pack (0 licences on file; market status recorded as **Not Marketed**). Before any further evaluation proceeds, current UK licensing and product status (e.g. Ezetrol, or combination products) should be confirmed directly via the MHRA Products database and the current BNF entry.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this evidence pack's structured safety fields (key warnings, contraindications, drug interactions) were not populated at the time of this data cutoff, and label warnings/contraindications are flagged as a blocking data gap (DG001) preventing an initial safety assessment.*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (e.g. NCT00093899, the ENHANCE trial NCT00552097, NCT00271817, NCT06005597) directly evaluate ezetimibe-containing regimens in hyperlipidaemia and closely related lipid disorders, meeting the L1 evidence threshold. However, ezetimibe currently has no UK marketing authorisation on file in this evidence pack, and a blocking safety data gap (SmPC warnings/contraindications) means the candidate cannot yet clear an initial safety screen.

**To proceed, the following is needed:**
- SmPC/labelling warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism-of-action data via DrugBank (DG002)
- Verification of current UK marketing authorisation status via the MHRA Products database
- A completed drug–drug interaction profile (DDI query currently returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

