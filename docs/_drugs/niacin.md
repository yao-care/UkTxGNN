---
layout: default
title: Niacin
parent: Model Prediction Only (L5)
nav_order: 441
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Niacin: predicted new indication Homozygous familial hypercholesterolaemia (evidence level L5). Approved use: Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia…"
---

# Niacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Niacin: From Hyperlipidaemia to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Niacin (nicotinic acid) is a lipid-modifying agent originally used for hypertriglyceridaemia, hyperlipidaemia and familial hyperlipidaemia.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolaemia (HoFH)**,
but there are currently **no registered clinical trials** and only **review-level publications** (none niacin-specific for HoFH), so the evidence is mainly model-based.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia, vitamin deficiency disorder (the UK authorisation record contains no indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolaemia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction with no direct studies; the data compiled for this report graded it L4, but the available literature consists of reviews and general lipid-therapy papers, not preclinical or mechanism studies of niacin in HoFH) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From general pharmacological knowledge, niacin lowers LDL-cholesterol, VLDL and triglycerides and raises HDL-cholesterol. This is thought to occur through reduced hepatic VLDL/apoB secretion (via DGAT2 inhibition) and GPR109A-mediated suppression of adipose tissue lipolysis.

Niacin is already used in hyperlipidaemia and familial hyperlipidaemia, which gives a plausible but indirect link to HoFH. However, HoFH is caused by absent or severely defective LDL receptor function. Niacin's LDL-lowering effect does not depend mainly on LDL receptor upregulation, so some residual benefit is conceivable, but it is likely to be modest relative to the severity of the disease.

The very high TxGNN score probably reflects the close similarity to the existing familial hyperlipidaemia indications rather than independent HoFH-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications retrieved are mostly reviews of familial hypercholesterolaemia or lipid-lowering therapy in general. None reports a niacin trial in HoFH.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Challenges in diagnosing and treating HoFH, a rare disease with absent or impaired LDL receptor function |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern management of homozygous and heterozygous familial hypercholesterolaemia |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Literature analysis of diagnosis and treatment options for familial hypercholesterolaemia |
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Scientific statement/Review | Arterioscler Thromb Vasc Biol | Non-statin LDL-lowering therapy; placebo-controlled trials showed niacin, bile acid sequestrants and fibrates each reduce CVD endpoints as monotherapy |
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Review | Expert Rev Cardiovasc Ther | Critical review of non-statin treatments, including niacin, for dyslipoproteinaemia |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | Review | Nat Rev Cardiol | Lipid-modifying agents beyond statins for severe hypercholesterolaemia or mixed dyslipidaemia |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atheroscler Suppl | Achievements and unmet needs in HoFH, including apheresis and lipid-lowering drugs |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Lomitapide (approved for HoFH) pharmacokinetic interactions with several lipid-lowering drugs, including niacin |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | Clinical study | Arteriosclerosis | Drug treatment of familial hypercholesterolaemia in children, including a small number with homozygous disease |
| [19947811](https://pubmed.ncbi.nlm.nih.gov/19947811/) | 2009 | Case report | Pharmacotherapy | Xanthomas in an 18-year-old with HoFH |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0212000U0AAAVAV | Nicotinic Acid Tab 500 mg M/R | Modified-release tablet (as implied by the product name) | Not available in the data compiled for this report |

Only one valid single-ingredient authorisation record was found. Its MHRA licence number format and indication text should be verified against the MHRA register and the BNF.

## Safety Considerations

**Drug Interactions** (100 interactions were identified; those listed in the data compiled for this report are mainly with glucose-lowering agents):
- **Moderate:** acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, ertugliflozin, exenatide, metformin, acetohexamide, glimepiride, glipizide, glyburide, and several insulins (human, aspart, degludec)
- **Minor:** acetylsalicylic acid (aspirin)

Niacin may affect glycaemic control, so closer glucose monitoring is advisable in patients on antidiabetic therapy. For other warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests almost entirely on the model score and on similarity to niacin's existing lipid indications. There are no registered trials and no niacin-specific HoFH publications, and the expected effect is likely modest in a disease driven by LDL receptor failure.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to support the mechanistic-link analysis
- A targeted search for niacin data in HoFH or other severe familial hypercholesterolaemia populations
- Safety information from the SmPC and BNF (warnings and contraindications), which is currently missing and blocks safety screening
- Confirmation of the approved indication, dosage form and manufacturer for the UK authorisation
- Comparison with established HoFH options (e.g. statins plus ezetimibe, PCSK9 inhibitors, lomitapide, LDL apheresis) to define any realistic role for niacin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

