---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 8
---

# Phenol
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

Using the evidence pack for Phenol (DB03255). Note: TxGNN's rank-1 prediction ("acrodermatitis chronica atrophicans", score 99.95%) has **zero supporting evidence** and is explicitly flagged in the pack itself as a high-score/no-evidence artefact — as are ranks 2, 3, 4, 6, 7 and 8 (several are drug-name false-positives, e.g. dry eye trials actually testing hydroxychloroquine, AL-38583, omega-3, not phenol). The only candidate with any real evidentiary basis is rank 5, **acne keloidalis (L3)**. I have built this report around that candidate rather than the top TxGNN score, and flagged the other seven as unsupported below — reporting the raw top-ranked prediction as "the" prediction would be misleading for a clinical audience.

---

# Phenol: From Topical Antiseptic/Chemical Peel Agent to Acne Keloidalis

## One-Sentence Summary

> Phenol has no UK marketing authorisation and no formally recorded original indication; it is historically used as a topical antiseptic and keratolytic (chemical peel) agent.
> Of eight indications proposed by the TxGNN model, only one — **Acne Keloidalis** (keloidal folliculitis) — is supported by any actual evidence,
> with **4 supporting publications** (no dedicated clinical trials) and an inferred mechanistic rationale from established chemical-peel dermatology literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on file (0 UK marketing authorisations); historically used as a topical antiseptic/keratolytic (chemical peel) agent |
| Predicted New Indication | Acne Keloidalis (keloidal folliculitis) |
| TxGNN Prediction Score | 99.94% (rank 1,029 of full model output) |
| Evidence Level | L3 (observational/case-series evidence only) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Phenol (flagged as a Blocking/High-severity data gap — see Conclusion). Based on known dermatological use, phenol is a classical deep chemical peeling and keratolytic agent, causing controlled superficial chemical destruction of the epidermis followed by re-epithelialisation. Modified low-toxicity phenol peel formulations have documented use for facial wrinkles, acne scarring and related hyperkeratotic/scar lesions in the dermatology literature (PMID 17204096).

Acne keloidalis (keloidal folliculitis) is a chronic scarring follicular disorder producing hyperkeratotic, keloid-like papules and nodules — mechanistically, the epidermal-remodelling action of chemical peeling is a plausible (if indirect) extension of phenol's known dermatological use. However, this link is inferred from general chemical-peel literature rather than from any study specifically designed to test phenol in acne keloidalis, so it remains a research hypothesis rather than an established indication.

The remaining seven TxGNN-predicted indications for this drug (acrodermatitis chronica atrophicans, childhood connective-tissue-disease-associated interstitial lung disease, neonatal dermatomyositis, amyopathic dermatomyositis, familial hydroa vacciniforme, severe non-proliferative diabetic retinopathy, and dry eye syndrome) have **no credible supporting evidence** — either no trials/literature at all, or trials/literature that on inspection test entirely different drugs (hydroxychloroquine, AL-38583, omega-3 fatty acids, berberine, aspirin, antimuscarinics). These are treated as TxGNN false positives and are not carried forward.

## Clinical Trial Evidence

Currently no related clinical trials registered for phenol in acne keloidalis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) | 2007 | Cohort/Case series | The Journal of Dermatology | Modified phenol peel (Exoderm) improved facial wrinkles, acne scars and related skin lesions in Asian patients with reduced side-effect profile |
| [16164153](https://pubmed.ncbi.nlm.nih.gov/16164153/) | 2005 | Review | Cutis | Reviews acne treatment in ethnic skin, including keloid scarring risk and peeling-based approaches |
| [866280](https://pubmed.ncbi.nlm.nih.gov/866280/) | 1977 | Review | Postgraduate Medicine | Discusses keloidal folliculitis and related dermatoses more common in black patients |
| [4278481](https://pubmed.ncbi.nlm.nih.gov/4278481/) | 1974 | Case report | Fortschritte der Medizin | Historical case report on scalp disease treatment (Crino-Kaban); limited direct relevance |

## UK Market Information

Phenol currently has no UK marketing authorisation on file (0 licenses; market status: Not marketed). No product-level dosage form or approved-indication data is available for this substance in the evidence pack.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: TFDA/UK label warnings and contraindications data are currently unavailable for this substance (data gap, Blocking severity) — this must be resolved before any safety assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No UK marketing authorisation exists for phenol, mechanism-of-action data is unavailable, and the only indication with any supporting evidence (acne keloidalis) rests on inferred mechanistic reasoning from general chemical-peel literature rather than a dedicated trial. The other seven TxGNN-predicted indications for this drug lack credible evidence entirely.

**To proceed, the following is needed:**
- Resolve the Blocking data gap on TFDA/SmPC warnings and contraindications (required before any S1 safety review)
- Obtain formal mechanism-of-action documentation from DrugBank or equivalent source
- A dedicated preclinical or clinical study testing phenol (not a substitute agent) specifically in acne keloidalis/keloidal folliculitis
- Re-screen the remaining seven predicted indications once genuine phenol-specific evidence (if any) becomes available; current signals for those are considered TxGNN artefacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

