---
layout: default
title: Rosiglitazone
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 0
---

# Rosiglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Rosiglitazone: From Type 2 Diabetes Mellitus — No TxGNN Predictions Available

## One-Sentence Summary

Rosiglitazone is a thiazolidinedione-class oral antidiabetic agent, originally indicated for the treatment of Type 2 Diabetes Mellitus via insulin sensitisation.
The current Evidence Pack contains **no TxGNN-predicted indications** for this drug, and Rosiglitazone is **not authorised for use in the United Kingdom** following market withdrawal in 2010.
A full repurposing evaluation cannot proceed until the critical data gaps identified below are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Not available — predictions absent from Evidence Pack |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (no prediction data present) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Drug Background and Mechanistic Context

Detailed, structured mechanism of action data is not available in this Evidence Pack. Based on published pharmacological knowledge, Rosiglitazone belongs to the thiazolidinedione (TZD) class and acts as a selective agonist of the peroxisome proliferator-activated receptor gamma (PPARγ), a nuclear receptor that regulates genes involved in glucose uptake, adipogenesis, and lipid metabolism. Its primary therapeutic effect is to improve peripheral insulin sensitivity in skeletal muscle and adipose tissue, reducing fasting and post-prandial blood glucose in patients with Type 2 Diabetes Mellitus.

The broader downstream effects of PPARγ activation — including modulation of inflammatory cytokines, adipokines, and cellular differentiation pathways — have prompted research interest in potential applications beyond glycaemic control. Published literature has explored Rosiglitazone's activity in conditions such as polycystic ovary syndrome (PCOS), non-alcoholic fatty liver disease (NAFLD), and certain neuroinflammatory disorders. However, none of these have been captured as TxGNN-predicted candidates in the current submission.

Since no predicted indications are present in the Evidence Pack, a formal mechanistic justification for a specific repurposing direction cannot be provided at this stage. Rerunning the TxGNN prediction pipeline is required before this analysis can proceed.

---

## UK Market Information

Rosiglitazone currently holds **no MHRA marketing authorisations** in the United Kingdom. The product (brand name **Avandia**, GlaxoSmithKline) was suspended across the European Union and United Kingdom following an EMA review in September 2010, which concluded that the cardiovascular benefits of Rosiglitazone no longer outweighed its risks — specifically an increased incidence of myocardial infarction and heart failure. There is no active BNF monograph for this drug, and it is not available for NHS prescribing or dispensing.

No licence table can be generated as there are no UK authorisations on record.

---

## Safety Considerations

Formal SmPC data is unavailable for the UK market given the drug's withdrawn status. The following safety signals are well-established from published regulatory assessments and pharmacovigilance records and are relevant to any future repurposing consideration:

- **Cardiovascular risk**: Increased incidence of myocardial infarction and ischaemic heart disease, forming the primary basis for EMA and MHRA suspension in 2010. This remains the most significant safety concern.
- **Heart failure and fluid retention**: Rosiglitazone causes sodium and water retention, which may precipitate or worsen congestive cardiac failure. Contraindicated in patients with any degree of heart failure.
- **Fracture risk**: Post-marketing data demonstrated an increased risk of peripheral fractures, predominantly in female patients.
- **Hepatotoxicity**: Liver function monitoring was required during active use; rare cases of hepatic failure were reported.
- **Macular oedema**: Reported in post-marketing surveillance; reversible on discontinuation.
- **Bladder cancer signal**: A theoretical class concern exists with PPARγ agonists (more prominently with pioglitazone); this warrants consideration in any long-term repurposing application.

Any further evaluation should reference the historical EMA assessment report (EMEA/H/C/268) and EMA's 2010 referral review. Suspected adverse reactions should be reported via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk).

---

## Critical Data Gaps

The following gaps were identified in this Evidence Pack and are prerequisites for a full evaluation:

| Gap ID | Item | Severity | Impact on Evaluation |
|--------|------|----------|----------------------|
| DG001 | SmPC warnings and contraindications (structured regulatory label data) | Blocking | Safety pre-assessment cannot be completed |
| DG002 | Mechanism of action — structured DrugBank data | High | Mechanistic relevance analysis is impaired |
| — | TxGNN predicted indications | Blocking | No repurposing candidate exists to evaluate |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Rosiglitazone is critically incomplete — no TxGNN-predicted indications have been generated, no UK marketing authorisations exist, and structured safety and mechanistic data are absent. Beyond data gaps, Rosiglitazone's regulatory history (EU/UK market withdrawal due to serious cardiovascular risk) constitutes a substantial independent barrier to any repurposing programme within the NHS context.

**To proceed, the following is needed:**

- **Data resolution**: Address DG001 (structured SmPC/label safety data) and DG002 (structured MOA from DrugBank API) before re-evaluation
- **Pipeline rerun**: Execute the TxGNN prediction pipeline for DB00412 to generate candidate indications; confirm the drug node is present and correctly mapped in the knowledge graph
- **Regulatory status review**: Confirm whether the MHRA suspension of Rosiglitazone (following the 2010 EMA referral) remains fully in force, or whether any partial lifting applies in the post-Brexit UK regulatory framework
- **Cardiovascular risk framework**: Any proposed repurposing indication must be accompanied by a formal cardiovascular safety risk stratification plan, given the class-level MI and heart failure signals that led to market withdrawal
- **Pharmacovigilance review**: Independent review of post-withdrawal global safety data (including FDA's 2013 partial restriction lift in the US) to establish whether a safety-restricted development pathway is scientifically justifiable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

