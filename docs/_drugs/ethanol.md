---
layout: default
title: Ethanol
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Ethanol: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Ethanol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Ethanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Ethanol: From No Recorded Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

> Ethanol is a long-established agent with one UK marketing authorisation on record, but no approved indication text is available in the data compiled for this report.
> The TxGNN model predicts it may be relevant to **migraine disorder**, but there are **no clinical trials** and the retrieved literature mainly describes ethanol as a migraine **trigger**, not a treatment.
> This prediction should be regarded as unsupported as a repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ethanol, and no original indication is recorded, so the link between an existing use and migraine cannot be established from the data compiled.

The high TxGNN score (0.9929) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of therapeutic benefit. The supporting literature points in the harmful direction:

- Ethanol-derived acetaldehyde acts through the CGRP receptor and TRPA1 in Schwann cells to evoke periorbital mechanical allodynia in mice (PMID 37101198).
- Opening of ATP-sensitive potassium channels activates meningeal nociceptors, a proposed route to migraine headache (PMID 40785517).
- Genetic association studies (alcohol dehydrogenase genotype, GABA receptor polymorphisms) link alcohol metabolism and GABAergic signalling to migraine susceptibility, not to treatment response.

Alcohol is widely regarded as a migraine trigger. The prediction should therefore not be read as support for repurposing. A second predicted indication, migraine with brainstem aura (score 0.9914), has the same weaknesses: no trials and no ethanol-specific therapeutic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below reports ethanol as a treatment for migraine. Several describe other compounds or are keyword-matching artefacts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | Reviews the complex relationship between alcohol and migraine |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Preclinical | J Biomed Sci | Acetaldehyde, via CGRP receptor and TRPA1, mediates ethanol-evoked allodynia in mice, relevant to migraine triggering |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | Preclinical | Cephalalgia | KATP channel opening activates meningeal nociceptors; implications for migraine origin |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetic association | Headache | Alcohol dehydrogenase 2 genotype and migraine risk |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | Cohort | Aerosp Med Hum Perform | Migraine history and outcomes in military pilots |
| [29299688](https://pubmed.ncbi.nlm.nih.gov/29299688/) | 2018 | Genetic association | J Neural Transm | GABA receptor gene polymorphisms and migraine risk |
| [19222595](https://pubmed.ncbi.nlm.nih.gov/19222595/) | 2009 | RCT (different drug: carisbamate) | Headache | Dose-response of carisbamate for migraine prevention; not ethanol |
| [20456191](https://pubmed.ncbi.nlm.nih.gov/20456191/) | 2010 | RCT (different intervention: menthol) | Int J Clin Pract | Topical menthol 10% for acute migraine; not ethanol |
| [30177906](https://pubmed.ncbi.nlm.nih.gov/30177906/) | 2018 | Pilot study (different compound: palmitoylethanolamide) | Front Neurol | Add-on palmitoylethanolamide in migraine with aura; not ethanol |
| [42153521](https://pubmed.ncbi.nlm.nih.gov/42153521/) | 2026 | Scoping review | Drug Alcohol Rev | CGRP signalling in alcohol use disorders |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190100000AAADAD | Ethanol 90% (including duty) | Not recorded | Not recorded |

---

## Safety Considerations

**Drug Interactions** (100 interactions recorded; selected examples shown):

- **Major:** eluxadoline
- **Moderate:** acarbose, albiglutide, acetohexamide, alogliptin, acetylsalicylic acid, atropine, bupropion, canagliflozin, chlorpropamide, dapagliflozin, dicyclomine, dronabinol, dulaglutide, empagliflozin
- **Minor:** doxycycline, cimetidine

Many of the moderate interactions involve antidiabetic agents, which is relevant to glycaemic control.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no clinical trials, and the literature indicates ethanol is a migraine trigger rather than a treatment. Evidence is at L5 (model prediction only).

**To proceed, the following is needed:**
- Clarification of the approved indication(s) and dosage form for the UK authorisation
- Mechanism of action data
- Warnings and contraindications from the SmPC and BNF
- Any credible clinical or mechanistic evidence of therapeutic benefit in migraine, as opposed to trigger effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

