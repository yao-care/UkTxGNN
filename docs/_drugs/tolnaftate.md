---
layout: default
title: Tolnaftate
parent: Model Prediction Only (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
---

# Tolnaftate
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

# Tolnaftate: From Superficial Fungal Infections to Ectothrix Infectious Disease

## One-Sentence Summary

Tolnaftate is a topical antifungal classically used to treat superficial fungal (dermatophyte) skin infections. The TxGNN model predicts it may also be effective for **ectothrix infectious disease** (dermatophyte infection of the hair shaft), with a prediction score of 98.59%, but **no clinical trials or published literature** currently support this specific indication — the link is mechanistic only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial fungal (dermatophyte) skin infections — noted in the evidence annotations as tolnaftate's classic, clinically established use; formal UK licence indication text is not currently on file |
| Predicted New Indication | Ectothrix Infectious Disease |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal mechanism-of-action record is not currently available for tolnaftate (flagged as a data gap in the source record). However, the evidence pack's own mechanistic annotations indicate that tolnaftate acts by inhibiting fungal squalene epoxidase, thereby blocking ergosterol biosynthesis in dermatophyte cell membranes — the accepted mode of action for this drug class.

Ectothrix infection is a pattern of hair-shaft invasion by dermatophyte fungi (typically seen in tinea capitis or tinea barbae), where fungal spores form a sheath around the outside of the hair shaft. This is mechanistically within the same fungal family that tolnaftate's established indication (superficial dermatophytosis) already targets, which is why the model assigns it a very high score.

That said, the evidence annotation for this specific prediction explicitly states there is "no direct clinical or literature evidence" supporting efficacy in ectothrix infection specifically. A further consideration is that topical agents such as tolnaftate typically have limited penetration into the hair follicle and shaft, which may limit efficacy against infections with a hair-invasion component even where the causative organism is susceptible in vitro. The prediction should therefore be treated as a plausible extrapolation from class mechanism rather than a validated indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Tolnaftate is currently **not marketed** in the UK, and no marketing authorisations are on file for this evidence pack. Formal UK licence and SmPC indication data are not yet available and are flagged as a blocking data gap (see Conclusion below).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high (98.59%), but this is driven by mechanistic plausibility alone — there are zero clinical trials and zero published studies specifically addressing tolnaftate in ectothrix infectious disease.
- The source evidence pack itself flags a data gap for both UK regulatory safety information (warnings/contraindications) and detailed mechanism-of-action data, both of which are prerequisites for any formal safety evaluation.
- For context, other candidates in the same evidence pack carry more supporting data (e.g. cutaneous candidiasis has literature but a mechanism-mismatch concern, since tolnaftate is not well established against *Candida*; the broader "skin disease caused by infection" category has systematic-review-level literature but is too heterogeneous to act on directly). None of these change the assessment for ectothrix infectious disease specifically.

**To proceed, the following is needed:**
- Resolution of the blocking data gap: UK/TFDA product labelling (warnings, contraindications) — required before any safety pre-screening (S1) can begin
- Resolution of the high-severity data gap: documented mechanism of action from DrugBank or equivalent source
- Targeted clinical or in vitro evidence on tolnaftate's efficacy and follicular penetration specifically against ectothrix-pattern dermatophyte infection
- Confirmation of UK marketing status, since the drug currently has no active licence on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

