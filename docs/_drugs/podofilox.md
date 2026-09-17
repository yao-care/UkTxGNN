---
layout: default
title: Podofilox
parent: Model Prediction Only (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Podofilox
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

# Podofilox: From Genital Warts to Vulvovaginal Candidiasis

## One-Sentence Summary

Podofilox (podophyllotoxin) is an antimitotic topical agent whose established clinical use — confirmed by the literature within this evidence pack — is the treatment of anogenital (genital) warts. The TxGNN model's top-ranked prediction for this drug is **Vulvovaginal Candidiasis**, but this is supported by only **1 non-specific publication** and **no clinical trials**, and the model's own mechanistic review flags the prediction as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in `taiwan_regulatory.licenses` (drug not marketed); literature within this evidence pack documents established use for anogenital/genital warts (e.g. PMID 8192173, 9449907) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 (model prediction only, no supportive studies) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for podofilox is not available in this evidence pack (MOA: Data Gap). Based on the literature captured here, podofilox is a podophyllotoxin derivative with an antimitotic, cytotoxic mechanism, used topically to destroy wart tissue caused by human papillomavirus (HPV) infection — its proven original use is anogenital warts, not an antifungal or anti-infective indication.

Vulvovaginal candidiasis, by contrast, is a fungal infection requiring antifungal activity (e.g. azole or polyene agents) to clear *Candida* organisms. The evidence pack's own mechanistic review is explicit on this point: **podofilox has no antifungal activity and no established mechanistic relationship to candidiasis treatment.** The single supporting reference (PMID 10537386) is a 1999 general review of sexually transmitted infection treatment guidelines that discusses vaginal discharge and genital warts as separate topics — it does not specifically link podofilox to candidiasis therapy.

Taken together, this appears to be a high-confidence TxGNN embedding-space association (both diseases occur in the genital tract, and podofilox is heavily associated with genital pathology in the knowledge graph) rather than a mechanistically grounded repurposing signal. This pattern — high similarity score, absent direct mechanistic support — is consistent with the L5/Hold classification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Review | American Family Physician | General CDC-guideline review of STD/vaginal infection treatment; does not specifically address podofilox for vulvovaginal candidiasis |

---

## UK Market Information

Podofilox is currently not marketed in the UK, and no marketing authorisations are recorded in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score (99.47%), the evidence base for this prediction is minimal (L5) and the model's own mechanistic rationale explicitly contradicts biological plausibility — podofilox is an antimitotic cytotoxic agent with no antifungal activity, and its sole supporting reference does not address this indication. This candidate should not proceed without substantial new evidence.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or SmPC
- MHRA/SmPC warnings, contraindications and DDI data (currently all Data Gap)
- Preclinical or in vitro evidence of any antifungal or anti-*Candida* activity, given none currently exists
- Note: the co-occurring predicted indication "Human Papilloma Virus Infection" (rank 3 in this evidence pack) is far better supported by existing literature and clinical trial data and may warrant separate, prioritised evaluation instead of this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

