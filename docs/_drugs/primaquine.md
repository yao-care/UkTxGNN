---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 480
evidence_level: L5
indication_count: 8
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

Using the evidence pack as given (Primaquine, DB01087), here is the report.

---

# Primaquine: From Antimalarial Therapy to Myiasis

## One-Sentence Summary

> Primaquine is an 8-aminoquinoline with an established, decades-long history as an antimalarial/antiprotozoal agent (used for radical cure of *P. vivax*/*P. ovale* and as a gametocytocide against *P. falciparum*), though formal original-indication licence data is not recorded in this evidence pack. The TxGNN model's top-ranked prediction is **Myiasis**, with a prediction score of **99.76%**, but **no clinical trials and no literature** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally recorded in this evidence pack (no MHRA licence data available); narrative evidence in the pack points to established antimalarial/antiprotozoal use |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for primaquine is not available in this evidence pack (data gap). However, the rationale text accompanying this prediction indicates that primaquine's known pharmacology is an antimalarial/antiprotozoal oxidative mechanism — active against protozoal parasites such as *Plasmodium* species and, per other candidates in this pack, *Toxoplasma gondii* and *Pneumocystis jirovecii*.

Myiasis, by contrast, is a parasitic skin/wound infestation caused by dipteran (fly) larvae — an entirely different phylum of organism to the protozoa primaquine is known to act against. There is no plausible biological link between primaquine's oxidative antiprotozoal mechanism and larvicidal activity against fly larvae. The evidence pack's own assessment concludes this prediction most likely reflects a knowledge-graph embedding artefact rather than a genuine pharmacological relationship, and the same conclusion is drawn for the closely related candidates *wound myiasis*, *creeping myiasis*, *furuncular myiasis*, and *nocardiosis* — all scoring similarly highly (>99%) with zero supporting trials or literature.

**Note on other candidates in this pack:** This evidence pack evaluated eight indications for primaquine in total. Two lower-ranked candidates are worth flagging for transparency: *malaria* (rank 7) is supported by dozens of completed Phase 2–4 trials and extensive literature — consistent with primaquine's known real-world antimalarial use — and *pneumocystosis* (rank 8) has decades-old trial evidence for clindamycin-primaquine combination therapy. Neither has yet been scored for evidence level/decision stage in this pack. *Toxoplasmosis* (rank 5) reaches evidence level L4 based on review-level literature only, with no dedicated trials. None of these change the assessment of myiasis itself, which remains the top-ranked but least biologically plausible prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisation is currently recorded for primaquine in this evidence pack. Market status is listed as **Not marketed**, with **0** licences on file.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (myiasis) has evidence level L5 — a model prediction with no supporting clinical trials or literature — and no plausible mechanistic link to primaquine's known antiprotozoal pharmacology. It should not proceed further as currently framed.

**To proceed, the following is needed:**
- MHRA/SmPC warnings and contraindications data (currently blocking — flagged as DG001)
- Confirmed mechanism of action data from DrugBank (flagged as DG002, High severity)
- Formal documentation of primaquine's original licensed indication(s), currently absent from this pack
- If research resources are to be allocated to primaquine repurposing at all, the lower-ranked but evidence-supported candidates in this pack (e.g. toxoplasmosis, L4) warrant consideration ahead of myiasis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

