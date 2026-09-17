---
layout: default
title: Praziquantel
parent: Model Prediction Only (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Praziquantel
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

# Praziquantel: From Parasitic Worm Infections to Uterine Corpus Epithelioid Leiomyosarcoma

## One-Sentence Summary

> Praziquantel is an anthelmintic, internationally used to treat trematode and cestode infections (e.g. schistosomiasis, tapeworm infections).
> The TxGNN model's top-ranked prediction is **Uterine Corpus Epithelioid Leiomyosarcoma**,
> but this is currently supported by **no clinical trials and no literature** — the evidence pack itself flags it as a likely knowledge-graph artefact with no known pharmacological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally available (no UK licence on record); internationally indicated for trematode/cestode (fluke/tapeworm) infections |
| Predicted New Indication | Uterine Corpus Epithelioid Leiomyosarcoma |
| TxGNN Prediction Score | 97.28% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a blocking data gap). Based on the information available in this evidence pack, Praziquantel's known pharmacological action is on the tegument (body wall) of flatworms (trematodes and cestodes), increasing calcium ion permeability to cause paralysis and death of the parasite. This mechanism has no established relationship to mammalian smooth-muscle tumour biology.

The evidence pack's own repurposing rationale for this candidate is explicit that **no plausible mechanistic link exists**: leiomyosarcoma pathogenesis is driven by pathways such as MED12, TP53 and RB1 dysregulation, which have no known overlap with the calcium-channel-mediated action of Praziquantel on parasite tegument. This candidate is assessed as arising from an indirect knowledge-graph connection rather than genuine pharmacological signal.

Consequently, this prediction does not currently have a credible biological rationale, and should not be interpreted as supporting a genuine repurposing opportunity without independent mechanistic or experimental validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Praziquantel currently holds **no UK marketing authorisation** (MHRA) and is not marketed in the UK (0 licences on record). No product-specific dosage form or licensed indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** A blocking data gap exists — UK-specific SmPC warnings and contraindications for Praziquantel have not yet been retrieved, which prevents this candidate from formally entering safety pre-assessment (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trial or literature support (L5, model prediction only), and the evidence pack itself identifies no plausible pharmacological mechanism linking Praziquantel's antiparasitic action to leiomyosarcoma. A blocking data gap in SmPC warnings/contraindications also prevents formal safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/MHRA SmPC labelling data (warnings, contraindications) — currently blocking
- Formal DrugBank mechanism-of-action confirmation
- Independent mechanistic or preclinical evidence linking Praziquantel to leiomyosarcoma before further evaluation

---

### Other Candidates Screened (for transparency)

This evidence pack evaluated 10 predicted indications for Praziquantel; all but one were assessed as **Hold** due to absent evidence and/or implausible mechanism (including *Plasmodium falciparum* malaria, retroperitoneal sarcoma, and other sarcoma subtypes — several explicitly noted as likely confounded or spurious signals). The only candidate reaching decision-stage S1 was **gnathomiasis** (rank 7, TxGNN score 96.47%, evidence level L4), supported by one case report of Praziquantel-associated worm expulsion — flagged for further research, not clinical use, given uncertainty over whether the effect reflects therapeutic efficacy or a worm evasion response.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

