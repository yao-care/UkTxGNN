---
layout: default
title: Prasterone
parent: Model Prediction Only (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From No Established UK Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Prasterone (DHEA) currently holds no UK marketing authorisation, and this evidence pack does not document an established original indication. The TxGNN model's top-ranked prediction — **heparin cofactor 2 deficiency** — is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags this high score as likely knowledge-graph noise rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented (no UK marketing licences on file) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Prasterone in this evidence pack. Based on general pharmacological knowledge, Prasterone (dehydroepiandrosterone, DHEA) is a weak endogenous androgen precursor; however, no original indication or UK licence history is on file to establish a baseline for comparison.

For the top-ranked prediction, the model's own rationale is explicit about its weakness: DHEA has no known direct biochemical relationship with the SERPIND1-mediated coagulation-regulation pathway underlying heparin cofactor 2 deficiency. The high TxGNN score is more plausibly explained by co-occurrence noise between steroid-hormone and coagulation-related genes within the knowledge graph than by any real mechanistic link. This is corroborated by the complete absence of supporting clinical trials or literature.

It is also worth noting that among the remaining nine ranked predictions in this pack, none reach a stronger evidence tier for a *therapeutic* signal at heparin cofactor 2 deficiency specifically. One related candidate — systemic sclerosis (rank 7) — has a more defensible observational basis (consistently low serum DHEA-S in patients with more severe disease), but this concerns a different indication entirely and remains hypothesis-generating only (see Conclusion). Separately, the thrombophilia-related candidates (ranks 4 and 6) are flagged in the source rationale as potential **safety signals in the opposite direction** — androgen/DHEA states have been associated with *increased* thrombotic risk in the literature, which argues against, rather than for, repurposing toward coagulation-deficiency indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Prasterone is **not currently marketed** in the UK. No MHRA marketing authorisations are recorded in this evidence pack (total licences: 0), so no product/dosage-form table can be produced.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this evidence pack flags TFDA-equivalent warnings/contraindications (DG001) as a **Blocking** data gap — this must be resolved before any formal safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (heparin cofactor 2 deficiency) has no clinical trial or literature support and is explicitly characterised in the model rationale as a probable knowledge-graph artefact rather than a genuine mechanistic signal. Combined with the absence of any UK marketing authorisation and missing core MOA/safety data, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Resolution of the Blocking data gap (DG001): sourcing of licensing-body/SmPC warnings and contraindications
- Resolution of the High-severity data gap (DG002): verified mechanism-of-action data from DrugBank or equivalent
- Independent mechanistic or preclinical evidence directly linking DHEA to SERPIND1/heparin cofactor 2 pathway biology, since none currently exists
- If pursuit is desired, consider redirecting evaluation toward the more biologically grounded systemic sclerosis signal (rank 7, L4/S1, "Research Question"), which is supported by six observational cohort studies linking low DHEA-S to disease severity — though this would require a dedicated proof-of-concept interventional study, as no trial of prasterone supplementation in SSc currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

