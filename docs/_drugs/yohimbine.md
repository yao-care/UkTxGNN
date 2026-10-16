---
layout: default
title: Yohimbine
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Yohimbine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the available data"
monitor_inn: "Yohimbine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "migraine with or without aura, susceptibility to", "primary hereditary glaucoma", "headache disorder", "transient ischemic attack (disease)", "common cold", "open-angle glaucoma"]
---

# Yohimbine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Yohimbine: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Yohimbine is a selective alpha-2 adrenoceptor antagonist marketed in the UK as a 5 mg tablet, although the data compiled for this report do not record an approved indication.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **7 publications**, almost all preclinical or indirect.
The evidence is weak, and the pharmacology points in an unfavourable direction, because migraine-related alpha-2 research mainly involves agonists such as clonidine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. From pharmacology records, yohimbine is a selective alpha-2 adrenoceptor antagonist with moderate affinity for alpha-1 adrenoceptors. It also binds several serotonin receptor subtypes (5-HT1A, 1B, 1D, 1E, 1F, 2B, 5A and 7). Many of these serotonin receptors are relevant to existing migraine treatments.

Preclinical work links noradrenergic and alpha-2 signalling to cortical spreading depression (the biological basis of migraine aura), trigeminovascular nociception and meningeal artery tone. This makes the pathway plausibly relevant.

However, the direction of effect is a concern. Alpha-2 agonists such as clonidine are the agents studied in migraine, and an antagonist such as yohimbine could act in the opposite direction. The literature is largely animal or in vitro work, and no clinical study has tested yohimbine in migraine. The link is therefore indirect.

Other predictions in the model's top ten (migraine with brainstem aura, headache disorder, migraine susceptibility) largely reuse the same migraine literature and add no independent support. Several others (ADHD, transient ischaemic attack, glaucoma) have mechanistic evidence suggesting yohimbine could worsen rather than improve the condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15829916](https://pubmed.ncbi.nlm.nih.gov/15829916/) | 2005 | Preclinical (rat) | J Cereb Blood Flow Metab | Both adrenergic agonists and antagonists influenced cortical spreading depression migration, suggesting a possible role in migraine prophylaxis |
| [29856967](https://pubmed.ncbi.nlm.nih.gov/29856967/) | 2018 | Preclinical (animal) | Exp Neurol | Stress modulated cortical excitability via alpha-2 adrenergic and glucocorticoid receptors, as assessed by spreading depression |
| [15778266](https://pubmed.ncbi.nlm.nih.gov/15778266/) | 2005 | Preclinical (animal) | J Pharmacol Exp Ther | Role of dopamine in a model of trigeminovascular nociception |
| [17103145](https://pubmed.ncbi.nlm.nih.gov/17103145/) | 2006 | Preclinical (isolated tissue) | Naunyn Schmiedebergs Arch Pharmacol | Effects of current and prospective antimigraine drugs on porcine meningeal artery |
| [23707349](https://pubmed.ncbi.nlm.nih.gov/23707349/) | 2013 | Preclinical (rat) | Eur J Pharmacol | Ergotamine's pressor responses (used in acute migraine) were blocked by yohimbine, identifying the alpha-adrenoceptor subtypes involved |
| [2985264](https://pubmed.ncbi.nlm.nih.gov/2985264/) | 1985 | Small observational study (children) | Cephalalgia | Platelet alpha-adrenoceptor binding measured with radiolabelled yohimbine; binding affinity differed between migrainous children and controls |
| [2905875](https://pubmed.ncbi.nlm.nih.gov/2905875/) | 1988 | Review | Ann Clin Res | Overview of therapeutic applications of drugs acting on alpha-adrenoceptors, mainly alpha-2 agonists |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704050Y0AAAMAM (BNF-style product code) | Yohimbine HCl Tab 5 mg | Tablet (not recorded in data) | Not recorded in data |

Only one single-ingredient product is listed, and it is recorded as valid. The compiled data do not give the manufacturer, dosage form or approved indication.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph:** The TxGNN knowledge graph (drug–disease contraindication links, not label text) lists anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, heart disease and cardiovascular disease.
- **Drug interactions (20 records):**
  - **Major:** iobenguane (I-131).
  - **Moderate:** lorcaserin, troglitazone, doxepin (oral and topical) and procarbazine.
  - **Minor:** morphine (including liposomal).
  - Receptor-binding records (serotonin, alpha-2 adrenoceptors) are also on file and are not interactions in the clinical sense.
- **Context from the pharmacology records:** One source states that yohimbine is no longer recommended as a treatment for erectile dysfunction.

Warning and contraindication text from the product information was not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and the literature is almost entirely animal, in vitro or indirect. Alpha-2 agonists, not antagonists, are the agents associated with migraine research, so the direction of effect is questionable. The very high prediction score appears to reflect model proximity rather than independent evidence. The knowledge graph also flags cardiovascular, hepatic, renal and anxiety-related conditions, which are relevant to a migraine population.

**To proceed, the following is needed:**
- Product information (SmPC) warnings, contraindications and the approved indication for the UK-listed tablet
- Detailed mechanism-of-action data, specifically whether alpha-2 antagonism could plausibly help rather than aggravate migraine
- Preclinical studies testing yohimbine itself in migraine models (for example spreading depression and trigeminovascular models)
- A cardiovascular and psychiatric safety assessment for the target population before any clinical study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

