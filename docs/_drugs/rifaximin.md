---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 6
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

Using no specific skill — this is a direct report-generation task fully specified by the system prompt template; I'll execute it directly against the given Evidence Pack.

# Rifaximin: From No UK-Licensed Indication to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a gut-selective, minimally absorbed rifamycin antibiotic; this evidence pack contains no confirmed original UK indication or marketing authorisation for the drug. The TxGNN model predicts potential relevance to **Oral Candidiasis**, but the only supporting literature (1 publication, no clinical trials) actually reports rifaximin as a **risk factor for** — not a treatment for — Candida infection, making this a signal that warrants caution rather than a supportive evidence base.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indication or marketing authorisation recorded in this evidence pack |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only; the one literature item found is directionally contradictory) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for rifaximin is not available in this evidence pack, and no confirmed original indication is on file (no UK marketing authorisation currently exists for this product). Based on general pharmacological knowledge captured in the repurposing rationale, rifaximin is a gut-selective rifamycin-class antibiotic with negligible systemic absorption (<0.4%), acting exclusively on bacterial RNA polymerase. It has **no antifungal activity**, so there is no direct mechanistic basis for efficacy against oral candidiasis, which is a fungal infection.

Critically, the single relevant publication identified does not support a therapeutic link — it reports the opposite association. A cohort/case-series study in allogeneic haematopoietic cell transplant recipients found that rifaximin use was **linked to an increased incidence of micafungin-resistant Candida species infections**, plausibly through disruption of gut/oral microbial flora and selection pressure favouring fungal overgrowth. This positions rifaximin as a potential **risk factor** for candidiasis rather than a candidate treatment, and the TxGNN prediction should be interpreted with this important caveat rather than as a positive repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort/Case series (risk factor study) | Annals of Hematology | Rifaximin use in allogeneic HSCT recipients was associated with **increased** micafungin-resistant Candida spp. infections — evidence of risk association, not therapeutic benefit |

## UK Market Information

Rifaximin currently holds **no marketing authorisation** on record in this evidence pack (0 licences; market status: not marketed). No product, dosage form, or approved indication details are available to list.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications, and drug interaction data for rifaximin are currently marked as blocking data gaps in this evidence pack and could not be evaluated.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 with no clinical trials, and the sole available publication points in the **opposite direction** to the prediction — associating rifaximin with increased, rather than reduced, Candida infection risk. Combined with the absence of a confirmed UK licence and blocking gaps in safety data, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- MHRA/SmPC-sourced warnings and contraindications (currently a blocking data gap)
- Verified mechanism of action from DrugBank
- Confirmation of rifaximin's original indication and any UK licensing status
- Direct clinical or mechanistic evidence supporting antifungal or anti-candidal benefit, given that current literature suggests a contrary risk association
- Reassessment if new trial or observational data specifically addressing oral candidiasis emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

