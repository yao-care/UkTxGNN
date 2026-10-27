---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Cyclopentolate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Cycloplegia"
monitor_inn: "Cyclopentolate"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Cyclopentolate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Cyclopentolate: From Cycloplegia to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Cyclopentolate is an antimuscarinic eye drop, originally used to produce cycloplegia (temporary paralysis of the eye's focusing muscle).
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cyclopentolate is a muscarinic antagonist (anticholinergic). Its use in cycloplegia is established, and mechanistically the same class effect could be relevant to conditions involving muscarinic-driven smooth muscle activity.

Cauda equina syndrome causes bladder, bowel and sexual dysfunction through nerve compression. An antimuscarinic could theoretically ease secondary detrusor overactivity symptoms. It would not treat the underlying compression, which needs surgical decompression. The high TxGNN score is a computational prediction only.

There are also practical concerns. Cyclopentolate is formulated only as an ophthalmic solution, so systemic exposure would be uncharacterised. Systemic anticholinergic effects, including CNS effects and urinary retention, would be a particular risk in this condition.

Two other predictions were also generated, both with L5 evidence and a Hold recommendation:
- **Neurogenic bladder (obsolete ontology term)**, score 99.40%. Antimuscarinics such as oxybutynin and tolterodine are established for neurogenic detrusor overactivity, so a class-level rationale exists. However, cyclopentolate has no clinical data here, and better-characterised, bladder-selective options are available. The term should be mapped to current terminology (neurogenic detrusor overactivity) before further work.
- **Irritable bowel syndrome**, score 99.27%. Anticholinergic antispasmodics such as dicyclomine and hyoscyamine are used for IBS symptoms. There is no evidence for cyclopentolate specifically, no oral or systemic formulation, and established alternatives already exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1105000E0AAABAB | Cyclopentolate HCl Eye Drops 0.5% | Eye drops | Not stated in the data compiled |

The authorisation number above is as recorded in the compiled data and does not follow the usual PL format, so it should be verified against the MHRA register. The product is a topical ophthalmic preparation.

## Safety Considerations

The compiled data holds no label-based warnings, contraindications or interaction records for this drug. The following comes from knowledge-graph drug-disease contraindication links, not from label text, and should be confirmed against the SmPC:

- **Contraindication links in the knowledge graph:**
  - Eye: angle-closure (closed-angle) glaucoma
  - Cardiovascular: hypertension, heart disease, coronary artery disease, sudden cardiac arrest, heart conduction disease, arteriosclerosis and atherosclerosis
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - Other: benign prostatic hyperplasia, brain injury, brain disease, Down syndrome

For full safety information, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications rest on model prediction only (L5), with no trials or publications. The ophthalmic-only formulation and the anticholinergic risks in a neurological and urological setting, together with established alternatives, give little incentive to pursue repurposing now.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (for example from DrugBank)
- SmPC-based warnings and contraindications, as the current safety data are incomplete
- Evidence of adequate systemic or target-organ exposure, and a suitable non-ophthalmic formulation
- Preclinical or clinical evidence in the target condition
- Reconciliation of the obsolete neurogenic bladder term with current terminology
- Verification of the marketing authorisation record, including approved indication and dosage form
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

