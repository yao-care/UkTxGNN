---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the evidence pack as provided (drug info, UK regulatory record, predicted indications with clinical trial/literature evidence). This is a direct content-generation task per the report template already specified in the prompt — no additional skill invocation needed (no coding, no external state to verify beyond what's in the JSON).

A few data-quality notes before the report: the `taiwan_regulatory` block shows **0 UK marketing authorisations** (fenofibrate not currently licensed in this dataset), `original_moa` and all safety fields are flagged `[Data Gap]`, and the single clinical trial retrieved for the top-ranked indication (NCT03510715) tests **alirocumab**, not fenofibrate — I've flagged this honestly in the trial table rather than overstating the evidence.

---

# Fenofibrate: From Dyslipidaemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate-class lipid-regulating agent whose established use is in dyslipidaemia and mixed hyperlipidaemia. The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, a rare and severe inherited form of hypercholesterolaemia, with **1 clinical trial** and **11 publications** currently linked to this indication — though only a small subset of that literature provides fenofibrate-specific evidence in HoFH patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (no UK marketing authorisation on file); literature within the evidence pack describes fenofibrate as a fibrate-class agent for dyslipidaemia/mixed hyperlipidaemia |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 (observational/case-level clinical data; no fenofibrate-specific RCT identified) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the drug-level record (`original_moa` is a data gap). Based on the supporting literature retrieved for this candidate, fenofibrate is a fibric acid derivative and PPAR-alpha (peroxisome proliferator-activated receptor alpha) agonist ([PMID 2226216](https://pubmed.ncbi.nlm.nih.gov/2226216/); [PMID 20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/)). PPAR-alpha activation upregulates lipoprotein lipase and apolipoprotein genes, lowering plasma triglycerides and raising HDL-cholesterol, with a more modest effect on LDL-cholesterol.

Dyslipidaemia/mixed hyperlipidaemia and HoFH sit on the same clinical spectrum — both are disorders of lipoprotein metabolism — but they differ substantially in mechanism and severity. HoFH results from biallelic loss-of-function mutations in the LDL receptor (or related) pathway, producing very high LDL-C from birth and a markedly elevated risk of premature cardiovascular disease. Standard HoFH management (statins, PCSK9 inhibitors, lomitapide, LDL apheresis) targets LDL-receptor-dependent or receptor-independent LDL clearance directly, whereas fenofibrate's principal benefit is on triglycerides and HDL rather than LDL-receptor function.

Mechanistically, fenofibrate could plausibly serve as an **adjunct** in HoFH to address residual hypertriglyceridaemia and low HDL-C, rather than as primary LDL-lowering therapy. This is supported by one older case-level observation: in a small fenofibrate study of type II hyperlipoproteinaemia, "one patient with homozygous familial hypercholesterolemia showed the greatest fall of total and LDL cholesterol" among the cohort ([PMID 6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/)). This is a single, uncontrolled observation from 1984 and should not be read as robust efficacy evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated **alirocumab** (a PCSK9 inhibitor), not fenofibrate, in children/adolescents (8–17y) with HoFH on background lipid-lowering therapy. Retrieved as the only disease-matched trial in this dataset; it does **not** constitute direct trial evidence for fenofibrate in HoFH and should be treated as contextual/background-therapy information only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Clinical study (case-level) | Pharmacological Research Communications | Fenofibrate 300 mg/day in type II hyperlipoproteinaemia (n=22); one HoFH patient showed the greatest fall in total and LDL cholesterol in the cohort — the only direct fenofibrate-in-HoFH data point identified |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Characterised PK interactions of lomitapide (an approved HoFH adjunct therapy) with commonly co-administered lipid drugs including fenofibrate |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Case report/review | Internal Medicine Journal | Discusses liver transplantation for HoFH and notes emerging lipid-lowering drug treatments as alternatives to LDL apheresis |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Positions fenofibrate monotherapy as indicated mainly for severe hypertriglyceridaemia (>500 mg/dL) with modest cardiovascular benefit, in the broader context of non-statin lipid drugs |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | Reviews pharmacologic/surgical treatment of dyslipidaemic children, listing fenofibrate among agents used in familial hypercholesterolaemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidaemia and cardiovascular prevention guideline; general lipid-management framework, not HoFH-specific |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Reviews dyslipidaemia management in pregnancy; general context only, not HoFH-specific |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews LDL-C lowering with statins and PCSK9 inhibitors; fenofibrate not a focus |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe as a cholesterol-absorption inhibitor; comparator drug class context only |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Reviews atorvastatin pharmacology; comparator drug class context only |

---

## UK Market Information

Fenofibrate does not currently hold a UK marketing authorisation in this dataset (`market_status: Not marketed`, 0 authorisations on record). No product name, dosage form, or licensed indication text is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: `key_warnings`, `contraindications`, and drug–drug interaction data are all recorded as data gaps in this evidence pack and could not be retrieved (see "To proceed" below).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking** data gap (DG001 — missing SmPC warnings/contraindications) prevents any initial safety assessment (S1 stage) for this candidate.
- Fenofibrate has **no current UK marketing authorisation** in this dataset, so a clinical-use pathway would need to be established before any repurposing could proceed.
- The only clinical trial retrieved for HoFH evaluates a different drug (alirocumab); direct clinical evidence of fenofibrate specifically in HoFH is limited to a single 1984 case-level observation and supporting mechanistic/PK literature — insufficient to support progression on efficacy grounds alone.

**To proceed, the following is needed:**
- Retrieve TFDA/MHRA SmPC warnings and contraindications (DG001, Blocking)
- Confirm mechanism of action via DrugBank API query (DG002)
- Clarify UK licensing status/pathway, given 0 current marketing authorisations
- Re-verify whether NCT03510715 involves fenofibrate as a concomitant/background therapy, or should be excluded as a non-relevant match
- Given standard HoFH care already centres on LDL-receptor-targeted therapies (statins, PCSK9 inhibitors, lomitapide, apheresis), clarify fenofibrate's intended clinical positioning as adjunct triglyceride/HDL therapy rather than primary LDL-lowering treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

