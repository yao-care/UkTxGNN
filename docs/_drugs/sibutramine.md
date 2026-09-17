---
layout: default
title: Sibutramine
parent: Model Prediction Only (L5)
nav_order: 530
evidence_level: L5
indication_count: 4
---

# Sibutramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Sibutramine: From Obesity (Appetite Suppression) to Hypervitaminosis

## One-Sentence Summary

> Sibutramine is historically associated with appetite suppression as a selective serotonin-noradrenaline reuptake inhibitor, though the original indication and detailed mechanism of action are not documented in the current evidence pack. The TxGNN model's top prediction flags **Hypervitaminosis** as a candidate new indication, but this is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic analysis found no identifiable biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (historically an appetite suppressant; see data gaps) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sibutramine (flagged as a blocking data gap in this pack). Based on known information, sibutramine is a selective serotonin–noradrenaline reuptake inhibitor historically used as an appetite suppressant, but the specific original indication text and confirmed MOA could not be extracted from the current data sources.

Critically, the model's own generated rationale for this prediction explicitly states that **no identifiable mechanistic link** exists between sibutramine's known pharmacology (appetite/serotonergic-noradrenergic modulation) and hypervitaminosis (a condition of excess vitamin accumulation). The high TxGNN score is assessed as likely reflecting node proximity noise within the knowledge graph rather than genuine biological plausibility.

This pattern repeats across all four top-ranked predictions in this evidence pack (hypervitaminosis, proximal 16p11.2 microdeletion syndrome, obsolete hypertelorism, and frontorhiny) — each carries a similarly high TxGNN score but the accompanying rationale independently concludes there is no mechanistic or clinical basis for the association, with two of the four even flagged as rare genetic syndromes or obsolete ontology terms rather than treatable conditions. This consistent lack of biological plausibility across the full ranked set is a strong signal that these results should not be acted upon without substantial further validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Sibutramine currently holds no UK marketing authorisations (0 licenses on record); market status is recorded as **Not Marketed**. No product, dosage form, or approved indication data is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Warnings, contraindications, and drug interaction data for sibutramine are currently unavailable in this evidence pack and are flagged as a blocking data gap (DG001) requiring MHRA/SmPC source review before any safety assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trial or literature evidence supports any of the top four predicted indications, all evidence is model-prediction-only (L5), and the model's own mechanistic rationale finds no plausible biological link for the top-ranked candidate. Combined with a blocking data gap on safety warnings/contraindications and the drug's "Not Marketed" UK status, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- MHRA/SmPC warnings and contraindications for sibutramine (blocking gap, DG001)
- Confirmed mechanism of action from DrugBank or equivalent source (DG002)
- Documented original indication history, including verification of past regulatory status (e.g., any historical withdrawal or restriction)
- Independent mechanistic or preclinical evidence connecting sibutramine's pharmacology to hypervitaminosis before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

