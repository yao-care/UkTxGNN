---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 593
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

> Travoprost is a prostaglandin F2α (FP) receptor agonist originally used to lower intraocular pressure in open-angle glaucoma and ocular hypertension.
> The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**,
> but currently there are **no clinical trials** and **no published literature** supporting this direction, and no mechanistic rationale has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension (inferred from clinical evidence in this pack; formal indication text not available) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for travoprost is not available in this evidence pack. Based on information found elsewhere within the pack (clinical trial descriptions and rationale notes for other candidate indications), travoprost is a prostaglandin F2α analogue that acts as an FP receptor agonist, lowering intraocular pressure primarily by increasing uveoscleral outflow. Its approved use is in the topical treatment of glaucoma and ocular hypertension.

Calciphylaxis (calcific uraemic arteriolopathy) is a systemic disorder of small-vessel vascular calcification, typically associated with end-stage renal disease and abnormal calcium/phosphate metabolism. There is no known pharmacological link between FP-receptor-mediated ocular hypotensive activity and the pathways driving vascular calcification.

The evidence pack's own rationale for this candidate explicitly states that no clinical trial or literature evidence exists, and that the prediction reflects only a TxGNN knowledge-graph embedding score rather than a validated mechanistic or clinical signal. This prediction should therefore be treated as hypothesis-generating only, not as a basis for clinical or regulatory action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Travoprost currently holds **no marketing authorisations** recorded in this evidence pack (market status: Not marketed; total licences: 0). No product-level UK/MHRA licence data is available for review at this time.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Structured MHRA/TFDA label warnings and contraindications data are currently unavailable (flagged as a Blocking data gap — DG001), and a formal mechanism-of-action reference (DG002) has not yet been retrieved. Both should be resolved before any safety-relevant decision is made.*

---

## Other Predicted Indications (Context)

For context, this evidence pack also scored nine additional candidate indications for travoprost (ranks 2–10), all with similarly high TxGNN scores (>99.9996%) but overwhelmingly weak supporting evidence:

- **Vascular disease** (rank 5, L4) — the only candidate with substantial clinical trial/literature volume, but all identified studies concern ophthalmic IOP-lowering or ocular tolerability outcomes, not systemic vascular disease. The evidence pack's own rationale suggests this may be a knowledge-graph ontology mismatch (glaucoma-related vascular nodes linked to broad "vascular disease" nodes) rather than a genuine repurposing signal.
- **Hemangioendothelioma** (rank 10, L4) — supported only by two case-report/review articles describing an **adverse event** (uveal effusion in a Sturge-Weber-Krabbe syndrome patient on topical travoprost), which is a safety signal, not efficacy evidence.
- All remaining candidates (visceral calciphylaxis, thoracic outlet syndrome subtypes, angiodysplasia of stomach, blue toe syndrome, lymphangiectasis, spontaneous coronary artery dissection) have **no supporting clinical trial or literature evidence** (L5) and, per the pack's own rationale notes, no plausible mechanistic link to travoprost's known pharmacology. Spontaneous coronary artery dissection is additionally flagged as clinically contraindicated for use of unvalidated vasoactive agents.

None of these candidates currently meet the threshold for further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (visceral calciphylaxis) has no clinical trial or literature support and no identified mechanistic rationale — it is a model-only (L5) signal. Travoprost is also not currently marketed in the UK, and core regulatory/safety data (label warnings, contraindications, MOA) are marked as data gaps in this evidence pack.

**To proceed, the following is needed:**
- Formal mechanism-of-action confirmation (DrugBank/SmPC) — currently a High-severity data gap
- MHRA/TFDA label warnings and contraindications data — currently a Blocking-severity data gap
- Preclinical or mechanistic studies linking FP-receptor agonism to vascular/soft-tissue calcification pathways
- If pursuing the "vascular disease" (rank 5) candidate instead, clarification of whether the KG signal reflects a genuine systemic vascular effect or an ontology labelling artefact from glaucoma-related trial data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

