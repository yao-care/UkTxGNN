---
layout: default
title: Levobunolol
parent: Model Prediction Only (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Levobunolol
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

# Levobunolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Levobunolol is a topical non-selective beta-adrenoceptor blocker with long-established use in lowering intraocular pressure in open-angle glaucoma and ocular hypertension. The TxGNN model predicts it may also be effective for **Primary Hereditary Glaucoma**, but this specific indication currently has **no clinical trials and no published literature** directly supporting it in the evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in UK regulatory data; literature evidence in this pack indicates established use in open-angle glaucoma and ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this drug (flagged as a blocking data gap). Based on literature evidence retrieved for closely related indications in this pack, levobunolol is described as "a potent non-selective beta-adrenoceptor blocking agent used for the topical treatment of increased intraocular pressure in patients with chronic open angle glaucoma or ocular hypertension" (PMID 2892662), acting by reducing aqueous humour production in the ciliary body.

Primary hereditary glaucoma and open-angle glaucoma share substantial pathophysiological overlap: both are characterised by elevated intraocular pressure with a structurally open anterior chamber angle, and both are managed primarily by reducing aqueous humour production or increasing outflow. Because levobunolol's beta-blocking mechanism targets aqueous humour production rather than a specific anatomical or genetic cause, its efficacy in classic open-angle glaucoma provides plausible mechanistic grounds for extension to hereditary forms presenting with the same open-angle phenotype.

That said, "Primary Hereditary Glaucoma" itself returned no matched clinical trials or literature in the evidence pack, despite a very high TxGNN score. The closely related term "glaucoma 1, open angle" (rank 2, score 99.58%) and "open angle glaucoma" (rank 3, score 99.46%) are supported by over a dozen randomised controlled trials against timolol and other comparators spanning four decades, which lends indirect, but not direct, support to this specific prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

*Note: closely related predicted indications in this evidence pack (open-angle glaucoma variants) are supported by extensive RCT literature — see repurposing candidate ranks 2–3 in the source pack — but none were indexed specifically against "Primary Hereditary Glaucoma."*

## Literature Evidence

Currently no related literature available.

## UK Market Information

Levobunolol currently holds no marketing authorisation in the United Kingdom (market status: Not Marketed; 0 licences on record). No product-specific dosage form or approved indication text is available for this evidence pack.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: mechanism of action and TFDA/MHRA-equivalent warning and contraindication data are recorded as blocking gaps in this evidence pack and must be resolved before any safety evaluation can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Primary Hereditary Glaucoma) has no direct clinical trial or literature support, the drug has no current UK marketing authorisation, and mechanism of action plus safety/contraindication data are missing — together these fall short of the threshold needed to progress.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank API query)
- SmPC/product-label warnings and contraindications for levobunolol
- Targeted literature and trial search specifically for hereditary/congenital open-angle glaucoma populations (including paediatric use, given the hereditary phenotype often presents early in life)
- Assessment of UK marketing authorisation pathway, since the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

