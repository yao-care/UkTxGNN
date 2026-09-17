---
layout: default
title: Telithromycin
parent: Model Prediction Only (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Telithromycin
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

# Telithromycin: From Unspecified Original Indication to Hyperamylasemia

## One-Sentence Summary

Telithromycin is a ketolide-class antibacterial; this evidence pack does not record its licensed original indication, and the drug currently holds no UK marketing authorisation. TxGNN's top-ranked prediction links it to **Hyperamylasemia**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review found no plausible biological link — this is a model-only signal, not a clinical lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no UK licence on file) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for telithromycin is not available in this evidence pack (Data Gap DG002, High severity). Telithromycin is generally documented as a ketolide-class antibacterial, structurally related to macrolides, acting by inhibiting bacterial protein synthesis via the 50S ribosomal subunit. No original indication is recorded in this dataset, and the drug has no UK marketing authorisation, so its established therapeutic use cannot be confirmed from the data provided.

Importantly, the evidence pack's own mechanistic assessment for hyperamylasemia is explicit that **no known mechanistic link exists**: hyperamylasemia is typically associated with pancreatic or salivary gland pathology, which has no plausible connection to an antibacterial's mode of action. The evidence pack itself characterises this as a high-scoring TxGNN association without biological plausibility — consistent with a knowledge-graph artefact rather than a genuine pharmacological signal.

By comparison, a lower-ranked prediction in this pack (rank 6, "septicemic plague") at least carries a loose theoretical rationale — ketolide antibacterial activity against gram-negative organisms such as *Yersinia pestis* — supported by one review-level publication (on the related ketolide cethromycin, not telithromycin itself). Even this stronger candidate remains L4/S1 ("Research Question") and is not sufficient to justify progression on its own.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: literature evidence exists elsewhere in this evidence pack for a lower-ranked candidate (rank 6, "septicemic plague" — one review article, PMID 23463743, on the related ketolide cethromycin), but none is attached to the top-ranked prediction (hyperamylasemia) reported here.*

---

## UK Market Information

Telithromycin currently holds **no marketing authorisation in the United Kingdom** (0 licences on record). No UK product information (brand name, dosage form, or approved indication text) is available in this evidence pack.

---

## Safety Considerations

Formal SmPC-sourced warnings, contraindications, and drug interaction data are not available in this evidence pack (Data Gap DG001, **Blocking severity** — this alone precludes a formal S1 safety evaluation).

However, the evidence pack's own mechanistic rationale narratives (attached to other candidate indications in this pack, not to the top-ranked hyperamylasemia prediction) flag several known safety signals for telithromycin that should inform any future assessment:

- **Hepatotoxicity**: noted as a reason telithromycin's use has been severely restricted in other markets.
- **Neuromuscular risk**: a boxed warning for exacerbation of myasthenia gravis is referenced.
- **Visual disturbances**: diplopia and accommodation difficulties are noted as known adverse effects.

These are flagged in the evidence pack as reasons for caution, not as supporting evidence for any new indication. Full SmPC/BNF data should be obtained before further evaluation, and any suspected adverse reactions should be reported via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hyperamylasemia) is evidence level L5 — a model prediction with no supporting clinical trials or literature — and the evidence pack's own review found no biological plausibility for the association. Telithromycin is not marketed in the UK, and critical drug-level safety data (SmPC warnings and contraindications) remain a Blocking data gap, which alone prevents progression to a formal safety evaluation (S1).

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain the SmPC/product label warnings and contraindications for telithromycin from an authoritative source (e.g. MHRA/EMA), given its known hepatotoxicity-related restrictions in other markets.
- Resolve High-severity data gap DG002: obtain confirmed mechanism of action data via DrugBank.
- Confirm telithromycin's licensed original indication(s) from an authoritative regulatory source, since none is recorded in this evidence pack.
- If any candidate is pursued further, reconsider the lower-ranked but mechanistically closer candidate (rank 6, "septicemic plague", L4/S1 "Research Question") rather than the top-ranked but mechanistically implausible hyperamylasemia signal.
- Given telithromycin's known hepatotoxicity and myasthenia gravis boxed-warning history, any future development would require a full risk-benefit and pharmacovigilance review before proceeding.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

