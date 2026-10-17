---
layout: default
title: Meclizine
parent: Model Prediction Only (L5)
nav_order: 387
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Meclizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Central nervous system origin vertigo"
monitor_inn: "meclizine"
predicted_indications: ["allergic urticaria", "common cold", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "cold urticaria"]
---

# Meclizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Meclizine: From Vertigo and Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Meclizine is a first-generation antihistamine, originally used for vertigo of central nervous system origin and motion sickness.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but there are currently **no registered clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Central nervous system origin vertigo; motion sickness (per the TxGNN knowledge graph; no approved indication text is available for the UK authorisations) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for meclizine is not available in the data compiled for this report. Based on known pharmacology, meclizine is a first-generation antihistamine with H1 receptor antagonist activity. Its established uses (vertigo and motion sickness) are thought to reflect its effects on the vestibular system and central nervous system.

Allergic urticaria is a histamine-mediated condition, so H1 receptor blockade offers a plausible mechanistic link. However, this is a computational prediction only. Established H1 antihistamines are already standard treatment for urticaria, so any added value of meclizine would have to be shown, for example by comparison with non-sedating antihistamines. Sedation and anticholinergic effects are also drawbacks.

Other predicted indications are listed below. All are supported by model prediction only, with no trials or publications:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Common cold | 99.49% | L5 | Possible symptom relief of rhinorrhoea and sneezing only; no disease modification |
| 3 | Nasal cavity disease | 99.48% | L5 | Broad category with no specific disease defined, which limits assessment |
| 4 | Pharyngitis | 99.45% | L5 | Any benefit would be indirect (for example, reduced postnasal drip) |
| 5 | Acute laryngopharyngitis | 99.37% | L5 | Weak rationale; anticholinergic drying could worsen throat irritation |
| 6 | Cold urticaria | 99.22% | L5 | Plausible link, as H1 antihistamines are first-line, but newer non-sedating agents are preferred |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000N0AAAAAA | Meclozine HCl Tab 12.5mg | Tablet | Indication text not available |
| 0406000N0BBAAAA | Sea-Legs Tab 12.5mg | Tablet | Indication text not available |
| 0406000N0BDAAAC | Traveleeze Pastil | Pastille | Indication text not available |

The identifiers above are as recorded in the data compiled for this report and are not in the standard MHRA "PL XXXXX/XXXX" format. They should be verified against the MHRA register. Dosage forms are inferred from product names because the dosage form field was empty. In the BNF, antihistamines for nausea and vertigo are classified under the nausea and vertigo section of the gastrointestinal chapter. No NICE appraisal data were available.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** benign prostatic hyperplasia, angle-closure glaucoma, pyloric stenosis, and bladder neck obstruction. These are consistent with the anticholinergic activity of meclizine.
- **Drug Interactions:** 252 potential interactions were identified. The two **Major** interactions shown are with **potassium citrate** and **potassium chloride**. Many **Moderate** interactions involve other anticholinergic or antimuscarinic agents (hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium, clidinium, mepenzolate, methscopolamine), as well as opioids (morphine, opium, loperamide), metoclopramide, nabilone, eliglustat, eluxadoline, and glycerol phenylbutyrate. Additive sedation and anticholinergic effects are the main concern.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score (99.67%) with no clinical trials or publications (evidence level L5). Established, better-tolerated antihistamines already exist for urticaria, and meclizine's sedative and anticholinergic profile is a disadvantage.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- Product label warnings and contraindications from the SmPC and BNF
- Approved indication text and dosage forms for the UK authorisations, and verification of the authorisation numbers
- A literature review and trial search for meclizine in urticaria
- Evidence of benefit over non-sedating H1 antihistamines
- A safety assessment covering sedation, anticholinergic burden, and the listed interactions and at-risk conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

